"""Descoberta e controle de apps do Windows, sem execução de comandos arbitrários.

Fontes: atalhos do Menu Iniciar/Desktop, Get-StartApps, App Paths (registro).
Somente arquivos existentes e atalhos nas pastas de apps são executados.
Todos os processos são abertos com shell=False; nada de PowerShell criado pela IA.
"""
from __future__ import annotations

from dataclasses import dataclass
from difflib import SequenceMatcher
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import threading
import time
from typing import Iterable
import unicodedata


def fold(value: str) -> str:
    value = unicodedata.normalize("NFKD", value.casefold())
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    value = re.sub(r"[^\w\s]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


@dataclass(frozen=True)
class AppEntry:
    name: str
    kind: str  # shortcut | appid | exe
    target: str
    origin: str = ""


ALIASES = {
    "vscode": "visual studio code", "vs code": "visual studio code",
    "code": "visual studio code", "visual studio": "visual studio",
    "chrome": "google chrome", "google chrome": "google chrome",
    "edge": "microsoft edge", "firefox": "mozilla firefox",
    "discord": "discord", "valorante": "valorant", "valorant": "valorant",
    "cs": "counter strike", "cs2": "counter strike", "steam": "steam",
    "spotify": "spotify", "teams": "microsoft teams",
    "word": "word", "excel": "excel", "powerpoint": "powerpoint",
    "paint": "paint", "bloco de notas": "bloco de notas",
    "notepad": "bloco de notas", "calculadora": "calculadora",
    "explorador de arquivos": "explorador de arquivos",
    "terminal": "terminal", "terminal do windows": "terminal",
}

# Comandos de sistema conhecidos; não há terminal/shell aqui.
BUILTINS = {
    "bloco de notas": "notepad.exe",
    "calculadora": "calc.exe",
    "paint": "mspaint.exe",
    "explorador de arquivos": "explorer.exe",
    "gerenciador de tarefas": "taskmgr.exe",
}


class WindowsAppCatalog:
    def __init__(self, entries: Iterable[AppEntry] | None = None, cache_seconds: float = 180):
        self._entries: list[AppEntry] = list(entries) if entries is not None else []
        self._last_scan = time.monotonic() if entries is not None else 0.0
        self._cache_seconds = cache_seconds
        self._lock = threading.RLock()
        self._fixed = entries is not None

    @staticmethod
    def _shortcut_dirs() -> list[Path]:
        env = os.environ
        bases = [
            Path(env.get("APPDATA", "")) / "Microsoft/Windows/Start Menu/Programs" if env.get("APPDATA") else None,
            Path(env.get("PROGRAMDATA", "")) / "Microsoft/Windows/Start Menu/Programs" if env.get("PROGRAMDATA") else None,
            Path(env.get("USERPROFILE", "")) / "Desktop" if env.get("USERPROFILE") else None,
            Path(env.get("PUBLIC", "")) / "Desktop" if env.get("PUBLIC") else None,
        ]
        return [p for p in bases if p and p.is_dir()]

    @classmethod
    def _from_shortcuts(cls) -> list[AppEntry]:
        entries = []
        for root in cls._shortcut_dirs():
            for ext in ("*.lnk", "*.url", "*.appref-ms"):
                for path in root.rglob(ext):
                    if path.is_file():
                        entries.append(AppEntry(path.stem, "shortcut", str(path), "menu/desktop"))
        return entries

    @staticmethod
    def _from_start_apps() -> list[AppEntry]:
        # Nunca inclui conteúdo transcrito ou obtido da IA nos argumentos PowerShell.
        script = '[Console]::OutputEncoding = [Text.Encoding]::UTF8; Get-StartApps | Select-Object Name,AppID | ConvertTo-Json -Compress -Depth 3'
        flags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
        try:
            result = subprocess.run(
                ["powershell.exe", "-NoProfile", "-NonInteractive", "-Command", script],
                capture_output=True, timeout=18, check=False, creationflags=flags,
            )
            if result.returncode or not result.stdout:
                return []
            data = json.loads(result.stdout.decode("utf-8-sig", errors="replace"))
            data = data if isinstance(data, list) else [data]
            return [AppEntry(obj["Name"], "appid", obj["AppID"], "Get-StartApps")
                    for obj in data if isinstance(obj, dict) and obj.get("Name") and obj.get("AppID")]
        except (OSError, ValueError, subprocess.TimeoutExpired):
            return []

    @staticmethod
    def _from_registry() -> list[AppEntry]:
        try:
            import winreg
        except ImportError:
            return []
        apps = []
        for hive in (winreg.HKEY_CURRENT_USER, winreg.HKEY_LOCAL_MACHINE):
            try:
                parent = winreg.OpenKey(hive, r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths")
            except OSError:
                continue
            with parent:
                index = 0
                while True:
                    try:
                        subname = winreg.EnumKey(parent, index)
                    except OSError:
                        break
                    index += 1
                    try:
                        with winreg.OpenKey(parent, subname) as key:
                            executable, _ = winreg.QueryValueEx(key, "")
                        executable = os.path.expandvars(str(executable)).strip().strip('"')
                        if Path(executable).is_file() and Path(executable).suffix.lower() == ".exe":
                            apps.append(AppEntry(Path(subname).stem, "exe", executable, "registro"))
                    except OSError:
                        continue
        return apps

    def refresh(self) -> list[AppEntry]:
        with self._lock:
            if self._fixed:
                return list(self._entries)
            if platform.system() != "Windows":
                self._entries = []
                self._last_scan = time.monotonic()
                return []
            entries = self._from_shortcuts() + self._from_start_apps() + self._from_registry()
            dedup: dict[tuple[str, str], AppEntry] = {}
            for entry in entries:
                key = (fold(entry.name), entry.target.lower())
                dedup[key] = entry
            self._entries = list(dedup.values())
            self._last_scan = time.monotonic()
            return list(self._entries)

    def all(self) -> list[AppEntry]:
        with self._lock:
            if not self._fixed and (not self._last_scan or time.monotonic() - self._last_scan > self._cache_seconds):
                return self.refresh()
            return list(self._entries)

    def names(self) -> list[str]:
        return sorted({entry.name for entry in self.all()}, key=str.casefold)

    @staticmethod
    def _score(query: str, name: str) -> float:
        if query == name:
            return 1.0
        if name.startswith(query + " "):
            return 0.92
        if query.startswith(name + " "):
            return 0.87
        if len(query) >= 4 and query in name.split():
            return 0.86
        if len(query) >= 5 and query in name:
            return 0.81
        return SequenceMatcher(None, query, name).ratio() * 0.80

    def find(self, query: str) -> AppEntry:
        query = fold(query)
        if not query or len(query) > 100:
            raise ValueError("Nome de aplicativo inválido.")
        name = ALIASES.get(query, query)
        entries = self.all()
        evaluated = [(self._score(name, fold(entry.name)), entry) for entry in entries]
        evaluated.sort(key=lambda item: (item[0], {"shortcut": 3, "exe": 2, "appid": 1}.get(item[1].kind, 0)), reverse=True)
        if not evaluated or evaluated[0][0] < 0.74:
            if name in BUILTINS:
                return AppEntry(name, "exe", BUILTINS[name], "Windows")
            alt = [(self._score(query, fold(entry.name)), entry) for entry in entries]
            alt.sort(key=lambda item: item[0], reverse=True)
            suggestions = ", ".join(dict.fromkeys(e.name for s, e in alt[:3] if s >= .40))
            hint = f" Sugestões: {suggestions}." if suggestions else ""
            raise LookupError(f"Não encontrei o aplicativo '{query}' neste Windows.{hint} Diga 'Marvin, atualize aplicativos' para buscar novamente.")
        best = evaluated[0][0]
        # Não escolher por engano 'Office' no lugar de 'Office 365' por exemplo.
        competing = list(dict.fromkeys(e.name for score, e in evaluated if score >= .86 and best-score <= .025))
        if len(competing) > 1 and best < 1:
            raise LookupError("Encontrei mais de um aplicativo: " + ", ".join(competing[:5]) + ". Diga o nome mais completo.")
        return evaluated[0][1]

    @staticmethod
    def _launch(entry: AppEntry) -> None:
        if platform.system() != "Windows":
            raise RuntimeError("A abertura de aplicativos exige Windows.")
        if entry.kind == "shortcut":
            if not Path(entry.target).is_file() or Path(entry.target).suffix.lower() not in (".lnk", ".url", ".appref-ms"):
                raise FileNotFoundError("O atalho não existe mais.")
            os.startfile(entry.target)
        elif entry.kind == "appid":
            # explorer abre aplicativos da Store e aplicativos tradicionais com AppUserModelID.
            if not entry.target or any(ch in entry.target for ch in ("\r", "\n", '"')):
                raise ValueError("Identificador de aplicativo inválido.")
            subprocess.Popen(["explorer.exe", "shell:AppsFolder\\" + entry.target], shell=False)
        elif entry.kind == "exe":
            # Apenas executáveis conhecidos ou caminhos existentes vindos do registro.
            if entry.origin != "Windows" and not Path(entry.target).is_file():
                raise FileNotFoundError("Executável não encontrado.")
            subprocess.Popen([entry.target], shell=False)
        else:
            raise ValueError("Tipo de aplicativo inválido.")

    def launch(self, query: str) -> str:
        entry = self.find(query)
        self._launch(entry)
        return f"Abrindo {entry.name}."


CATALOG = WindowsAppCatalog()


def list_apps() -> str:
    names = CATALOG.names()
    if not names:
        return "Não encontrei aplicativos no catálogo. Confirme que o MARVIN está rodando no Windows."
    first = ", ".join(names[:20])
    return f"Encontrei {len(names)} aplicativos e atalhos. Primeiros: {first}. Para ver todos, execute LISTAR_APPS.bat."


def open_known_folder(target: str) -> str:
    if platform.system() != "Windows":
        raise RuntimeError("Abrir pastas exige Windows.")
    home = Path.home()
    folders = {
        "downloads": home / "Downloads", "download": home / "Downloads",
        "documentos": home / "Documents", "documento": home / "Documents",
        "area de trabalho": home / "Desktop", "desktop": home / "Desktop",
        "imagens": home / "Pictures", "fotos": home / "Pictures",
        "musicas": home / "Music", "videos": home / "Videos",
    }
    key = fold(target)
    path = folders.get(key)
    if path is None:
        raise ValueError("Pasta não reconhecida; por segurança só abro pastas conhecidas por comando de voz.")
    if not path.is_dir():
        raise FileNotFoundError(f"Não encontrei a pasta {path}.")
    os.startfile(str(path))
    return f"Abrindo a pasta {key}."


def desktop_action(action: str, argument: str = "") -> str:
    """Gestos bem definidos; não aceita nomes de teclas fornecidos diretamente pela IA."""
    if platform.system() != "Windows":
        raise RuntimeError("Controle de janelas exige Windows.")
    import pyautogui as pg
    pg.FAILSAFE = True  # Canto superior esquerdo interrompe automação.
    keys = {
        "alt-tab": ("alt", "tab"), "show-desktop": ("win", "d"),
        "lock": ("win", "l"), "copy": ("ctrl", "c"),
        "paste": ("ctrl", "v"), "save": ("ctrl", "s"),
        "select-all": ("ctrl", "a"), "enter": ("enter",),
        "escape": ("esc",), "volume-mute": ("volumemute",),
        "volume-up": ("volumeup",), "volume-down": ("volumedown",),
    }
    if action == "screenshot":
        folder = Path.home() / "Pictures" / "MARVIN"
        folder.mkdir(parents=True, exist_ok=True)
        file = folder / time.strftime("captura-%Y%m%d-%H%M%S.png")
        pg.screenshot().save(file)
        return f"Capturei a tela em {file}. A imagem ficou apenas no seu computador."
    if action == "list-windows":
        try:
            from pywinauto import Desktop
            titles = list(dict.fromkeys(w.window_text().strip() for w in Desktop(backend="uia").windows() if w.window_text().strip()))
            return "Janelas abertas: " + (", ".join(titles[:16]) if titles else "nenhuma janela com título visível") + "."
        except Exception as exc:
            raise RuntimeError("Não consegui ler as janelas abertas: " + str(exc)[:130]) from exc
    if action == "focus":
        q = fold(argument)
        if not q:
            raise ValueError("Informe o nome da janela.")
        from pywinauto import Desktop
        found = [w for w in Desktop(backend="uia").windows() if q in fold(w.window_text()) and w.window_text()]
        if not found:
            return f"Não encontrei uma janela aberta com '{argument}'."
        if len(found) > 1:
            return "Encontrei várias janelas: " + ", ".join(w.window_text() for w in found[:4]) + ". Seja mais específico."
        found[0].set_focus()
        return f"Trocando para {found[0].window_text()}."
    if action == "minimize":
        pg.hotkey("win", "down")
        return "Minimizando a janela atual."
    if action == "maximize":
        pg.hotkey("win", "up")
        return "Maximizando a janela atual."
    if action == "close":
        # A interface precisa pedir confirmação ANTES de executar isso.
        pg.hotkey("alt", "f4")
        return "Enviei o comando para fechar a janela. Confira se o programa pediu para salvar."
    if action not in keys:
        raise ValueError("Comando de teclado não permitido.")
    pg.hotkey(*keys[action])
    labels = {"alt-tab": "Alternando janelas", "show-desktop": "Exibindo a área de trabalho",
              "lock": "Bloqueando o computador", "copy": "Copiando a seleção", "paste": "Colando",
              "save": "Salvando no aplicativo ativo", "select-all": "Selecionando tudo",
              "enter": "Pressionando Enter", "escape": "Pressionando Escape",
              "volume-up": "Aumentando o volume", "volume-down": "Diminuindo o volume", "volume-mute": "Alternando silêncio do áudio"}
    return labels[action] + "."
