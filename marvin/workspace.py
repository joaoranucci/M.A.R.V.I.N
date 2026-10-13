"""Bounded project files, atomic updates and verifiable development checks.

Only files below the configured workspace are exposed. Project code is data
until an explicit execution approval is given; static checks never import it.
"""
from __future__ import annotations

import ast
from datetime import datetime, timezone
import hashlib
from html.parser import HTMLParser
import io
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
import tempfile
import threading
import tokenize
import unicodedata
from urllib.parse import unquote, urlsplit

_INVALID = re.compile(r'[<>:"/\\|?*\x00-\x1f]')
_RESERVED = {"CON", "PRN", "AUX", "NUL", "CONIN$", "CONOUT$", *(f"COM{i}" for i in range(1, 10)), *(f"LPT{i}" for i in range(1, 10))}
_PRIVATE = {".marvin_versions", ".git", ".ssh", ".aws", ".gnupg"}
_SKIP = _PRIVATE | {"node_modules", ".venv", "venv", "__pycache__"}


def slug(name: str) -> str:
    value = unicodedata.normalize("NFKD", str(name)).encode("ascii", "ignore").decode("ascii").lower()
    value = re.sub(r"[^a-z0-9_-]+", "-", value).strip("-_")[:64]
    if not value or value.upper() in _RESERVED:
        raise ValueError("Nome de projeto inválido.")
    return value


def _secret_name(name: str) -> bool:
    low = name.casefold()
    return ((low == ".env" or low.startswith(".env.")) and low not in {".env.example", ".env.sample", ".env.template"}) or low in {"credentials.json", "id_rsa", "id_ed25519"} or low.endswith((".pem", ".key", ".p12", ".pfx"))


def _relative_file(path: str) -> Path:
    """Reject Windows aliases/traversal on every supported operating system."""
    p = str(path).replace("\\", "/")
    if not p or len(p) > 250 or p.startswith("/") or ":" in p:
        raise ValueError("Use um caminho relativo dentro do projeto.")
    parts = p.split("/")
    if any(x.casefold() in _PRIVATE or _secret_name(x) for x in parts):
        raise PermissionError("Backups, credenciais e pastas privadas não são acessíveis ao agente.")
    if len(parts) > 10 or any(not x or x in {".", ".."} or _INVALID.search(x) or x.endswith((".", " "))
                            or unicodedata.normalize("NFKC", x.split(".")[0]).upper() in _RESERVED for x in parts):
        raise ValueError("Nome de arquivo inválido ou caminho fora do projeto.")
    return Path(*parts)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def checked_path(root: Path, relative: Path) -> Path:
    """Reject symlinks, hardlinked files and Windows junction/reparse points.

    The configured root is trusted and resolved at construction. Descendants
    may not alias a different resource, even another path inside that root.
    """
    root = Path(root)
    relative = Path(relative)
    if relative.is_absolute() or any(part in {"", ".", ".."} for part in relative.parts):
        raise PermissionError("Caminho fora da pasta autorizada.")
    target = root
    for part in relative.parts:
        target = target / part
        try:
            info = target.lstat()
        except FileNotFoundError:
            continue
        if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & 0x400:
            raise PermissionError("Links simbólicos e junctions não são permitidos neste caminho.")
        if stat.S_ISREG(info.st_mode) and info.st_nlink > 1:
            raise PermissionError("Arquivo com múltiplos links não é permitido.")
    if not target.resolve().is_relative_to(root):
        raise PermissionError("Caminho fora da pasta autorizada.")
    return target


def atomic_write(target: Path, data: bytes, *, replace: bool = True) -> None:
    """Publish complete bytes from a same-directory temporary file.

    Exclusive publication prevents a new-file race from silently replacing an
    existing file. The temporary link is always removed afterwards.
    """
    descriptor, name = tempfile.mkstemp(prefix=".marvin-", suffix=".tmp", dir=target.parent)
    temporary = Path(name)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        if replace:
            os.replace(temporary, target)
        else:
            os.link(temporary, target)
    finally:
        temporary.unlink(missing_ok=True)


class _HTMLReferences(HTMLParser):
    def __init__(self):
        super().__init__()
        self.references: list[str] = []
        self.base_href = False

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == "base" and values.get("href"):
            self.base_href = True
        key = "href" if tag == "link" else "src" if tag in {"script", "img", "iframe", "source", "audio", "video"} else None
        if key and values.get(key):
            self.references.append(values[key])


class ProjectWorkspace:
    def __init__(self, root: Path | None = None):
        self.root = (Path(root) if root else Path(os.getenv("MARVIN_WORKSPACE_DIR") or Path.home() / "MARVIN_Projetos")).resolve()
        self.root.mkdir(parents=True, exist_ok=True)
        self._lock = threading.RLock()

    def project_path(self, project: str, relative: str | None = None) -> Path:
        name = slug(project)
        base = checked_path(self.root, Path(name))
        return checked_path(self.root, Path(name) / _relative_file(relative)) if relative is not None else base

    def create_project(self, name: str) -> dict:
        with self._lock:
            path = self.project_path(name)
            existed = path.is_dir()
            path.mkdir(parents=True, exist_ok=True)
            self.project_path(name)
            return {"ok": True, "status": "unchanged" if existed else "succeeded", "project": path.name,
                    "directory": str(path), "evidence": {"exists": path.is_dir()}, "changed_resources": [] if existed else [str(path)]}

    def write_project_file(self, project: str, path: str, content: str, overwrite: bool = False,
                           approve_overwrite=None, expected_sha256: str | None = None) -> dict:
        if not isinstance(content, str) or len(content.encode("utf-8")) > 160_000:
            raise ValueError("Arquivo grande demais (limite 160 KB). Divida o projeto em arquivos menores.")
        data = content.encode("utf-8")
        with self._lock:
            target = self.project_path(project, path)
            base = self.project_path(project)
            if not base.is_dir():
                raise FileNotFoundError("Crie o projeto antes de escrever arquivos.")
            if target.is_dir():
                raise ValueError("Esse caminho é uma pasta.")
            if target.exists() and target.stat().st_size > 160_000:
                raise ValueError("Arquivo existente excede 160 KB; requer edição manual ou ferramenta dedicada.")
            before = target.read_bytes() if target.exists() else None
            if expected_sha256 is not None and (before is None or sha256(before) != expected_sha256):
                raise RuntimeError("Conflito: o arquivo mudou desde a leitura. Leia a versão atual antes de editar.")
            backup = None
            if before is not None:
                if not overwrite:
                    raise FileExistsError("O arquivo já existe. Para alterar, use overwrite=true e obtenha confirmação.")
                if before == data:
                    return {"ok": True, "status": "unchanged", "file": str(target), "sha256": sha256(before), "bytes": len(before), "changed_resources": []}
                if approve_overwrite is None or not approve_overwrite(target):
                    raise PermissionError("Substituição de arquivo cancelada.")
                target = self.project_path(project, path)
                if not target.exists() or target.read_bytes() != before:
                    raise RuntimeError("Conflito: o arquivo mudou durante a aprovação. Nenhuma alteração foi aplicada.")
                stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S_%f")
                relative_backup = Path(base.name) / ".marvin_versions" / stamp / target.relative_to(base)
                backup = checked_path(self.root, relative_backup)
                backup.parent.mkdir(parents=True, exist_ok=True)
                checked_path(self.root, relative_backup)
                atomic_write(backup, before, replace=False)
            target.parent.mkdir(parents=True, exist_ok=True)
            target = self.project_path(project, path)
            if before is not None and (not target.is_file() or target.read_bytes() != before):
                raise RuntimeError("Conflito: arquivo alterado antes da gravação.")
            atomic_write(target, data, replace=before is not None)
            actual = self.project_path(project, path).read_bytes()
            if actual != data:
                raise RuntimeError("O conteúdo gravado não corresponde ao esperado; confira o backup.")
            result = {"ok": True, "status": "succeeded", "file": str(target), "bytes": len(data),
                      "sha256": sha256(actual), "evidence": {"sha256": sha256(actual), "exists": True}, "changed_resources": [str(target)]}
            if backup:
                result["backup"] = str(backup)
            return result

    def read_project_file(self, project: str, path: str) -> dict:
        target = self.project_path(project, path)
        if not target.is_file():
            raise FileNotFoundError("Arquivo não encontrado.")
        if target.stat().st_size > 40_000:
            raise ValueError("Leitura limitada a 40 KB; escolha um arquivo menor.")
        content = target.read_bytes()
        if len(content) > 40_000:
            raise ValueError("O arquivo cresceu durante a leitura; limite de 40 KB.")
        return {"ok": True, "file": str(target), "content": content.decode("utf-8"), "sha256": sha256(content)}

    def patch_project_file(self, project: str, path: str, old: str, new: str,
                           expected_sha256: str, approve_overwrite=None) -> dict:
        if not old or not isinstance(new, str):
            raise ValueError("Informe o trecho original não vazio e sua substituição.")
        current = self.read_project_file(project, path)
        if current["sha256"] != expected_sha256:
            raise RuntimeError("Conflito: o arquivo mudou desde a leitura.")
        if current["content"].count(old) != 1:
            raise ValueError("O trecho precisa aparecer exatamente uma vez. Leia o arquivo e detalhe a alteração.")
        return self.write_project_file(project, path, current["content"].replace(old, new, 1), True,
                                       approve_overwrite, expected_sha256)

    def list_projects(self) -> dict:
        projects = []
        for item in sorted(self.root.iterdir()):
            try:
                if item.name == slug(item.name) and checked_path(self.root, Path(item.name)).is_dir():
                    projects.append({"project": item.name, "directory": str(item)})
            except (ValueError, PermissionError, OSError):
                continue
            if len(projects) == 100:
                break
        return {"ok": True, "projects": projects}

    def _files(self, project: str, limit: int = 1000):
        folder = self.project_path(project)
        if not folder.is_dir():
            raise FileNotFoundError("Projeto não encontrado.")
        count = 0
        for directory, dirs, names in os.walk(folder, followlinks=False):
            allowed = []
            for name in sorted(dirs):
                if name.casefold() in _SKIP or _secret_name(name):
                    continue
                try:
                    self.project_path(project, (Path(directory) / name).relative_to(folder).as_posix())
                except (ValueError, PermissionError, OSError):
                    continue
                allowed.append(name)
            dirs[:] = allowed
            for name in sorted(names):
                try:
                    target = self.project_path(project, (Path(directory) / name).relative_to(folder).as_posix())
                except (ValueError, PermissionError, OSError):
                    continue
                if target.is_file():
                    yield target
                    count += 1
                    if count >= limit:
                        return

    def list_project_files(self, project: str) -> dict:
        folder = self.project_path(project)
        files = [p.relative_to(folder).as_posix() for p in self._files(project, 101)]
        return {"ok": True, "project": folder.name, "directory": str(folder), "files": files[:100], "truncated": len(files) > 100}

    def search_project_files(self, project: str, query: str) -> dict:
        if not isinstance(query, str) or not 1 <= len(query) <= 200:
            raise ValueError("Busca deve conter de 1 a 200 caracteres.")
        folder = self.project_path(project)
        matches = []
        for target in self._files(project, 500):
            if target.stat().st_size > 160_000:
                continue
            try:
                lines = target.read_text(encoding="utf-8").splitlines()
            except (UnicodeError, OSError):
                continue
            for number, line in enumerate(lines, 1):
                if query.casefold() in line.casefold():
                    matches.append({"file": target.relative_to(folder).as_posix(), "line": number, "text": line[:400]})
                    if len(matches) >= 50:
                        return {"ok": True, "matches": matches, "truncated": True}
        return {"ok": True, "matches": matches, "truncated": False}

    def verify_project(self, project: str) -> dict:
        folder = self.project_path(project)
        checks, skipped = [], []
        files = list(self._files(project, 501))
        for target in files[:500]:
            relative = target.relative_to(folder).as_posix()
            if target.suffix.lower() not in {".py", ".json", ".html", ".htm"}:
                continue
            if target.stat().st_size > 160_000:
                skipped.append(relative + ": excede 160 KB")
                continue
            kind = {".py": "python-syntax", ".json": "json-syntax"}.get(target.suffix.lower(), "html-local-resources")
            try:
                raw = target.read_bytes()
                if kind == "python-syntax":
                    encoding, _ = tokenize.detect_encoding(io.BytesIO(raw).readline)
                    ast.parse(raw.decode(encoding), filename=relative)
                elif kind == "json-syntax":
                    json.loads(raw.decode("utf-8-sig"))
                else:
                    parser = _HTMLReferences()
                    parser.feed(raw.decode("utf-8-sig"))
                    if parser.base_href:
                        skipped.append(relative + ": recursos com <base href> exigem navegador")
                    for reference in ([] if parser.base_href else parser.references):
                        url = urlsplit(reference)
                        if url.scheme or url.netloc or not url.path:
                            continue
                        path = unquote(url.path)
                        resource = folder / path.lstrip("/") if path.startswith("/") else target.parent / path
                        normalized = Path(os.path.abspath(resource))
                        if not normalized.is_relative_to(folder):
                            raise ValueError("Recurso fora do projeto: " + reference)
                        resource = self.project_path(project, normalized.relative_to(folder).as_posix())
                        if not resource.is_file():
                            raise ValueError("Recurso local ausente: " + reference)
                checks.append({"file": relative, "check": kind, "ok": True, "sha256": sha256(raw)})
            except (SyntaxError, ValueError, UnicodeError, OSError) as exc:
                checks.append({"file": relative, "check": kind, "ok": False, "error": str(exc)[:700]})
        if len(files) > 500:
            skipped.append("Limite de 500 arquivos atingido.")
        passed = bool(checks) and all(item["ok"] for item in checks)
        return {"ok": passed, "status": "succeeded" if passed else "failed" if checks else "not_checked",
                "project": folder.name, "checks": checks, "skipped": skipped,
                "evidence": {"checked": len(checks), "failed": sum(not item["ok"] for item in checks)},
                "message": "Verificação estática; não executa código nem comprova aparência ou funcionamento em navegador."}

    def run_project_check(self, project: str, check: str = "python-tests", cancel_event=None,
                          approve_execution=None, timeout: float = 60) -> dict:
        from .process_runner import run_project_check
        return run_project_check(self.project_path(project), check=check, cancel_event=cancel_event,
                                 approve_execution=approve_execution, timeout=timeout)

    def open_project(self, project: str, path: str = "") -> dict:
        target = self.project_path(project, path) if path else self.project_path(project)
        if not target.exists():
            raise FileNotFoundError("Projeto ou arquivo não encontrado.")
        if target.is_file() and target.suffix.lower() not in {".html", ".htm", ".txt", ".md", ".pdf", ".png", ".jpg", ".jpeg", ".gif", ".css", ".json"}:
            raise PermissionError("Abra a pasta para revisar esse arquivo. Executáveis e scripts exigem execução aprovada.")
        if sys.platform == "win32":
            os.startfile(str(target))  # type: ignore[attr-defined]
        elif sys.platform == "darwin":
            subprocess.Popen(["open", str(target)], stdin=subprocess.DEVNULL)
        else:
            subprocess.Popen(["xdg-open", str(target)], stdin=subprocess.DEVNULL)
        return {"ok": True, "status": "requested", "opened": str(target),
                "evidence": {"path_exists": True, "os_request_accepted": True},
                "message": "Abertura solicitada ao sistema; janela/conteúdo ainda não observados."}
