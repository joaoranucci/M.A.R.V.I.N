import { ExpoSpeechRecognitionModule, RecognizerIntentExtraLanguageModel } from 'expo-speech-recognition';
import { Platform } from 'react-native';
import { log } from '../../core/logging/logger';
import { settings } from '../../core/settings';
import { fromRecognizerVolume, setLevel } from './level';

/**
 * Single owner of Android's SpeechRecognizer. Command capture and wake-word
 * listening never run at the same time; starting one stops the other.
 */
export type SttMode = 'command' | 'wake';
export type MicPermission = 'granted' | 'denied' | 'blocked';

export interface SttCallbacks {
  onPartial?: (text: string) => void;
  onFinal?: (text: string) => void;
  onError?: (code: string, message: string) => void;
  onEnd?: () => void;
}

let mode: SttMode | null = null;
let callbacks: SttCallbacks = {};
let gotFinal = false;
let initialized = false;

function init() {
  if (initialized) return;
  initialized = true;
  ExpoSpeechRecognitionModule.addListener('result', (event) => {
    const text = event.results[0]?.transcript?.trim() ?? '';
    if (!text) return;
    if (event.isFinal) {
      gotFinal = true;
      callbacks.onFinal?.(text);
    } else callbacks.onPartial?.(text);
  });
  ExpoSpeechRecognitionModule.addListener('volumechange', (event) => {
    if (mode === 'command') setLevel(fromRecognizerVolume(event.value));
  });
  ExpoSpeechRecognitionModule.addListener('nomatch', () => {
    if (!gotFinal) callbacks.onError?.('no-speech', 'Não entendi.');
  });
  ExpoSpeechRecognitionModule.addListener('error', (event) => {
    if (event.error === 'aborted') return;
    log.warn('stt', `${mode ?? '-'} erro ${event.error} (${event.code ?? -1})`);
    callbacks.onError?.(event.error, event.message);
  });
  ExpoSpeechRecognitionModule.addListener('end', () => {
    const done = callbacks.onEnd;
    mode = null;
    setLevel(0);
    done?.();
  });
}

export async function micPermission(request: boolean): Promise<MicPermission> {
  const current = await ExpoSpeechRecognitionModule.getPermissionsAsync();
  if (current.granted) return 'granted';
  if (!request) return current.canAskAgain ? 'denied' : 'blocked';
  const asked = await ExpoSpeechRecognitionModule.requestPermissionsAsync();
  if (asked.granted) return 'granted';
  return asked.canAskAgain ? 'denied' : 'blocked';
}

export interface RecognitionAvailability {
  available: boolean;
  onDevice: boolean;
  reason: string | null;
}

export function recognitionAvailability(): RecognitionAvailability {
  if (Platform.OS !== 'android' && Platform.OS !== 'ios') return { available: false, onDevice: false, reason: 'Plataforma sem reconhecimento.' };
  try {
    const available = ExpoSpeechRecognitionModule.isRecognitionAvailable();
    const onDevice = ExpoSpeechRecognitionModule.supportsOnDeviceRecognition();
    return {
      available,
      onDevice,
      reason: available ? null : 'Nenhum serviço de reconhecimento de fala no aparelho (instale/ative o app Google ou “Reconhecimento de fala do Google”).',
    };
  } catch (error) {
    return { available: false, onDevice: false, reason: error instanceof Error ? error.message : 'Reconhecimento indisponível.' };
  }
}

/** Whether the Portuguese model is installed for on-device recognition (Android 13+). */
export async function offlinePortuguese(): Promise<'installed' | 'missing' | 'unsupported'> {
  if (!recognitionAvailability().onDevice) return 'unsupported';
  try {
    const { installedLocales } = await ExpoSpeechRecognitionModule.getSupportedLocales({});
    return installedLocales.some((l) => /^pt[-_]BR$/i.test(l)) ? 'installed' : 'missing';
  } catch {
    return 'unsupported';
  }
}

export async function downloadOfflinePortuguese(): Promise<string> {
  const result = await ExpoSpeechRecognitionModule.androidTriggerOfflineModelDownload({ locale: 'pt-BR' });
  return result.status === 'download_success'
    ? 'Pacote de português instalado.'
    : result.status === 'opened_dialog'
      ? 'Confirme o download na janela do Android.'
      : 'Download agendado pelo Android; pode levar alguns minutos (Wi-Fi recomendado).';
}

export function activeMode(): SttMode | null {
  return mode;
}

export function startRecognition(next: SttMode, handlers: SttCallbacks): void {
  init();
  if (mode) ExpoSpeechRecognitionModule.abort();
  mode = next;
  callbacks = handlers;
  gotFinal = false;
  const { onDeviceRecognition, silenceMs } = settings();
  const availability = recognitionAvailability();
  const wake = next === 'wake';
  ExpoSpeechRecognitionModule.start({
    lang: 'pt-BR',
    interimResults: true,
    continuous: wake,
    maxAlternatives: 1,
    addsPunctuation: !wake,
    // Wake word listening only runs fully on-device; command capture follows the user setting.
    requiresOnDeviceRecognition: wake ? true : onDeviceRecognition && availability.onDevice,
    contextualStrings: ['Marvin', 'MARVIN'],
    androidIntentOptions: {
      EXTRA_LANGUAGE_MODEL: RecognizerIntentExtraLanguageModel.LANGUAGE_MODEL_FREE_FORM,
      EXTRA_SPEECH_INPUT_COMPLETE_SILENCE_LENGTH_MILLIS: silenceMs,
      EXTRA_SPEECH_INPUT_POSSIBLY_COMPLETE_SILENCE_LENGTH_MILLIS: silenceMs,
    },
    volumeChangeEventOptions: { enabled: !wake, intervalMillis: 70 },
  });
}

/** Ask for the final result now (user tapped "Concluir"). */
export function finishRecognition(): void {
  if (mode) ExpoSpeechRecognitionModule.stop();
}

/** Discard everything immediately. */
export function abortRecognition(): void {
  if (mode) {
    ExpoSpeechRecognitionModule.abort();
    mode = null;
    setLevel(0);
  }
}

export function sttErrorMessage(code: string): string {
  switch (code) {
    case 'no-speech':
    case 'speech-timeout':
      return 'Não ouvi nada. Toque no núcleo e fale quando ele acender.';
    case 'not-allowed':
      return 'Sem permissão de microfone. Você pode permitir nas configurações ou digitar.';
    case 'network':
      return 'O reconhecimento de fala precisa de internet neste aparelho (ou do pacote offline de português).';
    case 'audio-capture':
    case 'busy':
      return 'O microfone está ocupado (talvez uma chamada ou outro app).';
    case 'language-not-supported':
      return 'Português do Brasil não está disponível no reconhecimento deste aparelho.';
    case 'service-not-allowed':
      return 'O serviço de reconhecimento de fala está desativado ou ausente no aparelho.';
    default:
      return 'Falha no reconhecimento de fala. Tente de novo ou use “Digitar”.';
  }
}
