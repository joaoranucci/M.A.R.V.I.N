"""Local configuration: never rewrite .env while upgrading the application."""
from __future__ import annotations

import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERSION = "0.7.0"
PREFERENCE_KEYS = {"MARVIN_MIC_DEVICE", "MARVIN_MIC_RATE", "MARVIN_OUTPUT_DEVICE",
                   "MARVIN_VOICE", "MARVIN_SPEAK", "MARVIN_WAKE", "MARVIN_VOLUME",
                   "MARVIN_CONTINUITY_SECONDS"}


def load_config(root: Path = ROOT) -> Path:
    explicit = set(os.environ)
    try:
        from dotenv import load_dotenv
        load_dotenv(root / ".env")
    except ImportError:
        # Text/local mode must boot without installing any optional dependency.
        path = root / ".env"
        if path.is_file():
            for line in path.read_text(encoding="utf-8-sig").splitlines():
                key, sep, value = line.partition("=")
                if sep and key.strip().isidentifier():
                    os.environ.setdefault(key.strip(), value.strip().strip("\"'"))
    data = Path(os.getenv("MARVIN_DATA_DIR") or root / "data").resolve()
    prefs = data / "preferences.json"
    if prefs.is_file():
        try:
            values = json.loads(prefs.read_text(encoding="utf-8"))
            for key, value in values.items():
                if key in PREFERENCE_KEYS and key not in explicit and isinstance(value, (str, int, float, bool)):
                    os.environ[key] = str(value)
        except (OSError, ValueError, AttributeError):
            pass
    return data


def save_preferences(data: Path, values: dict) -> None:
    if set(values) - PREFERENCE_KEYS:
        raise ValueError("Preferência não permitida.")
    data.mkdir(parents=True, exist_ok=True)
    path = data / "preferences.json"
    try:
        current = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    except (OSError, ValueError):
        current = {}
    current = {k: v for k, v in current.items() if k in PREFERENCE_KEYS}
    current.update({k: str(v) for k, v in values.items()})
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(current, ensure_ascii=False, indent=2), encoding="utf-8")
    temporary.replace(path)
    os.environ.update({k: str(v) for k, v in values.items()})
