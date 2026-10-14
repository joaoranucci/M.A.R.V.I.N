"""AIML Chat Completions transport and adapter for the existing tool ledger."""
import json
from types import SimpleNamespace
from urllib.error import HTTPError, URLError
from urllib.request import Request, build_opener, HTTPRedirectHandler

ENDPOINT = "https://api.aimlapi.com/v1/chat/completions"


class AimlError(Exception):
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code
        self.provider = "aiml"


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def schema_json(schema):
    if hasattr(schema, 'model_dump'):
        schema = schema.model_dump(mode='json', exclude_none=True, by_alias=True)
    if isinstance(schema, dict):
        return {key: (value.lower() if key == 'type' and isinstance(value, str)
                      else schema_json(value)) for key, value in schema.items()}
    if isinstance(schema, list):
        return [schema_json(value) for value in schema]
    return schema


class AimlClient:
    def __init__(self, api_key, timeout_ms):
        self.api_key, self.timeout = api_key, timeout_ms / 1000
        self.models = self

    def close(self):
        pass

    def complete(self, messages, model, tools=None, max_tokens=2048):
        if not self.api_key:
            raise AimlError('Configure AIML_API_KEY no .env.')
        payload = {'model': model, 'messages': messages, 'max_completion_tokens': max_tokens}
        if tools:
            payload.update(tools=tools, tool_choice='auto')
        request = Request(ENDPOINT, data=json.dumps(payload).encode('utf-8'), headers={
            'Authorization': 'Bearer ' + self.api_key, 'Content-Type': 'application/json'}, method='POST')
        try:
            with build_opener(NoRedirect()).open(request, timeout=self.timeout) as response:
                raw = response.read(2_000_001)
            if len(raw) > 2_000_000:
                raise AimlError('Resposta AIML excedeu o limite de tamanho.')
            message = json.loads(raw)['choices'][0]['message']
            if not isinstance(message, dict):
                raise ValueError('invalid message')
            return message
        except HTTPError as exc:
            # Never include the remote body, request headers or credentials in logs.
            code = exc.code
            exc.close()
            labels = {401: 'Chave AIML inválida ou revogada.', 402: 'Saldo/créditos AIML insuficientes.',
                      403: 'Acesso negado pela AIML.', 404: 'Modelo ou endpoint AIML indisponível.',
                      429: 'Limite de requisições ou cota AIML atingido.'}
            raise AimlError(labels.get(code, 'Requisição AIML rejeitada.'), code) from None
        except (URLError, TimeoutError):
            raise AimlError('Falha de conexão ou timeout na AIML.') from None
        except (ValueError, KeyError, IndexError, TypeError):
            raise AimlError('Resposta AIML inválida ou sem mensagens.') from None

    def generate_content(self, model, contents, config):
        """Translate wire formats only. Tool execution remains in ActionAgent."""
        from google.genai import types
        get = lambda name, default=None: config.get(name, default) if isinstance(config, dict) else getattr(config, name, default)
        messages = []
        if get('system_instruction'):
            messages.append({'role': 'system', 'content': get('system_instruction')})
        if isinstance(contents, str):
            messages.append({'role': 'user', 'content': contents})
        else:
            for content in contents:
                text, calls, results = [], [], []
                for part in content.parts or []:
                    if part.text:
                        text.append(part.text)
                    if part.function_call:
                        call = part.function_call
                        calls.append({'id': call.id, 'type': 'function', 'function': {
                            'name': call.name, 'arguments': json.dumps(call.args or {})}})
                    if part.function_response:
                        result = part.function_response
                        results.append({'role': 'tool', 'tool_call_id': result.id,
                                        'content': json.dumps(result.response, ensure_ascii=False)})
                if text or calls:
                    message = {'role': 'assistant' if content.role == 'model' else 'user',
                               'content': '\n'.join(text) or None}
                    if calls:
                        message['tool_calls'] = calls
                    messages.append(message)
                messages.extend(results)
        tools = []
        for tool in get('tools', []) or []:
            if getattr(tool, 'google_search', None) is not None:
                raise AimlError('Pesquisa Google grounding exige Gemini; selecione Brave ou SearXNG para AIML.')
            for function in tool.function_declarations or []:
                tools.append({'type': 'function', 'function': {
                    'name': function.name, 'description': function.description or '',
                    'parameters': schema_json(function.parameters_json_schema or function.parameters)
                                  or {'type': 'object', 'properties': {}}}})
        message = self.complete(messages, model, tools, get('max_output_tokens') or 2048)
        text = message.get('content') or ''
        if not isinstance(text, str):
            raise AimlError('Formato de texto AIML não suportado.')
        parts, calls, ids = [], [], set()
        if text:
            parts.append(types.Part.from_text(text=text))
        for item in message.get('tool_calls') or []:
            try:
                call_id, function = item['id'], item['function']
                args = json.loads(function['arguments'])
                if not isinstance(args, dict) or not isinstance(call_id, str) or not call_id or call_id in ids:
                    raise ValueError('invalid tool call')
                call = types.FunctionCall(id=call_id, name=function['name'], args=args)
            except (KeyError, TypeError, ValueError):
                raise AimlError('Chamada de ferramenta AIML inválida; nenhuma ação executada.') from None
            ids.add(call_id)
            calls.append(call)
            parts.append(types.Part(function_call=call))
        if not text.strip() and not calls:
            raise AimlError('AIML retornou uma resposta vazia.')
        return SimpleNamespace(text=text, function_calls=calls, candidates=[
            SimpleNamespace(content=types.Content(role='model', parts=parts))])
