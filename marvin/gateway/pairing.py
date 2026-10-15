"""Device pairing with short-lived single-use codes and revocable device tokens."""
from __future__ import annotations

import hashlib
import secrets
import threading
import time
import uuid

from .store import Store, iso, later, parse_iso, utc_now

MAX_ATTEMPTS_PER_CODE = 5
GLOBAL_FAILURES = 10
GLOBAL_WINDOW_SECONDS = 600
LOCKOUT_SECONDS = 300


class PairingError(Exception):
    def __init__(self, code: str, message: str, status: int = 400):
        super().__init__(message)
        self.code, self.status = code, status


def token_hash(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()


def code_hash(pair_id: str, code: str) -> str:
    return hashlib.sha256(f"{pair_id}:{code}".encode("utf-8")).hexdigest()


class Pairing:
    def __init__(self, store: Store, ttl_seconds: int = 300):
        self.store, self.ttl = store, ttl_seconds
        self._failures: list[float] = []
        self._locked_until = 0.0
        self._guard = threading.Lock()
        self._seen: dict[str, float] = {}

    def create_code(self) -> dict:
        """A new code invalidates previous unused codes: one pairing window at a time."""
        pair_id, code = uuid.uuid4().hex, f"{secrets.randbelow(10 ** 6):06d}"
        now = iso()
        with self.store.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            db.execute("UPDATE pair_codes SET expires_at=? WHERE used_at IS NULL AND expires_at > ?", (now, now))
            db.execute("INSERT INTO pair_codes(id, code_hash, created_at, expires_at) VALUES (?, ?, ?, ?)",
                       (pair_id, code_hash(pair_id, code), now, later(self.ttl)))
        return {"id": pair_id, "code": code, "expires_at": later(self.ttl), "ttl_seconds": self.ttl}

    def code_state(self, pair_id: str) -> str:
        row = self.store.one("SELECT * FROM pair_codes WHERE id=?", (pair_id,))
        if row is None:
            return "missing"
        if row["used_at"]:
            return "used"
        return "expired" if parse_iso(row["expires_at"]) <= utc_now() else "active"

    def _fail(self) -> None:
        now = time.monotonic()
        self._failures = [t for t in self._failures if now - t < GLOBAL_WINDOW_SECONDS] + [now]
        if len(self._failures) >= GLOBAL_FAILURES:
            self._locked_until = now + LOCKOUT_SECONDS
            self._failures.clear()

    def pair(self, code: str, name: str, platform: str, app_version: str) -> dict:
        with self._guard:
            if time.monotonic() < self._locked_until:
                raise PairingError("pairing_locked", "Muitas tentativas. Gere um novo código no PC em alguns minutos.", 429)
            if not (isinstance(code, str) and len(code) == 6 and code.isdigit()):
                self._fail()
                raise PairingError("invalid_code", "Código inválido ou expirado.", 401)
            now = iso()
            with self.store.connect() as db:
                db.execute("BEGIN IMMEDIATE")
                active = db.execute("SELECT * FROM pair_codes WHERE used_at IS NULL AND expires_at > ?"
                                    " ORDER BY created_at DESC LIMIT 1", (now,)).fetchone()
                if active is None or not secrets.compare_digest(active["code_hash"], code_hash(active["id"], code)):
                    if active is not None:
                        attempts = active["attempts"] + 1
                        expires = now if attempts >= MAX_ATTEMPTS_PER_CODE else active["expires_at"]
                        db.execute("UPDATE pair_codes SET attempts=?, expires_at=? WHERE id=?",
                                   (attempts, expires, active["id"]))
                    db.commit()
                    self._fail()
                    raise PairingError("invalid_code", "Código inválido ou expirado.", 401)
                device_id, token = uuid.uuid4().hex, secrets.token_urlsafe(32)
                db.execute("INSERT INTO devices(id, name, platform, app_version, token_hash, created_at, last_seen_at)"
                           " VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (device_id, name[:80] or "Celular", platform[:20], app_version[:40], token_hash(token), now, now))
                db.execute("UPDATE pair_codes SET used_at=?, device_id=? WHERE id=?", (now, device_id, active["id"]))
        return {"device_id": device_id, "token": token}

    def authenticate(self, token: str) -> dict | None:
        if not token or len(token) > 200:
            return None
        device = self.store.one("SELECT * FROM devices WHERE token_hash=? AND revoked_at IS NULL", (token_hash(token),))
        if device is None:
            return None
        now = time.monotonic()
        if now - self._seen.get(device["id"], 0) > 60:
            self._seen[device["id"]] = now
            self.store.execute("UPDATE devices SET last_seen_at=? WHERE id=?", (iso(), device["id"]))
        return device

    def devices(self) -> list[dict]:
        rows = self.store.all("SELECT id, name, platform, app_version, created_at, last_seen_at, revoked_at"
                              " FROM devices ORDER BY created_at DESC")
        return rows

    def revoke(self, device_id: str) -> bool:
        changed = self.store.execute("UPDATE devices SET revoked_at=? WHERE id=? AND revoked_at IS NULL",
                                     (iso(), device_id))
        return changed > 0
