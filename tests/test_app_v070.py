"""Real Tk event-loop smoke tests; no physical audio, desktop action or API."""
import os
from pathlib import Path
import tempfile
import time
import tkinter as tk
import unittest
from unittest.mock import patch

from marvin.app import MarvinApp
from marvin.runtime import TaskControl


class AppTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        root = Path(self.tmp.name)
        self.env = patch.dict(os.environ, {'MARVIN_DATA_DIR': str(root/'data'),
            'MARVIN_WORKSPACE_DIR': str(root/'projects'), 'MARVIN_WAKE': 'false',
            'MARVIN_SPEAK': 'false', 'MARVIN_VISUAL': 'false', 'GEMINI_API_KEY': ''})
        self.env.start()
        self.addCleanup(self.env.stop)
        self.path_patch = patch('marvin.app.ROOT', root)
        self.path_patch.start()
        self.addCleanup(self.path_patch.stop)
        original = tk.Tk
        def withdrawn():
            window = original()
            window.withdraw()
            return window
        try:
            with patch('marvin.app.tk.Tk', side_effect=withdrawn):
                self.app = MarvinApp()
        except tk.TclError as exc:
            self.skipTest('Tk display unavailable: ' + str(exc))
        self.addCleanup(self.close)

    def close(self):
        self.app.on_close()
        deadline = time.monotonic()+3
        while not self.app.instance_lock.stream.closed and time.monotonic()<deadline:
            time.sleep(.01)
        self.assertTrue(self.app.instance_lock.stream.closed)

    def pump(self, predicate, seconds=3):
        end = time.monotonic()+seconds
        while not predicate() and time.monotonic()<end:
            self.app.window.update()
            time.sleep(.01)
        self.assertTrue(predicate())

    def test_text_queue_runs_through_ui_and_persists_results(self):
        self.app.process('Marvin, lembre que uso Python')
        self.app.process('o que você lembra de mim?')
        self.pump(lambda: not self.app.busy and not self.app.pending)
        tasks = self.app.runtime.tasks.list_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertTrue(all(t['state']=='completed' for t in tasks))
        self.assertIn('uso Python', self.app.chat.get('1.0', 'end'))
        self.assertIn('uso Python', self.app.memory.facts())

    def test_stale_voice_result_cannot_execute_new_command(self):
        stale = TaskControl()
        self.app.post('heard', (stale, 'lembre que NAO_EXECUTAR'))
        self.app.poll_ui()
        self.assertEqual(self.app.memory.facts(), [])
        self.assertEqual(self.app.runtime.tasks.list_tasks(), [])

    def test_oversized_input_does_not_leave_busy(self):
        self.app.text.insert(0, 'x'*12001)
        self.app.send()
        self.assertFalse(self.app.busy)
        self.assertEqual(self.app.runtime.tasks.list_tasks(), [])

    def test_cancel_removes_queued_work(self):
        self.app.busy = True
        self.app.process('lembre que nunca será executado')
        self.assertEqual(len(self.app.pending), 1)
        self.app.cancel_all()
        self.assertEqual(self.app.pending, [])
        self.assertEqual(self.app.runtime.tasks.list_tasks()[0]['state'], 'cancelled')
        self.assertEqual(self.app.memory.facts(), [])
        self.app.busy = False

    def test_panels_read_real_storage(self):
        self.app.memory.remember('Preferência de teste')
        self.app.show_memory()
        self.app.show_tasks()
        self.app.show_reminders()
        self.app.window.update()
        self.assertGreaterEqual(sum(isinstance(w, tk.Toplevel) for w in self.app.window.winfo_children()), 3)


if __name__=='__main__':
    unittest.main()
