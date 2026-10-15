import { createAudioPlayer, setAudioModeAsync, type AudioPlayer } from 'expo-audio';
import { Directory, File, Paths } from 'expo-file-system';
import * as Speech from 'expo-speech';
import { Platform } from 'react-native';
import { log } from '../../core/logging/logger';
import { useConnectivity } from '../../core/net/connectivity';
import { settings, useSettings } from '../../core/settings';
import { spokenText } from '../assistant/nlp/text';
import { gateway } from '../gateway/api';
import { acquireFocus, releaseFocus } from './audioSession';
import { fromFrames, setLevel, startDecay, stopDecay } from './level';

const MAX_SPOKEN = 1100;
const ttsDir = new Directory(Paths.cache, 'tts');

export interface SpeakResult {
  interrupted: boolean;
  engine: 'device' | 'server' | 'none';
  error?: string;
}

interface Playback {
  id: number;
  engine: 'device' | 'server';
  abort: AbortController;
  player: AudioPlayer | null;
  file: File | null;
  timer: ReturnType<typeof setInterval> | null;
  resolve?: (result: SpeakResult) => void;
}

let generation = 0;
let current: Playback | null = null;

export function cleanupTempAudio(): void {
  try { if (ttsDir.exists) ttsDir.delete(); }
  catch { log.warn('tts', 'Não foi possível limpar o áudio temporário.'); }
}

export function speechExcerpt(text: string): string {
  const clean = spokenText(text);
  if (clean.length <= MAX_SPOKEN) return clean;
  const cut = clean.slice(0, MAX_SPOKEN);
  const end = Math.max(cut.lastIndexOf('. '), cut.lastIndexOf('! '), cut.lastIndexOf('? '));
  return (end > 300 ? cut.slice(0, end + 1) : cut) + ' Os detalhes estão na tela.';
}

function removeResources(owner: Playback) {
  if (owner.timer) clearInterval(owner.timer);
  owner.timer = null;
  try { owner.player?.pause(); } catch { /* already released */ }
  try { owner.player?.remove(); } catch { /* already released */ }
  owner.player = null;
  try { owner.file?.delete(); } catch { /* already removed */ }
  owner.file = null;
}

function done(owner: Playback, result: SpeakResult) {
  if (current !== owner) return;
  current = null;
  removeResources(owner);
  stopDecay();
  releaseFocus();
  owner.resolve?.(result);
  owner.resolve = undefined;
}

function estimatedEnvelope(owner: Playback) {
  if (owner.timer) clearInterval(owner.timer);
  let t = 0;
  owner.timer = setInterval(() => {
    if (current !== owner) return;
    t++;
    setLevel(0.35 + 0.25 * Math.abs(Math.sin(t / 2.3)) + 0.15 * Math.abs(Math.sin(t / 0.9)), true);
  }, 90);
}

function speakDevice(text: string, owner: Playback): Promise<SpeakResult> {
  const { deviceVoiceId, speechRate, speechVolume } = settings();
  owner.engine = 'device';
  return new Promise((resolve) => {
    owner.resolve = resolve;
    Speech.speak(text, {
      language: 'pt-BR', voice: deviceVoiceId ?? undefined,
      rate: speechRate, volume: speechVolume,
      ...(Platform.OS === 'ios' ? { useApplicationAudioSession: true } : {}),
      onStart: () => { if (current === owner) estimatedEnvelope(owner); },
      onDone: () => done(owner, { interrupted: false, engine: 'device' }),
      onStopped: () => done(owner, { interrupted: true, engine: 'device' }),
      onError: (error) => done(owner, { interrupted: false, engine: 'device', error: error.message }),
    });
  });
}

async function speakServer(text: string, owner: Playback): Promise<SpeakResult> {
  const { serverVoiceId, speechRate, speechVolume } = settings();
  const audio = await gateway.speech(text, serverVoiceId, speechRate, owner.abort.signal);
  if (current !== owner) return { interrupted: true, engine: 'server' };
  if (!ttsDir.exists) ttsDir.create({ intermediates: true });
  const bytes = new Uint8Array(audio);
  const isWav = bytes[0] === 0x52 && bytes[1] === 0x49;
  const file = new File(ttsDir, 'fala-' + owner.id + (isWav ? '.wav' : '.mp3'));
  file.create({ overwrite: true });
  file.write(bytes);
  owner.file = file;
  await setAudioModeAsync({
    interruptionMode: Platform.OS === 'ios' ? 'doNotMix' : 'mixWithOthers',
    playsInSilentMode: true, shouldPlayInBackground: false,
    ...(Platform.OS === 'ios' ? { allowsRecording: true } : {}),
  });
  if (current !== owner) return { interrupted: true, engine: 'server' };
  if (!acquireFocus('speak')) throw new Error('Áudio interrompido pelo sistema.');
  return new Promise((resolve) => {
    owner.resolve = resolve;
    const created = createAudioPlayer(file.uri);
    owner.player = created;
    created.volume = speechVolume;
    if (created.isAudioSamplingSupported) {
      try {
        created.setAudioSamplingEnabled(true);
        created.addListener('audioSampleUpdate', (sample) => {
          if (current === owner) setLevel(fromFrames(sample.channels[0]?.frames ?? []));
        });
      } catch { estimatedEnvelope(owner); }
    } else estimatedEnvelope(owner);
    created.addListener('playbackStatusUpdate', (status) => {
      if (status.didJustFinish) done(owner, { interrupted: false, engine: 'server' });
    });
    created.play();
  });
}

/** A new utterance waits for the old device synthesizer to stop before taking the microphone/audio session. */
export async function speak(text: string): Promise<SpeakResult> {
  const stopping = stopSpeaking();
  const mine = ++generation;
  await stopping;
  const excerpt = speechExcerpt(text);
  if (mine !== generation) return { interrupted: true, engine: 'none' };
  if (!excerpt) return { interrupted: false, engine: 'none' };
  if (!acquireFocus('speak')) return { interrupted: true, engine: 'none', error: 'Áudio ocupado por uma chamada ou interrupção do sistema.' };
  const owner: Playback = { id: mine, engine: 'device', abort: new AbortController(), player: null, file: null, timer: null };
  current = owner;
  startDecay();
  try {
    if (settings().voiceProvider === 'server' && useConnectivity.getState().gateway === 'online') {
      owner.engine = 'server';
      try { return await speakServer(excerpt, owner); }
      catch {
        if (current !== owner) return { interrupted: true, engine: 'server' };
        log.warn('tts', 'Voz do PC indisponível; usando a voz do aparelho.');
        removeResources(owner);
        if (!acquireFocus('speak')) {
          const result: SpeakResult = { interrupted: true, engine: 'none' };
          done(owner, result);
          return result;
        }
      }
    }
    return await speakDevice(excerpt, owner);
  } catch {
    const result: SpeakResult = { interrupted: false, engine: owner.engine, error: 'Não foi possível reproduzir esta voz.' };
    done(owner, result);
    return result;
  }
}

/** Stop is invoked before any await: cancel synthesis, pause/remove audio, discard stale callbacks. */
export function stopSpeaking(): Promise<void> {
  const mine = ++generation;
  const owner = current;
  current = null;
  owner?.abort.abort();
  if (owner) {
    removeResources(owner);
    owner.resolve?.({ interrupted: true, engine: owner.engine });
    owner.resolve = undefined;
  }
  stopDecay();
  return Speech.stop().catch(() => {}).finally(() => {
    if (generation === mine && !current) releaseFocus();
  });
}

export function isSpeaking(): boolean { return current !== null; }

/** Plays a short sample of a specific voice (settings screen). */
export async function testVoice(kind: 'device' | 'server', voiceId: string): Promise<SpeakResult> {
  const previous = settings();
  const sample = 'Olá, João. Eu sou o MARVIN. Esta é a minha voz.';
  const patch = kind === 'device' ? { voiceProvider: 'device' as const, deviceVoiceId: voiceId } : { voiceProvider: 'server' as const, serverVoiceId: voiceId };
  const original = { voiceProvider: previous.voiceProvider, deviceVoiceId: previous.deviceVoiceId, serverVoiceId: previous.serverVoiceId };
  useSettings.setState(patch);
  try {
    return await speak(sample);
  } finally {
    useSettings.setState(original);
  }
}
