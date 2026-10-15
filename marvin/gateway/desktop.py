"""Structured commands from paired devices to this computer.

Every command has a client-generated ID (deduplication), an expiry in server
time, validated parameters and a recorded lifecycle:
received -> started -> completed | dispatched | failed, or expired / cancelled / rejected.
`dispatched` means Windows accepted the request but the result was not observed.
Nothing received before a restart is executed after it.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import timedelta
import queue
import re
import threading
from typing import Callable
from urllib.parse import urlsplit

from .events import EventLog
from .store import Store, dumps, iso, parse_iso, utc_now

MAX_TTL_SECONDS = 300
DEFAULT_TTL_SECONDS = 60
KNOWN_FOLDERS = ("downloads", "documentos", "area de trabalho", "imagens", "musicas", "videos")
FINAL = {"completed", "dispatched", "failed", "expired", "cancelled", "rejected", "needs_reconciliation"}


class CommandError(Exception):
    def __init__(self, code: str, message: str, status: int = 400, extra: dict | None = None):
        super().__init__(message)
        self.code, self.status, self.extra = code, status, extra or {}


@dataclass(frozen=True)
class Action:
    id: str
    label: str
    description: str
    params: dict = field(default_factory=dict)  # name -> {"type", "required", ...}
    confirm: bool = False
    risk: str = "low"  # low | destructive
    verifiable: bool = False
    preview: str = ""


CATALOG: dict[str, Action] = {a.id: a for a in [
    Action("open_browser", "Abrir o navegador", "Abre o navegador padrão no PC, opcionalmente em um endereço https.",
           {"url": {"type": "url", "required": False}}),
    Action("web_search", "Pesquisar no navegador", "Abre uma pesquisa do Google no navegador do PC.",
           {"query": {"type": "text", "required": True, "max": 200}}),
    Action("open_app", "Abrir aplicativo", "Abre um aplicativo instalado encontrado no Menu Iniciar.",
           {"name": {"type": "text", "required": True, "max": 80}}),
    Action("open_folder", "Abrir pasta", "Abre uma pasta conhecida do usuário no Explorador.",
           {"folder": {"type": "enum", "required": True, "values": list(KNOWN_FOLDERS)}}),
    Action("create_project_folder", "Criar pasta de projeto",
           "Cria uma pasta dentro do workspace de projetos do MARVIN (nunca fora dele).",
           {"name": {"type": "text", "required": True, "max": 80}}, verifiable=True),
    Action("list_windows", "Listar janelas abertas", "Lê os títulos das janelas abertas no PC.", verifiable=True),
    Action("volume", "Ajustar volume", "Aumenta, diminui ou silencia o som do PC.",
           {"direction": {"type": "enum", "required": True, "values": ["up", "down", "mute"]}}),
    Action("lock_screen", "Bloquear o computador", "Bloqueia a sessão do Windows (Win+L).", confirm=True,
           risk="destructive", preview="A sessão do Windows será bloqueada. Trabalhos abertos continuam em execução."),
    Action("shutdown", "Desligar o computador", "Pede ao Windows para desligar o PC (sem forçar o fechamento de apps).",
           confirm=True, risk="destructive",
           preview="O Windows vai desligar agora. Apps com trabalho não salvo podem impedir ou perder dados."),
    Action("continue_task", "Continuar tarefa do PC",
           "Pede ao MARVIN para revisar a última tarefa pendente; efeitos anteriores não são repetidos.",
           {"task_id": {"type": "text", "required": False, "max": 64}}),
]}

SAFE_TEXT = re.compile(r"^[^;&|<>`\r\n\x00]{1,200}$")


def validate(action_id: str, params: dict) -> dict:
    action = CATALOG.get(action_id)
    if action is None:
        raise CommandError("unknown_action", "Ação não disponível neste computador.", 422)
    if not isinstance(params, dict):
        raise CommandError("invalid_params", "Parâmetros devem ser um objeto.", 422)
    unknown = set(params) - set(action.params)
    if unknown:
        raise CommandError("invalid_params", "Parâmetro não aceito: " + ", ".join(sorted(unknown)), 422)
    clean = {}
    for name, rule in action.params.items():
        value = params.get(name)
        if value in (None, ""):
            if rule.get("required"):
                raise CommandError("invalid_params", f"Informe {name}.", 422)
            continue
        if not isinstance(value, str):
            raise CommandError("invalid_params", f"{name} deve ser texto.", 422)
        value = value.strip()
        if rule["type"] == "enum" and value not in rule["values"]:
            raise CommandError("invalid_params", f"Valor inválido para {name}.", 422)
        if rule["type"] == "text" and (len(value) > rule.get("max", 200) or not SAFE_TEXT.match(value)):
            raise CommandError("invalid_params", f"Texto inválido para {name}.", 422)
        if rule["type"] == "url":
            parts = urlsplit(value)
            if parts.scheme != "https" or not parts.hostname or len(value) > 500 or parts.username:
                raise CommandError("invalid_params", "Use um endereço https completo.", 422)
        clean[name] = value
    return clean


def _default_handlers(presence) -> dict[str, Callable[[dict], dict]]:
    """Real effects on this PC. Returned 'state' is completed only when observed."""
    def open_browser(p):
        import webbrowser
        webbrowser.open(p.get("url") or "https://www.google.com")
        return {"state": "dispatched", "message": "Pedido enviado ao Windows para abrir o navegador."}

    def web_search(p):
        import webbrowser
        from urllib.parse import quote_plus
        webbrowser.open("https://www.google.com/search?q=" + quote_plus(p["query"]))
        return {"state": "dispatched", "message": "Pesquisa enviada ao navegador do PC."}

    def open_app(p):
        from ..windows_control import CATALOG as APPS
        return {"state": "dispatched", "message": APPS.launch(p["name"])}

    def open_folder(p):
        from ..windows_control import open_known_folder
        return {"state": "dispatched", "message": open_known_folder(p["folder"])}

    def create_project_folder(p):
        result = presence.workspace.create_project(p["name"])
        exists = bool(result.get("evidence", {}).get("exists"))
        verb = "já existia" if result.get("status") == "unchanged" else "foi criada"
        return {"state": "completed" if exists else "failed", "verified": exists,
                "message": f"A pasta {result['project']} {verb} em {result['directory']}.",
                "result": {"project": result["project"], "directory": result["directory"], "existed": result["status"] == "unchanged"}}

    def list_windows(p):
        from ..windows_control import desktop_action
        return {"state": "completed", "verified": True, "message": desktop_action("list-windows")}

    def volume(p):
        from ..windows_control import desktop_action
        desktop_action({"up": "volume-up", "down": "volume-down", "mute": "volume-mute"}[p["direction"]])
        return {"state": "dispatched", "message": "Comando de volume enviado ao Windows."}

    def lock_screen(p):
        from ..windows_control import desktop_action
        desktop_action("lock")
        return {"state": "dispatched", "message": "Pedido de bloqueio enviado ao Windows."}

    def shutdown(p):
        from ..power import shutdown_computer
        return {"state": "dispatched", "message": shutdown_computer()}

    def continue_task(p):
        submitted = presence.submit("continue a última tarefa", origin="mobile")
        return {"state": "completed", "verified": True, "message": "Pedido de continuação registrado no MARVIN do PC.",
                "result": {"assistant_task_id": submitted.get("task_id")}}

    return {"open_browser": open_browser, "web_search": web_search, "open_app": open_app,
            "open_folder": open_folder, "create_project_folder": create_project_folder,
            "list_windows": list_windows, "volume": volume, "lock_screen": lock_screen,
            "shutdown": shutdown, "continue_task": continue_task}


class DesktopAgent:
    def __init__(self, store: Store, events: EventLog, presence=None, *, enabled: bool = True,
                 handlers: dict[str, Callable[[dict], dict]] | None = None):
        self.store, self.events, self.presence = store, events, presence
        self.enabled = enabled and presence is not None
        self.handlers = handlers if handlers is not None else (_default_handlers(presence) if presence else {})
        self.queue: queue.Queue[str] = queue.Queue()
        self.stop = threading.Event()
        self.thread: threading.Thread | None = None
        self.last_heartbeat = utc_now()
        self._reconcile_after_restart()

    def _reconcile_after_restart(self) -> None:
        now = iso()
        self.store.execute("UPDATE commands SET state='expired', message='O gateway reiniciou antes da execução; nada foi executado.',"
                           " finished_at=?, updated_at=? WHERE state IN ('received', 'awaiting_confirmation')", (now, now))
        self.store.execute("UPDATE commands SET state='needs_reconciliation', message='O gateway reiniciou durante a execução;"
                           " confira o resultado no PC.', finished_at=?, updated_at=? WHERE state='started'", (now, now))

    def start(self) -> None:
        if self.enabled and self.thread is None:
            self.thread = threading.Thread(target=self._loop, daemon=True, name="MARVIN-mobile-desktop")
            self.thread.start()

    def close(self) -> None:
        self.stop.set()

    def online(self) -> bool:
        return self.enabled and self.thread is not None and self.thread.is_alive()

    def catalog(self) -> list[dict]:
        return [{"id": a.id, "label": a.label, "description": a.description, "params": a.params,
                 "requires_confirmation": a.confirm, "risk": a.risk, "verifiable": a.verifiable,
                 "preview": a.preview, "available": self.online() and a.id in self.handlers} for a in CATALOG.values()]

    @staticmethod
    def public(row: dict) -> dict:
        import json
        return {"command_id": row["id"], "action": row["action"], "params": json.loads(row["params"]),
                "state": row["state"], "message": row["message"], "verified": bool(row["verified"]),
                "result": json.loads(row["result"]) if row["result"] else None, "created_at": row["created_at"],
                "expires_at": row["expires_at"], "started_at": row["started_at"], "finished_at": row["finished_at"],
                "updated_at": row["updated_at"]}

    def get(self, command_id: str) -> dict | None:
        row = self.store.one("SELECT * FROM commands WHERE id=?", (command_id,))
        return self.public(row) if row else None

    def list(self, limit: int = 50) -> list[dict]:
        return [self.public(r) for r in self.store.all("SELECT * FROM commands ORDER BY created_at DESC LIMIT ?",
                                                        (min(max(limit, 1), 200),))]

    def submit(self, device_id: str, command_id: str, action_id: str, params: dict, *,
               expires_at: str | None, confirmed: bool) -> tuple[dict, bool]:
        if not re.fullmatch(r"[A-Za-z0-9_-]{8,64}", command_id or ""):
            raise CommandError("invalid_command_id", "Identificador de comando inválido.", 422)
        clean = validate(action_id, params)
        existing = self.store.one("SELECT * FROM commands WHERE id=?", (command_id,))
        if existing:
            if existing["action"] != action_id or existing["params"] != dumps(clean) or existing["device_id"] != device_id:
                raise CommandError("command_id_reused", "Identificador já usado por outro comando.", 409)
            return self.public(existing), True
        if not self.online():
            raise CommandError("desktop_offline", "O agente do computador não está ativo.", 503)
        action = CATALOG[action_id]
        if action.confirm and not confirmed:
            raise CommandError("confirmation_required", "Esta ação exige sua confirmação explícita.", 428,
                               {"preview": {"title": action.label, "description": action.preview, "risk": action.risk}})
        now = utc_now()
        if expires_at:
            try:
                expiry = parse_iso(expires_at)
            except ValueError:
                raise CommandError("invalid_expiry", "Validade inválida.", 422) from None
            if expiry <= now:
                raise CommandError("expired", "O comando perdeu a validade antes de chegar ao PC. Confirme novamente.", 410)
            if expiry > now + timedelta(seconds=MAX_TTL_SECONDS + 5):
                raise CommandError("invalid_expiry", "Validade máxima de 5 minutos.", 422)
        else:
            expiry = now + timedelta(seconds=DEFAULT_TTL_SECONDS)
        stamp = iso(now)
        self.store.execute("INSERT INTO commands(id, device_id, action, params, state, message, created_at, expires_at, updated_at)"
                           " VALUES (?, ?, ?, ?, 'received', 'Pedido recebido pelo PC.', ?, ?, ?)",
                           (command_id, device_id, action_id, dumps(clean), stamp, iso(expiry), stamp))
        record = self.get(command_id)
        self.events.publish("desktop.command", record)
        self.queue.put(command_id)
        return record, False

    def cancel(self, command_id: str) -> dict:
        now = iso()
        changed = self.store.execute("UPDATE commands SET state='cancelled', message='Cancelado antes de iniciar.',"
                                     " finished_at=?, updated_at=? WHERE id=? AND state='received'", (now, now, command_id))
        record = self.get(command_id)
        if record is None:
            raise CommandError("not_found", "Comando não encontrado.", 404)
        if changed:
            self.events.publish("desktop.command", record)
        return record

    def _transition(self, command_id: str, state: str, message: str, **extra) -> dict:
        now = iso()
        sets, args = ["state=?", "message=?", "updated_at=?"], [state, message[:2000], now]
        if state == "started":
            sets.append("started_at=?")
            args.append(now)
        if state in FINAL:
            sets.append("finished_at=?")
            args.append(now)
        if "result" in extra and extra["result"] is not None:
            sets.append("result=?")
            args.append(dumps(extra["result"]))
        if extra.get("verified"):
            sets.append("verified=1")
        self.store.execute(f"UPDATE commands SET {', '.join(sets)} WHERE id=?", (*args, command_id))
        record = self.get(command_id)
        self.events.publish("desktop.command", record)
        return record

    def _loop(self) -> None:
        while not self.stop.is_set():
            self.last_heartbeat = utc_now()
            try:
                command_id = self.queue.get(timeout=1)
            except queue.Empty:
                continue
            try:
                self.execute(command_id)
            except Exception:  # noqa: BLE001 - recorded on the command, never retried
                self._transition(command_id, "failed", "Falha interna ao executar o comando.")

    def execute(self, command_id: str) -> dict | None:
        row = self.store.one("SELECT * FROM commands WHERE id=?", (command_id,))
        if row is None or row["state"] != "received":
            return None
        expiry = parse_iso(row["expires_at"])
        lock = getattr(getattr(self.presence, "runtime", None), "desktop_lock", None)
        remaining = (expiry - utc_now()).total_seconds()
        acquired = remaining > 0 and (lock.acquire(timeout=remaining) if lock else True)
        if not acquired:
            return self._transition(command_id, "expired", "O PC estava ocupado e o comando perdeu a validade. Nada foi executado.")
        try:
            current = self.store.one("SELECT state FROM commands WHERE id=?", (command_id,))
            if current["state"] != "received":
                return None
            if utc_now() >= expiry:
                return self._transition(command_id, "expired", "O comando perdeu a validade. Nada foi executado.")
            import json
            self._transition(command_id, "started", "Execução iniciada no PC.")
            handler = self.handlers.get(row["action"])
            if handler is None:
                return self._transition(command_id, "rejected", "Ação não disponível neste computador.")
            try:
                outcome = handler(json.loads(row["params"]))
            except (ValueError, FileNotFoundError, PermissionError, RuntimeError, OSError) as exc:
                return self._transition(command_id, "failed", str(exc)[:500] or type(exc).__name__)
            return self._transition(command_id, outcome.get("state", "dispatched"), outcome.get("message", ""),
                                    result=outcome.get("result"), verified=outcome.get("verified", False))
        finally:
            if lock:
                lock.release()
