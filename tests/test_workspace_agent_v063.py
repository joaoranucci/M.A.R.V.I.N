"""Functional tests for actual project creation and safe self-edit proposal workflow."""
from __future__ import annotations
import json
import os
from pathlib import Path
import sys
import tempfile
import types as pytypes
import unittest
from unittest.mock import patch

from marvin.action_agent import ActionAgent, project_intent
from marvin.brain import Brain
from marvin.memory import Memory
from marvin.workspace import ProjectWorkspace
from marvin.self_edit import SourceEditor


class WorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.workspace = ProjectWorkspace(self.root / 'projects')

    def test_creates_full_virtual_phone(self):
        created = self.workspace.create_project('Celular Virtual')
        self.assertEqual(created['project'], 'celular-virtual')
        html = '<!DOCTYPE html><html><head><title>Celular virtual</title></head><body>MARVIN</body></html>'
        result = self.workspace.write_project_file('Celular Virtual', 'index.html', html)
        self.assertTrue(result['ok'])
        self.assertEqual(self.workspace.read_project_file('Celular Virtual','index.html')['content'], html)
        self.assertIn('index.html', self.workspace.list_project_files('Celular Virtual')['files'])
        with patch('os.startfile', create=True) as open_win, patch('sys.platform', 'win32'):
            result = self.workspace.open_project('Celular Virtual','index.html')
            open_win.assert_called_once()
        self.assertTrue(result['opened'].endswith('index.html'))

    def test_no_path_traversal_or_absolute_paths(self):
        self.workspace.create_project('test')
        for path in ('../danger.py', '../../.env', 'C:\\Windows\\system.ini', '/etc/passwd',
                     'a/../../evil.py', 'file|calc.bat', 'CON.txt', '.\\..\\other'):
            with self.subTest(path=path), self.assertRaises((ValueError, PermissionError)):
                self.workspace.write_project_file('test', path, 'x')
        self.assertFalse((self.root/'danger.py').exists())

    def test_overwrite_needs_approval(self):
        self.workspace.create_project('test')
        self.workspace.write_project_file('test','a.py','print(1)')
        with self.assertRaises(FileExistsError):
            self.workspace.write_project_file('test','a.py','print(2)')
        with self.assertRaises(PermissionError):
            self.workspace.write_project_file('test','a.py','print(2)',overwrite=True,
                approve_overwrite=lambda path: False)
        self.assertEqual(self.workspace.read_project_file('test','a.py')['content'], 'print(1)')
        self.workspace.write_project_file('test','a.py','print(2)',overwrite=True,
            approve_overwrite=lambda path: True)
        self.assertEqual(self.workspace.read_project_file('test','a.py')['content'], 'print(2)')

    def test_symlink_blocks_escape(self):
        self.workspace.create_project('test')
        outside = self.root / 'outside'
        outside.mkdir()
        try:
            (self.workspace.project_path('test')/'link').symlink_to(outside, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest('No symlink permission')
        with self.assertRaises(PermissionError):
            self.workspace.write_project_file('test','link/hidden.txt','do not write')


class SourceEditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root/'marvin').mkdir()
        (self.root/'marvin'/'demo.py').write_text('x = 1\n',encoding='utf-8')
        self.editor = SourceEditor(self.root)

    def test_proposal_requires_user_application_with_backup(self):
        before = (self.root/'marvin'/'demo.py').read_text()
        item = self.editor.propose_self_edit('marvin/demo.py','x = 2\n','Mudança controlada')
        self.assertTrue(item['changed'])
        self.assertEqual((self.root/'marvin'/'demo.py').read_text(),before)
        self.assertIn('+x = 2', self.editor.diff(item['proposal_id']))
        approved = self.editor.apply_reviewed(item['proposal_id'])
        self.assertIn('backup',approved)
        self.assertEqual((self.root/'marvin'/'demo.py').read_text(), 'x = 2\n')
        self.assertEqual(Path(approved['backup']).read_text(), 'x = 1\n')

    def test_cannot_patch_env_or_use_traversal(self):
        (self.root/'.env').write_text('SECRET=top-secret')
        for path in ('.env','../.env','marvin/../.env','marvin/not_found.py','C:\\Windows\\test.py'):
            with self.subTest(path=path), self.assertRaises(PermissionError):
                self.editor.propose_self_edit(path,'x=7','reason')

    def test_stale_edits_not_applied(self):
        proposal = self.editor.propose_self_edit('marvin/demo.py','x=2\n','change')
        (self.root/'marvin'/'demo.py').write_text('x=3\n')
        with self.assertRaises(RuntimeError):
            self.editor.apply_reviewed(proposal['proposal_id'])

    def test_syntax_error_blocked(self):
        with self.assertRaises(SyntaxError):
            self.editor.propose_self_edit('marvin/demo.py','def oops(\n','broken')


class FakePart:
    def __init__(self, text=None): self.text = text
    @staticmethod
    def from_text(text): return FakePart(text)
    @staticmethod
    def from_function_response(**kwargs): return FakePart(kwargs)

class FakeContent:
    def __init__(self, role, parts): self.role, self.parts = role, parts

class Stub:
    def __init__(self, **kwargs): self.kwargs = kwargs

class FakeTypes:
    Content = FakeContent
    Part = FakePart
    FunctionDeclaration = Stub
    Tool = Stub
    GenerateContentConfig = Stub
    AutomaticFunctionCallingConfig = Stub
    ToolConfig = Stub
    FunctionCallingConfig = Stub

class ModelStub:
    def __init__(self):
        self.index=0
        self.seen=[]
    def generate_content(self, model, contents, config):
        self.seen.append((model, contents, config))
        tasks = [
            ('create_project',{'name':'Celular Virtual'}),
            ('write_project_file',{'project':'Celular Virtual','path':'index.html',
                                   'content':'<!DOCTYPE html><html><body>Celular Virtual</body></html>'}),
            ('open_project',{'project':'Celular Virtual','path':'index.html'}),
        ]
        if self.index < len(tasks):
            name, args = tasks[self.index]
            self.index += 1
            fn = pytypes.SimpleNamespace(name=name, args=args, id=f'call{self.index}')
            return pytypes.SimpleNamespace(function_calls=[fn],
                    candidates=[pytypes.SimpleNamespace(content=FakeContent('model', [FakePart('call')]))])
        return pytypes.SimpleNamespace(function_calls=[], text='Criei a pasta e o index.html e abri o projeto.')


class AgentIntegrationTests(unittest.TestCase):
    def test_gemini_tool_calls_create_real_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root/'marvin').mkdir()
            (root/'marvin'/'demo.py').write_text('x=1')
            mem = Memory(root/'db.sqlite')
            models = ModelStub()
            with patch.dict(os.environ, {'GEMINI_API_KEY':'TEST','GEMINI_MODEL':'gemini-3.5-flash-lite'}):
                brain = Brain(mem, client=pytypes.SimpleNamespace(models=models))
            workspace=ProjectWorkspace(root/'projects')
            agent=ActionAgent(brain, mem, workspace, SourceEditor(root))
            fake_google = pytypes.ModuleType('google')
            fake_genai = pytypes.ModuleType('google.genai')
            fake_genai.types = FakeTypes
            with patch.dict(sys.modules, {'google':fake_google,'google.genai':fake_genai}), \
                 patch('marvin.workspace.sys.platform','win32'), \
                 patch('marvin.workspace.os.startfile',create=True) as opener:
                answer = agent.assist('Monte você mesmo um celular virtual, crie uma pasta, escreva o código e abra o projeto')
            self.assertIn('Criei',answer)
            self.assertTrue((root/'projects'/'celular-virtual'/'index.html').exists())
            opener.assert_called_once()
            self.assertGreaterEqual(len(models.seen),4)
            self.assertEqual(mem.recent()[-1][0], 'model')

    def test_memory_persists_between_instances(self):
        with tempfile.TemporaryDirectory() as tmp:
            db=Path(tmp)/'memory.db'
            Memory(db).remember('Gosto de projetos open source')
            self.assertIn('Gosto de projetos open source',Memory(db).facts())
            Memory(db).clear()
            self.assertEqual(Memory(db).facts(),[])

    def test_filesystem_tool_restricted_even_if_model_requests_escape(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/'marvin').mkdir()
            (root/'marvin'/'x.py').write_text('x=1')
            with patch.dict(os.environ, {'GEMINI_API_KEY':'TEST'}):
                mem=Memory(root/'memory.db')
                agent=ActionAgent(Brain(mem),mem,ProjectWorkspace(root/'projects'),SourceEditor(root))
            agent.dispatch('create_project', {'name':'test'}, 'crie test')
            with self.assertRaises(ValueError):
                agent.dispatch('write_project_file', {'project':'test','path':'../../outside','content':'no'}, 'escreva')
            with self.assertRaises(PermissionError):
                agent.dispatch('run_shell',{'command':'rm -rf /'}, 'execute')
            with self.assertRaises(PermissionError):
                agent.dispatch('propose_self_edit',{'path':'marvin/x.py','content':'x=2','reason':'no'}, 'oi')

    def test_priority_for_code_projects(self):
        self.assertTrue(project_intent('abra o VS Code e escreva o código para mim'))
        self.assertTrue(project_intent('Crie uma pasta e monte o celular virtual'))
        self.assertFalse(project_intent('clique no botão do Chrome'))

if __name__ == '__main__':
    unittest.main()
