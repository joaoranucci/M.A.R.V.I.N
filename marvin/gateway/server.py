"""Wires gateway services and runs them on HTTPS (uvicorn with the pinned identity)."""
from __future__ import annotations

import threading
import time
import uuid

from .api import create_app
from .assistant import AssistantService
from .config import GatewayConfig
from .desktop import DesktopAgent
from .documents import DocumentPipeline
from .events import EventLog
from .items import Items
from .pairing import Pairing
from .speech import SpeechService
from .store import Store
from .tls import display_fingerprint, ensure_identity
from .vault import VaultAdapter


def server_id(config: GatewayConfig) -> str:
    path = config.directory / "server-id"
    if path.is_file():
        return path.read_text(encoding="utf-8").strip()
    config.directory.mkdir(parents=True, exist_ok=True)
    value = uuid.uuid4().hex
    path.write_text(value, encoding="utf-8")
    return value


class Gateway:
    def __init__(self, config: GatewayConfig, presence=None, *, desktop_handlers=None):
        self.config, self.presence = config, presence
        self.store = Store(config.database)
        self.server_id = server_id(config)
        self.events = EventLog(self.store, config.event_retention)
        self.pairing = Pairing(self.store, config.pair_ttl_seconds)
        self.vault = VaultAdapter(config.vault_url, config.vault_token_file)
        self.assistant = AssistantService(presence, self.store, self.events,
                                          ollama_url=config.ollama_url, ollama_model=config.ollama_model)
        self.desktop = DesktopAgent(self.store, self.events, presence, enabled=config.desktop_actions,
                                    handlers=desktop_handlers)
        self.documents = DocumentPipeline(self.store, self.events, self.vault, config.directory / "spool")
        self.items = Items(self.store)
        self.speech = SpeechService()
        self.app = create_app(self)
        self.server = None
        self.thread = None
        self.pin = ""

    def start_services(self) -> None:
        self.desktop.start()
        self.documents.start()

    def close(self) -> None:
        self.desktop.close()
        self.documents.close()
        for worker in (self.desktop.thread, self.documents.thread):
            if worker is not None and worker is not threading.current_thread():
                worker.join(timeout=5)
        if self.server is not None:
            self.server.should_exit = True
        if self.presence is not None and self.assistant._on_presence_event in self.presence.listeners:
            self.presence.listeners.remove(self.assistant._on_presence_event)

    def _uvicorn(self):
        import uvicorn
        cert, key, self.pin = ensure_identity(self.config.directory, self.config.server_name)
        config = uvicorn.Config(self.app, host=self.config.host, port=self.config.port, ssl_certfile=str(cert),
                                ssl_keyfile=str(key), access_log=False, log_level="warning", timeout_keep_alive=30)
        return uvicorn.Server(config)

    def start_background(self) -> "Gateway":
        """Used by the Presence desktop process: HTTPS server on a daemon thread."""
        self.start_services()
        self.server = self._uvicorn()
        self.thread = threading.Thread(target=self.server.run, daemon=True, name="MARVIN-mobile-gateway")
        self.thread.start()
        for _ in range(100):
            if self.server.started:
                break
            time.sleep(.05)
        if not self.server.started:
            raise RuntimeError(f"Não foi possível abrir a porta {self.config.port} do gateway mobile.")
        return self

    def serve_forever(self) -> None:
        self.start_services()
        self.server = self._uvicorn()
        self.server.run()

    def describe(self) -> str:
        if not self.pin:
            _, _, self.pin = ensure_identity(self.config.directory, self.config.server_name)
        return (f"Gateway mobile em https://{self.config.advertised()}:{self.config.port} "
                f"· impressão digital {display_fingerprint(self.pin)}")
