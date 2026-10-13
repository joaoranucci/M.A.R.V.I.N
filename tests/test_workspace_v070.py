"""Real temporary-file and subprocess checks of project engineering safeguards."""
from __future__ import annotations

import json
import os
from pathlib import Path
import tempfile
import threading
import time
import unittest
from unittest.mock import patch

from marvin.process_runner import filtered_environment
from marvin.self_edit import SourceEditor
from marvin.workspace import ProjectWorkspace, atomic_write


class WorkspaceEngineeringTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.workspace = ProjectWorkspace(self.root / "projects")
        self.workspace.create_project("Loja")

    def test_compare_and_swap_preserves_external_change(self):
        original = self.workspace.write_project_file("Loja", "app.py", "value = 1\n")
        target = Path(original["file"])

        def approve(path):
            path.write_text("value = 3\n", encoding="utf-8")
            return True

        with self.assertRaisesRegex(RuntimeError, "Conflito"):
            self.workspace.write_project_file("Loja", "app.py", "value = 2\n", True, approve, original["sha256"])
        self.assertEqual(target.read_text(), "value = 3\n")
        with self.assertRaisesRegex(RuntimeError, "Conflito"):
            self.workspace.write_project_file("Loja", "app.py", "value = 2\n", True, lambda p: True, original["sha256"])

    def test_new_file_atomic_publication_refuses_race(self):
        target = self.workspace.project_path("Loja", "already.txt")
        target.write_bytes(b"first")
        with self.assertRaises(FileExistsError):
            atomic_write(target, b"second", replace=False)
        self.assertEqual(target.read_bytes(), b"first")
        self.assertFalse(list(target.parent.glob(".marvin-*.tmp")))

    def test_write_failure_keeps_original_and_backup(self):
        self.workspace.write_project_file("Loja", "app.py", "value = 1\n")
        with patch("marvin.workspace.os.replace", side_effect=OSError("injected disk failure")):
            with self.assertRaises(OSError):
                self.workspace.write_project_file("Loja", "app.py", "value = 2\n", True, lambda p: True)
        self.assertEqual(self.workspace.read_project_file("Loja", "app.py")["content"], "value = 1\n")
        backups = list((self.workspace.project_path("Loja") / ".marvin_versions").rglob("app.py"))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_text(), "value = 1\n")

    def test_private_and_windows_aliases_are_rejected(self):
        for name in (".env", ".ENV.local", ".marvin_versions/x.txt", ".MARVIN_VERSIONS/x.txt", "foo./a.py", "COM¹.txt", "dir/NUL.py", "hello ", "a.py:secret", ".aws/config", "cert.pem"):
            with self.subTest(name=name), self.assertRaises((PermissionError, ValueError)):
                self.workspace.write_project_file("Loja", name, "secret")
        self.workspace.write_project_file("Loja", ".env.example", "API_KEY=\n")

    def test_protected_backup_link_cannot_write_outside(self):
        self.workspace.write_project_file("Loja", "app.py", "value = 1\n")
        outside = self.root / "outside"
        outside.mkdir()
        alias = self.workspace.project_path("Loja") / ".marvin_versions"
        try:
            alias.symlink_to(outside, target_is_directory=True)
        except OSError:
            self.skipTest("Symlink creation unavailable for this Windows account")
        with self.assertRaises(PermissionError):
            self.workspace.write_project_file("Loja", "app.py", "value = 2\n", True, lambda p: True)
        self.assertFalse(list(outside.iterdir()))

    def test_hardlink_cannot_read_private_file(self):
        secret = self.root / "secret.txt"
        secret.write_text("secret")
        os.link(secret, self.workspace.project_path("Loja") / "innocent.txt")
        with self.assertRaises(PermissionError):
            self.workspace.read_project_file("Loja", "innocent.txt")

    def test_patch_requires_unique_text_and_preserves_backup(self):
        write = self.workspace.write_project_file("Loja", "app.py", "price = 2\n")
        fixed = self.workspace.patch_project_file("Loja", "app.py", "2", "3", write["sha256"], lambda p: True)
        self.assertEqual(Path(fixed["backup"]).read_text(), "price = 2\n")
        self.assertEqual(self.workspace.read_project_file("Loja", "app.py")["content"], "price = 3\n")

    def test_static_checks_find_real_defects_without_execution(self):
        self.workspace.write_project_file("Loja", "app.py", "from pathlib import Path\nPath('should-not-exist').write_text('bad')\n")
        self.workspace.write_project_file("Loja", "products.json", '{"products": [}')
        self.workspace.write_project_file("Loja", "index.html", '<script src="missing.js"></script>')
        result = self.workspace.verify_project("Loja")
        self.assertFalse(result["ok"])
        self.assertEqual(result["evidence"]["failed"], 2)
        self.assertFalse((self.workspace.project_path("Loja") / "should-not-exist").exists())
        self.workspace.write_project_file("Loja", "products.json", '{"products": []}', True, lambda p: True)
        self.workspace.write_project_file("Loja", "missing.js", "console.log('ready')")
        self.assertTrue(self.workspace.verify_project("Loja")["ok"])

    def test_secret_content_excluded_from_search_and_listing(self):
        (self.workspace.project_path("Loja") / ".env").write_text("SECRET=hunter2")
        self.workspace.write_project_file("Loja", "readme.md", "hello")
        self.assertEqual(self.workspace.search_project_files("Loja", "hunter2")["matches"], [])
        self.assertNotIn(".env", self.workspace.list_project_files("Loja")["files"])
        self.assertEqual(self.workspace.list_projects()["projects"][0]["project"], "loja")

    def test_execution_requires_concrete_approval(self):
        self.workspace.write_project_file("Loja", "test_app.py", "import unittest\nclass Test(unittest.TestCase):\n def test_ok(self): self.assertEqual(2+2,4)\n")
        with self.assertRaises(PermissionError):
            self.workspace.run_project_check("Loja")
        requests = []
        result = self.workspace.run_project_check("Loja", approve_execution=lambda request: requests.append(request) or True)
        self.assertTrue(result["ok"], result)
        self.assertEqual(result["evidence"]["test_count"], 1)
        self.assertEqual(result["exit_code"], 0)
        self.assertIn("unittest", requests[0]["argv"])
        self.assertIn("não é uma sandbox", requests[0]["warning"])

    def test_empty_suite_is_not_reported_as_test_success(self):
        result = self.workspace.run_project_check("Loja", approve_execution=lambda request: True)
        self.assertEqual(result["status"], "not_checked")
        self.assertFalse(result["ok"])

    def test_process_timeout_cancellation_and_bounded_output(self):
        self.workspace.write_project_file("Loja", "test_slow.py", "import time\nprint('x' * 100000, flush=True)\ntime.sleep(20)\n")
        result = self.workspace.run_project_check("Loja", timeout=.6, approve_execution=lambda request: True)
        self.assertEqual(result["status"], "timed_out")
        self.assertTrue(result["truncated"])
        self.assertLessEqual(len(result["stdout"]), 32000)
        event = threading.Event()
        timer = threading.Timer(.4, event.set)
        timer.start()
        self.addCleanup(timer.cancel)
        started = time.monotonic()
        result = self.workspace.run_project_check("Loja", cancel_event=event, approve_execution=lambda request: True)
        self.assertEqual(result["status"], "cancelled")
        self.assertLess(time.monotonic() - started, 8)

    def test_process_environment_omits_credentials(self):
        with patch.dict(os.environ, {"GEMINI_API_KEY": "top-secret", "GOOGLE_APPLICATION_CREDENTIALS": "private.json", "NODE_OPTIONS": "--require=bad.js", "PYTHONPATH": "bad", "PATH": "system-bin"}):
            env = filtered_environment()
        self.assertEqual(env["PATH"], "system-bin")
        for key in ("GEMINI_API_KEY", "GOOGLE_APPLICATION_CREDENTIALS", "NODE_OPTIONS", "PYTHONPATH"):
            self.assertNotIn(key, env)


class MultiFileProposalTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "marvin").mkdir()
        for name in ("first.py", "second.py"):
            (self.root / "marvin" / name).write_text("value = 1\n", encoding="utf-8")
        self.editor = SourceEditor(self.root)

    def propose(self):
        return self.editor.propose_changes({"marvin/first.py": "value = 2\n", "marvin/second.py": "value = 3\n"}, "Consistent two-file update")

    def test_proposal_review_apply_and_rollback(self):
        proposal = self.propose()
        token = proposal["proposal_id"]
        self.assertIn("+value = 2", self.editor.diff(token))
        self.assertIn("+value = 3", self.editor.diff(token))
        self.assertEqual((self.root / "marvin/first.py").read_text(), "value = 1\n")
        self.assertEqual(len(self.editor.pending()[0]["files"]), 2)
        applied = self.editor.apply_reviewed(token)
        self.assertEqual(applied["evidence"]["verified_files"], 2)
        self.assertEqual((self.root / "marvin/second.py").read_text(), "value = 3\n")
        self.assertEqual(self.editor.pending(), [])
        self.editor.rollback_reviewed(token)
        self.assertEqual((self.root / "marvin/first.py").read_text(), "value = 1\n")
        self.assertEqual((self.root / "marvin/second.py").read_text(), "value = 1\n")

    def test_any_stale_file_prevents_entire_apply(self):
        proposal = self.propose()
        (self.root / "marvin/second.py").write_text("external = True\n")
        with self.assertRaises(RuntimeError):
            self.editor.apply_reviewed(proposal["proposal_id"])
        self.assertEqual((self.root / "marvin/first.py").read_text(), "value = 1\n")

    def test_mid_apply_failure_rolls_back_prior_files(self):
        proposal = self.propose()
        actual = atomic_write

        def fail_second(target, data, **kwargs):
            if Path(target).resolve() == (self.root / "marvin/second.py").resolve():
                raise OSError("simulated failure")
            return actual(target, data, **kwargs)

        with patch("marvin.self_edit.atomic_write", side_effect=fail_second):
            with self.assertRaisesRegex(RuntimeError, "rolled_back"):
                self.editor.apply_reviewed(proposal["proposal_id"])
        self.assertEqual((self.root / "marvin/first.py").read_text(), "value = 1\n")
        manifest = json.loads((self.root / "data/code_backups" / proposal["proposal_id"] / "transaction.json").read_text())
        self.assertEqual(manifest["status"], "rolled_back")

    def test_proposal_tampering_and_stale_rollback_blocked(self):
        proposal = self.propose()
        token = proposal["proposal_id"]
        payload = self.root / "data/code_proposals" / f"{token}.0.new"
        original = payload.read_bytes()
        payload.write_text("tampered = True\n")
        with self.assertRaises(RuntimeError):
            self.editor.apply_reviewed(token)
        payload.write_bytes(original)
        self.editor.apply_reviewed(token)
        (self.root / "marvin/second.py").write_text("external = True\n")
        with self.assertRaises(RuntimeError):
            self.editor.rollback_reviewed(token)
        self.assertEqual((self.root / "marvin/first.py").read_text(), "value = 2\n")


if __name__ == "__main__":
    unittest.main()
