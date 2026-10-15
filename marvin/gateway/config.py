"""Gateway settings from environment variables; no secrets live here."""
from __future__ import annotations

from dataclasses import dataclass, field
import os
from pathlib import Path
import socket


def _bool(name: str, default: bool) -> bool:
    value = os.getenv(name)
    if value is None or not value.strip():
        return default
    return value.strip().lower() in {"1", "true", "sim", "yes", "on"}


def _port(name: str, default: int) -> int:
    try:
        value = int(os.getenv(name, str(default)))
    except ValueError:
        return default
    return value if 1024 <= value <= 65535 else default


def lan_addresses() -> list[str]:
    """Best-effort IPv4 addresses of this PC; UDP connect sends no packet."""
    found: list[str] = []
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as probe:
            probe.connect(("192.0.2.1", 9))
            found.append(probe.getsockname()[0])
    except OSError:
        pass
    try:
        for info in socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET):
            address = info[4][0]
            if address not in found:
                found.append(address)
    except OSError:
        pass
    return [a for a in found if not a.startswith("127.")]


@dataclass
class GatewayConfig:
    data_dir: Path
    host: str = "0.0.0.0"
    port: int = 8770
    advertise_host: str = ""
    vault_url: str = "http://127.0.0.1:8765"
    vault_token_file: Path | None = None
    pair_ttl_seconds: int = 300
    event_retention: int = 5000
    desktop_actions: bool = True
    ollama_url: str = "http://127.0.0.1:11434"
    ollama_model: str = ""
    server_name: str = field(default_factory=socket.gethostname)

    @property
    def directory(self) -> Path:
        return self.data_dir / "gateway"

    @property
    def database(self) -> Path:
        return self.directory / "gateway.db"

    def advertised(self) -> str:
        if self.advertise_host:
            return self.advertise_host
        addresses = lan_addresses()
        return addresses[0] if addresses else "127.0.0.1"

    @classmethod
    def from_env(cls, data_dir: Path) -> "GatewayConfig":
        token_file = os.getenv("MARVIN_VAULT_TOKEN_FILE", "").strip()
        return cls(
            data_dir=Path(data_dir),
            host=os.getenv("MARVIN_MOBILE_HOST", "0.0.0.0").strip() or "0.0.0.0",
            port=_port("MARVIN_MOBILE_PORT", 8770),
            advertise_host=os.getenv("MARVIN_MOBILE_ADVERTISE_HOST", "").strip(),
            vault_url=os.getenv("MARVIN_VAULT_URL", "http://127.0.0.1:8765").strip(),
            vault_token_file=Path(token_file) if token_file else None,
            desktop_actions=_bool("MARVIN_MOBILE_DESKTOP_ACTIONS", True),
            ollama_model=os.getenv("MARVIN_MOBILE_OLLAMA_MODEL", "").strip(),
        )


def gateway_enabled() -> bool:
    return _bool("MARVIN_MOBILE_GATEWAY", False)
