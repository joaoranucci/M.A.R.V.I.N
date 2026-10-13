import os
import sys
import tempfile
import types as builtin_types
import unittest
from unittest.mock import patch
from pathlib import Path
from marvin.brain import Brain, friendly_error, FREE_CANDIDATES
from marvin.commands import detect, execute_local
from marvin.memory import Memory
from marvin.voice import wake_phrase, MALE_EDGE_VOICES

class Error404(Exception):
    code = 404

class Error429(Exception):
    code = 429

class FakePart:
    @staticmethod
    def from_text(text):
        return text

class FakeContent:
    def __init__(self, role, parts):
        self.role, self.parts = role, parts

class FakeConfig:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

class FakeModels:
    def __init__(self):
        self.attempted = []
    def generate_content(self, model, contents, config):
        self.attempted.append(model)
        if model == 'gemini-3.5-flash-lite':
            raise Error404('404 NOT_FOUND')
        return builtin_types.SimpleNamespace(text='Olá, sou o Marvin!')
    def list(self):
        return [builtin_types.SimpleNamespace(name='models/gemini-3.5-flash-lite', supported_actions=['generateContent'])]

class FakeClient:
    def __init__(self):
        self.models = FakeModels()

class UpgradeTests(unittest.TestCase):
    def test_wake_word_c_marvin(self):
        for sentence in ('C Marvin', 'Cê Marvin', 'Se Marvin', 'Ei Marvin', 'Hey Marvin', 'Marvin'):
            self.assertEqual(wake_phrase(sentence), (True, ''))

    def test_wake_with_command(self):
        self.assertEqual(wake_phrase('C Marvin, abra a calculadora'), (True, 'abra a calculadora'))
        self.assertEqual(wake_phrase('Ei Marvin pesquise no Google por python'), (True, 'pesquise no google por python'))

    def test_wake_requires_name(self):
        self.assertEqual(wake_phrase('abra a calculadora'), (False, ''))
        self.assertEqual(wake_phrase('martelo'), (False, ''))

    def test_c_marvin_command_detect(self):
        self.assertEqual(detect('C Marvin, abra a calculadora').value, 'open-app:calculadora')
        self.assertEqual(detect('Ei Marvin abre o bloco de notas').value, 'open-app:bloco de notas')

    def test_google_search_opens_browser_not_grounding(self):
        command = detect('C Marvin, pesquise no Google por Docker')
        self.assertEqual(command.kind, 'local')
        self.assertEqual(command.value, 'google-browser:docker')
        with patch('marvin.commands.webbrowser.open') as opened:
            execute_local(command.value)
        self.assertEqual(opened.call_count, 1)
        self.assertIn('google.com/search', opened.call_args.args[0])

    def test_no_untrusted_shell(self):
        self.assertEqual(detect('C Marvin executar powershell deletar pasta').kind, 'ask')

    def test_male_voice_list_only(self):
        self.assertTrue(all(name.startswith('pt-BR-') and name.endswith('Neural') for name in MALE_EDGE_VOICES))
        self.assertIn('pt-BR-AntonioNeural', MALE_EDGE_VOICES)

    def test_errors(self):
        self.assertIn('404', friendly_error(Error404('not found')))
        self.assertIn('Limite gratuito', friendly_error(Error429('RESOURCE_EXHAUSTED')))

    def test_legacy_env_model_is_ignored(self):
        with tempfile.TemporaryDirectory() as t:
            with patch.dict(os.environ, {'GEMINI_MODEL': 'gemini-2.5-flash', 'GEMINI_API_KEY': 'fake-test-key'}):
                brain = Brain(Memory(Path(t) / 'db.sqlite'), client=FakeClient())
                self.assertEqual(brain._models(), list(FREE_CANDIDATES))

    def test_failover_to_free_model_on_404(self):
        with tempfile.TemporaryDirectory() as t:
            fake = FakeClient()
            with patch.dict(os.environ, {'GEMINI_MODEL': 'gemini-3.5-flash-lite', 'GEMINI_API_KEY': 'fake-test-key'}):
                brain = Brain(Memory(Path(t) / 'db.sqlite'), client=fake)
                fake_google = builtin_types.ModuleType('google')
                fake_genai = builtin_types.ModuleType('google.genai')
                fake_genai.types = builtin_types.SimpleNamespace(Content=FakeContent, Part=FakePart, GenerateContentConfig=FakeConfig)
                with patch.dict(sys.modules, {'google': fake_google, 'google.genai': fake_genai}):
                    result, sources = brain.ask('Oi')
                self.assertEqual(result, 'Olá, sou o Marvin!')
                self.assertEqual(sources, [])
                self.assertEqual(fake.models.attempted, list(FREE_CANDIDATES))
                self.assertEqual(brain.active_model, 'gemini-3.1-flash-lite')

    def test_diagnostic_list_warns_it_is_not_generation(self):
        with tempfile.TemporaryDirectory() as t:
            with patch.dict(os.environ, {'GEMINI_API_KEY': 'fake-test-key'}):
                brain = Brain(Memory(Path(t) / 'db.sqlite'), client=FakeClient())
                self.assertIn('encontrados', brain.diagnose())

if __name__ == '__main__':
    unittest.main()
