import { requireOptionalNativeModule, type EventSubscription } from 'expo-modules-core';

export type AudioRoute = 'speaker' | 'earpiece' | 'wired' | 'bluetooth' | 'usb' | 'hdmi';

export interface AudioState {
  outputs: AudioRoute[];
  route: AudioRoute;
  mode: number;
  inCall: boolean;
  volume: number;
  maxVolume: number;
}

export interface FocusChange extends AudioState {
  change: 'gain' | 'loss' | 'loss_transient' | 'duck' | 'other';
  kind: 'speak' | 'listen';
}

export interface SharedFile {
  name: string;
  mimeType: string | null;
  size: number;
  uri: string | null;
  error: string | null;
}

export interface SharedPayload {
  files: SharedFile[];
  text: string | null;
}

export interface CertificateProbe {
  pin: string;
  subject: string;
  notAfter: number;
}

type Events = {
  onAudioFocusChange: (event: FocusChange) => void;
  onAudioRouteChange: (event: AudioState) => void;
  onBecomingNoisy: (event: AudioState) => void;
  onCallStateChange: (event: AudioState) => void;
  onSharedFiles: (event: SharedPayload) => void;
};

interface NativeModuleShape {
  setPinnedKeys(pins: string[]): void;
  getPinnedKeys(): string[];
  probeCertificate(host: string, port: number): Promise<CertificateProbe>;
  requestAudioFocus(kind: 'speak' | 'listen'): boolean;
  abandonAudioFocus(): void;
  getAudioState(): AudioState;
  consumeSharedFiles(): SharedPayload | null;
  addListener<K extends keyof Events>(event: K, listener: Events[K]): EventSubscription;
}

const native = requireOptionalNativeModule<NativeModuleShape>('MarvinNative');

/** False in Expo Go / web: features depending on it report themselves unavailable. */
export const isNativeAvailable = native != null;

const FALLBACK_AUDIO: AudioState = { outputs: [], route: 'speaker', mode: 0, inCall: false, volume: 0, maxVolume: 0 };

export const MarvinNative = {
  setPinnedKeys: (pins: string[]) => native?.setPinnedKeys(pins),
  getPinnedKeys: (): string[] => native?.getPinnedKeys() ?? [],
  probeCertificate: (host: string, port: number): Promise<CertificateProbe> =>
    native ? native.probeCertificate(host, port) : Promise.reject(new Error('Módulo nativo indisponível nesta build.')),
  requestAudioFocus: (kind: 'speak' | 'listen'): boolean => native?.requestAudioFocus(kind) ?? true,
  abandonAudioFocus: () => native?.abandonAudioFocus(),
  getAudioState: (): AudioState => native?.getAudioState() ?? FALLBACK_AUDIO,
  consumeSharedFiles: (): SharedPayload | null => native?.consumeSharedFiles() ?? null,
  addListener<K extends keyof Events>(event: K, listener: Events[K]): EventSubscription {
    return native ? native.addListener(event, listener) : { remove() {} };
  },
};
