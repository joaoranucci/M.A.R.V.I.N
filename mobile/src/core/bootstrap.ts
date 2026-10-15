import { create } from 'zustand';
import { MarvinNative, type SharedPayload } from '../../modules/marvin-native';
import { loadActivities } from '../features/activities/repo';
import { startListening } from '../features/assistant/controller';
import { setWearableTrigger } from '../features/devices/wearables/hub';
import { loadConversation, pruneConversation } from '../features/conversation/repo';
import '../features/devices/desktop';
import { loadDocuments } from '../features/documents/service';
import { loadMemories } from '../features/memory/service';
import { loadItems, notificationStatus } from '../features/tasks/service';
import { startAudioSession } from '../features/voice/audioSession';
import { cleanupTempAudio } from '../features/voice/tts';
import { getDb } from './db/database';
import { onEvent, onResync, startEventStream } from './events/eventStream';
import { log } from './logging/logger';
import { refreshConnectivity, startConnectivity, useConnectivity } from './net/connectivity';
import { connectionInfo, useConnectionInfo } from './security/credentials';
import { useSettings } from './settings';
import { syncNow } from './sync/syncEngine';

/** Files shared from the Android share sheet, waiting for the user to confirm the upload. */
export const useShare = create<{ payload: SharedPayload | null }>(() => ({ payload: null }));

let started = false;
let debounce: ReturnType<typeof setTimeout> | null = null;

function syncSoon(reason: string) {
  if (debounce) clearTimeout(debounce);
  debounce = setTimeout(() => void syncNow(reason), 800);
}

export async function reloadLocalData() {
  await Promise.all([loadConversation(), loadMemories(), loadItems(), loadActivities(), loadDocuments()]);
}

export async function bootstrap(): Promise<void> {
  if (started) return;
  started = true;
  await getDb();
  await useSettings.getState().load();
  await useConnectionInfo.getState().load();
  cleanupTempAudio();
  await pruneConversation();
  await reloadLocalData();
  void notificationStatus(false);

  startAudioSession();
  // A bracelet/glasses trigger behaves exactly like tapping the core.
  setWearableTrigger(() => void startListening());
  startConnectivity();
  startEventStream();

  onResync(() => syncNow('resync'));
  useConnectivity.subscribe((state, previous) => {
    if (state.gateway === 'online' && previous.gateway !== 'online') void syncNow('reconectado');
  });
  onEvent('memory.changed', () => syncSoon('memória alterada'));
  onEvent('item.changed', () => syncSoon('item alterado'));
  onEvent('assistant.task', () => syncSoon('tarefa'));
  onEvent('device.revoked', (event) => {
    const id = (event.data as { device_id?: string }).device_id;
    if (id && id === connectionInfo().connection?.deviceId) void refreshConnectivity();
  });

  const shared = MarvinNative.consumeSharedFiles();
  if (shared) useShare.setState({ payload: shared });
  MarvinNative.addListener('onSharedFiles', (payload) => useShare.setState({ payload }));
  log.info('app', 'inicializado');
}
