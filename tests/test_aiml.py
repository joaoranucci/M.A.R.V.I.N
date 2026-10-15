import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch
from urllib.error import HTTPError
from google.genai import types

from marvin.aiml import AimlClient, AimlError, ENDPOINT
from marvin.brain import Brain, friendly_error, safe_error_detail
from marvin.config import reload_gemini_config
from marvin.memory import Memory
from marvin.action_agent import function_response_part, ActionAgent, SPEC
from marvin.tool_registry import ToolRegistry
from marvin.workspace import ProjectWorkspace
from marvin.self_edit import SourceEditor
from marvin.task_store import TaskStore


class AimlTests(unittest.TestCase):
    def test_http_payload_and_authorization(self):
        response = Mock()
        response.__enter__ = Mock(return_value=response)
        response.__exit__ = Mock(return_value=False)
        response.read.return_value = json.dumps({'choices': [{'message': {'content': 'OK'}}]}).encode()
        opener = Mock()
        opener.open.return_value = response
        with patch('marvin.aiml.build_opener', return_value=opener):
            result = AimlClient('test-secret', 5000).complete([{'role': 'user', 'content': 'oi'}], 'openai/gpt-5-5')
        req = opener.open.call_args.args[0]
        self.assertEqual(req.full_url, ENDPOINT)
        self.assertEqual(req.get_header('Authorization'), 'Bearer test-secret')
        self.assertEqual(json.loads(req.data)['model'], 'openai/gpt-5-5')
        self.assertEqual(opener.open.call_args.kwargs['timeout'], 5)
        self.assertEqual(result['content'], 'OK')

    def test_tools_round_trip_preserves_call_ids(self):
        client = AimlClient('fake', 5000)
        tool = types.Tool(function_declarations=[types.FunctionDeclaration(name='list_projects', parameters=types.Schema(type='OBJECT', properties={}))])
        config = types.GenerateContentConfig(tools=[tool])
        messages = [types.Content(role='user', parts=[types.Part.from_text(text='liste projetos')])]
        with patch.object(client, 'complete', side_effect=[{'content': None, 'tool_calls': [
            {'id': 'call-one', 'function': {'name': 'list_projects', 'arguments': '{}'}}]}, {'content': 'Pronto'}]) as complete:
            reply = client.generate_content('model', messages, config)
            messages.append(reply.candidates[0].content)
            messages.append(types.Content(role='user', parts=[function_response_part(types, reply.function_calls[0], {'ok': True})]))
            client.generate_content('model', messages, config)
        sent = complete.call_args.args[0]
        self.assertEqual(sent[-2]['tool_calls'][0]['id'], 'call-one')
        self.assertEqual(sent[-1]['tool_call_id'], 'call-one')
        self.assertEqual(sent[-1]['role'], 'tool')
        self.assertEqual(complete.call_args.args[2][0]['function']['parameters']['type'], 'object')

    def test_bad_arguments_rejected_before_execution(self):
        client = AimlClient('fake', 5000)
        with patch.object(client, 'complete', return_value={'tool_calls': [{'id': 'one', 'function': {'name': 'run', 'arguments': '[]'}}]}):
            with self.assertRaises(AimlError):
                client.generate_content('model', 'oi', {})

    def test_http_errors_do_not_expose_body_or_secret(self):
        opener = Mock()
        opener.open.side_effect = HTTPError(ENDPOINT, 403, 'remote secret', {}, None)
        with patch('marvin.aiml.build_opener', return_value=opener):
            with self.assertRaises(AimlError) as caught:
                AimlClient('test-secret', 5000).complete([], 'model')
        self.assertIn('403', friendly_error(caught.exception))
        self.assertNotIn('secret', friendly_error(caught.exception))
        with patch.dict(os.environ, {'AIML_API_KEY': 'test-secret'}):
            self.assertNotIn('test-secret', safe_error_detail(Exception('test-secret')))

    def test_provider_reload_and_conversation_memory(self):
        with tempfile.TemporaryDirectory() as directory, patch.dict(os.environ, {}, clear=True):
            root = Path(directory)
            (root / '.env').write_text('MARVIN_LLM_PROVIDER=aiml\nAIML_API_KEY=fake\nAIML_MODEL=openai/gpt-5-5\n')
            reload_gemini_config(root)
            client = AimlClient('fake', 5000)
            brain = Brain(Memory(root/'mem.db'), client=client)
            with patch.object(client, 'complete', return_value={'content': 'Olá'}):
                answer, _ = brain.ask('oi')
            self.assertEqual(brain.provider, 'aiml')
            self.assertEqual(brain._models(), ['openai/gpt-5-5'])
            self.assertEqual(answer, 'Olá')
            self.assertTrue(brain.last_ask_ok)
            self.assertEqual(len(brain.memory.recent()), 2)

    def test_google_grounding_not_sent_to_aiml(self):
        client = AimlClient('fake', 5000)
        with patch.object(client, 'complete') as complete:
            with self.assertRaises(AimlError):
                client.generate_content('model', 'pesquise', types.GenerateContentConfig(tools=[types.Tool(google_search=types.GoogleSearch())]))
        complete.assert_not_called()

    def test_all_existing_tool_schemas_are_serializable(self):
        agent = ActionAgent.__new__(ActionAgent)
        agent.registry = ToolRegistry(SPEC)
        tool = agent.declarations(types)
        client = AimlClient('fake', 5000)
        with patch.object(client, 'complete', return_value={'content': 'OK'}) as complete:
            client.generate_content('model', 'oi', types.GenerateContentConfig(tools=[tool]))
        json.dumps(complete.call_args.args[2])
        self.assertGreater(len(complete.call_args.args[2]), 10)

    def test_agent_executes_and_records_aiml_tool_once(self):
        with tempfile.TemporaryDirectory() as directory, patch.dict(os.environ, {'MARVIN_LLM_PROVIDER': 'aiml', 'AIML_API_KEY': 'fake'}):
            root = Path(directory)
            memory = Memory(root/'memory.db')
            store = TaskStore(memory.db_path)
            workspace = ProjectWorkspace(root/'projects')
            client = AimlClient('fake', 5000)
            agent = ActionAgent(Brain(memory, client=client), memory, workspace, SourceEditor(root), task_store=store)
            task = store.create('Crie projeto Demo')
            with patch.object(client, 'complete', side_effect=[{'tool_calls': [
                {'id': 'create-one', 'function': {'name': 'create_project', 'arguments': '{"name":"Demo"}'}}]},
                {'content': 'Projeto criado.'}]) as complete:
                answer = agent.assist('Crie projeto Demo', task_id=task['id'])
            self.assertEqual(agent.last_outcome, 'completed')
            self.assertTrue(workspace.project_path('Demo').is_dir())
            self.assertEqual(len(store.steps(task['id'])), 1)
            self.assertEqual(complete.call_count, 2)
            self.assertIn('criado', answer)
