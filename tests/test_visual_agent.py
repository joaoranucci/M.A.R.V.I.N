import os
import unittest
from unittest.mock import patch
from marvin.visual_agent import VisualSettings, visual_intent, visual_risk, VisualAgent

class VisualTests(unittest.TestCase):
 def test_interactions(self):
  for s in ['Marvin, clique no botão salvar', 'Marvin, abre o VS Code e ativa o autosave',
            'preencha o formulário', 'Marvin, mude a configuração do VS Code']:
   self.assertTrue(visual_intent(s),s)
 def test_questions_stay_in_brain(self):
  for s in ['Marvin, pesquise no Google por python', 'Marvin, abra o Discord',
            'Como configurar o VS Code?', 'Explique como clicar no botão salvar']:
   self.assertFalse(visual_intent(s),s)
 def test_sensitive(self):
  self.assertTrue(visual_risk('Envie a mensagem para o cliente'))
  self.assertFalse(visual_risk('clique em configurações'))
 def test_configuration_guard(self):
  with patch.dict(os.environ,{'UI_TARS_BASE_URL':'http://exemplo.com/v1','UI_TARS_MODEL':'ui-tars','UI_TARS_ALLOW_REMOTE':'false'}):
   with self.assertRaisesRegex(RuntimeError,'HTTPS'):
    VisualSettings.from_env()
  with patch.dict(os.environ,{'UI_TARS_BASE_URL':'https://example.com/v1','UI_TARS_MODEL':'ui-tars','UI_TARS_ALLOW_REMOTE':'false'}):
   with self.assertRaisesRegex(RuntimeError,'autorizar'):
    VisualSettings.from_env()
 def test_local_configuration(self):
  with patch.dict(os.environ,{'UI_TARS_BASE_URL':'http://127.0.0.1:8000/v1','UI_TARS_MODEL':'ui-tars-1.5-7b','UI_TARS_MAX_STEPS':'500'}):
   self.assertEqual(VisualSettings.from_env().max_steps,25)
 def test_empty_agent(self):
  with self.assertRaises(ValueError): VisualAgent().run('')
 def test_cancelled_visual_does_not_launch_process(self):
  import threading
  stop = threading.Event()
  stop.set()
  with patch('marvin.visual_agent.subprocess.Popen') as process:
   with self.assertRaisesRegex(RuntimeError, 'cancelada'):
    VisualAgent().run('clique no botão', cancel_event=stop)
  process.assert_not_called()
 def test_negation_and_quoted_commands_are_not_visual_orders(self):
  self.assertFalse(visual_intent('não clique em salvar'))
  self.assertFalse(visual_intent('explique "clique em salvar"'))
if __name__=='__main__': unittest.main()
