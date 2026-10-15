"""HTTPS API for paired devices. Contract: docs/mobile/API_GATEWAY.md.

Errors always use {"error": {"code", "message"}}. Every route except /v1/health
and /v1/pair requires `Authorization: Bearer <device token>`.
"""
from __future__ import annotations

import asyncio
import time
import uuid
from typing import Literal

from fastapi import Depends, FastAPI, File, Form, Header, HTTPException, Query, Request, UploadFile
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel, Field

from . import API_VERSION, GATEWAY_VERSION
from .assistant import ConflictError
from .desktop import CommandError
from .documents import UploadError
from .items import ItemConflict
from .pairing import PairingError
from .speech import SpeechUnavailable
from .store import iso
from .vault import MAX_FILE_BYTES, SUPPORTED_EXTENSIONS, VaultError, VaultUnavailable

DEFAULT_BODY_LIMIT = 256_000
UPLOAD_BODY_LIMIT = MAX_FILE_BYTES + 512_000
MAX_WAIT = 25


class BodyLimit:
    """Rejects oversized bodies, including chunked uploads without Content-Length."""
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            return await self.app(scope, receive, send)
        limit = UPLOAD_BODY_LIMIT if scope["path"] == "/v1/documents" else DEFAULT_BODY_LIMIT
        declared = dict(scope.get("headers") or []).get(b"content-length")
        if declared is not None:
            try:
                too_big = int(declared) > limit
            except ValueError:
                too_big = True
            if too_big:
                response = JSONResponse({"error": {"code": "payload_too_large", "message": "Pedido grande demais."}}, 413)
                return await response(scope, receive, send)
        total = 0

        async def limited():
            nonlocal total
            message = await receive()
            if message["type"] == "http.request":
                total += len(message.get("body", b""))
                if total > limit:
                    raise HTTPException(413, "Pedido grande demais.")
            return message

        return await self.app(scope, limited, send)


def error(status: int, code: str, message: str, **extra) -> JSONResponse:
    return JSONResponse({"error": {"code": code, "message": message, **extra}}, status_code=status)


class PairIn(BaseModel):
    code: str = Field(min_length=6, max_length=6)
    device_name: str = Field(min_length=1, max_length=80)
    platform: Literal["android", "ios", "wearable", "other"] = "android"
    app_version: str = Field(default="", max_length=40)


class MessageIn(BaseModel):
    client_id: str = Field(min_length=8, max_length=64, pattern=r"^[A-Za-z0-9_-]+$")
    text: str = Field(min_length=1, max_length=12000)
    engine: Literal["marvin", "ollama"] = "marvin"
    source: Literal["voice", "text"] = "text"


class DecisionIn(BaseModel):
    accepted: bool


class MemoryIn(BaseModel):
    client_id: str = Field(min_length=8, max_length=64, pattern=r"^[A-Za-z0-9_-]+$")
    content: str = Field(min_length=1, max_length=20000)
    category: str = Field(default="geral", min_length=1, max_length=40)
    origin: Literal["user_request", "assistant_inference", "imported"] = "user_request"
    source: str = Field(default="mobile-text", max_length=40)


class MemoryUpdate(BaseModel):
    content: str = Field(min_length=1, max_length=20000)
    category: str = Field(default="geral", min_length=1, max_length=40)
    origin: Literal["user_request", "assistant_inference", "imported"] = "user_request"
    base_updated_at: str | None = Field(default=None, max_length=40)


class AskIn(BaseModel):
    question: str = Field(min_length=3, max_length=600)
    document_id: str | None = Field(default=None, max_length=64)
    category: str = Field(default="", max_length=64)


class ItemIn(BaseModel):
    kind: Literal["task", "reminder", "note"]
    title: str = Field(min_length=1, max_length=300)
    notes: str = Field(default="", max_length=4000)
    due_at: str | None = Field(default=None, max_length=40)
    done: bool = False
    deleted: bool = False
    base_rev: int | None = Field(default=None, ge=0)


class CommandIn(BaseModel):
    command_id: str = Field(min_length=8, max_length=64)
    action: str = Field(min_length=1, max_length=40)
    params: dict = Field(default_factory=dict)
    expires_at: str | None = Field(default=None, max_length=40)
    confirmed: bool = False


class SpeechIn(BaseModel):
    text: str = Field(min_length=1, max_length=4000)
    voice: str = Field(min_length=1, max_length=40)
    rate: float = Field(default=1.0, ge=0.5, le=2.0)


def create_app(gateway) -> BodyLimit:
    """`gateway` is a server.Gateway with pairing, events, assistant, vault, documents, items, desktop, speech."""
    app = FastAPI(title="MARVIN Mobile Gateway", version=GATEWAY_VERSION, docs_url=None, redoc_url=None,
                  openapi_url=None)

    @app.middleware("http")
    async def headers(request: Request, call_next):
        response = await call_next(request)
        response.headers["Cache-Control"] = "no-store"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["Referrer-Policy"] = "no-referrer"
        return response

    @app.exception_handler(RequestValidationError)
    async def invalid(request, exc):
        first = exc.errors()[0] if exc.errors() else {}
        field = ".".join(str(p) for p in first.get("loc", [])[1:]) or "pedido"
        return error(422, "invalid_request", f"Campo inválido: {field}.")

    @app.exception_handler(HTTPException)
    async def http_error(request, exc):
        codes = {401: "unauthorized", 404: "not_found", 413: "payload_too_large", 405: "method_not_allowed"}
        return error(exc.status_code, codes.get(exc.status_code, "http_error"), str(exc.detail))

    @app.exception_handler(PairingError)
    async def pairing_error(request, exc):
        return error(exc.status, exc.code, str(exc))

    @app.exception_handler(CommandError)
    async def command_error(request, exc):
        return error(exc.status, exc.code, str(exc), **exc.extra)

    @app.exception_handler(UploadError)
    async def upload_error(request, exc):
        return error(exc.status, exc.code, str(exc))

    @app.exception_handler(VaultUnavailable)
    async def vault_unavailable(request, exc):
        return error(503, exc.code, str(exc))

    @app.exception_handler(VaultError)
    async def vault_error(request, exc):
        status = exc.status if exc.status in {400, 404, 409, 413, 415, 422} else 502
        return error(status, "vault_error", str(exc))

    @app.exception_handler(SpeechUnavailable)
    async def speech_unavailable(request, exc):
        return error(503, "speech_unavailable", str(exc))

    @app.exception_handler(ConflictError)
    async def conflict(request, exc):
        return error(409, "conflict", str(exc))

    @app.exception_handler(ItemConflict)
    async def item_conflict(request, exc):
        return error(409, "revision_conflict", "O item foi alterado em outro dispositivo.", server_item=exc.server_item)

    @app.exception_handler(ValueError)
    async def value_error(request, exc):
        return error(400, "invalid_request", str(exc)[:300])

    @app.exception_handler(FileNotFoundError)
    async def missing(request, exc):
        return error(404, "not_found", str(exc)[:300] or "Não encontrado.")

    @app.exception_handler(RuntimeError)
    async def runtime_error(request, exc):
        return error(503, "unavailable", str(exc)[:300])

    def device(authorization: str = Header(default="")) -> dict:
        scheme, _, token = authorization.partition(" ")
        found = gateway.pairing.authenticate(token.strip()) if scheme.lower() == "bearer" else None
        if found is None:
            raise HTTPException(401, "Dispositivo não vinculado ou acesso revogado.")
        return found

    def server_info() -> dict:
        return {"server_id": gateway.server_id, "name": gateway.config.server_name, "version": GATEWAY_VERSION,
                "api_version": API_VERSION}

    # ---- public ---------------------------------------------------------------
    @app.get("/v1/health")
    def health():
        return {"ok": True, "service": "marvin-gateway", "server_time": iso(), **server_info()}

    @app.post("/v1/pair", status_code=201)
    def pair(body: PairIn):
        result = gateway.pairing.pair(body.code, body.device_name.strip(), body.platform, body.app_version)
        gateway.events.publish("device.paired", {"device_id": result["device_id"], "name": body.device_name.strip()[:80]})
        return {**result, "server": server_info()}

    # ---- session & devices -----------------------------------------------------
    @app.get("/v1/session")
    def session(me: dict = Depends(device)):
        return {"device": {k: me[k] for k in ("id", "name", "platform", "created_at")}, "server": server_info(),
                "server_time": iso()}

    @app.get("/v1/devices")
    def devices(me: dict = Depends(device)):
        return [{**d, "current": d["id"] == me["id"]} for d in gateway.pairing.devices()]

    @app.delete("/v1/devices/{device_id}", status_code=204)
    def revoke(device_id: str, me: dict = Depends(device)):
        target = me["id"] if device_id == "self" else device_id
        if not gateway.pairing.revoke(target):
            raise FileNotFoundError("Dispositivo não encontrado ou já revogado.")
        gateway.events.publish("device.revoked", {"device_id": target})
        return Response(status_code=204)

    @app.get("/v1/capabilities")
    def capabilities(me: dict = Depends(device)):
        return {"api_version": API_VERSION, "server": server_info(),
                "events": {"transport": "long-poll", "max_wait_seconds": MAX_WAIT},
                "conversation": {"engines": gateway.assistant.engines(), "cancel": True, "history": True,
                                 "streaming": False, "approvals": True},
                "memories": {"backend": "marvin-vault", "search": "text", "origins": ["user_request", "assistant_inference", "imported"]},
                "documents": {"formats": list(SUPPORTED_EXTENSIONS), "max_bytes": MAX_FILE_BYTES, "ocr": False,
                              "async_indexing": True, "document_scoped_ask": "category",
                              "llm_answers": "ollama-local-in-vault"},
                "items": {"kinds": ["task", "reminder", "note"]},
                "desktop": {"online": gateway.desktop.online(), "actions": gateway.desktop.catalog()},
                "speech": {"voices": gateway.speech.voices()}}

    @app.get("/v1/status")
    def status(me: dict = Depends(device)):
        presence = gateway.presence
        assistant = {"state": "unavailable", "reason": "Runtime do MARVIN inativo."}
        if presence is not None:
            alive = bool(presence.worker and presence.worker.is_alive())
            assistant = {"state": ("busy" if presence.busy else "ok") if alive else "unavailable",
                         "queue": presence.jobs.qsize(), "phase": presence.phase,
                         "reason": None if alive else "Fila do MARVIN parada."}
        desktop = {"state": "online" if gateway.desktop.online() else "offline",
                   "reason": None if gateway.desktop.online() else
                   ("Ações no PC desativadas (MARVIN_MOBILE_DESKTOP_ACTIONS=false)." if not gateway.config.desktop_actions
                    else "Agente do computador inativo.")}
        return {"server_time": iso(), "gateway": {"state": "ok", **server_info()}, "assistant": assistant,
                "vault": gateway.vault.status(), "desktop_agent": desktop,
                "approval_pending": gateway.assistant.approval() is not None}

    # ---- events ----------------------------------------------------------------
    @app.get("/v1/events")
    async def events(after: int = Query(0, ge=0), wait: int = Query(MAX_WAIT, ge=0, le=MAX_WAIT),
                     me: dict = Depends(device)):
        deadline = time.monotonic() + wait
        while True:
            batch = gateway.events.since(after, me["id"])
            if batch["events"] or batch["reset"] or time.monotonic() >= deadline:
                return {**batch, "server_time": iso()}
            await asyncio.sleep(0.3)

    # ---- conversation ------------------------------------------------------------
    @app.post("/v1/conversation/messages", status_code=202)
    def send_message(body: MessageIn, me: dict = Depends(device)):
        return gateway.assistant.submit(me["id"], body.client_id, body.text, body.engine)

    @app.get("/v1/conversation/history")
    def history(after_id: int = Query(0, ge=0), limit: int = Query(100, ge=1, le=500), me: dict = Depends(device)):
        return gateway.assistant.history(after_id, limit)

    @app.get("/v1/assistant/tasks")
    def assistant_tasks(limit: int = Query(50, ge=1, le=200), me: dict = Depends(device)):
        return gateway.assistant.tasks(limit)

    @app.get("/v1/assistant/tasks/{task_id}")
    async def assistant_task(task_id: str, wait: int = Query(0, ge=0, le=MAX_WAIT), me: dict = Depends(device)):
        deadline = time.monotonic() + wait
        while True:
            task = gateway.assistant.task(task_id)
            if task is None:
                raise FileNotFoundError("Tarefa não encontrada.")
            if task["state"] in {"completed", "failed", "cancelled", "needs_reconciliation", "waiting_user"} \
                    or time.monotonic() >= deadline:
                return task
            await asyncio.sleep(0.4)

    @app.post("/v1/assistant/tasks/{task_id}/cancel")
    def cancel_task(task_id: str, me: dict = Depends(device)):
        return {"task_id": task_id, "state": gateway.assistant.cancel(task_id)}

    @app.get("/v1/approvals")
    def approvals(me: dict = Depends(device)):
        current = gateway.assistant.approval()
        return [current] if current else []

    @app.post("/v1/approvals/{approval_id}")
    def decide(approval_id: str, body: DecisionIn, me: dict = Depends(device)):
        gateway.assistant.decide(approval_id, body.accepted)
        return {"ok": True}

    # ---- memories ----------------------------------------------------------------
    @app.get("/v1/memories")
    def memories(q: str = Query("", max_length=200), me: dict = Depends(device)):
        return gateway.vault.list_memories(q=q) if q else gateway.vault.all_memories()

    @app.post("/v1/memories", status_code=201)
    def create_memory(body: MemoryIn, response: Response, me: dict = Depends(device)):
        memory, duplicate = gateway.vault.create_memory(content=body.content.strip(), category=body.category.strip(),
                                                        origin=body.origin, source=body.source, client_id=body.client_id,
                                                        device_id=me["id"])
        if duplicate:
            response.status_code = 200
        gateway.events.publish("memory.changed", {"id": memory["id"], "action": "created"})
        return {**memory, "duplicate": duplicate}

    @app.put("/v1/memories/{memory_id}")
    def update_memory(memory_id: str, body: MemoryUpdate, me: dict = Depends(device)):
        result, memory = gateway.vault.update_memory(memory_id, content=body.content.strip(),
                                                     category=body.category.strip(), origin=body.origin,
                                                     base_updated_at=body.base_updated_at)
        if result == "missing":
            raise FileNotFoundError("Memória não encontrada (pode ter sido excluída em outro dispositivo).")
        if result == "conflict":
            return error(409, "revision_conflict", "A memória foi alterada em outro dispositivo.", server_item=memory)
        gateway.events.publish("memory.changed", {"id": memory_id, "action": "updated"})
        return memory

    @app.delete("/v1/memories/{memory_id}", status_code=204)
    def delete_memory(memory_id: str, me: dict = Depends(device)):
        if gateway.vault.delete_memory(memory_id):
            gateway.events.publish("memory.changed", {"id": memory_id, "action": "deleted"})
        return Response(status_code=204)

    # ---- documents & knowledge -----------------------------------------------------
    @app.get("/v1/documents")
    def documents(me: dict = Depends(device)):
        return gateway.vault.list_documents()

    @app.post("/v1/documents", status_code=202)
    async def upload(response: Response, file: UploadFile = File(...), category: str = Form("geral"),
                     client_id: str = Form(...), me: dict = Depends(device)):
        raw = await file.read(MAX_FILE_BYTES + 1)
        record, duplicate = await asyncio.to_thread(gateway.documents.receive, me["id"], client_id,
                                                    file.filename or "", category, raw)
        if duplicate:
            response.status_code = 200
        return {**record, "duplicate": duplicate}

    @app.get("/v1/documents/uploads")
    def uploads(me: dict = Depends(device)):
        return gateway.documents.list()

    @app.get("/v1/documents/uploads/{upload_id}")
    def upload_state(upload_id: str, me: dict = Depends(device)):
        record = gateway.documents.get(upload_id)
        if record is None:
            raise FileNotFoundError("Envio não encontrado.")
        return record

    @app.delete("/v1/documents/{document_id}", status_code=204)
    def delete_document(document_id: str, x_confirm_delete: str = Header(default=""), me: dict = Depends(device)):
        if x_confirm_delete != "yes":
            return error(409, "confirmation_required", "Envie X-Confirm-Delete: yes para excluir.")
        if not gateway.vault.delete_document(document_id):
            raise FileNotFoundError("Documento não encontrado.")
        gateway.events.publish("document.deleted", {"document_id": document_id})
        return Response(status_code=204)

    @app.get("/v1/knowledge/search")
    def search(q: str = Query(min_length=2, max_length=600), document_id: str = Query("", max_length=64),
               category: str = Query("", max_length=64), top_k: int = Query(6, ge=1, le=20), me: dict = Depends(device)):
        return gateway.vault.search(q, category=category, top_k=top_k, document_id=document_id)

    @app.post("/v1/knowledge/ask")
    def ask(body: AskIn, me: dict = Depends(device)):
        return gateway.vault.ask(body.question, category=body.category, document_id=body.document_id or "")

    @app.get("/v1/knowledge/chunks/{chunk_id}")
    def chunk(chunk_id: str, me: dict = Depends(device)):
        found = gateway.vault.chunk(chunk_id)
        if found is None:
            raise FileNotFoundError("Trecho não encontrado.")
        return found

    # ---- personal items --------------------------------------------------------------
    @app.get("/v1/items")
    def items(since: str | None = Query(None, max_length=40), me: dict = Depends(device)):
        return {"items": gateway.items.list(since), "server_time": iso()}

    @app.put("/v1/items/{item_id}")
    def put_item(item_id: str, body: ItemIn, me: dict = Depends(device)):
        uuid.UUID(item_id)
        status, item = gateway.items.put(item_id, body.model_dump(exclude={"base_rev"}), body.base_rev, me["id"])
        if status != "unchanged":
            gateway.events.publish("item.changed", {"id": item_id, "rev": item["rev"], "by": me["id"]})
        return {"status": status, "item": item}

    # ---- desktop ------------------------------------------------------------------------
    @app.get("/v1/desktop/actions")
    def actions(me: dict = Depends(device)):
        return {"online": gateway.desktop.online(), "actions": gateway.desktop.catalog()}

    @app.post("/v1/desktop/commands", status_code=202)
    def command(body: CommandIn, response: Response, me: dict = Depends(device)):
        record, duplicate = gateway.desktop.submit(me["id"], body.command_id, body.action, body.params,
                                                   expires_at=body.expires_at, confirmed=body.confirmed)
        if duplicate:
            response.status_code = 200
        return {**record, "duplicate": duplicate}

    @app.get("/v1/desktop/commands")
    def commands(limit: int = Query(50, ge=1, le=200), me: dict = Depends(device)):
        return gateway.desktop.list(limit)

    @app.get("/v1/desktop/commands/{command_id}")
    def command_state(command_id: str, me: dict = Depends(device)):
        record = gateway.desktop.get(command_id)
        if record is None:
            raise FileNotFoundError("Comando não encontrado.")
        return record

    @app.post("/v1/desktop/commands/{command_id}/cancel")
    def cancel_command(command_id: str, me: dict = Depends(device)):
        return gateway.desktop.cancel(command_id)

    @app.get("/v1/desktop/reminders")
    def desktop_reminders(me: dict = Depends(device)):
        if gateway.presence is None:
            return []
        return gateway.presence.runtime.scheduler.list_reminders()

    # ---- speech -------------------------------------------------------------------------
    @app.get("/v1/voice/voices")
    def voices(me: dict = Depends(device)):
        return gateway.speech.voices()

    @app.post("/v1/voice/speech")
    def speech(body: SpeechIn, me: dict = Depends(device)):
        audio, media = gateway.speech.synthesize(body.text, body.voice, body.rate)
        return Response(content=audio, media_type=media)

    return BodyLimit(app)
