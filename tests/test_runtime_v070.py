import json
import os
from pathlib import Path
import tempfile
import threading
import time
import types
import unittest
from unittest.mock import patch, Mock

from marvin.memory import Memory
from marvin.workspace import ProjectWorkspace
from marvin.runtime import Runtime, TaskControl
from marvin.config import load_config
from marvin.instance import InstanceLock
from marvin.maintenance import snapshot, restore_code
from marvin.telemetry import EventLog


class RuntimeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.mem = Memory(self.root/'data'/'db.sqlite')
        self.space = ProjectWorkspace(self.root/'projects')
        self.agent = types.SimpleNamespace(assist=Mock(return_value='Sem alteração'), last_outcome='completed')
        self.runtime = Runtime(self.mem, self.space, self.agent)

    def test_local_memory_survives_restart_without_model(self):
        result = self.runtime.run('Marvin, lembre que eu gosto de café')
        self.assertEqual(result['state'], 'completed')
        new = Runtime(Memory(self.mem.db_path), self.space, self.agent)
        result = new.run('o que você lembra de mim?')
        self.assertIn('gosto de café', result['answer'])
        self.agent.assist.assert_not_called()
        step = new.tasks.steps(result['task_id'])[0]
        self.assertEqual(step['state'], 'completed')

    def test_same_task_cannot_repeat_effect(self):
        prepared = self.runtime.prepare('Marvin, lembre que gosto de azul')
        with patch.object(self.mem, 'remember', wraps=self.mem.remember) as remember:
            first = self.runtime.run(prepared['objective'], prepared['id'])
            second = self.runtime.run(prepared['objective'], prepared['id'])
        self.assertEqual(remember.call_count, 1)
        self.assertEqual(first['answer'], second['answer'])
        with self.assertRaises(ValueError):
            self.runtime.run('outro pedido', prepared['id'])

    def test_close_requires_permission_in_core(self):
        with patch('marvin.runtime.execute_local') as execute:
            result = self.runtime.run('feche a janela')
        execute.assert_not_called()
        self.assertEqual(result['state'], 'waiting_user')

    def test_open_reference_records_request_not_observed_success(self):
        self.space.create_project('loja')
        self.mem.set_context({'project': 'loja'})
        with patch.object(self.space, 'open_project', return_value={'ok': True, 'status': 'requested'}) as opened:
            result = self.runtime.run('agora abre o último projeto')
        opened.assert_called_once_with('loja', '')
        self.assertEqual(result['state'], 'needs_reconciliation')

    def test_reference_without_project_asks_for_name(self):
        result = self.runtime.run('abra o resultado')
        self.assertEqual(result['state'], 'waiting_user')
        self.agent.assist.assert_not_called()

    def test_reminder_local_and_ambiguous_date(self):
        good = self.runtime.run('me lembre daqui a 10 minutos de beber água')
        bad = self.runtime.run('me lembre amanhã de beber água')
        self.assertEqual(good['state'], 'completed')
        self.assertEqual(bad['state'], 'waiting_user')
        self.assertEqual(len(self.runtime.scheduler.list_reminders()), 1)

    def test_cancel_before_action(self):
        token = TaskControl()
        token.set()
        result = self.runtime.run('lembre que teste', control=token)
        self.assertEqual(result['state'], 'cancelled')
        self.assertEqual(self.mem.facts(), [])

    def test_paused_worker_resumes_and_keeps_result(self):
        started = threading.Event()
        proceed = threading.Event()
        output = []
        def assist(question, notify, task_id, cancel_event):
            started.set()
            proceed.wait(2)
            cancel_event.wait_if_paused()
            return 'Terminei'
        self.agent.assist = assist
        worker = threading.Thread(target=lambda: output.append(self.runtime.run('Oi')))
        worker.start()
        self.assertTrue(started.wait(2))
        self.runtime.pause()
        proceed.set()
        deadline = time.monotonic()+2
        while time.monotonic() < deadline and self.runtime.tasks.get(self.runtime.active_id)['state'] != 'paused':
            time.sleep(.01)
        self.assertEqual(self.runtime.tasks.get(self.runtime.active_id)['state'], 'paused')
        self.runtime.resume()
        worker.join(2)
        self.assertFalse(worker.is_alive())
        self.assertEqual(output[0]['state'], 'completed')

    def test_observer_failure_does_not_reexecute(self):
        self.runtime.emit = Mock(side_effect=RuntimeError('observer broken'))
        result = self.runtime.run('lembre que uso Python')
        self.assertEqual(result['state'], 'completed')
        self.assertEqual(len(self.mem.facts()), 1)

    def test_explicit_test_configuration_beats_saved_preferences(self):
        data = self.root/'other'
        data.mkdir()
        (data/'preferences.json').write_text(json.dumps({'MARVIN_WAKE': 'true'}))
        with patch.dict(os.environ, {'MARVIN_DATA_DIR': str(data), 'MARVIN_WAKE': 'false'}):
            load_config(self.root)
            self.assertEqual(os.environ['MARVIN_WAKE'], 'false')

    def test_singleton_and_metadata_only_logs(self):
        lock = InstanceLock(self.root/'locks')
        try:
            with self.assertRaises(RuntimeError):
                InstanceLock(self.root/'locks')
        finally:
            lock.close()
        next_lock = InstanceLock(self.root/'locks')
        next_lock.close()
        log = EventLog(self.root/'logs')
        log.record({'type': 'task.finished', 'payload': {'objective': 'SEGREDO', 'state': 'completed'}})
        log.close()
        content = (self.root/'logs'/'events.jsonl').read_text(encoding='utf-8')
        self.assertNotIn('SEGREDO', content)
        self.assertIn('completed', content)

    def test_code_recovery_preserves_data_and_configuration(self):
        (self.root/'main.py').write_text('x = 1')
        (self.root/'.env').write_text('SECRET=unchanged')
        old = snapshot(self.root)
        (self.root/'main.py').write_text('x = 2')
        restore_code(old, self.root)
        self.assertEqual((self.root/'main.py').read_text(), 'x = 1')
        self.assertEqual((self.root/'.env').read_text(), 'SECRET=unchanged')
        self.assertTrue(self.mem.db_path.exists())

    def test_scripted_engineering_demo_runs_real_failing_then_passing_test(self):
        from marvin.demo import demonstrate
        result = demonstrate(self.root/'demo')
        self.assertEqual(result['before_exit_code'], 1)
        self.assertEqual(result['after_exit_code'], 0)
        self.assertEqual(result['tests']['test_count'], 1)
        self.assertTrue((Path(result['directory'])/'app.py').is_file())
        self.assertTrue(result['scripted_demo'])


if __name__ == '__main__':
    unittest.main()
