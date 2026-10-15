"""Certificate upgrades preserve the existing key and the pin used by paired phones."""
from datetime import datetime, timedelta, timezone
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.x509.oid import ExtendedKeyUsageOID, NameOID

from marvin.gateway.tls import ensure_identity, spki_pin


class MobileTLSTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.lan = patch("marvin.gateway.tls.lan_addresses", return_value=["192.168.1.12"])
        self.hostname = patch("marvin.gateway.tls.socket.gethostname", return_value="PC-TESTE")
        self.lan.start()
        self.hostname.start()

    def tearDown(self):
        self.hostname.stop()
        self.lan.stop()
        self.temp.cleanup()

    def test_new_identity_is_stable_and_valid_for_apple_server_auth(self):
        cert_path, key_path, pin = ensure_identity(self.root, "teste")
        first = cert_path.read_bytes()
        private = key_path.read_bytes()
        cert = x509.load_pem_x509_certificate(first)
        self.assertIn(ExtendedKeyUsageOID.SERVER_AUTH, cert.extensions.get_extension_for_class(x509.ExtendedKeyUsage).value)
        self.assertEqual(ensure_identity(self.root, "teste")[2], pin)
        self.assertEqual(cert_path.read_bytes(), first)
        self.assertEqual(key_path.read_bytes(), private)

    def test_legacy_upgrade_adds_eku_without_rotating_key_or_pairing_pin(self):
        folder = self.root / "tls"
        folder.mkdir()
        key = ec.generate_private_key(ec.SECP256R1())
        name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "MARVIN Gateway legado")])
        now = datetime.now(timezone.utc)
        legacy = (x509.CertificateBuilder().subject_name(name).issuer_name(name).public_key(key.public_key())
                  .serial_number(x509.random_serial_number()).not_valid_before(now - timedelta(days=1))
                  .not_valid_after(now + timedelta(days=3650))
                  .add_extension(x509.SubjectAlternativeName([x509.DNSName("localhost")]), critical=False)
                  .add_extension(x509.BasicConstraints(ca=False, path_length=None), critical=True).sign(key, hashes.SHA256()))
        cert_path, key_path = folder / "gateway-cert.pem", folder / "gateway-key.pem"
        private = key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8, serialization.NoEncryption())
        key_path.write_bytes(private)
        old = legacy.public_bytes(serialization.Encoding.PEM)
        cert_path.write_bytes(old)
        pin = spki_pin(old)
        self.assertEqual(ensure_identity(self.root, "teste")[2], pin)
        self.assertEqual(key_path.read_bytes(), private)
        self.assertNotEqual(cert_path.read_bytes(), old)
        self.assertEqual((folder / "gateway-cert.previous.pem").read_bytes(), old)
        self.assertEqual(spki_pin(cert_path.read_bytes()), pin)

    def test_dhcp_and_vpn_san_refresh_preserves_private_key_and_pin(self):
        cert, key, pin = ensure_identity(self.root, "teste")
        private = key.read_bytes()
        with patch("marvin.gateway.tls.lan_addresses", return_value=["10.1.2.3", "100.65.1.12"]):
            self.assertEqual(ensure_identity(self.root, "teste")[2], pin)
        names = x509.load_pem_x509_certificate(cert.read_bytes()).extensions.get_extension_for_class(x509.SubjectAlternativeName).value
        self.assertIn("10.1.2.3", [str(ip) for ip in names.get_values_for_type(x509.IPAddress)])
        self.assertEqual(key.read_bytes(), private)

    def test_missing_existing_key_does_not_silently_replace_identity(self):
        cert, key, _ = ensure_identity(self.root, "teste")
        original = cert.read_bytes()
        key.unlink()
        with self.assertRaises(ValueError):
            ensure_identity(self.root, "teste")
        self.assertEqual(cert.read_bytes(), original)
        self.assertFalse(key.exists())
