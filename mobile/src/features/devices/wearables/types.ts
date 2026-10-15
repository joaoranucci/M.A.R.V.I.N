/**
 * Extension point for the future bracelet (main wearable software) and glasses.
 * Command/telemetry transport and audio transport are separate on purpose: a BLE GATT
 * control channel cannot be assumed to carry voice (see docs/mobile/WEARABLES.md).
 * Nothing here talks to real hardware yet.
 */
export type WearableKind = 'bracelet' | 'glasses';
export type LinkState = 'disconnected' | 'connecting' | 'connected' | 'unauthorized';

export type WearableEvent =
  | { type: 'trigger'; source: WearableKind; gesture: 'press' | 'double_press' | 'hold' | 'voice_activity' }
  | { type: 'link'; source: WearableKind; state: LinkState }
  | { type: 'battery'; source: WearableKind; level: number; charging: boolean | null }
  | { type: 'capabilities'; source: WearableKind; capabilities: WearableCapabilities };

export interface WearableCapabilities {
  microphone: boolean;
  speaker: boolean;
  display: boolean;
  camera: boolean;
  haptics: boolean;
  battery: boolean;
  /** Firmware-declared protocol version; the app refuses unknown majors. */
  protocolVersion: string;
}

/** Control channel: small, acknowledged, idempotent messages (e.g. BLE GATT characteristic). */
export interface WearableCommandTransport {
  readonly kind: WearableKind;
  readonly label: string;
  connect(): Promise<void>;
  disconnect(): Promise<void>;
  send(message: { id: string; type: string; payload: Record<string, unknown> }): Promise<{ id: string; ok: boolean }>;
  onEvent(listener: (event: WearableEvent) => void): () => void;
}

/** Audio channel: streaming frames with its own codec and latency budget (LE Audio/LC3, HFP, or vendor). */
export interface WearableAudioTransport {
  readonly codec: string;
  readonly sampleRate: number;
  startCapture(onFrame: (frame: Uint8Array) => void): Promise<void>;
  stopCapture(): Promise<void>;
  play(frames: AsyncIterable<Uint8Array>): Promise<void>;
  stopPlayback(): Promise<void>;
}

export interface WearableAdapter {
  id: string;
  kind: WearableKind;
  simulated: boolean;
  command: WearableCommandTransport;
  audio?: WearableAudioTransport;
}
