"""Gateway SQLite: devices, pairing, events, commands, uploads and personal items.

Separate from marvin.db so the gateway schema evolves without touching the core.
Device tokens and pairing codes are stored only as SHA-256 hashes.
"""
from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import sqlite3
import threading

SCHEMA_VERSION = 1
MIGRATIONS = {
    1: (
        "CREATE TABLE devices (id TEXT PRIMARY KEY, name TEXT NOT NULL, platform TEXT NOT NULL,"
        " app_version TEXT NOT NULL DEFAULT '', token_hash TEXT NOT NULL UNIQUE, created_at TEXT NOT NULL,"
        " last_seen_at TEXT, revoked_at TEXT)",
        "CREATE TABLE pair_codes (id TEXT PRIMARY KEY, code_hash TEXT NOT NULL, created_at TEXT NOT NULL,"
        " expires_at TEXT NOT NULL, used_at TEXT, attempts INTEGER NOT NULL DEFAULT 0, device_id TEXT)",
        "CREATE TABLE events (seq INTEGER PRIMARY KEY AUTOINCREMENT, type TEXT NOT NULL, payload TEXT NOT NULL,"
        " created_at TEXT NOT NULL, device_id TEXT)",
        "CREATE TABLE requests (client_id TEXT PRIMARY KEY, device_id TEXT NOT NULL, kind TEXT NOT NULL,"
        " ref TEXT NOT NULL, fingerprint TEXT NOT NULL, created_at TEXT NOT NULL)",
        "CREATE TABLE jobs (id TEXT PRIMARY KEY, device_id TEXT NOT NULL, engine TEXT NOT NULL, text TEXT NOT NULL,"
        " state TEXT NOT NULL, answer TEXT NOT NULL DEFAULT '', created_at TEXT NOT NULL, updated_at TEXT NOT NULL)",
        "CREATE TABLE commands (id TEXT PRIMARY KEY, device_id TEXT NOT NULL, action TEXT NOT NULL, params TEXT NOT NULL,"
        " state TEXT NOT NULL, message TEXT NOT NULL DEFAULT '', result TEXT, verified INTEGER NOT NULL DEFAULT 0,"
        " created_at TEXT NOT NULL, expires_at TEXT NOT NULL, started_at TEXT, finished_at TEXT, updated_at TEXT NOT NULL)",
        "CREATE TABLE uploads (id TEXT PRIMARY KEY, device_id TEXT NOT NULL, filename TEXT NOT NULL, category TEXT NOT NULL,"
        " size INTEGER NOT NULL, sha256 TEXT NOT NULL, state TEXT NOT NULL, message TEXT NOT NULL DEFAULT '',"
        " document_id TEXT, chunks INTEGER, created_at TEXT NOT NULL, updated_at TEXT NOT NULL)",
        "CREATE TABLE items (id TEXT PRIMARY KEY, kind TEXT NOT NULL, title TEXT NOT NULL, notes TEXT NOT NULL DEFAULT '',"
        " due_at TEXT, done INTEGER NOT NULL DEFAULT 0, deleted INTEGER NOT NULL DEFAULT 0, rev INTEGER NOT NULL,"
        " created_at TEXT NOT NULL, updated_at TEXT NOT NULL, updated_by TEXT NOT NULL DEFAULT '')",
        "CREATE INDEX events_device_idx ON events(device_id, seq)",
        "CREATE INDEX commands_created_idx ON commands(created_at DESC)",
        "CREATE INDEX items_updated_idx ON items(updated_at)",
    ),
}


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def iso(value: datetime | None = None) -> str:
    return (value or utc_now()).astimezone(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def parse_iso(value: str) -> datetime:
    parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("Data sem fuso horário.")
    return parsed.astimezone(timezone.utc)


def later(seconds: float) -> str:
    return iso(utc_now() + timedelta(seconds=seconds))


def dumps(value) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), allow_nan=False, default=str)


class Store:
    def __init__(self, path: Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.RLock()
        self._migrate()

    @contextmanager
    def connect(self):
        connection = sqlite3.connect(str(self.path), timeout=10)
        try:
            connection.row_factory = sqlite3.Row
            connection.execute("PRAGMA busy_timeout=10000")
            yield connection
            connection.commit()
        except BaseException:
            connection.rollback()
            raise
        finally:
            connection.close()

    def _migrate(self) -> None:
        with self._lock, self.connect() as db:
            db.execute("PRAGMA journal_mode=WAL")
            current = db.execute("PRAGMA user_version").fetchone()[0]
            if current > SCHEMA_VERSION:
                raise RuntimeError("gateway.db é de uma versão mais nova do MARVIN.")
            for version in range(current + 1, SCHEMA_VERSION + 1):
                db.execute("BEGIN IMMEDIATE")
                for statement in MIGRATIONS[version]:
                    db.execute(statement)
                db.execute(f"PRAGMA user_version={version}")

    def one(self, sql: str, args=()) -> dict | None:
        with self.connect() as db:
            row = db.execute(sql, args).fetchone()
        return dict(row) if row else None

    def all(self, sql: str, args=()) -> list[dict]:
        with self.connect() as db:
            return [dict(row) for row in db.execute(sql, args).fetchall()]

    def execute(self, sql: str, args=()) -> int:
        with self.connect() as db:
            return db.execute(sql, args).rowcount
