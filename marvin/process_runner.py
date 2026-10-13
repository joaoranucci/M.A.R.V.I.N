"""Approved, bounded project checks. This is not an operating-system sandbox.

No model-provided command strings or executable paths are accepted. An approved
project test still runs with the user's OS account and can have arbitrary side
effects; the approval explicitly describes that limit.
"""
from __future__ import annotations

import json
import math
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import sys
import threading
import time

from .workspace import checked_path


def filtered_environment() -> dict[str, str]:
    allowed = {"PATH", "SYSTEMROOT", "WINDIR", "COMSPEC", "PATHEXT", "TEMP", "TMP", "LANG", "LC_ALL", "TERM"}
    result = {name: value for name, value in os.environ.items() if name.upper() in allowed}
    result.update({"PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1", "PYTHONDONTWRITEBYTECODE": "1",
                   "NO_COLOR": "1", "CI": "true", "npm_config_update_notifier": "false",
                   "npm_config_audit": "false", "npm_config_fund": "false"})
    return result


def _command(folder: Path, check: str) -> list[str]:
    if check == "python-tests":
        return [str(Path(sys.executable).resolve()), "-I", "-B", "-m", "unittest", "discover", "-s", str(folder), "-v"]
    if check not in {"node-test", "node-build"}:
        raise ValueError("Verificação desconhecida. Use python-tests, node-test ou node-build.")
    package = checked_path(folder, Path("package.json"))
    if not package.is_file() or package.stat().st_size > 160_000:
        raise ValueError("package.json ausente ou grande demais.")
    manifest = json.loads(package.read_text(encoding="utf-8-sig"))
    task = "test" if check == "node-test" else "build"
    if not isinstance(manifest, dict) or not isinstance(manifest.get("scripts"), dict) or not isinstance(manifest["scripts"].get(task), str):
        raise ValueError("O projeto não define o script " + task + ".")
    node = shutil.which("node")
    npm = shutil.which("npm")
    if not node or not npm:
        raise FileNotFoundError("Node.js/npm não encontrados. A verificação estática continua disponível.")
    # Invoke npm's JS entry point directly; never launch npm.cmd through a shell.
    npm_path = Path(npm).resolve()
    candidates = [npm_path.parent / "node_modules" / "npm" / "bin" / "npm-cli.js",
                  Path(node).resolve().parent / "node_modules" / "npm" / "bin" / "npm-cli.js", npm_path]
    cli = next((p for p in candidates if p.is_file() and p.name == "npm-cli.js"), None)
    if cli is None:
        raise FileNotFoundError("Entrada npm-cli.js não encontrada para execução sem shell.")
    if Path(node).resolve().is_relative_to(folder) or cli.resolve().is_relative_to(folder):
        raise PermissionError("O runtime deve estar instalado fora do projeto.")
    return [str(Path(node).resolve()), str(cli.resolve()), "--ignore-scripts", "run", task]


class _Capture:
    def __init__(self, maximum=32_000):
        self.maximum = maximum
        self.parts: list[bytes] = []
        self.size = 0
        self.truncated = False
        self.lock = threading.Lock()

    def consume(self, stream):
        try:
            while True:
                chunk = stream.read1(4096)
                if not chunk:
                    break
                with self.lock:
                    room = max(0, self.maximum - self.size)
                    self.parts.append(chunk[:room]) if room else None
                    self.size += min(room, len(chunk))
                    self.truncated |= len(chunk) > room
        except (OSError, ValueError):
            pass
        finally:
            stream.close()

    def text(self):
        with self.lock:
            return b"".join(self.parts).decode("utf-8", errors="replace")


def _terminate(process):
    if os.name == "nt":
        taskkill = Path(os.environ.get("SystemRoot", r"C:\Windows")) / "System32" / "taskkill.exe"
        try:
            subprocess.run([str(taskkill), "/PID", str(process.pid), "/T", "/F"],
                           stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                           timeout=5, creationflags=subprocess.CREATE_NO_WINDOW, check=False)
        except (OSError, subprocess.TimeoutExpired):
            pass
    else:
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
    if process.poll() is None:
        process.kill()
    try:
        process.wait(timeout=3)
    except subprocess.TimeoutExpired:
        pass


def run_project_check(folder: Path, check: str = "python-tests", cancel_event=None,
                      approve_execution=None, timeout: float = 60) -> dict:
    started = time.monotonic()
    folder = Path(folder)
    checked_path(folder.parent.resolve(), Path(folder.name))
    if not folder.is_dir():
        raise FileNotFoundError("Projeto não encontrado.")
    if isinstance(timeout, bool) or not isinstance(timeout, (int, float)) or not math.isfinite(timeout) or not 0 < timeout <= 120:
        raise ValueError("Timeout precisa estar entre 0 e 120 segundos.")
    event = cancel_event if cancel_event is not None else threading.Event()
    if event.is_set():
        return {"ok": False, "status": "cancelled", "message": "Cancelado antes da execução.", "exit_code": None}
    argv = _command(folder, check)
    approval = {"project": folder.name, "directory": str(folder), "check": check, "argv": argv,
                "timeout": timeout,
                "warning": "Executa código do projeto com a sua conta do Windows/sistema. Pode ler arquivos, usar rede e alterar dados; não é uma sandbox. O ambiente não herda chaves de API. Revise o código antes de autorizar."}
    if approve_execution is None or not approve_execution(approval):
        raise PermissionError("Execução requer aprovação explícita do comando e projeto apresentados.")
    checked_path(folder.parent.resolve(), Path(folder.name))
    if argv != _command(folder, check):
        raise RuntimeError("O comando mudou durante a aprovação. Solicite uma nova execução.")
    if event.is_set():
        return {"ok": False, "status": "cancelled", "message": "Cancelado antes da execução.", "exit_code": None}
    options = {"creationflags": subprocess.CREATE_NO_WINDOW | subprocess.CREATE_NEW_PROCESS_GROUP} if os.name == "nt" else {"start_new_session": True}
    process = subprocess.Popen(argv, cwd=folder, env=filtered_environment(), shell=False,
                               stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **options)
    stdout, stderr = _Capture(), _Capture()
    readers = [threading.Thread(target=capture.consume, args=(stream,), daemon=True)
               for capture, stream in ((stdout, process.stdout), (stderr, process.stderr))]
    for reader in readers:
        reader.start()
    execution_started = time.monotonic()
    status = "succeeded"
    while process.poll() is None:
        if event.is_set():
            status = "cancelled"
            _terminate(process)
            break
        if time.monotonic() - execution_started >= timeout:
            status = "timed_out"
            _terminate(process)
            break
        event.wait(0.05)
    for reader in readers:
        reader.join(timeout=1)
    incomplete = any(reader.is_alive() for reader in readers)
    if incomplete:
        _terminate(process)
        for reader in readers:
            reader.join(timeout=1)
    output, errors = stdout.text(), stderr.text()
    if status == "succeeded" and process.returncode != 0:
        status = "failed"
    if status == "succeeded" and incomplete:
        status = "needs_reconciliation"
    count = None
    if check == "python-tests":
        matched = re.search(r"Ran (\d+) tests? in", errors)
        count = int(matched.group(1)) if matched else None
        if status in {"succeeded", "failed"} and count == 0 and process.returncode in {0, 5}:
            status = "not_checked"
    return {"ok": status == "succeeded", "status": status, "check": check, "argv": argv,
            "directory": str(folder), "exit_code": process.returncode, "stdout": output, "stderr": errors,
            "truncated": stdout.truncated or stderr.truncated, "duration_ms": round((time.monotonic() - started) * 1000),
            "evidence": {"pid": process.pid, "exit_code": process.returncode, "test_count": count,
                         "output_complete": not any(reader.is_alive() for reader in readers)},
            "message": "Processo finalizado; efeitos externos do código do projeto não são revertidos automaticamente."}
