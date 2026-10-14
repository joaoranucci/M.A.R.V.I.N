import json
import os
from array import array
from pathlib import Path
import tempfile
import threading
import types
import unittest
from unittest.mock import Mock, patch

from marvin.barge_in import SpeechOnset
from marvin import voice
from marvin.brain import Brain
from marvin.memory import Memory
from marvin.search import search_web, _cache


class ConversationTests(unittest.TestCase):
    def test_onset_rejects_short_noise_and_accepts_sustained_speech(self):
        detector = SpeechOnset(650)
        loud = array('h', [2000]*1600).tobytes()
        quiet = array('h', [50]*1600).tobytes()
        self.assertFalse(detector.feed(loud,16000,playing=True))
        self.assertFalse(detector.feed(quiet,16000,playing=True))
        self.assertFalse(detector.feed(loud,16000,playing=True))
        self.assertTrue(detector.feed(loud,16000,playing=True))
        self.assertFalse(detector.feed(loud,16000,playing=False))

    def test_speech_interrupt_does_not_cancel_task(self):
        task = threading.Event()
        def playback(*args):
            voice.cancel_speech()
        with patch.object(voice,'_piper_speak',side_effect=playback):
            self.assertEqual(voice.speak('Oi',voice=voice.OFFLINE_VOICE,cancel_event=task),'interrompida')
        self.assertFalse(task.is_set())

    def test_wake_capture_continues_after_interrupt_without_wake_word(self):
        stop, pause = threading.Event(), threading.Event()
        pause.set()
        loud = array('h',[2000]*1600).tobytes()
        quiet = array('h',[0]*1600).tobytes()
        def microphone(sd, callback, status):
            for block in [loud,loud,loud,quiet,quiet]:
                callback(block,1600,None,None)
            return Mock(),16000
        class Recognizer:
            def __init__(self): self.n=0
            def AcceptWaveform(self,block):
                self.n+=1
                return self.n>=4
            def Result(self): return json.dumps({'text':'explique melhor'})
        heard=[]
        def command(text):
            heard.append(text)
            stop.set()
        with patch.dict('sys.modules',{'sounddevice':types.SimpleNamespace()}), \
             patch.object(voice,'ensure_model'), patch.object(voice,'_open_microphone',side_effect=microphone), \
             patch.object(voice,'_new_recognizer',side_effect=lambda *a:Recognizer()), \
             patch.object(voice,'is_speaking',return_value=True), patch.object(voice,'cancel_speech') as cancel, \
             patch('marvin.barge_in.is_voice',return_value=True), \
             patch.dict(os.environ,{'MARVIN_BARGE_IN':'true','MARVIN_BARGE_THRESHOLD':'650'}):
            barge=Mock()
            voice.listen_wake(command,Mock(),stop,pause,on_barge=barge)
        cancel.assert_called_once()
        barge.assert_called_once()
        self.assertEqual(heard,['explique melhor'])

    def test_brave_results_are_cached_and_credentials_are_in_header(self):
        _cache.clear()
        response=Mock()
        response.__enter__=Mock(return_value=response)
        response.__exit__=Mock(return_value=False)
        response.read.return_value=json.dumps({'web':{'results':[
            {'title':'Fonte','url':'https://example.com','description':'Texto'},
            {'title':'Inválido','url':'javascript:alert(1)'}]}}).encode()
        with patch.dict(os.environ,{'BRAVE_SEARCH_API_KEY':'test-token'}), patch('marvin.search.urlopen',return_value=response) as fetch:
            first=search_web('consulta', 'brave')
            second=search_web('consulta','brave')
        self.assertEqual(first,second)
        self.assertEqual(len(first),1)
        fetch.assert_called_once()
        self.assertNotIn('test-token',fetch.call_args.args[0].full_url)

    def test_google_search_requires_sources_and_uses_thinking_level(self):
        with tempfile.TemporaryDirectory() as directory:
            memory=Memory(Path(directory)/'mem.db')
            models=Mock()
            models.generate_content.return_value=types.SimpleNamespace(text='Resposta sem evidência',candidates=[])
            with patch.dict(os.environ,{'GEMINI_API_KEY':'mock','MARVIN_SEARCH_PROVIDER':'google','MARVIN_REASONING':'profundo'}):
                brain=Brain(memory,client=types.SimpleNamespace(models=models))
                answer,sources=brain.ask('notícias',search=True)
            self.assertFalse(brain.last_ask_ok)
            self.assertEqual(sources,[])
            self.assertIn('fontes verificáveis',answer)
            config=models.generate_content.call_args.kwargs['config']
            self.assertEqual(config.thinking_config.thinking_level,'HIGH')
            self.assertIsNotNone(config.tools[0].google_search)
            self.assertEqual(memory.recent(),[])


if __name__=='__main__':
    unittest.main()
