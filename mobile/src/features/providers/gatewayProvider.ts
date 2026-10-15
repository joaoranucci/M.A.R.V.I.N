import { onEvent } from '../../core/events/eventStream';
import { log } from '../../core/logging/logger';
import { settings } from '../../core/settings';
import { gateway } from '../gateway/api';
import { GatewayError } from '../gateway/client';
import type { AssistantProvider, ProviderReply } from './types';

const FINAL = new Set(['completed', 'failed', 'cancelled', 'waiting_user', 'needs_reconciliation']);
type Waiter = { resolve: (reply: ProviderReply) => void; progress?: (message: string) => void };
const waiters = new Map<string, Waiter>();

onEvent('assistant.answer', (event) => {
  const data = event.data as { task_id?: string; text?: string; state?: string; engine?: string };
  if (!data.task_id) return;
  const waiter = waiters.get(data.task_id);
  if (!waiter) return;
  waiters.delete(data.task_id);
  waiter.resolve({ text: data.text ?? '', state: (data.state as ProviderReply['state']) ?? 'completed', taskId: data.task_id, engine: data.engine });
});

onEvent('assistant.progress', (event) => {
  const data = event.data as { task_id?: string; message?: string; tool?: string };
  if (!data.task_id) return;
  const waiter = waiters.get(data.task_id);
  if (waiter?.progress) waiter.progress(data.message ?? (data.tool ? 'Executando uma ação no PC' : 'Processando'));
});

const sleep = (ms: number) => new Promise((resolve) => setTimeout(resolve, ms));

/** Fallback when the event stream is down: long-poll the task until it is final. */
async function pollTask(taskId: string, signal: AbortSignal): Promise<ProviderReply | null> {
  await sleep(3000);
  while (!signal.aborted && waiters.has(taskId)) {
    try {
      const task = await gateway.task(taskId, 20, signal);
      if (FINAL.has(task.state)) {
        return { text: task.answer ?? '', state: task.state as ProviderReply['state'], taskId, engine: task.engine };
      }
    } catch (error) {
      if (error instanceof GatewayError && error.kind === 'aborted') return null;
      await sleep(2000);
    }
  }
  return null;
}

export const gatewayProvider: AssistantProvider = {
  id: 'gateway',
  label: 'MARVIN do PC',
  async send(request) {
    const accepted = await gateway.sendMessage({ client_id: request.clientId, text: request.text, engine: settings().engine, source: request.source });
    request.onQueued?.(accepted.task_id);
    if (accepted.duplicate && FINAL.has(accepted.state)) {
      const task = await gateway.task(accepted.task_id);
      return { text: task.answer ?? '', state: task.state as ProviderReply['state'], taskId: task.id, engine: task.engine };
    }
    return new Promise<ProviderReply>((resolve, reject) => {
      const local = new AbortController();
      const settle = (reply: ProviderReply) => {
        waiters.delete(accepted.task_id);
        local.abort();
        resolve(reply);
      };
      waiters.set(accepted.task_id, { resolve: settle, progress: request.onProgress });
      request.signal.addEventListener('abort', () => {
        waiters.delete(accepted.task_id);
        local.abort();
        reject(new GatewayError('aborted', 'Cancelado.'));
      });
      pollTask(accepted.task_id, local.signal)
        .then((reply) => reply && settle(reply))
        .catch((error) => log.warn('assistant', `poll: ${error instanceof Error ? error.message : String(error)}`));
    });
  },
  async cancel(taskId) {
    await gateway.cancelTask(taskId);
  },
};
