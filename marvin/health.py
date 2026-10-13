"""Read-only diagnostics; no network calls, microphone capture or model downloads."""
from __future__ import annotations

import argparse
import importlib.util
from importlib import metadata
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys

from .config import ROOT, VERSION, load_config


def installed(module):
    try:
        return importlib.util.find_spec(module) is not None
    except (ImportError, ValueError):
        return False


def hardware():
    result = {"system": platform.system(), "architecture": platform.machine(),
              "cpu": platform.processor(), "ram_gib": None, "gpus": [],
              "cpu_instructions": "Não verificadas; nenhum novo binário/modelo foi selecionado."}
    if os.name == "nt":
        try:
            import winreg
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\DESCRIPTION\System\CentralProcessor\0") as key:
                result["cpu"] = winreg.QueryValueEx(key, "ProcessorNameString")[0].strip()
            import ctypes
            class MemoryStatus(ctypes.Structure):
                _fields_ = [("length", ctypes.c_ulong), ("load", ctypes.c_ulong),
                            ("total", ctypes.c_ulonglong), ("available", ctypes.c_ulonglong),
                            ("page", ctypes.c_ulonglong), ("avail_page", ctypes.c_ulonglong),
                            ("virtual", ctypes.c_ulonglong), ("avail_virtual", ctypes.c_ulonglong),
                            ("extended", ctypes.c_ulonglong)]
            mem = MemoryStatus()
            mem.length = ctypes.sizeof(mem)
            if ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(mem)):
                result["ram_gib"] = round(mem.total / 1024 ** 3, 1)
        except (OSError, ImportError):
            result["hardware_access"] = "Algumas consultas do Windows não foram autorizadas neste processo."
    nvidia = shutil.which("nvidia-smi")
    if nvidia:
        try:
            proc = subprocess.run([nvidia, "--query-gpu=name,memory.total,driver_version", "--format=csv,noheader"],
                capture_output=True, text=True, timeout=5, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
            if proc.returncode == 0:
                result["gpus"] = proc.stdout.strip().splitlines()[:8]
        except (OSError, subprocess.TimeoutExpired):
            result["gpu_access"] = "Não foi possível consultar VRAM/driver."
    return result


def collect_health(root=ROOT, data_dir=None, include_hardware=False):
    root = Path(root)
    data = Path(data_dir) if data_dir else root / "data"
    versions = {}
    for package in ("google-genai", "python-dotenv", "vosk", "sounddevice", "piper-tts", "pygame", "edge-tts", "pywinauto", "tzdata"):
        try:
            versions[package] = metadata.version(package)
        except metadata.PackageNotFoundError:
            versions[package] = "ausente"
    from .scheduler import TIMEZONE_SOURCE
    capabilities = {
        "texto_local": "disponível",
        "memoria_tarefas_lembretes": "disponível; banco criado/migrado ao iniciar",
        "gemini": "configurado; acesso/cota exigem Testar Google" if os.getenv("GEMINI_API_KEY", "") not in ("", "COLE_SUA_CHAVE_AQUI") else "sem chave; comandos locais disponíveis",
        "microfone": "biblioteca instalada; dispositivo físico não testado" if installed("sounddevice") else "sounddevice ausente",
        "reconhecimento": "instalado; voz real não validada" if installed("vosk") else "vosk ausente",
        "voz_piper": "instalado; saída física não testada" if installed("piper") else "piper ausente",
        "voz_online": "opcional instalada; rede não testada" if installed("edge_tts") else "edge-tts ausente",
        "ui_tars": "SDK instalado; servidor/controle não testados" if (root/"ui_tars_bridge/node_modules/@ui-tars/sdk").exists() else "SDK opcional ausente",
        "pesquisa": "abre navegador; leitura de fontes via URL quando solicitada",
        "interrupcao_voz": "botão/Esc; reconhecimento durante TTS não validado",
        "lembretes": "persistentes; requerem MARVIN aberto, PC acordado e relógio correto",
        "vestivel": "simulador; Bluetooth e hardware físico não validados",
    }
    report = {"version": VERSION, "python": sys.version.split()[0], "executable": sys.executable,
              "data_directory": str(data), "dependencies": versions, "capabilities": capabilities,
              "timezone": TIMEZONE_SOURCE, "node_installed": bool(shutil.which("node")),
              "free_disk_gib": round(shutil.disk_usage(root).free / 1024**3, 1)}
    if include_hardware:
        report["hardware"] = hardware()
    return report


def format_health(report):
    return json.dumps(report, ensure_ascii=False, indent=2)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--hardware", action="store_true")
    args = parser.parse_args()
    data = load_config()
    print(format_health(collect_health(ROOT, data, include_hardware=args.hardware)))


if __name__ == "__main__":
    main()
