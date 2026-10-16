const { AndroidConfig, withInfoPlist } = require('expo/config-plugins');

function applyIOSInfoPlist(info) {
  return {
    ...info,
    NSMicrophoneUsageDescription: 'O MARVIN usa o microfone quando você toca no núcleo para falar.',
    NSSpeechRecognitionUsageDescription: 'O MARVIN transcreve sua fala em português. Se o modo local estiver desligado, o iOS pode usar o serviço de reconhecimento da Apple.',
    NSCameraUsageDescription: 'O MARVIN usa a câmera somente para ler o QR Code do seu computador.',
    NSLocalNetworkUsageDescription: 'O MARVIN conecta ao seu computador na rede local para conversar, enviar documentos e executar os comandos que você autorizar.',
    NSAppTransportSecurity: {
      ...info.NSAppTransportSecurity,
      NSAllowsArbitraryLoads: false,
      NSAllowsLocalNetworking: true,
    },
  };
}

function withMarvinIOS(config) {
  // Last plugin: expo-camera may remove the microphone description when video recording is disabled.
  config = withInfoPlist(config, (mod) => {
    mod.modResults = applyIOSInfoPlist(mod.modResults);
    return mod;
  });
  return AndroidConfig.Permissions.withPermissions(config, ['android.permission.RECORD_AUDIO']);
}

module.exports = withMarvinIOS;
module.exports.applyIOSInfoPlist = applyIOSInfoPlist;
