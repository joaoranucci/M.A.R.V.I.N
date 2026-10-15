import os
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

from marvin.commands import detect
from marvin.memory import Memory
from marvin.runtime import Runtime
from marvin.workspace import ProjectWorkspace
from marvin.power import shutdown_computer


class PowerTests(unittest.TestCase):
    def test_explicit_requests(self):
        for text in ('Marvin, desligue meu computador', 'desliga o PC',
                     'pode desligar meu notebook', 'desligue o computador agora, por favor'):
            with self.subTest(text=text):
                self.assertEqual(detect(text).value, 'power:shutdown')

    def test_mentions_negation_and_extra_commands_do_not_shutdown(self):
        for text in ('não desligue meu computador', 'como desligar o computador',
                     'explique desligue meu computador', 'desligue meu computador e apague arquivos',
                     'se eu pedir desligue meu computador', 'desligue a luz', '"desligue meu computador"'):
            with self.subTest(text=text):
                self.assertNotEqual(detect(text).value, 'power:shutdown')

    @unittest.skipUnless(os.name == 'nt', 'Windows shutdown transport')
    def test_fixed_command_without_forced_closing(self):
        with patch('marvin.power.subprocess.run', return_value=SimpleNamespace(returncode=0)) as run:
            self.assertIn('enviado', shutdown_computer())
        args, kwargs = run.call_args
        self.assertEqual(args[0][1:], ['/s', '/t', '0'])
        self.assertTrue(Path(args[0][0]).is_absolute())
        self.assertFalse(kwargs['shell'])

    @unittest.skipUnless(os.name == 'nt', 'Windows shutdown transport')
    def test_failure_is_not_reported_as_success(self):
        with patch('marvin.power.subprocess.run', return_value=SimpleNamespace(returncode=5)):
            with self.assertRaises(OSError): shutdown_computer()

    def test_runtime_no_confirmation_or_model_and_no_replay(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            agent = SimpleNamespace(assist=Mock())
            confirm = Mock(return_value=False)
            runtime = Runtime(Memory(root/'db.sqlite'), ProjectWorkspace(root/'projects'), agent,
                              confirm_action=confirm)
            with patch('marvin.power.shutdown_computer', return_value='Pedido enviado.') as shutdown:
                task = runtime.prepare('Marvin, desligue meu computador')
                runtime.run(task['objective'], task['id'])
                runtime.run(task['objective'], task['id'])
            shutdown.assert_called_once()
            confirm.assert_not_called()
            agent.assist.assert_not_called()
