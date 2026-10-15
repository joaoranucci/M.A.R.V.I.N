import { create } from 'zustand';
import { kvGet, kvSet } from './db/database';

export type ReduceMotion = 'system' | 'on' | 'off';
export type VoiceProvider = 'device' | 'server';
export type Engine = 'marvin' | 'ollama';

export interface Settings {
  userName: string;
  engine: Engine;
  voiceProvider: VoiceProvider;
  deviceVoiceId: string | null;
  serverVoiceId: string;
  speechRate: number;
  speechVolume: number;
  speakReplies: boolean;
  onDeviceRecognition: boolean;
  silenceMs: number;
  wakeWordEnabled: boolean;
  reduceMotion: ReduceMotion;
  historyRetentionDays: number;
  confirmCommonDesktopActions: boolean;
  demoMode: boolean;
  onboardingDone: boolean;
}

export const DEFAULT_SETTINGS: Settings = {
  userName: 'João',
  engine: 'marvin',
  voiceProvider: 'server',
  deviceVoiceId: null,
  serverVoiceId: 'piper-faber',
  speechRate: 1.0,
  speechVolume: 1.0,
  speakReplies: true,
  onDeviceRecognition: false,
  silenceMs: 1400,
  wakeWordEnabled: false,
  reduceMotion: 'system',
  historyRetentionDays: 30,
  confirmCommonDesktopActions: false,
  demoMode: false,
  onboardingDone: false,
};

interface SettingsState extends Settings {
  loaded: boolean;
  load: () => Promise<void>;
  update: (patch: Partial<Settings>) => Promise<void>;
}

const KEY = 'settings.v1';

export const useSettings = create<SettingsState>((set, get) => ({
  ...DEFAULT_SETTINGS,
  loaded: false,
  load: async () => {
    const raw = await kvGet(KEY);
    let stored: Partial<Settings> = {};
    try {
      stored = raw ? (JSON.parse(raw) as Partial<Settings>) : {};
    } catch {
      stored = {};
    }
    set({ ...DEFAULT_SETTINGS, ...stored, loaded: true });
  },
  update: async (patch) => {
    set(patch);
    const state = get();
    const snapshot: Settings = Object.fromEntries(
      (Object.keys(DEFAULT_SETTINGS) as (keyof Settings)[]).map((k) => [k, state[k]]),
    ) as unknown as Settings;
    await kvSet(KEY, JSON.stringify(snapshot));
  },
}));

export const settings = () => useSettings.getState();
