"""Comandos da biblioteca tratados localmente antes do agente de nuvem.

Nao grava conversas na memoria antiga nem recorre ao Gemini em caso de falha.
O instalador desativa TTS para esses comandos, pois a voz existente usa nuvem.
"""
from __future__ import annotations

import json
import re
import unicodedata
from marvin_vault.client import VaultClient, VaultClientError


def detect_command(text: str) -> str | None:
    value = text.strip()
    value = re.sub(r"^(?:(?:ei|hey|ola|olá|ok)\s+)?marvin(?:[, :]+|$)", "", value, flags=re.I).strip()
    value = re.sub(r"^por favor[, ]*", "", value, flags=re.I).strip()
    normalized = "".join(c for c in unicodedata.normalize("NFKD", value.casefold())
                         if not unicodedata.combining(c)).strip(" .!?")
    if normalized in {"status da api", "status do cofre", "status da biblioteca", "status api"}:
        return json.dumps({"op": "status", "value": ""})
    patterns = [
        ("save", r"^(?:salv(?:e|ar) na mem[oó]ria|salv(?:e|ar) mem[oó]ria|guarde na mem[oó]ria|lembre que|memorize que)(?:\s*[:,-]\s*|\s+|$)(.*)$"),
        ("memory", r"^(?:busque|buscar|procure|pesquise) (?:na |a )?mem[oó]ria(?:\s*[:,-]\s*|\s+|$)(.*)$"),
        ("search", r"^(?:(?:busque|buscar|procure|pesquise) (?:na biblioteca|nos documentos)|buscar documentos)(?:\s*[:,-]\s*|\s+|$)(.*)$"),
        ("ask", r"^(?:pergunte [aà] biblioteca|perguntar (?:[aà] )?biblioteca|consulte [aà] biblioteca)(?:\s*[:,-]\s*|\s+|$)(.*)$"),
    ]
    for op, pattern in patterns:
        matched = re.match(pattern, value, flags=re.I | re.S)
        if matched:
            return json.dumps({"op": op, "value": matched.group(1).strip()}, ensure_ascii=False)
    return None


def execute_command(serialized: str, *, client: VaultClient | None = None) -> str:
    command = json.loads(serialized)
    operation, value = command["op"], command["value"]
    if operation != "status" and not value:
        return "Informe o conteudo depois do comando. Exemplo: buscar memoria: trabalho."
    try:
        client = client or VaultClient()
        if operation == "save":
            title, separator, body = value.partition("|")
            if not separator:
                body = value
                title = value.splitlines()[0][:120]
            title, body = title.strip(), body.strip()
            if not title or not body or len(title) > 256 or len(body) > 20000:
                return "Use salvar memoria: titulo | conteudo (titulo ate 256; conteudo ate 20000 caracteres)."
            entry = client.salvar_memoria(title, body, tags=["comando-local"])
            return "Memoria salva no cofre local: " + entry["title"]
        if operation == "memory":
            if len(value) > 200:
                return "Use ate 200 caracteres para buscar memorias."
            entries = client.buscar_memoria(value)
            if not entries:
                return "Nao encontrei memorias para essa busca. Tente uma palavra, como trabalho."
            return "Memorias do cofre:\n" + "\n".join(
                "- " + entry["title"] + ": " + str(entry["body"])[:1600] for entry in entries)
        if operation in {"search", "ask"}:
            if not 3 <= len(value) <= 600:
                return "Use de 3 a 600 caracteres para consultar a biblioteca."
            if operation == "search":
                hits = client.buscar_documentos(value)
                if not hits:
                    return "Nao encontrei trechos. Importe documentos ou tente outros termos."
                return "Trechos da biblioteca local:\n\n" + "\n\n".join(
                    f"[FONTE {i}] {hit['filename']} - parte {hit['part']}\n{hit['text']}"
                    for i, hit in enumerate(hits, 1))
            result = client.perguntar_biblioteca(value)
            answer = result["answer"]
            sources = result.get("sources", [])
            if sources:
                answer += "\n\nFontes recuperadas:\n" + "\n".join(
                    f"[FONTE {i}] {s['filename']} - parte {s['part']}"
                    for i, s in enumerate(sources, 1))
            return answer
        if operation == "status":
            data = client.status()
            return (f"API local v{data['version']} conectada. "
                    f"{data['memories']} memorias, {data['documents']} documentos, "
                    f"{data['chunks']} trechos. Busca por palavras (BM25).")
        return "Comando de cofre desconhecido."
    except VaultClientError as exc:
        return "Nao consegui consultar o cofre: " + str(exc)
