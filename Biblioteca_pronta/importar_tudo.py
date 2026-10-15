"""Importa os textos preparados via API local existente. Somente biblioteca padrao.

Nao recebe senha mestra, nao cria banco e nao repete POST automaticamente.
O token e lido do cofre local desbloqueado pela API.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import uuid
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, ProxyHandler, Request, build_opener

ROOT = Path(__file__).resolve().parent
MAX_FILE_BYTES = 20 * 1024 * 1024


class ImportFailure(RuntimeError):
    pass


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def local_base(value: str) -> str:
    try:
        parts = urlsplit(value)
        port = parts.port
    except ValueError:
        raise ImportFailure("Endereco da API invalido.") from None
    if (parts.scheme != "http" or parts.hostname not in {"127.0.0.1", "::1"}
            or parts.path not in {"", "/"} or parts.query or parts.fragment
            or parts.username is not None or parts.password is not None
            or port == 0 or any(c.isspace() for c in value)):
        raise ImportFailure("Use somente a API deste computador: http://127.0.0.1:8765")
    return value.rstrip("/")


def default_token_path() -> Path:
    override = os.environ.get("MARVIN_VAULT_HOME")
    if override:
        return Path(override).expanduser().resolve() / "api-token.txt"
    if os.name == "nt":
        home = Path(os.environ.get("LOCALAPPDATA") or Path.home() / "AppData/Local")
    else:
        home = Path(os.environ.get("XDG_DATA_HOME") or Path.home() / ".local/share")
    return home / "MarvinVault/api-token.txt"


def load_token(path: Path) -> str:
    try:
        token = path.read_text(encoding="utf-8").strip()
    except (OSError, UnicodeError):
        raise ImportFailure("api-token.txt nao encontrado. Confira o cofre e inicie INICIAR_API.bat.") from None
    if len(token) < 32 or not token.isascii() or any(c.isspace() for c in token):
        raise ImportFailure("Token local invalido. Use api-token.txt do mesmo cofre aberto pela API.")
    return token


def validate_files(root: Path = ROOT) -> tuple[dict, list[tuple[dict, Path]]]:
    try:
        manifest = json.loads((root / "manifesto.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        raise ImportFailure("Manifesto ausente ou invalido. Extraia o ZIP inteiro novamente.") from None
    if manifest.get("schema_version") != 1 or not isinstance(manifest.get("files"), list):
        raise ImportFailure("Versao de manifesto nao suportada.")
    entries = manifest["files"]
    if not entries or len(entries) > 500 or manifest.get("prepared_files") != len(entries):
        raise ImportFailure("Lista de documentos invalida.")
    result = []
    seen = set()
    base = root.resolve()
    for item in entries:
        relative = Path(item["path"])
        unresolved = base / relative
        path = unresolved.resolve()
        if (relative.is_absolute() or not path.is_relative_to(base) or path in seen
                or unresolved.is_symlink()):
            raise ImportFailure("Caminho de documento invalido no manifesto.")
        seen.add(path)
        try:
            data = path.read_bytes()
        except OSError:
            raise ImportFailure("Falta um documento. Extraia o ZIP inteiro: " + path.name) from None
        if not data or len(data) > MAX_FILE_BYTES or len(data) != item["bytes"]:
            raise ImportFailure("Tamanho de documento incorreto: " + path.name)
        if hashlib.sha256(data).hexdigest() != item["sha256"]:
            raise ImportFailure("Documento alterado ou incompleto: " + path.name)
        data.decode("utf-8")
        if path.name != item["filename"] or path.suffix.lower() != ".md":
            raise ImportFailure("Nome de documento invalido.")
        result.append((item, path))
    return manifest, result


class LocalAPI:
    def __init__(self, base_url: str, token: str):
        self.base_url = local_base(base_url)
        self.token = token
        self.opener = build_opener(ProxyHandler({}), NoRedirect())

    def call(self, route: str, *, method="GET", body: bytes | None = None,
             content_type="application/json", authenticated=True):
        headers = {"Accept": "application/json"}
        if authenticated:
            headers["Authorization"] = "Bearer " + self.token
        if body is not None:
            headers["Content-Type"] = content_type
        req = Request(self.base_url + route, data=body, headers=headers, method=method)
        try:
            with self.opener.open(req, timeout=300) as response:
                data = response.read(1_000_001)
        except HTTPError as exc:
            code = exc.code
            exc.close()
            reason = {
                400: "a API recusou o arquivo; confira formato e limites",
                401: "token recusado; use o mesmo cofre da API aberta",
                404: "rota nao encontrada; confira se a MARVIN Vault API esta aberta",
                413: "arquivo acima do limite da API",
                422: "dados de importacao recusados",
            }.get(code, "pedido recusado pela API local")
            raise ImportFailure(f"HTTP {code}: {reason}.") from None
        except (URLError, OSError, TimeoutError):
            raise ImportFailure("API sem resposta. Mantenha INICIAR_API.bat aberto. "
                                "Uma importacao ja iniciada pode ter concluido; aguarde antes de repetir.") from None
        if len(data) > 1_000_000:
            raise ImportFailure("Resposta da API acima do limite.")
        try:
            return json.loads(data)
        except (ValueError, UnicodeError):
            raise ImportFailure("Resposta invalida da API.") from None

    def check(self):
        health = self.call("/health", authenticated=False)
        if not isinstance(health, dict) or health.get("service") != "marvin-vault" or health.get("ok") is not True:
            raise ImportFailure("O servico dessa porta nao e a MARVIN Vault API.")
        # A leitura autentica antes de enviar qualquer documento.
        self.call("/v1/knowledge/documents?limit=1")
        return health

    def upload(self, item: dict, path: Path, category: str):
        boundary = "MARVIN" + uuid.uuid4().hex
        header = (f"--{boundary}\r\nContent-Disposition: form-data; name=\"category\"\r\n\r\n"
                  f"{category}\r\n--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; "
                  f"filename=\"{path.name}\"\r\nContent-Type: text/markdown; charset=utf-8\r\n\r\n").encode("utf-8")
        body = header + path.read_bytes() + f"\r\n--{boundary}--\r\n".encode("ascii")
        result = self.call("/v1/knowledge/upload", method="POST", body=body,
                           content_type="multipart/form-data; boundary=" + boundary)
        if not isinstance(result, dict) or result.get("status") not in {"importado", "duplicado"}:
            raise ImportFailure("A API nao confirmou a importacao.")
        try:
            document_id = str(uuid.UUID(result["document_id"]))
        except (KeyError, ValueError, TypeError):
            raise ImportFailure("A API nao informou um documento valido.") from None
        parent = self.call("/v1/entries/" + document_id)
        attrs = parent.get("attributes", {})
        if (parent.get("kind") != "documento_importado" or attrs.get("sha256") != item["sha256"]
                or attrs.get("category") != category or attrs.get("char_count") != item["normalized_chars"]
                or attrs.get("chunk_count") != item["chunks"]):
            raise ImportFailure("A verificacao do documento importado nao conferiu: " + path.name)
        return result


def run(api: LocalAPI, root: Path = ROOT, *, category="biblioteca") -> dict:
    category = category.strip()
    if not category.strip() or len(category) > 64 or any(c in category for c in "\r\n"):
        raise ImportFailure("Categoria invalida.")
    manifest, files = validate_files(root)
    print(f"Colecao: {manifest['source_documents']} documentos originais; {len(files)} arquivos preparados.", flush=True)
    health = api.check()
    print("API conectada. Versao:", health.get("version", "desconhecida"), flush=True)
    totals = {"importado": 0, "duplicado": 0, "verificado": 0, "trechos": 0}
    for index, (item, path) in enumerate(files, 1):
        print(f"[{index}/{len(files)}] {path.name}", flush=True)
        result = api.upload(item, path, category)
        totals[result["status"]] += 1
        totals["verificado"] += 1
        totals["trechos"] += item["chunks"]
        print("  " + result["status"] + " e verificado.", flush=True)
    print("RESULTADO:", json.dumps(totals, ensure_ascii=False), flush=True)
    return totals


def main() -> int:
    parser = argparse.ArgumentParser(description="Importar a colecao preparada para a MARVIN Vault API local")
    parser.add_argument("--base-url", default=os.environ.get("MARVIN_VAULT_URL", "http://127.0.0.1:8765"))
    parser.add_argument("--token-file", type=Path)
    parser.add_argument("--categoria", default="biblioteca")
    parser.add_argument("--conferir-arquivos", action="store_true")
    args = parser.parse_args()
    try:
        if args.conferir_arquivos:
            manifest, files = validate_files()
            print(f"OK: {len(files)} arquivos conferidos, {manifest['source_documents']} fontes originais.")
            return 0
        token = load_token(args.token_file or default_token_path())
        run(LocalAPI(args.base_url, token), category=args.categoria)
        return 0
    except KeyboardInterrupt:
        print("Interrompido. Os documentos ja concluidos ficam salvos; nao ha repeticao automatica.")
        return 130
    except (ImportFailure, OSError, ValueError, KeyError, TypeError) as exc:
        print("ERRO:", str(exc))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
