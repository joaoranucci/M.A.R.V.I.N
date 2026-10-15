"""Upload pipeline: received -> processing -> available | failed.

The Vault indexes synchronously, so the gateway accepts the bytes, answers
`received` and indexes in the background. While the Vault is closed the upload
waits (retried; Vault deduplicates by SHA-256) and fails after one hour.
"""
from __future__ import annotations

from datetime import timedelta
import hashlib
from pathlib import Path
import queue
import threading
import time
import uuid

from .events import EventLog
from .store import Store, iso, parse_iso, utc_now
from .vault import MAX_FILE_BYTES, SUPPORTED_EXTENSIONS, VaultAdapter, VaultError, VaultUnavailable

WAIT_LIMIT = timedelta(hours=1)
RETRY_SECONDS = 30


class UploadError(Exception):
    def __init__(self, code: str, message: str, status: int = 400):
        super().__init__(message)
        self.code, self.status = code, status


def safe_filename(name: str) -> str:
    name = Path(str(name).replace("\\", "/")).name.strip()
    if not name or name in {".", ".."} or len(name) > 200:
        raise UploadError("invalid_filename", "Nome de arquivo inválido.")
    return name


class DocumentPipeline:
    def __init__(self, store: Store, events: EventLog, vault: VaultAdapter, spool: Path):
        self.store, self.events, self.vault, self.spool = store, events, vault, Path(spool)
        self.spool.mkdir(parents=True, exist_ok=True)
        self.queue: queue.Queue[str] = queue.Queue()
        self.stop = threading.Event()
        self.thread: threading.Thread | None = None
        for row in store.all("SELECT id FROM uploads WHERE state IN ('received', 'processing')"):
            self.queue.put(row["id"])

    def start(self) -> None:
        if self.thread is None:
            self.thread = threading.Thread(target=self._loop, daemon=True, name="MARVIN-mobile-documents")
            self.thread.start()

    def close(self) -> None:
        self.stop.set()

    @staticmethod
    def public(row: dict) -> dict:
        return {"upload_id": row["id"], "filename": row["filename"], "category": row["category"], "size": row["size"],
                "state": row["state"], "message": row["message"], "document_id": row["document_id"],
                "chunks": row["chunks"], "created_at": row["created_at"], "updated_at": row["updated_at"]}

    def get(self, upload_id: str) -> dict | None:
        row = self.store.one("SELECT * FROM uploads WHERE id=?", (upload_id,))
        return self.public(row) if row else None

    def list(self, limit: int = 50) -> list[dict]:
        return [self.public(r) for r in self.store.all("SELECT * FROM uploads ORDER BY created_at DESC LIMIT ?",
                                                        (min(max(limit, 1), 200),))]

    def receive(self, device_id: str, client_id: str, filename: str, category: str, raw: bytes) -> tuple[dict, bool]:
        filename = safe_filename(filename)
        if not (8 <= len(client_id) <= 64):
            raise UploadError("invalid_client_id", "Identificador de envio inválido.", 422)
        previous = self.store.one("SELECT * FROM requests WHERE client_id=?", (client_id,))
        if previous:
            current = self.get(previous["ref"])
            if previous["device_id"] != device_id or current is None:
                raise UploadError("client_id_reused", "Identificador já usado.", 409)
            return current, True
        suffix = Path(filename).suffix.lower()
        if suffix not in SUPPORTED_EXTENSIONS:
            raise UploadError("unsupported_format", f"Formato {suffix or 'sem extensão'} não é aceito pela biblioteca.", 415)
        if not raw:
            raise UploadError("empty_file", "Arquivo vazio.")
        if len(raw) > MAX_FILE_BYTES:
            raise UploadError("file_too_large", "Arquivo acima de 20 MB.", 413)
        category = (category or "geral").strip()[:64] or "geral"
        upload_id, now = uuid.uuid4().hex, iso()
        (self.spool / upload_id).write_bytes(raw)
        digest = hashlib.sha256(raw).hexdigest()
        with self.store.connect() as db:
            db.execute("INSERT INTO uploads VALUES (?, ?, ?, ?, ?, ?, 'received', 'Arquivo recebido pelo PC.', NULL, NULL, ?, ?)",
                       (upload_id, device_id, filename, category, len(raw), digest, now, now))
            db.execute("INSERT INTO requests VALUES (?, ?, 'upload', ?, ?, ?)", (client_id, device_id, upload_id, digest, now))
        record = self.get(upload_id)
        self.events.publish("document.upload", record)
        self.queue.put(upload_id)
        return record, False

    def _set(self, upload_id: str, state: str, message: str, **fields) -> None:
        sets, args = ["state=?", "message=?", "updated_at=?"], [state, message[:500], iso()]
        for key in ("document_id", "chunks"):
            if key in fields:
                sets.append(f"{key}=?")
                args.append(fields[key])
        self.store.execute(f"UPDATE uploads SET {', '.join(sets)} WHERE id=?", (*args, upload_id))
        self.events.publish("document.upload", self.get(upload_id))
        if state in {"available", "failed"}:
            (self.spool / upload_id).unlink(missing_ok=True)

    def process(self, upload_id: str) -> bool:
        """Returns False when it must be retried later (Vault unavailable)."""
        row = self.store.one("SELECT * FROM uploads WHERE id=?", (upload_id,))
        if row is None or row["state"] not in {"received", "processing"}:
            return True
        path = self.spool / upload_id
        if not path.is_file():
            self._set(upload_id, "failed", "O arquivo temporário não existe mais no PC. Envie novamente.")
            return True
        self._set(upload_id, "processing", "Extraindo texto e indexando no cofre.")
        try:
            result = self.vault.upload(row["filename"], path.read_bytes(), row["category"])
        except VaultUnavailable as exc:
            if utc_now() - parse_iso(row["created_at"]) > WAIT_LIMIT:
                self._set(upload_id, "failed", "O cofre ficou indisponível por mais de uma hora: " + str(exc))
                return True
            self._set(upload_id, "received", "Aguardando o cofre do PC: " + str(exc))
            return False
        except VaultError as exc:
            self._set(upload_id, "failed", str(exc))
            return True
        duplicate = result.get("status") == "duplicado"
        message = ("Documento já estava na biblioteca; nada foi duplicado." if duplicate else
                   f"Disponível para consulta em {result.get('chunks', 0)} trechos.")
        self._set(upload_id, "available", message, document_id=result.get("document_id"), chunks=result.get("chunks"))
        return True

    def _loop(self) -> None:
        waiting: dict[str, float] = {}
        while not self.stop.is_set():
            now = time.monotonic()
            for upload_id, due in list(waiting.items()):
                if due <= now:
                    waiting.pop(upload_id)
                    self.queue.put(upload_id)
            try:
                upload_id = self.queue.get(timeout=1)
            except queue.Empty:
                continue
            try:
                if not self.process(upload_id):
                    waiting[upload_id] = time.monotonic() + RETRY_SECONDS
            except Exception:  # noqa: BLE001
                self._set(upload_id, "failed", "Falha interna ao indexar o documento.")
