import { createAudioPlayer, setAudioModeAsync, type AudioPlayer } from 'expo-audio';
import { Directory, File, Paths } from 'expo-file-system';
import * as Speech from 'expo-speech';
import { log } from '../../core/logging/logger';
import { useConnectivity } from '../../core/net/connectivity';
import { settings, useSettings } from '../../core/settings';
import { spokenText } from '../assistant/nlp/text';
import { gateway } from '../gateway/api';
import { acquireFocus, releaseFocus } from './audioSession';
import { fromFrames, setLevel, startDecay, stopDecay } from './level';

/**
 * Speech output. Server voices (Faber local / Antônio online) are synthesized on the PC
 * and played here; device voices use Android TextToSpeech. Temporary audio files are
 * deleted after playback and on startup.
 */
const MAX_SPOKEN = 1100;
const ttsDir = new Directory(Paths.cache, 'tts');

export interface SpeakResult {
  interrupted: boolean;
  engine: 'device' | 'server' | 'none';
  error?: string;
}

let player: AudioPlayer | null = null;
let currentFile: File | null = null;
let finish: ((result: SpeakResult) => void) | null = null;
let generation = 0;
let estimateTimer: ReturnType<typeof setInterval> | null = null;
let abort: AbortController | null = null;

export function cleanupTempAudio(): void {
  try {
    if (ttsDir.exists) ttsDir.delete();
  } catch (error) {
    log.warn('tts', `limpeza: ${error instanceof Error ? error.message : String(error)}`);
  }
}

export function speechExcerpt(text: string): string {
  const clean = spokenText(text);
  if (clean.length <= MAX_SPOKEN) return clean;
  const cut = clean.slice(0, MAX_SPOKEN);
  const end = Math.max(cut.lastIndexOf('. '), cut.lastIndexOf('! '), cut.lastIndexOf('? '));
  return (end > 300 ? cut.slice(0, end + 1) : cut) + ' Os detalhes estão na tela.';
}

function done(result: SpeakResult) {
  const callback = finish;
  finish = null;
  if (estimateTimer) clearInterval(estimateTimer);
  estimateTimer = null;
  stopDecay();
  releaseFocus();
  if (player) {
    try {
      player.remove();
    } catch {
      // already released
    }
    player = null;
  }
  if (currentFile) {
    try {
      currentFile.delete();
    } catch {
      // temp file may be gone
    }
    currentFile = null;
  }
  callback?.(result);
}

function estimatedEnvelope() {
  // Device TTS exposes no amplitude: a soft procedural pulse, flagged as estimated.
  let t = 0;
  estimateTimer = setInterval(() => {
    t += 1;
    setLevel(0.35 + 0.25 * Math.abs(Math.sin(t / 2.3)) + 0.15 * Math.abs(Math.sin(t / 0.9)), true);
  }, 90);
}

function speakDevice(text: string, mine: number): Promise<SpeakResult> {
  const { deviceVoiceId, speechRate, speechVolume } = settings();
  return new Promise((resolve) => {
    finish = resolve;
    Speech.speak(text, {
      language: 'pt-BR',
      voice: deviceVoiceId ?? undefined,
      rate: speechRate,
      volume: speechVolume,
      onStart: () => {
        if (mine === generation) estimatedEnvelope();
      },
      onDone: () => {
        if (mine === generation) done({ interrupted: false, engine: 'device' });
      },
      onStopped: () => {
        if (mine === generation) done({ interrupted: true, engine: 'device' });
      },
      onError: (error) => {
        if (mine === generation) done({ interrupted: false, engine: 'device', error: error.message });
      },
    });
  });
}

async function speakServer(text: string, mine: number): Promise<SpeakResult> {
  const { serverVoiceId, speechRate, speechVolume } = settings();
  abort = new AbortController();
  const audio = await gateway.speech(text, serverVoiceId, speechRate, abort.signal);
  if (mine !== generation) return { interrupted: true, engine: 'server' };
  if (!ttsDir.exists) ttsDir.create({ intermediates: true });
  const bytes = new Uint8Array(audio);
  const isWav = bytes[0] === 0x52 && bytes[1] === 0x49; // "RI"FF
  const file = new File(ttsDir, `fala-${Date.now()}.${isWav ? 'wav' : 'mp3'}`);
  file.create({ overwrite: true });
  file.write(bytes);
  currentFile = file;
  await setAudioModeAsync({ interruptionMode: 'mixWithOthers', playsInSilentMode: true, shouldPlayInBackground: false });
  return new Promise((resolve) => {
    finish = resolve;
    const created = createAudioPlayer(file.uri);
    player = created;
    created.volume = speechVolume;
    if (created.isAudioSamplingSupported) {
      try {
        created.setAudioSamplingEnabled(true);
        created.addListener('audioSampleUpdate', (sample) => {
          const frames = sample.channels[0]?.frames ?? [];
          setLevel(fromFrames(frames));
        });
      } catch {
        estimatedEnvelope();
      }
    } else estimatedEnvelope();
    created.addListener('playbackStatusUpdate', (status) => {
      if (mine !== generation) return;
      if (status.didJustFinish) done({ interrupted: false, engine: 'server' });
    });
    created.play();
  });
}

/** Speaks a reply. Resolves when finished or interrupted; never throws. */
export async function speak(text: string): Promise<SpeakResult> {
  stopSpeaking();
  const excerpt = speechExcerpt(text);
  if (!excerpt) return { interrupted: false, engine: 'none' };
  const mine = ++generation;
  if (!acquireFocus('speak')) return { interrupted: true, engine: 'none', error: 'Áudio ocupado por uma chamada.' };
  startDecay();
  const { voiceProvider } = settings();
  const serverReady = voiceProvider === 'server' && useConnectivity.getState().gateway === 'online';
  if (serverReady) {
    try {
      return await speakServer(excerpt, mine);
    } catch (error) {
      if (mine !== generation) return { interrupted: true, engine: 'server' };
      log.warn('tts', `voz do PC indisponível, usando a do aparelho: ${error instanceof Error ? error.message : String(error)}`);
      if (player || currentFile) done({ interrupted: true, engine: 'server' });
      if (!acquireFocus('speak')) return { interrupted: true, engine: 'none' };
      startDecay();
    }
  }
  return speakDevice(excerpt, mine);
}

/** Immediate stop: device TTS, PC audio playback and any pending synthesis request. */
export function stopSpeaking(): void {
  generation++;
  abort?.abort();
  abort = null;
  void Speech.stop();
  if (finish || player || currentFile) done({ interrupted: true, engine: player ? 'server' : 'device' });
}

export function isSpeaking(): boolean {
  return finish !== null;
}

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
