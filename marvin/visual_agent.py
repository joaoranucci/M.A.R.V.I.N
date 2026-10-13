"""Ponte opcional entre MARVIN (Python) e UI-TARS SDK (Node.js).

Não oferece modo pago, elevação de privilégios, shell arbitrário nem conexão remota
oculta. Cada tarefa passa por confirmação explícita na interface do Windows.
"""
from __future__ import annotations
from dataclasses import dataclass
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import threading
import time
from collections import deque
from urllib.parse import urlparse

BRIDGE_DIR = Path(__file__).resolve().parent.parent / 'ui_tars_bridge'
EVENT_PREFIX = 'MARVIN_EVENT:'


def visual_intent(text: str) -> bool:
    """Encaminha apenas pedidos claramente referentes a interagir com a tela."""
    from .commands import normalize
    n = normalize(text)
    n = re.sub(r'^(?:(?:ei|hey|c|ce|se|ok|ola) )?marvin(?:[,;:]? |$)', '', n).strip()
    if n.startswith(('nao ', 'se ', 'explique', 'me explique', 'como ', 'o que ', 'qual ', 'quais ', 'pesquise', 'pesquisa ', 'procure ')):
        return False
    if any(mark in n for mark in ('"', '“', '”', "'", '`')):
        return False
    direct = (
        'clique ', 'clica ', 'clicar ', 'digite ', 'escreva na tela',
        'preencha ', 'arraste ', 'navegue no ', 'interaja com ', 'faça na tela ',
        'faca na tela ', 'faça no computador ', 'faca no computador ',
        'execute na tela ', 'use o mouse ', 'use o teclado ',
        'mude a configuracao ', 'altere a configuracao ', 'configure no ',
        'ative no ', 'desative no ',
    )
    if n.startswith(direct): return True
    # Intenção explícita no meio da frase, sem transformar perguntas técnicas em cliques.
    if re.search(r'\b(?:clique|clica|clicar|digite|preencha|arraste|selecione|navegue)\b',n):
        return True
    # Abrir programa + tarefa adicional (não apenas abrir o app).
    return bool(re.search(
      r'^(?:abre|abra|abrir|inicia|inicie)\b.+\be\s+(?:ative|ativa|desative|desativa|configure|configura|mude|altere|abra|clique|digite|procure|encontre|preencha|salve)\b',n))


def visual_risk(task: str) -> bool:
    from .commands import normalize
    n = normalize(task)
    return bool(re.search(r'\b(?:apague|exclua|delete|remova|formate|pague|compre|envie|publique|poste|instale|desinstale|senha|cartao|pagamento|transferencia|privado)\b',n))


@dataclass(frozen=True)
class VisualSettings:
    base_url: str
    api_key: str
    model: str
    max_steps: int

    @classmethod
    def from_env(cls) -> 'VisualSettings':
        url = os.getenv('UI_TARS_BASE_URL','').strip().rstrip('/')
        model = os.getenv('UI_TARS_MODEL','').strip()
        if not url or not model:
            raise RuntimeError('Configure UI_TARS_BASE_URL e UI_TARS_MODEL no arquivo .env. A chave Gemini não é um modelo UI-TARS.')
        parsed=urlparse(url)
        if parsed.scheme not in ('http','https') or not parsed.hostname or parsed.username or parsed.password:
            raise RuntimeError('UI_TARS_BASE_URL deve ser uma URL HTTP(S) válida, sem senha embutida.')
        if parsed.scheme!='https' and parsed.hostname not in ('127.0.0.1','localhost','::1'):
            raise RuntimeError('Modelo remoto deve usar HTTPS para proteger capturas de tela e credenciais.')
        if parsed.hostname not in ('127.0.0.1','localhost','::1') and os.getenv('UI_TARS_ALLOW_REMOTE','false').lower()!='true':
            raise RuntimeError('Modelo remoto pode receber imagens da sua tela. Ative UI_TARS_ALLOW_REMOTE=true somente após autorizar esse envio.')
        try: steps=int(os.getenv('UI_TARS_MAX_STEPS','10'))
        except ValueError: steps=10
        steps=max(1,min(steps,25))
        return cls(base_url=url,api_key=os.getenv('UI_TARS_API_KEY','local'),model=model,max_steps=steps)


class VisualAgent:
    def __init__(self):
        self._lock=threading.Lock()
        self._process: subprocess.Popen|None=None

    @staticmethod
    def readiness() -> str:
        if not shutil.which('node'):
            return 'Node.js não encontrado. Instale Node.js 22 e execute INSTALAR_UI_TARS.bat.'
        if not (BRIDGE_DIR/'node_modules'/'@ui-tars'/'sdk').exists():
            return 'SDK não instalado. Execute INSTALAR_UI_TARS.bat após instalar o Node.js.'
        try: VisualSettings.from_env()
        except RuntimeError as exc: return str(exc)
        return 'Integração SDK instalada e configurada; modelo e controle de tela ainda não testados.'

    def cancel(self):
        with self._lock:
            proc=self._process
        if proc and proc.poll() is None:
            try: proc.terminate()
            except OSError: pass

    def run(self, task: str, notify=lambda kind,message: None, *, cancel_event=None, timeout_seconds=180) -> str:
        if not task or len(task)>2000: raise ValueError('A tarefa deve ter de 1 a 2000 caracteres.')
        token = cancel_event if cancel_event is not None else threading.Event()
        if token.is_set():
            raise RuntimeError('Tarefa visual cancelada antes de iniciar.')
        if not 0 < timeout_seconds <= 600:
            raise ValueError('Tempo limite visual deve ser maior que zero e até 600 segundos.')
        settings=VisualSettings.from_env()
        node=shutil.which('node')
        if not node: raise RuntimeError('Node.js 22 não está instalado/no PATH. Execute INSTALAR_UI_TARS.bat.')
        if not (BRIDGE_DIR/'node_modules'/'@ui-tars'/'sdk').exists():
            raise RuntimeError('SDK UI-TARS ausente. Execute INSTALAR_UI_TARS.bat.')
        from .process_runner import filtered_environment, _terminate
        env=filtered_environment()
        env.update(UI_TARS_BASE_URL=settings.base_url,UI_TARS_API_KEY=settings.api_key,
                   UI_TARS_MODEL=settings.model,UI_TARS_MAX_STEPS=str(settings.max_steps))
        options = ({'creationflags': subprocess.CREATE_NO_WINDOW | subprocess.CREATE_NEW_PROCESS_GROUP}
                   if os.name == 'nt' else {'start_new_session': True})
        with self._lock:
            if self._process and self._process.poll() is None:
                raise RuntimeError('Já existe uma tarefa visual em execução.')
            if token.is_set():
                raise RuntimeError('Tarefa visual cancelada antes de iniciar.')
            proc=subprocess.Popen([node,str(BRIDGE_DIR/'runner.mjs'),task],
                 cwd=str(BRIDGE_DIR),env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,
                 stdin=subprocess.DEVNULL,text=True,encoding='utf-8',errors='replace',
                 bufsize=1,**options)
            self._process=proc
        stop_watch = threading.Event()
        timed_out = threading.Event()
        def watchdog():
            deadline = time.monotonic() + timeout_seconds
            while not stop_watch.wait(.05) and proc.poll() is None:
                if token.is_set() or time.monotonic() >= deadline:
                    if not token.is_set():
                        timed_out.set()
                    _terminate(proc)
                    return
        watcher = threading.Thread(target=watchdog, daemon=True)
        watcher.start()
        err_lines=deque(maxlen=12)
        def collect_errors():
            try:
                for line in proc.stderr:
                    err_lines.append(line.strip()[:350])
            except Exception: pass
        threading.Thread(target=collect_errors,daemon=True).start()
        done=False
        try:
            for line in proc.stdout:
                if not line.startswith(EVENT_PREFIX):continue
                try: payload=json.loads(line[len(EVENT_PREFIX):])
                except json.JSONDecodeError:continue
                kind=payload.get('type')
                detail=str(payload.get('message',''))[:300]
                if kind=='progress': notify('progress',detail)
                if kind=='complete':
                    done=True
                    notify('progress',detail or 'Execução terminada.')
                if kind=='error': notify('progress','Falha UI-TARS: '+detail)
            returncode=proc.wait(timeout=5)
            if timed_out.is_set():
                raise RuntimeError('Tempo limite do agente visual atingido. Confira efeitos já realizados na tela.')
            if returncode!=0:
                brief='; '.join(err_lines)[-600:]
                raise RuntimeError('UI-TARS interrompido. '+(brief or f'Saída {returncode}.'))
            if not done:
                raise RuntimeError('UI-TARS encerrou sem confirmar o resultado da tarefa.')
            return 'Tarefa visual encerrada. Confira a tela para verificar o resultado.'
        finally:
            stop_watch.set()
            if proc.poll() is None:
                _terminate(proc)
            watcher.join(timeout=1)
            with self._lock:
                if self._process is proc:self._process=None
