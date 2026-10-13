# Arquitetura v0.7

`main.py → app.MarvinApp → runtime.Runtime → comandos locais / ActionAgent → ToolRegistry → adaptadores`.

`Memory`, `TaskStore` e `Scheduler` usam SQLite com conexões por operação. `Runtime` não importa Tkinter nem drivers de áudio. A interface envia pedidos e recebe eventos por uma fila limitada. O controle de desktop é serializado; pesquisas/leituras ainda passam pelo executor serial nesta versão.

## Componentes

| Módulo | Responsabilidade |
| --- | --- |
| app.py | Widgets, autorizações, fila de pedidos, eventos e controles |
| runtime.py | Ciclo de tarefa, pausa/cancelamento, caminhos locais e referências |
| action_agent.py / brain.py | Protocolo Gemini, ferramentas, retries limitados e contexto |
| tool_registry.py | Schemas, efeitos, escopos fixos e autorização por intenção |
| workspace.py / process_runner.py | Arquivos, hashes, verificações e processos aprovados |
| task_store.py | Tarefas, ledger e recuperação de interrupções |
| memory.py / scheduler.py | Migração, memória, contexto e lembretes com leases |
| voice.py | Microfone exclusivo, Vosk, Piper/Edge e reprodução cancelável |
| visual_agent.py / runner.mjs | Ponte visual opcional, processo limitado e cancelável |
| self_edit.py | Propostas multiarquivo, revisão, aplicação e recuperação |
| health.py / telemetry.py | Capacidades e logs limitados sem conteúdo de usuário |
| web_reader.py | HTTP público de URL explícita, sem cookies nem JavaScript |
| device_link.py | Simulador local, independente do núcleo/UI |

## Estado e confirmação

Estados: queued, running, waiting_user, paused, completed, failed, cancelled e needs_reconciliation. O identificador estável da etapa permite reutilizar resultados e rejeitar repetição incerta. Gravar resultado, serializar resposta e pedir continuação ao modelo são operações separadas.

O ledger não garante exatamente uma execução em serviços externos. Se ocorrer queda entre efeito e registro, a etapa fica incerta. Abertura de app/arquivo também fica pendente de observação, pois aceitação pelo Windows não comprova a janela desejada.

Nesta versão, uma falha histórica não é apagada por uma mensagem final do modelo: a tarefa permanece falha/conservadora. A continuação após reinício mostra resultados e solicita o próximo passo; não reproduz automaticamente o objetivo anterior inteiro. Planejamento complexo ainda é realizado pelo modelo dentro do laço de ferramentas, sem editor persistente de DAG/plano.

## Decisões

- Evolução incremental; Tkinter e SQLite mantidos.
- Um processo e um executor de desktop. Lock do diretório de dados impede duas instâncias padrão concorrentes.
- Esquema legado de mensagens/fatos preservado; tabelas complementares e versão por componente.
- Sem nova infraestrutura distribuída, banco vetorial, serviço pago ou modelo local pesado.
- Autorização de execução apresenta comando concreto; execução não é isolamento de sistema.
- Núcleo de voz permanece half duplex. A interrupção confiável por botão vem antes de prometer cancelamento acústico de eco.
- O transporte vestível é simulado. Sessões e limites podem ser exercitados sem alegar validação Bluetooth.
