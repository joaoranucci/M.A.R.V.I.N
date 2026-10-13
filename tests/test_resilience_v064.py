"""Regression tests for Gemini transient failure, audio selection, and offline phone."""
from pathlib import Path
import os
import sys
import tempfile
import types
import unittest
from unittest.mock import patch

from marvin.brain import Brain, transient_server_error
from marvin.action_agent import ActionAgent
from marvin.memory import Memory
from marvin.workspace import ProjectWorkspace
from marvin.self_edit import SourceEditor
from marvin.offline_projects import try_generate_offline
from marvin.voice import _input_candidates, _open_microphone


class ServiceUnavailable(Exception):
    code = 503

class TestTypes:
    class Part:
        @staticmethod
        def from_text(text): return types.SimpleNamespace(text=text)
    class Content:
        def __init__(self, role, parts): self.role, self.parts = role, parts
    class _Opts:
        def __init__(self, **kwargs): self.kwargs = kwargs
    GenerateContentConfig = _Opts
    Tool = _Opts
    FunctionDeclaration = _Opts
    AutomaticFunctionCallingConfig = _Opts
    ToolConfig = _Opts
    FunctionCallingConfig = _Opts

class FakeModel:
    def __init__(self, outcomes): self.outcomes = list(outcomes); self.calls=[]
    def generate_content(self, model, contents, config):
        self.calls.append(model)
        result = self.outcomes.pop(0)
        if isinstance(result, Exception): raise result
        return result

class ResilienceTests(unittest.TestCase):
    def setUp(self):
        t = tempfile.TemporaryDirectory()
        self.addCleanup(t.cleanup)
        self.path=Path(t.name)
        self.mem=Memory(self.path/'mem.db')
        (self.path/'marvin').mkdir()
        (self.path/'marvin'/'demo.py').write_text('a=1')
        self.workspace=ProjectWorkspace(self.path/'projetos')

    def _agent(self, outcomes):
        models=FakeModel(outcomes)
        with patch.dict(os.environ, {'GEMINI_API_KEY':'mock-key','GEMINI_MODEL':'gemini-3.5-flash-lite'}):
            brain=Brain(self.mem,client=types.SimpleNamespace(models=models))
        return ActionAgent(brain,self.mem,self.workspace,SourceEditor(self.path)), models

    def _google(self):
        fake=types.ModuleType('google.genai');fake.types=TestTypes
        return patch.dict(sys.modules,{'google.genai':fake})

    def test_503_is_transient_not_key_refusal(self):
        from marvin.brain import friendly_error, invalid_key
        err=ServiceUnavailable('service unavailable')
        self.assertTrue(transient_server_error(err))
        self.assertFalse(invalid_key(err))
        self.assertIn('temporariamente', friendly_error(err))

    def test_action_agent_switches_model_before_any_file_action(self):
        ok=types.SimpleNamespace(function_calls=[],text='Sim, MARVIN funcionando')
        agent, models=self._agent([ServiceUnavailable(),ok])
        with self._google():
            result=agent.assist('Oi, tudo bem?')
        self.assertEqual(result,'Sim, MARVIN funcionando')
        self.assertEqual(models.calls,['gemini-3.5-flash-lite','gemini-3.1-flash-lite'])

    def test_503_offline_virtual_phone_writes_three_real_files(self):
        agent,models=self._agent([ServiceUnavailable(),ServiceUnavailable()])
        with self._google(), patch('marvin.workspace.sys.platform','win32'), patch('marvin.workspace.os.startfile',create=True) as opening:
            answer=agent.assist('Marvin, crie um projeto chamado Celular Virtual. Monte uma interface de smartphone')
        self.assertIn('protótipo offline',answer)
        for name in ['index.html','style.css','app.js']:
            self.assertTrue((self.path/'projetos'/'celular-virtual'/name).is_file())
        opening.assert_called_once()
        self.assertEqual(len(models.calls),2)

    def test_no_offline_for_other_projects(self):
        agent,_=self._agent([ServiceUnavailable(),ServiceUnavailable()])
        with self._google():
            answer=agent.assist('Crie um projeto de e-commerce')
        self.assertIn('Não consegui',answer)
        self.assertFalse((self.path/'projetos'/'e-commerce').exists())

    def test_no_overwrite_offline_template(self):
        self.workspace.create_project('Celular Virtual')
        self.workspace.write_project_file('Celular Virtual','index.html','EXISTENTE')
        with patch('marvin.workspace.sys.platform','win32'), patch('marvin.workspace.os.startfile',create=True):
            result=try_generate_offline(self.workspace,'crie um celular virtual')
        self.assertIn('preservados',result)
        self.assertEqual((self.path/'projetos'/'celular-virtual'/'index.html').read_text(),'EXISTENTE')

class FakeStream:
    def __init__(self, fail=False): self.fail=fail;self.closed=False;self.started=False
    def start(self):
        if self.fail: raise RuntimeError('PaErrorCode -9999 MME')
        self.started=True
    def close(self): self.closed=True

class AudioTests(unittest.TestCase):
    def setUp(self):
        self.devices=[
            {'name':'Microfone Realtek', 'hostapi':0,'max_input_channels':1,'default_samplerate':48000},
            {'name':'Microfone Realtek', 'hostapi':1,'max_input_channels':1,'default_samplerate':48000},
            {'name':'Alto falante', 'hostapi':1,'max_input_channels':0,'default_samplerate':48000},
        ]
        self.hosts=[{'name':'MME'},{'name':'Windows WASAPI'}]
        self.streams=[]
        self.calls=[]
        def RawInputStream(**kwargs):
            self.calls.append(kwargs)
            obj=FakeStream(fail=kwargs['device']==1)
            self.streams.append(obj)
            return obj
        self.sd=types.SimpleNamespace(query_devices=lambda:self.devices,
            query_hostapis=lambda:self.hosts,
            default=types.SimpleNamespace(device=(0,2)),RawInputStream=RawInputStream)

    def test_native_rate_and_wasapi_fallback(self):
        with patch.dict(os.environ,{'MARVIN_MIC_DEVICE':'','MARVIN_MIC_RATE':'auto'}):
            stream,rate=_open_microphone(self.sd,lambda *args:None)
        self.assertEqual(rate,48000)
        self.assertEqual(self.calls[-1]['device'],0)
        self.assertEqual(self.calls[-1]['blocksize'],0)
        self.assertTrue(self.streams[0].closed)
        self.assertTrue(stream.started)
        stream.close()

    def test_explicit_index_restricts_to_matching_device(self):
        with patch.dict(os.environ,{'MARVIN_MIC_DEVICE':'1','MARVIN_MIC_RATE':'auto'}):
            options=_input_candidates(self.sd)
        self.assertTrue(options)
        self.assertEqual(options[0][0],1)
        self.assertTrue(all(idx in (0,1) for idx,rate,_,_ in options))

    def test_invalid_microphone_index_explained(self):
        with patch.dict(os.environ,{'MARVIN_MIC_DEVICE':'27'}):
            with self.assertRaisesRegex(RuntimeError,'LISTAR_MICROFONES'):
                _input_candidates(self.sd)

if __name__=='__main__': unittest.main()
