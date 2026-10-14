import tempfile
import threading
import time
import unittest
from pathlib import Path
from fastapi.testclient import TestClient
from starlette.websockets import WebSocketDisconnect
from marvin.presence import Presence
from marvin.presence_api import create_app
from marvin.workspace import ProjectWorkspace

class PresenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        root=Path(self.tmp.name)
        self.p=Presence(root/'data',ProjectWorkspace(root/'projects'),audio=False)
        self.client=TestClient(create_app(self.p,'test-session','http://testserver'))
    def tearDown(self):
        self.client.close()
        self.p.close()
        self.tmp.cleanup()
    def login(self):
        self.client.get('/bootstrap?key=test-session',follow_redirects=False)
    def test_session_and_origin_are_required(self):
        self.assertEqual(self.client.get('/api/state').status_code,401)
        self.login()
        self.assertEqual(self.client.get('/api/state').status_code,200)
        body={'action':'keyboard','value':True}
        self.assertEqual(self.client.post('/api/control',json=body).status_code,403)
        self.assertEqual(self.client.post('/api/control',json=body,headers={'origin':'http://evil.test'}).status_code,403)
        self.assertFalse(self.p.keyboard)
        self.assertEqual(self.client.post('/api/control',json=body,headers={'origin':'http://testserver'}).status_code,200)
        self.assertTrue(self.p.keyboard)
        self.assertEqual(self.client.get('/api/state',headers={'host':'evil.test'}).status_code,403)
    def test_websocket_checks_origin_and_cookie(self):
        with self.assertRaises(WebSocketDisconnect):
            with self.client.websocket_connect('/events',headers={'origin':'http://testserver'}): pass
        self.login()
        with self.client.websocket_connect('/events',headers={'origin':'http://testserver'}) as ws:
            self.assertEqual(ws.receive_json()['phase'],'idle')
    def test_voice_navigation_does_not_call_model(self):
        self.p.workspace.create_project('projeto-composto')
        self.p.focus('projeto-composto')
        self.assertEqual(self.p.focus_project,'projeto-composto')
        self.p.workspace.create_project('oculos')
        self.p.submit('Marvin, abrir teclado')
        self.assertTrue(self.p.keyboard)
        self.p.submit('Marvin, vamos trabalhar no projeto dos oculos')
        self.assertEqual(self.p.focus_project,'oculos')
        self.p.submit('Marvin, modo compacto')
        self.assertTrue(self.p.compact)
        self.p.submit('Marvin, expandir')
        self.assertFalse(self.p.compact)
        self.assertEqual(self.p.runtime.tasks.list_tasks(),[])
    def test_approval_is_scoped_and_single_use(self):
        result=[]
        t=threading.Thread(target=lambda:result.append(self.p.confirm('Executar',{'command':'test'})))
        t.start()
        for _ in range(100):
            if self.p.approval: break
            time.sleep(.01)
        with self.assertRaises(ValueError): self.p.decide('stale',True)
        self.assertEqual(self.p.snapshot()['phase'],'approval')
        self.p.decide(self.p.approval['id'],False)
        t.join(2)
        self.assertEqual(result,[False])
        with self.assertRaises(ValueError): self.p.decide('stale',True)
    def test_cancel_removes_pending_work(self):
        self.p.keyboard=True
        self.p.submit('lembre que esta tarefa foi cancelada')
        self.assertFalse(self.p.keyboard)
        self.p.cancel()
        self.assertEqual(self.p.runtime.tasks.list_tasks()[0]['state'],'cancelled')
        self.assertEqual(self.p.memory.facts(),[])
    def test_project_context_and_path_boundary(self):
        self.p.workspace.create_project('oculos')
        self.p.workspace.write_project_file('oculos','README.md','# Arquitetura')
        self.assertEqual(self.p.project_details('oculos')['documents'],['README.md'])
        self.login()
        result=self.client.get('/api/project/oculos/file',params={'path':'../../outside.txt'})
        self.assertIn(result.status_code,(400,403))
