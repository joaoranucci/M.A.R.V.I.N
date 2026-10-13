"""Local one-shot reminders; no thread starts on import.

Delivery is at-least-once: claim, show the notification, then acknowledge it.
If the app crashes between display and ack the same occurrence can be shown
again after its lease, but cannot silently disappear before display.
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path
import re
import unicodedata
import uuid
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from .memory import connect, migrate, utc_now


TIMEZONE = "America/Sao_Paulo"
try:
    SAO_PAULO = ZoneInfo(TIMEZONE)
    TIMEZONE_SOURCE = "IANA"
except ZoneInfoNotFoundError:
    # Windows without tzdata: transparent fallback for contemporary scheduling.
    # Install tzdata for rule changes/historical dates. Do not use host timezone.
    SAO_PAULO = timezone(timedelta(hours=-3), TIMEZONE)
    TIMEZONE_SOURCE = "fixed UTC-03 fallback; install tzdata for IANA rules"


def _local(value: datetime | None) -> datetime:
    value = value or datetime.now(SAO_PAULO)
    return value.replace(tzinfo=SAO_PAULO) if value.tzinfo is None else value.astimezone(SAO_PAULO)


def _utc(value: datetime) -> str:
    return _local(value).astimezone(timezone.utc).isoformat(timespec="microseconds")


def _record(row) -> dict:
    data = dict(row)
    data["due_local"] = datetime.fromisoformat(data["due_at"]).astimezone(SAO_PAULO).isoformat(timespec="seconds")
    return data


def parse_reminder(text: str, now: datetime | None = None) -> dict:
    """Parse an explicit single occurrence, without silently inventing a time.

    Supports "daqui a 2 minutos/duas horas", "amanhã às 09:30" and
    "2026-10-14 09:30" (optional ISO offset). Other dates require clarification.
    """
    original = str(text).strip()
    normalized = "".join(c for c in unicodedata.normalize("NFD", original.lower()) if not unicodedata.combining(c))
    now = _local(now)
    numbers = {"um": 1, "uma": 1, "dois": 2, "duas": 2, "tres": 3, "quatro": 4, "cinco": 5, "seis": 6, "sete": 7, "oito": 8, "nove": 9, "dez": 10, "quinze": 15, "trinta": 30}
    relative = re.search(r"\bdaqui\s+a\s+(\d+|um|uma|dois|duas|tres|quatro|cinco|seis|sete|oito|nove|dez|quinze|trinta)\s+(minutos?|horas?|dias?)\b", normalized)
    tomorrow = re.search(r"\bamanha\s+(?:as?\s+)?(\d{1,2})(?:(?::|h)(\d{2})|h\b)", normalized)
    absolute = re.search(r"\b\d{4}-\d{2}-\d{2}[t ]\d{2}:\d{2}(?::\d{2})?(?:z|[+-]\d{2}:\d{2})?\b", normalized)
    matches = [match for match in (relative, tomorrow, absolute) if match]
    if len(matches) != 1 or len(re.findall(r"\b(?:daqui\s+a|amanha|\d{4}-\d{2}-\d{2}[t ])", normalized)) > 1:
        raise ValueError("Informe uma data e um horário: 'daqui a 10 minutos', 'amanhã às 09:30' ou '2026-10-14 09:30'.")
    match = matches[0]
    if relative:
        value = relative.group(1)
        amount = int(value) if value.isdigit() else numbers[value]
        if amount < 1 or amount > 100000:
            raise ValueError("Intervalo fora dos limites; informe uma data explícita.")
        unit = relative.group(2)
        seconds = amount * (60 if unit.startswith("minuto") else 3600 if unit.startswith("hora") else 86400)
        due = (now.astimezone(timezone.utc) + timedelta(seconds=seconds)).astimezone(SAO_PAULO)
    elif tomorrow:
        hour, minute = int(tomorrow.group(1)), int(tomorrow.group(2) or 0)
        due = (now + timedelta(days=1)).replace(hour=hour, minute=minute, second=0, microsecond=0)
    else:
        due = _local(datetime.fromisoformat(absolute.group(0).replace("z", "+00:00")))
    if due <= now:
        raise ValueError("Esse horário já passou. Informe uma data futura.")
    # NFD strips marks but preserves the length for usual Portuguese characters.
    # Slice using positions in normalized text, whose characters map 1:1 here.
    message = (original[:match.start()] + " " + original[match.end():]).strip(" ,.;:")
    message = re.sub(r"^(?:marvin[, ]+)?(?:me\s+)?(?:lembre|lembra|lembrar|avise|avisa)(?:-me)?\b\s*", "", message, flags=re.I)
    message = re.sub(r"^(?:crie|criar|agende|agendar)\s+(?:um\s+)?lembrete\s*", "", message, flags=re.I)
    message = re.sub(r"\s+", " ", message)
    message = re.sub(r"^(?:(?:em|de|do|da|para|pra|que)\s+)+", "", message, flags=re.I).strip(" ,.;:")
    if not message:
        raise ValueError("Informe o conteúdo do lembrete.")
    return {"message": message, "due_at": due, "timezone": TIMEZONE, "timezone_source": TIMEZONE_SOURCE}


class Scheduler:
    def __init__(self, db_path: Path):
        self.db_path = Path(db_path)
        migrate(self.db_path, "scheduler", 1, (
            "CREATE TABLE IF NOT EXISTS reminders (id TEXT PRIMARY KEY, session_id TEXT NOT NULL, message TEXT NOT NULL, due_at TEXT NOT NULL, timezone TEXT NOT NULL, state TEXT NOT NULL DEFAULT 'pending', claim_token TEXT, lease_until TEXT, attempts INTEGER NOT NULL DEFAULT 0, created_at TEXT NOT NULL, delivered_at TEXT)",
            "CREATE INDEX IF NOT EXISTS reminders_due_idx ON reminders(state, due_at)",
        ))

    def add(self, message: str, due_at: datetime | str, session_id: str = "default") -> dict:
        message = str(message).strip()
        if not message or len(message) > 2000:
            raise ValueError("Lembrete deve ter entre 1 e 2.000 caracteres.")
        if isinstance(due_at, str):
            due_at = datetime.fromisoformat(due_at.replace("Z", "+00:00"))
        if not isinstance(due_at, datetime):
            raise TypeError("Data do lembrete deve ser datetime ou ISO 8601.")
        reminder_id = uuid.uuid4().hex
        with connect(self.db_path) as connection:
            connection.execute("INSERT INTO reminders(id, session_id, message, due_at, timezone, created_at) VALUES (?, ?, ?, ?, ?, ?)", (reminder_id, session_id, message, _utc(due_at), TIMEZONE, utc_now()))
            return _record(connection.execute("SELECT * FROM reminders WHERE id=?", (reminder_id,)).fetchone())

    def parse_and_add(self, text: str, now: datetime | None = None, session_id: str = "default") -> dict:
        parsed = parse_reminder(text, now)
        return self.add(parsed["message"], parsed["due_at"], session_id)

    def list_reminders(self, include_done: bool = False) -> list[dict]:
        with connect(self.db_path) as connection:
            where = "" if include_done else "WHERE state IN ('pending', 'claimed')"
            return [_record(row) for row in connection.execute(f"SELECT * FROM reminders {where} ORDER BY due_at LIMIT 1000")]

    def cancel(self, reminder_id: str) -> bool:
        with connect(self.db_path) as connection:
            return connection.execute("UPDATE reminders SET state='cancelled', claim_token=NULL, lease_until=NULL WHERE id=? AND state IN ('pending', 'claimed')", (reminder_id,)).rowcount > 0

    def claim_due(self, now: datetime | None = None, lease_seconds: int = 60) -> list[dict]:
        now = _local(now)
        if not 1 <= lease_seconds <= 3600:
            raise ValueError("Lease deve durar entre 1 e 3.600 segundos.")
        with connect(self.db_path) as connection:
            connection.execute("BEGIN IMMEDIATE")
            rows = connection.execute("SELECT id FROM reminders WHERE due_at <= ? AND (state='pending' OR (state='claimed' AND lease_until <= ?)) ORDER BY due_at LIMIT 100", (_utc(now), _utc(now))).fetchall()
            result = []
            for row in rows:
                token = uuid.uuid4().hex
                connection.execute("UPDATE reminders SET state='claimed', claim_token=?, lease_until=?, attempts=attempts+1 WHERE id=?", (token, _utc(now + timedelta(seconds=lease_seconds)), row[0]))
                result.append(_record(connection.execute("SELECT * FROM reminders WHERE id=?", (row[0],)).fetchone()))
            return result

    def ack(self, reminder_id: str, claim_token: str) -> bool:
        """Acknowledge only after notification is rendered by the UI thread."""
        with connect(self.db_path) as connection:
            return connection.execute("UPDATE reminders SET state='delivered', delivered_at=?, claim_token=NULL, lease_until=NULL WHERE id=? AND state='claimed' AND claim_token=?", (utc_now(), reminder_id, claim_token)).rowcount > 0
