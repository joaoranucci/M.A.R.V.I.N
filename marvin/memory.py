"""Local memory. SQLite connections are closed, and migrations back up old data.

Backups are retained until removed by the user and may contain facts subsequently
deleted from the live store. Legacy messages/facts tables keep their schema.
"""
from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime, timezone
import json
import sqlite3
from pathlib import Path
import re
import threading
import unicodedata
import uuid


_MIGRATION_LOCK = threading.RLock()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="microseconds")


@contextmanager
def connect(db_path: Path):
    """Commit/rollback AND close (SQLite's own context manager does not close)."""
    connection = sqlite3.connect(str(db_path), timeout=10)
    try:
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys=ON")
        yield connection
        connection.commit()
    except BaseException:
        connection.rollback()
        raise
    finally:
        connection.close()


def migrate(db_path: Path, component: str, version: int, statements: tuple[str, ...]) -> None:
    """Apply an additive component migration after backing up an existing DB."""
    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    with _MIGRATION_LOCK, connect(db_path) as connection:
        tables = {row[0] for row in connection.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        current = 0
        if "schema_migrations" in tables:
            row = connection.execute("SELECT version FROM schema_migrations WHERE component=?", (component,)).fetchone()
            current = int(row[0]) if row else 0
        if current > version:
            raise RuntimeError(f"Banco {component} versão {current} é mais novo que este MARVIN ({version}).")
        if current == version:
            return
        if tables:
            backup_dir = db_path.parent / "backups"
            backup_dir.mkdir(parents=True, exist_ok=True)
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
            backup_path = backup_dir / f"{db_path.name}.{component}.v{current}.{stamp}.{uuid.uuid4().hex[:6]}.bak"
            with connect(backup_path) as backup:
                connection.backup(backup)
        connection.execute("BEGIN IMMEDIATE")
        connection.execute("CREATE TABLE IF NOT EXISTS schema_migrations (component TEXT PRIMARY KEY, version INTEGER NOT NULL, applied_at TEXT NOT NULL)")
        for statement in statements:
            connection.execute(statement)
        connection.execute("INSERT OR REPLACE INTO schema_migrations VALUES (?, ?, ?)", (component, version, utc_now()))


def _tokens(text: str) -> set[str]:
    normalized = "".join(c for c in unicodedata.normalize("NFKD", text.casefold()) if not unicodedata.combining(c))
    stop = {"a", "o", "as", "os", "de", "da", "do", "das", "dos", "e", "em", "um", "uma", "que", "me", "meu", "minha", "para", "por", "com", "sobre", "voce", "lembra", "lembrar", "qual", "quais", "esse", "essa", "isso"}
    return {token for token in re.findall(r"\w+", normalized) if len(token) > 1 and token not in stop}


class Memory:
    def __init__(self, db_path: Path):
        self.db_path = Path(db_path)
        migrate(self.db_path, "memory", 1, (
            "CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY AUTOINCREMENT, role TEXT NOT NULL CHECK(role IN ('user', 'model')), content TEXT NOT NULL, created_at TEXT DEFAULT CURRENT_TIMESTAMP)",
            "CREATE TABLE IF NOT EXISTS facts (id INTEGER PRIMARY KEY AUTOINCREMENT, fact TEXT NOT NULL UNIQUE, created_at TEXT DEFAULT CURRENT_TIMESTAMP)",
            "CREATE TABLE IF NOT EXISTS fact_metadata (fact_id INTEGER PRIMARY KEY REFERENCES facts(id) ON DELETE CASCADE, category TEXT NOT NULL DEFAULT 'fact', origin TEXT NOT NULL DEFAULT 'user', scope TEXT NOT NULL DEFAULT 'personal', status TEXT NOT NULL DEFAULT 'active', reviewed_at TEXT NOT NULL)",
            "INSERT OR IGNORE INTO fact_metadata (fact_id, reviewed_at) SELECT id, COALESCE(created_at, CURRENT_TIMESTAMP) FROM facts",
            "CREATE TABLE IF NOT EXISTS session_context (session_id TEXT PRIMARY KEY, data TEXT NOT NULL, updated_at TEXT NOT NULL)",
        ))

    @staticmethod
    def _note(fact: str) -> str:
        note = str(fact).strip()
        if not note or len(note) > 500:
            raise ValueError("A lembrança deve ter entre 1 e 500 caracteres.")
        if re.search(r"(?:api[_ -]?key|senha|password|token|secret)\s*[:=]\s*\S+|-----BEGIN .*PRIVATE KEY", note, re.I):
            raise ValueError("Não salve senhas, tokens ou chaves na memória. Use um gerenciador de credenciais.")
        return note

    def remember(self, fact: str, *, category: str = "fact", origin: str = "user", scope: str = "personal") -> dict:
        note = self._note(fact)
        if category not in {"fact", "preference", "project", "decision"}:
            raise ValueError("Categoria de memória inválida.")
        with connect(self.db_path) as connection:
            connection.execute("INSERT OR IGNORE INTO facts(fact) VALUES (?)", (note,))
            fact_id = connection.execute("SELECT id FROM facts WHERE fact=?", (note,)).fetchone()[0]
            connection.execute("INSERT OR IGNORE INTO fact_metadata VALUES (?, ?, ?, ?, 'active', ?)", (fact_id, category, origin, scope, utc_now()))
        return {"ok": True, "memory": note, "id": fact_id}

    def facts(self, limit: int = 25) -> list[str]:
        return [row["fact"] for row in self.list_facts(min(max(int(limit), 1), 100))]

    def list_facts(self, limit: int = 100) -> list[dict]:
        with connect(self.db_path) as connection:
            rows = connection.execute("SELECT f.*, m.category, m.origin, m.scope, m.status, m.reviewed_at FROM facts f LEFT JOIN fact_metadata m ON m.fact_id=f.id WHERE COALESCE(m.status, 'active')='active' ORDER BY f.id DESC LIMIT ?", (min(max(int(limit), 1), 10000),)).fetchall()
        return [dict(row) for row in rows]

    def relevant(self, query: str, limit: int = 8) -> list[str]:
        """Accent-insensitive lexical retrieval; no claim of semantic matching."""
        terms = _tokens(query)
        if not terms:
            return []
        scored = []
        for row in self.list_facts(10000):
            overlap = terms & _tokens(row["fact"])
            if overlap:
                scored.append((len(overlap), row["id"], row["fact"]))
        scored.sort(reverse=True)
        return [row[2] for row in scored[:min(max(int(limit), 1), 100)]]

    @staticmethod
    def _invalidate_context(connection: sqlite3.Connection) -> None:
        # Summaries may paraphrase an old fact. Invalidate them; keep active paths.
        invalid = {"summary", "session_summary", "memories", "memory", "facts", "relevant_memories"}
        for row in connection.execute("SELECT session_id, data FROM session_context").fetchall():
            context = json.loads(row["data"])
            for key in invalid:
                context.pop(key, None)
            connection.execute("UPDATE session_context SET data=?, updated_at=? WHERE session_id=?", (json.dumps(context, ensure_ascii=False), utc_now(), row["session_id"]))

    def edit_fact(self, fact_id: int, fact: str) -> dict:
        note = self._note(fact)
        with connect(self.db_path) as connection:
            cursor = connection.execute("UPDATE facts SET fact=? WHERE id=?", (note, int(fact_id)))
            if not cursor.rowcount:
                raise KeyError(f"Lembrança {fact_id} não encontrada.")
            connection.execute("UPDATE fact_metadata SET reviewed_at=? WHERE fact_id=?", (utc_now(), fact_id))
            self._invalidate_context(connection)
        return {"ok": True, "id": int(fact_id), "memory": note}

    def delete_fact(self, fact_id: int) -> bool:
        with connect(self.db_path) as connection:
            deleted = connection.execute("DELETE FROM facts WHERE id=?", (int(fact_id),)).rowcount > 0
            if deleted:
                self._invalidate_context(connection)
        return deleted

    def forget_fact(self, fact: str) -> None:
        with connect(self.db_path) as connection:
            connection.execute("DELETE FROM facts WHERE fact = ?", (fact,))
            self._invalidate_context(connection)

    def recent(self, limit: int = 8) -> list[tuple[str, str]]:
        with connect(self.db_path) as connection:
            rows = connection.execute(
                "SELECT role, content FROM messages ORDER BY id DESC LIMIT ?", (min(max(int(limit), 1), 1000),)
            ).fetchall()
        return [(str(row[0]), str(row[1])) for row in reversed(rows)]

    def add_pair(self, question: str, answer: str) -> None:
        with connect(self.db_path) as connection:
            connection.executemany(
                "INSERT INTO messages (role, content) VALUES (?, ?)",
                (("user", question), ("model", answer)),
            )

    def get_context(self, session_id: str = "default") -> dict:
        with connect(self.db_path) as connection:
            row = connection.execute("SELECT data FROM session_context WHERE session_id=?", (session_id,)).fetchone()
        return json.loads(row[0]) if row else {}

    def set_context(self, context: dict, session_id: str = "default") -> dict:
        """Merge entities atomically; assigning None removes an entity."""
        if not isinstance(context, dict):
            raise TypeError("Contexto deve ser um objeto.")
        with connect(self.db_path) as connection:
            connection.execute("BEGIN IMMEDIATE")
            row = connection.execute("SELECT data FROM session_context WHERE session_id=?", (session_id,)).fetchone()
            merged = json.loads(row[0]) if row else {}
            for key, value in context.items():
                if value is None:
                    merged.pop(key, None)
                else:
                    merged[key] = value
            data = json.dumps(merged, ensure_ascii=False, allow_nan=False)
            if len(data.encode("utf-8")) > 65536:
                raise ValueError("Contexto excede 64 KiB; salve somente referências e resumos curtos.")
            connection.execute("INSERT INTO session_context VALUES (?, ?, ?) ON CONFLICT(session_id) DO UPDATE SET data=excluded.data, updated_at=excluded.updated_at", (session_id, data, utc_now()))
        return merged

    def export(self) -> dict:
        """Return a full JSON-serializable export; caller chooses destination."""
        with connect(self.db_path) as connection:
            messages = [dict(row) for row in connection.execute("SELECT * FROM messages ORDER BY id")]
            contexts = {row["session_id"]: json.loads(row["data"]) for row in connection.execute("SELECT * FROM session_context")}
            facts = [dict(row) for row in connection.execute("SELECT f.*, m.category, m.origin, m.scope, m.status, m.reviewed_at FROM facts f LEFT JOIN fact_metadata m ON m.fact_id=f.id ORDER BY f.id")]
        return {"version": 1, "exported_at": utc_now(), "facts": facts, "messages": messages, "sessions": contexts}

    def clear(self) -> None:
        """Clear live memory and entities; task/reminder history stays intact."""
        with connect(self.db_path) as connection:
            connection.execute("DELETE FROM messages")
            connection.execute("DELETE FROM facts")
            connection.execute("DELETE FROM session_context")
