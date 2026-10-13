"""Create/repair an isolated environment while preserving .env, data and projects."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import os
from pathlib import Path
import shutil
import subprocess
import sys
import venv

ROOT = Path(__file__).resolve().parent


def usable(executable):
    try:
        return subprocess.run([str(executable), "-c", "import sys, tkinter; assert sys.version_info >= (3, 11)"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=15,
            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0)).returncode == 0
    except (OSError, subprocess.TimeoutExpired):
        return False


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--core-only", action="store_true", help="Instala somente conversa/texto; áudio é opcional.")
    args = parser.parse_args()
    if sys.version_info < (3, 11):
        raise SystemExit("Instale Python 3.12 x64 (com Tkinter) para o conjunto de recursos validado.")
    target = ROOT / ".venv"
    if target.is_symlink() or target.resolve().parent != ROOT:
        raise SystemExit("A pasta .venv não pode apontar para fora da instalação.")
    executable = target / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    if not usable(executable):
        if target.exists():
            # Exact checked sibling paths, no recursive deletion or shell interpolation.
            saved = ROOT / (".venv.backup-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%f"))
            if saved.parent.resolve() != ROOT:
                raise SystemExit("Destino de backup inválido.")
            target.rename(saved)
            print("Ambiente anterior preservado em", saved.name)
        venv.EnvBuilder(with_pip=True).create(target)
    requirements = ROOT / ("requirements-core.txt" if args.core_only else "requirements.txt")
    code = subprocess.call([str(executable), "-m", "pip", "install", "-r", str(requirements)], cwd=ROOT)
    if code:
        raise SystemExit("Instalação incompleta. Sua configuração e seus dados foram preservados. Confira a rede e a compatibilidade do Python; --core-only instala apenas texto.")
    if not (ROOT / ".env").exists():
        shutil.copyfile(ROOT / ".env.example", ROOT / ".env")
    print("Instalação concluída. Abra C MARVIN.bat. Para conferir recursos, use DIAGNOSTICO.bat.")


if __name__ == "__main__":
    main()
