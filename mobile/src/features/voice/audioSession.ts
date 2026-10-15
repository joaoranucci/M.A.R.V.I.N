import { Platform } from 'react-native';
import { create } from 'zustand';
import { MarvinNative, type AudioRoute, type AudioState } from '../../../modules/marvin-native';
import { log } from '../../core/logging/logger';

/**
 * One owner for audio focus. Calls, other apps taking focus and headphone
 * disconnection all reach the assistant as a single "interrupted" signal.
 */
export type InterruptionReason = 'call' | 'focus_lost' | 'headphones_removed';

interface AudioSessionState {
  route: AudioRoute;
  outputs: AudioRoute[];
  inCall: boolean;
  lastInterruption: InterruptionReason | null;
}

export const useAudioSession = create<AudioSessionState>(() => ({ route: 'speaker', outputs: [], inCall: false, lastInterruption: null }));

const listeners = new Set<(reason: InterruptionReason) => void>();
let started = false;

function apply(state: AudioState) {
  useAudioSession.setState({ route: state.route, outputs: state.outputs, inCall: state.inCall });
}

function interrupt(reason: InterruptionReason) {
  useAudioSession.setState({ lastInterruption: reason });
  log.info('audio', `interrompido: ${reason}`);
  for (const listener of listeners) listener(reason);
}

export function startAudioSession(): void {
  if (started) return;
  started = true;
  apply(MarvinNative.getAudioState());
  MarvinNative.addListener('onAudioRouteChange', apply);
  MarvinNative.addListener('onBecomingNoisy', (state) => {
    apply(state);
    interrupt('headphones_removed');
  });
  MarvinNative.addListener('onCallStateChange', (state) => {
    apply(state);
    if (state.inCall) interrupt('call');
  });
  MarvinNative.addListener('onAudioFocusChange', (event) => {
    apply(event);
    if (event.change !== 'loss' && event.change !== 'loss_transient') return;
    if (event.inCall) interrupt('call');
    else if (Platform.OS === 'ios' || !listening) interrupt('focus_lost');
  });
}

export function onInterruption(listener: (reason: InterruptionReason) => void): () => void {
  listeners.add(listener);
  return () => listeners.delete(listener);
}

let listening = false;

export function acquireFocus(kind: 'speak' | 'listen'): boolean {
  const state = MarvinNative.getAudioState();
  apply(state);
  if (state.inCall) return false;
  if (kind === 'listen' && Platform.OS === 'android') {
    // Android's recognizer service takes audio focus itself; requesting it here would
    // make its own focus request look like "another app" and abort the capture.
    listening = true;
    return true;
  }
  listening = false;
  return MarvinNative.requestAudioFocus(kind);
}

export function releaseFocus(): void {
  listening = false;
  MarvinNative.abandonAudioFocus();
}

export const routeLabel: Record<AudioRoute, string> = {
  speaker: 'Alto-falante',
  earpiece: 'Fone do aparelho',
  wired: 'Fone com fio',
  bluetooth: 'Bluetooth',
  usb: 'Áudio USB',
  hdmi: 'HDMI',
  airplay: 'AirPlay',
};

let preferred: 'system' | 'speaker' | 'earpiece' = 'system';

export const preferredAudioRoute = () => preferred;

export function selectAudioRoute(route: 'system' | 'speaker' | 'earpiece'): boolean {
  const changed = MarvinNative.setPreferredAudioRoute(route);
  if (changed) {
    preferred = route;
    apply(MarvinNative.getAudioState());
  }
  return changed;
}
