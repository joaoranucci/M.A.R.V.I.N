# MARVIN Mobile Gateway — contrato v1

Implementação: `marvin/gateway/api.py` · cliente: `mobile/src/features/gateway/` · testes: `tests/test_mobile_gateway.py`.

## Transporte e autenticação

- HTTPS com certificado autoassinado do PC (EC P-256). O app fixa o **SHA-256 da chave pública (SPKI)**, recebido no QR Code ou conferido pela impressão digital no pareamento manual.
- Porta padrão `8770` (`MARVIN_MOBILE_PORT`). Escuta em `0.0.0.0` por padrão (`MARVIN_MOBILE_HOST`) para alcançar a rede local/VPN; libere apenas na rede **privada** do Firewall do Windows.
- Todas as rotas, exceto `GET /v1/health` e `POST /v1/pair`, exigem `Authorization: Bearer <token do dispositivo>`.
- Erros: `{"error": {"code": "...", "message": "...", ...extras}}`. Corpo máximo 256 KB (upload: 20 MB + margem).
- Tokens e códigos ficam no servidor apenas como SHA-256. O token do Vault e chaves de IA nunca saem do PC.

## Vinculação

| Método | Rota | Corpo / resposta |
|---|---|---|
| GET | `/v1/health` | `{ok, service:"marvin-gateway", server_id, name, version, api_version, server_time}` |
| POST | `/v1/pair` | `{code, device_name, platform, app_version}` → `201 {device_id, token, server}`. Código de 6 dígitos, 5 min, uso único, 5 tentativas; 10 falhas em 10 min bloqueiam por 5 min (`429`). |
| GET | `/v1/session` | dispositivo atual |
| GET | `/v1/devices` | lista com `current` |
| DELETE | `/v1/devices/{id\|self}` | revoga (`204`) |

QR Code: `marvin://pair?v=1&h=<host>&p=<porta>&c=<código>&k=<pin SPKI base64>&n=<nome>&s=<server_id>`.

## Capacidades e estado

- `GET /v1/capabilities` — motores de conversa (`marvin`, `ollama`, com `local_model`), formatos de documento, `ocr:false`, catálogo de ações do PC, vozes do PC, transporte de eventos.
- `GET /v1/status` — `assistant` (ok/busy/unavailable), `vault` (ok/unavailable + motivo), `desktop_agent` (online/offline), `approval_pending`. Distingue **servidor indisponível** (sem resposta), **cofre fechado** e **computador/agente desconectado**.

## Eventos (long-poll)

`GET /v1/events?after=<seq>&wait=0..25` → `{events:[{seq,type,time,data}], last_seq, reset, server_time}`.
`seq` é persistido (sobrevive a reinícios). `reset:true` = cursor fora da retenção (5000) ou de outro banco → o cliente ressincroniza por REST e continua de `last_seq`.

Tipos: `assistant.task`, `assistant.progress`, `assistant.answer` (`task_id`, `text`, `state`, `origin`), `assistant.error`, `approval.requested`, `approval.resolved`, `desktop.command`, `desktop.reminder`, `document.upload`, `document.deleted`, `memory.changed`, `item.changed`, `device.paired`, `device.revoked`.

## Conversa

| Método | Rota | Notas |
|---|---|---|
| POST | `/v1/conversation/messages` | `{client_id, text, engine:"marvin"\|"ollama", source}` → `202 {task_id, state, duplicate}`. Idempotente por `client_id`; mesmo id com outro texto → `409`. |
| GET | `/v1/conversation/history?after_id=&limit=` | histórico compartilhado do Runtime (continuidade PC ↔ celular). |
| GET | `/v1/assistant/tasks[?limit]` | tarefas de IA (PC e celular, `origin`). |
| GET | `/v1/assistant/tasks/{id}?wait=0..25` | long-poll até estado final. |
| POST | `/v1/assistant/tasks/{id}/cancel` | cancela só essa tarefa (na fila: `cancelled`; em execução: `cancelling`, cooperativo). |
| GET/POST | `/v1/approvals`, `/v1/approvals/{id}` | autorizações pedidas pelo Runtime (`{accepted}`). |

Pedidos do celular **não são falados nos alto-falantes do PC** e comandos de janela (“modo compacto”) vindos do celular não alteram a tela do PC.

## Memórias (Vault)

`GET /v1/memories[?q]`, `POST /v1/memories {client_id, content, category, origin, source}` (idempotente; `200` se já existia), `PUT /v1/memories/{id} {content, category, origin, base_updated_at}` (`409 revision_conflict` com `server_item`), `DELETE /v1/memories/{id}` (idempotente).
`origin`: `user_request` | `assistant_inference` | `imported`. Registros antigos da ponte desktop (`origin: marvin-local`) aparecem como `user_request` / `source: desktop`.

## Documentos e conhecimento

| Método | Rota | Notas |
|---|---|---|
| GET | `/v1/documents` | documentos indexados (com `created_at`). |
| POST | `/v1/documents` | multipart `file`, `category`, `client_id` → `202 {upload_id, state:"received"}`. Idempotente por `client_id`. `415` formato, `413` tamanho. |
| GET | `/v1/documents/uploads[/{id}]` | `received → processing → available \| failed` (com motivo). Cofre fechado: permanece `received` e é reprocessado; falha após 1 h. |
| DELETE | `/v1/documents/{id}` | exige `X-Confirm-Delete: yes`. |
| GET | `/v1/knowledge/search?q&document_id&category&top_k` | trechos com `chunk_id`, `filename`, `part`, `excerpt`. |
| POST | `/v1/knowledge/ask` | `{question, document_id?, category?}` → `{answer, generated, model, sources[{chunk_id, filename, part, excerpt}], sources_in_document, llm_unavailable_reason}`. |
| GET | `/v1/knowledge/chunks/{chunk_id}` | texto completo da referência. |

## Itens pessoais

`GET /v1/items[?since]`, `PUT /v1/items/{uuid} {kind: task|reminder|note, title, notes, due_at, done, deleted, base_rev}` → `{status: created|updated|unchanged, item}` ou `409 revision_conflict` com `server_item`. Exclusões são marcadas (`deleted:true`).

## Ações no computador

| Método | Rota | Notas |
|---|---|---|
| GET | `/v1/desktop/actions` | catálogo com parâmetros, `requires_confirmation`, `risk`, `verifiable`, `available`. |
| POST | `/v1/desktop/commands` | `{command_id, action, params, expires_at, confirmed}` → `202` (`200` se duplicado). `410` vencido, `422` inválido, `428` exige confirmação (com `preview`), `409` id reutilizado, `503` agente offline. |
| GET | `/v1/desktop/commands[/{id}]` | estado. |
| POST | `/v1/desktop/commands/{id}/cancel` | só antes de iniciar. |
| GET | `/v1/desktop/reminders` | lembretes do PC (leitura). |

Estados: `received`, `started`, `completed` (resultado observado), `dispatched` (aceito pelo Windows, sem confirmação visual), `failed`, `expired`, `cancelled`, `rejected`, `needs_reconciliation`. Validade máxima 5 min em tempo do servidor. Ao reiniciar, nada pendente é executado (`received` → `expired`; `started` → `needs_reconciliation`).

Ações v1: `open_browser{url?}`, `web_search{query}`, `open_app{name}`, `open_folder{folder}`, `create_project_folder{name}` (somente no workspace), `list_windows`, `volume{direction}`, `lock_screen` (confirmação), `shutdown` (confirmação), `continue_task{task_id?}`.

## Voz

`GET /v1/voice/voices` · `POST /v1/voice/speech {text≤1200, voice, rate}` → `audio/wav` (Piper Faber, local) ou `audio/mpeg` (Edge, online).

## Propostas para a MARVIN Vault API (não implementadas lá)

O gateway contorna estas lacunas, mas o ideal é resolvê-las no Vault:

1. `POST /v1/knowledge/ask` com `document_id` (hoje só `category`) e `chunk_id` nas fontes.
2. Importação assíncrona com estado (`GET /v1/knowledge/imports/{id}`), em vez de bloquear a requisição.
3. Busca de registros por atributo exato (`client_id`) em vez de substring.
4. `created_at` em `GET /v1/knowledge/documents`.
5. OCR opcional para PDFs digitalizados, anunciado em `/v1/status`.
6. Escopo de token (somente leitura / memórias / documentos) para não usar um token único com acesso total.
