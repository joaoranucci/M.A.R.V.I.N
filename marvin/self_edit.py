"""Reviewable multi-file self-edit proposals with backups and recovery records.

Preparing a proposal never changes source. Only explicit UI approval may call
apply_reviewed. Files are replaced atomically one at a time; the transaction
journal and originals survive a crash because a multi-file replace is not an
OS-level atomic transaction.
"""
from __future__ import annotations

import difflib
import hashlib
import json
from pathlib import Path
import threading
import time
import uuid

from .workspace import atomic_write, checked_path, _relative_file


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


class SourceEditor:
    def __init__(self, app_root: Path):
        self.root = Path(app_root).resolve()
        self.proposals = checked_path(self.root, Path("data/code_proposals"))
        self.proposals.mkdir(parents=True, exist_ok=True)
        self._lock = threading.RLock()

    def _internal(self, relative: str) -> Path:
        return checked_path(self.root, Path(relative))

    def _target(self, relative_path: str) -> Path:
        clean = str(relative_path).replace("\\", "/")
        try:
            p = _relative_file(clean)
        except (ValueError, PermissionError) as exc:
            raise PermissionError("Caminho inválido para editar o MARVIN.") from exc
        chunks = clean.split("/")
        valid = (len(chunks) == 2 and chunks[0] in {"marvin", "tests"} and chunks[1].endswith(".py")) or chunks == ["ui_tars_bridge", "runner.mjs"]
        if not valid or len(clean) > 180:
            raise PermissionError("Somente módulos Python existentes e o runner do UI-TARS podem receber propostas.")
        target = checked_path(self.root, p)
        if not target.is_file():
            raise PermissionError("Arquivo original não encontrado ou fora do MARVIN.")
        return target

    def read_source(self, path: str) -> dict:
        target = self._target(path)
        if target.stat().st_size > 160_000:
            raise ValueError("Arquivo grande demais para esta ferramenta.")
        original = target.read_bytes()
        return {"file": str(target.relative_to(self.root)), "content": original.decode("utf-8"), "sha256": sha(original)}

    def propose_self_edit(self, path: str, content: str, reason: str) -> dict:
        return self.propose_changes({path: content}, reason)

    def propose_changes(self, changes: dict[str, str], reason: str) -> dict:
        if not isinstance(changes, dict) or not 1 <= len(changes) <= 20:
            raise ValueError("Proponha entre 1 e 20 arquivos existentes por revisão.")
        with self._lock:
            prepared = []
            targets = set()
            total = 0
            for path, content in changes.items():
                target = self._target(path)
                identity = str(target).casefold()
                if identity in targets:
                    raise ValueError("Um arquivo aparece mais de uma vez na proposta.")
                targets.add(identity)
                if not isinstance(content, str) or len(content.encode("utf-8")) > 160_000:
                    raise ValueError("Mudança grande demais (160 KB por arquivo).")
                raw = content.encode("utf-8")
                total += len(raw)
                if total > 800_000:
                    raise ValueError("Proposta excede 800 KB.")
                if target.suffix == ".py":
                    compile(raw, str(target), "exec")
                before = target.read_bytes()
                if before != raw:
                    prepared.append((target.relative_to(self.root).as_posix(), before, raw))
            if not prepared:
                return {"ok": True, "changed": False, "message": "Não há mudanças."}
            token = uuid.uuid4().hex[:16]
            entries = []
            for index, (path, before, after) in enumerate(prepared):
                payload = f"{token}.new" if len(prepared) == 1 else f"{token}.{index}.new"
                original = f"{token}.{index}.old"
                atomic_write(self._internal("data/code_proposals/" + payload), after, replace=False)
                atomic_write(self._internal("data/code_proposals/" + original), before, replace=False)
                entries.append({"file": path, "original_sha256": sha(before), "proposed_sha256": sha(after),
                                "payload": payload, "original": original})
            metadata = {"version": 2, "id": token, "file": entries[0]["file"], "files": [entry["file"] for entry in entries],
                        "reason": str(reason)[:1000], "original_sha256": entries[0]["original_sha256"],
                        "created": int(time.time()), "status": "pending", "changes": entries,
                        "verification": {"python_syntax": "passed", "runtime_tests": "not_run",
                                         "message": "Sintaxe Python verificada. Testes de execução não foram executados."}}
            atomic_write(self._internal(f"data/code_proposals/{token}.json"),
                         json.dumps(metadata, ensure_ascii=False).encode("utf-8"), replace=False)
            return {"ok": True, "changed": True, "proposal_id": token, "files": metadata["files"],
                    "verification": metadata["verification"],
                    "message": "Alteração proposta, mas NÃO aplicada. Abra REVISAR CÓDIGO para aprovar todos os arquivos."}

    @staticmethod
    def _validate_id(proposal_id: str):
        if not isinstance(proposal_id, str) or len(proposal_id) != 16 or not all(c in "0123456789abcdef" for c in proposal_id):
            raise ValueError("ID de proposta inválido.")

    def _proposal(self, proposal_id: str) -> dict:
        self._validate_id(proposal_id)
        source = self._internal(f"data/code_proposals/{proposal_id}.json")
        if source.stat().st_size > 100_000:
            raise ValueError("Metadados da proposta grandes demais.")
        meta = json.loads(source.read_text(encoding="utf-8"))
        if meta.get("id") != proposal_id:
            raise ValueError("Proposta corrompida.")
        return meta

    def _entries(self, meta):
        entries = meta.get("changes") or [{"file": meta["file"], "original_sha256": meta["original_sha256"],
                                           "payload": meta["id"] + ".new"}]
        if not isinstance(entries, list) or not 1 <= len(entries) <= 20:
            raise ValueError("Proposta corrompida.")
        seen = set()
        for entry in entries:
            identity = str(self._target(entry["file"])).casefold()
            if identity in seen:
                raise ValueError("Proposta contém arquivos duplicados.")
            seen.add(identity)
        return entries

    def _blob(self, meta, entry, key="payload"):
        name = entry[key]
        if not isinstance(name, str) or Path(name).name != name or "/" in name or "\\" in name or not name.startswith(meta["id"] + "."):
            raise ValueError("Conteúdo da proposta inválido.")
        _relative_file(name)
        path = self._internal("data/code_proposals/" + name)
        if path.stat().st_size > 160_000:
            raise ValueError("Conteúdo da proposta grande demais.")
        content = path.read_bytes()
        expected = entry.get("proposed_sha256" if key == "payload" else "original_sha256")
        if expected and sha(content) != expected:
            raise RuntimeError("Conteúdo da proposta foi alterado; gere uma nova revisão.")
        return content

    def pending(self) -> list[dict]:
        results = []
        folder = self._internal("data/code_proposals")
        for path in folder.glob("*.json"):
            try:
                meta = self._proposal(path.stem)
                if meta.get("status", "pending") != "pending":
                    continue
                for entry in self._entries(meta):
                    self._blob(meta, entry)
                results.append(meta)
            except (TypeError, ValueError, KeyError, RuntimeError, OSError):
                continue
        return sorted(results, key=lambda z: z["created"], reverse=True)

    def diff(self, proposal_id: str) -> str:
        meta = self._proposal(proposal_id)
        output = []
        for entry in self._entries(meta):
            current = self._target(entry["file"]).read_bytes()
            if sha(current) != entry["original_sha256"]:
                output.append(f"CONFLITO em {entry['file']}: mudou desde a proposta; aplicação será bloqueada.\n")
            before = self._blob(meta, entry, "original") if "original" in entry else current
            after = self._blob(meta, entry)
            output.extend(difflib.unified_diff(before.decode("utf-8").splitlines(keepends=True),
                                             after.decode("utf-8").splitlines(keepends=True),
                                             fromfile="original/" + entry["file"], tofile="proposto/" + entry["file"]))
        text = "".join(output)
        if len(text) > 1_000_000:
            raise ValueError("Diff grande demais para revisar com segurança. Divida a proposta.")
        return text

    def _journal(self, token: str, manifest: dict):
        target = self._internal(f"data/code_backups/{token}/transaction.json")
        atomic_write(target, json.dumps(manifest, ensure_ascii=False).encode("utf-8"))

    def apply_reviewed(self, proposal_id: str) -> dict:
        """Only call in direct response to explicit approval of the full diff."""
        with self._lock:
            meta = self._proposal(proposal_id)
            if meta.get("status", "pending") != "pending":
                raise RuntimeError("Esta proposta já foi processada. Consulte os backups antes de continuar.")
            changes = []
            for entry in self._entries(meta):
                target = self._target(entry["file"])
                before = target.read_bytes()
                if sha(before) != entry["original_sha256"]:
                    raise RuntimeError("O arquivo foi alterado depois da proposta. Gere uma nova proposta: " + entry["file"])
                proposed = self._blob(meta, entry)
                if target.suffix == ".py":
                    compile(proposed, str(target), "exec")
                changes.append((entry, target, before, proposed))
            manifest = {"id": proposal_id, "status": "preparing", "created": int(time.time()), "files": []}
            directory = self._internal(f"data/code_backups/{proposal_id}")
            if directory.exists():
                raise RuntimeError("Já há uma transação/backup para esta proposta. Reconcilie antes de tentar novamente.")
            directory.mkdir(parents=True)
            self._journal(proposal_id, manifest)
            for entry, target, before, proposed in changes:
                backup = self._internal(f"data/code_backups/{proposal_id}/" + entry["file"])
                backup.parent.mkdir(parents=True, exist_ok=True)
                atomic_write(backup, before, replace=False)
                manifest["files"].append({"file": entry["file"], "original_sha256": sha(before), "proposed_sha256": sha(proposed)})
            manifest["status"] = "applying"
            self._journal(proposal_id, manifest)
            applied = []
            try:
                for entry, target, before, proposed in changes:
                    target = self._target(entry["file"])
                    if target.read_bytes() != before:
                        raise RuntimeError("Arquivo alterado durante aplicação: " + entry["file"])
                    atomic_write(target, proposed)
                    applied.append((entry, target, before, proposed))
                    if target.read_bytes() != proposed:
                        raise RuntimeError("Conteúdo aplicado diverge da proposta: " + entry["file"])
                manifest["status"] = "applied"
                self._journal(proposal_id, manifest)
                meta["status"] = "applied"
                atomic_write(self._internal(f"data/code_proposals/{proposal_id}.json"), json.dumps(meta, ensure_ascii=False).encode("utf-8"))
            except Exception as error:
                failures = []
                for entry, target, before, proposed in reversed(applied):
                    try:
                        target = self._target(entry["file"])
                        if target.read_bytes() != proposed:
                            raise RuntimeError("Arquivo mudou após aplicação; restauração automática bloqueada.")
                        atomic_write(target, before)
                        if target.read_bytes() != before:
                            raise RuntimeError("Restauração não verificada.")
                    except Exception:
                        failures.append(entry["file"])
                manifest.update(status="needs_reconciliation" if failures else "rolled_back", rollback_failures=failures)
                self._journal(proposal_id, manifest)
                raise RuntimeError(f"Falha na aplicação; estado {manifest['status']}. Backups: {directory}. {error}") from error
            return {"ok": True, "file": str(changes[0][1]), "files": [entry["file"] for entry, *_ in changes],
                    "backup": str(directory / changes[0][0]["file"]), "backup_directory": str(directory),
                    "evidence": {"verified_files": len(changes), "transaction": str(directory / "transaction.json")},
                    "message": "Alterações aplicadas e verificadas. Reinicie o MARVIN para carregá-las."}

    def rollback_reviewed(self, proposal_id: str) -> dict:
        """Explicit user recovery only; preserves files edited after application."""
        self._validate_id(proposal_id)
        with self._lock:
            path = self._internal(f"data/code_backups/{proposal_id}/transaction.json")
            manifest = json.loads(path.read_text(encoding="utf-8"))
            if manifest.get("id") != proposal_id or manifest.get("status") not in {"applied", "applying", "needs_reconciliation", "rolling_back"}:
                raise RuntimeError("Transação não pode ser restaurada nesse estado.")
            prepared = []
            for entry in manifest["files"]:
                target = self._target(entry["file"])
                current = target.read_bytes()
                if sha(current) == entry["original_sha256"]:
                    continue
                if sha(current) != entry["proposed_sha256"]:
                    raise RuntimeError("Arquivo mudou após aplicação; recuperação precisa de revisão: " + entry["file"])
                before = self._internal(f"data/code_backups/{proposal_id}/" + entry["file"]).read_bytes()
                if sha(before) != entry["original_sha256"]:
                    raise RuntimeError("Backup não corresponde ao original.")
                prepared.append((entry, target, current, before))
            manifest["status"] = "rolling_back"
            self._journal(proposal_id, manifest)
            for entry, target, current, before in prepared:
                target = self._target(entry["file"])
                if target.read_bytes() != current:
                    raise RuntimeError("Arquivo mudou durante recuperação; consulte a transação.")
                atomic_write(target, before)
                if target.read_bytes() != before:
                    raise RuntimeError("Não foi possível verificar a restauração.")
            manifest["status"] = "rolled_back"
            self._journal(proposal_id, manifest)
            return {"ok": True, "status": "rolled_back", "files": [entry["file"] for entry, *_ in prepared]}
