"""Explicit user shutdown command; fixed arguments, no shell or forced closing."""
import os
from pathlib import Path
import subprocess


def shutdown_computer():
    if os.name != "nt":
        raise OSError("Desligamento disponível somente no Windows.")
    executable = Path(os.environ.get("SystemRoot", r"C:\Windows")) / "System32" / "shutdown.exe"
    # /t 0 avoids the implicit /f of a positive Windows shutdown timeout.
    # Apps with unsaved work may still block shutdown through Windows itself.
    result = subprocess.run([str(executable), "/s", "/t", "0"],
                            shell=False, capture_output=True, timeout=10,
                            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    if result.returncode:
        raise OSError(f"O Windows recusou o desligamento (código {result.returncode}).")
    return "Pedido de desligamento enviado ao Windows."
