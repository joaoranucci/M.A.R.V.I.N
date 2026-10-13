"""Agent contract, persistence, SDK correlation, cancellation and scope regressions."""
from pathlib import Path
import os
import sys
import tempfile
import threading
import types
import unittest
from unittest.mock import patch

from marvin.action_agent import ActionAgent, action_prompt, function_response_part, SPEC
from marvin.brain import Brain, FREE_CANDIDATES, friendly_error
from marvin.memory import Memory
from marvin.self_edit import SourceEditor
from marvin.task_store import TaskStore
from marvin.tool_registry import ToolRegistry
from marvin.workspace import ProjectWorkspace


class Part:
    @staticmethod
    def from_text(text):
        return types.SimpleNamespace(text=text)

    @staticmethod
    def from_function_response(*, name, response):
        return types.SimpleNamespace(function_response=types.SimpleNamespace(name=name, response=response, id=None))


class Opts:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class SDK:
    Part = Part
    Content = GenerateContentConfig = Tool = FunctionDeclaration = Opts
    AutomaticFunctionCallingConfig = ToolConfig = FunctionCallingConfig = Opts


class Unavailable(Exception):
    code = 503


def fn(name="create_project", args=None, call_id="one", marker=None):
    call = types.SimpleNamespace(name=name, args=args if args is not None else {"name": "Demo"}, id=call_id)
    content = types.SimpleNamespace(role="model", parts=[marker or {"opaque_signature": "preserve-me"}])
    return types.SimpleNamespace(function_calls=[call], candidates=[types.SimpleNamespace(content=content)])


def text(answer="Pronto"):
    return types.SimpleNamespace(function_calls=[], text=answer)


class Models:
    def __init__(self, outcomes):
        self.outcomes, self.calls = list(outcomes), []

    def generate_content(self, **kwargs):
        self.calls.append({**kwargs, "contents": list(kwargs["contents"])})
        outcome = self.outcomes.pop(0)
        if isinstance(outcome, Exception):
            raise outcome
        return outcome


class AgentRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "marvin").mkdir()
        (self.root / "marvin" / "demo.py").write_text("x = 1\n", encoding="utf-8")
        self.memory = Memory(self.root / "memory.db")
        self.store = TaskStore(self.root / "memory.db")
        self.workspace = ProjectWorkspace(self.root / "projects")
        self.task = self.store.create("Crie projeto Demo")
        fake = types.ModuleType("google.genai")
        fake.types = SDK
        patcher = patch.dict(sys.modules, {"google.genai": fake})
        patcher.start()
        self.addCleanup(patcher.stop)

    def agent(self, outcomes):
        models = Models(outcomes)
        with patch.dict(os.environ, {"GEMINI_API_KEY": "not-a-real-key", "GEMINI_MODEL": FREE_CANDIDATES[0]}):
            brain = Brain(self.memory, client=types.SimpleNamespace(models=models))
        return ActionAgent(brain, self.memory, self.workspace, SourceEditor(self.root), task_store=self.store), models

    def test_real_effect_recorded_before_serialization_error(self):
        agent, models = self.agent([fn()])
        with patch.object(Part, "from_function_response", side_effect=TypeError("unsupported factory")):
            answer = agent.assist("Crie projeto Demo", task_id=self.task["id"])
        self.assertIn("não repeti", answer)
        self.assertTrue(self.workspace.project_path("Demo").is_dir())
        self.assertEqual(len(models.calls), 1)
        row = self.store.steps(self.task["id"])[0]
        self.assertEqual(row["state"], "completed")
        self.assertTrue(row["result"]["ok"])
        self.assertEqual(agent.last_outcome, "failed")

    def test_old_factory_preserves_call_id_and_candidate_identity(self):
        first = fn(call_id="original-call")
        agent, models = self.agent([first, text()])
        agent.assist("Crie projeto Demo", task_id=self.task["id"])
        sent = models.calls[1]["contents"]
        self.assertIs(sent[-2], first.candidates[0].content)
        self.assertEqual(sent[-1].parts[0].function_response.id, "original-call")
        self.assertEqual(agent.last_outcome, "completed")
        self.assertEqual(self.memory.get_context()["project"], "demo")

    def test_repeated_provider_id_reuses_recorded_result(self):
        agent, _ = self.agent([fn(), fn(), text()])
        with patch.object(self.workspace, "create_project", wraps=self.workspace.create_project) as create:
            agent.assist("Crie projeto Demo", task_id=self.task["id"])
        self.assertEqual(create.call_count, 1)
        self.assertEqual(len(self.store.steps(self.task["id"])), 1)

    def test_identical_args_with_different_ids_are_distinct_intents(self):
        agent, _ = self.agent([fn(call_id="one"), fn(call_id="two"), text()])
        with patch.object(self.workspace, "create_project", wraps=self.workspace.create_project) as create:
            agent.assist("Crie projeto Demo", task_id=self.task["id"])
        self.assertEqual(create.call_count, 2)
        self.assertEqual(len(self.store.steps(self.task["id"])), 2)

    def test_persisted_completed_result_is_reused_after_new_instance(self):
        first, _ = self.agent([fn(), text()])
        first.assist("Crie projeto Demo", task_id=self.task["id"])
        second, _ = self.agent([fn(), text()])
        with patch.object(self.workspace, "create_project") as create:
            second.assist("Crie projeto Demo", task_id=self.task["id"])
        create.assert_not_called()

    def test_interrupted_intent_cannot_repeat_effect(self):
        self.store.begin_step(self.task["id"], "one", "create_project", {"name": "Demo"})
        agent, _ = self.agent([fn()])
        with patch.object(self.workspace, "create_project") as create:
            answer = agent.assist("Crie projeto Demo", task_id=self.task["id"])
        create.assert_not_called()
        self.assertIn("reconciliar", answer)
        self.assertEqual(agent.last_outcome, "needs_reconciliation")

    def test_network_retry_after_effect_stays_on_same_model(self):
        agent, models = self.agent([fn(), Unavailable(), Unavailable()])
        with patch("marvin.brain.retry_wait"):
            agent.assist("Crie projeto Demo", task_id=self.task["id"])
        self.assertEqual([c["model"] for c in models.calls], [FREE_CANDIDATES[0]] * 3)
        self.assertEqual(len(self.store.steps(self.task["id"])), 1)
        self.assertEqual(agent.last_outcome, "failed")
        self.assertEqual(models.calls[1]["contents"], models.calls[2]["contents"])

    def test_cancel_before_request_has_no_effect(self):
        agent, models = self.agent([])
        token = threading.Event()
        token.set()
        agent.assist("Crie projeto Demo", task_id=self.task["id"], cancel_event=token)
        self.assertEqual(agent.last_outcome, "cancelled")
        self.assertFalse(models.calls)
        self.assertFalse(self.store.steps(self.task["id"]))

    def test_cancel_between_calls_preserves_first_effect(self):
        both = fn()
        both.function_calls.append(types.SimpleNamespace(name="create_project", args={"name": "Other"}, id="two"))
        agent, _ = self.agent([both])
        token = threading.Event()
        original = self.workspace.create_project
        def create(name):
            value = original(name)
            token.set()
            return value
        with patch.object(self.workspace, "create_project", side_effect=create):
            agent.assist("Crie os projetos", task_id=self.task["id"], cancel_event=token)
        self.assertEqual(agent.last_outcome, "cancelled")
        self.assertEqual(len(self.store.steps(self.task["id"])), 1)
        self.assertTrue(self.workspace.project_path("Demo").exists())
        self.assertFalse(self.workspace.project_path("Other").exists())

    def test_quoted_or_negated_action_does_not_execute(self):
        for question in ['Explique o comando "crie projeto Demo"', "Não crie um projeto", "Como criar projeto Demo?"]:
            with self.subTest(question=question):
                agent, models = self.agent([fn(), text("Posso explicar.")])
                with patch.object(self.workspace, "create_project") as create:
                    agent.assist(question)
                create.assert_not_called()
                self.assertEqual(models.calls[0]["config"].tool_config.function_calling_config.mode, "AUTO")
                self.assertFalse(action_prompt(question))

    def test_action_for_app_does_not_authorize_file_writes(self):
        agent, _ = self.agent([])
        with self.assertRaises(PermissionError):
            agent.dispatch("create_project", {"name": "Unexpected"}, "Abra a calculadora")

    def test_negated_open_in_chained_request_is_enforced(self):
        agent, _ = self.agent([])
        with self.assertRaises(PermissionError):
            agent.dispatch("open_project", {"project": "Demo"}, "Crie projeto Demo mas não abra o projeto")

    def test_invalid_fields_never_reach_adapter(self):
        agent, _ = self.agent([])
        for args in [{"name": 10}, {"name": "Demo", "shell": "anything"}, {}]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                agent.dispatch("create_project", args, "Crie um projeto")

    def test_unknown_runtime_failure_is_not_reported_complete(self):
        agent, _ = self.agent([fn()])
        with patch.object(self.workspace, "create_project", side_effect=OSError("disk error")):
            agent.assist("Crie projeto Demo", task_id=self.task["id"])
        self.assertEqual(agent.last_outcome, "needs_reconciliation")
        self.assertEqual(self.store.steps(self.task["id"])[0]["state"], "needs_reconciliation")

    def test_final_text_does_not_complete_unexecuted_action(self):
        agent, _ = self.agent([text("Criei todos os arquivos")])
        agent.assist("Crie projeto Demo", task_id=self.task["id"])
        self.assertEqual(agent.last_outcome, "failed")
        self.assertFalse(self.workspace.project_path("Demo").exists())

    def test_open_request_requires_reconciliation(self):
        self.workspace.create_project("Demo")
        agent, _ = self.agent([fn("open_project", {"project": "Demo"}), text("Abertura solicitada.")])
        with patch("marvin.workspace.sys.platform", "win32"), patch("marvin.workspace.os.startfile", create=True):
            agent.assist("Abra projeto Demo", task_id=self.task["id"])
        self.assertEqual(agent.last_outcome, "needs_reconciliation")

    def test_sdk_metadata_missing_prevents_effect(self):
        response = fn()
        response.candidates = []
        agent, _ = self.agent([response])
        with patch.object(self.workspace, "create_project") as create:
            agent.assist("Crie projeto Demo")
        create.assert_not_called()


class ProviderContractTests(unittest.TestCase):
    def test_credentials_redacted(self):
        with patch.dict(os.environ, {"GEMINI_API_KEY": "secret-env-value"}):
            result = friendly_error(RuntimeError("request secret-env-value api_key=another-secret"))
        self.assertNotIn("secret-env-value", result)
        self.assertNotIn("another-secret", result)

    def test_real_installed_sdk_factory_and_schema(self):
        try:
            from google.genai import types as actual_types
        except ImportError:
            self.skipTest("Optional google-genai not installed")
        call = types.SimpleNamespace(name="verify_project", id="call-123")
        result = function_response_part(actual_types, call, {"ok": True})
        self.assertEqual(result.function_response.id, "call-123")
        self.assertEqual(len(ToolRegistry(SPEC).declarations(actual_types).function_declarations), len(SPEC))


if __name__ == "__main__":
    unittest.main()
