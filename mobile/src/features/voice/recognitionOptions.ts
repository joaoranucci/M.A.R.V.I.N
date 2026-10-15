import type { ExpoSpeechRecognitionOptions } from 'expo-speech-recognition';

export function platformRecognitionOptions(_silenceMs: number): Partial<ExpoSpeechRecognitionOptions> { return {}; }
