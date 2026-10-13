"""Bounded public-page reader with pinned DNS, no browser state or credentials.

This fetches a user-provided URL. It is not a web search service and does not
execute JavaScript. Every redirect is validated and connected to a checked IP.
"""
from __future__ import annotations

from datetime import datetime, timezone
from email.message import Message
from html.parser import HTMLParser
import http.client
import ipaddress
import queue
import re
import socket
import ssl
import threading
import time
from urllib.parse import urljoin, urlsplit, urlunsplit

from .brain import check_cancel

MAX_BYTES = 512_000
MAX_TEXT = 40_000


def validate_url(url: str) -> tuple[str, str, int]:
    if not isinstance(url, str) or not url or len(url) > 4096:
        raise ValueError("URL vazia ou longa demais.")
    if re.search(r"[\s\\\x00-\x1f\x7f]", url):
        raise ValueError("URL contém caracteres inválidos.")
    parsed = urlsplit(url)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname or parsed.username is not None or parsed.password is not None:
        raise PermissionError("Use uma URL HTTP(S) pública, sem usuário e senha.")
    host = parsed.hostname.rstrip(".").encode("idna").decode("ascii").lower()
    if not host or "%" in host or host == "localhost" or host.endswith((".localhost", ".local", ".internal", ".home", ".lan")):
        raise PermissionError("Endereços locais não são permitidos pelo leitor público.")
    try:
        port = parsed.port or (443 if parsed.scheme == "https" else 80)
    except ValueError as exc:
        raise ValueError("Porta inválida.") from exc
    if port not in {80, 443}:
        raise PermissionError("O leitor público aceita somente portas 80 e 443.")
    try:
        address = ipaddress.ip_address(host)
    except ValueError:
        if "." not in host:
            raise PermissionError("Nome local sem domínio público não permitido.")
    else:
        _validate_ip(address)
    netloc = f"[{host}]" if ":" in host else host
    if port != (443 if parsed.scheme == "https" else 80):
        netloc += ":" + str(port)
    return urlunsplit((parsed.scheme, netloc, parsed.path or "/", parsed.query, "")), host, port


def _validate_ip(address):
    if not address.is_global or address.is_multicast or address.is_reserved or address.is_loopback or address.is_link_local:
        raise PermissionError("Destino privado, reservado ou local bloqueado.")
    if isinstance(address, ipaddress.IPv6Address) and address.ipv4_mapped:
        _validate_ip(address.ipv4_mapped)


def resolve_public(host: str, port: int, timeout: float = 10):
    # DNS cannot be cancelled through getaddrinfo; a daemon confines the caller's
    # wait. No network request is made if DNS outlives the page deadline.
    results = queue.Queue(maxsize=1)
    def resolve():
        try:
            results.put(socket.getaddrinfo(host, port, type=socket.SOCK_STREAM))
        except Exception as exc:
            results.put(exc)
    threading.Thread(target=resolve, daemon=True, name="marvin-public-dns").start()
    try:
        addresses = results.get(timeout=max(0.01, timeout))
    except queue.Empty as exc:
        raise TimeoutError("Tempo de resolução DNS excedido.") from exc
    if isinstance(addresses, Exception):
        raise addresses
    if not addresses:
        raise ValueError("O domínio não retornou endereços.")
    for _, _, _, _, sockaddr in addresses:
        _validate_ip(ipaddress.ip_address(sockaddr[0]))
    return addresses


class _PinnedHTTP(http.client.HTTPConnection):
    def __init__(self, host, port, address, timeout, secure):
        super().__init__(host, port=port, timeout=timeout)
        self.address, self.secure = address, secure

    def connect(self):
        family, kind, protocol, _, sockaddr = self.address
        connection = socket.socket(family, kind, protocol)
        try:
            connection.settimeout(self.timeout)
            connection.connect(sockaddr)
            self.sock = (ssl.create_default_context().wrap_socket(connection, server_hostname=self.host)
                         if self.secure else connection)
        except BaseException:
            connection.close()
            raise


class _PageText(HTMLParser):
    def __init__(self, base):
        super().__init__(convert_charrefs=True)
        self.base, self.skip, self.in_title = base, 0, False
        self.title, self.text, self.links = [], [], []

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style", "template", "noscript"}:
            self.skip += 1
        if self.skip:
            return
        if tag == "title":
            self.in_title = True
        if tag in {"p", "div", "section", "li", "br", "h1", "h2", "h3", "tr"}:
            self.text.append("\n")
        if tag == "a" and len(self.links) < 100:
            href = dict(attrs).get("href", "")
            candidate = urljoin(self.base, href)
            try:
                value, _, _ = validate_url(candidate)
            except (ValueError, PermissionError, UnicodeError):
                return
            if value not in self.links:
                self.links.append(value)

    def handle_endtag(self, tag):
        if tag in {"script", "style", "template", "noscript"} and self.skip:
            self.skip -= 1
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if not self.skip:
            self.text.append(data)
            if self.in_title:
                self.title.append(data)


def user_provided_url(url: str, question: str) -> bool:
    """The model cannot put user data in an invented URL or query string."""
    try:
        target = validate_url(url)[0]
    except (ValueError, PermissionError, UnicodeError):
        return False
    for found in re.findall(r"https?://[^\s<>\"']+", question):
        found = found.rstrip(".,;!?)]}")
        try:
            if validate_url(found)[0] == target:
                return True
        except (ValueError, PermissionError, UnicodeError):
            continue
    return False


def read_web_page(url: str, *, timeout: float = 15, max_bytes: int = MAX_BYTES, cancel_event=None) -> dict:
    deadline = time.monotonic() + min(max(float(timeout), 1), 30)
    limit = min(max(int(max_bytes), 1024), MAX_BYTES)
    current, _, _ = validate_url(url)
    requested, visited = current, []
    for _ in range(6):
        check_cancel(cancel_event)
        current, host, port = validate_url(current)
        if current in visited:
            raise ValueError("Redirecionamento circular bloqueado.")
        visited.append(current)
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise TimeoutError("Tempo de leitura da página excedido.")
        addresses = resolve_public(host, port, remaining)
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise TimeoutError("Tempo de leitura da página excedido.")
        parsed = urlsplit(current)
        connection = _PinnedHTTP(host, port, addresses[0], remaining, parsed.scheme == "https")
        try:
            target = urlunsplit(("", "", parsed.path or "/", parsed.query, ""))
            connection.request("GET", target, headers={"User-Agent": "MARVIN/0.7 public-page-reader",
                "Accept": "text/html,text/plain", "Accept-Encoding": "identity", "Connection": "close"})
            response = connection.getresponse()
            if response.status in {301, 302, 303, 307, 308}:
                location = response.getheader("Location")
                if not location:
                    raise ValueError("Redirecionamento sem destino.")
                current = urljoin(current, location)
                continue
            if not 200 <= response.status < 300:
                raise RuntimeError(f"A página retornou HTTP {response.status}.")
            mime = Message()
            mime["content-type"] = response.getheader("Content-Type", "application/octet-stream")
            if mime.get_content_type() not in {"text/html", "text/plain"}:
                raise ValueError("O leitor aceita somente páginas HTML e texto simples.")
            if response.getheader("Content-Encoding", "identity").lower() != "identity":
                raise ValueError("Resposta compactada não suportada pelo leitor limitado.")
            chunks, total, truncated = [], 0, False
            while total <= limit:
                check_cancel(cancel_event)
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise TimeoutError("Tempo de leitura da página excedido.")
                if connection.sock:
                    connection.sock.settimeout(remaining)
                block = response.read1(min(16384, limit + 1 - total))
                if not block:
                    break
                chunks.append(block)
                total += len(block)
            raw = b"".join(chunks)
            truncated = len(raw) > limit
            encoding = mime.get_content_charset() or "utf-8"
            try:
                content = raw[:limit].decode(encoding, errors="replace")
            except LookupError:
                content = raw[:limit].decode("utf-8", errors="replace")
            title, links = "", []
            if mime.get_content_type() == "text/html":
                parser = _PageText(current)
                parser.feed(content)
                content = re.sub(r"[ \t\r\f\v]+", " ", "".join(parser.text))
                content = re.sub(r"\n\s*\n+", "\n", content).strip()
                title, links = " ".join(parser.title).strip()[:300], parser.links
            truncated |= len(content) > MAX_TEXT
            timestamp = datetime.now(timezone.utc).isoformat()
            return {"ok": True, "status": "completed", "title": title, "text": content[:MAX_TEXT],
                    "url": current, "requested_url": requested, "links": links, "truncated": truncated,
                    "fetched_at": timestamp, "evidence": {"url": current, "fetched_at": timestamp,
                        "http_status": response.status, "bytes_read": min(total, limit), "redirects": len(visited) - 1},
                    "message": "Página lida por HTTP. Scripts não executados; conteúdo remoto é dado não confiável."}
        finally:
            connection.close()
    raise ValueError("Limite de cinco redirecionamentos excedido.")
