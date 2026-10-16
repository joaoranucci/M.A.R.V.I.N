import * as Notifications from 'expo-notifications';
import { Platform } from 'react-native';
import { create } from 'zustand';
import { getDb, kvGet, kvSet } from '../../core/db/database';
import { newId, nowIso } from '../../core/ids';
import { log } from '../../core/logging/logger';
import { settings } from '../../core/settings';
import { enqueue, registerProcessor, registerPuller } from '../../core/sync/syncEngine';
import { gateway } from '../gateway/api';
import { GatewayError } from '../gateway/client';
import type { TItem } from '../gateway/schemas';

/** Personal tasks, reminders and notes: local-first, synced with revision numbers. */
export type ItemKind = 'task' | 'reminder' | 'note';

export interface Item {
  id: string;
  kind: ItemKind;
  title: string;
  notes: string;
  due_at: string | null;
  done: number;
  deleted: number;
  rev: number;
  created_at: string;
  updated_at: string;
  sync_state: 'pending' | 'synced' | 'conflict' | 'local_only';
  notification_id: string | null;
  conflict: string | null;
  demo: number;
}

export type NotificationStatus = 'granted' | 'denied' | 'undetermined';

interface ItemsStore {
  items: Item[];
  notifications: NotificationStatus;
}
export const useItems = create<ItemsStore>(() => ({ items: [], notifications: 'undetermined' }));

Notifications.setNotificationHandler({
  handleNotification: async () => ({ shouldShowBanner: true, shouldShowList: true, shouldPlaySound: true, shouldSetBadge: false }),
});

export async function loadItems(): Promise<Item[]> {
  const db = await getDb();
  const rows = await db.getAllAsync<Item>(
    'SELECT * FROM items WHERE deleted = 0 AND demo = ? ORDER BY done, COALESCE(due_at, created_at)',
    settings().demoMode ? 1 : 0,
  );
  useItems.setState({ items: rows });
  return rows;
}

export async function notificationStatus(request: boolean): Promise<NotificationStatus> {
  let permission = await Notifications.getPermissionsAsync();
  if (permission.status !== 'granted' && request && permission.canAskAgain) permission = await Notifications.requestPermissionsAsync();
  const allowed = permission.granted || (Platform.OS === 'ios' &&
    (permission.ios?.status === Notifications.IosAuthorizationStatus.PROVISIONAL ||
     permission.ios?.status === Notifications.IosAuthorizationStatus.EPHEMERAL));
  // Android reports "denied" before the first prompt; only a refusal that blocks asking again counts as denied.
  const value: NotificationStatus =
    allowed ? 'granted' : permission.status === 'denied' && !permission.canAskAgain ? 'denied' : 'undetermined';
  useItems.setState({ notifications: value });
  return value;
}

async function ensureChannel() {
  if (Platform.OS === 'android') {
    await Notifications.setNotificationChannelAsync('lembretes', {
      name: 'Lembretes do MARVIN',
      importance: Notifications.AndroidImportance.HIGH,
      lightColor: '#38D6FF',
    });
  }
}

/** Schedules a local notification; returns null when it cannot (and says why to the caller). */
async function schedule(item: Item, askPermission = true): Promise<string | null> {
  if (!item.due_at || item.done || item.deleted) return null;
  const when = new Date(item.due_at);
  if (when.getTime() <= Date.now()) return null;
  if ((await notificationStatus(askPermission)) !== 'granted') return null;
  await ensureChannel();
  return Notifications.scheduleNotificationAsync({
    content: { title: 'MARVIN · lembrete', body: item.title, data: { itemId: item.id } },
    trigger: { type: Notifications.SchedulableTriggerInputTypes.DATE, date: when, ...(Platform.OS === 'android' ? { channelId: 'lembretes' } : {}) },
  });
}

async function unschedule(item: Item) {
  if (item.notification_id) {
    try {
      await Notifications.cancelScheduledNotificationAsync(item.notification_id);
    } catch {
      // already delivered or cleared
    }
  }
}

async function persistLocal(item: Item) {
  const db = await getDb();
  await db.runAsync(
    `INSERT INTO items(id, kind, title, notes, due_at, done, deleted, rev, created_at, updated_at, sync_state, notification_id, conflict, demo)
     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
     ON CONFLICT(id) DO UPDATE SET kind = excluded.kind, title = excluded.title, notes = excluded.notes, due_at = excluded.due_at,
       done = excluded.done, deleted = excluded.deleted, rev = excluded.rev, updated_at = excluded.updated_at,
       sync_state = excluded.sync_state, notification_id = excluded.notification_id, conflict = excluded.conflict`,
    item.id, item.kind, item.title, item.notes, item.due_at, item.done, item.deleted, item.rev, item.created_at, item.updated_at,
    item.sync_state, item.notification_id, item.conflict, item.demo,
  );
}

export interface SaveResult {
  item: Item;
  notified: boolean;
  notificationIssue: string | null;
}

export async function saveItem(input: Partial<Item> & { kind: ItemKind; title: string }): Promise<SaveResult> {
  const db = await getDb();
  const existing = input.id ? await db.getFirstAsync<Item>('SELECT * FROM items WHERE id = ?', input.id) : null;
  const now = nowIso();
  const demo = settings().demoMode ? 1 : 0;
  const item: Item = {
    id: existing?.id ?? input.id ?? newId(),
    kind: input.kind,
    title: input.title.trim(),
    notes: input.notes ?? existing?.notes ?? '',
    due_at: input.due_at !== undefined ? input.due_at : existing?.due_at ?? null,
    done: input.done ?? existing?.done ?? 0,
    deleted: input.deleted ?? existing?.deleted ?? 0,
    rev: existing?.rev ?? 0,
    created_at: existing?.created_at ?? now,
    updated_at: now,
    sync_state: demo ? 'local_only' : 'pending',
    notification_id: existing?.notification_id ?? null,
    conflict: null,
    demo: existing?.demo ?? demo,
  };
  if (existing) await unschedule(existing);
  let notificationIssue: string | null = null;
  item.notification_id = null;
  if (item.kind === 'reminder' && item.due_at && !item.done && !item.deleted) {
    try {
      item.notification_id = await schedule(item);
      if (!item.notification_id) {
        notificationIssue =
          new Date(item.due_at).getTime() <= Date.now()
            ? 'O horário já passou.'
            : 'Notificações desativadas: o lembrete aparece apenas dentro do app. Ative nos ajustes de notificações do aparelho.';
      }
    } catch (error) {
      notificationIssue = 'Não foi possível agendar a notificação neste aparelho.';
      log.warn('tasks', `agendamento: ${error instanceof Error ? error.message : String(error)}`);
    }
  }
  await persistLocal(item);
  if (!item.demo) await enqueue('item.put', { id: item.id }, { id: `item-${item.id}` });
  await loadItems();
  return { item, notified: !!item.notification_id, notificationIssue };
}

export async function setDone(item: Item, done: boolean) {
  return saveItem({ ...item, done: done ? 1 : 0 });
}

export async function removeItem(item: Item) {
  return saveItem({ ...item, deleted: 1 });
}

export async function resolveItemConflict(id: string, keep: 'mine' | 'server') {
  const db = await getDb();
  const item = await db.getFirstAsync<Item>('SELECT * FROM items WHERE id = ?', id);
  if (!item?.conflict) return;
  const server = JSON.parse(item.conflict) as TItem;
  if (keep === 'server') {
    await unschedule(item);
    const next: Item = {
      ...item, kind: server.kind, title: server.title, notes: server.notes, due_at: server.due_at ?? null,
      done: server.done ? 1 : 0, deleted: server.deleted ? 1 : 0, rev: server.rev, updated_at: server.updated_at,
      sync_state: 'synced', conflict: null, notification_id: null,
    };
    next.notification_id = next.kind === 'reminder' ? await schedule(next).catch(() => null) : null;
    await persistLocal(next);
  } else {
    await db.runAsync("UPDATE items SET rev = ?, sync_state = 'pending', conflict = NULL WHERE id = ?", server.rev, id);
    await enqueue('item.put', { id }, { id: `item-${id}` });
  }
  await loadItems();
}

registerProcessor('item.put', async ({ id }: { id: string }) => {
  const db = await getDb();
  const item = await db.getFirstAsync<Item>('SELECT * FROM items WHERE id = ?', id);
  if (!item || item.sync_state !== 'pending') return;
  try {
    const result = await gateway.putItem(id, {
      kind: item.kind, title: item.title, notes: item.notes, due_at: item.due_at, done: !!item.done, deleted: !!item.deleted,
      base_rev: item.rev || null,
    });
    await db.runAsync("UPDATE items SET rev = ?, sync_state = 'synced' WHERE id = ? AND updated_at = ?", result.item.rev, id, item.updated_at);
  } catch (error) {
    if (error instanceof GatewayError && error.status === 409) {
      await db.runAsync("UPDATE items SET sync_state = 'conflict', conflict = ? WHERE id = ?", JSON.stringify(error.extra.server_item ?? null), id);
      return;
    }
    throw error;
  }
});

registerPuller('items', async () => {
  if (settings().demoMode) return;
  const since = await kvGet('items.since');
  const { items, server_time } = await gateway.items(since ?? undefined);
  const db = await getDb();
  for (const remote of items) {
    const local = await db.getFirstAsync<Item>('SELECT * FROM items WHERE id = ?', remote.id);
    if (local && local.sync_state !== 'synced') {
      continue; // local edit pending: the push detects and surfaces any conflict
    }
    if (local && local.rev >= remote.rev) continue;
    if (local) await unschedule(local);
    const next: Item = {
      id: remote.id, kind: remote.kind, title: remote.title, notes: remote.notes, due_at: remote.due_at ?? null,
      done: remote.done ? 1 : 0, deleted: remote.deleted ? 1 : 0, rev: remote.rev, created_at: remote.created_at,
      updated_at: remote.updated_at, sync_state: 'synced', notification_id: null, conflict: null, demo: 0,
    };
    // Never prompt for permission from a background sync.
    if (next.kind === 'reminder') next.notification_id = await schedule(next, false).catch(() => null);
    await persistLocal(next);
  }
  await kvSet('items.since', server_time);
  await loadItems();
});
