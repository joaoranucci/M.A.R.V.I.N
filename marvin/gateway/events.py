"""Persistent event log consumed by long-poll with a sequence cursor.

Sequence numbers survive restarts, so a client can detect gaps (reset) and
deduplicate replays by seq. Payloads must never include tokens or file bytes.
"""
from __future__ import annotations

import json
import threading

from .store import Store, dumps, iso


class EventLog:
    def __init__(self, store: Store, retention: int = 5000):
        self.store, self.retention = store, retention
        self._lock = threading.Lock()
        self._published = 0
        row = store.one("SELECT COALESCE(MAX(seq), 0) AS seq FROM events")
        self.last_seq = int(row["seq"]) if row else 0

    def publish(self, kind: str, payload: dict | None = None, device_id: str | None = None) -> int:
        with self._lock:
            with self.store.connect() as db:
                cursor = db.execute("INSERT INTO events(type, payload, created_at, device_id) VALUES (?, ?, ?, ?)",
                                    (kind, dumps(payload or {}), iso(), device_id))
                seq = int(cursor.lastrowid)
                self._published += 1
                if self._published % 200 == 0:
                    db.execute("DELETE FROM events WHERE seq <= ?", (seq - self.retention,))
            self.last_seq = seq
            return seq

    def since(self, after: int, device_id: str, limit: int = 200) -> dict:
        after = max(int(after), 0)
        oldest = self.store.one("SELECT MIN(seq) AS seq FROM events")
        oldest_seq = int(oldest["seq"]) if oldest and oldest["seq"] is not None else self.last_seq + 1
        # The client cursor is ahead of this server (database replaced) or behind retention.
        # On reset the client resynchronizes through REST and continues from last_seq.
        if after > self.last_seq or (after > 0 and after + 1 < oldest_seq):
            return {"events": [], "last_seq": self.last_seq, "reset": True}
        with self.store.connect() as db:
            db.execute("BEGIN")  # one snapshot: no event can slip between both reads
            ceiling = int(db.execute("SELECT COALESCE(MAX(seq), 0) FROM events").fetchone()[0])
            rows = db.execute("SELECT * FROM events WHERE seq > ? AND seq <= ? AND (device_id IS NULL OR device_id = ?)"
                              " ORDER BY seq LIMIT ?", (after, ceiling, device_id, min(max(limit, 1), 500))).fetchall()
        events = [{"seq": r["seq"], "type": r["type"], "time": r["created_at"], "data": json.loads(r["payload"])}
                  for r in rows]
        full_page = len(events) >= min(max(limit, 1), 500)
        last = events[-1]["seq"] if full_page else ceiling
        return {"events": events, "last_seq": max(last, after), "reset": False}
