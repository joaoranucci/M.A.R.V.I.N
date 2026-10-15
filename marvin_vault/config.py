"""Caminhos privados e token de acesso local."""
from __future__ import annotations
import os
from pathlib import Path


def root_dir() -> Path:
    override = os.environ.get("MARVIN_VAULT_HOME")
    if override:
        return Path(override).expanduser().resolve()
    if os.name == "nt":
        return Path(os.environ.get("LOCALAPPDATA") or Path.home() / "AppData" / "Local") / "MarvinVault"
    return Path(os.environ.get("XDG_DATA_HOME") or Path.home() / ".local" / "share") / "MarvinVault"


def db_file() -> Path:
    return root_dir() / "vault.sqlite3"


def token_file() -> Path:
    return root_dir() / "api-token.txt"


def ensure_token() -> str:
    from .vault import new_api_token
    file = token_file()
    if file.exists():
        return file.read_text(encoding="utf-8").strip()
    file.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    token = new_api_token()
    # Cria de forma exclusiva; nunca substitui token existente.
    with file.open("x", encoding="utf-8") as fp:
        fp.write(token + "\n")
    if os.name != "nt":
        file.chmod(0o600)
    return token


def get_token() -> str:
    return token_file().read_text(encoding="utf-8").strip()
