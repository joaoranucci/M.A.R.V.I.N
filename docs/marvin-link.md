# MARVIN Link v1 — simulador local

`SIMULAR_LINK.bat` ou `EXECUTAR.bat -m marvin.device_link --demo` executa uma troca **em memória, sem Bluetooth ou socket**. Identidades como `simulated-glasses` são fixtures; não são dispositivos autenticados.

O simulador negocia versão/capacidades e MTU, abre sessão e transporta controle, status, cancelamento e bytes de mídia. Usa IDs de mensagem estáveis, sequência por sessão, fragmentos limitados e ledger SQLite para comandos. Repetir um ID confirmado devolve o resultado; repetir com conteúdo diferente falha; interrupção após efeito fica `needs_reconciliation`.

Limites: até 64 KiB por mensagem, 512 fragmentos, quatro montagens simultâneas, 128 KiB acumulados e expiração dos buffers. O overhead JSON/base64 entra no tamanho dos frames. Mídia gera contagem/hash de bytes; não é capturada, decodificada nem reproduzida pelo simulador.

A demonstração incrementa um contador uma única vez, repete o mesmo comando antes e depois de reconectar e cancela a sessão. Os testes também cobrem versões incompatíveis, fragmentos inválidos, sequência antiga e queda durante uma mutação.

## O que falta para hardware

- Escolher e medir placas reais; não se presume compra de ESP32-S3 ou Radxa.
- Transporte BLE autenticado usando bibliotecas/plataforma; este código não implementa criptografia própria.
- Firmware, pareamento, microfone, codec, câmera, saída de áudio, alimentação e indicadores.
- Medir MTU útil, throughput, jitter, perda, interferência, latência, energia e temperatura.
- Validar botão/cancelamento, reconexão e replay entre processos/dispositivos reais.
- Validar captura e reprodução em sequência antes de streaming e interrupção simultânea.

A topologia planejada continua: pulseira hospeda núcleo/memória, óculos são interface, PC executa desktop. Um celular não foi introduzido como dependência. Passar no simulador não comprova rádio, bateria, conforto, qualidade de áudio ou portabilidade física.
