"""Self-signed TLS identity pinned by paired devices (SHA-256 of the SPKI).

The private key never leaves the data directory. Regenerating it invalidates
every pairing, because the pin delivered in the QR code no longer matches.
"""
from __future__ import annotations

import base64
from datetime import timedelta
import hashlib
import ipaddress
import os
from pathlib import Path
import socket

from .config import lan_addresses
from .store import utc_now


def _paths(directory: Path) -> tuple[Path, Path]:
    return directory / "tls" / "gateway-cert.pem", directory / "tls" / "gateway-key.pem"


def spki_pin(cert_pem: bytes) -> str:
    from cryptography import x509
    from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
    cert = x509.load_pem_x509_certificate(cert_pem)
    spki = cert.public_key().public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)
    return base64.b64encode(hashlib.sha256(spki).digest()).decode("ascii")


def display_fingerprint(pin: str) -> str:
    """Short, human-comparable form shown on both screens during manual pairing."""
    digest = base64.b64decode(pin)[:10].hex().upper()
    return "-".join(digest[i:i + 4] for i in range(0, len(digest), 4))


def ensure_identity(directory: Path, server_name: str) -> tuple[Path, Path, str]:
    cert_path, key_path = _paths(directory)
    if cert_path.is_file() and key_path.is_file():
        return cert_path, key_path, spki_pin(cert_path.read_bytes())
    from cryptography import x509
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import ec
    from cryptography.x509.oid import NameOID

    cert_path.parent.mkdir(parents=True, exist_ok=True)
    key = ec.generate_private_key(ec.SECP256R1())
    name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "MARVIN Gateway " + server_name[:40]),
                      x509.NameAttribute(NameOID.ORGANIZATION_NAME, "MARVIN")])
    alt: list[x509.GeneralName] = [x509.DNSName("localhost")]
    try:
        alt.append(x509.DNSName(socket.gethostname()))
    except (OSError, ValueError):
        pass
    for address in ["127.0.0.1", *lan_addresses()]:
        try:
            alt.append(x509.IPAddress(ipaddress.ip_address(address)))
        except ValueError:
            pass
    now = utc_now()
    cert = (x509.CertificateBuilder().subject_name(name).issuer_name(name)
            .public_key(key.public_key()).serial_number(x509.random_serial_number())
            .not_valid_before(now - timedelta(days=1)).not_valid_after(now + timedelta(days=3650))
            .add_extension(x509.SubjectAlternativeName(alt), critical=False)
            .add_extension(x509.BasicConstraints(ca=False, path_length=None), critical=True)
            .sign(key, hashes.SHA256()))
    key_bytes = key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8,
                                  serialization.NoEncryption())
    # Exclusive creation: never overwrite an identity created concurrently.
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_BINARY", 0)
    descriptor = os.open(key_path, flags, 0o600)
    with os.fdopen(descriptor, "wb") as stream:
        stream.write(key_bytes)
    cert_path.write_bytes(cert.public_bytes(serialization.Encoding.PEM))
    return cert_path, key_path, spki_pin(cert_path.read_bytes())
