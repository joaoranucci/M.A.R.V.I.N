import type { ExpoSpeechRecognitionOptions } from 'expo-speech-recognition';
import { preferredAudioRoute } from './audioSession';

export function platformRecognitionOptions(_silenceMs: number): Partial<ExpoSpeechRecognitionOptions> {
  return {
    iosTaskHint: 'confirmation',
    iosCategory: {
      category: 'playAndRecord',
      mode: 'measurement',
      categoryOptions: preferredAudioRoute() === 'earpiece' ? ['allowBluetooth'] : ['allowBluetooth', 'defaultToSpeaker'],
    },
  };
}
