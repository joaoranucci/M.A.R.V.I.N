import { create } from 'zustand';
import { log } from '../../../core/logging/logger';
import type { LinkState, WearableAdapter, WearableEvent, WearableKind } from './types';

/**
 * Routes wearable events to the assistant. A "trigger" from the bracelet or glasses
 * starts listening exactly like a tap on the core. Battery/link are shown only when
 * the hardware actually reports them.
 */
interface WearableStatus {
  link: LinkState;
  battery: number | null;
  charging: boolean | null;
  simulated: boolean;
  lastEventAt: string | null;
}

interface HubState {
  devices: Partial<Record<WearableKind, WearableStatus>>;
}

export const useWearables = create<HubState>(() => ({ devices: {} }));

const adapters = new Map<string, WearableAdapter>();
const unsubscribers = new Map<string, () => void>();
let triggerHandler: ((source: WearableKind) => void) | null = null;

export function setWearableTrigger(handler: (source: WearableKind) => void) {
  triggerHandler = handler;
}

function update(kind: WearableKind, patch: Partial<WearableStatus>, simulated: boolean) {
  useWearables.setState((s) => ({
    devices: {
      ...s.devices,
      [kind]: { link: 'disconnected', battery: null, charging: null, simulated, ...s.devices[kind], ...patch, lastEventAt: new Date().toISOString() },
    },
  }));
}

export function handleWearableEvent(event: WearableEvent, simulated: boolean) {
  switch (event.type) {
    case 'trigger':
      log.info('wearable', `${event.source}: ${event.gesture}${simulated ? ' (simulado)' : ''}`);
      update(event.source, {}, simulated);
      triggerHandler?.(event.source);
      break;
    case 'link':
      update(event.source, { link: event.state }, simulated);
      break;
    case 'battery':
      update(event.source, { battery: event.level, charging: event.charging }, simulated);
      break;
    case 'capabilities':
      update(event.source, {}, simulated);
      break;
  }
}

export async function registerWearable(adapter: WearableAdapter) {
  adapters.set(adapter.id, adapter);
  unsubscribers.set(adapter.id, adapter.command.onEvent((event) => handleWearableEvent(event, adapter.simulated)));
  await adapter.command.connect();
}

export async function unregisterWearable(id: string) {
  const adapter = adapters.get(id);
  unsubscribers.get(id)?.();
  unsubscribers.delete(id);
  adapters.delete(id);
  if (adapter) {
    await adapter.command.disconnect();
    useWearables.setState((s) => {
      const devices = { ...s.devices };
      delete devices[adapter.kind];
      return { devices };
    });
  }
}

export function registeredWearables(): WearableAdapter[] {
  return [...adapters.values()];
}
