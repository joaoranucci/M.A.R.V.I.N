"""MARVIN Link v1, LOCAL SIMULATOR ONLY: bounded frames and durable control IDs.

There is no Bluetooth, socket, pairing, encryption or hardware control here.
Only explicitly supplied Python handlers can run, in this process. Device names
are test fixtures, not authenticated identities. A transport must authenticate a
device before exposing this interface. No background workers start on import.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
from pathlib import Path
import re
import tempfile
import threading
import time
from typing import Callable
import uuid

from .memory import connect, migrate, utc_now


VERSION = 1
MAX_MESSAGE_BYTES = 65536
CAPABILITIES = frozenset({"control", "status", "media:audio", "media:image"})
_ID = re.compile(r"^[A-Za-z0-9_-]{1,64}$")


class ProtocolError(ValueError):
    pass


def _encode(value) -> bytes:
    try:
        return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"), allow_nan=False).encode("utf-8")
    except (TypeError, ValueError, RecursionError) as error:
        raise ProtocolError("Conteúdo não é JSON válido.") from error


def _identifier(value) -> bool:
    return isinstance(value, str) and _ID.fullmatch(value) is not None


def make_message(session_id: str, sequence: int, message_type: str, payload: dict,
                 message_id: str | None = None) -> dict:
    return {"version": VERSION, "session_id": session_id, "message_id": message_id or uuid.uuid4().hex,
            "sequence": sequence, "type": message_type, "format": "json",
            "size": len(_encode(payload)), "payload": payload}


def fragment_message(message: dict, mtu: int = 512) -> list[bytes]:
    """Frames include JSON/base64 overhead and each fits the negotiated MTU."""
    if not 256 <= mtu <= 4096:
        raise ProtocolError("MTU simulado deve estar entre 256 e 4096 bytes.")
    if not _identifier(message.get("session_id")) or not _identifier(message.get("message_id")):
        raise ProtocolError("Identificadores inválidos.")
    encoded = _encode(message)
    if len(encoded) > MAX_MESSAGE_BYTES:
        raise ProtocolError("Mensagem excede 64 KiB.")
    # Compute the worst-case overhead, including the maximum 3-digit fragment ID.
    base = {"v": VERSION, "s": message["session_id"], "m": message["message_id"], "i": 511, "n": 512, "b": ""}
    chunk_size = ((mtu - len(_encode(base))) // 4) * 3
    if chunk_size < 1:
        raise ProtocolError("MTU insuficiente para o envelope.")
    count = max(1, (len(encoded) + chunk_size - 1) // chunk_size)
    if count > 512:
        raise ProtocolError("Mensagem requer mais de 512 fragmentos neste MTU.")
    frames = []
    for index in range(count):
        frame = dict(base, i=index, n=count, b=base64.b64encode(encoded[index * chunk_size:(index + 1) * chunk_size]).decode("ascii"))
        frames.append(_encode(frame))
    return frames


class FragmentReassembler:
    def __init__(self, mtu: int = 512, *, max_buffers: int = 4,
                 max_total_bytes: int = 131072, ttl_seconds: float = 5):
        if not 256 <= mtu <= 4096 or not 1 <= max_buffers <= 16 or not 1 <= max_total_bytes <= 1048576 or not 0 < ttl_seconds <= 60:
            raise ProtocolError("Limites inválidos para fragmentação.")
        self.mtu, self.max_buffers = mtu, max_buffers
        self.max_total_bytes, self.ttl_seconds = max_total_bytes, ttl_seconds
        self.buffers: dict[tuple[str, str], dict] = {}

    @property
    def buffered_bytes(self) -> int:
        return sum(sum(len(chunk) for chunk in buffer["chunks"].values()) for buffer in self.buffers.values())

    def clear(self) -> None:
        self.buffers.clear()

    def feed(self, frame: bytes, now: float | None = None) -> dict | None:
        now = time.monotonic() if now is None else now
        for key in list(self.buffers):
            if now - self.buffers[key]["started"] >= self.ttl_seconds:
                del self.buffers[key]
        if not isinstance(frame, bytes) or len(frame) > self.mtu:
            raise ProtocolError("Frame excede o MTU negociado.")
        try:
            data = json.loads(frame)
        except (ValueError, UnicodeError, RecursionError) as error:
            raise ProtocolError("Frame JSON inválido.") from error
        if not isinstance(data, dict) or set(data) != {"v", "s", "m", "i", "n", "b"}:
            raise ProtocolError("Envelope de fragmento inválido.")
        if type(data["v"]) is not int or data["v"] != VERSION or not _identifier(data["s"]) or not _identifier(data["m"]):
            raise ProtocolError("Versão ou identificador de fragmento inválido.")
        if type(data["n"]) is not int or type(data["i"]) is not int or not 1 <= data["n"] <= 512 or not 0 <= data["i"] < data["n"]:
            raise ProtocolError("Sequência de fragmento inválida.")
        try:
            chunk = base64.b64decode(data["b"], validate=True)
        except (ValueError, TypeError) as error:
            raise ProtocolError("Payload base64 inválido.") from error
        key = (data["s"], data["m"])
        if key not in self.buffers:
            if len(self.buffers) >= self.max_buffers:
                raise ProtocolError("Backpressure: limite de mensagens incompletas atingido.")
            self.buffers[key] = {"started": now, "count": data["n"], "chunks": {}}
        buffer = self.buffers[key]
        old = buffer["chunks"].get(data["i"])
        if buffer["count"] != data["n"] or (old is not None and old != chunk):
            del self.buffers[key]
            raise ProtocolError("Fragmento duplicado conflitante.")
        if old is not None:
            return None
        if self.buffered_bytes + len(chunk) > self.max_total_bytes or sum(map(len, buffer["chunks"].values())) + len(chunk) > MAX_MESSAGE_BYTES:
            del self.buffers[key]
            raise ProtocolError("Backpressure: limite de bytes atingido.")
        buffer["chunks"][data["i"]] = chunk
        if len(buffer["chunks"]) != buffer["count"]:
            return None
        raw = b"".join(buffer["chunks"][index] for index in range(buffer["count"]))
        del self.buffers[key]
        try:
            message = json.loads(raw)
        except (ValueError, UnicodeError, RecursionError) as error:
            raise ProtocolError("Mensagem remontada inválida.") from error
        if not isinstance(message, dict) or message.get("session_id") != key[0] or message.get("message_id") != key[1]:
            raise ProtocolError("Identidade do envelope diverge da mensagem.")
        return message


class LinkSimulator:
    """Single-owner local endpoint. Callers own handler permissions and threads.

    Handler signature: handler(args: dict, cancelled: threading.Event) -> dict.
    Construct once per endpoint DB; startup recovers in-flight commands. A second
    concurrently active process on the same DB is not a supported transport.
    """
    def __init__(self, db_path: Path, handlers: dict[str, Callable] | None = None):
        self.db_path = Path(db_path)
        self.handlers = dict(handlers or {})
        self.cancelled = threading.Event()
        self.session_id: str | None = None
        self.negotiated: dict | None = None
        self.fragments = FragmentReassembler()
        migrate(self.db_path, "device_link", 1, (
            "CREATE TABLE IF NOT EXISTS link_sessions (id TEXT PRIMARY KEY, device_id TEXT NOT NULL, state TEXT NOT NULL, last_sequence INTEGER NOT NULL DEFAULT -1, created_at TEXT NOT NULL)",
            "CREATE TABLE IF NOT EXISTS link_commands (device_id TEXT NOT NULL, message_id TEXT NOT NULL, session_id TEXT NOT NULL REFERENCES link_sessions(id), digest TEXT NOT NULL, state TEXT NOT NULL, result TEXT, created_at TEXT NOT NULL, PRIMARY KEY(device_id, message_id))",
        ))
        with connect(self.db_path) as connection:
            connection.execute("UPDATE link_commands SET state='needs_reconciliation' WHERE state='running'")
            connection.execute("UPDATE link_sessions SET state='disconnected' WHERE state='active'")

    def hello(self, versions: list[int], capabilities: list[str], mtu: int = 512) -> dict:
        if not isinstance(versions, list) or any(type(item) is not int for item in versions) or VERSION not in versions:
            raise ProtocolError("Versão incompatível; este simulador oferece MARVIN Link 1.")
        if not isinstance(capabilities, list) or any(not isinstance(item, str) for item in capabilities):
            raise ProtocolError("Capacidades inválidas.")
        if self.session_id is not None:
            self.disconnect()
        self.fragments = FragmentReassembler(mtu)
        self.negotiated = {"type": "CAPABILITIES", "version": VERSION, "capabilities": sorted(CAPABILITIES.intersection(capabilities)),
                           "mtu": mtu, "max_message_bytes": MAX_MESSAGE_BYTES, "simulated": True}
        return dict(self.negotiated)

    def start_session(self, device_id: str = "simulated-glasses") -> str:
        if self.negotiated is None or not _identifier(device_id):
            raise ProtocolError("Negocie HELLO e informe um identificador local válido.")
        if self.session_id is not None:
            self.disconnect(keep_negotiation=True)
        self.cancelled = threading.Event()
        self.session_id = uuid.uuid4().hex
        with connect(self.db_path) as connection:
            connection.execute("INSERT INTO link_sessions(id,device_id,state,created_at) VALUES (?,?,'active',?)", (self.session_id, device_id, utc_now()))
        return self.session_id

    def disconnect(self, *, keep_negotiation: bool = False) -> None:
        self.cancelled.set()
        self.fragments.clear()
        if self.session_id is not None:
            with connect(self.db_path) as connection:
                connection.execute("UPDATE link_sessions SET state='disconnected' WHERE id=? AND state='active'", (self.session_id,))
        self.session_id = None
        if not keep_negotiation:
            self.negotiated = None

    def receive_frame(self, frame: bytes) -> dict | None:
        if self.session_id is None:
            raise ProtocolError("Nenhuma sessão conectada.")
        message = self.fragments.feed(frame)
        return self.receive(message) if message is not None else None

    @staticmethod
    def _ack(message: dict, state: str, result=None, replayed: bool = False) -> dict:
        return {"type": "ACK", "message_id": message["message_id"], "state": state, "result": result, "replayed": replayed, "simulated": True}

    def receive(self, message: dict) -> dict:
        if not isinstance(message, dict) or set(message) != {"version", "session_id", "message_id", "sequence", "type", "format", "size", "payload"}:
            raise ProtocolError("Envelope de mensagem inválido.")
        if len(_encode(message)) > MAX_MESSAGE_BYTES or type(message["version"]) is not int or message["version"] != VERSION or message["format"] != "json":
            raise ProtocolError("Formato, tamanho ou versão inválido.")
        if not _identifier(message["message_id"]) or message["session_id"] != self.session_id or self.negotiated is None:
            raise ProtocolError("Sessão obsoleta ou identificador inválido.")
        if type(message["sequence"]) is not int or not 0 <= message["sequence"] <= 2147483647 or not isinstance(message["payload"], dict) or type(message["size"]) is not int or message["size"] != len(_encode(message["payload"])):
            raise ProtocolError("Sequência, tamanho ou payload inválido.")
        kind, payload = message["type"], message["payload"]
        required = {"CONTROL": "control", "MEDIA_AUDIO": "media:audio", "MEDIA_IMAGE": "media:image", "HEARTBEAT": "status", "DEVICE_STATUS": "status", "BUTTON_PRESSED": "status", "CANCEL": None, "SESSION_END": None}
        if not isinstance(kind, str) or kind not in required or (required[kind] and required[kind] not in self.negotiated["capabilities"]):
            raise ProtocolError("Tipo não suportado ou capacidade não negociada.")
        if kind == "CONTROL" and (not isinstance(payload.get("command"), str) or payload.get("command") not in self.handlers or not isinstance(payload.get("args"), dict)):
            raise ProtocolError("Comando local não registrado ou argumentos inválidos.")
        cancel_event = self.cancelled
        digest = hashlib.sha256(_encode({"type": kind, "payload": payload})).hexdigest()
        with connect(self.db_path) as connection:
            connection.execute("BEGIN IMMEDIATE")
            session = connection.execute("SELECT * FROM link_sessions WHERE id=?", (self.session_id,)).fetchone()
            if session is None or session["state"] != "active":
                raise ProtocolError("Sessão encerrada; inicie uma nova sessão.")
            existing = connection.execute("SELECT * FROM link_commands WHERE device_id=? AND message_id=?", (session["device_id"], message["message_id"])).fetchone()
            if existing:
                if existing["digest"] != digest:
                    raise ProtocolError("Replay conflitante: ID já usado para outro conteúdo.")
                connection.execute("UPDATE link_sessions SET last_sequence=MAX(last_sequence,?) WHERE id=?", (message["sequence"], self.session_id))
                return self._ack(message, existing["state"], json.loads(existing["result"]) if existing["result"] else None, True)
            if message["sequence"] <= session["last_sequence"]:
                raise ProtocolError("Sequência antiga sem comando conhecido; replay rejeitado.")
            connection.execute("UPDATE link_sessions SET last_sequence=? WHERE id=?", (message["sequence"], self.session_id))
            if kind in {"CANCEL", "SESSION_END"}:
                connection.execute("UPDATE link_sessions SET state='cancelled' WHERE id=?", (self.session_id,))
            elif kind == "CONTROL":
                connection.execute("INSERT INTO link_commands VALUES (?, ?, ?, ?, 'running', NULL, ?)", (session["device_id"], message["message_id"], self.session_id, digest, utc_now()))
        if kind in {"CANCEL", "SESSION_END"}:
            self.cancelled.set()
            self.fragments.clear()
            return self._ack(message, "cancelled")
        if kind.startswith("MEDIA_"):
            try:
                data = base64.b64decode(payload["data"], validate=True)
                media_format = payload["format"]
                if not isinstance(media_format, str) or len(media_format) > 64:
                    raise ValueError("Formato de mídia inválido")
            except (KeyError, ValueError, TypeError) as error:
                raise ProtocolError("Mídia exige formato e bytes base64 válidos.") from error
            # Only transfer evidence. No media content is persisted or decoded.
            return self._ack(message, "received", {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(), "format": media_format})
        if kind != "CONTROL":
            return self._ack(message, "received")
        try:
            result = self.handlers[payload["command"]](payload["args"], cancel_event)
            if not isinstance(result, dict) or type(result.get("ok")) is not bool:
                raise ProtocolError("Handler deve fornecer resultado com ok booleano.")
            encoded_result = _encode(result)
            if len(encoded_result) > MAX_MESSAGE_BYTES:
                raise ProtocolError("Resultado excede 64 KiB.")
            state = "completed" if result["ok"] else "failed"
        except Exception as error:
            # A handler may fail after a side effect. Never turn this into retry.
            state = "needs_reconciliation"
            result = {"ok": False, "status": state, "error_code": type(error).__name__, "message": "Handler interrompido; confira o efeito antes de continuar."}
            encoded_result = _encode(result)
        with connect(self.db_path) as connection:
            connection.execute("UPDATE link_commands SET state=?, result=? WHERE device_id=? AND message_id=?", (state, encoded_result.decode("utf-8"), session["device_id"], message["message_id"]))
        return self._ack(message, state, result)


def demo() -> dict:
    """Deterministic local exchange; no personal files, radio or network used."""
    counter = {"value": 0}
    def increment(args, cancelled):
        counter["value"] += args["amount"]
        return {"ok": True, "counter": counter["value"]}
    with tempfile.TemporaryDirectory(prefix="marvin-link-simulator-") as directory:
        simulator = LinkSimulator(Path(directory) / "link.db", {"counter.increment": increment})
        capabilities = simulator.hello([VERSION], ["control", "media:audio"], 256)
        session = simulator.start_session()
        command = make_message(session, 1, "CONTROL", {"command": "counter.increment", "args": {"amount": 1}})
        response = None
        for frame in fragment_message(command, 256):
            response = simulator.receive_frame(frame) or response
        first = response
        replay = simulator.receive(command)
        simulator.disconnect()
        simulator.hello([VERSION], ["control"])
        reconnected = simulator.start_session()
        retry = simulator.receive(make_message(reconnected, 1, "CONTROL", command["payload"], command["message_id"]))
        cancellation = simulator.receive(make_message(reconnected, 2, "CANCEL", {}))
        return {"simulated": True, "transport": "in-process; no radio", "negotiated": capabilities, "first": first,
                "replay": replay, "after_reconnect": retry, "cancel": cancellation, "actual_handler_calls": counter["value"]}


def main() -> None:
    parser = argparse.ArgumentParser(description="MARVIN Link: simulador local, sem Bluetooth ou hardware")
    parser.add_argument("--demo", action="store_true", help="Executar troca simulada com replay e reconexão")
    args = parser.parse_args()
    if args.demo:
        print(json.dumps(demo(), indent=2, ensure_ascii=False))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
