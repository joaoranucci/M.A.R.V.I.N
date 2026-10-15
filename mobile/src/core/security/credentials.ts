import * as SecureStore from 'expo-secure-store';
import { create } from 'zustand';
import { MarvinNative } from '../../../modules/marvin-native';
import { kvDelete, kvGet, kvSet } from '../db/database';

/**
 * Device token lives only in the OS secure store (Android Keystore / iOS Keychain).
 * The non-secret connection description (host, port, pin, server id) lives in SQLite.
 */
export interface Connection {
  host: string;
  port: number;
  pin: string;
  serverId: string;
  serverName: string;
  deviceId: string;
  pairedAt: string;
}

const TOKEN_KEY = 'marvin.device-token';
const CONNECTION_KEY = 'connection.v1';
const OPTIONS: SecureStore.SecureStoreOptions = { keychainAccessible: SecureStore.WHEN_UNLOCKED_THIS_DEVICE_ONLY };

interface ConnectionState {
  connection: Connection | null;
  token: string | null;
  loaded: boolean;
  load: () => Promise<void>;
  save: (connection: Connection, token: string) => Promise<void>;
  updateAddress: (host: string, port: number) => Promise<void>;
  clear: () => Promise<void>;
}

export const useConnectionInfo = create<ConnectionState>((set, get) => ({
  connection: null,
  token: null,
  loaded: false,
  load: async () => {
    const raw = await kvGet(CONNECTION_KEY);
    let connection: Connection | null = null;
    try {
      connection = raw ? (JSON.parse(raw) as Connection) : null;
    } catch {
      connection = null;
    }
    const token = connection ? await SecureStore.getItemAsync(TOKEN_KEY, OPTIONS) : null;
    if (connection) MarvinNative.setPinnedKeys([connection.pin]);
    set({ connection: token ? connection : null, token, loaded: true });
  },
  save: async (connection, token) => {
    await SecureStore.setItemAsync(TOKEN_KEY, token, OPTIONS);
    await kvSet(CONNECTION_KEY, JSON.stringify(connection));
    MarvinNative.setPinnedKeys([connection.pin]);
    set({ connection, token });
  },
  updateAddress: async (host, port) => {
    const current = get().connection;
    if (!current) return;
    const next = { ...current, host, port };
    await kvSet(CONNECTION_KEY, JSON.stringify(next));
    set({ connection: next });
  },
  clear: async () => {
    await SecureStore.deleteItemAsync(TOKEN_KEY, OPTIONS);
    await kvDelete(CONNECTION_KEY);
    MarvinNative.setPinnedKeys([]);
    set({ connection: null, token: null });
  },
}));

export const connectionInfo = () => useConnectionInfo.getState();
