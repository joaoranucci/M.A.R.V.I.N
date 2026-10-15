import { makeMutable } from 'react-native-reanimated';

/**
 * Audio amplitude 0..1 read by the core animation on the UI thread.
 * `estimated` is true when the source does not expose real amplitude (device TTS).
 */
export const audioLevel = makeMutable(0);
export const levelIsEstimated = makeMutable(false);

let decayTimer: ReturnType<typeof setInterval> | null = null;

export function setLevel(value: number, estimated = false): void {
  audioLevel.value = Math.max(0, Math.min(1, value));
  levelIsEstimated.value = estimated;
}

/** expo-speech-recognition volume: -2..10 dB-like scale; <= 0 is inaudible. */
export function fromRecognizerVolume(value: number): number {
  return Math.max(0, Math.min(1, value / 10));
}

/** RMS of PCM frames (-1..1) with a soft curve so speech fills the range. */
export function fromFrames(frames: number[]): number {
  if (!frames.length) return 0;
  let sum = 0;
  const step = Math.max(1, Math.floor(frames.length / 256));
  let count = 0;
  for (let i = 0; i < frames.length; i += step) {
    sum += frames[i] * frames[i];
    count++;
  }
  return Math.min(1, Math.sqrt(sum / count) * 3.2);
}

export function startDecay(): void {
  if (decayTimer) return;
  decayTimer = setInterval(() => {
    audioLevel.value = audioLevel.value * 0.82;
  }, 80);
}

export function stopDecay(): void {
  if (decayTimer) clearInterval(decayTimer);
  decayTimer = null;
  audioLevel.value = 0;
}
