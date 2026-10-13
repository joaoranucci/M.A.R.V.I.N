"""Bounded metadata-only JSONL logs. Never logs prompts, files or tool arguments."""
import json
import logging
from logging.handlers import RotatingFileHandler


class EventLog:
    def __init__(self, directory):
        directory.mkdir(parents=True, exist_ok=True)
        self.handler = RotatingFileHandler(directory / "events.jsonl", maxBytes=512_000, backupCount=2, encoding="utf-8")
        self.logger = logging.Logger("marvin-events", level=logging.INFO)
        self.logger.addHandler(self.handler)

    def record(self, event):
        # Whitelist metadata; the original payload can contain user content.
        record = {key: event.get(key) for key in ("type", "task_id", "session_id", "time", "origin")}
        record["payload"] = {key: value for key, value in event.get("payload", {}).items()
                             if key in {"tool", "ok", "state", "duration_ms"} and isinstance(value, (str, int, bool, float))}
        self.logger.info(json.dumps(record, ensure_ascii=False))

    def close(self):
        self.handler.close()
        self.logger.removeHandler(self.handler)
