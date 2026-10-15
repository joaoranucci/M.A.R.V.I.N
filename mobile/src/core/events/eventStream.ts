import { AppState, type AppStateStatus } from 'react-native';
import { gateway } from '../../features/gateway/api';
import { GatewayError } from '../../features/gateway/client';
import type { TGatewayEvent } from '../../features/gateway/schemas';
import { kvGet, kvSet } from '../db/database';
import { log } from '../logging/logger';
import { refreshConnectivity, reportGatewayFailure, useConnectivity } from '../net/connectivity';
import { connectionInfo } from '../security/credentials';

/**
 * Long-poll consumer. The cursor is persisted after handlers run, so an event is
 * processed at most once per seq; a gap reported by the server triggers a resync.
 */
type Handler = (event: TGatewayEvent) => void | Promise<void>;
type ResyncHandler = () => void | Promise<void>;

const handlers = new Map<string, Set<Handler>>();
const resyncHandlers = new Set<ResyncHandler>();
const CURSOR_KEY = 'events.cursor';
const WAIT_SECONDS = 25;

let running = false;
let controller: AbortController | null = null;
let cursor = 0;
let serverId: string | null = null;
let appState: AppStateStatus = AppState.currentState;

export function onEvent(type: string, handler: Handler): () => void {
  const set = handlers.get(type) ?? new Set();
  set.add(handler);
  handlers.set(type, set);
  return () => set.delete(handler);
}

export function onResync(handler: ResyncHandler): () => void {
  resyncHandlers.add(handler);
  return () => resyncHandlers.delete(handler);
}

async function dispatch(event: TGatewayEvent) {
  for (const handler of [...(handlers.get(event.type) ?? []), ...(handlers.get('*') ?? [])]) {
    try {
      await handler(event);
    } catch (error) {
      log.error('events', `handler ${event.type}`, error);
    }
  }
}

async function resync() {
  for (const handler of resyncHandlers) {
    try {
      await handler();
    } catch (error) {
      log.error('events', 'resync', error);
    }
  }
}

const sleep = (ms: number) => new Promise((resolve) => setTimeout(resolve, ms));

async function loop() {
  let backoff = 1000;
  while (running) {
    const connection = connectionInfo().connection;
    if (!connection || appState !== 'active') {
      await sleep(1000);
      continue;
    }
    if (serverId !== connection.serverId) {
      // Cursor belongs to one server; a different PC starts from scratch.
      serverId = connection.serverId;
      const stored = await kvGet(`${CURSOR_KEY}.${serverId}`);
      cursor = stored ? Number(stored) || 0 : 0;
      if (cursor === 0) await resync();
    }
    controller = new AbortController();
    try {
      const batch = await gateway.events(cursor, WAIT_SECONDS, controller.signal);
      backoff = 1000;
      if (useConnectivity.getState().gateway !== 'online') void refreshConnectivity();
      if (batch.reset) {
        log.warn('events', 'lacuna de eventos; ressincronizando');
        await resync();
        cursor = batch.last_seq;
      } else {
        for (const event of batch.events) {
          if (event.seq <= cursor) continue; // replay after reconnect
          await dispatch(event);
          cursor = event.seq;
        }
        cursor = Math.max(cursor, batch.last_seq);
      }
      await kvSet(`${CURSOR_KEY}.${serverId}`, String(cursor));
    } catch (error) {
      if (error instanceof GatewayError && error.kind === 'aborted') continue;
      reportGatewayFailure(error);
      if (error instanceof GatewayError && error.kind === 'unauthorized') {
        await sleep(15000);
        continue;
      }
      await sleep(backoff);
      backoff = Math.min(backoff * 2, 30000);
    } finally {
      controller = null;
    }
  }
}

export function startEventStream(): void {
  if (running) return;
  running = true;
  AppState.addEventListener('change', (next) => {
    const wasActive = appState === 'active';
    appState = next;
    if (wasActive && next !== 'active') controller?.abort();
  });
  void loop();
}

/** Called after pairing with another server or after wiping local data. */
export function resetEventCursor(): void {
  serverId = null;
  cursor = 0;
  controller?.abort();
}
