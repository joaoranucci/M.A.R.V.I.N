"""Validated tool contracts shared by model declarations and local dispatch.

The registry contains no shell escape hatch. Results preserve legacy fields while
adding a stable execution envelope for checkpoints and diagnostics.
"""
from __future__ import annotations

from dataclasses import dataclass
import json
import re
import unicodedata


def normalized(text: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", text.lower())
                   if not unicodedata.combining(c))


def intent_text(question: str) -> str:
    # Quoted commands and code are data, never independent authorization.
    text = re.sub(r"```[\s\S]*?```|`[^`]*`|\"[^\"]*\"|'[^']*'|“[^”]*”", " ", question)
    return normalized(text)


def authorized_intent(question: str, verbs: str) -> bool:
    text = intent_text(question)
    # Discussion, questions about commands, and hypothetical examples are not orders.
    if re.match(r"\s*(?:marvin[, ]+)?(?:explique|explica|como|o que|qual|descreva|traduza|resuma|imagine|exemplo|se eu)\b", text):
        return False
    for clause in re.split(r"[.;!?\n]|\b(?:mas|depois|entao|e)\b", text):
        if re.search(r"\b(nao|nunca|jamais|sem|evite|proibido)\b", clause):
            continue
        if re.search(r"\b(?:" + verbs + r")\b", clause):
            return True
    return False


ACTION_VERBS = ("crie|criar|cria|monte|montar|construa|construir|faca|fazer|salve|salvar|"
                "escreva|escrever|abra|abre|abrir|altere|alterar|corrija|corrigir|modifique|"
                "modificar|atualize|guarde|lembre|memorize|anote|mude|melhore|edite|"
                "execute|executar|rode|rodar|teste|testar|continue|continuar")


@dataclass(frozen=True)
class ToolContract:
    name: str
    description: str
    parameters: dict
    effect: str = "read"
    scope: str = "managed_projects"
    capabilities: tuple[str, ...] = ("filesystem",)
    timeout_seconds: int = 10
    repeat_policy: str = "recorded_result_only"
    verifier: str = "adapter_result"

    @property
    def result_schema(self):
        return {"type": "object", "required": ["ok", "status", "data", "message", "evidence",
                                                "changed_resources", "duration_ms", "retryable"]}

    def validate(self, args: dict):
        if not isinstance(args, dict):
            raise ValueError("Argumentos da ferramenta devem ser um objeto.")
        fields = self.parameters["properties"]
        extras = set(args) - set(fields)
        missing = set(self.parameters.get("required", ())) - set(args)
        if missing or extras:
            raise ValueError(f"Argumentos inválidos em {self.name}: ausentes={sorted(missing)}, extras={sorted(extras)}.")
        for key, value in args.items():
            field = fields[key]
            kind = field["type"]
            valid = ((kind == "string" and isinstance(value, str))
                     or (kind == "boolean" and type(value) is bool)
                     or (kind == "object" and isinstance(value, dict)))
            if not valid:
                raise ValueError(f"{key} deve ter tipo {kind}.")
            if kind == "object" and not all(isinstance(k, str) and isinstance(v, str) for k, v in value.items()):
                raise ValueError(f"{key} aceita somente caminhos e conteúdos em texto.")
            if kind == "string" and key not in ("content", "old", "new", "path") and not value.strip():
                raise ValueError(f"{key} não pode ser vazio.")
            if "enum" in field and value not in field["enum"]:
                raise ValueError(f"Valor inválido para {key}.")
        if len(json.dumps(args, ensure_ascii=False).encode("utf-8")) > 2_000_000:
            raise ValueError("Argumentos excedem o limite de 2 MB.")


class ToolRegistry:
    def __init__(self, specs: dict):
        self.contracts = {}
        for name, (description, fields, required) in specs.items():
            properties = {}
            for key, value in fields.items():
                properties[key] = ({"type": "boolean", "description": "Confirma solicitação de sobrescrita"}
                    if isinstance(value, bool) else value if isinstance(value, dict)
                    else {"type": "string", "description": value})
            effect = ("write" if name in {"create_project", "write_project_file", "patch_project_file", "remember_fact", "propose_self_edit", "propose_changes"}
                      else "execute" if name in {"open_project", "launch_app", "run_project_check"} else "read")
            scope = ("public_url" if name == "read_web_page" else "memory" if name in {"remember_fact", "recall_facts"} else "source_proposals"
                     if name in {"read_marvin_code", "propose_self_edit", "propose_changes"} else
                     "desktop_catalog" if name == "launch_app" else "managed_projects")
            capabilities = (scope,)
            self.contracts[name] = ToolContract(name, description,
                {"type": "object", "properties": properties, "required": required, "additionalProperties": False},
                effect, scope, capabilities, 60 if name == "run_project_check" else 15 if name == "read_web_page" else 10)

    def get(self, name):
        if name not in self.contracts:
            raise PermissionError("Ferramenta não autorizada.")
        return self.contracts[name]

    def validate(self, name, args, question):
        contract = self.get(name)
        contract.validate(args)
        if contract.effect != "read" and not authorized_intent(question, ACTION_VERBS):
            raise PermissionError("O pedido atual não autoriza esta ação; texto citado ou explicativo não é uma ordem.")
        # An unrelated action in another clause cannot grant this tool's effect.
        denied_verbs = {"open_project": "abr|abra|abre|abrir", "launch_app": "abra|abre|abrir|inicie|iniciar",
                        "remember_fact": "lembre|lembrar|guarde|guardar|salve|memorize|anote",
                        "run_project_check": "execute|executar|rode|rodar|teste|testar|verifique|verificar"}
        verb_set = denied_verbs.get(name)
        text = intent_text(question)
        if verb_set and re.search(r"\b(?:nao|nunca|jamais|sem)\s+(?:\w+\s+){0,2}(?:" + verb_set + r")\b", text):
            raise PermissionError("O pedido proíbe explicitamente esta ação.")
        if name == "launch_app" and not authorized_intent(question, "abra|abre|abrir|inicie|iniciar|execute"):
            raise PermissionError("Abrir outro aplicativo exige um pedido de abertura.")
        if name in {"create_project", "write_project_file", "patch_project_file"} and not authorized_intent(question,
                "crie|criar|cria|monte|montar|construa|construir|faca|fazer|salve|salvar|escreva|escrever|"
                "altere|alterar|corrija|corrigir|modifique|modificar|atualize|mude|melhore|edite|continue|continuar"):
            raise PermissionError("O pedido não autoriza criar ou alterar arquivos.")
        return contract

    def declarations(self, types):
        return types.Tool(function_declarations=[types.FunctionDeclaration(name=c.name,
            description=c.description, parameters_json_schema=c.parameters) for c in self.contracts.values()])

    @staticmethod
    def result(raw, *, duration_ms=0, error_code=None, message="", uncertain=False):
        raw = raw if isinstance(raw, dict) else {"result": raw}
        ok = raw.get("ok", "error" not in raw and not error_code) is True and not uncertain
        result = dict(raw)
        result.update(ok=ok, status="needs_reconciliation" if uncertain else raw.get("status", "completed" if ok else "failed"),
                      data=raw, error_code=error_code or raw.get("error_code"),
                      message=message or raw.get("message", ""), evidence=raw.get("evidence", []),
                      changed_resources=raw.get("changed_resources", []), duration_ms=round(duration_ms, 2),
                      retryable=False)
        return result
