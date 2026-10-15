"""Personal tasks, reminders and notes synchronized with revision numbers.

A write must name the revision it was based on. A different server revision is
a conflict returned to the device, which decides; nothing is merged silently.
Deletions are tombstones so other devices learn about them.
"""
from __future__ import annotations

from .store import Store, iso, parse_iso

KINDS = {"task", "reminder", "note"}


class ItemConflict(Exception):
    def __init__(self, server_item: dict):
        super().__init__("Conflito de versão")
        self.server_item = server_item


def public(row: dict) -> dict:
    return {"id": row["id"], "kind": row["kind"], "title": row["title"], "notes": row["notes"],
            "due_at": row["due_at"], "done": bool(row["done"]), "deleted": bool(row["deleted"]), "rev": row["rev"],
            "created_at": row["created_at"], "updated_at": row["updated_at"], "updated_by": row["updated_by"]}


def validate(data: dict) -> dict:
    kind = data.get("kind")
    if kind not in KINDS:
        raise ValueError("Tipo de item inválido.")
    title = str(data.get("title", "")).strip()
    if not 1 <= len(title) <= 300:
        raise ValueError("Título deve ter de 1 a 300 caracteres.")
    notes = str(data.get("notes") or "")
    if len(notes) > 4000:
        raise ValueError("Notas com mais de 4.000 caracteres.")
    due_at = data.get("due_at")
    if due_at:
        due_at = iso(parse_iso(due_at))
    return {"kind": kind, "title": title, "notes": notes, "due_at": due_at or None,
            "done": 1 if data.get("done") else 0, "deleted": 1 if data.get("deleted") else 0}


class Items:
    def __init__(self, store: Store):
        self.store = store

    def list(self, since: str | None = None) -> list[dict]:
        if since:
            rows = self.store.all("SELECT * FROM items WHERE updated_at > ? ORDER BY updated_at", (iso(parse_iso(since)),))
        else:
            rows = self.store.all("SELECT * FROM items ORDER BY updated_at")
        return [public(r) for r in rows]

    def put(self, item_id: str, data: dict, base_rev: int | None, device_id: str) -> tuple[str, dict]:
        clean = validate(data)
        now = iso()
        with self.store.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            row = db.execute("SELECT * FROM items WHERE id=?", (item_id,)).fetchone()
            if row is None:
                db.execute("INSERT INTO items VALUES (?, ?, ?, ?, ?, ?, ?, 1, ?, ?, ?)",
                           (item_id, clean["kind"], clean["title"], clean["notes"], clean["due_at"], clean["done"],
                            clean["deleted"], now, now, device_id))
                status = "created"
            else:
                current = dict(row)
                same = all(current[k] == clean[k] for k in clean)
                if same:
                    return "unchanged", public(current)
                if base_rev != current["rev"]:
                    raise ItemConflict(public(current))
                db.execute("UPDATE items SET kind=?, title=?, notes=?, due_at=?, done=?, deleted=?, rev=rev+1,"
                           " updated_at=?, updated_by=? WHERE id=?",
                           (clean["kind"], clean["title"], clean["notes"], clean["due_at"], clean["done"],
                            clean["deleted"], now, device_id, item_id))
                status = "updated"
            saved = dict(db.execute("SELECT * FROM items WHERE id=?", (item_id,)).fetchone())
        return status, public(saved)
