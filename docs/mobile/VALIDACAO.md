# MARVIN Mobile v0.1 — validação (15/10/2026)

Ambiente: Windows 11, Node 24.15, JDK 17, Expo SDK 57 / RN 0.86. APK release (`mobile/dist/MARVIN-Mobile-0.1.0-preview.apk`, arm64-v8a + x86_64, ~107 MB) instalado num emulador Android 16 (API 36, Google APIs). Gateway em pasta de dados temporária, cofre temporário com o **código real** da MARVIN Vault v0.3 (porta 8799). Seu cofre real, `.env` e chaves de IA não foram usados.

## Automatizado

| Suíte | Resultado |
|---|---|
| `tests/test_mobile_gateway.py` (pareamento, eventos, conversa idempotente, cancelamento, comandos, memórias, documentos, itens, limites) | 20/20 ok |
| Suíte completa do MARVIN | 222/226 ok; as 4 falhas são de `test_app_v070` e já existiam com a alteração não commitada em `marvin/app.py` (ponte do Vault) — o mesmo teste passa no HEAD |
| Adaptador do Vault contra o código real v0.3 | ok (origem, idempotência, conflito, duplicado, PDF inválido, busca por documento, trecho, `/ask` sem modelo) |
| `npm test` (intenções pt-BR, datas, eco, QR, impressão digital) | 10/10 ok |
| `npx tsc --noEmit` / bundle Metro | ok |

## No emulador (APK sem servidor de desenvolvimento)

| Fluxo | Resultado |
|---|---|
| Abrir app, vincular por código + impressão digital (módulo nativo lê o certificado) | ok; TLS fixado funciona no `fetch` |
| Permissão de microfone negada → mensagem + “Digitar”; permitida → estado “ouvindo” com Cancelar/Concluir | ok (após corrigir conflito de foco de áudio com o reconhecedor) |
| Silêncio → “Não ouvi nada” | ok |
| Texto → PC → resposta por eventos → fala (voz do PC) → interromper em < 0,6 s | ok |
| “lembre que…” → memória `user_request` sincronizada no cofre | ok |
| Criar pasta no PC → `completed` verificado; repetir → “já existia” | ok |
| Ação destrutiva → prévia âmbar → recusada, nada enviado | ok |
| Gateway parado → “Servidor MARVIN indisponível”; memória salva localmente; voz cai para a do aparelho | ok |
| Comando offline enfileirado → executado uma vez ao reconectar dentro da validade | ok |
| Comando enfileirado vencido (> 5 min) → não executado, “Precisa de nova decisão” | ok |
| Compartilhar arquivo pelo app Arquivos → MARVIN → `received → processing → available` → pergunta → referência | ok (corrigido upload multipart para o `fetch` do Expo) |
| Instrução embutida em documento | exibida como texto, nada executado |
| Histórico do PC aparece no celular com selo “no PC” | ok |
| Modo demonstração identificado; “desligar” apenas simulado | ok |
| Fechar à força e reabrir: vínculo, histórico e memórias persistem | ok |
| Revogação pelo PC → “Acesso revogado” | ok |

## Não validado / pendente

- Reconhecimento de fala com voz real (o microfone do emulador é silencioso) — **testar em aparelho físico**.
- Leitura do QR Code pela câmera — testar em aparelho; o atalho `marvin://pair?...` abre a tela mas o cartão de confirmação ainda não aparece (corrigir).
- Escuta por “Marvin”: o emulador não tem o pacote offline pt-BR; o app desativa e explica. Testar em aparelho com o pacote (botão de download adicionado).
- Chamadas telefônicas e desconexão de fones: código nativo pronto, não exercitado.
- Notificações de lembrete reais, iOS, wearables físicos, escuta em segundo plano: fora desta etapa.
- Conversa livre com LLM: depende da chave configurada no `.env` do PC (não usada no teste).
