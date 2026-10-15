"""Ponte para o adaptador Tk atual, antes da criacao de tarefas do Runtime.

Usa o protocolo real do app.py enviado: pending, TaskControl, set_busy,
worker e post. Chamadas de cofre nao passam por Runtime.prepare/run nem TTS.
"""
from __future__ import annotations

from .vault_bridge import detect_command, execute_command


def route_vault(app, question, task_id=None) -> bool:
    from .runtime import TaskControl, request_text

    text = request_text(question)
    serialized = detect_command(text)
    if serialized is None:
        return False
    app.interrupted_listening = False
    if app.busy:
        if len(app.pending) >= 8:
            app.append("status", "A fila ja tem 8 pedidos. Aguarde ou cancele.")
        else:
            # Somente em RAM. Nao gravar o conteudo privado na tabela antiga de tarefas.
            app.pending.append((question, task_id))
            app.append("status", "Consulta ao cofre colocada na fila.")
        return True

    app.token = TaskControl()
    token = app.token
    app.set_busy()
    app.append("you", text)

    def worker():
        try:
            if token.is_set():
                return
            answer = execute_command(serialized)
            if token.is_set():
                app.post("note", "Operacao do cofre encerrada apos o cancelamento. "
                         "Uma gravacao ja iniciada pode ter concluido; consulte a memoria antes de repetir.")
            else:
                # O poll_ui atual recebe texto, nao a tupla usada pela interface antiga.
                app.post("reply", answer)
        except Exception:
            # Nao registrar documentos ou detalhes de tokens em logs da interface.
            app.post("note", "Falha na consulta ao cofre local. Execute DIAGNOSTICO_API.bat na pasta da API.")
        finally:
            app.post("finish")

    try:
        app.worker(worker, name="MARVIN-vault")
    except Exception:
        app.post("note", "Nao foi possivel iniciar a consulta ao cofre.")
        app.post("finish")
    return True
