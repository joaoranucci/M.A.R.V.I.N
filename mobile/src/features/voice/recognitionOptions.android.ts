import type { ExpoSpeechRecognitionOptions } from 'expo-speech-recognition';

export function platformRecognitionOptions(silenceMs: number): Partial<ExpoSpeechRecognitionOptions> {
  return { androidIntentOptions: {
    EXTRA_LANGUAGE_MODEL: 'free_form',
    EXTRA_SPEECH_INPUT_COMPLETE_SILENCE_LENGTH_MILLIS: silenceMs,
    EXTRA_SPEECH_INPUT_POSSIBLY_COMPLETE_SILENCE_LENGTH_MILLIS: silenceMs,
  } };
}
