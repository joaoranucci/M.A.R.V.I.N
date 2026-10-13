"""UI-independent task coordinator. No microphone, Tk or model SDK on import."""
from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path
import re
import threading
import time

from .commands import detect, execute_local, normalize
from .task_store import TaskStore
from .scheduler import Scheduler


class TaskControl(threading.Event):
    """Cooperative cancellation and pause between steps; never promise rollback."""
    def __init__(self):
        super().__init__()
        self.paused = threading.Event()
        self.on_pause = None

    def wait_if_paused(self):
        if self.paused.is_set() and not self.is_set() and self.on_pause:
            self.on_pause()
        while self.paused.is_set() and not self.is_set():
            self.wait(0.1)
        return not self.is_set()


def request_text(text: str) -> str:
    return re.sub(r"^(?:(?:ei|hey|c|ce|se|ok|ola)\s+)?marvin[,:\s]*", "", text.strip(), flags=re.I).strip()


class Runtime:
    def __init__(self, memory, workspace, agent, emit=None, session_id="desktop", confirm_action=None):
        self.memory, self.workspace, self.agent = memory, workspace, agent
        self.session_id = session_id
        self.tasks = TaskStore(memory.db_path)
        self.scheduler = Scheduler(memory.db_path)
        self.agent.task_store = self.tasks
        self.emit = emit or (lambda event: None)
        self.confirm_action = confirm_action or (lambda description: False)
        self.desktop_lock = threading.Lock()
        self._control_lock = threading.RLock()
        self.active_id = None
        self.control = None
        self.recovered = self.tasks.recover_interrupted()

    def event(self, kind, task_id=None, **payload):
        event = {"type": kind, "task_id": task_id, "session_id": self.session_id,
                 "time": datetime.now(timezone.utc).isoformat(), "origin": "runtime", "payload": payload}
        try:
            self.emit(event)
        except Exception:
            # An observer failure must never cause replay of a completed effect.
            pass

    def prepare(self, question):
        if not question.strip() or len(question) > 12000:
            raise ValueError("Use um pedido de 1 a 12.000 caracteres.")
        task = self.tasks.create(question, session_id=self.session_id,
                                 scope={"workspace": str(self.workspace.root)})
        self.event("task.queued", task["id"], objective=question)
        return task

    def cancel(self):
        if self.control:
            self.control.set()
            self.event("task.cancelling", self.active_id)

    def pause(self):
        with self._control_lock:
            if self.control and self.active_id and not self.control.is_set():
                task = self.tasks.get(self.active_id)
                if task and task["state"] == "running":
                    self.control.paused.set()
                    self.event("task.pause_requested", self.active_id)

    def _mark_paused(self):
        with self._control_lock:
            if self.active_id and self.control and self.control.paused.is_set():
                self.tasks.set_state(self.active_id, "paused", "Pausado em um checkpoint entre etapas.")
                self.event("task.paused", self.active_id)

    def resume(self):
        with self._control_lock:
            if self.control and self.active_id and self.control.paused.is_set() and not self.control.is_set():
                task = self.tasks.get(self.active_id)
                if task and task["state"] in {"paused", "running"}:
                    self.tasks.set_state(self.active_id, "running", "Execução retomada.")
                    self.control.paused.clear()
                    self.event("task.started", self.active_id)

    def describe_tasks(self):
        items = self.tasks.list_tasks(limit=15)
        return "\n".join(f"{t['id'][:8]} · {t['state']} · {t['objective'][:130]}" for t in items) or "Nenhuma tarefa registrada."

    def status(self):
        if self.active_id:
            task = self.tasks.get(self.active_id)
            steps = self.tasks.steps(self.active_id)
            return f"Tarefa {task['id'][:8]}: {task['state']}. {len(steps)} etapa(s) registrada(s). Objetivo: {task['objective']}"
        return "Nenhuma tarefa em execução.\n" + self.describe_tasks()

    def _context(self):
        # Agent currently uses the default durable conversation context too.
        return self.memory.get_context()

    def _local(self, question):
        """Return (tool name, arguments, callable), or None for model assistance."""
        raw = request_text(question)
        n = normalize(raw)
        # Explanations, quoted commands and negation never become local effects.
        if re.match(r"^(explique|como |o que significa|nao |não |se eu |traduza|descreva)", n):
            return None
        if n in {"tarefas", "liste tarefas", "mostre minhas tarefas pendentes", "minhas tarefas", "status"}:
            return "list_tasks", {}, lambda: {"message": self.describe_tasks()}
        if n in {"liste projetos", "meus projetos", "mostre meus projetos"}:
            return "list_projects", {}, self.workspace.list_projects
        if n in {"o que voce lembra de mim", "o que voce lembra", "mostre memoria", "minha memoria"}:
            return "recall_facts", {}, lambda: {"message": "\n".join(self.memory.facts(50)) or "Nenhuma lembrança salva."}
        remember = re.match(r"^(?:lembre que|memorize que|guarde que)\s+(.+)$", raw, re.I)
        if remember:
            fact = remember.group(1).strip()
            return "remember_fact", {"fact": fact}, lambda: dict(self.memory.remember(fact), message="Lembrança salva: " + fact)
        forget = re.match(r"^(?:esqueça|esqueca|esquece)\s+(?:que\s+)?(.+)$", raw, re.I)
        if forget:
            fact = forget.group(1).strip()
            def remove():
                if fact not in self.memory.facts(100):
                    return {"status": "waiting_user", "message": "Informe a lembrança completa para excluir. Consulte MEMÓRIA."}
                self.memory.forget_fact(fact)
                return {"message": "Lembrança excluída."}
            return "forget_fact", {"fact": fact}, remove
        if re.match(r"^(?:(?:me )?lembre |(?:crie|agende) (?:um )?lembrete )", n):
            def add_reminder():
                try:
                    item = self.scheduler.parse_and_add(raw)
                    return {"message": f"Lembrete salvo para {item['due_local']}: {item['message']}. Funciona enquanto o MARVIN estiver aberto.", "reminder": item}
                except ValueError as exc:
                    return {"status": "waiting_user", "message": str(exc)}
            return "schedule_reminder", {"text": raw}, add_reminder
        if n in {"meus lembretes", "liste lembretes", "mostre meus lembretes"}:
            return "list_reminders", {}, lambda: {"message": json.dumps(self.scheduler.list_reminders(), ensure_ascii=False, indent=2)}
        if n.startswith("cancele lembrete "):
            reminder_id = raw.rsplit(" ", 1)[-1]
            def cancel_reminder():
                changed = self.scheduler.cancel(reminder_id)
                return {"ok": changed, "message": "Lembrete cancelado." if changed else "Nenhum lembrete pendente com esse ID."}
            return "cancel_reminder", {"id": reminder_id}, cancel_reminder
        if re.match(r"^(?:agora )?(?:abra|abre|abrir|verifique|verifica|valide)\b", n) and re.search(
                r"(?:ultimo projeto|esse projeto|este projeto|o resultado|projeto que (?:acabou|voce acabou) de criar)", n):
            ctx = self._context()
            project = ctx.get("project")
            if not project:
                return "resolve_project", {}, lambda: {"status": "waiting_user", "message": "Ainda não há projeto ativo. Informe o nome do projeto."}
            if re.search(r"\b(verifique|verifica|valide)\b", n):
                return "verify_project", {"project": project}, lambda: self.workspace.verify_project(project)
            relative = ctx.get("file", "") if "resultado" in n else ""
            return "open_project", {"project": project, "path": relative}, lambda: self.workspace.open_project(project, relative)
        # 'Abra o projeto X' is not an application called 'projeto X'.
        opened = re.fullmatch(r"(?:abra|abre|abrir) (?:o )?projeto (.+)", raw, re.I)
        if opened:
            project = opened.group(1).strip()
            def open_it():
                result = self.workspace.open_project(project)
                self.memory.set_context({"project": project, "file": None})
                return result
            return "open_project", {"project": project}, open_it
        if n in {"continue", "continue a tarefa de ontem", "continue a ultima tarefa"}:
            pending = [t for t in self.tasks.list_tasks(limit=20) if t["id"] != self.active_id and t["state"] in {"failed", "paused", "needs_reconciliation", "waiting_user", "queued"}]
            if pending:
                chosen = pending[0]
                details = self.tasks.steps(chosen["id"])
                return "recovery_review", {"task": chosen["id"]}, lambda: {
                    "status": "waiting_user", "message": "A tarefa anterior precisa de revisão antes de novas ações: " + chosen["objective"] + "\nEtapas preservadas:\n" + json.dumps(details, ensure_ascii=False, default=str)[:5000] + "\nDescreva a próxima etapa desejada; os efeitos anteriores não serão repetidos automaticamente."}
        action = detect(question)
        if action.kind == "local":
            def local_command():
                if action.value in {"desktop:close", "desktop:lock"}:
                    label = "Fechar a janela ativa? Alterações não salvas podem ser perdidas." if action.value.endswith("close") else "Bloquear o computador?"
                    if not self.confirm_action(label):
                        return {"ok": False, "status": "waiting_user", "message": "Ação não autorizada; nada foi executado."}
                answer = execute_local(action.value)
                observed = action.value in {"relogio", "list-apps", "refresh-apps", "desktop:list-windows"}
                return {"ok": True, "message": answer, "status": "succeeded" if observed else "requested"}
            return "windows_command", {"value": action.value}, local_command
        return None

    def run(self, question, task_id=None, control=None):
        question = question.strip()
        task_id = task_id or self.prepare(question)["id"]
        token = control if control is not None else TaskControl()
        stored = self.tasks.get(task_id)
        if not stored or stored["objective"] != question:
            raise ValueError("ID de tarefa não corresponde ao objetivo solicitado.")
        if stored["state"] != "queued":
            return {"task_id": task_id, "state": stored["state"], "answer": stored.get("message") or "Tarefa já registrada; use TAREFAS para revisar antes de criar uma continuação."}
        with self.desktop_lock:
            # Another invocation may have completed while this caller waited.
            stored = self.tasks.get(task_id)
            if stored["state"] != "queued":
                return {"task_id": task_id, "state": stored["state"], "answer": stored.get("message") or "Tarefa já processada; revise antes de continuar."}
            self.active_id, self.control = task_id, token
            token.on_pause = self._mark_paused
            started = time.monotonic()
            self.tasks.set_state(task_id, "running")
            self.event("task.started", task_id)
            outcome = "failed"
            try:
                if not token.wait_if_paused():
                    outcome, answer = "cancelled", "Cancelado antes de executar."
                else:
                    local = self._local(question)
                    if local:
                        name, args, fn = local
                        if not token.wait_if_paused():
                            from .brain import RequestCancelled
                            raise RequestCancelled("Cancelado antes da etapa local.")
                        step = self.tasks.begin_step(task_id, "local:1", name, args)
                        if not step.get("created", False):
                            outcome, answer = "needs_reconciliation", "Essa etapa já foi registrada. Confira o resultado em TAREFAS antes de repetir."
                        else:
                            self.event("tool.requested", task_id, tool=name)
                            try:
                                if not token.wait_if_paused():
                                    result = {"ok": False, "status": "cancelled", "message": "Cancelado antes da ação."}
                                else:
                                    result = fn()
                            except Exception as exc:
                                result = {"ok": False, "status": "failed", "message": f"{type(exc).__name__}: {str(exc)[:400]}"}
                            result.setdefault("ok", result.get("status") != "waiting_user")
                            if result.get("status") == "requested":
                                result["status"] = "needs_reconciliation"
                                result.setdefault("message", "Solicitação enviada ao sistema. Confira o resultado na tela.")
                            self.tasks.finish_step(task_id, "local:1", result)
                            self.event("tool.finished", task_id, tool=name, ok=result.get("ok", True))
                            answer = result.get("message") or json.dumps(result, ensure_ascii=False, indent=2)
                            outcome = ("needs_reconciliation" if result.get("status") == "needs_reconciliation" else
                                       "waiting_user" if result.get("status") == "waiting_user" else
                                       "failed" if result.get("ok") is False else "completed")
                            self.memory.add_pair(question, answer)
                    else:
                        answer = self.agent.assist(question, notify=lambda message: self.event("task.progress", task_id, message=message),
                                                   task_id=task_id, cancel_event=token)
                        outcome = getattr(self.agent, "last_outcome", "failed")
                if token.is_set():
                    outcome = "cancelled"
                    answer = "Cancelado. Efeitos já realizados estão em TAREFAS.\n" + answer
            except Exception as exc:
                from .brain import friendly_error
                answer = "Não concluí a tarefa. " + friendly_error(exc)
                outcome = "cancelled" if token.is_set() else "failed"
            finally:
                try:
                    with self._control_lock:
                        try:
                            self.tasks.set_state(task_id, outcome, answer if 'answer' in locals() else "Falha interna.")
                        except ValueError:
                            outcome = "failed"
                            answer = "Há etapas pendentes ou com falha. Revise TAREFAS.\n" + answer
                            self.tasks.set_state(task_id, outcome, answer)
                    self.memory.set_context({"last_task_id": task_id})
                    self.event("task.finished", task_id, state=outcome, duration_ms=int((time.monotonic()-started)*1000))
                finally:
                    self.active_id, self.control = None, None
                    token.on_pause = None
            return {"task_id": task_id, "state": outcome, "answer": answer}
