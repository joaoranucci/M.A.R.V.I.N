import type { WearableAdapter, WearableEvent, WearableKind } from './types';

/**
 * Demonstration-only adapter. It exercises the event path (link, battery, trigger)
 * without any radio, and is always labeled "simulado" in the interface.
 */
export function createSimulatedWearable(kind: WearableKind): WearableAdapter & { emit(event: WearableEvent): void } {
  const listeners = new Set<(event: WearableEvent) => void>();
  const emit = (event: WearableEvent) => listeners.forEach((l) => l(event));
  return {
    id: `sim-${kind}`,
    kind,
    simulated: true,
    emit,
    command: {
      kind,
      label: kind === 'bracelet' ? 'Pulseira (simulada)' : 'Óculos (simulados)',
      async connect() {
        emit({ type: 'link', source: kind, state: 'connected' });
        emit({ type: 'battery', source: kind, level: 0.8, charging: false });
      },
      async disconnect() {
        emit({ type: 'link', source: kind, state: 'disconnected' });
      },
      async send(message) {
        return { id: message.id, ok: true };
      },
      onEvent(listener) {
        listeners.add(listener);
        return () => listeners.delete(listener);
      },
    },
  };
}
