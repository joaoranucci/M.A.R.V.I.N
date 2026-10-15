# MARVIN Mobile (Android e iOS · v0.1)

App de voz do MARVIN: núcleo animado, conversa falada em pt-BR, memórias com origem, biblioteca de documentos, tarefas e ações verificáveis no computador. Expo SDK 57 · React Native 0.86 · TypeScript · Nova Arquitetura.

Decisões: [docs/mobile/DECISOES.md](../docs/mobile/DECISOES.md) · Contrato do gateway: [docs/mobile/API_GATEWAY.md](../docs/mobile/API_GATEWAY.md) · Wearables: [docs/mobile/WEARABLES.md](../docs/mobile/WEARABLES.md) · Validação: [docs/mobile/VALIDACAO.md](../docs/mobile/VALIDACAO.md)

Instalação no iPhone, EAS pelo Windows e TestFlight: [guia iOS](../docs/mobile/IOS.md). Auditoria: [dependências](../docs/mobile/IOS_DEPENDENCIAS.md). Evidências e limites: [validação iOS](../docs/mobile/IOS_VALIDACAO.md).

## Como as peças se conectam

```
Celular (este app) ──HTTPS fixado (TLS)──► Gateway Mobile no PC (marvin/gateway, porta 8770)
                                              ├─► Runtime/Presença do MARVIN (conversa, tarefas, ações, aprovações)
                                              ├─► MARVIN Vault API 127.0.0.1:8765 (memórias e documentos; token fica no PC)
                                              └─► Ollama 127.0.0.1:11434 (motor alternativo, opcional)
```

## Pré-requisitos no Windows

- Node.js 22.13+ (testado com 24.15), JDK 17 (Microsoft OpenJDK 17 ou o JBR do Android Studio), Android SDK com plataforma 36 e build-tools.
- No PC do MARVIN: `.venv` do projeto com `python-multipart` e `segno` (`pip install -r requirements-desktop.txt -r requirements-mobile-gateway.txt`).

## 1. Ligar o gateway no PC

Escolha um:

- `INICIAR_PRESENCA_COM_CELULAR.bat` — interface Presença + gateway no mesmo processo (mesma fila e autorizações).
- `INICIAR_GATEWAY_CELULAR.bat` — só o gateway, sem janela e sem áudio no PC.

Na primeira execução o Windows pode perguntar sobre o firewall: permita somente em **redes privadas**. Para usar fora de casa, use uma VPN (WireGuard/Tailscale) e defina `MARVIN_MOBILE_ADVERTISE_HOST` com o IP da VPN.

Memórias e biblioteca exigem a MARVIN Vault API aberta e desbloqueada (`C:\API Marvin\INICIAR_API.bat`).

## 2. Vincular o celular

1. No PC: `PAREAR_CELULAR.bat` (abre uma página com QR Code e mostra código + impressão digital).
2. No app: **Dispositivos › Vincular computador** › ler o QR, ou digitar endereço, porta e código e conferir a impressão digital.
3. Revogar: no app (Dispositivos ou Configurações › Conexão › Encerrar sessão) ou no PC com `DISPOSITIVOS_CELULAR.bat`.

O celular precisa do **IP do PC** (ex.: `192.168.0.10`). `localhost` no celular é o próprio celular.

## 3. Desenvolvimento

```bash
cd mobile
npm ci
npx expo prebuild -p android
npx expo run:android
```

`npm start` sobe o Metro para o development build (`expo-dev-client`). Expo Go não serve: o app usa módulos nativos (TLS fixado, áudio, compartilhamento).

Verificações:

```bash
npm run lint
npm run typecheck
npm test
npx expo-doctor
```

## 4. APK de prévia (abre sem servidor de desenvolvimento)

```bash
npm run apk:preview
```

ou `GERAR_APK_CELULAR.bat` na raiz. Saída: `mobile/dist/MARVIN-Mobile-0.1.0-preview.apk` (arm64-v8a + x86_64, assinado com a chave de debug — serve para instalar e testar, não para a Play Store). Instale com `adb install -r dist\MARVIN-Mobile-0.1.0-preview.apk` ou copiando o arquivo para o celular (permita “instalar apps desconhecidos”).

Se o Gradle falhar com `Unable to establish loopback connection`, o script já aplica `JAVA_TOOL_OPTIONS=-Djdk.net.unixdomain.tmpdir=C:\tmp\uds`.

## Organização

```
modules/marvin-native/      Kotlin/Swift: transporte HTTPS fixado, foco/sessão de áudio, interrupções e rotas
plugins/withShareIntent.js  menu Compartilhar do Android
plugins/withMarvinIOS.js    permissões iOS/rede local geradas por CNG
src/app/                    telas (expo-router): MARVIN, Biblioteca, Atividades, Dispositivos, Configurações
src/core/                   SQLite, credenciais seguras, conectividade, eventos (long-poll), sincronização, logs sem segredos
src/features/assistant/     controlador de voz/estados, intenções pt-BR (puras, testadas), eco
src/features/voice/         reconhecimento, síntese (aparelho ou PC), sessão de áudio, amplitude
src/features/{memory,tasks,documents,devices,conversation,providers,gateway}
```

## Configuração de exemplo

O app não tem segredos nem variáveis públicas. Tudo o que é configurável fica nas telas (endereço do PC, voz, motor, retenção). Do lado do PC, veja as variáveis `MARVIN_MOBILE_*` em `.env.example`.
