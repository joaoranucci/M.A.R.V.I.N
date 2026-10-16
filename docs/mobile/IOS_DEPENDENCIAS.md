# Auditoria Android/iOS — MARVIN Mobile

Base efetivamente resolvida: Expo 57.0.30, expo-modules-core 57.0.23, React Native 0.86.3 e React 19.2.3. Não houve atualização de major do SDK. A matriz descreve a decisão de implementação; o resultado de compilação e de testes está em [IOS_VALIDACAO.md](IOS_VALIDACAO.md).

## Dependências diretas de runtime

| Pacote | Versão no lockfile | Uso/adaptação iOS |
| --- | --- | --- |
| `@expo-google-fonts/space-grotesk` | 0.4.1 | Fontes empacotadas pelo plugin; mesmos arquivos TTF nas duas plataformas. |
| `@expo/vector-icons` | 15.1.1 | Ícones/fontes universais; dependem do sistema de assets do Expo. |
| `@shopify/react-native-skia` | 2.6.2 | Núcleo animado nativo; requer build iOS, não apenas verificação JS. |
| `expo` | 57.0.30 | SDK 57 mantido; CNG e módulos locais. |
| `expo-application` | 57.0.3 | Versão/número de build; sem uso de identificadores exclusivos do Android. |
| `expo-asset` | 57.0.20 | Peer nativo obrigatório de expo-audio; promovido de transitivo para direto. |
| `expo-audio` | 57.0.5 | Resposta binária do PC; modo iOS sem mistura e sem reprodução em segundo plano. |
| `expo-build-properties` | 57.0.22 | CNG: iOS 16.4 e arquiteturas Android existentes. |
| `expo-camera` | 57.0.6 | Scanner QR; câmera somente na tela focada e mediante permissão. |
| `expo-constants` | 57.0.22 | Configuração universal do runtime. |
| `expo-crypto` | 57.0.4 | IDs/UUIDs; sem implementação Android obrigatória no JS. |
| `expo-dev-client` | 57.0.20 | Development builds Android/iOS; Expo Go continua insuficiente. |
| `expo-device` | 57.0.2 | Modelo do aparelho; fallback iPhone no nome de pareamento. |
| `expo-document-picker` | 57.0.3 | Importação Arquivos/iCloud; copia para cache antes de reter na outbox. |
| `expo-file-system` | 57.0.7 | SQLite/documentos/áudio e cópias retidas no sandbox; sem permissão ampla de armazenamento. |
| `expo-font` | 57.0.4 | Fontes incorporadas; fonte monoespaçada iOS usa Menlo. |
| `expo-haptics` | 57.0.3 | Feedback por toque; a disponibilidade física depende do aparelho. |
| `expo-linking` | 57.0.13 | Peer/integração do Router e esquema marvin. |
| `expo-network` | 57.0.2 | Conectividade universal; falha de rede local não é tratada como autorização TLS. |
| `expo-notifications` | 57.0.23 | Lembretes locais; canal só no Android e autorização provisória considerada no iOS. |
| `expo-router` | 57.0.28 | Rotas compartilhadas; +native-intent protege links frios/quentes. |
| `expo-secure-store` | 57.0.4 | Mesmo token/mesma chave; Keychain com acessibilidade apenas deste aparelho. |
| `expo-sharing` | 57.0.23 | Exportação do diagnóstico no iOS; não cria uma Share Extension de entrada. |
| `expo-speech` | 57.0.3 | Vozes do sistema; usa a sessão de áudio do aplicativo no iOS. |
| `expo-speech-recognition` | 57.1.1 | Versão 57.1.1 lida nos fontes; módulo opcional, opções separadas e APIs Android guardadas. |
| `expo-splash-screen` | 57.0.10 | Inicialização e splash universais. |
| `expo-sqlite` | 57.0.4 | Mesma base/esquema/chaves/outbox; sem reset ou migração destrutiva. |
| `expo-status-bar` | 57.0.1 | Status bar clara na interface escura. |
| `expo-system-ui` | 57.0.4 | Aparência universal; sem chamada Android obrigatória no caminho iOS. |
| `react` | 19.2.3 | Versão 19.2.3 mantida. |
| `react-dom` | 19.2.3 | Peer resolvido na árvore; não adiciona interface web ao aplicativo. |
| `react-native` | 0.86.3 | 0.86.3 mantido, conforme SDK 57; validação nativa separada. |
| `react-native-gesture-handler` | 2.32.0 | Raiz de gestos preservada nas duas plataformas. |
| `react-native-reanimated` | 4.5.1 | Animação/UI nativa; versão recomendada pelo SDK mantida. |
| `react-native-safe-area-context` | 5.7.0 | Insets do núcleo, abas e telas; não usa medidas Android fixas. |
| `react-native-screens` | 4.26.2 | Stack nativa nas duas plataformas. |
| `react-native-worklets` | 0.10.1 | Par compatível com Reanimated, mantido. |
| `zod` | 4.6.7 | Validação compartilhada dos contratos do Gateway; JS/TS. |
| `zustand` | 5.0.15 | Estado compartilhado; armazenamento persistente existente preservado. |

## Desenvolvimento e reprodução

| Pacote | Versão resolvida |
| --- | --- |
| `@react-native/metro-config` | 0.86.3 |
| `@types/react` | 19.2.18 |
| `eslint` | 9.39.5 |
| `eslint-config-expo` | 57.0.2 |
| `typescript` | 6.0.3 |

O lockfile original não reproduzia uma instalação limpa com os peers atuais. React DOM foi alinhado à versão do React, Metro foi explicitado e lint foi instalado usando Expo. O Expo Doctor apontou expo-asset como peer nativo ausente de expo-audio; ele passou a ser dependência direta. A resolução foi conferida pelo Expo instalado. Não foi usado --legacy-peer-deps como procedimento final de instalação.

O npm recente bloqueia scripts de dependências sem autorização no manifest. Foram declarados somente os scripts das versões fixadas de @shopify/react-native-skia 2.6.2 e unrs-resolver 1.12.2, necessários às bibliotecas nativas/resolução do lint. Não há autorização global. [Referência npm](https://docs.npmjs.com/cli/v11/commands/npm-install-scripts/).

## Chamadas e módulos específicos de plataforma

| Área | Android preservado | iOS |
| --- | --- | --- |
| Gateway | OkHttp dedicado, prazo/cancelamento, pin por operação | URLSession efêmero, pin SPKI + datas + host, prazo/cancelamento |
| Upload/áudio/eventos | Mesmo adaptador nativo e contrato | Multipart em arquivo, áudio binário e long polling pelo mesmo transporte |
| Inicialização | Ponte nativa opcional | Ausência do módulo não derruba importação; gateway sem transporte seguro fica indisponível |
| STT | Intent extras e download offline somente no Android | Opções AVAudioSession/pt-BR; sem downloader Android; escolha local sem fallback silencioso para rede |
| Voz | TextToSpeech e foco existentes | expo-speech na sessão do app; AVAudioSession com interrupções/rotas |
| Fones/chamadas | Monitor Kotlin existente | Notificações de interrupção/rotas; nenhum reinício automático da captura |
| Saída | Rotas existentes | Automática/alto-falante/auricular; Bluetooth/AirPlay pelo sistema |
| Configurações TTS | Linking.sendIntent guardado por Android | Linking.openSettings; orientação de vozes em Ajustes |
| Wake word | Experimental, primeiro plano, modelo local | Desativado nesta versão; acionamento por toque |
| Câmera | QR e intenção de câmera preservados | Câmera só no foco; recusa permite abrir ajustes/modo manual |
| Rede local | Mesma LAN/VPN | NSLocalNetworkUsageDescription; nenhuma lib de descoberta/multicast adicionada |
| Notificações | Canal Android somente nesse ramo | Permissões iOS, autorização provisória, gatilho sem channelId |
| Arquivos | Picker e compartilhamento de entrada existentes | Picker no sandbox; extensão de entrada avaliada separadamente |
| Armazenamento seguro | Android Keystore | iOS Keychain, mesmo nome/chaves, dispositivo apenas |
| UI | Núcleo e navegação existentes | Áreas seguras, teclado, Menlo e textos de sistema adequados |

O campo inCall no evento iOS representa conservadoramente uma interrupção do sistema; AVAudioSession não identifica com precisão toda chamada telefônica. O comportamento é interromper áudio/captura e exigir novo toque.

## Dependências nativas próprias

- Kotlin: Expo Modules, react-android/OkHttp e androidx.core existentes. MarvinHttp não depende de uma implementação de fetch nem envia credenciais a redirecionamentos.
- Swift: ExpoModulesCore, Foundation, AVFoundation, Security e CryptoKit. Deployment target 16.4. Podspec lista somente os quatro fontes do módulo; testes SwiftPM não entram no pod do app.
- Config plugins: withShareIntent permanece Android. withMarvinIOS é executado por último para conservar a permissão de microfone após expo-camera e declarar a rede local sem liberar TLS arbitrário.
- Gateway: requisitos mínimos em requirements-mobile-gateway.txt. Migração do certificado mantém a chave/pin e adiciona EKU serverAuth e SAN atual; testes verificam preservação.

## Fontes usadas

- [SDK 57 e versões suportadas](https://docs.expo.dev/versions/v57.0.0/)
- [Módulos Expo](https://docs.expo.dev/modules/module-api/)
- [Código do reconhecimento 57.1.1](https://github.com/jamsch/expo-speech-recognition)
- [Audio](https://docs.expo.dev/versions/v57.0.0/sdk/audio/), [Speech](https://docs.expo.dev/versions/v57.0.0/sdk/speech/), [Asset](https://docs.expo.dev/versions/v57.0.0/sdk/asset/)
- [DocumentPicker](https://docs.expo.dev/versions/v57.0.0/sdk/document-picker/), [SecureStore](https://docs.expo.dev/versions/v57.0.0/sdk/securestore/), [Notifications](https://docs.expo.dev/versions/v57.0.0/sdk/notifications/)
- [Requisitos TLS da Apple](https://support.apple.com/en-us/103769)
