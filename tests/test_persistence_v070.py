"""Persistent behavior under migration, concurrent calls and interrupted effects."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest

from marvin.memory import Memory, connect, migrate
from marvin.scheduler import SAO_PAULO, Scheduler, parse_reminder
from marvin.task_store import TaskStore


class DatabaseCase(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.db = self.root / "memory.db"


class MemoryMigrationTests(DatabaseCase):
    def test_old_schema_is_preserved_and_backup_is_from_before_migration(self):
        with connect(self.db) as connection:
            connection.execute("CREATE TABLE messages (id INTEGER PRIMARY KEY AUTOINCREMENT, role TEXT NOT NULL CHECK(role IN ('user','model')), content TEXT NOT NULL, created_at TEXT DEFAULT CURRENT_TIMESTAMP)")
            connection.execute("CREATE TABLE facts (id INTEGER PRIMARY KEY AUTOINCREMENT, fact TEXT NOT NULL UNIQUE, created_at TEXT DEFAULT CURRENT_TIMESTAMP)")
            connection.execute("INSERT INTO facts(fact) VALUES ('O projeto loja usa Flask')")
            connection.execute("INSERT INTO messages(role,content) VALUES ('user','Oi')")
            original_schema = [tuple(row) for row in connection.execute("PRAGMA table_info(facts)")]
        memory = Memory(self.db)
        self.assertEqual(memory.facts(), ["O projeto loja usa Flask"])
        self.assertEqual(memory.recent(), [("user", "Oi")])
        with connect(self.db) as connection:
            self.assertEqual([tuple(row) for row in connection.execute("PRAGMA table_info(facts)")], original_schema)
        backups = list((self.root / "backups").glob("*.bak"))
        self.assertEqual(len(backups), 1)
        with connect(backups[0]) as connection:
            self.assertEqual(connection.execute("SELECT fact FROM facts").fetchone()[0], "O projeto loja usa Flask")
            self.assertIsNone(connection.execute("SELECT name FROM sqlite_master WHERE name='session_context'").fetchone())
        Memory(self.db)
        self.assertEqual(list((self.root / "backups").glob("*.bak")), backups)

    def test_newer_schema_is_not_overwritten(self):
        Memory(self.db)
        with connect(self.db) as connection:
            connection.execute("UPDATE schema_migrations SET version=99 WHERE component='memory'")
        with self.assertRaisesRegex(RuntimeError, "mais novo"):
            Memory(self.db)

    def test_failed_migration_rolls_back_but_keeps_recovery_backup(self):
        Memory(self.db).remember("Projeto original")
        with self.assertRaises(sqlite3.OperationalError):
            migrate(self.db, "broken", 1, ("CREATE TABLE transient_table (id TEXT)", "THIS IS INVALID SQL"))
        with connect(self.db) as connection:
            self.assertIsNone(connection.execute("SELECT name FROM sqlite_master WHERE name='transient_table'").fetchone())
            self.assertIsNone(connection.execute("SELECT version FROM schema_migrations WHERE component='broken'").fetchone())
        self.assertEqual(Memory(self.db).facts(), ["Projeto original"])
        self.assertTrue(list((self.root / "backups").glob("*.broken.*.bak")))

    def test_relevant_facts_edit_and_delete_survive_restart(self):
        memory = Memory(self.db)
        memory.remember("Prefiro café sem açúcar", category="preference")
        fact = memory.remember("O projeto loja usa Flask", category="project")
        memory.set_context({"active_project": "loja", "summary": "Loja usa Flask", "facts": ["Flask"]})
        self.assertEqual(memory.relevant("O que lembra sobre café?"), ["Prefiro café sem açúcar"])
        memory.edit_fact(fact["id"], "O projeto loja usa Django")
        restarted = Memory(self.db)
        self.assertEqual(restarted.relevant("Flask"), [])
        self.assertEqual(restarted.relevant("Django"), ["O projeto loja usa Django"])
        self.assertEqual(restarted.get_context(), {"active_project": "loja"})
        self.assertTrue(restarted.delete_fact(fact["id"]))
        self.assertFalse(restarted.delete_fact(fact["id"]))
        self.assertEqual(Memory(self.db).relevant("Django"), [])
        with connect(self.db) as connection:
            self.assertIsNone(connection.execute("SELECT * FROM fact_metadata WHERE fact_id=?", (fact["id"],)).fetchone())

    def test_context_merges_across_threads_and_is_session_scoped(self):
        memory = Memory(self.db)
        with ThreadPoolExecutor(max_workers=6) as pool:
            list(pool.map(lambda index: memory.set_context({f"file{index}": f"{index}.py"}), range(12)))
        self.assertEqual(len(Memory(self.db).get_context()), 12)
        memory.set_context({"file0": None, "active_project": "loja"})
        memory.set_context({"active_project": "outro"}, "other")
        self.assertNotIn("file0", memory.get_context())
        self.assertEqual(memory.get_context("other"), {"active_project": "outro"})

    def test_export_and_clear_are_real_and_do_not_remove_reminders(self):
        memory = Memory(self.db)
        memory.remember("Meu editor é VS Code")
        memory.add_pair("Olá", "Olá, João")
        memory.set_context({"active_project": "loja"})
        scheduler = Scheduler(self.db)
        scheduler.add("Beber água", datetime(2030, 1, 1, 10, tzinfo=SAO_PAULO))
        exported = json.loads(json.dumps(memory.export(), ensure_ascii=False))
        self.assertEqual(len(exported["messages"]), 2)
        self.assertEqual(exported["facts"][0]["origin"], "user")
        self.assertEqual(exported["sessions"]["default"]["active_project"], "loja")
        memory.clear()
        self.assertEqual(memory.facts(), [])
        self.assertEqual(memory.recent(), [])
        self.assertEqual(memory.get_context(), {})
        self.assertEqual(len(scheduler.list_reminders()), 1)

    def test_connection_is_closed_even_after_error(self):
        memory = Memory(self.db)
        memory.remember("Uma lembrança")
        with self.assertRaises(ValueError):
            memory.set_context({"huge": "a" * 70000})
        # On Windows an open SQLite handle prevents this rename/delete cycle.
        renamed = self.db.with_name("renamed.db")
        self.db.rename(renamed)
        renamed.unlink()


class TaskRecoveryTests(DatabaseCase):
    def test_same_logical_step_has_one_winner_and_replays_recorded_result(self):
        store = TaskStore(self.db)
        task = store.create("Criar arquivo")
        with ThreadPoolExecutor(max_workers=6) as pool:
            claims = list(pool.map(lambda _: store.begin_step(task["id"], "write-1", "write", {"path": "a.txt"}), range(12)))
        self.assertEqual(sum(item["created"] for item in claims), 1)
        result = {"ok": True, "evidence": {"sha256": "observed"}}
        store.finish_step(task["id"], "write-1", result)
        retry = TaskStore(self.db).begin_step(task["id"], "write-1", "write", {"path": "a.txt"})
        self.assertFalse(retry["created"])
        self.assertEqual(retry["result"], result)
        self.assertEqual(retry["state"], "completed")

    def test_ids_identify_logical_calls_not_only_identical_arguments(self):
        store = TaskStore(self.db)
        task = store.create("Dois cliques")
        self.assertTrue(store.begin_step(task["id"], "first", "click", {"x": 20})["created"])
        store.finish_step(task["id"], "first", {"ok": True})
        self.assertTrue(store.begin_step(task["id"], "second", "click", {"x": 20})["created"])
        with self.assertRaisesRegex(ValueError, "reutilizado"):
            store.begin_step(task["id"], "first", "click", {"x": 30})

    def test_crash_preserves_done_steps_and_marks_uncertain_effect(self):
        store = TaskStore(self.db)
        task = store.create("Criar arquivo e abrir aplicativo", scope={"project": "loja"})
        store.begin_step(task["id"], "create", "write", {})
        store.finish_step(task["id"], "create", {"ok": True, "path": "index.html"})
        store.begin_step(task["id"], "open", "launch", {})
        restarted = TaskStore(self.db)
        recovered = restarted.recover_interrupted()
        self.assertEqual(recovered[0]["state"], "needs_reconciliation")
        self.assertEqual(recovered[0]["scope"], {"project": "loja"})
        self.assertEqual([step["state"] for step in restarted.steps(task["id"])], ["completed", "needs_reconciliation"])
        self.assertEqual(restarted.steps(task["id"])[0]["result"]["path"], "index.html")
        self.assertFalse(restarted.begin_step(task["id"], "open", "launch", {})["created"])
        with self.assertRaises(ValueError):
            restarted.set_state(task["id"], "running")
        with self.assertRaises(ValueError):
            restarted.begin_step(task["id"], "new", "write", {})
        self.assertEqual(restarted.recover_interrupted(), [])

    def test_cancel_blocks_new_steps_but_records_inflight_completion(self):
        store = TaskStore(self.db)
        task = store.create("Arquivo")
        store.begin_step(task["id"], "write", "write", {})
        store.set_state(task["id"], "cancelled")
        store.finish_step(task["id"], "write", {"ok": True})
        with self.assertRaises(ValueError):
            store.begin_step(task["id"], "next", "write", {})
        self.assertEqual(store.get(task["id"])["state"], "cancelled")
        self.assertEqual(store.steps(task["id"])[0]["state"], "completed")

    def test_cannot_complete_with_failure_or_pending_result(self):
        store = TaskStore(self.db)
        task = store.create("Uma tarefa")
        store.begin_step(task["id"], "one", "write", {})
        with self.assertRaises(ValueError):
            store.set_state(task["id"], "completed")
        store.finish_step(task["id"], "one", {"ok": False, "error_code": "denied"})
        with self.assertRaises(ValueError):
            store.set_state(task["id"], "completed")
        with self.assertRaises(ValueError):
            store.finish_step(task["id"], "one", {"ok": True})
        store.set_state(task["id"], "failed", "Acesso negado")
        self.assertEqual(store.events(task["id"])[-1]["message"], "Acesso negado")


class ReminderTests(DatabaseCase):
    NOW = datetime(2026, 10, 13, 23, 55, tzinfo=SAO_PAULO)

    def test_relative_time_crosses_midnight_with_explicit_timezone(self):
        parsed = parse_reminder("Me lembre daqui a 10 minutos de beber água", self.NOW)
        self.assertEqual(parsed["message"], "beber água")
        self.assertEqual(parsed["due_at"], datetime(2026, 10, 14, 0, 5, tzinfo=SAO_PAULO))
        self.assertEqual(parsed["timezone"], "America/Sao_Paulo")
        hours = parse_reminder("Me lembre de descansar daqui a duas horas", self.NOW)
        self.assertEqual(hours["message"], "descansar")
        self.assertEqual(hours["due_at"] - self.NOW, timedelta(hours=2))

    def test_tomorrow_and_iso_dates_do_not_use_host_timezone(self):
        parsed = parse_reminder("lembre amanhã às 10:00 de pagar conta", self.NOW)
        self.assertEqual(parsed["message"], "pagar conta")
        self.assertEqual(parsed["due_at"], datetime(2026, 10, 14, 10, tzinfo=SAO_PAULO))
        parsed = parse_reminder("Me lembre em 2026-10-15T13:30:00Z de reunião", self.NOW)
        self.assertEqual(parsed["message"], "reunião")
        self.assertEqual(parsed["due_at"].hour, 10)
        self.assertEqual(parsed["due_at"].minute, 30)

    def test_missing_or_ambiguous_dates_do_not_create_an_occurrence(self):
        scheduler = Scheduler(self.db)
        for text in ["Me lembre amanhã de pagar", "Me lembre de café", "Me lembre daqui a 0 minutos de café", "Me lembre amanhã às 99:00 de café", "Me lembre daqui a 2 horas amanhã às 10:00 de café", "Me lembre daqui a 2 horas e daqui a 3 horas de café", "Me lembre 2020-01-01 10:00 de café"]:
            with self.subTest(text=text), self.assertRaises(ValueError):
                scheduler.parse_and_add(text, self.NOW)
        self.assertEqual(scheduler.list_reminders(), [])

    def test_claim_crash_reclaims_same_occurrence_and_old_ack_is_rejected(self):
        scheduler = Scheduler(self.db)
        reminder = scheduler.add("Beber água", self.NOW)
        first = scheduler.claim_due(self.NOW, lease_seconds=60)[0]
        restarted = Scheduler(self.db)
        self.assertEqual(restarted.claim_due(self.NOW + timedelta(seconds=59)), [])
        second = restarted.claim_due(self.NOW + timedelta(seconds=61))[0]
        self.assertEqual(second["id"], reminder["id"])
        self.assertNotEqual(first["claim_token"], second["claim_token"])
        self.assertFalse(restarted.ack(reminder["id"], first["claim_token"]))
        self.assertTrue(restarted.ack(reminder["id"], second["claim_token"]))
        self.assertEqual(restarted.claim_due(self.NOW + timedelta(days=1)), [])
        self.assertEqual(restarted.list_reminders(), [])
        self.assertEqual(restarted.list_reminders(include_done=True)[0]["state"], "delivered")

    def test_simultaneous_claimers_do_not_duplicate_active_delivery(self):
        scheduler = Scheduler(self.db)
        scheduler.add("Lembrete", self.NOW)
        with ThreadPoolExecutor(max_workers=6) as pool:
            results = list(pool.map(lambda _: scheduler.claim_due(self.NOW), range(12)))
        self.assertEqual(sum(len(rows) for rows in results), 1)

    def test_cancellation_survives_restart_and_invalidates_pending_ack(self):
        scheduler = Scheduler(self.db)
        reminder = scheduler.add("Lembrete", self.NOW)
        claim = scheduler.claim_due(self.NOW)[0]
        self.assertTrue(scheduler.cancel(reminder["id"]))
        restarted = Scheduler(self.db)
        self.assertFalse(restarted.ack(reminder["id"], claim["claim_token"]))
        self.assertEqual(restarted.claim_due(self.NOW + timedelta(days=1)), [])
        self.assertEqual(restarted.list_reminders(include_done=True)[0]["state"], "cancelled")

    def test_persisted_times_are_utc_and_local_display_is_sao_paulo(self):
        scheduler = Scheduler(self.db)
        reminder = scheduler.add("Almoço", datetime(2026, 10, 14, 15, tzinfo=timezone.utc))
        self.assertIn("T15:00:00", reminder["due_at"])
        self.assertTrue(reminder["due_at"].endswith("+00:00"))
        self.assertTrue(reminder["due_local"].endswith("12:00:00-03:00"))
        self.assertEqual(Scheduler(self.db).claim_due(datetime(2026, 10, 14, 14, 59, tzinfo=timezone.utc)), [])


if __name__ == "__main__":
    unittest.main()
