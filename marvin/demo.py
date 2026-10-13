"""Scripted engineering demonstration with REAL files/tests, no LLM or desktop automation."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import uuid

from .config import ROOT
from .memory import Memory
from .task_store import TaskStore
from .workspace import ProjectWorkspace


def demonstrate(directory: Path):
    directory = Path(directory).resolve()
    memory = Memory(directory / "demo.db")
    tasks = TaskStore(memory.db_path)
    workspace = ProjectWorkspace(directory / "projects")
    project = "saudacao-" + datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + "-" + uuid.uuid4().hex[:4]
    first = tasks.create("Demonstração: criar projeto com um defeito conhecido e reproduzir pelo teste.", scope={"workspace": str(workspace.root)})
    tasks.set_state(first["id"], "running")
    def record(task, step, tool, args, fn):
        entry = tasks.begin_step(task["id"], step, tool, args)
        if not entry["created"]:
            raise RuntimeError("Demonstração não repete efeitos existentes.")
        result = fn()
        tasks.finish_step(task["id"], step, result)
        return result
    record(first, "create", "create_project", {"name": project}, lambda: workspace.create_project(project))
    source = 'def saudacao(nome):\n    return "Ola, " + nome + "."\n'
    test = ('import unittest\nfrom app import saudacao\n\nclass SaudacaoTests(unittest.TestCase):\n'
            '    def test_nome_e_pontuacao(self):\n        self.assertEqual(saudacao("Joao"), "Ola, Joao!")\n')
    for name, content in (("app.py", source), ("tests/__init__.py", ""), ("tests/test_app.py", test)):
        record(first, "write:"+name, "write_project_file", {"project": project, "path": name},
               lambda name=name, content=content: workspace.write_project_file(project, name, content))
    before = record(first, "test", "run_project_check", {"project": project, "check": "python-tests"},
        lambda: workspace.run_project_check(project, approve_execution=lambda details: True))
    tasks.set_state(first["id"], "failed", "Falha esperada reproduzida pelo teste real.")
    if before["ok"] or before.get("exit_code") != 1:
        raise RuntimeError("O teste inicial não reproduziu a falha esperada: " + json.dumps(before))
    repair = tasks.create("Demonstração: corrigir pontuação, verificar e preservar continuidade.", scope={"workspace": str(workspace.root)})
    tasks.set_state(repair["id"], "running")
    read = record(repair, "read", "read_project_file", {"project": project, "path": "app.py"},
                  lambda: dict(workspace.read_project_file(project, "app.py"), ok=True))
    record(repair, "patch", "patch_project_file", {"project": project, "path": "app.py", "expected_sha256": read["sha256"]},
           lambda: workspace.patch_project_file(project, "app.py", '+ "."', '+ "!"', read["sha256"], approve_overwrite=lambda path: True))
    static = record(repair, "verify", "verify_project", {"project": project}, lambda: workspace.verify_project(project))
    after = record(repair, "test", "run_project_check", {"project": project, "check": "python-tests"},
        lambda: workspace.run_project_check(project, approve_execution=lambda details: True))
    if not static["ok"] or not after["ok"]:
        tasks.set_state(repair["id"], "failed", "Verificação não passou.")
        raise RuntimeError("Correção não confirmada: " + json.dumps(after))
    memory.set_context({"project": project, "file": "app.py", "last_task_id": repair["id"]})
    memory.add_pair("Corrija o projeto de saudação", "Corrigido: teste real passou.")
    tasks.set_state(repair["id"], "completed", "Patch aplicado e teste real passou.")
    return {"scripted_demo": True, "llm_used": False, "physical_devices_used": False,
            "directory": str(workspace.project_path(project)), "database": str(memory.db_path),
            "baseline_task": first["id"], "repair_task": repair["id"], "before_exit_code": before["exit_code"],
            "after_exit_code": after["exit_code"], "tests": after["evidence"], "test_output": after["stderr"],
            "context_after_restart": Memory(memory.db_path).get_context(),
            "result": "Código e testes reais. Sequência pré-programada; não mede compreensão de linguagem pelo modelo."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", type=Path, default=ROOT/"data"/"engineering_demo")
    args = parser.parse_args()
    print(json.dumps(demonstrate(args.directory), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
