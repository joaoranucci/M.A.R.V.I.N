"""Loopback API authenticated by a per-launch HttpOnly session cookie."""
from contextlib import asynccontextmanager
import asyncio
import secrets
from pathlib import Path
from typing import Literal

from fastapi import FastAPI, HTTPException, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from .config import ROOT


class Command(BaseModel):
    text: str = Field(min_length=1, max_length=12000)


class Control(BaseModel):
    action: Literal['listen', 'cancel', 'pause', 'resume', 'privacy', 'keyboard', 'view', 'compact', 'focus']
    value: str | bool | None = None


class Decision(BaseModel):
    id: str
    accepted: bool


class Preferences(BaseModel):
    values: dict[str, str]


class Reminder(BaseModel):
    message: str = Field(min_length=1, max_length=2000)
    due_at: str


class NewProject(BaseModel):
    name: str = Field(min_length=1, max_length=80)


def create_app(presence, token, origin, dist=None):
    dist = Path(dist) if dist else ROOT / 'desktop' / 'dist'
    app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

    @app.middleware('http')
    async def session(request: Request, call_next):
        if request.headers.get('host') != origin.split('://', 1)[1]:
            return JSONResponse({'detail':'Host inválido'}, status_code=403)
        if request.url.path.startswith('/api/'):
            if not secrets.compare_digest(request.cookies.get('marvin_session', ''), token):
                return JSONResponse({'detail':'Sessão expirada. Reabra o MARVIN.'}, status_code=401)
            if request.method != 'GET' and request.headers.get('origin') != origin:
                return JSONResponse({'detail':'Origem inválida'}, status_code=403)
            try:
                if int(request.headers.get('content-length', '0')) > 64000:
                    return JSONResponse({'detail':'Pedido muito grande'}, status_code=413)
            except ValueError:
                return JSONResponse({'detail':'Pedido inválido'}, status_code=400)
        response = await call_next(request)
        response.headers['Referrer-Policy'] = 'no-referrer'
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['Cache-Control'] = 'no-store'
        response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self' ws://" + origin.split('://',1)[1] + "; frame-ancestors 'none'; base-uri 'none'; object-src 'none'"
        return response

    @app.exception_handler(ValueError)
    async def value_error(request, exc):
        return JSONResponse({'detail':str(exc)}, status_code=400)

    @app.exception_handler(PermissionError)
    async def permission_error(request, exc):
        return JSONResponse({'detail':str(exc)}, status_code=403)

    @app.exception_handler(FileNotFoundError)
    async def missing(request, exc):
        return JSONResponse({'detail':str(exc)}, status_code=404)

    @app.get('/bootstrap')
    def bootstrap(key: str = ''):
        if not secrets.compare_digest(key, token):
            raise HTTPException(403, 'Sessão inválida')
        response = RedirectResponse('/', status_code=303)
        response.set_cookie('marvin_session', token, httponly=True, samesite='strict', path='/')
        return response

    @app.get('/api/state')
    def state():
        return presence.snapshot()

    @app.get('/api/dashboard')
    def dashboard():
        return presence.dashboard()

    @app.get('/api/project/{project}')
    def project(project: str):
        return presence.project_details(project)

    @app.get('/api/project/{project}/file')
    def read_file(project: str, path: str):
        return presence.workspace.read_project_file(project, path)

    @app.get('/api/tasks/{task_id}')
    def steps(task_id: str):
        return {'steps':presence.runtime.tasks.steps(task_id)}

    @app.post('/api/command', status_code=202)
    def command(body: Command):
        return presence.submit(body.text)

    @app.post('/api/control')
    def control(body: Control):
        action, value = body.action, body.value
        if action == 'listen': presence.listen_once()
        elif action == 'cancel': presence.cancel()
        elif action == 'pause': presence.runtime.pause()
        elif action == 'resume': presence.runtime.resume()
        elif action == 'privacy':
            if not isinstance(value, bool): raise ValueError('Valor inválido')
            presence.set_privacy(value)
        elif action == 'keyboard':
            if not isinstance(value, bool): raise ValueError('Valor inválido')
            presence.keyboard = value
        elif action == 'compact':
            if not isinstance(value, bool): raise ValueError('Valor inválido')
            presence.set_compact(value)
        elif action == 'view': presence.navigate(str(value))
        elif action == 'focus': presence.focus(str(value or ''))
        return {'ok':True}

    @app.post('/api/approval')
    def decision(body: Decision):
        presence.decide(body.id, body.accepted)
        return {'ok':True}

    @app.post('/api/preferences')
    def preferences(body: Preferences):
        presence.preferences(body.values)
        return {'ok':True}

    @app.post('/api/reminders', status_code=201)
    def reminder(body: Reminder):
        result = presence.runtime.scheduler.add(body.message, body.due_at)
        presence.emit('reminder.created', message='Novo lembrete salvo')
        return result

    @app.post('/api/projects', status_code=201)
    def create_project(body: NewProject):
        result = presence.workspace.create_project(body.name)
        presence.focus(result['project'])
        presence.emit('project.created', project=result['project'])
        return result

    @app.websocket('/events')
    async def events(ws: WebSocket):
        if ws.headers.get('origin') != origin or not secrets.compare_digest(ws.cookies.get('marvin_session',''),token):
            await ws.close(code=1008)
            return
        await ws.accept()
        try:
            while not presence.stop.is_set():
                await asyncio.wait_for(ws.send_json(presence.snapshot()), timeout=3)
                await asyncio.sleep(.12)
        except (WebSocketDisconnect, RuntimeError, asyncio.TimeoutError):
            pass

    if (dist / 'assets').is_dir():
        app.mount('/assets', StaticFiles(directory=dist / 'assets'), name='assets')

    @app.get('/')
    def index():
        if not (dist / 'index.html').is_file():
            raise HTTPException(503, 'Compile a interface: npm run build na pasta desktop.')
        return FileResponse(dist / 'index.html')

    return app
