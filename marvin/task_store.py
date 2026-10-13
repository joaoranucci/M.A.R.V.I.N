"""Persistent task checkpoints and an intent-before-effect execution ledger.

The caller must use a stable step_id for retries. A returned ``created=False``
never permits executing the effect again. Interrupted effects require external
reconciliation; exactly-once delivery cannot be promised for desktop actions.
"""
from __future__ import annotations

import json
from pathlib import Path
import uuid

from .memory import connect, migrate, utc_now


STATES = frozenset({"queued", "running", "waiting_user", "paused", "completed", "failed", "cancelled", "needs_reconciliation"})


def _json(value) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, allow_nan=False)
    if len(payload.encode("utf-8")) > 1024 * 1024:
        raise ValueError("Registro excede 1 MiB; persista referências aos artefatos maiores.")
    return payload


def _task(row) -> dict | None:
    if row is None:
        return None
    data = dict(row)
    data["scope"] = json.loads(data["scope"])
    return data


def _step(row, *, created: bool = False) -> dict:
    data = dict(row)
    data["args"] = json.loads(data["args"])
    data["result"] = json.loads(data["result"]) if data["result"] is not None else None
    data["created"] = created
    return data


class TaskStore:
    def __init__(self, db_path: Path):
        self.db_path = Path(db_path)
        migrate(self.db_path, "tasks", 1, (
            "CREATE TABLE IF NOT EXISTS tasks (id TEXT PRIMARY KEY, session_id TEXT NOT NULL, objective TEXT NOT NULL, scope TEXT NOT NULL, state TEXT NOT NULL, message TEXT NOT NULL DEFAULT '', created_at TEXT NOT NULL, updated_at TEXT NOT NULL)",
            "CREATE TABLE IF NOT EXISTS task_steps (id TEXT PRIMARY KEY, task_id TEXT NOT NULL REFERENCES tasks(id), step_id TEXT NOT NULL, tool TEXT NOT NULL, args TEXT NOT NULL, state TEXT NOT NULL, result TEXT, created_at TEXT NOT NULL, finished_at TEXT, UNIQUE(task_id, step_id))",
            "CREATE TABLE IF NOT EXISTS task_events (id INTEGER PRIMARY KEY AUTOINCREMENT, task_id TEXT NOT NULL REFERENCES tasks(id), state TEXT NOT NULL, message TEXT NOT NULL, created_at TEXT NOT NULL)",
            "CREATE INDEX IF NOT EXISTS task_state_idx ON tasks(state, updated_at)",
        ))

    def create(self, objective: str, session_id: str = "default", scope=None) -> dict:
        objective = str(objective).strip()
        if not objective or len(objective) > 20000:
            raise ValueError("Objetivo deve ter entre 1 e 20.000 caracteres.")
        task_id, now = uuid.uuid4().hex, utc_now()
        with connect(self.db_path) as connection:
            connection.execute("INSERT INTO tasks VALUES (?, ?, ?, ?, 'queued', '', ?, ?)", (task_id, session_id, objective, _json(scope or {}), now, now))
            connection.execute("INSERT INTO task_events(task_id, state, message, created_at) VALUES (?, 'queued', '', ?)", (task_id, now))
            return _task(connection.execute("SELECT * FROM tasks WHERE id=?", (task_id,)).fetchone())

    def get(self, task_id: str) -> dict | None:
        with connect(self.db_path) as connection:
            return _task(connection.execute("SELECT * FROM tasks WHERE id=?", (task_id,)).fetchone())

    def list_tasks(self, limit: int = 20) -> list[dict]:
        with connect(self.db_path) as connection:
            return [_task(row) for row in connection.execute("SELECT * FROM tasks ORDER BY updated_at DESC LIMIT ?", (min(max(int(limit), 1), 1000),))]

    def set_state(self, task_id: str, state: str, message: str = "") -> dict:
        if state not in STATES:
            raise ValueError(f"Estado de tarefa inválido: {state}")
        with connect(self.db_path) as connection:
            connection.execute("BEGIN IMMEDIATE")
            task = connection.execute("SELECT * FROM tasks WHERE id=?", (task_id,)).fetchone()
            if task is None:
                raise KeyError(task_id)
            if task["state"] in {"completed", "cancelled"} and state != task["state"]:
                raise ValueError("Uma tarefa concluída/cancelada é imutável; crie outra tarefa.")
            pending = connection.execute("SELECT state FROM task_steps WHERE task_id=? AND state <> 'completed'", (task_id,)).fetchall()
            if state == "completed" and pending:
                raise ValueError("A tarefa ainda possui etapas com falha ou efeito incerto.")
            if state == "running" and any(row[0] == "needs_reconciliation" for row in pending):
                raise ValueError("Reconcilie as etapas incertas antes de continuar.")
            now = utc_now()
            connection.execute("UPDATE tasks SET state=?, message=?, updated_at=? WHERE id=?", (state, str(message)[:20000], now, task_id))
            connection.execute("INSERT INTO task_events(task_id, state, message, created_at) VALUES (?, ?, ?, ?)", (task_id, state, str(message)[:20000], now))
            return _task(connection.execute("SELECT * FROM tasks WHERE id=?", (task_id,)).fetchone())

    def begin_step(self, task_id: str, step_id: str, tool: str, args: dict) -> dict:
        if not step_id or not tool or not isinstance(args, dict):
            raise ValueError("Uma etapa exige ID estável, ferramenta e argumentos em objeto.")
        encoded = _json(args)
        with connect(self.db_path) as connection:
            connection.execute("BEGIN IMMEDIATE")
            existing = connection.execute("SELECT * FROM task_steps WHERE task_id=? AND step_id=?", (task_id, step_id)).fetchone()
            if existing:
                if existing["tool"] != tool or existing["args"] != encoded:
                    raise ValueError("ID de etapa reutilizado com ferramenta ou argumentos diferentes.")
                return _step(existing)
            task = connection.execute("SELECT state FROM tasks WHERE id=?", (task_id,)).fetchone()
            if task is None:
                raise KeyError(task_id)
            if task[0] not in {"queued", "running"}:
                raise ValueError(f"A tarefa está {task[0]}; novos passos não estão autorizados.")
            now = utc_now()
            connection.execute("INSERT INTO task_steps VALUES (?, ?, ?, ?, ?, 'running', NULL, ?, NULL)", (uuid.uuid4().hex, task_id, str(step_id), str(tool), encoded, now))
            connection.execute("UPDATE tasks SET state='running', updated_at=? WHERE id=?", (now, task_id))
            return _step(connection.execute("SELECT * FROM task_steps WHERE task_id=? AND step_id=?", (task_id, step_id)).fetchone(), created=True)

    def finish_step(self, task_id: str, step_id: str, result: dict) -> dict:
        """Persist observed result, even if cancellation happened during the effect."""
        encoded = _json(result)
        if not isinstance(result, dict):
            raise ValueError("Resultado de ferramenta deve ser um objeto.")
        state = "completed" if result.get("ok") is True else "failed"
        if result.get("status") in {"uncertain", "needs_reconciliation"}:
            state = "needs_reconciliation"
        with connect(self.db_path) as connection:
            connection.execute("BEGIN IMMEDIATE")
            existing = connection.execute("SELECT * FROM task_steps WHERE task_id=? AND step_id=?", (task_id, step_id)).fetchone()
            if existing is None:
                raise KeyError((task_id, step_id))
            if existing["result"] is not None:
                if existing["result"] != encoded:
                    raise ValueError("Resultado já gravado; reconciliação deve ser explícita.")
                return _step(existing)
            now = utc_now()
            connection.execute("UPDATE task_steps SET state=?, result=?, finished_at=? WHERE task_id=? AND step_id=?", (state, encoded, now, task_id, step_id))
            connection.execute("UPDATE tasks SET updated_at=? WHERE id=?", (now, task_id))
            return _step(connection.execute("SELECT * FROM task_steps WHERE task_id=? AND step_id=?", (task_id, step_id)).fetchone())

    def steps(self, task_id: str) -> list[dict]:
        with connect(self.db_path) as connection:
            return [_step(row) for row in connection.execute("SELECT * FROM task_steps WHERE task_id=? ORDER BY created_at, rowid", (task_id,))]

    def events(self, task_id: str) -> list[dict]:
        with connect(self.db_path) as connection:
            return [dict(row) for row in connection.execute("SELECT * FROM task_events WHERE task_id=? ORDER BY id", (task_id,))]

    def recover_interrupted(self) -> list[dict]:
        """Call once at startup, before any executor runs. Never replay effects."""
        with connect(self.db_path) as connection:
            connection.execute("BEGIN IMMEDIATE")
            interrupted = connection.execute("SELECT id FROM tasks WHERE state='running' OR id IN (SELECT task_id FROM task_steps WHERE state='running')").fetchall()
            now = utc_now()
            message = "Execução interrompida. Confira os efeitos já registrados antes de continuar."
            for row in interrupted:
                connection.execute("UPDATE task_steps SET state='needs_reconciliation' WHERE task_id=? AND state='running'", (row[0],))
                connection.execute("UPDATE tasks SET state='needs_reconciliation', message=?, updated_at=? WHERE id=?", (message, now, row[0]))
                connection.execute("INSERT INTO task_events(task_id, state, message, created_at) VALUES (?, 'needs_reconciliation', ?, ?)", (row[0], message, now))
            return [_task(connection.execute("SELECT * FROM tasks WHERE id=?", (row[0],)).fetchone()) for row in interrupted]
