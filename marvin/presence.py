"""Headless adapter: native audio, durable runtime and contextual UI state.

The UI never executes shell code. Worker events and approvals cross this adapter,
so rendering and GPU animation do not block audio or task execution.
"""
from __future__ import annotations

from collections import deque
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import queue
import re
import threading
import time
import uuid

from .action_agent import ActionAgent
from .brain import Brain, safe_error_detail
from .commands import normalize
from .config import ROOT, load_config, save_preferences
from .instance import InstanceLock
from .memory import Memory
from .runtime import Runtime, TaskControl, request_text
from .self_edit import SourceEditor
from .workspace import ProjectWorkspace
from . import voice


class Presence:
    def __init__(self, data_dir=None, workspace=None, *, audio=True):
        self.data_dir = Path(data_dir) if data_dir else load_config()
        self.instance = InstanceLock(self.data_dir)
        self.memory = Memory(self.data_dir / 'marvin.db')
        self.workspace = workspace or ProjectWorkspace()
        self.brain = Brain(self.memory)
        self.guard = threading.RLock()
        self.stop = threading.Event()
        self.jobs = queue.Queue(maxsize=8)
        self.token = TaskControl()
        self.wake_stop = threading.Event()
        self.wake_pause = threading.Event()
        self.wake_thread = None
        self.manual_thread = None
        self.voice_guard = threading.Lock()
        self.audio_enabled = audio
        self.privacy = False
        self.busy = False
        self.phase = 'idle'
        self.status = 'Pronto para estar com você'
        self.view = 'home'
        self.keyboard = False
        self.compact = False
        self.focus_project = None
        self.focus_requested = ''
        self.seq = 0
        self.events = deque(maxlen=60)
        self.messages = deque(({'role': 'assistant' if role == 'model' else 'user', 'text': text}
                               for role, text in self.memory.recent(limit=12)), maxlen=30)
        self.sources = []
        self.approval = None
        self.approval_event = threading.Event()
        self.approval_answer = False
        self.native = None
        self.worker = None
        self.ticker = None
        agent = ActionAgent(self.brain, self.memory, self.workspace, SourceEditor(ROOT),
            confirm_overwrite=lambda path: self.confirm('Substituir arquivo', {'path': str(path)}),
            confirm_execution=lambda details: self.confirm('Executar verificação', details))
        self.runtime = Runtime(self.memory, self.workspace, agent, emit=self.on_event,
                               confirm_action=lambda text: self.confirm('Autorizar ação', {'message': text}))

    def emit(self, kind, **payload):
        with self.guard:
            self.seq += 1
            self.events.append({'id': self.seq, 'type': kind, 'time': datetime.now(timezone.utc).isoformat(), **payload})

    def set_phase(self, phase, status=None):
        with self.guard:
            self.phase = phase
            if status:
                self.status = status

    def on_event(self, event):
        kind, payload = event['type'], event.get('payload', {})
        self.emit(kind, task_id=event.get('task_id'), **payload)
        if kind == 'tool.requested':
            tool = payload.get('tool', '')
            self.set_phase('searching' if 'web' in tool or 'search' in tool else 'executing',
                           'Consultando fontes' if 'web' in tool else 'Executando sua solicitação')
        elif kind == 'task.progress':
            message = payload.get('message', '')
            self.set_phase('searching' if 'fontes' in message.lower() else 'thinking', message)

    def confirm(self, title, details):
        with self.guard:
            self.approval_event.clear()
            self.approval_answer = False
            self.approval = {'id': uuid.uuid4().hex, 'title': title, 'details': details}
            self.set_phase('approval', 'Uma decisão sua para continuar')
        self.emit('approval.requested', title=title)
        deadline = time.monotonic() + 120
        while not self.stop.is_set() and not self.token.is_set() and time.monotonic() < deadline:
            if self.approval_event.wait(.1):
                break
        with self.guard:
            answer = self.approval_answer and not self.token.is_set() and not self.stop.is_set()
            self.approval = None
            self.set_phase('executing', 'Continuando' if answer else 'Ação não autorizada')
            return answer

    def decide(self, approval_id, accepted):
        with self.guard:
            if not self.approval or self.approval['id'] != approval_id:
                raise ValueError('Esta autorização já expirou.')
            if self.approval_event.is_set():
                raise ValueError('Esta autorização já foi respondida.')
            self.approval_answer = accepted is True
            self.approval_event.set()

    def start(self):
        self.worker = threading.Thread(target=self.run_jobs, daemon=True, name='MARVIN-runtime')
        self.worker.start()
        self.ticker = threading.Thread(target=self.tick, daemon=True, name='MARVIN-reminders')
        self.ticker.start()
        self.start_wake()

    def start_wake(self):
        with self.voice_guard:
            if not self.audio_enabled or self.privacy or self.stop.is_set() or os.getenv('MARVIN_WAKE', 'true') != 'true':
                return
            if (self.manual_thread and self.manual_thread.is_alive()) or (self.wake_thread and self.wake_thread.is_alive()):
                return
            self.wake_stop = threading.Event()
            generation = self.wake_stop
            def run():
                try:
                    voice.listen_wake(lambda text: self.heard(text, generation), self.audio_status,
                        generation, self.wake_pause,
                        on_wake=lambda: self.set_phase('listening', 'Estou ouvindo'),
                        on_barge=lambda: self.set_phase('listening', 'Pode falar. Estou ouvindo você.'))
                except Exception as exc:
                    if not generation.is_set():
                        self.emit('audio.error', message=safe_error_detail(exc))
                        self.set_phase('idle', 'Microfone indisponível · use o teclado')
            self.wake_thread = threading.Thread(target=run, daemon=True, name='MARVIN-wake')
            self.wake_thread.start()

    def audio_status(self, text):
        with self.guard:
            self.status = text
            if text.startswith(('Ouvindo', 'Estou ouvindo', 'MARVIN ativado')):
                self.phase = 'listening'
            elif text.startswith('Aguardando') and not self.busy:
                self.phase = 'idle'

    def heard(self, text, generation):
        if generation.is_set() or self.privacy or self.stop.is_set():
            return
        try:
            self.submit(text)
        except Exception as exc:
            self.emit('audio.error', message=safe_error_detail(exc))

    def listen_once(self):
        with self.voice_guard:
            if self.privacy:
                raise ValueError('O microfone está pausado. Ative-o para conversar.')
            if not self.audio_enabled:
                raise ValueError('Áudio desativado nesta sessão.')
            if self.manual_thread and self.manual_thread.is_alive():
                return
            if self.busy and not voice.is_speaking():
                raise ValueError('Aguarde a tarefa ou use o teclado para colocar outro pedido na fila.')
            voice.cancel_speech()
            self.wake_stop.set()
            manual_cancel = threading.Event()
            self.manual_cancel = manual_cancel
            self.set_phase('listening', 'Pode falar, estou ouvindo')
            def run():
                try:
                    if self.wake_thread:
                        self.wake_thread.join(timeout=6)
                    if self.privacy or self.stop.is_set():
                        return
                    text = voice.listen(status=self.audio_status, cancel_event=manual_cancel)
                    if text and not manual_cancel.is_set() and not self.privacy:
                        self.submit(text)
                except Exception as exc:
                    self.emit('audio.error', message=safe_error_detail(exc))
                finally:
                    if not self.busy:
                        self.set_phase('idle', 'Diga “Marvin” ou abra o teclado')
            self.manual_thread = threading.Thread(target=run, daemon=True, name='MARVIN-listen')
            self.manual_thread.start()

    def navigate(self, view):
        if view not in {'home', 'focus', 'projects', 'tasks', 'agenda', 'knowledge', 'search', 'settings'}:
            raise ValueError('Painel desconhecido.')
        with self.guard:
            self.view = view

    def set_compact(self, compact):
        if self.native:
            self.native.set_compact(compact)
        with self.guard:
            self.compact = compact

    def focus(self, requested):
        projects = self.workspace.list_projects()['projects']
        wanted = normalize(requested).replace("-", " ")
        matches = [p['project'] for p in projects if normalize(p['project']).replace('-', ' ') == wanted]
        if not matches:
            matches = [p['project'] for p in projects if wanted in normalize(p['project']).replace('-', ' ') or normalize(p['project']).replace('-', ' ') in wanted]
        with self.guard:
            self.view = 'focus'
            self.focus_requested = requested
            self.focus_project = matches[0] if len(matches) == 1 else None
        if self.focus_project:
            self.memory.set_context({'project': self.focus_project})
        self.emit('focus.changed', project=self.focus_project, requested=requested)

    def ui_command(self, text):
        n = normalize(request_text(text))
        if n in {'abrir teclado', 'abra o teclado', 'abra teclado', 'modo digitacao', 'digitar', 'mostrar teclado'}:
            self.keyboard = True
            return True
        if n in {'fechar teclado', 'feche o teclado', 'ocultar teclado'}:
            self.keyboard = False
            return True
        if n in {'recolher', 'recolha', 'modo compacto', 'minimizar'}:
            self.set_compact(True)
            return True
        if n in {'expandir', 'expanda', 'voltar', 'tela cheia'}:
            self.set_compact(False)
            return True
        views = {'minha agenda': 'agenda', 'mostre minha agenda': 'agenda', 'abrir agenda': 'agenda',
                 'mostrar projetos': 'projects', 'meus projetos': 'projects', 'inicio': 'home',
                 'mostrar tarefas': 'tasks', 'minhas tarefas': 'tasks', 'mostrar memoria': 'knowledge'}
        if n in views:
            self.navigate(views[n])
            return True
        match = re.fullmatch(r'(?:vamos trabalhar (?:no|na)|foco (?:no|na)|abrir focus (?:no|na)?|focus)\s*(?:projeto\s+)?(.+)', n)
        if match:
            self.focus(match.group(1))
            return True
        return False

    def submit(self, text):
        text = str(text).strip()
        if not text or len(text) > 12000:
            raise ValueError('Escreva um pedido de até 12.000 caracteres.')
        with self.guard:
            if self.stop.is_set():
                raise ValueError('O MARVIN está encerrando.')
            if self.ui_command(text):
                if not self.busy:
                    self.wake_pause.clear()
                    self.set_phase('idle', 'Pronto')
                return {'ui': True}
            n = normalize(request_text(text))
            if n in {'pare', 'cancelar', 'cancele', 'pare de falar'}:
                self.cancel()
                return {'cancelled': True}
            if self.jobs.full():
                raise ValueError('Há oito pedidos na fila. Aguarde ou cancele.')
            task = self.runtime.prepare(text)
            self.messages.append({'role': 'user', 'text': text})
            self.keyboard = False
            self.jobs.put_nowait((text, task['id']))
            if re.match(r'^(pesquis|busqu|procur|consult)', n):
                self.view = 'search'
            return {'task_id': task['id']}

    def run_jobs(self):
        while not self.stop.is_set():
            with self.guard:
                if self.jobs.empty():
                    work = None
                else:
                    work = self.jobs.get_nowait()
                    self.busy = True
                    self.token = TaskControl()
            if work is None:
                self.stop.wait(.1)
                continue
            question, task_id = work
            with self.guard:
                if self.token.is_set() or self.stop.is_set():
                    self.runtime.tasks.set_state(task_id, 'cancelled', 'Cancelado antes da execução')
                    self.busy = False
                    self.jobs.task_done()
                    continue
                self.busy = True
                self.wake_pause.set()
                self.set_phase('thinking', 'Organizando seu pedido')
            try:
                result = self.runtime.run(question, task_id=task_id, control=self.token)
                answer = result['answer']
                with self.guard:
                    self.messages.append({'role': 'assistant', 'text': answer, 'state': result['state']})
                    self.sources = [{'title': m[0], 'url': m[1]} for m in re.findall(r'\[([^\]]+)\]\((https?://[^\s)]+)\)', answer)][:8]
                self.emit('answer', message=answer, state=result['state'])
                if self.audio_enabled and os.getenv('MARVIN_SPEAK', 'true') == 'true' and not self.token.is_set() and not self.privacy:
                    self.set_phase('speaking', 'Preparando a voz')
                    voice.speak(answer, voice=os.getenv('MARVIN_VOICE', voice.DEFAULT_VOICE),
                                cancel_event=self.token, status=self.audio_status)
            except Exception as exc:
                self.emit('task.error', message=safe_error_detail(exc))
            finally:
                with self.guard:
                    self.busy = False
                    self.wake_pause.clear()
                    if self.phase != 'listening':
                        self.set_phase('idle', 'Diga “Marvin”, estou por aqui')
                self.jobs.task_done()

    def cancel(self):
        with self.guard:
            self.token.set()
            self.runtime.cancel()
            voice.cancel_speech()
            if hasattr(self, 'manual_cancel'):
                self.manual_cancel.set()
            self.approval_answer = False
            self.approval_event.set()
            while True:
                try:
                    _, task_id = self.jobs.get_nowait()
                    self.runtime.tasks.set_state(task_id, 'cancelled', 'Cancelado na fila')
                    self.jobs.task_done()
                except queue.Empty:
                    break
            self.set_phase('idle', 'Cancelamento solicitado')

    def set_privacy(self, enabled):
        self.privacy = enabled
        if enabled:
            self.wake_stop.set()
            voice.cancel_speech()
            if hasattr(self, 'manual_cancel'):
                self.manual_cancel.set()
            self.set_phase('idle', 'Microfone pausado')
        else:
            self.start_wake()

    def preferences(self, values):
        allowed = {'MARVIN_SPEAK', 'MARVIN_WAKE', 'MARVIN_VOICE', 'MARVIN_BARGE_IN', 'MARVIN_BARGE_THRESHOLD', 'MARVIN_REASONING', 'MARVIN_SEARCH_PROVIDER'}
        if set(values)-allowed:
            raise ValueError('Preferência desconhecida.')
        for k, v in values.items():
            if k in {'MARVIN_SPEAK','MARVIN_WAKE','MARVIN_BARGE_IN'} and v not in {'true','false'}:
                raise ValueError('Valor booleano inválido.')
            if k == 'MARVIN_VOICE' and v not in voice.VOICE_OPTIONS:
                raise ValueError('Voz inválida.')
            if k == 'MARVIN_REASONING' and v not in {'rapido','equilibrado','profundo'}:
                raise ValueError('Modo inválido.')
            if k == 'MARVIN_SEARCH_PROVIDER' and v not in {'google','brave','searxng'}:
                raise ValueError('Provedor inválido.')
            if k == 'MARVIN_BARGE_THRESHOLD' and not 100 <= float(v) <= 10000:
                raise ValueError('Limiar inválido.')
        save_preferences(self.data_dir, values)
        if values.get('MARVIN_WAKE') == 'false':
            self.wake_stop.set()
        if values.get('MARVIN_SPEAK') == 'false':
            voice.cancel_speech()

    def dashboard(self):
        tasks = self.runtime.tasks.list_tasks(60)
        projects = self.workspace.list_projects()['projects']
        facts = self.memory.list_facts(50)
        return {'projects': projects, 'tasks': tasks, 'reminders': self.runtime.scheduler.list_reminders(),
                'facts': facts, 'capabilities': {'gemini': bool(self.brain.api_key and self.brain.api_key != 'COLE_SUA_CHAVE_AQUI'),
                'brave': bool(os.getenv('BRAVE_SEARCH_API_KEY')), 'searxng': bool(os.getenv('SEARXNG_URL'))}}

    def project_details(self, project):
        result = self.workspace.list_project_files(project)
        documents = [p for p in result['files'] if p.lower().endswith(('.md', '.txt', '.json'))]
        result['documents'] = documents[:30]
        result['tasks'] = [t for t in self.runtime.tasks.list_tasks(100) if normalize(project).replace('-', ' ') in normalize(t['objective']).replace('-', ' ')]
        result['notes'] = self.memory.relevant(project, limit=8)
        return result

    def snapshot(self):
        with self.guard:
            phase = 'speaking' if voice.is_speaking() and self.phase != 'approval' else self.phase
            return {'phase': phase, 'status': self.status, 'busy': self.busy, 'privacy': self.privacy,
                'view': self.view, 'keyboard': self.keyboard, 'compact': self.compact,
                'native': self.native is not None, 'focus_project': self.focus_project,
                'focus_requested': self.focus_requested, 'messages': list(self.messages),
                'sources': list(self.sources), 'events': list(self.events), 'seq': self.seq,
                'approval': self.approval, 'queue': self.jobs.qsize(), 'audio': voice.audio_snapshot(),
                'preferences': {k: os.getenv(k, default) for k, default in {
                    'MARVIN_VOICE':voice.DEFAULT_VOICE,'MARVIN_SPEAK':'true','MARVIN_WAKE':'true',
                    'MARVIN_BARGE_IN':'true','MARVIN_BARGE_THRESHOLD':'650',
                    'MARVIN_REASONING':'equilibrado','MARVIN_SEARCH_PROVIDER':'google'}.items()}}

    def tick(self):
        while not self.stop.wait(1):
            try:
                self.start_wake()
                for reminder in self.runtime.scheduler.claim_due():
                    message = 'Lembrete: ' + reminder['message']
                    with self.guard:
                        self.messages.append({'role':'assistant','text':message})
                    self.emit('reminder', message=message)
                    self.runtime.scheduler.ack(reminder['id'], reminder['claim_token'])
            except Exception as exc:
                self.emit('system.error', message=safe_error_detail(exc))

    def close(self):
        self.stop.set()
        self.wake_stop.set()
        self.cancel()
        for thread in (self.worker, self.wake_thread, self.manual_thread, self.ticker):
            if thread and thread is not threading.current_thread():
                thread.join(timeout=35)
        self.brain.close()
        self.instance.close()
