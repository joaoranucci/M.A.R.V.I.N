import { create } from 'zustand';
import { GatewayError } from '../../features/gateway/client';
import { getDb } from '../db/database';
import { newId, nowIso } from '../ids';
import { log } from '../logging/logger';
import { useConnectivity } from '../net/connectivity';

/**
 * Local-first sync. Writes go to SQLite and to an ordered outbox; the outbox is
 * flushed when the gateway is reachable. Every operation is idempotent on the
 * server (client ids / revisions), so retrying after a lost response is safe.
 * Operations with an expiry (PC commands) are never sent late: they wait for a new decision.
 */
export type OutboxKind = 'memory.create' | 'memory.update' | 'memory.delete' | 'item.put' | 'document.upload' | 'desktop.command';

export interface OutboxRow {
  id: string;
  kind: OutboxKind;
  payload: string;
  created_at: string;
  attempts: number;
  last_error: string | null;
  expires_at: string | null;
  state: string;
}

type Processor = (payload: any, row: OutboxRow) => Promise<void>;
type Puller = () => Promise<void>;

const processors = new Map<OutboxKind, Processor>();
const expiredHandlers = new Map<OutboxKind, (payload: any) => Promise<void>>();
const pullers = new Map<string, Puller>();

interface SyncState {
  running: boolean;
  lastSyncAt: string | null;
  lastError: string | null;
  pending: number;
}
export const useSync = create<SyncState>(() => ({ running: false, lastSyncAt: null, lastError: null, pending: 0 }));

export function registerProcessor(kind: OutboxKind, processor: Processor, onExpired?: (payload: any) => Promise<void>) {
  processors.set(kind, processor);
  if (onExpired) expiredHandlers.set(kind, onExpired);
}

export function registerPuller(name: string, puller: Puller) {
  pullers.set(name, puller);
}

async function countPending() {
  const db = await getDb();
  const row = await db.getFirstAsync<{ n: number }>("SELECT COUNT(*) AS n FROM outbox WHERE state = 'pending'");
  useSync.setState({ pending: row?.n ?? 0 });
}

export async function enqueue(kind: OutboxKind, payload: unknown, options: { id?: string; expiresAt?: string } = {}) {
  const db = await getDb();
  const id = options.id ?? newId();
  await db.runAsync(
    'INSERT OR REPLACE INTO outbox(id, kind, payload, created_at, attempts, last_error, expires_at, state) VALUES (?, ?, ?, ?, 0, NULL, ?, ?)',
    id,
    kind,
    JSON.stringify(payload),
    nowIso(),
    options.expiresAt ?? null,
    'pending',
  );
  await countPending();
  void syncNow('enqueue');
  return id;
}

export async function outboxRows(): Promise<OutboxRow[]> {
  const db = await getDb();
  return db.getAllAsync<OutboxRow>('SELECT * FROM outbox ORDER BY created_at');
}

export async function dropOutbox(id: string) {
  const db = await getDb();
  await db.runAsync('DELETE FROM outbox WHERE id = ?', id);
  await countPending();
}

async function flush(): Promise<boolean> {
  const db = await getDb();
  const rows = await db.getAllAsync<OutboxRow>("SELECT * FROM outbox WHERE state = 'pending' ORDER BY created_at");
  for (const row of rows) {
    const payload = JSON.parse(row.payload);
    if (row.expires_at && Date.parse(row.expires_at) <= Date.now()) {
      await db.runAsync("UPDATE outbox SET state = 'expired', last_error = ? WHERE id = ?", 'Perdeu a validade antes do envio.', row.id);
      await expiredHandlers.get(row.kind)?.(payload);
      continue;
    }
    const processor = processors.get(row.kind);
    if (!processor) continue;
    try {
      await processor(payload, row);
      await db.runAsync('DELETE FROM outbox WHERE id = ?', row.id);
    } catch (error) {
      const message = error instanceof Error ? error.message : String(error);
      if (error instanceof GatewayError && (error.retryable || error.kind === 'unauthorized' || error.kind === 'not_paired')) {
        await db.runAsync('UPDATE outbox SET attempts = attempts + 1, last_error = ? WHERE id = ?', message, row.id);
        return false; // keep order: stop and retry later
      }
      log.warn('sync', `${row.kind} recusado: ${message}`);
      await db.runAsync("UPDATE outbox SET state = 'failed', attempts = attempts + 1, last_error = ? WHERE id = ?", message, row.id);
    }
  }
  return true;
}

let current: Promise<void> | null = null;

export function syncNow(reason: string): Promise<void> {
  if (current) return current;
  if (useConnectivity.getState().gateway !== 'online') return Promise.resolve();
  current = (async () => {
    useSync.setState({ running: true });
    try {
      const flushed = await flush();
      if (flushed) {
        for (const [name, puller] of pullers) {
          try {
            await puller();
          } catch (error) {
            log.warn('sync', `pull ${name}: ${error instanceof Error ? error.message : String(error)}`);
          }
        }
      }
      useSync.setState({ lastSyncAt: nowIso(), lastError: null });
    } catch (error) {
      useSync.setState({ lastError: error instanceof Error ? error.message : String(error) });
      log.error('sync', `falha (${reason})`, error);
    } finally {
      useSync.setState({ running: false });
      await countPending();
      current = null;
    }
  })();
  return current;
}
