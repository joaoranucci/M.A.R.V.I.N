"""Diagnóstico local: endpoints, modelo anunciado e opcional teste com imagem sintética.
Não envia capturas reais da tela. Biblioteca padrão; sem solicitações externas.
"""
from __future__ import annotations
import base64
import json
import os
from pathlib import Path
import struct
import sys
import urllib.error
import urllib.request
import zlib

from dotenv import load_dotenv
from .visual_agent import VisualSettings

ROOT = Path(__file__).resolve().parent.parent


def request_json(url: str, payload: dict | None = None, timeout=12) -> dict:
    raw = json.dumps(payload).encode('utf-8') if payload else None
    req = urllib.request.Request(url, data=raw, headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as exc:
        detail = exc.read(300).decode('utf-8', 'replace')
        raise RuntimeError(f'HTTP {exc.code} em {url}: {detail}') from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f'Servidor nao acessivel em {url}: {exc.reason}') from exc


def make_synthetic_png() -> str:
    """16x16 PNG with a red left half and white right half."""
    def chunk(kind: bytes, body: bytes) -> bytes:
        payload = kind + body
        return struct.pack('>I', len(body)) + payload + struct.pack('>I', zlib.crc32(payload) & 0xffffffff)
    scanline = b'\x00' + b'\xf0\x20\x20' * 8 + b'\xff\xff\xff' * 8
    png = b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB',16,16,8,2,0,0,0)) + chunk(b'IDAT', zlib.compress(scanline * 16)) + chunk(b'IEND',b'')
    return base64.b64encode(png).decode('ascii')


def main() -> int:
    load_dotenv(ROOT/'.env')
    try:
        config=VisualSettings.from_env()
        if not config.base_url.startswith('http://127.0.0.1:8080/v1'):
            print('AVISO: endpoint diferente do servidor local padrao:',config.base_url)
        prefix = config.base_url.rstrip('/')
        print('Testando:', prefix)
        models = request_json(prefix+'/models')
        ids = [m.get('id','') for m in models.get('data',[]) if isinstance(m,dict)]
        print('Modelos anunciados:', ', '.join(ids) or '(vazio)')
        if config.model not in ids:
            print(f'FALHA: UI_TARS_MODEL={config.model!r} nao esta anunciado pelo servidor.')
            return 2
        print('OK - servidor disponivel; nome do modelo encontrado.')
        if '--vision' not in sys.argv:
            print('Para testar de verdade imagem + texto, execute:')
            print(r' .venv\Scripts\python.exe -m marvin.model_probe --vision')
            return 0
        prompt = 'Look at the test image and indicate if the red area is on the left or right. Do not click.'
        payload = {'model': config.model, 'max_tokens': 120, 'temperature':0,
                   'messages':[{'role':'user','content':[{'type':'text','text':prompt},
                   {'type':'image_url','image_url':{'url':'data:image/png;base64,'+make_synthetic_png()}}]}]}
        print('Executando inferencia visual de teste; pode demorar com CPU...')
        result = request_json(prefix+'/chat/completions',payload,timeout=240)
        answer = ((result.get('choices') or [{}])[0].get('message') or {}).get('content')
        print('Resposta visual:', str(answer)[:600])
        if not answer:
            print('FALHA: nenhuma resposta retornada pelo modelo.')
            return 3
        print('OK - endpoint multimodal respondeu. Ainda e preciso validar os comandos UI-TARS.')
        return 0
    except (RuntimeError,ValueError,TimeoutError) as exc:
        print('ERRO:',exc)
        return 1

if __name__ == '__main__':
    raise SystemExit(main())
