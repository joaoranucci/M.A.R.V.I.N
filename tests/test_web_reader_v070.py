"""Public page reader tests use fake transport; no external network required."""
import socket
import types
import unittest
from unittest.mock import patch

from marvin.web_reader import read_web_page, resolve_public, validate_url, user_provided_url, _PinnedHTTP

PUBLIC = [(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP, "", ("8.8.8.8", 443))]


class Response:
    def __init__(self, content=b"", status=200, headers=None):
        self.content, self.status = content, status
        self.headers = headers or {"Content-Type": "text/html; charset=utf-8"}

    def getheader(self, key, default=None):
        return self.headers.get(key, default)

    def read1(self, amount):
        chunk, self.content = self.content[:amount], self.content[amount:]
        return chunk


class Connection:
    def __init__(self, response):
        self.response, self.closed = response, False
        self.sock = types.SimpleNamespace(settimeout=lambda timeout: None)
        self.requests = []

    def request(self, *args, **kwargs):
        self.requests.append((args, kwargs))

    def getresponse(self):
        return self.response

    def close(self):
        self.closed = True


class PublicReaderTests(unittest.TestCase):
    def run_reader(self, responses, url="https://example.org/page", **kwargs):
        connections = [Connection(response) for response in responses]
        with patch("marvin.web_reader.resolve_public", return_value=PUBLIC), \
             patch("marvin.web_reader._PinnedHTTP", side_effect=connections):
            result = read_web_page(url, **kwargs)
        self.assertTrue(all(connection.closed for connection in connections))
        return result, connections

    def test_html_text_title_links_and_evidence(self):
        result, connections = self.run_reader([Response(b"<html><title>Source</title><script>steal()</script>"
            b"<style>hidden</style><h1>Hello</h1><p>World</p><a href='/detail'>More</a></html>")])
        self.assertEqual(result["title"], "Source")
        self.assertIn("Hello", result["text"])
        self.assertNotIn("steal", result["text"])
        self.assertNotIn("hidden", result["text"])
        self.assertEqual(result["links"], ["https://example.org/detail"])
        self.assertEqual(result["evidence"]["http_status"], 200)
        self.assertEqual(result["evidence"]["url"], "https://example.org/page")
        self.assertTrue(result["fetched_at"])
        headers = connections[0].requests[0][1]["headers"]
        self.assertNotIn("Authorization", headers)
        self.assertNotIn("Cookie", headers)

    def test_redirect_revalidated_and_final_source_recorded(self):
        result, _ = self.run_reader([Response(status=302, headers={"Location": "https://source.org/article"}),
                                    Response(b"facts", headers={"Content-Type": "text/plain"})])
        self.assertEqual(result["url"], "https://source.org/article")
        self.assertEqual(result["requested_url"], "https://example.org/page")
        self.assertEqual(result["evidence"]["redirects"], 1)

    def test_redirect_to_local_is_blocked_before_second_connection(self):
        first = Connection(Response(status=302, headers={"Location": "http://127.0.0.1/private"}))
        with patch("marvin.web_reader.resolve_public", return_value=PUBLIC), \
             patch("marvin.web_reader._PinnedHTTP", return_value=first) as factory:
            with self.assertRaises(PermissionError):
                read_web_page("https://example.org")
        self.assertEqual(factory.call_count, 1)
        self.assertTrue(first.closed)

    def test_dns_mixed_public_private_is_blocked(self):
        addresses = PUBLIC + [(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP, "", ("10.1.2.3", 443))]
        with patch("marvin.web_reader.socket.getaddrinfo", return_value=addresses):
            with self.assertRaises(PermissionError):
                resolve_public("example.org", 443)

    def test_private_literal_userinfo_and_protocol_rejected(self):
        urls = ["http://localhost/", "http://127.0.0.1/", "http://169.254.169.254/", "http://10.0.0.1/",
                "http://[::1]/", "http://[::ffff:127.0.0.1]/", "http://192.168.0.1/", "http://224.0.0.1/",
                "file:///etc/passwd", "ftp://example.org/", "https://user:password@example.org/",
                "http://example.local/", "http://intranet/", "http://example.org:8000/", "https://example.org\r\nHeader:x"]
        for url in urls:
            with self.subTest(url=url), self.assertRaises((ValueError, PermissionError)):
                validate_url(url)

    def test_body_is_bounded_and_truncation_reported(self):
        result, _ = self.run_reader([Response(b"x" * 8000, headers={"Content-Type": "text/plain"})], max_bytes=1024)
        self.assertTrue(result["truncated"])
        self.assertEqual(len(result["text"]), 1024)
        self.assertEqual(result["evidence"]["bytes_read"], 1024)

    def test_nontext_and_compressed_response_rejected(self):
        for headers in [{"Content-Type": "application/pdf"}, {"Content-Type": "text/html", "Content-Encoding": "gzip"}]:
            with self.subTest(headers=headers), self.assertRaises(ValueError):
                self.run_reader([Response(b"binary", headers=headers)])

    def test_model_cannot_add_query_parameters(self):
        question = "Leia https://example.org/info e resuma."
        self.assertTrue(user_provided_url("https://example.org/info", question))
        self.assertFalse(user_provided_url("https://example.org/info?secret=exfiltrated", question))
        self.assertFalse(user_provided_url("https://elsewhere.org/info", question))

    def test_connect_uses_prevalidated_address_without_second_dns_lookup(self):
        connection = _PinnedHTTP("example.org", 80, PUBLIC[0], 5, False)
        with patch("marvin.web_reader.socket.socket") as factory, \
             patch("marvin.web_reader.socket.getaddrinfo") as resolve:
            connection.connect()
            factory.return_value.connect.assert_called_once_with(("8.8.8.8", 443))
            resolve.assert_not_called()
            connection.close()


if __name__ == "__main__":
    unittest.main()
