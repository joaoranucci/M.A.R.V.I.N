# Validação iOS — MARVIN Mobile

Data: 15/10/2026. Cada resultado abaixo tem escopo próprio. Código TypeScript aprovado não significa compatibilidade física validada.

## Evidência disponível

A [CI Mobile](https://github.com/joaoranucci/M.A.R.V.I.N/actions/workflows/mobile.yml) contém jobs separados para JS, Gateway, Kotlin, Swift, aplicação iOS e UI. O job de UI depende da compilação real da aplicação e usa o artefato desse mesmo run.

| Verificação | Resultado durante a preparação | Limite |
| --- | --- | --- |
| Instalação limpa npm ci | Passou após correção do lockfile | Não testa uma execução nativa |
| Lint e typecheck | Passaram | Verificação estática |
| Testes JS/contratos puros | 18 testes na base; conferência final em andamento | NLP, URL/TLS policy, QR/link e CNG |
| Gateway Python | 25 testes passaram; teste adicional de SAN explícito incluído | Integração em processo, sem iPhone/Windows real |
| Kotlin | Módulo nativo compilado no Linux/Android SDK | Não foi executado em Android físico |
| Swift certificate/URLSession | 10 XCTest passaram no macOS, Xcode 26.6, Swift 6.3.3 | Testes de rede nativa no Mac; não são testes no iOS Simulator |
| CNG iOS, pods e configuração | Preparação/compilação em andamento | Verificar run final antes da distribuição |
| Aplicação iOS completa | Em andamento | Sem assinatura Apple |
| UI no simulador | Fluxo preparado; depende do artefato compilado | Não cobre microfone/câmera/chamadas reais |
| iPhone físico | Não executado | Aparelho/UDID/provisionamento não fornecidos |
| IPA/TestFlight | Não gerados/enviados | Conta/projeto EAS e assinatura Apple pendentes |

O registro final desta seção será atualizado com o run concluído antes da entrega.

## O que os testes nativos cobrem

Os fontes de certificado e URLSession são os mesmos usados pelo pod do app. Os testes SwiftPM sobem servidores HTTPS efêmeros com certificados EC/RSA e conferem:

- SPKI idêntico ao produzido pelo Gateway Python.
- Certificado/pin correto; datas vencidas/futuras e SAN/host errado recusados.
- Pin errado impede qualquer requisição HTTP e cabeçalho de autorização.
- Inspeção manual não envia HTTP.
- Redirecionamentos sem encaminhamento.
- Áudio binário sem alteração de bytes.
- Multipart e recusa de arquivo fora do sandbox.
- Long polling e cancelamento antes/durante a operação.

Os testes Python cobrem conversa/eventos, memórias e conflitos, documentos/estados/referências, tarefas/revisões, comandos e confirmações, tokens independentes Android/iOS e renovação do certificado sem mudar a chave/pin.

A CI compila o aplicativo real por CNG/CocoaPods/Xcode. Compilar para o destino genérico de simulador, sozinho, não prova que o simulador foi iniciado. O job separado de UI instala a aplicação e executa o fluxo Maestro.

## Aceitação ainda necessária em iPhone físico

1. Parear por QR, manual e link com app encerrado/aberto; conferir impressão digital; trocar servidor sem aprovação automática.
2. Rejeitar pin, certificado vencido e endereço fora do SAN. Validar renovação do Gateway mantendo chave/tokens. Revogar apenas o iPhone e confirmar Android intacto.
3. Recusar microfone, reconhecimento, câmera, rede local e notificações; verificar orientação para Ajustes e alternativa Digitar.
4. Transcrever português com e sem conexão. Testar escolha local sem modelo e sem fallback online implícito.
5. Testar vozes pt-BR do sistema/PC, velocidade, volume, modo silencioso e interrupção pelo núcleo.
6. Receber ligação/interrupção de outro app, conectar/desconectar fones com fio/Bluetooth e trocar alto-falante/auricular/AirPlay. A captura não deve reabrir sozinha.
7. Validar núcleo animado/redução de movimento, orientação suportada, Dynamic Type, áreas seguras, abas e teclado sem campo de texto fixo.
8. Importar do Arquivos e iCloud Drive; cancelar picker; arquivo vazio, formato incompatível, até 20 MiB/acima do limite, perda de conexão e retomada idempotente da outbox.
9. Fazer conversa, memória, pesquisa/biblioteca, tarefas/notificações e comandos reais pelo mesmo Gateway; verificar confirmações e reconciliação de ações incertas.
10. Bloquear/desbloquear, fechar/reabrir e atualizar o app. Preservar histórico, filas, preferências, pareamento e token no Keychain.
11. Instalar a prévia em aparelho provisionado e depois pelo TestFlight. Não usar uma build de simulador como comprovação de instalação física.

A Share Extension de entrada tem avaliação própria no [guia iOS](IOS.md); não está instalada nem validada.

## Requisitos pendentes da distribuição

- Vincular o project ID real à conta Expo/EAS.
- Apple Developer Program/equipe com acesso ao bundle identifier e aos certificados/perfis.
- iPhone cadastrado por UDID para desenvolvimento/prévia física.
- App do App Store Connect e acesso para a submissão TestFlight.

Nenhuma assinatura ou credencial foi substituída por valores fictícios. Siga o [guia de instalação](IOS.md).
