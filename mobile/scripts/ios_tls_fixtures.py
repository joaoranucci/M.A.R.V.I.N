"""Ephemeral HTTPS fixtures for the exact Swift URLSession transport. Never uses user credentials."""
from __future__ import annotations

import argparse
import base64
from datetime import datetime, timedelta, timezone
from hashlib import sha256
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import ipaddress
import json
from pathlib import Path
import ssl
import threading
import time

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec, rsa
from cryptography.x509.oid import ExtendedKeyUsageOID, NameOID


def generate(root: Path, name: str) -> dict:
    now = datetime.now(timezone.utc)
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048) if name == "rsa" else ec.generate_private_key(ec.SECP256R1())
    subject = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "MARVIN test fixture")])
    start = now - timedelta(days=1)
    end = now + timedelta(days=7)
    if name == "expired":
        start, end = now - timedelta(days=7), now - timedelta(days=2)
    if name == "future":
        start = now + timedelta(days=2)
    names = [x509.DNSName("wrong-host.invalid")] if name == "wrong-host" else [x509.IPAddress(ipaddress.ip_address("127.0.0.1")), x509.DNSName("localhost")]
    cert = (x509.CertificateBuilder().subject_name(subject).issuer_name(subject)
            .public_key(key.public_key()).serial_number(x509.random_serial_number())
            .not_valid_before(start).not_valid_after(end)
            .add_extension(x509.SubjectAlternativeName(names), critical=False)
            .add_extension(x509.BasicConstraints(ca=False, path_length=None), critical=True)
            .add_extension(x509.ExtendedKeyUsage([ExtendedKeyUsageOID.SERVER_AUTH]), critical=False)
            .sign(key, hashes.SHA256()))
    (root / (name + ".pem")).write_bytes(cert.public_bytes(serialization.Encoding.PEM))
    (root / (name + ".der")).write_bytes(cert.public_bytes(serialization.Encoding.DER))
    private = root / (name + ".key")
    private.write_bytes(key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8, serialization.NoEncryption()))
    private.chmod(0o600)
    spki = key.public_key().public_bytes(serialization.Encoding.DER, serialization.PublicFormat.SubjectPublicKeyInfo)
    return {"pin": base64.b64encode(sha256(spki).digest()).decode("ascii")}


def serve(root: Path, name: str) -> ThreadingHTTPServer:
    counts = {"requests": 0, "authorized": 0}
    lock = threading.Lock()

    class Handler(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"

        def log_message(self, *_args):
            pass

        def reply(self, status, body, content_type="application/json", headers=None):
            data = body if isinstance(body, bytes) else json.dumps(body).encode()
            try:
                self.send_response(status)
                self.send_header("Content-Type", content_type)
                self.send_header("Content-Length", str(len(data)))
                self.send_header("Cache-Control", "no-store")
                for key, value in (headers or {}).items():
                    self.send_header(key, value)
                self.end_headers()
                self.wfile.write(data)
            except (BrokenPipeError, ConnectionResetError, ssl.SSLError):
                pass

        def count(self):
            with lock:
                counts["requests"] += 1
                counts["authorized"] += int(self.headers.get("Authorization") is not None)

        def do_GET(self):
            path = self.path.split("?")[0]
            if path == "/v1/count":
                with lock:
                    snapshot = dict(counts)
                return self.reply(200, snapshot)
            self.count()
            if path == "/v1/redirect":
                return self.reply(302, {}, headers={"Location": "https://localhost:%d/v1/health" % self.server.server_port})
            if path == "/v1/binary":
                return self.reply(200, bytes(range(256)), "audio/wav")
            if path == "/v1/slow":
                time.sleep(2)
            if path == "/v1/events":
                time.sleep(0.1)
                return self.reply(200, {"events": [], "last_seq": 0, "reset": False})
            return self.reply(200, {"ok": True})

        def do_POST(self):
            self.count()
            data = self.rfile.read(int(self.headers.get("Content-Length", "0")))
            valid = all(part in data for part in [b'name="client_id"', b"document-test", b'name="category"', b'name="file"', "português".encode()])
            return self.reply(201 if valid else 400, {"multipart_ok": valid})

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    server.daemon_threads = True
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.load_cert_chain(str(root / (name + ".pem")), str(root / (name + ".key")))
    server.socket = context.wrap_socket(server.socket, server_side=True)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--serve", action="store_true")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    fixtures = {}
    servers = []
    for name in ["valid", "expired", "future", "wrong-host", "rsa"]:
        fixtures[name] = generate(args.output, name)
        if args.serve:
            server = serve(args.output, name)
            servers.append(server)
            fixtures[name]["port"] = server.server_port
    (args.output / "fixtures.json").write_text(json.dumps(fixtures), encoding="utf-8")
    if args.serve:
        threading.Event().wait()


if __name__ == "__main__":
    main()
