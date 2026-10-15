"""Cliente para a API local, sem dependencias adicionais nem senha mestra.

Operacoes POST nao sao repetidas automaticamente. O cliente nao aceita hosts
remotos, proxies ou redirecionamentos. O token nunca entra nas mensagens de erro.
"""
from __future__ import annotations

import json
import os
import uuid
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlsplit
from urllib.request import HTTPRedirectHandler, ProxyHandler, Request, build_opener

DEFAULT_URL = "http://127.0.0.1:8765"
MAX_RESPONSE_BYTES = 2_000_000


class VaultClientError(RuntimeError):
    pass


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def local_url(value: str) -> str:
    try:
        parts = urlsplit(value)
        port = parts.port
    except (TypeError, ValueError):
        raise VaultClientError("Endereco da API invalido.") from None
    if (parts.scheme != "http" or parts.hostname not in {"127.0.0.1", "::1"}
            or parts.username is not None or parts.password is not None
            or parts.path not in {"", "/"} or parts.query or parts.fragment
            or port == 0 or any(c.isspace() for c in value)):
        raise VaultClientError("Use somente http://127.0.0.1:PORTA para a API local.")
    return value.rstrip("/")


def local_json(base: str, route: str, *, token: str | None = None,
               method: str = "GET", payload: Any = None, timeout: float = 10,
               confirm_delete: bool = False) -> Any:
    base = local_url(base)
    if not route.startswith("/") or route.startswith("//") or "\r" in route or "\n" in route:
        raise VaultClientError("Rota da API invalida.")
    headers = {"Accept": "application/json"}
    if token is not None:
        if len(token) < 32 or not token.isascii() or any(c.isspace() for c in token):
            raise VaultClientError("Token local invalido. Confira api-token.txt; nao use a senha mestra.")
        headers["Authorization"] = "Bearer " + token
    body = None
    if payload is not None:
        body = json.dumps(payload, ensure_ascii=False, allow_nan=False).encode("utf-8")
        headers["Content-Type"] = "application/json"
    if confirm_delete:
        headers["X-Confirm-Delete"] = "yes"
    request = Request(base + route, data=body, headers=headers, method=method)
    # Nao respeitar HTTP_PROXY ou o proxy global do Windows para o cofre local.
    opener = build_opener(ProxyHandler({}), NoRedirect())
    try:
        with opener.open(request, timeout=timeout) as response:
            if response.status == 204:
                return None
            raw = response.read(MAX_RESPONSE_BYTES + 1)
    except HTTPError as exc:
        code = exc.code
        exc.close()
        message = {
            401: "Token recusado. Use o api-token.txt do mesmo cofre iniciado pela API.",
            403: "Acesso recusado pela API local.",
            404: "Rota ou registro nao encontrado. Confira a versao da API.",
            413: "Registro maior que o limite da API. Divida o conteudo.",
            422: "Dados invalidos. Confira tamanho e formato dos campos.",
            503: "Ollama indisponivel. Abra o Ollama e instale o modelo configurado.",
        }.get(code, "Falha na API local (HTTP " + str(code) + ").")
        raise VaultClientError(message) from None
    except (URLError, OSError, TimeoutError):
        raise VaultClientError("API local sem resposta. Execute INICIAR_API.bat e mantenha a janela aberta.") from None
    if len(raw) > MAX_RESPONSE_BYTES:
        raise VaultClientError("Resposta da API muito grande. Reduza o limite da consulta.")
    try:
        return json.loads(raw)
    except (ValueError, UnicodeError):
        raise VaultClientError("A API devolveu uma resposta invalida.") from None


class VaultClient:
    def __init__(self, *, base_url: str | None = None, token: str | None = None):
        self.base_url = local_url(base_url or os.getenv("MARVIN_VAULT_URL", DEFAULT_URL))
        self._token = token

    def _read_token(self) -> str:
        if self._token is not None:
            return self._token
        from .config import get_token
        try:
            return get_token()
        except (OSError, UnicodeError):
            raise VaultClientError("api-token.txt nao encontrado. Crie o cofre ou confira MARVIN_VAULT_HOME.") from None

    def _call(self, method: str, route: str, payload: Any = None, *, timeout: float = 10,
              confirm_delete: bool = False):
        return local_json(self.base_url, route, token=self._read_token(), method=method,
                          payload=payload, timeout=timeout, confirm_delete=confirm_delete)

    def health(self) -> dict:
        data = local_json(self.base_url, "/health")
        if not isinstance(data, dict) or data.get("service") != "marvin-vault" or data.get("ok") is not True:
            raise VaultClientError("O servico nessa porta nao e a MARVIN Vault API.")
        return data

    def status(self) -> dict:
        return self._call("GET", "/v1/status")

    def salvar_memoria(self, titulo: str, conteudo: str, *, tags: list[str] | None = None) -> dict:
        return self._call("POST", "/v1/entries", {
            "kind": "memoria", "title": titulo, "body": conteudo,
            "tags": tags or [], "attributes": {"origin": "marvin-local"}})

    def buscar_memoria(self, consulta: str, *, limit: int = 5) -> list[dict]:
        return self._call("GET", "/v1/entries?" + urlencode({
            "q": consulta, "kind": "memoria", "limit": limit}))

    def buscar_documentos(self, consulta: str, *, category: str = "", top_k: int = 4) -> list[dict]:
        return self._call("GET", "/v1/knowledge/search?" + urlencode({
            "q": consulta, "category": category, "top_k": top_k}))

    def perguntar_biblioteca(self, pergunta: str, *, category: str = "", top_k: int = 4) -> dict:
        return self._call("POST", "/v1/knowledge/ask", {
            "question": pergunta, "category": category, "top_k": top_k}, timeout=195)

    def smoke(self) -> dict:
        """Testa escrita/leitura e exclui exclusivamente o registro temporario criado."""
        self.health()
        marker = "Teste temporario " + str(uuid.uuid4())
        item = self.salvar_memoria(marker, "Teste local temporario de escrita e leitura.", tags=["smoke"])
        entry_id = str(uuid.UUID(item["id"]))
        try:
            read = self._call("GET", "/v1/entries/" + entry_id)
            if read.get("title") != marker:
                raise VaultClientError("A leitura do registro temporario falhou.")
        finally:
            self._call("DELETE", "/v1/entries/" + entry_id, confirm_delete=True)
        return {"ok": True, "temporary_record_removed": True}
