# MARVIN Mobile — Android e iPhone

Base mantida: Expo **57.0.30**, React Native **0.86.3**, React **19.2.3**. O SDK requer iOS **16.4+**, Node **22.13+** e Xcode **26.4+**. Foi consultada a [documentação do SDK 57](https://docs.expo.dev/versions/v57.0.0/).

O status de compilação, simulador e aparelho físico está separado em [IOS_VALIDACAO.md](IOS_VALIDACAO.md). Passar no TypeScript não equivale a validar um iPhone. A auditoria está em [IOS_DEPENDENCIAS.md](IOS_DEPENDENCIAS.md).

## Gerar um instalavel para o seu iPhone

**Este repositorio contem o aplicativo e o gerador; ainda nao ha um `.ipa` assinado ou link TestFlight entregue.** A build anterior foi para simulador e nao instala no iPhone.

No Windows, atualize/baixe este repositorio inteiro, instale **Node.js 22.13 ou superior** e abra **[`GERAR_IPHONE.bat`](../../GERAR_IPHONE.bat)** na raiz do projeto:

1. O atalho instala as dependencias e executa lint, typecheck e testes.
2. Faca login na sua conta Expo quando a ferramenta solicitar e escolha/crie o projeto EAS.
3. Cadastre seu iPhone: abra no **Safari do iPhone** o link ou QR mostrado pela CLI e conclua o cadastro.
4. A CLI solicitara login no **Apple Developer Program ativo** e a equipe com acesso ao identificador `dev.marvin.mobile`. Inclua o seu iPhone no perfil de provisionamento.
5. Aguarde a compilacao no EAS. **Somente quando terminar com sucesso**, abra o link de instalacao mostrado pela CLI no iPhone. O arquivo `.ipa` tambem fica nos detalhes dessa build no EAS.

Esse fluxo usa o perfil **preview**: aplicativo com JavaScript embutido, sem servidor Metro. Ele nao envia automaticamente ao TestFlight/App Store. Somente aparelhos incluidos no provisionamento podem instalar a previa. Se ja cadastrou esse iPhone, execute `GERAR_IPHONE.bat -DeviceAlreadyRegistered` para pular o cadastro; na compilacao, confira se ele esta incluido.

O login e a autenticacao em duas etapas acontecem nas ferramentas oficiais. Nao envie senha, codigo Apple, token Expo ou certificado por chat, nem os grave no GitHub. O comando `eas init` salva o project ID real no projeto local; preserve essa vinculacao para as proximas builds. O gerador nao apaga dados do MARVIN.

**Pendente para gerar a primeira build assinada:** acesso ao projeto Expo/EAS, conta Apple Developer ativa com permissao de certificados/perfis para o bundle ID e UDID do iPhone no perfil. Sem essas etapas, nenhum `.ipa` instalavel sera produzido. Nao foi executada uma build assinada ou um teste em iPhone fisico nesta sessao.

Referencia oficial: [EAS — distribuicao interna](https://docs.expo.dev/build/internal-distribution/). Para TestFlight e opcoes avancadas, consulte as secoes de assinatura abaixo.

## Implementação

- Módulo Swift real: AVAudioSession, interrupções, rotas de saída, inspeção de certificado e HTTPS.
- URLSession no iOS e OkHttp dedicado no Android para requisições, uploads, áudio binário e eventos. Interfaces TypeScript e contratos do Gateway compartilhados.
- QR e links exigem comparação da impressão digital antes do envio do código. O link original é preservado antes da decodificação pelo Router, incluindo SPKI com `+`, `/` e `=`.
- Voz no iPhone por toque no núcleo, transcrição pt-BR e vozes do sistema/PC. Não há escuta por nome em segundo plano ou com o app encerrado.
- Documentos pelo seletor Arquivos/iCloud Drive, com cópia no sandbox e a mesma fila de upload.
- Núcleo animado e abas preservados. O campo de texto abre somente pelo botão **Digitar**.
- Projeto nativo gerado por CNG e plugins. Não copie pastas iOS/Android geradas de outra instalação.

## Atualizar o Gateway no PC

Novas instalações da interface por `INSTALAR_INTERFACE.bat` incluem as dependências do Gateway por `requirements-desktop.txt`. Para atualizar uma instalação existente, atualize também os fontes do PC e instale o conjunto menor abaixo no ambiente já usado pelo MARVIN:

No PowerShell:

```powershell
Set-Location 'C:\M.A.R.V.I.N'
.\.venv\Scripts\python.exe -m pip install -r requirements-mobile-gateway.txt
```

Feche e reinicie o Gateway pelo atalho habitual: `INICIAR_PRESENCA_COM_CELULAR.bat` ou `INICIAR_GATEWAY_CELULAR.bat`. A Vault API continua no endereço configurado, com seu token somente no PC.

Certificados antigos não incluíam **serverAuth**, exigido pelo TLS da Apple. O Gateway renova o certificado com **a mesma chave privada** e inclui os endereços LAN e `MARVIN_MOBILE_ADVERTISE_HOST` no SAN. Guarda o primeiro certificado anterior em `gateway-cert.previous.pem`. O pin SPKI, os tokens por dispositivo e os bancos são preservados. Após mudar o IP/VPN, reinicie o Gateway para carregar o certificado atualizado.

Não apague `gateway-key.pem` nem os bancos para corrigir TLS. Uma chave ausente/incompatível gera erro para permitir restaurar o backup. Certificado de CA externa deve ser renovado pelo emissor; essa identidade não é substituída automaticamente.

Use o IP/nome do PC na mesma rede ou VPN, porta padrão 8770. `localhost` no iPhone é o próprio iPhone.

## Segurança e dados preservados

O iOS verifica o SHA-256 do **DER SubjectPublicKeyInfo completo**, as datas do certificado e a política SSL para o host. Usa somente a folha conferida como âncora daquela conexão. Um certificado de CA pública com pin diferente também é recusado. Redirecionamentos não encaminham credenciais.

A inspeção manual cancela o desafio TLS depois de ler o certificado: não envia HTTP, código ou token. Cada sessão é efêmera, sem cache/cookies/credenciais persistentes. Uploads ficam restritos ao sandbox e a 20 MiB; o multipart temporário é removido ao terminar/cancelar.

O plugin declara rede local e mantém `NSAllowsArbitraryLoads=false`. Não desativa TLS nem instala confiança global. O iPhone tem transporte próprio; a configuração OkHttp não é reutilizada como implementação iOS.

| Dado/contrato | Preservação |
| --- | --- |
| Identificador | `dev.marvin.mobile` nas duas plataformas |
| Token por dispositivo | `marvin.device-token`; Keystore/Keychain |
| Keychain | `WHEN_UNLOCKED_THIS_DEVICE_ONLY` |
| Conexão/preferências | `connection.v1` e `settings.v1` |
| Dados/sincronização | Mesmo SQLite, IDs, revisões, tombstones e outbox |
| Documentos | Mesmo `client_id`, categoria, cópia retida e estados assíncronos |
| Eventos | Long polling `/v1/events`, cursor e ressincronização |
| Comandos no PC | Mesmas confirmações, expiração e reconciliação; sem repetição cega |

A ausência do módulo de reconhecimento não derruba a inicialização JS. A ausência do transporte seguro informa indisponibilidade e exige uma build nativa atualizada.

Para atualizar uma instalação Android existente, preserve a chave de assinatura original. Se passar a gerar pelo EAS, importe essa mesma chave em `npx eas-cli@latest credentials --platform android`. Uma assinatura diferente impede a atualização sobre o app instalado; não desinstale o app para contornar esse erro, pois isso pode apagar os dados locais. No iOS, mantenha a equipe e o bundle identifier já usados pela instalação.

## Gerar iOS pelo Windows com EAS

O Windows pode solicitar builds e submissões na nuvem. Compilação local e simulador iOS exigem Mac/Xcode. **Expo Go não executa este projeto**; use development build ou prévia.

Requisitos da conta do responsável:

1. Conta Expo/EAS e projeto vinculado.
2. Apple Developer Program ativo, com acesso a certificados, perfis e ao identificador `dev.marvin.mobile`.
3. Desenvolvimento/prévia física: UDID do iPhone incluído no provisionamento.
4. TestFlight: app registrado no App Store Connect e permissão de envio.

Não foram inventados Team ID, project ID, certificados ou segredos. Faça login na CLI; não envie credenciais por chat.

```powershell
Set-Location 'C:\M.A.R.V.I.N\mobile'
npm ci
npx eas-cli@latest login
npx eas-cli@latest init
npx eas-cli@latest build:configure
```

`init` grava o project ID real. Preserve o bundle identifier se já registrado para este app. Antes da primeira distribuição, confirme que ele pertence à sua equipe.

| Perfil em eas.json | Destino | Uso |
| --- | --- | --- |
| `development` | iPhone físico | Development client; precisa do Metro |
| `development-simulator` | Simulador no Mac | Development client para simulador |
| `preview` | iPhone físico | Distribuição interna, JS embutido, sem Metro |
| `production` | App Store Connect | Distribuição de loja, incremento de build |
| `submit.production` | TestFlight | Conta/app reais, configuração interativa |

### Desenvolvimento

```powershell
npx eas-cli@latest device:create
npx eas-cli@latest build --platform ios --profile development
npx expo start --dev-client
```

Abra no iPhone o link de cadastro da CLI. O aparelho cadastrado no Expo só entra no Apple Developer Portal quando incluído no perfil da build. Instale pelo link do EAS; habilite Modo Desenvolvedor se o iOS solicitar. O development client precisa alcançar o Metro.

Ao cadastrar outro aparelho, gere outra build ou use `npx eas-cli@latest build:resign` para incluir o UDID.

### Prévia e TestFlight

```powershell
npx eas-cli@latest build --platform ios --profile preview
# TestFlight:
npx eas-cli@latest build --platform ios --profile production
npx eas-cli@latest submit --platform ios --profile production --latest
```

A prévia interna exige aparelho no provisionamento; não exige Metro. Uma build de simulador não instala em iPhone físico. A submissão solicita equipe/app quando necessário; complete os dados de privacidade, exportação e teste no App Store Connect. Enviar ao TestFlight não publica na App Store.

## Primeiro uso no iPhone

1. Inicie o Gateway atualizado e gere o pareamento no PC.
2. Abra **Dispositivos › Vincular computador**. Use QR, código manual ou `marvin://pair`.
3. Compare a impressão digital com a do PC e confirme.
4. Permita **Rede Local** ao conectar. Se recusou, ajuste em Ajustes › Apps › MARVIN.
5. Toque no núcleo e permita **Microfone** e **Reconhecimento de Fala**. A recusa mantém **Digitar** disponível.
6. Em **Voz e fala**, selecione/teste a voz e ajuste saída, volume e velocidade.
7. Selecione Bluetooth/AirPlay na Central de Controle. Chamada/interrupção ou desconexão de fones interrompe a sessão; retome por toque.
8. Em **Biblioteca › Documentos › Escolher arquivo**, selecione no Arquivos/iCloud Drive. A primeira conexão fornece formatos/limite. Depois, a cópia retida permite enfileirar uploads offline.

Se escolheu reconhecimento local e o modelo está indisponível, o app não muda silenciosamente para a rede. Desative a preferência explicitamente para autorizar o serviço do sistema. O iOS controla o fim automático da captura; **Concluir** encerra por toque.

As notificações existentes são lembretes locais. A recusa mantém o lembrete no app. Eventos do Gateway usam conexão em primeiro plano; não foi criado APNs para entregar todos esses eventos com o aplicativo encerrado.

## Menu Compartilhar: avaliação separada

**Implementado no iPhone:** importar pelo seletor do sistema e compartilhar diagnóstico para fora via `expo-sharing`.

**Fora desta implementação:** extensão iOS que aparece como destino no menu Compartilhar de outros apps. Não há um alvo fictício registrado.

Essa extensão precisa de outro target, App Group/entitlements, provisionamento do app e da extensão, cópia de arquivos com acesso temporário e confirmação no aplicativo principal. Deve ter plugin CNG e fila no App Group, sem levar tokens em URLs ou compartilhar Keychain sem necessidade. Requer teste separado com Arquivos, Safari e provedores externos. A entrada Android existente foi preservada.

## Verificações

```powershell
npm ci
npx expo install --check
npm run lint
npm run typecheck
npm test
npx expo-doctor
npx expo export --platform ios
```

A CI também compila Kotlin, testa o Gateway Python, compila/testa certificado e URLSession no macOS, gera o projeto CNG/CocoaPods e compila a aplicação para simulador. O fluxo Maestro verifica telas, teclado e links frios/quentes sem parear com um PC real. O resultado efetivamente obtido está em [IOS_VALIDACAO.md](IOS_VALIDACAO.md).

Para repetir TLS no Mac:

```bash
python3 -m venv /tmp/marvin-test-venv
/tmp/marvin-test-venv/bin/pip install cryptography
/tmp/marvin-test-venv/bin/python scripts/ios_tls_fixtures.py --output /tmp/marvin-tls-fixtures --serve
# Em outro terminal, na pasta mobile:
MARVIN_CERT_FIXTURES=/tmp/marvin-tls-fixtures swift test --package-path modules/marvin-native/ios
```

As chaves/certificados dos testes são efêmeros. Para a UI, instale a `.app` do artefato em um simulador Mac, use Maestro CLI 2.11.0 e rode `maestro test --test-output-dir /tmp/marvin-ui .maestro/ios-smoke.yaml`. As imagens ficam na subpasta `takeScreenshot` do pacote de artefatos.

Também é possível repetir uma build existente em **Actions › Run compiled iOS Simulator app › Run workflow**, informando `artifact_run_id`: o número de um run de **push** da CI Mobile que contenha `MARVIN-iOS-Simulator`. O workflow recusa a reutilização se os fontes do app tiverem mudado. A CI principal chama esse mesmo fluxo automaticamente com o artefato da própria compilação.

Referências: [Expo Modules](https://docs.expo.dev/modules/module-api/), [links nativos](https://docs.expo.dev/router/advanced/native-intent/), [Speech 57](https://docs.expo.dev/versions/v57.0.0/sdk/speech/), [Audio 57](https://docs.expo.dev/versions/v57.0.0/sdk/audio/), [SecureStore 57](https://docs.expo.dev/versions/v57.0.0/sdk/securestore/), [distribuição interna](https://docs.expo.dev/build/internal-distribution/), [EAS Submit iOS](https://docs.expo.dev/submit/ios/), [TLS Apple](https://support.apple.com/en-us/103769).
