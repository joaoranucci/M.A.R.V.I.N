import { create } from 'zustand';
import { getDb, kvGet, kvSet } from '../../core/db/database';
import { newId, nowIso } from '../../core/ids';
import { settings } from '../../core/settings';
import { registerPuller } from '../../core/sync/syncEngine';
import { normalize } from '../assistant/nlp/text';
import { gateway } from '../gateway/api';

/**
 * Conversation history: kept for reviewing and continuity, with its own retention.
 * It is never turned into permanent memory automatically.
 */
export type MessageRole = 'user' | 'assistant' | 'system';
export type MessageStatus = 'sending' | 'sent' | 'done' | 'failed' | 'cancelled' | 'offline';

export interface Reference {
  document_id?: string | null;
  filename?: string | null;
  part?: number | null;
  chunk_id?: string | null;
  excerpt?: string;
}

export interface ChatMessage {
  id: string;
  role: MessageRole;
  text: string;
  created_at: string;
  status: MessageStatus;
  source: string;
  origin: 'mobile' | 'desktop';
  task_id: string | null;
  server_id: number | null;
  engine: string | null;
  refs: string | null;
  demo: number;
}

export const useConversation = create<{ messages: ChatMessage[] }>(() => ({ messages: [] }));

export async function loadConversation(limit = 300): Promise<ChatMessage[]> {
  const db = await getDb();
  const rows = await db.getAllAsync<ChatMessage>(
    // rowid keeps insertion order for messages stored within the same second (PC history).
    'SELECT * FROM (SELECT *, rowid AS rid FROM messages WHERE demo = ? ORDER BY created_at DESC, rid DESC LIMIT ?) ORDER BY created_at, rid',
    settings().demoMode ? 1 : 0,
    limit,
  );
  useConversation.setState({ messages: rows });
  return rows;
}

export async function addMessage(message: Partial<ChatMessage> & { role: MessageRole; text: string }): Promise<ChatMessage> {
  const db = await getDb();
  const row: ChatMessage = {
    id: newId(), created_at: nowIso(), status: 'done', source: 'text', origin: 'mobile', task_id: null, server_id: null,
    engine: null, refs: null, demo: settings().demoMode ? 1 : 0, ...message,
  };
  await db.runAsync(
    'INSERT INTO messages(id, role, text, created_at, status, source, origin, task_id, server_id, engine, refs, demo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
    row.id, row.role, row.text, row.created_at, row.status, row.source, row.origin, row.task_id, row.server_id, row.engine, row.refs, row.demo,
  );
  await loadConversation();
  return row;
}

export async function updateMessage(id: string, patch: Partial<ChatMessage>): Promise<void> {
  const keys = Object.keys(patch).filter((k) => k !== 'id') as (keyof ChatMessage)[];
  if (!keys.length) return;
  const db = await getDb();
  await db.runAsync(`UPDATE messages SET ${keys.map((k) => `${k} = ?`).join(', ')} WHERE id = ?`, ...keys.map((k) => patch[k] as never), id);
  await loadConversation();
}

export async function findByTask(taskId: string, role: MessageRole): Promise<ChatMessage | null> {
  const db = await getDb();
  return db.getFirstAsync<ChatMessage>('SELECT * FROM messages WHERE task_id = ? AND role = ? LIMIT 1', taskId, role);
}

export async function clearConversation(): Promise<void> {
  const db = await getDb();
  await db.runAsync('DELETE FROM messages');
  await loadConversation();
}

export async function pruneConversation(): Promise<void> {
  const days = settings().historyRetentionDays;
  if (days <= 0) return;
  const db = await getDb();
  await db.runAsync('DELETE FROM messages WHERE created_at < ?', new Date(Date.now() - days * 86400000).toISOString());
}

export function parseRefs(message: ChatMessage): Reference[] {
  if (!message.refs) return [];
  try {
    return JSON.parse(message.refs) as Reference[];
  } catch {
    return [];
  }
}

/**
 * Continuity with the PC: the shared Runtime history is merged by server id.
 * Messages sent from this phone are recognized (same role and text) instead of duplicated.
 */
registerPuller('conversation-history', async () => {
  if (settings().demoMode) return;
  const key = 'history.after';
  const after = Number((await kvGet(key)) ?? '0') || 0;
  const remote = await gateway.history(after, 200);
  if (!remote.length) return;
  const db = await getDb();
  const unlinked = await db.getAllAsync<ChatMessage>(
    "SELECT * FROM messages WHERE server_id IS NULL AND demo = 0 AND origin = 'mobile' AND created_at > ? ORDER BY created_at",
    new Date(Date.now() - 3 * 86400000).toISOString(),
  );
  for (const message of remote) {
    const exists = await db.getFirstAsync<{ id: string }>('SELECT id FROM messages WHERE server_id = ?', message.id);
    if (exists) continue;
    const match = unlinked.find((m) => m.role === message.role && normalize(m.text) === normalize(message.text));
    if (match) {
      await db.runAsync('UPDATE messages SET server_id = ? WHERE id = ?', message.id, match.id);
      unlinked.splice(unlinked.indexOf(match), 1);
      continue;
    }
    const created = message.created_at ? new Date(message.created_at.replace(' ', 'T') + (message.created_at.includes('Z') || message.created_at.includes('+') ? '' : 'Z')).toISOString() : nowIso();
    await db.runAsync(
      "INSERT INTO messages(id, role, text, created_at, status, source, origin, task_id, server_id, engine, refs, demo) VALUES (?, ?, ?, ?, 'done', 'desktop', 'desktop', NULL, ?, 'marvin', NULL, 0)",
      newId(), message.role, message.text, created, message.id,
    );
  }
  await kvSet(key, String(remote[remote.length - 1].id));
  await loadConversation();
});
