# Validação iOS — MARVIN Mobile

Data: 16/10/2026. Cada resultado abaixo tem escopo próprio. Código TypeScript aprovado não significa compatibilidade física validada.

## Evidência disponível

A [CI Mobile](https://github.com/joaoranucci/M.A.R.V.I.N/actions/workflows/mobile.yml) contém jobs separados para JS, Gateway, Kotlin, Swift, aplicação iOS e UI. A CI chama o workflow de UI com o artefato da própria compilação. A execução manual também pode reutilizar uma build de push: antes de instalar, confere que os fontes do aplicativo correspondem ao artefato.

| Verificação | Resultado registrado | Limite |
| --- | --- | --- |
| Instalação limpa npm ci | Passou após correção do lockfile | Não testa uma execução nativa |
| Lint e typecheck | Passaram | Verificação estática |
| Testes JS/contratos puros | 18 testes passaram | NLP, URL/TLS policy, QR/link e CNG |
| Gateway Python | 26 testes passaram | Integração em processo, sem iPhone/Windows real |
| Kotlin | Módulo nativo compilado no Linux/Android SDK | Não foi executado em Android físico |
| Swift certificate/URLSession | 10 XCTest passaram no macOS, Xcode 26.6, Swift 6.3.3 | Testes de rede nativa no Mac; não são testes no iOS Simulator |
| CNG iOS, pods e configuração | Gerados e verificados em CI | Info.plist, esquema marvin e pod MarvinNative conferidos |
| Aplicação iOS completa | Release compilada para iOS Simulator com Xcode 26.6 | Sem assinatura Apple; não instala em iPhone físico |
| UI no simulador | Passou: iPhone 17, iOS 26.5; 1 fluxo Maestro, 3 min 8 s | Não cobre áudio, câmera, importação ou Gateway real em iPhone |
| iPhone físico | Não executado | Aparelho/UDID/provisionamento não fornecidos |
| IPA/TestFlight | Não gerados/enviados | Conta/projeto EAS e assinatura Apple pendentes |

A aplicação completa foi compilada no [run 38891500385](https://github.com/joaoranucci/M.A.R.V.I.N/actions/runs/38891500385), commit `1c4f3843d5d2a699871f9fd3241e6a10e8e0ef58`. Os jobs de lint/typecheck, 18 testes JS, 26 testes Gateway, 10 testes Swift e compilação Kotlin desse run passaram. O teste de UI usa essa mesma build; seu workflow confere os fontes nativos, JavaScript/TypeScript, dependências, assets e plugins antes de reutilizar um artefato.

## Execução real no simulador

O [run 38901642198](https://github.com/joaoranucci/M.A.R.V.I.N/actions/runs/38901642198), commit `3d86e02b297da9b25e804afeabe3b6b45c7f7bf9`, instalou a aplicação Release do run 38891500385 e executou o fluxo completo com sucesso. Os arquivos do aplicativo usados pela build e pelo teste eram iguais; as mudanças posteriores eram de automação e documentação.

As [oito capturas originais](evidence/README.md) foram conferidas visualmente e estão versionadas no repositório. A execução cobriu:

- Tela principal e núcleo renderizado, com campo de mensagem oculto por padrão.
- Abertura do teclado, digitação de “teste de teclado”, posicionamento do campo e fechamento.
- Abas Biblioteca/Memórias, Atividades/Tarefas, Dispositivos e Configurações/Voz.
- Listagem nativa das vozes disponíveis e chamada da preferência de saída ao módulo Swift, alternando Alto-falante/Automática sem erro.
- Abertura de `marvin://pair` com o app encerrado e com ele aberto; troca do nome do PC e manutenção da confirmação explícita da impressão digital.
- Link com dados inválidos, com erro visível e aplicativo utilizável.

O teste não confirmou o pareamento com um computador: os endereços, código e pin das capturas são dados sintéticos. Não enviou comandos ao Windows. A preferência de rota foi chamada sem reprodução ativa; isso não comprova troca física de saída, microfone, transcrição, TTS, chamadas ou Bluetooth. O seletor de documentos e as permissões de rede local também precisam de verificação física. A animação apareceu em quadros distintos; fluidez e desempenho em aparelhos antigos não foram medidos.

A automação trata a introdução do teclado em simulador novo e o texto de acessibilidade composto do UITextView. O driver XCTest pode demorar no primeiro boot; o limite de inicialização foi ampliado para cinco minutos. Os logs e artefatos permitem distinguir uma falha do driver de uma falha do aplicativo.

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
