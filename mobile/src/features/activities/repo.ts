import { create } from 'zustand';
import { getDb } from '../../core/db/database';
import { nowIso } from '../../core/ids';
import { settings } from '../../core/settings';

/**
 * Persistent activity log so progress survives closing the app.
 * kind: assistant (AI processing), desktop (actions on the PC), upload (documents).
 */
export type ActivityKind = 'assistant' | 'desktop' | 'upload';

export interface Activity {
  id: string;
  kind: ActivityKind;
  title: string;
  state: string;
  detail: string | null;
  ref: string | null;
  created_at: string;
  updated_at: string;
  payload: string | null;
  demo: number;
}

export const useActivities = create<{ items: Activity[] }>(() => ({ items: [] }));

export async function loadActivities(): Promise<Activity[]> {
  const db = await getDb();
  const rows = await db.getAllAsync<Activity>(
    'SELECT * FROM activities WHERE demo = ? ORDER BY updated_at DESC LIMIT 200',
    settings().demoMode ? 1 : 0,
  );
  useActivities.setState({ items: rows });
  return rows;
}

export async function upsertActivity(activity: Partial<Activity> & { id: string; kind: ActivityKind }): Promise<void> {
  const db = await getDb();
  const existing = await db.getFirstAsync<Activity>('SELECT * FROM activities WHERE id = ?', activity.id);
  const now = nowIso();
  const merged: Activity = {
    title: '',
    state: 'received',
    detail: null,
    ref: null,
    payload: null,
    created_at: now,
    demo: settings().demoMode ? 1 : 0,
    ...existing,
    ...Object.fromEntries(Object.entries(activity).filter(([, v]) => v !== undefined)),
    updated_at: activity.updated_at ?? now,
  } as Activity;
  await db.runAsync(
    `INSERT INTO activities(id, kind, title, state, detail, ref, created_at, updated_at, payload, demo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
     ON CONFLICT(id) DO UPDATE SET title = excluded.title, state = excluded.state, detail = excluded.detail, ref = excluded.ref,
       updated_at = excluded.updated_at, payload = excluded.payload`,
    merged.id, merged.kind, merged.title, merged.state, merged.detail, merged.ref, merged.created_at, merged.updated_at, merged.payload, merged.demo,
  );
  await loadActivities();
}

export async function getActivity(id: string): Promise<Activity | null> {
  const db = await getDb();
  return db.getFirstAsync<Activity>('SELECT * FROM activities WHERE id = ?', id);
}

export const assistantStateLabel: Record<string, string> = {
  sending: 'Enviando',
  queued: 'Na fila do PC',
  started: 'Processando',
  running: 'Processando',
  paused: 'Pausada',
  pause_requested: 'Pausando',
  cancelling: 'Cancelando',
  completed: 'Concluída',
  failed: 'Falhou',
  cancelled: 'Cancelada',
  waiting_user: 'Aguardando você',
  needs_reconciliation: 'Resultado incerto',
  offline: 'Não enviada (sem conexão)',
};

export const desktopStateLabel: Record<string, string> = {
  sending: 'Enviando ao PC',
  queued_offline: 'Aguardando o PC (válido por pouco tempo)',
  received: 'Pedido recebido pelo PC',
  started: 'Execução iniciada',
  completed: 'Concluída e verificada',
  dispatched: 'Enviada ao Windows (sem confirmação visual)',
  failed: 'Falhou',
  expired: 'Perdeu a validade — nada foi executado',
  cancelled: 'Cancelada',
  rejected: 'Recusada pelo PC',
  needs_reconciliation: 'Resultado incerto — confira no PC',
  awaiting_confirmation: 'Aguardando sua confirmação',
  needs_decision: 'Precisa de nova decisão',
  simulated: 'Simulada (demonstração) — nada foi executado',
};

export const uploadStateLabel: Record<string, string> = {
  queued_offline: 'Aguardando conexão para enviar',
  uploading: 'Enviando',
  received: 'Enviado',
  processing: 'Em processamento',
  available: 'Disponível para consulta',
  failed: 'Falha',
};

export function isFinal(kind: ActivityKind, state: string): boolean {
  if (kind === 'upload') return state === 'available' || state === 'failed';
  if (kind === 'desktop') return ['completed', 'dispatched', 'failed', 'expired', 'cancelled', 'rejected', 'needs_reconciliation', 'needs_decision', 'simulated'].includes(state);
  return ['completed', 'failed', 'cancelled', 'waiting_user', 'needs_reconciliation', 'offline'].includes(state);
}
