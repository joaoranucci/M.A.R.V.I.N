import os
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

from marvin.config import load_config, reload_gemini_config
from marvin.brain import Brain, FREE_CANDIDATES
from marvin.memory import Memory
from marvin.health import collect_health, format_health


class AIReadinessTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def test_bom_and_quoted_key_load_without_exposure(self):
        (self.root / '.env').write_text('GEMINI_API_KEY="test-secret"\n', encoding='utf-8-sig')
        with patch.dict(os.environ, {}, clear=True):
            load_config(self.root)
            self.assertEqual(os.environ['GEMINI_API_KEY'], 'test-secret')
            report = collect_health(self.root)
            self.assertTrue(report['configuration']['gemini_key_present'])
            self.assertNotIn('test-secret', format_health(report))

    def test_explicit_reload_changes_key_but_not_data_or_audio(self):
        (self.root / '.env').write_text('GEMINI_API_KEY="new-key"\nMARVIN_DATA_DIR=other\nMARVIN_WAKE=true\n', encoding='utf-8')
        with patch.dict(os.environ, {'GEMINI_API_KEY': 'old', 'MARVIN_DATA_DIR': 'original', 'MARVIN_WAKE': 'false'}):
            reload_gemini_config(self.root)
            self.assertEqual(os.environ['GEMINI_API_KEY'], 'new-key')
            self.assertEqual(os.environ['MARVIN_DATA_DIR'], 'original')
            self.assertEqual(os.environ['MARVIN_WAKE'], 'false')

    def test_invalid_reload_preserves_working_key(self):
        for content in ('', 'GEMINI_API_KEY=COLE_SUA_CHAVE_AQUI'):
            (self.root / '.env').write_text(content, encoding='utf-8')
            with patch.dict(os.environ, {'GEMINI_API_KEY': 'working'}):
                with self.assertRaises(ValueError):
                    reload_gemini_config(self.root)
                self.assertEqual(os.environ['GEMINI_API_KEY'], 'working')

    def brain(self, responses):
        memory = Memory(self.root / 'memory.db')
        models = Mock()
        models.generate_content.side_effect = responses
        models.list.return_value = [SimpleNamespace(name=name, supported_actions=['generateContent']) for name in FREE_CANDIDATES]
        with patch.dict(os.environ, {'GEMINI_API_KEY': 'fake'}):
            return Brain(memory, client=SimpleNamespace(models=models))

    def test_empty_conversation_is_not_success_or_memory(self):
        brain = self.brain([SimpleNamespace(text='  '), None])
        brain.ask('oi')
        self.assertFalse(brain.last_ask_ok)
        self.assertIsNone(brain.active_model)
        self.assertEqual(brain.memory.recent(), [])

    def test_empty_response_falls_back_to_text(self):
        brain = self.brain([None, SimpleNamespace(text='Olá')])
        answer, _ = brain.ask('oi')
        self.assertEqual(answer, 'Olá')
        self.assertTrue(brain.last_ask_ok)
        self.assertEqual(brain.active_model, FREE_CANDIDATES[1])

    def test_diagnostic_rejects_empty_generation(self):
        brain = self.brain([SimpleNamespace(text=None), SimpleNamespace(text='')])
        result = brain.diagnose()
        self.assertIn('Nenhum modelo passou', result)
        self.assertNotIn('geração funcionando', result)

    def test_diagnostic_records_verified_model(self):
        brain = self.brain([SimpleNamespace(text='OK')])
        self.assertIn('geração funcionando', brain.diagnose())
        self.assertEqual(brain.active_model, FREE_CANDIDATES[0])
