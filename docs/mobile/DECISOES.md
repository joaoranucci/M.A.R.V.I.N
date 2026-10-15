# MARVIN Mobile — registro de decisões (v0.1)

Data: 15/10/2026. Cada decisão registra o motivo e o que precisa ser revisto.

## Contexto inspecionado

| Componente | Local | Contrato real encontrado |
|---|---|---|
| MARVIN Windows (Presença v0.8) | `C:\M.A.R.V.I.N` | `Presence` + `Runtime` + `TaskStore` (SQLite). API FastAPI **somente 127.0.0.1**, autenticada por cookie de sessão por execução. Sem vinculação de dispositivos, sem acesso pela rede. |
| MARVIN Vault API v0.3 | `C:\API Marvin` | FastAPI **somente 127.0.0.1:8765**, um único token Bearer (`api-token.txt`). Memórias (`/v1/entries`), documentos (`/v1/knowledge/*`), RAG via Ollama. Importação **síncrona**, sem OCR, sem filtro por documento em `/ask`, sem eventos. |
| Ollama | `127.0.0.1:11434` | Neste PC só existe `glm-5.3:cloud` — modelo **remoto** (ollama.com), não local. |

Nenhuma das APIs pode ser acessada pelo celular sem mudanças: escutam só em loopback, não têm TLS, não têm credencial por dispositivo nem revogação.

## D1 — Gateway Mobile no PC em vez de expor as APIs existentes

Criado `marvin/gateway` (Python/FastAPI, mesmo ambiente do MARVIN). Ele é a **única** superfície exposta à rede local/VPN e:

- roda dentro do processo da Presença (mesmo `Runtime`, fila e autorizações) ou sozinho (`python -m marvin.gateway serve`, sem janela e sem áudio no PC);
- encaminha memórias e documentos ao Vault pelo loopback, usando o token do Vault **que nunca sai do PC**;
- registra comandos do computador com ID, validade, deduplicação e estados;
- publica eventos com sequência persistida (long-poll com cursor).

Motivo: não alterar a API do Vault (projeto separado), manter chaves de provedores e o token do Vault no servidor e ter um ponto único de autenticação. O adaptador do Vault fica isolado em `marvin/gateway/vault.py`; o do app, em `mobile/src/features/gateway`.

## D2 — TLS com certificado autoassinado fixado (pinning) no pareamento

O gateway gera chave EC P-256 + certificado no primeiro uso. O QR Code de pareamento leva o hash SHA-256 da chave pública (SPKI). O app Android instala uma fábrica OkHttp (módulo nativo local `marvin-native`) que aceita **apenas** esse certificado para o gateway e mantém a validação normal do sistema para os demais hosts. Pareamento manual mostra a impressão digital para comparação com a do PC.

Sem TLS não há conexão em build de produção (`cleartext` desativado). VPN (WireGuard/Tailscale) é opcional e soma uma camada; não substitui o TLS.

## D3 — Vinculação por código temporário/QR e token por dispositivo

Código de 6 dígitos válido por 5 minutos, uso único, 5 tentativas. O token do dispositivo (256 bits) é guardado no `SecureStore` (Android Keystore) e no servidor só como hash. Revogação pelo app, pelo PC (`MARVIN_CELULAR.bat devices/revoke`) ou ao encerrar a sessão.

## D4 — Transporte de eventos: long-poll HTTP com cursor

WebSocket do React Native usa um cliente OkHttp próprio que não passa pela fábrica com pinning. Long-poll (`GET /v1/events?after=SEQ&wait=25`) funciona com o pinning, reconecta sem estado, e a sequência persistida evita duplicidade e detecta lacunas (`reset`).

Verificado no código: no SDK 57 o `fetch` global é o `expo/fetch`, cujo módulo nativo cria o cliente com `OkHttpClientProvider.createClient()` — portanto passa pela fábrica com o certificado fixado. Uploads multipart usam `File` do `expo-file-system` (o formato `{uri, name, type}` do RN não é aceito por esse `fetch`).

## D5 — Stack do app

| Necessidade | Escolha | Motivo |
|---|---|---|
| Base | Expo SDK 57 (RN 0.86, React 19.2, Nova Arquitetura), development build | SDK estável mais recente em 15/10/2026; módulos nativos via `expo prebuild`. |
| Navegação | `expo-router` (abas + pilha) | Padrão do SDK, deep link `marvin://`. |
| Dados locais | `expo-sqlite` | Migrações versionadas, funciona offline. |
| Credenciais | `expo-secure-store` | Keystore no Android, Keychain no iOS. |
| Fala → texto | `expo-speech-recognition` 57.x | `SpeechRecognizer` do Android, pt-BR, eventos de volume, opção de reconhecimento no aparelho. |
| Texto → fala | `expo-speech` (vozes do aparelho) + voz do PC (Piper Faber local / Edge Antônio online) tocada com `expo-audio` | Voz masculina natural disponível mesmo quando o TTS do aparelho não tem uma. |
| Núcleo animado | `@shopify/react-native-skia` + Reanimated | Desenho na GPU, animação na thread de UI, amplitude real do microfone/áudio. |
| Validação | `zod` | Toda resposta do servidor é validada antes de uso. |
| Estado | `zustand` | Pequeno, sem boilerplate. |
| Câmera/QR | `expo-camera` | Leitura de QR integrada. |
| Arquivos | `expo-document-picker` + `expo-file-system`; compartilhamento Android via intent-filter no módulo local | Sem permissão de armazenamento (SAF). |
| Notificações | `expo-notifications` (locais) | Lembretes offline; sem push/servidor pago. |
| Rede | `expo-network` | Distinguir sem rede / servidor fora / PC desconectado. |

Sem serviços pagos obrigatórios: reconhecimento usa o serviço do Android; conversa usa o provedor já configurado no PC.

## D6 — Voz half-duplex e proteção contra eco

O microfone nunca fica aberto enquanto o MARVIN fala. Depois da fala há um intervalo de guarda, e transcrições muito parecidas com a última fala do MARVIN são descartadas. Interrupção imediata por botão; foco de áudio, chamadas e desconexão de fones interrompem fala e escuta (módulo nativo).

## D7 — Palavra de ativação em etapa separada

1. Toque no núcleo (de ponta a ponta) — implementado.
2. “Marvin” com o app aberto e em primeiro plano, com indicador de microfone sempre visível e desativação em um toque — implementado como **experimental** (depende do reconhecimento contínuo do Android 13+).
3. Segundo plano (serviço em primeiro plano com notificação, Vosk local) — **ponto de extensão documentado**, não implementado. Sem promessa para app encerrado nem para iOS.

## D8 — Memória com origem explícita

Memórias têm `origin` (`user_request`, `assistant_inference`, `imported`), `source` (`mobile-voice`, `mobile-text`, `desktop`, `vault`), datas e `sync_state`. A fonte canônica é o Vault (criptografado). O histórico de conversa fica em tabela própria, com retenção configurável, e **não** vira memória automaticamente.

## D9 — Documentos: estados reais

O Vault indexa de forma síncrona. O gateway recebe o arquivo, responde `received`, processa em segundo plano (`processing`) e só então informa `available` (com trechos) ou `failed` (motivo). Formatos aceitos vêm do servidor; OCR é anunciado como indisponível.

## D10 — Ações no computador por comandos estruturados

`command_id` gerado no celular (deduplicação), validade de até 5 minutos em tempo do servidor, parâmetros validados por ação, estados `received → started → completed/failed/needs_reconciliation`, além de `expired`, `cancelled` e `rejected`. Ações destrutivas (bloquear, desligar) exigem prévia e decisão. Comandos vencidos na fila offline nunca são enviados sem nova decisão.

## D11 — Provedores de IA

Interface `AssistantProvider` no app: `gateway` (runtime do PC com o provedor configurado lá), `local` (regras determinísticas, sem LLM: memórias, tarefas, notas) e `demo` (explicitamente marcado). No servidor, motores `marvin` (Runtime/Brain) e `ollama` (se houver modelo; local ou remoto é informado). Não há modelo no celular nesta versão.

## D12 — Wearables

Camada `features/devices/wearables` com transporte de comandos separado do de áudio e eventos tipados (acionamento, conexão, bateria). Simulador só em modo demonstração. Perfis BLE/áudio a definir com o hardware em `docs/mobile/WEARABLES.md`.
