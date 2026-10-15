# Pulseira e óculos — o que precisa ser definido com o hardware

Arquitetura alvo: **óculos ⇄ (Bluetooth) ⇄ pulseira** (software principal do wearable) **⇄ celular** ⇄ gateway no PC.
No app: `mobile/src/features/devices/wearables/` (`types.ts`, `hub.ts`, `simulator.ts`). Nada fala com rádio real nesta versão; o simulador só existe no modo demonstração e é identificado como tal.

## Separação obrigatória

| Canal | Uso | Por que separado |
|---|---|---|
| Comando/telemetria | acionamento, estado, bateria, capacidades, comandos curtos | mensagens pequenas, confirmadas e idempotentes; cabe em GATT |
| Áudio | microfone dos óculos/pulseira, fala do MARVIN | fluxo contínuo com codec, latência e consumo próprios; GATT não é adequado para voz |

## Decisões pendentes com o hardware

1. **Papel BLE**: celular como *central* da pulseira? A pulseira é central dos óculos? Quem mantém a conexão quando o app está em segundo plano?
2. **Serviços GATT próprios** (UUIDs de 128 bits): característica de comando (write with response), de eventos (notify/indicate), de capacidades (read). MTU negociado e fragmentação acima dele.
3. **Serviços padrão**: Battery Service `0x180F` (nível), Device Information `0x180A` (firmware/versão). O app só mostra bateria se o hardware expuser.
4. **Segurança**: LE Secure Connections com *bonding*; vínculo pulseira ↔ conta MARVIN (token próprio, revogável como os celulares); proteção contra repetição (contador/nonce por mensagem).
5. **Áudio**: LE Audio (LC3, Android 13+ com suporte do chip), HFP/A2DP clássico, ou codec proprietário (Opus) sobre canal L2CAP CoC. Definir taxa, latência alvo (< 300 ms ida) e quem faz a detecção de voz/palavra de ativação (no wearable economiza rádio).
6. **Protocolo**: envelope versionado `{id, type, payload}` (CBOR ou protobuf), confirmação por `id`, `protocolVersion` com major incompatível recusado.
7. **Eventos mínimos**: `trigger` (toque/duplo toque/segurar/atividade de voz), `link` (conectado, conectando, não autorizado), `battery` (nível, carregando), `capabilities` (mic, alto-falante, display, câmera, háptico).
8. **Atualização de firmware (OTA)**, recuperação e logs de diagnóstico sem dados pessoais.
9. **Segundo plano no Android**: serviço em primeiro plano `connectedDevice` com notificação; limites de varredura; Companion Device Manager para associação estável.
10. **Privacidade**: indicador físico de microfone/câmera nos óculos; nenhum áudio contínuo enviado ao PC sem acionamento.

## Como o app usa hoje

`hub.ts` recebe `WearableEvent`s de qualquer `WearableAdapter`. Um `trigger` chama o mesmo fluxo do toque no núcleo (`startListening`). `link`/`battery` atualizam a tela Dispositivos. Um adaptador real implementará `WearableCommandTransport` (BLE) e, separadamente, `WearableAudioTransport`.
