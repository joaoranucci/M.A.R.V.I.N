import { requireOptionalNativeModule } from 'expo-modules-core';
import { platformRecognitionOptions } from './recognitionOptions';

// Type-only import: a missing or Android-only module cannot crash iPhone startup.
type SpeechModule = typeof import('expo-speech-recognition').ExpoSpeechRecognitionModule;
const speech = requireOptionalNativeModule<SpeechModule>('ExpoSpeechRecognition');
import { Platform } from 'react-native';
import { log } from '../../core/logging/logger';
import { settings } from '../../core/settings';
import { fromRecognizerVolume, setLevel } from './level';

/**
 * Single owner of the platform speech recognizer. Command capture and wake-word
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
  if (initialized || !speech) return;
  initialized = true;
  speech!.addListener('result', (event) => {
    if (!mode) return;
    const text = event.results[0]?.transcript?.trim() ?? '';
    if (!text) return;
    if (event.isFinal) {
      gotFinal = true;
      callbacks.onFinal?.(text);
    } else callbacks.onPartial?.(text);
  });
  speech!.addListener('volumechange', (event) => {
    if (mode === 'command') setLevel(fromRecognizerVolume(event.value));
  });
  speech!.addListener('nomatch', () => {
    if (!gotFinal) callbacks.onError?.('no-speech', 'Não entendi.');
  });
  speech!.addListener('error', (event) => {
    if (event.error === 'aborted') return;
    log.warn('stt', `${mode ?? '-'} erro ${event.error} (${event.code ?? -1})`);
    callbacks.onError?.(event.error, event.message);
  });
  speech!.addListener('end', () => {
    const done = callbacks.onEnd;
    mode = null;
    setLevel(0);
    done?.();
  });
}

export async function micPermission(request: boolean): Promise<MicPermission> {
  if (!speech) return 'blocked';
  const current = await speech!.getPermissionsAsync();
  if (current.granted) return 'granted';
  if (!request || !current.canAskAgain) return current.canAskAgain ? 'denied' : 'blocked';
  const asked = await speech!.requestPermissionsAsync();
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
  if (!speech) return { available: false, onDevice: false, reason: 'Reconhecimento nativo ausente. Instale a build de desenvolvimento do MARVIN.' };
  try {
    const available = speech!.isRecognitionAvailable();
    const onDevice = speech!.supportsOnDeviceRecognition();
    return {
      available,
      onDevice,
      reason: available ? null : Platform.OS === 'ios'
        ? 'Reconhecimento indisponível. Confira os idiomas, Siri e as restrições de privacidade em Ajustes do iPhone.'
        : 'Nenhum serviço de reconhecimento no aparelho. Ative o serviço de fala do Android.',
    };
  } catch (error) {
    return { available: false, onDevice: false, reason: error instanceof Error ? error.message : 'Reconhecimento indisponível.' };
  }
}

/** Whether the Portuguese model is installed for on-device recognition (Android 13+). */
export async function offlinePortuguese(): Promise<'installed' | 'missing' | 'unsupported'> {
  if (Platform.OS !== 'android' || !speech || !recognitionAvailability().onDevice) return 'unsupported';
  try {
    const { installedLocales } = await speech!.getSupportedLocales({});
    return installedLocales.some((l) => /^pt[-_]BR$/i.test(l)) ? 'installed' : 'missing';
  } catch {
    return 'unsupported';
  }
}

export async function downloadOfflinePortuguese(): Promise<string> {
  if (Platform.OS !== 'android' || !speech) return 'O iPhone gerencia os idiomas em Ajustes; o app não baixa modelos do Android.';
  const result = await speech!.androidTriggerOfflineModelDownload({ locale: 'pt-BR' });
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
  const availability = recognitionAvailability();
  const wake = next === 'wake';
  const { onDeviceRecognition, silenceMs } = settings();
  if (!speech || !availability.available || (wake && Platform.OS === 'ios') || ((wake || onDeviceRecognition) && !availability.onDevice)) {
    handlers.onError?.('service-not-allowed', availability.reason ?? 'Reconhecimento local indisponível.');
    handlers.onEnd?.();
    return;
  }
  if (mode) abortRecognition();
  mode = next;
  callbacks = handlers;
  gotFinal = false;
  try {
    speech.start({
      lang: 'pt-BR',
      interimResults: true,
      continuous: wake,
      maxAlternatives: 1,
      addsPunctuation: !wake,
      // An explicit offline choice must never silently fall back to an online recognizer.
      requiresOnDeviceRecognition: wake || onDeviceRecognition,
      contextualStrings: ['Marvin', 'MARVIN'],
      ...platformRecognitionOptions(silenceMs),
      volumeChangeEventOptions: { enabled: !wake, intervalMillis: 70 },
    });
  } catch {
    mode = null;
    callbacks = {};
    handlers.onError?.('audio-capture', 'Não foi possível iniciar a captura.');
    handlers.onEnd?.();
  }
}

/** Ask for the final result now (user tapped "Concluir"). */
export function finishRecognition(): void {
  if (mode) speech?.stop();
}

/** Discard everything immediately. */
export function abortRecognition(): void {
  if (mode) {
    speech?.abort();
    mode = null;
    callbacks = {};
    setLevel(0);
  }
}

export function sttErrorMessage(code: string): string {
  switch (code) {
    case 'no-speech':
    case 'speech-timeout':
      return 'Não ouvi nada. Toque no núcleo e fale quando ele acender.';
    case 'not-allowed':
      return 'Sem permissão de microfone ou reconhecimento de fala. Permita nos ajustes do aparelho ou use “Digitar”.';
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
