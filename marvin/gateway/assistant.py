"""Conversation engines exposed to devices.

`marvin`: the Presence Runtime (same queue, tools, approvals and provider as the PC).
`ollama`: optional plain chat with a model served by Ollama on this PC, without tools.
The engine list reports availability and whether a model is local or remote.
"""
from __future__ import annotations

import hashlib
import json
import threading
import uuid
from urllib.error import URLError
from urllib.request import ProxyHandler, Request, build_opener

from .events import EventLog
from .store import Store, iso

TERMINAL = {"completed", "failed", "cancelled", "needs_reconciliation", "waiting_user"}
OLLAMA_SYSTEM = ("Você é o MARVIN, assistente pessoal do João. Responda em português do Brasil, com clareza e "
                 "brevidade, em texto que possa ser lido em voz alta. Neste modo você não executa ações nem "
                 "acessa arquivos; se pedirem uma ação, diga que ela precisa do MARVIN completo no PC.")


class ConflictError(Exception):
    pass


def fingerprint(*parts: str) -> str:
    return hashlib.sha256("\x1f".join(parts).encode("utf-8")).hexdigest()


class AssistantService:
    def __init__(self, presence, store: Store, events: EventLog, *, ollama_url: str, ollama_model: str = ""):
        self.presence, self.store, self.events = presence, store, events
        self.ollama_url, self.ollama_model = ollama_url.rstrip("/"), ollama_model
        self._opener = build_opener(ProxyHandler({}))
        self._cancelled: set[str] = set()
        if presence is not None:
            presence.listeners.append(self._on_presence_event)

    # ---- engines --------------------------------------------------------------
    def _ollama_models(self) -> list[dict]:
        try:
            with self._opener.open(Request(self.ollama_url + "/api/tags"), timeout=2) as response:
                data = json.loads(response.read(500_000))
        except (URLError, OSError, ValueError):
            return []
        return [{"name": m.get("name", ""), "remote": bool(m.get("remote_host")),
                 "remote_host": m.get("remote_host")} for m in data.get("models", []) if m.get("name")]

    def _ollama_choice(self) -> dict | None:
        models = self._ollama_models()
        if self.ollama_model:
            return next((m for m in models if m["name"] == self.ollama_model), None)
        local = [m for m in models if not m["remote"]]
        return (local or models or [None])[0]

    def engines(self) -> list[dict]:
        result = []
        if self.presence is not None:
            brain = self.presence.brain
            configured = bool(brain.api_key and brain.api_key != "COLE_SUA_CHAVE_AQUI")
            result.append({"id": "marvin", "label": "MARVIN do PC", "available": True,
                           "provider": brain.provider, "model": brain.configured_model, "llm_configured": configured,
                           "local_model": False, "tools": True,
                           "note": ("Comandos locais funcionam sem IA. Conversa livre usa " + brain.provider +
                                    (" com cota e limites da sua conta." if configured else ", mas a chave não está configurada no PC."))})
        choice = self._ollama_choice()
        result.append({"id": "ollama", "label": "Modelo via Ollama no PC", "available": choice is not None,
                       "provider": "ollama", "model": choice["name"] if choice else None,
                       "local_model": bool(choice and not choice["remote"]), "tools": False,
                       "note": ("Nenhum modelo no Ollama." if choice is None else
                                ("Modelo executado neste PC." if not choice["remote"] else
                                 "Modelo remoto (" + str(choice["remote_host"]) + "): sujeito a limites do serviço."))})
        return result

    # ---- submit ---------------------------------------------------------------
    def submit(self, device_id: str, client_id: str, text: str, engine: str = "marvin") -> dict:
        text = text.strip()
        digest = fingerprint(engine, text)
        previous = self.store.one("SELECT * FROM requests WHERE client_id=?", (client_id,))
        if previous:
            if previous["fingerprint"] != digest or previous["device_id"] != device_id:
                raise ConflictError("Este identificador de mensagem já foi usado com outro conteúdo.")
            return {"task_id": previous["ref"], "engine": engine, "duplicate": True, **self.task_state(previous["ref"])}
        if engine == "marvin":
            if self.presence is None:
                raise RuntimeError("O runtime do MARVIN não está ativo neste gateway.")
            submitted = self.presence.submit(text, origin="mobile")
            task_id = submitted["task_id"]
        elif engine == "ollama":
            choice = self._ollama_choice()
            if choice is None:
                raise RuntimeError("Nenhum modelo disponível no Ollama do PC.")
            task_id = "ol-" + uuid.uuid4().hex
            now = iso()
            self.store.execute("INSERT INTO jobs VALUES (?, ?, 'ollama', ?, 'queued', '', ?, ?)",
                               (task_id, device_id, text, now, now))
            threading.Thread(target=self._run_ollama, args=(task_id, text, choice["name"]), daemon=True,
                             name="MARVIN-ollama").start()
        else:
            raise ValueError("Motor de conversa desconhecido.")
        self.store.execute("INSERT INTO requests VALUES (?, ?, 'message', ?, ?, ?)",
                           (client_id, device_id, task_id, digest, iso()))
        return {"task_id": task_id, "engine": engine, "duplicate": False, "state": "queued"}

    def _run_ollama(self, job_id: str, text: str, model: str) -> None:
        self._set_job(job_id, "running")
        payload = {"model": model, "stream": False, "options": {"num_predict": 600},
                   "messages": [{"role": "system", "content": OLLAMA_SYSTEM}, {"role": "user", "content": text}]}
        try:
            request = Request(self.ollama_url + "/api/chat", data=json.dumps(payload).encode("utf-8"),
                              headers={"Content-Type": "application/json"}, method="POST")
            with self._opener.open(request, timeout=180) as response:
                answer = str(json.loads(response.read(2_000_000))["message"]["content"]).strip()
            state = "completed" if answer else "failed"
            answer = answer or "O modelo devolveu uma resposta vazia."
        except Exception as exc:  # noqa: BLE001 - reported to the device as a failure
            state, answer = "failed", "Não consegui consultar o modelo no Ollama: " + type(exc).__name__
        if job_id in self._cancelled:
            state, answer = "cancelled", "Cancelado. A resposta do modelo foi descartada."
        self._set_job(job_id, state, answer)
        self.events.publish("assistant.answer", {"task_id": job_id, "text": answer, "state": state,
                                                 "origin": "mobile", "engine": "ollama"})

    def _set_job(self, job_id: str, state: str, answer: str = "") -> None:
        self.store.execute("UPDATE jobs SET state=?, answer=?, updated_at=? WHERE id=?", (state, answer, iso(), job_id))
        self.events.publish("assistant.task", {"task_id": job_id, "state": state, "engine": "ollama"})

    # ---- tasks ----------------------------------------------------------------
    def task_state(self, task_id: str) -> dict:
        task = self.task(task_id)
        return {"state": task["state"]} if task else {"state": "unknown"}

    def task(self, task_id: str) -> dict | None:
        if task_id.startswith("ol-"):
            job = self.store.one("SELECT * FROM jobs WHERE id=?", (task_id,))
            if job is None:
                return None
            return {"id": job["id"], "engine": "ollama", "objective": job["text"], "state": job["state"],
                    "answer": job["answer"] or None, "created_at": job["created_at"], "updated_at": job["updated_at"],
                    "origin": "mobile", "steps": []}
        if self.presence is None:
            return None
        task = self.presence.runtime.tasks.get(task_id)
        if task is None:
            return None
        steps = [{"tool": s.get("tool"), "state": s.get("state"), "created_at": s.get("created_at"),
                  "finished_at": s.get("finished_at")} for s in self.presence.runtime.tasks.steps(task_id)]
        final = task["state"] in TERMINAL
        return {"id": task["id"], "engine": "marvin", "objective": task["objective"], "state": task["state"],
                "answer": task.get("message") if final else None, "created_at": task["created_at"],
                "updated_at": task["updated_at"], "origin": self._origin(task_id), "steps": steps}

    def _origin(self, task_id: str) -> str:
        return "mobile" if self.store.one("SELECT 1 FROM requests WHERE ref=?", (task_id,)) else "desktop"

    def tasks(self, limit: int = 50) -> list[dict]:
        items = []
        if self.presence is not None:
            mobile = {r["ref"] for r in self.store.all("SELECT ref FROM requests WHERE kind='message'")}
            for task in self.presence.runtime.tasks.list_tasks(limit):
                final = task["state"] in TERMINAL
                items.append({"id": task["id"], "engine": "marvin", "objective": task["objective"][:300],
                              "state": task["state"], "answer": (task.get("message") or "")[:600] if final else None,
                              "created_at": task["created_at"], "updated_at": task["updated_at"],
                              "origin": "mobile" if task["id"] in mobile else "desktop"})
        for job in self.store.all("SELECT * FROM jobs ORDER BY updated_at DESC LIMIT ?", (limit,)):
            items.append({"id": job["id"], "engine": "ollama", "objective": job["text"][:300], "state": job["state"],
                          "answer": job["answer"][:600] or None, "created_at": job["created_at"],
                          "updated_at": job["updated_at"], "origin": "mobile"})
        items.sort(key=lambda t: t["updated_at"], reverse=True)
        return items[:limit]

    def cancel(self, task_id: str) -> str:
        if task_id.startswith("ol-"):
            job = self.store.one("SELECT state FROM jobs WHERE id=?", (task_id,))
            if job is None:
                raise FileNotFoundError("Tarefa não encontrada.")
            if job["state"] in TERMINAL:
                return job["state"]
            # The HTTP call cannot be interrupted; its result is discarded.
            self._cancelled.add(task_id)
            return "cancelling"
        if self.presence is None:
            raise FileNotFoundError("Tarefa não encontrada.")
        return self.presence.cancel_task(task_id)

    def history(self, after_id: int = 0, limit: int = 100) -> list[dict]:
        if self.presence is None:
            return []
        return [{"id": m["id"], "role": "assistant" if m["role"] == "model" else "user", "text": m["content"],
                 "created_at": m["created_at"]} for m in self.presence.memory.messages_since(after_id, limit)]

    # ---- approvals ------------------------------------------------------------
    def approval(self) -> dict | None:
        if self.presence is None:
            return None
        with self.presence.guard:
            current = self.presence.approval
            return dict(current) if current else None

    def decide(self, approval_id: str, accepted: bool) -> None:
        self.presence.decide(approval_id, accepted)
        self.events.publish("approval.resolved", {"id": approval_id, "accepted": bool(accepted)})

    # ---- presence bridge ------------------------------------------------------
    def _on_presence_event(self, event: dict) -> None:
        kind = event.get("type", "")
        task_id = event.get("task_id")
        if kind == "answer":
            self.events.publish("assistant.answer", {"task_id": task_id, "text": event.get("message", ""),
                                                     "state": event.get("state"), "origin": event.get("origin", "desktop"),
                                                     "engine": "marvin"})
        elif kind in {"task.queued", "task.started", "task.paused", "task.cancelling", "task.pause_requested"}:
            self.events.publish("assistant.task", {"task_id": task_id, "state": kind.split(".", 1)[1], "engine": "marvin"})
        elif kind == "task.finished":
            self.events.publish("assistant.task", {"task_id": task_id, "state": event.get("state"), "engine": "marvin"})
        elif kind == "task.progress":
            self.events.publish("assistant.progress", {"task_id": task_id, "message": str(event.get("message", ""))[:300]})
        elif kind == "tool.requested":
            self.events.publish("assistant.progress", {"task_id": task_id, "tool": event.get("tool"), "phase": "executing"})
        elif kind == "task.error":
            self.events.publish("assistant.error", {"task_id": task_id, "message": str(event.get("message", ""))[:300]})
        elif kind == "approval.requested":
            approval = self.approval()
            if approval:
                self.events.publish("approval.requested", approval)
        elif kind == "reminder":
            self.events.publish("desktop.reminder", {"message": str(event.get("message", ""))[:500]})
