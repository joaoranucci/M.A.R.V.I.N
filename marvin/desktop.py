"""Native WebView2 host; React and FastAPI can also run in a browser for testing."""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import secrets
import socket
import threading
import time
import webbrowser

from .config import ROOT
from .presence import Presence
from .presence_api import create_app


class NativeWindow:
    def __init__(self, window):
        self.window = window
        self.geometry = None

    def set_compact(self, compact):
        if compact:
            if self.geometry is None:
                self.geometry = (self.window.width, self.window.height, self.window.x, self.window.y)
            self.window.on_top = True
            self.window.resize(270, 310)
            import webview
            screen = webview.screens[0]
            self.window.move(max(0, screen.width-300), max(0, screen.height-370))
        else:
            self.window.on_top = False
            if self.geometry:
                w,h,x,y = self.geometry
                self.window.resize(w,h)
                self.window.move(x,y)
                self.geometry = None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--browser', action='store_true')
    parser.add_argument('--no-open', action='store_true')
    parser.add_argument('--no-audio', action='store_true')
    parser.add_argument('--data-dir')
    parser.add_argument('--workspace')
    args = parser.parse_args()
    if not (ROOT/'desktop/dist/index.html').is_file():
        raise SystemExit('Interface não compilada. Execute INSTALAR_INTERFACE.bat.')
    from .workspace import ProjectWorkspace
    import uvicorn
    presence = Presence(args.data_dir, ProjectWorkspace(Path(args.workspace)) if args.workspace else None, audio=not args.no_audio)
    listener = socket.socket()
    listener.bind(('127.0.0.1',0))
    origin = 'http://127.0.0.1:' + str(listener.getsockname()[1])
    token = secrets.token_urlsafe(40)
    app = create_app(presence, token, origin)
    server = uvicorn.Server(uvicorn.Config(app, host='127.0.0.1', access_log=False, log_level='warning'))
    thread = threading.Thread(target=lambda:server.run(sockets=[listener]), daemon=True, name='MARVIN-API')
    thread.start()
    for _ in range(100):
        if server.started: break
        time.sleep(.05)
    if not server.started:
        presence.close()
        raise SystemExit('Não foi possível iniciar a interface local.')
    url = origin + '/bootstrap?key=' + token
    session_file = presence.data_dir/'presence-session.json'
    session_file.write_text(json.dumps({'origin':origin,'url':url,'pid':os.getpid()}),encoding='utf-8')
    try:
        presence.start()
        if args.browser or args.no_open:
            if not args.no_open: webbrowser.open(url)
            while thread.is_alive(): time.sleep(.25)
        else:
            import webview
            window = webview.create_window('MARVIN · Presença', url, width=1440, height=940,
                min_size=(250,280), background_color='#070c15', text_select=True)
            presence.native = NativeWindow(window)
            webview.start(gui='edgechromium', private_mode=True)
    except KeyboardInterrupt:
        pass
    finally:
        server.should_exit = True
        presence.close()
        listener.close()
        if session_file.exists(): session_file.unlink()


if __name__ == '__main__':
    main()
