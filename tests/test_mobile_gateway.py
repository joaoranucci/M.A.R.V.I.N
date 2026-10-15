"""Mobile gateway: pairing, events, conversation, desktop commands, memories, documents, items.

The Vault is a loopback HTTP fake implementing only the v0.3 routes the adapter uses.
Presence runs without audio; desktop effects use injected handlers (nothing opens on this PC).
"""
import json
import tempfile
import threading
import time
import unittest
import uuid
from datetime import datetime, timedelta, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

from fastapi.testclient import TestClient

from marvin.gateway.config import GatewayConfig
from marvin.gateway.desktop import DesktopAgent
from marvin.gateway.server import Gateway
from marvin.gateway.store import iso
from marvin.gateway.tls import ensure_identity, spki_pin
from marvin.presence import Presence
from marvin.workspace import ProjectWorkspace

TOKEN = "t" * 48


class FakeVault:
    def __init__(self):
        self.entries = {}
        self.ask_available = False
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), self._handler())
        self.url = f"http://127.0.0.1:{self.server.server_address[1]}"
        threading.Thread(target=self.server.serve_forever, daemon=True).start()

    def close(self):
        self.server.shutdown()
        self.server.server_close()

    def _handler(vault):
        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass

            def _send(self, status, body=None):
                raw = b"" if body is None else json.dumps(body).encode()
                self.send_response(status)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(raw)))
                self.end_headers()
                self.wfile.write(raw)

            def _auth(self):
                if self.headers.get("Authorization") != "Bearer " + TOKEN:
                    self._send(401, {"detail": "Token invalido"})
                    return False
                return True

            def _body(self):
                return self.rfile.read(int(self.headers.get("Content-Length", 0)))

            def do_GET(self):
                parts = urlsplit(self.path)
                query = {k: v[0] for k, v in parse_qs(parts.query).items()}
                if parts.path == "/health":
                    return self._send(200, {"ok": True, "service": "marvin-vault", "version": "0.3.0"})
                if not self._auth():
                    return
                if parts.path == "/v1/status":
                    return self._send(200, {"ok": True, "version": "0.3.0", "memories": len(vault.entries),
                                            "documents": 0, "chunks": 0, "categories": [], "search": "bm25"})
                if parts.path == "/v1/entries":
                    items = [e for e in vault.entries.values() if not query.get("kind") or e["kind"] == query["kind"]]
                    if query.get("q"):
                        items = [e for e in items if query["q"].casefold() in json.dumps(e).casefold()]
                    offset, limit = int(query.get("offset", 0)), int(query.get("limit", 50))
                    return self._send(200, items[offset:offset + limit])
                if parts.path.startswith("/v1/entries/"):
                    entry = vault.entries.get(parts.path.rsplit("/", 1)[1])
                    return self._send(200, entry) if entry else self._send(404, {"detail": "Registro nao encontrado"})
                if parts.path == "/v1/knowledge/search":
                    hits = [{"chunk_id": e["id"], "document_id": e["attributes"]["document_id"], "filename": e["title"],
                             "part": e["attributes"]["part"], "category": e["attributes"]["category"], "score": 1.0,
                             "text": e["body"]} for e in vault.entries.values() if e["kind"] == "trecho_documento"
                            and query["q"].split()[0].casefold() in e["body"].casefold()]
                    return self._send(200, hits)
                self._send(404, {"detail": "Not Found"})

            def do_POST(self):
                if not self._auth():
                    return
                if self.path == "/v1/entries":
                    data = json.loads(self._body())
                    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
                    entry = {"id": str(uuid.uuid4()), "created_at": now, "updated_at": now, **data}
                    vault.entries[entry["id"]] = entry
                    return self._send(201, entry)
                if self.path == "/v1/knowledge/upload":
                    raw = self._body()
                    name = raw.split(b'filename="', 1)[1].split(b'"', 1)[0].decode()
                    if name.endswith(".pdf"):
                        return self._send(400, {"detail": "Nenhum texto util encontrado. PDF escaneado exige OCR (nao incluido)."})
                    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
                    doc = {"id": str(uuid.uuid4()), "kind": "documento_importado", "title": name, "created_at": now,
                           "updated_at": now, "body": {}, "tags": [],
                           "attributes": {"category": "geral", "chunk_count": 1, "sha256": "x", "extension": ".md"}}
                    chunk = {"id": str(uuid.uuid4()), "kind": "trecho_documento", "title": name, "created_at": now,
                             "updated_at": now, "tags": [], "body": raw.split(b"\r\n\r\n", 2)[2].split(b"\r\n--")[0].decode(),
                             "attributes": {"document_id": doc["id"], "part": 1, "total": 1, "category": "geral"}}
                    vault.entries.update({doc["id"]: doc, chunk["id"]: chunk})
                    return self._send(201, {"status": "importado", "document_id": doc["id"], "filename": name, "chunks": 1})
                if self.path == "/v1/knowledge/ask":
                    if not vault.ask_available:
                        return self._send(503, {"detail": "Nao consegui consultar o Ollama local."})
                self._send(404, {"detail": "Not Found"})

            def do_PUT(self):
                if not self._auth():
                    return
                entry_id = self.path.rsplit("/", 1)[1]
                if entry_id not in vault.entries:
                    return self._send(404, {"detail": "Registro nao encontrado"})
                data = json.loads(self._body())
                current = vault.entries[entry_id]
                current.update(data)
                current["updated_at"] = datetime.now(timezone.utc).isoformat(timespec="microseconds")
                self._send(200, current)

            def do_DELETE(self):
                if not self._auth():
                    return
                if self.headers.get("X-Confirm-Delete") != "yes":
                    return self._send(409, {"detail": "confirme"})
                entry_id = self.path.rsplit("/", 1)[1]
                if vault.entries.pop(entry_id, None) is None:
                    return self._send(404, {"detail": "Registro nao encontrado"})
                self._send(204)
        return Handler


class GatewayTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.vault = FakeVault()
        token_file = root / "api-token.txt"
        token_file.write_text(TOKEN, encoding="utf-8")
        self.presence = Presence(root / "data", ProjectWorkspace(root / "projects"), audio=False)
        self.presence.start()
        self.effects = []
        handlers = {
            "open_browser": lambda p: self.effects.append(("browser", p)) or {"state": "dispatched", "message": "ok"},
            "create_project_folder": lambda p: {"state": "completed", "verified": True, "message": "criada",
                                                "result": self.presence.workspace.create_project(p["name"])},
            "lock_screen": lambda p: self.effects.append(("lock", p)) or {"state": "dispatched", "message": "ok"},
        }
        self.config = GatewayConfig(data_dir=root / "data", vault_url=self.vault.url, vault_token_file=token_file,
                                    ollama_url="http://127.0.0.1:9")
        self.gateway = Gateway(self.config, self.presence, desktop_handlers=handlers)
        self.gateway.start_services()
        self.client = TestClient(self.gateway.app)
        self.auth = self.pair()

    def tearDown(self):
        self.client.close()
        self.gateway.close()
        self.presence.close()
        self.vault.close()
        self.tmp.cleanup()

    def pair(self, name="Pixel"):
        code = self.gateway.pairing.create_code()["code"]
        response = self.client.post("/v1/pair", json={"code": code, "device_name": name, "platform": "android"})
        self.assertEqual(response.status_code, 201, response.text)
        return {"Authorization": "Bearer " + response.json()["token"]}

    def wait_event(self, kind, predicate=lambda d: True, after=0, timeout=10):
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            batch = self.client.get(f"/v1/events?after={after}&wait=1", headers=self.auth).json()
            for event in batch["events"]:
                if event["type"] == kind and predicate(event["data"]):
                    return event
            after = batch["last_seq"]
        self.fail(f"evento {kind} não chegou")

    # ---- pairing ------------------------------------------------------------
    def test_pairing_codes_are_single_use_and_tokens_revocable(self):
        self.assertTrue(self.client.get("/v1/health").json()["ok"])
        self.assertEqual(self.client.get("/v1/capabilities").status_code, 401)
        self.assertEqual(self.client.get("/v1/capabilities", headers={"Authorization": "Bearer nope"}).status_code, 401)
        code = self.gateway.pairing.create_code()["code"]
        wrong = "000000" if code != "000000" else "111111"
        self.assertEqual(self.client.post("/v1/pair", json={"code": wrong, "device_name": "X"}).status_code, 401)
        first = self.client.post("/v1/pair", json={"code": code, "device_name": "Tablet"})
        self.assertEqual(first.status_code, 201)
        self.assertEqual(self.client.post("/v1/pair", json={"code": code, "device_name": "Outro"}).status_code, 401)
        token = {"Authorization": "Bearer " + first.json()["token"]}
        self.assertEqual(self.client.get("/v1/session", headers=token).status_code, 200)
        self.assertEqual(self.client.delete("/v1/devices/self", headers=token).status_code, 204)
        self.assertEqual(self.client.get("/v1/session", headers=token).status_code, 401)
        self.assertEqual(self.client.get("/v1/session", headers=self.auth).status_code, 200)
        stored = json.dumps(self.gateway.store.all("SELECT * FROM devices"))
        self.assertNotIn(first.json()["token"], stored)

    def test_code_invalidated_after_five_failures(self):
        code = self.gateway.pairing.create_code()["code"]
        wrong = "000000" if code != "000000" else "111111"
        for _ in range(5):
            self.client.post("/v1/pair", json={"code": wrong, "device_name": "X"})
        self.assertEqual(self.client.post("/v1/pair", json={"code": code, "device_name": "X"}).status_code, 401)

    def test_tls_identity_is_stable_and_pinned_by_spki(self):
        cert, key, pin = ensure_identity(self.config.directory, "teste")
        self.assertEqual(pin, spki_pin(cert.read_bytes()))
        self.assertEqual(ensure_identity(self.config.directory, "teste")[2], pin)
        self.assertNotIn(b"PRIVATE", cert.read_bytes())

    # ---- events -------------------------------------------------------------
    def test_event_cursor_dedup_and_reset(self):
        start = self.gateway.events.last_seq
        seqs = [self.gateway.events.publish("test.ping", {"n": i}) for i in range(3)]
        batch = self.client.get(f"/v1/events?after={start}&wait=0", headers=self.auth).json()
        self.assertEqual([e["seq"] for e in batch["events"] if e["type"] == "test.ping"], seqs)
        again = self.client.get(f"/v1/events?after={batch['last_seq']}&wait=0", headers=self.auth).json()
        self.assertEqual(again["events"], [])
        self.assertTrue(self.client.get("/v1/events?after=999999&wait=0", headers=self.auth).json()["reset"])
        targeted = self.gateway.events.publish("test.private", {}, device_id="someone-else")
        mine = self.client.get(f"/v1/events?after={targeted - 1}&wait=0", headers=self.auth).json()
        self.assertEqual(mine["events"], [])

    # ---- conversation ---------------------------------------------------------
    def test_message_is_idempotent_and_answer_reaches_device(self):
        cursor = self.gateway.events.last_seq
        body = {"client_id": "msg-" + uuid.uuid4().hex, "text": "que horas são", "source": "voice"}
        first = self.client.post("/v1/conversation/messages", json=body, headers=self.auth)
        self.assertEqual(first.status_code, 202, first.text)
        task_id = first.json()["task_id"]
        event = self.wait_event("assistant.answer", lambda d: d["task_id"] == task_id, after=cursor)
        self.assertEqual(event["data"]["origin"], "mobile")
        self.assertIn("Agora são", event["data"]["text"])
        repeat = self.client.post("/v1/conversation/messages", json=body, headers=self.auth).json()
        self.assertEqual((repeat["task_id"], repeat["duplicate"]), (task_id, True))
        self.assertEqual(len(self.presence.runtime.tasks.list_tasks()), 1)
        changed = self.client.post("/v1/conversation/messages", json={**body, "text": "outra"}, headers=self.auth)
        self.assertEqual(changed.status_code, 409)
        task = self.client.get(f"/v1/assistant/tasks/{task_id}", headers=self.auth).json()
        self.assertEqual((task["state"], task["origin"]), ("completed", "mobile"))
        history = self.client.get("/v1/conversation/history", headers=self.auth).json()
        self.assertEqual([m["role"] for m in history[-2:]], ["user", "assistant"])

    def test_mobile_window_commands_do_not_change_pc_screen(self):
        self.client.post("/v1/conversation/messages", json={"client_id": "m-" + uuid.uuid4().hex,
                                                           "text": "Marvin, modo compacto"}, headers=self.auth)
        self.assertFalse(self.presence.compact)

    def test_cancel_only_the_selected_queued_task(self):
        with self.presence.runtime.desktop_lock:  # hold the executor so both tasks stay queued
            a = self.client.post("/v1/conversation/messages", json={"client_id": "a-" + uuid.uuid4().hex,
                                                                   "text": "que horas são"}, headers=self.auth).json()
            b = self.client.post("/v1/conversation/messages", json={"client_id": "b-" + uuid.uuid4().hex,
                                                                   "text": "que dia é hoje"}, headers=self.auth).json()
            state = self.client.post(f"/v1/assistant/tasks/{b['task_id']}/cancel", headers=self.auth).json()["state"]
            self.assertEqual(state, "cancelled")
        task_a = self.client.get(f"/v1/assistant/tasks/{a['task_id']}?wait=10", headers=self.auth).json()
        self.assertEqual(task_a["state"], "completed")
        self.assertEqual(self.client.get(f"/v1/assistant/tasks/{b['task_id']}", headers=self.auth).json()["state"], "cancelled")

    # ---- desktop commands -------------------------------------------------------
    def command(self, action, params=None, **extra):
        body = {"command_id": "cmd-" + uuid.uuid4().hex, "action": action, "params": params or {}, **extra}
        return body, self.client.post("/v1/desktop/commands", json=body, headers=self.auth)

    def wait_command(self, command_id, timeout=5):
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            record = self.client.get(f"/v1/desktop/commands/{command_id}", headers=self.auth).json()
            if record["state"] not in {"received", "started"}:
                return record
            time.sleep(.05)
        self.fail("comando não terminou")

    def test_command_lifecycle_dedup_and_validation(self):
        body, response = self.command("create_project_folder", {"name": "projeto-celular"})
        self.assertEqual(response.status_code, 202, response.text)
        self.assertEqual(response.json()["state"], "received")
        record = self.wait_command(body["command_id"])
        self.assertEqual((record["state"], record["verified"]), ("completed", True))
        self.assertTrue((Path(self.tmp.name) / "projects" / "projeto-celular").is_dir())
        again = self.client.post("/v1/desktop/commands", json=body, headers=self.auth)
        self.assertEqual((again.status_code, again.json()["duplicate"]), (200, True))
        reused = self.client.post("/v1/desktop/commands", json={**body, "params": {"name": "outro"}}, headers=self.auth)
        self.assertEqual(reused.status_code, 409)
        self.assertEqual(self.command("open_browser", {"url": "http://inseguro.test"})[1].status_code, 422)
        self.assertEqual(self.command("open_app", {"name": "calc & del"})[1].status_code, 422)
        self.assertEqual(self.command("format_disk")[1].status_code, 422)
        self.assertEqual(self.command("open_browser", {"extra": "x"})[1].status_code, 422)

    def test_destructive_action_requires_explicit_confirmation(self):
        _, response = self.command("lock_screen")
        self.assertEqual(response.status_code, 428)
        self.assertIn("preview", response.json()["error"])
        self.assertEqual(self.effects, [])
        body, response = self.command("lock_screen", confirmed=True)
        self.assertEqual(response.status_code, 202)
        self.assertEqual(self.wait_command(body["command_id"])["state"], "dispatched")
        self.assertEqual(self.effects, [("lock", {})])

    def test_expired_commands_never_run(self):
        past = iso(datetime.now(timezone.utc) - timedelta(seconds=1))
        self.assertEqual(self.command("open_browser", expires_at=past)[1].status_code, 410)
        far = iso(datetime.now(timezone.utc) + timedelta(hours=1))
        self.assertEqual(self.command("open_browser", expires_at=far)[1].status_code, 422)
        soon = iso(datetime.now(timezone.utc) + timedelta(seconds=1))
        with self.presence.runtime.desktop_lock:  # PC busy longer than the validity
            body, response = self.command("open_browser", expires_at=soon)
            self.assertEqual(response.status_code, 202)
            time.sleep(1.5)
        self.assertEqual(self.wait_command(body["command_id"])["state"], "expired")
        self.assertEqual(self.effects, [])

    def test_restart_does_not_replay_pending_commands(self):
        now = iso()
        self.gateway.store.execute("INSERT INTO commands(id, device_id, action, params, state, created_at, expires_at, updated_at)"
                                   " VALUES ('pending-1', 'd', 'open_browser', '{}', 'received', ?, ?, ?)", (now, now, now))
        DesktopAgent(self.gateway.store, self.gateway.events, self.presence, handlers={})
        self.assertEqual(self.gateway.desktop.get("pending-1")["state"], "expired")

    def test_cancel_before_start(self):
        with self.presence.runtime.desktop_lock:
            body, _ = self.command("open_browser")
            cancelled = self.client.post(f"/v1/desktop/commands/{body['command_id']}/cancel", headers=self.auth).json()
            self.assertEqual(cancelled["state"], "cancelled")
        time.sleep(.3)
        self.assertEqual(self.effects, [])

    # ---- memories ----------------------------------------------------------------
    def test_memories_roundtrip_with_origin_and_conflicts(self):
        body = {"client_id": "mem-" + uuid.uuid4().hex, "content": "Prefiro estudar depois do trabalho.",
                "category": "preferencia", "origin": "user_request", "source": "mobile-voice"}
        created = self.client.post("/v1/memories", json=body, headers=self.auth)
        self.assertEqual(created.status_code, 201, created.text)
        memory = created.json()
        self.assertEqual((memory["origin"], memory["source"], memory["category"]), ("user_request", "mobile-voice", "preferencia"))
        duplicate = self.client.post("/v1/memories", json=body, headers=self.auth)
        self.assertEqual((duplicate.status_code, duplicate.json()["id"]), (200, memory["id"]))
        self.assertEqual(len(self.client.get("/v1/memories", headers=self.auth).json()), 1)
        found = self.client.get("/v1/memories?q=estudar", headers=self.auth).json()
        self.assertEqual(found[0]["id"], memory["id"])
        update = {"content": "Prefiro estudar à noite.", "category": "preferencia", "origin": "user_request",
                  "base_updated_at": memory["updated_at"]}
        updated = self.client.put(f"/v1/memories/{memory['id']}", json=update, headers=self.auth)
        self.assertEqual(updated.status_code, 200, updated.text)
        stale = self.client.put(f"/v1/memories/{memory['id']}", json=update, headers=self.auth)
        self.assertEqual(stale.status_code, 409)
        self.assertEqual(stale.json()["error"]["server_item"]["content"], "Prefiro estudar à noite.")
        self.assertEqual(self.client.delete(f"/v1/memories/{memory['id']}", headers=self.auth).status_code, 204)
        self.assertEqual(self.client.get("/v1/memories", headers=self.auth).json(), [])

    def test_vault_offline_is_reported_not_faked(self):
        self.vault.close()
        response = self.client.get("/v1/memories", headers=self.auth)
        self.assertEqual((response.status_code, response.json()["error"]["code"]), (503, "vault_offline"))
        status = self.client.get("/v1/status", headers=self.auth).json()
        self.assertEqual(status["vault"]["state"], "unavailable")
        self.vault = FakeVault()  # tearDown closes it

    # ---- documents -----------------------------------------------------------------
    def upload(self, name, content=b"# Notas\nSQLite guarda dados locais.", client_id=None):
        return self.client.post("/v1/documents", headers=self.auth,
                                data={"category": "geral", "client_id": client_id or "up-" + uuid.uuid4().hex},
                                files={"file": (name, content, "application/octet-stream")})

    def test_document_states_and_references(self):
        self.assertEqual(self.upload("foto.jpg").status_code, 415)
        response = self.upload("notas.md")
        self.assertEqual(response.status_code, 202, response.text)
        upload_id = response.json()["upload_id"]
        self.assertEqual(response.json()["state"], "received")
        deadline = time.monotonic() + 5
        while time.monotonic() < deadline:
            record = self.client.get(f"/v1/documents/uploads/{upload_id}", headers=self.auth).json()
            if record["state"] in {"available", "failed"}:
                break
            time.sleep(.05)
        self.assertEqual(record["state"], "available")
        states = [e["data"]["state"] for e in self.client.get("/v1/events?after=0&wait=0", headers=self.auth).json()["events"]
                  if e["type"] == "document.upload" and e["data"]["upload_id"] == upload_id]
        self.assertEqual(states[:3], ["received", "processing", "available"])
        hits = self.client.get(f"/v1/knowledge/search?q=SQLite&document_id={record['document_id']}", headers=self.auth).json()
        self.assertEqual(hits[0]["document_id"], record["document_id"])
        chunk = self.client.get(f"/v1/knowledge/chunks/{hits[0]['chunk_id']}", headers=self.auth).json()
        self.assertIn("SQLite", chunk["text"])
        answer = self.client.post("/v1/knowledge/ask", json={"question": "SQLite guarda o quê?",
                                                              "document_id": record["document_id"]}, headers=self.auth).json()
        self.assertFalse(answer["generated"])
        self.assertTrue(answer["llm_unavailable_reason"])
        self.assertEqual(answer["sources"][0]["chunk_id"], hits[0]["chunk_id"])

    def test_scanned_pdf_fails_with_reason(self):
        upload_id = self.upload("digitalizado.pdf", b"%PDF-1.4 fake").json()["upload_id"]
        deadline = time.monotonic() + 5
        while time.monotonic() < deadline:
            record = self.gateway.documents.get(upload_id)
            if record["state"] in {"available", "failed"}:
                break
            time.sleep(.05)
        self.assertEqual(record["state"], "failed")
        self.assertIn("OCR", record["message"])

    def test_upload_retry_is_idempotent(self):
        client_id = "up-" + uuid.uuid4().hex
        first = self.upload("a.md", client_id=client_id).json()
        second = self.upload("a.md", client_id=client_id)
        self.assertEqual((second.status_code, second.json()["upload_id"]), (200, first["upload_id"]))

    # ---- items ---------------------------------------------------------------------
    def test_items_revision_conflicts(self):
        item_id = str(uuid.uuid4())
        created = self.client.put(f"/v1/items/{item_id}", json={"kind": "task", "title": "Estudar"}, headers=self.auth).json()
        self.assertEqual((created["status"], created["item"]["rev"]), ("created", 1))
        ok = self.client.put(f"/v1/items/{item_id}", json={"kind": "task", "title": "Estudar SQL", "base_rev": 1},
                             headers=self.auth).json()
        self.assertEqual(ok["item"]["rev"], 2)
        conflict = self.client.put(f"/v1/items/{item_id}", json={"kind": "task", "title": "Outro", "base_rev": 1},
                                   headers=self.auth)
        self.assertEqual(conflict.status_code, 409)
        self.assertEqual(conflict.json()["error"]["server_item"]["title"], "Estudar SQL")
        same = self.client.put(f"/v1/items/{item_id}", json={"kind": "task", "title": "Estudar SQL", "base_rev": 1},
                               headers=self.auth).json()
        self.assertEqual(same["status"], "unchanged")
        listed = self.client.get("/v1/items", headers=self.auth).json()["items"]
        self.assertEqual(len(listed), 1)

    def test_body_limit(self):
        response = self.client.post("/v1/conversation/messages", headers=self.auth,
                                    content=json.dumps({"client_id": "big-" + "x" * 10, "text": "a" * 300_000}),
                                    )
        self.assertEqual(response.status_code, 413)

    def test_capabilities_and_status_are_honest(self):
        caps = self.client.get("/v1/capabilities", headers=self.auth).json()
        self.assertFalse(caps["documents"]["ocr"])
        ollama = next(e for e in caps["conversation"]["engines"] if e["id"] == "ollama")
        self.assertFalse(ollama["available"])
        actions = {a["id"]: a for a in caps["desktop"]["actions"]}
        self.assertTrue(actions["shutdown"]["requires_confirmation"])
        self.assertFalse(actions["open_app"]["available"])  # no handler injected in this test
        status = self.client.get("/v1/status", headers=self.auth).json()
        self.assertEqual((status["vault"]["state"], status["desktop_agent"]["state"]), ("ok", "online"))


if __name__ == "__main__":
    unittest.main()
