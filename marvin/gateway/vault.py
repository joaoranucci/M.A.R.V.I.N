"""Isolated adapter for MARVIN Vault API v0.3 (loopback only, token stays on the PC).

Only routes that exist in the inspected Vault contract are used. Missing
capabilities (document-scoped /ask, async indexing, OCR) are reported, not faked.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
import uuid
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlsplit
from urllib.request import HTTPRedirectHandler, ProxyHandler, Request, build_opener

MAX_RESPONSE = 4_000_000
MEMORY_KIND = "memoria"
ORIGINS = {"user_request", "assistant_inference", "imported"}
SUPPORTED_EXTENSIONS = (".txt", ".md", ".markdown", ".rst", ".pdf", ".docx", ".html", ".htm", ".json", ".csv",
                        ".py", ".js", ".jsx", ".ts", ".tsx", ".sql", ".yaml", ".yml", ".toml", ".ini", ".ps1",
                        ".bat", ".sh", ".css", ".xml")
MAX_FILE_BYTES = 20 * 1024 * 1024


class VaultUnavailable(Exception):
    """Vault process not running, locked, or token missing."""
    def __init__(self, code: str, message: str):
        super().__init__(message)
        self.code = code


class VaultError(Exception):
    def __init__(self, status: int, message: str):
        super().__init__(message)
        self.status = status


class _NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def _loopback(url: str) -> str:
    parts = urlsplit(url)
    if parts.scheme != "http" or parts.hostname not in {"127.0.0.1", "::1"} or parts.path not in {"", "/"}:
        raise ValueError("MARVIN_VAULT_URL deve ser http://127.0.0.1:PORTA")
    return url.rstrip("/")


def _default_token_file() -> Path:
    override = os.environ.get("MARVIN_VAULT_HOME")
    if override:
        return Path(override).expanduser() / "api-token.txt"
    base = os.environ.get("LOCALAPPDATA") or str(Path.home() / "AppData" / "Local")
    return Path(base) / "MarvinVault" / "api-token.txt"


class VaultAdapter:
    def __init__(self, base_url: str, token_file: Path | None = None, timeout: float = 15):
        self.base_url = _loopback(base_url)
        self.token_file = token_file or _default_token_file()
        self.timeout = timeout
        self._opener = build_opener(ProxyHandler({}), _NoRedirect())

    def _token(self) -> str:
        try:
            token = self.token_file.read_text(encoding="utf-8").strip()
        except OSError:
            raise VaultUnavailable("vault_not_configured", "Cofre não configurado neste PC (api-token.txt ausente).") from None
        if len(token) < 32:
            raise VaultUnavailable("vault_not_configured", "Token do cofre inválido no PC.")
        return token

    def _call(self, method: str, route: str, payload: Any = None, *, body: bytes | None = None,
              content_type: str | None = None, auth: bool = True, timeout: float | None = None,
              confirm_delete: bool = False) -> Any:
        headers = {"Accept": "application/json"}
        if auth:
            headers["Authorization"] = "Bearer " + self._token()
        if payload is not None:
            body = json.dumps(payload, ensure_ascii=False, allow_nan=False).encode("utf-8")
            content_type = "application/json"
        if content_type:
            headers["Content-Type"] = content_type
        if confirm_delete:
            headers["X-Confirm-Delete"] = "yes"
        request = Request(self.base_url + route, data=body, headers=headers, method=method)
        try:
            with self._opener.open(request, timeout=timeout or self.timeout) as response:
                if response.status == 204:
                    return None
                raw = response.read(MAX_RESPONSE + 1)
        except HTTPError as exc:
            status = exc.code
            try:
                detail = json.loads(exc.read(20000) or b"{}").get("detail", "")
            except (ValueError, AttributeError):
                detail = ""
            finally:
                exc.close()
            if status == 401:
                raise VaultUnavailable("vault_token_rejected", "O cofre recusou o token do PC. Confira api-token.txt.") from None
            if isinstance(detail, list):
                detail = "Dados inválidos para o cofre."
            raise VaultError(status, str(detail)[:300] or f"Falha no cofre (HTTP {status}).") from None
        except (URLError, OSError, TimeoutError):
            raise VaultUnavailable("vault_offline", "Cofre de memória fechado no PC. Execute INICIAR_API.bat e desbloqueie.") from None
        if len(raw) > MAX_RESPONSE:
            raise VaultError(502, "Resposta do cofre grande demais.")
        try:
            return json.loads(raw)
        except ValueError:
            raise VaultError(502, "Resposta inválida do cofre.") from None

    # ---- status -------------------------------------------------------------
    def status(self) -> dict:
        try:
            health = self._call("GET", "/health", auth=False, timeout=3)
            if not isinstance(health, dict) or health.get("service") != "marvin-vault":
                return {"state": "unavailable", "code": "vault_wrong_service", "message": "Outro serviço responde na porta do cofre."}
            data = self._call("GET", "/v1/status", timeout=5)
            return {"state": "ok", "version": health.get("version"), "memories": data.get("memories"),
                    "documents": data.get("documents"), "chunks": data.get("chunks"),
                    "categories": data.get("categories", []), "search": data.get("search", "bm25")}
        except VaultUnavailable as exc:
            return {"state": "unavailable", "code": exc.code, "message": str(exc)}
        except VaultError as exc:
            return {"state": "unavailable", "code": "vault_error", "message": str(exc)}

    # ---- memories -----------------------------------------------------------
    @staticmethod
    def to_memory(entry: dict) -> dict:
        attrs = entry.get("attributes") or {}
        tags = entry.get("tags") or []
        body = entry.get("body")
        content = body if isinstance(body, str) else json.dumps(body, ensure_ascii=False)
        origin = attrs.get("origin")
        if origin not in ORIGINS:
            # Desktop bridge records ('marvin-local') come from explicit "lembre que" commands.
            origin = "user_request" if origin == "marvin-local" else "imported"
        source = attrs.get("source") or ("desktop" if attrs.get("origin") == "marvin-local" else "vault")
        category = attrs.get("category") or next((t for t in tags if t not in {"comando-local", "smoke"}), "geral")
        return {"id": entry["id"], "title": entry.get("title", ""), "content": content, "category": str(category)[:40],
                "origin": origin, "source": str(source)[:40], "client_id": attrs.get("client_id"),
                "created_at": entry.get("created_at"), "updated_at": entry.get("updated_at")}

    def list_memories(self, q: str = "", limit: int = 200, offset: int = 0) -> list[dict]:
        query = urlencode({"q": q, "kind": MEMORY_KIND, "limit": min(max(limit, 1), 200), "offset": max(offset, 0)})
        return [self.to_memory(e) for e in self._call("GET", "/v1/entries?" + query)]

    def all_memories(self) -> list[dict]:
        found, offset = [], 0
        while True:
            page = self.list_memories(limit=200, offset=offset)
            found.extend(page)
            if len(page) < 200 or offset > 20000:
                return found
            offset += 200

    def find_by_client_id(self, client_id: str) -> dict | None:
        for memory in self.list_memories(q=client_id, limit=20):
            if memory.get("client_id") == client_id:
                return memory
        return None

    @staticmethod
    def _entry(content: str, category: str, origin: str, source: str, client_id: str | None,
               title: str = "", device_id: str = "", extra: dict | None = None) -> dict:
        attributes = dict(extra or {})
        attributes.update({"origin": origin, "source": source, "category": category})
        if client_id:
            attributes["client_id"] = client_id
        if device_id:
            attributes["device_id"] = device_id
        first_line = content.strip().splitlines()[0] if content.strip() else "Memória"
        return {"kind": MEMORY_KIND, "title": (title or first_line)[:120], "body": content,
                "tags": [category], "attributes": attributes}

    def create_memory(self, *, content: str, category: str, origin: str, source: str, client_id: str,
                      device_id: str) -> tuple[dict, bool]:
        existing = self.find_by_client_id(client_id)
        if existing:
            return existing, True
        entry = self._call("POST", "/v1/entries", self._entry(content, category, origin, source, client_id,
                                                               device_id=device_id))
        return self.to_memory(entry), False

    def get_memory(self, memory_id: str) -> dict | None:
        try:
            entry = self._call("GET", "/v1/entries/" + str(uuid.UUID(memory_id)))
        except VaultError as exc:
            if exc.status == 404:
                return None
            raise
        return self.to_memory(entry) if entry.get("kind") == MEMORY_KIND else None

    def update_memory(self, memory_id: str, *, content: str, category: str, origin: str,
                      base_updated_at: str | None) -> tuple[str, dict | None]:
        entry_id = str(uuid.UUID(memory_id))
        try:
            current = self._call("GET", "/v1/entries/" + entry_id)
        except VaultError as exc:
            if exc.status == 404:
                return "missing", None
            raise
        if current.get("kind") != MEMORY_KIND:
            return "missing", None
        if base_updated_at and current.get("updated_at") != base_updated_at:
            return "conflict", self.to_memory(current)
        attrs = dict(current.get("attributes") or {})
        source = attrs.get("source") or "vault"
        payload = self._entry(content, category, origin, source, attrs.get("client_id"), extra=attrs)
        updated = self._call("PUT", "/v1/entries/" + entry_id, payload)
        return "updated", self.to_memory(updated)

    def delete_memory(self, memory_id: str) -> bool:
        entry_id = str(uuid.UUID(memory_id))
        current = self.get_memory(entry_id)
        if current is None:
            return False
        try:
            self._call("DELETE", "/v1/entries/" + entry_id, confirm_delete=True)
        except VaultError as exc:
            if exc.status != 404:
                raise
        return True

    # ---- documents ----------------------------------------------------------
    def list_documents(self) -> list[dict]:
        documents, offset = [], 0
        while True:
            query = urlencode({"kind": "documento_importado", "limit": 200, "offset": offset})
            page = self._call("GET", "/v1/entries?" + query)
            for entry in page:
                attrs = entry.get("attributes") or {}
                documents.append({"document_id": entry["id"], "filename": entry.get("title", ""),
                                  "category": attrs.get("category", "geral"), "chunks": attrs.get("chunk_count", 0),
                                  "chars": attrs.get("char_count", 0), "extension": attrs.get("extension", ""),
                                  "sha256": attrs.get("sha256", ""), "created_at": entry.get("created_at"),
                                  "state": "available"})
            if len(page) < 200 or offset > 20000:
                return documents
            offset += 200

    def upload(self, filename: str, raw: bytes, category: str) -> dict:
        boundary = "marvin" + uuid.uuid4().hex
        safe = filename.replace('"', "").replace("\r", "").replace("\n", "")[:220]
        parts = [
            f"--{boundary}\r\nContent-Disposition: form-data; name=\"category\"\r\n\r\n{category}\r\n".encode("utf-8"),
            (f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{safe}\"\r\n"
             "Content-Type: application/octet-stream\r\n\r\n").encode("utf-8"), raw, f"\r\n--{boundary}--\r\n".encode("utf-8")]
        return self._call("POST", "/v1/knowledge/upload", body=b"".join(parts),
                          content_type="multipart/form-data; boundary=" + boundary, timeout=300)

    def delete_document(self, document_id: str) -> bool:
        try:
            self._call("DELETE", "/v1/knowledge/documents/" + str(uuid.UUID(document_id)), confirm_delete=True)
        except VaultError as exc:
            if exc.status == 404:
                return False
            raise
        return True

    def search(self, q: str, *, category: str = "", top_k: int = 5, document_id: str = "") -> list[dict]:
        wanted = 20 if document_id else min(max(top_k, 1), 20)
        hits = self._call("GET", "/v1/knowledge/search?" + urlencode({"q": q, "category": category, "top_k": wanted}),
                          timeout=60)
        if document_id:
            hits = [h for h in hits if h.get("document_id") == document_id][:top_k]
        return [{"chunk_id": h["chunk_id"], "document_id": h["document_id"], "filename": h["filename"],
                 "part": h["part"], "category": h.get("category", ""), "score": h.get("score", 0),
                 "excerpt": str(h.get("text", ""))[:900]} for h in hits]

    def chunk(self, chunk_id: str) -> dict | None:
        try:
            entry = self._call("GET", "/v1/entries/" + str(uuid.UUID(chunk_id)))
        except VaultError as exc:
            if exc.status == 404:
                return None
            raise
        if entry.get("kind") != "trecho_documento":
            return None
        attrs = entry.get("attributes") or {}
        return {"chunk_id": entry["id"], "document_id": attrs.get("document_id"), "filename": entry.get("title", ""),
                "part": attrs.get("part"), "total": attrs.get("total"), "category": attrs.get("category", ""),
                "text": str(entry.get("body", ""))}

    def ask(self, question: str, *, category: str = "", document_id: str = "") -> dict:
        """Vault /ask has no document filter: scope by category and report what was used."""
        if document_id and not category:
            match = next((d for d in self.list_documents() if d["document_id"] == document_id), None)
            if match is None:
                raise VaultError(404, "Documento não encontrado.")
            category = match["category"]
        passages = self.search(question, category=category, top_k=8)
        try:
            result = self._call("POST", "/v1/knowledge/ask", {"question": question, "category": category, "top_k": 8},
                                timeout=200)
            answer, model, generated = result.get("answer", ""), result.get("model"), True
            used = result.get("sources", [])
        except VaultError as exc:
            if exc.status != 503:
                raise
            answer, model, generated, used = "", None, False, []
            unavailable = str(exc)
        else:
            unavailable = ""
        index = {(p["document_id"], p["part"]): p for p in passages}
        sources = []
        for source in (used if generated else passages):
            key = (source.get("document_id"), source.get("part"))
            passage = index.get(key, {})
            sources.append({"document_id": source.get("document_id"), "filename": source.get("filename"),
                            "part": source.get("part"), "chunk_id": passage.get("chunk_id"),
                            "excerpt": passage.get("excerpt", ""), "score": source.get("score", 0)})
        in_scope = [s for s in sources if not document_id or s["document_id"] == document_id]
        return {"answer": answer, "generated": generated, "model": model, "sources": sources,
                "document_id": document_id or None, "sources_in_document": len(in_scope),
                "llm_unavailable_reason": unavailable or None}
