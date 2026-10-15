import { newId } from '../../core/ids';
import { log } from '../../core/logging/logger';
import { useConnectivity } from '../../core/net/connectivity';
import { settings } from '../../core/settings';
import { enqueue, registerProcessor, registerPuller } from '../../core/sync/syncEngine';
import { onEvent } from '../../core/events/eventStream';
import { getActivity, loadActivities, upsertActivity } from '../activities/repo';
import { gateway } from '../gateway/api';
import { GatewayError, serverNow } from '../gateway/client';
import { DesktopCommand, type TDesktopCommand } from '../gateway/schemas';

/**
 * Structured PC commands: client-generated id (dedup), expiry in server time,
 * explicit confirmation for destructive actions, lifecycle mirrored from the PC.
 */
export const COMMAND_TTL_SECONDS = 60;
export const OFFLINE_TTL_SECONDS = 300;

export interface CommandRequest {
  action: string;
  params: Record<string, string>;
  summary: string;
}

export interface CommandOutcome {
  state: string;
  message: string;
  commandId: string;
  needsConfirmation?: { title: string; description: string; risk: string };
}

const listeners = new Set<(command: TDesktopCommand) => void>();
export function onCommandUpdate(listener: (command: TDesktopCommand) => void): () => void {
  listeners.add(listener);
  return () => listeners.delete(listener);
}

export function actionInfo(actionId: string) {
  return useConnectivity.getState().capabilities?.desktop.actions.find((a) => a.id === actionId) ?? null;
}

/** True when the UI must show a preview and ask before sending. */
export function needsPreview(actionId: string): boolean {
  const info = actionInfo(actionId);
  if (info?.requires_confirmation || ['lock_screen', 'shutdown'].includes(actionId)) return true;
  return settings().confirmCommonDesktopActions;
}

async function mirror(record: TDesktopCommand, summary?: string) {
  const existing = await getActivity(record.command_id);
  await upsertActivity({
    id: record.command_id,
    kind: 'desktop',
    title: summary ?? existing?.title ?? actionInfo(record.action)?.label ?? record.action,
    state: record.state,
    detail: record.message,
    ref: record.action,
    payload: JSON.stringify({ verified: record.verified, result: record.result ?? null, expires_at: record.expires_at }),
  });
  for (const listener of listeners) listener(record);
}

export async function sendCommand(request: CommandRequest, confirmed: boolean, commandId = newId()): Promise<CommandOutcome> {
  if (settings().demoMode) {
    await upsertActivity({ id: commandId, kind: 'desktop', title: request.summary, state: 'simulated', detail: 'Modo demonstração: nenhuma ação foi enviada ao computador.', ref: request.action });
    return { state: 'simulated', message: 'Demonstração: nada foi executado no computador.', commandId };
  }
  const expiresAt = new Date(serverNow().getTime() + COMMAND_TTL_SECONDS * 1000).toISOString();
  await upsertActivity({ id: commandId, kind: 'desktop', title: request.summary, state: 'sending', detail: null, ref: request.action });
  try {
    const record = await gateway.sendCommand({ command_id: commandId, action: request.action, params: request.params, expires_at: expiresAt, confirmed });
    await mirror(record, request.summary);
    return { state: record.state, message: record.message, commandId };
  } catch (error) {
    if (error instanceof GatewayError && error.status === 428) {
      const preview = (error.extra.preview as CommandOutcome['needsConfirmation']) ?? { title: request.summary, description: '', risk: 'destructive' };
      await upsertActivity({ id: commandId, kind: 'desktop', title: request.summary, state: 'awaiting_confirmation', detail: preview?.description ?? null });
      return { state: 'awaiting_confirmation', message: error.message, commandId, needsConfirmation: preview };
    }
    if (error instanceof GatewayError && error.status === 410) {
      await upsertActivity({ id: commandId, kind: 'desktop', title: request.summary, state: 'needs_decision', detail: error.message });
      return { state: 'needs_decision', message: error.message, commandId };
    }
    if (error instanceof GatewayError && error.retryable) {
      await upsertActivity({ id: commandId, kind: 'desktop', title: request.summary, state: 'failed', detail: 'Computador indisponível. Nada foi enviado.' });
      return { state: 'offline', message: 'O computador está indisponível. O comando não foi enviado.', commandId };
    }
    const message = error instanceof Error ? error.message : 'Falha ao enviar o comando.';
    await upsertActivity({ id: commandId, kind: 'desktop', title: request.summary, state: error instanceof GatewayError && error.status === 503 ? 'failed' : 'rejected', detail: message });
    return { state: 'rejected', message, commandId };
  }
}

/** User chose "enviar quando o PC voltar": kept for at most 5 minutes, then needs a new decision. */
export async function queueCommandUntilOnline(request: CommandRequest, confirmed: boolean): Promise<string> {
  const id = newId();
  const expiresAt = new Date(Date.now() + OFFLINE_TTL_SECONDS * 1000).toISOString();
  await upsertActivity({ id, kind: 'desktop', title: request.summary, state: 'queued_offline', detail: 'Será enviado se o PC voltar em até 5 minutos.', ref: request.action, payload: JSON.stringify({ request, confirmed }) });
  await enqueue('desktop.command', { id, request, confirmed }, { id: `desktop-${id}`, expiresAt });
  return id;
}

export async function cancelCommand(commandId: string): Promise<void> {
  const record = await gateway.cancelCommand(commandId);
  await mirror(record);
}

registerProcessor(
  'desktop.command',
  async ({ id, request, confirmed }: { id: string; request: CommandRequest; confirmed: boolean }) => {
    const outcome = await sendCommand(request, confirmed, id);
    if (outcome.state === 'offline') throw new GatewayError('network', 'PC ainda indisponível.');
  },
  async ({ id, request }: { id: string; request: CommandRequest }) => {
    // Never executed late: the user must decide again.
    await upsertActivity({ id, kind: 'desktop', title: request.summary, state: 'needs_decision', detail: 'O PC não voltou a tempo. Confirme de novo se ainda quiser.', payload: JSON.stringify({ request }) });
  },
);

registerPuller('desktop-commands', async () => {
  if (settings().demoMode) return;
  const commands = await gateway.commands();
  for (const command of commands.slice(0, 40)) {
    const existing = await getActivity(command.command_id);
    if (!existing || existing.state !== command.state) await mirror(command);
  }
  await loadActivities();
});

onEvent('desktop.command', async (event) => {
  const parsed = DesktopCommand.safeParse(event.data);
  if (parsed.success) await mirror(parsed.data);
  else log.warn('desktop', 'evento de comando fora do contrato');
});
