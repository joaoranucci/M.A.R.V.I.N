import { create } from 'zustand';
import { getDb } from '../../core/db/database';
import { newId, nowIso } from '../../core/ids';
import { log } from '../../core/logging/logger';
import { enqueue, registerProcessor, registerPuller } from '../../core/sync/syncEngine';
import { settings } from '../../core/settings';
import { gateway } from '../gateway/api';
import { GatewayError } from '../gateway/client';
import type { TMemory } from '../gateway/schemas';

/**
 * Memories are local-first and synchronized with the Vault through the gateway.
 * origin: what the user asked to keep (user_request) vs. what the assistant inferred
 * (assistant_inference) vs. records that came from elsewhere (imported).
 */
export type MemoryOrigin = 'user_request' | 'assistant_inference' | 'imported';
export type SyncState = 'local_only' | 'pending_create' | 'pending_update' | 'pending_delete' | 'synced' | 'conflict';

export interface Memory {
  id: string;
  server_id: string | null;
  content: string;
  category: string;
  origin: MemoryOrigin;
  source: string;
  created_at: string;
  updated_at: string;
  server_updated_at: string | null;
  sync_state: SyncState;
  conflict: string | null;
  demo: number;
}

export const CATEGORIES = ['geral', 'preferencia', 'trabalho', 'estudos', 'projetos', 'saude', 'pessoas'];
export const originLabel: Record<MemoryOrigin, string> = {
  user_request: 'Você pediu para guardar',
  assistant_inference: 'Inferência do MARVIN',
  imported: 'Importada',
};

interface MemoryStore {
  items: Memory[];
  version: number;
}
export const useMemories = create<MemoryStore>(() => ({ items: [], version: 0 }));

export async function loadMemories(query = ''): Promise<Memory[]> {
  const db = await getDb();
  const demo = settings().demoMode ? 1 : 0;
  const rows = query
    ? await db.getAllAsync<Memory>(
        "SELECT * FROM memories WHERE sync_state != 'pending_delete' AND demo = ? AND (content LIKE ? OR category LIKE ?) ORDER BY updated_at DESC",
        demo,
        `%${query}%`,
        `%${query}%`,
      )
    : await db.getAllAsync<Memory>("SELECT * FROM memories WHERE sync_state != 'pending_delete' AND demo = ? ORDER BY updated_at DESC", demo);
  if (!query) useMemories.setState((s) => ({ items: rows, version: s.version + 1 }));
  return rows;
}

export async function createMemory(content: string, category: string, origin: MemoryOrigin, source: string): Promise<Memory> {
  const db = await getDb();
  const now = nowIso();
  const demo = settings().demoMode ? 1 : 0;
  const memory: Memory = {
    id: newId(), server_id: null, content: content.trim(), category, origin, source, created_at: now, updated_at: now,
    server_updated_at: null, sync_state: demo ? 'local_only' : 'pending_create', conflict: null, demo,
  };
  await db.runAsync(
    'INSERT INTO memories(id, server_id, content, category, origin, source, created_at, updated_at, server_updated_at, sync_state, conflict, demo) VALUES (?, NULL, ?, ?, ?, ?, ?, ?, NULL, ?, NULL, ?)',
    memory.id, memory.content, category, origin, source, now, now, memory.sync_state, demo,
  );
  if (!demo) await enqueue('memory.create', { id: memory.id }, { id: `memory-create-${memory.id}` });
  await loadMemories();
  return memory;
}

export async function updateMemory(id: string, patch: { content: string; category: string; origin?: MemoryOrigin }): Promise<void> {
  const db = await getDb();
  const current = await db.getFirstAsync<Memory>('SELECT * FROM memories WHERE id = ?', id);
  if (!current) return;
  const state: SyncState = current.demo ? 'local_only' : current.sync_state === 'pending_create' ? 'pending_create' : 'pending_update';
  await db.runAsync(
    'UPDATE memories SET content = ?, category = ?, origin = ?, updated_at = ?, sync_state = ?, conflict = NULL WHERE id = ?',
    patch.content.trim(), patch.category, patch.origin ?? current.origin, nowIso(), state, id,
  );
  if (state === 'pending_update') await enqueue('memory.update', { id }, { id: `memory-update-${id}` });
  await loadMemories();
}

export async function deleteMemory(id: string): Promise<void> {
  const db = await getDb();
  const current = await db.getFirstAsync<Memory>('SELECT * FROM memories WHERE id = ?', id);
  if (!current) return;
  if (!current.server_id || current.demo) {
    await db.runAsync('DELETE FROM memories WHERE id = ?', id);
    await db.runAsync('DELETE FROM outbox WHERE id IN (?, ?)', `memory-create-${id}`, `memory-update-${id}`);
  } else {
    await db.runAsync("UPDATE memories SET sync_state = 'pending_delete', updated_at = ? WHERE id = ?", nowIso(), id);
    await db.runAsync('DELETE FROM outbox WHERE id = ?', `memory-update-${id}`);
    await enqueue('memory.delete', { id, server_id: current.server_id }, { id: `memory-delete-${id}` });
  }
  await loadMemories();
}

/** Conflict resolution chosen by the user. */
export async function resolveConflict(id: string, keep: 'mine' | 'server'): Promise<void> {
  const db = await getDb();
  const current = await db.getFirstAsync<Memory>('SELECT * FROM memories WHERE id = ?', id);
  if (!current?.conflict) return;
  const server = JSON.parse(current.conflict) as TMemory;
  if (keep === 'server') {
    await db.runAsync(
      "UPDATE memories SET content = ?, category = ?, origin = ?, server_updated_at = ?, updated_at = ?, sync_state = 'synced', conflict = NULL WHERE id = ?",
      server.content, server.category, server.origin, server.updated_at, server.updated_at, id,
    );
  } else {
    await db.runAsync("UPDATE memories SET server_updated_at = ?, sync_state = 'pending_update', conflict = NULL WHERE id = ?", server.updated_at, id);
    await enqueue('memory.update', { id }, { id: `memory-update-${id}` });
  }
  await loadMemories();
}

/** Local lexical search used by voice ("o que você lembra sobre…") — works offline. */
export async function recall(query: string | null): Promise<Memory[]> {
  const all = await loadMemories();
  if (!query) return all.slice(0, 5);
  const words = query.toLowerCase().split(/\s+/).filter((w) => w.length > 2);
  return all.filter((m) => words.some((w) => m.content.toLowerCase().includes(w) || m.category.includes(w))).slice(0, 5);
}

// ---- sync ------------------------------------------------------------------------------
registerProcessor('memory.create', async ({ id }: { id: string }) => {
  const db = await getDb();
  const m = await db.getFirstAsync<Memory>('SELECT * FROM memories WHERE id = ?', id);
  if (!m || m.server_id) return;
  const saved = await gateway.createMemory({ client_id: m.id, content: m.content, category: m.category, origin: m.origin, source: m.source });
  await db.runAsync(
    "UPDATE memories SET server_id = ?, server_updated_at = ?, sync_state = CASE WHEN sync_state = 'pending_create' THEN 'synced' ELSE sync_state END WHERE id = ?",
    saved.id, saved.updated_at, id,
  );
  // An edit made while the create was in flight still needs to be pushed.
  const after = await db.getFirstAsync<Memory>('SELECT * FROM memories WHERE id = ?', id);
  if (after && (after.content !== saved.content || after.category !== saved.category)) {
    await db.runAsync("UPDATE memories SET sync_state = 'pending_update' WHERE id = ?", id);
    await enqueue('memory.update', { id }, { id: `memory-update-${id}` });
  }
});

registerProcessor('memory.update', async ({ id }: { id: string }) => {
  const db = await getDb();
  const m = await db.getFirstAsync<Memory>('SELECT * FROM memories WHERE id = ?', id);
  if (!m || !m.server_id || m.sync_state !== 'pending_update') return;
  try {
    const saved = await gateway.updateMemory(m.server_id, {
      content: m.content, category: m.category, origin: m.origin, base_updated_at: m.server_updated_at,
    });
    await db.runAsync("UPDATE memories SET server_updated_at = ?, sync_state = 'synced' WHERE id = ? AND updated_at = ?", saved.updated_at, id, m.updated_at);
  } catch (error) {
    if (error instanceof GatewayError && error.status === 409) {
      await db.runAsync("UPDATE memories SET sync_state = 'conflict', conflict = ? WHERE id = ?", JSON.stringify(error.extra.server_item ?? null), id);
      return;
    }
    if (error instanceof GatewayError && error.status === 404) {
      // Deleted on another device: keep the local text as a new record instead of losing it.
      await db.runAsync("UPDATE memories SET server_id = NULL, sync_state = 'pending_create' WHERE id = ?", id);
      await enqueue('memory.create', { id }, { id: `memory-create-${id}` });
      return;
    }
    throw error;
  }
});

registerProcessor('memory.delete', async ({ id, server_id }: { id: string; server_id: string }) => {
  await gateway.deleteMemory(server_id);
  const db = await getDb();
  await db.runAsync('DELETE FROM memories WHERE id = ?', id);
});

registerPuller('memories', async () => {
  if (settings().demoMode) return;
  const remote = await gateway.memories();
  const db = await getDb();
  const local = await db.getAllAsync<Memory>('SELECT * FROM memories WHERE demo = 0');
  const byServer = new Map(local.filter((m) => m.server_id).map((m) => [m.server_id as string, m]));
  const byId = new Map(local.map((m) => [m.id, m]));
  const seen = new Set<string>();
  for (const r of remote) {
    seen.add(r.id);
    const existing = byServer.get(r.id) ?? (r.client_id ? byId.get(r.client_id) : undefined);
    if (!existing) {
      await db.runAsync(
        "INSERT OR IGNORE INTO memories(id, server_id, content, category, origin, source, created_at, updated_at, server_updated_at, sync_state, conflict, demo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'synced', NULL, 0)",
        r.client_id ?? newId(), r.id, r.content, r.category, r.origin, r.source, r.created_at, r.updated_at, r.updated_at,
      );
      continue;
    }
    if (existing.sync_state === 'synced' && existing.server_updated_at !== r.updated_at) {
      await db.runAsync(
        'UPDATE memories SET server_id = ?, content = ?, category = ?, origin = ?, source = ?, updated_at = ?, server_updated_at = ? WHERE id = ?',
        r.id, r.content, r.category, r.origin, r.source, r.updated_at, r.updated_at, existing.id,
      );
    } else if (!existing.server_id) {
      await db.runAsync('UPDATE memories SET server_id = ?, server_updated_at = ? WHERE id = ?', r.id, r.updated_at, existing.id);
    }
  }
  // Removed on another device: synced local copies go away; local pending edits are kept.
  for (const m of local) {
    if (m.server_id && !seen.has(m.server_id) && m.sync_state === 'synced') {
      await db.runAsync('DELETE FROM memories WHERE id = ?', m.id);
    }
  }
  log.info('sync', `memórias: ${remote.length} no cofre`);
  await loadMemories();
});
