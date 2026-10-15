"""Command line: serve, pair, devices, revoke, info.

    python -m marvin.gateway serve        # headless MARVIN + gateway (no window, no PC audio)
    python -m marvin.gateway pair         # temporary code + QR (opens a local page)
    python -m marvin.gateway devices
    python -m marvin.gateway revoke <device_id>
"""
from __future__ import annotations

import argparse
import html
import os
from pathlib import Path
import sys
import time
from urllib.parse import urlencode

from ..config import load_config
from .config import GatewayConfig
from .pairing import Pairing
from .server import Gateway, server_id
from .store import Store
from .tls import display_fingerprint, ensure_identity


def _config(args) -> GatewayConfig:
    data_dir = Path(args.data_dir).resolve() if getattr(args, "data_dir", None) else load_config()
    config = GatewayConfig.from_env(data_dir)
    if getattr(args, "host", None):
        config.host = args.host
    if getattr(args, "port", None):
        config.port = args.port
    if getattr(args, "advertise", None):
        config.advertise_host = args.advertise
    if getattr(args, "no_desktop_actions", False):
        config.desktop_actions = False
    return config


def pairing_url(config: GatewayConfig, code: str, pin: str) -> str:
    query = urlencode({"v": 1, "h": config.advertised(), "p": config.port, "c": code, "k": pin,
                       "n": config.server_name[:40], "s": server_id(config)})
    return "marvin://pair?" + query


def cmd_pair(args) -> None:
    config = _config(args)
    _, _, pin = ensure_identity(config.directory, config.server_name)
    pairing = Pairing(Store(config.database), config.pair_ttl_seconds)
    code = pairing.create_code()
    url = pairing_url(config, code["code"], pin)
    fingerprint = display_fingerprint(pin)
    print("\nMARVIN · vincular celular")
    print(f"  Endereço:  {config.advertised()}:{config.port}")
    print(f"  Código:    {code['code'][:3]} {code['code'][3:]}   (válido por {config.pair_ttl_seconds // 60} min, uso único)")
    print(f"  Impressão digital do PC: {fingerprint}")
    page = None
    try:
        import segno
        qr = segno.make(url, error="m")
        svg = qr.svg_inline(scale=7, border=3, dark="#000000", light="#ffffff")
        page = config.directory / "pareamento.html"
        page.write_text(f"""<!doctype html><meta charset="utf-8"><title>Vincular celular ao MARVIN</title>
<style>body{{background:#05080d;color:#e7f3fb;font:16px system-ui;display:grid;place-items:center;min-height:100vh;margin:0}}
main{{text-align:center;max-width:460px}} .qr{{background:#fff;border-radius:16px;padding:12px;display:inline-block}}
h1{{font-weight:600;letter-spacing:.08em}} code{{font-size:28px;letter-spacing:.2em;color:#5fe0ff}} small{{color:#8aa3b5}}</style>
<main><h1>MARVIN</h1><p>No app, toque em <b>Vincular computador</b> e leia o código abaixo.</p>
<div class="qr">{svg}</div><p>Ou digite o código <code>{html.escape(code['code'])}</code></p>
<p><small>Endereço {html.escape(config.advertised())}:{config.port} · Impressão digital {html.escape(fingerprint)}<br>
Expira em {config.pair_ttl_seconds // 60} minutos. Esta página é apagada ao usar ou expirar.</small></p></main>""",
                        encoding="utf-8")
        if not args.no_open and os.name == "nt":
            os.startfile(str(page))  # noqa: S606 - local file created above
        print(f"  QR Code:   {page}")
    except ImportError:
        print("  (instale segno para gerar o QR Code; o código acima funciona sozinho)")
    print("\nAguardando o celular... (Ctrl+C para sair)")
    try:
        while True:
            state = pairing.code_state(code["id"])
            if state != "active":
                print("Celular vinculado." if state == "used" else "Código expirado. Gere outro se precisar.")
                break
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        if page and page.exists():
            page.unlink()


def cmd_devices(args) -> None:
    pairing = Pairing(Store(_config(args).database))
    devices = pairing.devices()
    if not devices:
        print("Nenhum dispositivo vinculado.")
    for d in devices:
        state = "REVOGADO " + d["revoked_at"] if d["revoked_at"] else "ativo · visto " + str(d["last_seen_at"])
        print(f"{d['id']}  {d['name']:<24} {d['platform']:<8} {state}")


def cmd_revoke(args) -> None:
    pairing = Pairing(Store(_config(args).database))
    print("Acesso revogado." if pairing.revoke(args.device_id) else "Dispositivo não encontrado ou já revogado.")


def cmd_info(args) -> None:
    config = _config(args)
    gateway_dir = config.directory
    _, _, pin = ensure_identity(gateway_dir, config.server_name)
    print(f"Endereço anunciado: https://{config.advertised()}:{config.port}")
    print(f"Escuta em: {config.host}:{config.port}")
    print(f"Impressão digital: {display_fingerprint(pin)}")
    print(f"Dados: {gateway_dir}")


def cmd_serve(args) -> None:
    config = _config(args)
    from ..presence import Presence
    from ..workspace import ProjectWorkspace
    try:
        presence = Presence(config.data_dir, ProjectWorkspace(Path(args.workspace)) if args.workspace else None, audio=False)
    except RuntimeError as exc:
        sys.exit(str(exc) + " Se a janela do MARVIN estiver aberta, ative MARVIN_MOBILE_GATEWAY=true nela.")
    gateway = Gateway(config, presence)
    presence.start()
    print(gateway.describe())
    print("Sem janela e sem áudio no PC. Ctrl+C encerra.")
    try:
        gateway.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        gateway.close()
        presence.close()


def main() -> None:
    parser = argparse.ArgumentParser(prog="python -m marvin.gateway", description="MARVIN Mobile Gateway")
    parser.add_argument("--data-dir")
    sub = parser.add_subparsers(dest="command", required=True)
    serve = sub.add_parser("serve")
    serve.add_argument("--host")
    serve.add_argument("--port", type=int)
    serve.add_argument("--advertise")
    serve.add_argument("--workspace")
    serve.add_argument("--no-desktop-actions", action="store_true")
    pair = sub.add_parser("pair")
    pair.add_argument("--advertise")
    pair.add_argument("--port", type=int)
    pair.add_argument("--no-open", action="store_true")
    sub.add_parser("devices")
    revoke = sub.add_parser("revoke")
    revoke.add_argument("device_id")
    sub.add_parser("info")
    args = parser.parse_args()
    {"serve": cmd_serve, "pair": cmd_pair, "devices": cmd_devices, "revoke": cmd_revoke, "info": cmd_info}[args.command](args)


if __name__ == "__main__":
    main()
