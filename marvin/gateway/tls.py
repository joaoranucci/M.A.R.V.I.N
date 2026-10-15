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
    """Keep the device's pinned key; renew only the managed server certificate.

    Apple TLS checks the endpoint SAN and serverAuth EKU. Older MARVIN certificates
    omitted EKU and may predate a DHCP/VPN address change. Reissuing with the SAME
    private key keeps every Android/iPhone pin and every per-device token valid.
    """
    from cryptography import x509
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import ec
    from cryptography.x509.oid import ExtendedKeyUsageOID, NameOID
    from datetime import timezone
    import uuid

    cert_path, key_path = _paths(directory)
    cert_path.parent.mkdir(parents=True, exist_ok=True)
    now = utc_now()
    current = x509.load_pem_x509_certificate(cert_path.read_bytes()) if cert_path.is_file() else None

    names: list[x509.GeneralName] = [x509.DNSName("localhost")]
    try:
        names.append(x509.DNSName(socket.gethostname().encode("idna").decode("ascii")))
    except (OSError, ValueError, UnicodeError):
        pass
    for address in ["127.0.0.1", *lan_addresses()]:
        try:
            names.append(x509.IPAddress(ipaddress.ip_address(address)))
        except ValueError:
            pass

    old_names: list[x509.GeneralName] = []
    server_auth = False
    if current is not None:
        try:
            old_names = list(current.extensions.get_extension_for_class(x509.SubjectAlternativeName).value)
        except x509.ExtensionNotFound:
            pass
        try:
            server_auth = ExtendedKeyUsageOID.SERVER_AUTH in current.extensions.get_extension_for_class(x509.ExtendedKeyUsage).value
        except x509.ExtensionNotFound:
            pass
        expiry = getattr(current, "not_valid_after_utc", None)
        if expiry is None:
            expiry = current.not_valid_after.replace(tzinfo=timezone.utc)
        if server_auth and set(names).issubset(set(old_names)) and expiry > now + timedelta(days=30):
            if not key_path.is_file():
                raise ValueError("A chave TLS existente está ausente. Restaure o backup; ela não será substituída.")
            return cert_path, key_path, spki_pin(cert_path.read_bytes())

    if key_path.is_file():
        key = serialization.load_pem_private_key(key_path.read_bytes(), password=None)
    elif current is not None:
        raise ValueError("A chave TLS existente está ausente. Restaure o backup; ela não será substituída.")
    else:
        key = ec.generate_private_key(ec.SECP256R1())
        key_bytes = key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8, serialization.NoEncryption())
        flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_BINARY", 0)
        try:
            descriptor = os.open(key_path, flags, 0o600)
            with os.fdopen(descriptor, "wb") as stream:
                stream.write(key_bytes)
        except FileExistsError:
            # Another gateway startup won the race. Always use its identity.
            key = serialization.load_pem_private_key(key_path.read_bytes(), password=None)

    if current is not None:
        old_spki = current.public_key().public_bytes(serialization.Encoding.DER, serialization.PublicFormat.SubjectPublicKeyInfo)
        new_spki = key.public_key().public_bytes(serialization.Encoding.DER, serialization.PublicFormat.SubjectPublicKeyInfo)
        if old_spki != new_spki:
            raise ValueError("O certificado e a chave TLS não correspondem. Restaure o backup; nenhum pareamento foi alterado.")
        if current.issuer != current.subject:
            raise ValueError("O certificado TLS externo precisa ser renovado pelo seu emissor para incluir serverAuth e os endereços atuais.")
        subject = current.subject
    else:
        subject = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "MARVIN Gateway " + server_name[:40]),
                             x509.NameAttribute(NameOID.ORGANIZATION_NAME, "MARVIN")])

    all_names = list(dict.fromkeys([*old_names, *names]))
    cert = (x509.CertificateBuilder().subject_name(subject).issuer_name(subject)
            .public_key(key.public_key()).serial_number(x509.random_serial_number())
            .not_valid_before(now - timedelta(days=1)).not_valid_after(now + timedelta(days=397))
            .add_extension(x509.SubjectAlternativeName(all_names), critical=False)
            .add_extension(x509.BasicConstraints(ca=False, path_length=None), critical=True)
            .add_extension(x509.ExtendedKeyUsage([ExtendedKeyUsageOID.SERVER_AUTH]), critical=False)
            .sign(key, hashes.SHA256()))
    temporary = cert_path.with_name(".gateway-cert-" + uuid.uuid4().hex + ".tmp")
    try:
        if current is not None:
            backup = cert_path.with_name("gateway-cert.previous.pem")
            try:
                descriptor = os.open(backup, os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_BINARY", 0), 0o600)
                with os.fdopen(descriptor, "wb") as stream:
                    stream.write(cert_path.read_bytes())
            except FileExistsError:
                pass
        temporary.write_bytes(cert.public_bytes(serialization.Encoding.PEM))
        os.replace(temporary, cert_path)
    finally:
        temporary.unlink(missing_ok=True)
    return cert_path, key_path, spki_pin(cert_path.read_bytes())
