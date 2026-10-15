import * as Network from 'expo-network';
import { create } from 'zustand';
import { gateway } from '../../features/gateway/api';
import { GatewayError } from '../../features/gateway/client';
import type { TCapabilities } from '../../features/gateway/schemas';
import { kvGet, kvSet } from '../db/database';
import { log } from '../logging/logger';
import { connectionInfo } from '../security/credentials';

export type GatewayState = 'unpaired' | 'checking' | 'online' | 'unreachable' | 'unauthorized';

export interface ConnectivityState {
  network: 'unknown' | 'offline' | 'online';
  internet: boolean | null;
  gateway: GatewayState;
  gatewayMessage: string | null;
  assistant: 'ok' | 'busy' | 'unavailable' | 'unknown';
  assistantReason: string | null;
  vault: 'ok' | 'unavailable' | 'unknown';
  vaultMessage: string | null;
  desktop: 'online' | 'offline' | 'unknown';
  desktopReason: string | null;
  capabilities: TCapabilities | null;
  lastOkAt: string | null;
  latencyMs: number | null;
}

const initial: ConnectivityState = {
  network: 'unknown',
  internet: null,
  gateway: 'unpaired',
  gatewayMessage: null,
  assistant: 'unknown',
  assistantReason: null,
  vault: 'unknown',
  vaultMessage: null,
  desktop: 'unknown',
  desktopReason: null,
  capabilities: null,
  lastOkAt: null,
  latencyMs: null,
};

export const useConnectivity = create<ConnectivityState>(() => initial);
const set = (patch: Partial<ConnectivityState>) => useConnectivity.setState(patch);
const CAPS_KEY = 'capabilities.v1';

let refreshing: Promise<void> | null = null;
let timer: ReturnType<typeof setInterval> | null = null;
let subscription: { remove(): void } | null = null;

function applyNetwork(state: Network.NetworkState) {
  set({
    network: state.isConnected === false ? 'offline' : state.isConnected ? 'online' : 'unknown',
    internet: state.isInternetReachable ?? null,
  });
}

async function loadCachedCapabilities() {
  const raw = await kvGet(CAPS_KEY);
  if (raw && !useConnectivity.getState().capabilities) {
    try {
      set({ capabilities: JSON.parse(raw) as TCapabilities });
    } catch {
      // Cached copy is only a convenience for offline display.
    }
  }
}

export async function refreshCapabilities(): Promise<TCapabilities | null> {
  try {
    const caps = await gateway.capabilities();
    set({ capabilities: caps });
    await kvSet(CAPS_KEY, JSON.stringify(caps));
    return caps;
  } catch (error) {
    log.warn('connectivity', `capacidades indisponíveis: ${error instanceof Error ? error.message : String(error)}`);
    return useConnectivity.getState().capabilities;
  }
}

async function doRefresh(): Promise<void> {
  try {
    applyNetwork(await Network.getNetworkStateAsync());
  } catch {
    // Keep the previous network state.
  }
  if (!connectionInfo().connection) {
    set({ gateway: 'unpaired', gatewayMessage: null, assistant: 'unknown', vault: 'unknown', desktop: 'unknown' });
    return;
  }
  const previous = useConnectivity.getState().gateway;
  if (useConnectivity.getState().network === 'offline') {
    set({ gateway: 'unreachable', gatewayMessage: 'Sem rede no celular.', desktop: 'unknown', vault: 'unknown', assistant: 'unknown' });
    return;
  }
  if (previous !== 'online') set({ gateway: 'checking' });
  const started = Date.now();
  try {
    const status = await gateway.status();
    set({
      gateway: 'online',
      gatewayMessage: null,
      latencyMs: Date.now() - started,
      lastOkAt: new Date().toISOString(),
      assistant: status.assistant.state === 'busy' ? 'busy' : status.assistant.state === 'ok' ? 'ok' : 'unavailable',
      assistantReason: status.assistant.reason ?? null,
      vault: status.vault.state === 'ok' ? 'ok' : 'unavailable',
      vaultMessage: status.vault.message ?? null,
      desktop: status.desktop_agent.state === 'online' ? 'online' : 'offline',
      desktopReason: status.desktop_agent.reason ?? null,
    });
    if (previous !== 'online' || !useConnectivity.getState().capabilities) await refreshCapabilities();
  } catch (error) {
    if (error instanceof GatewayError && error.kind === 'unauthorized') {
      set({ gateway: 'unauthorized', gatewayMessage: 'Este celular foi desvinculado no computador. Vincule novamente.' });
    } else {
      set({
        gateway: 'unreachable',
        gatewayMessage: error instanceof Error ? error.message : 'Servidor indisponível.',
        desktop: 'unknown',
        vault: 'unknown',
        assistant: 'unknown',
      });
    }
  }
}

export function refreshConnectivity(): Promise<void> {
  if (!refreshing) refreshing = doRefresh().finally(() => (refreshing = null));
  return refreshing;
}

export function startConnectivity(): void {
  void loadCachedCapabilities();
  subscription?.remove();
  subscription = Network.addNetworkStateListener((state) => {
    const before = useConnectivity.getState().network;
    applyNetwork(state);
    if (before !== useConnectivity.getState().network) void refreshConnectivity();
  });
  if (timer) clearInterval(timer);
  timer = setInterval(() => void refreshConnectivity(), 20000);
  void refreshConnectivity();
}

export function stopConnectivity(): void {
  subscription?.remove();
  subscription = null;
  if (timer) clearInterval(timer);
  timer = null;
}

/** Mark the gateway unreachable from any failed request, without waiting for the next poll. */
export function reportGatewayFailure(error: unknown): void {
  if (error instanceof GatewayError) {
    if (error.kind === 'unauthorized') set({ gateway: 'unauthorized', gatewayMessage: 'Acesso revogado. Vincule novamente.' });
    else if (error.kind === 'network' || error.kind === 'timeout') set({ gateway: 'unreachable', gatewayMessage: error.message });
  }
}

export interface Availability {
  label: string;
  tone: 'ok' | 'warn' | 'off';
  detail: string;
  works: string[];
  unavailable: string[];
}

/** Human summary distinguishing no network, server down and PC agent offline. */
export function describeAvailability(state: ConnectivityState, demo: boolean): Availability {
  const local = ['Memórias e notas salvas no celular', 'Tarefas e lembretes locais', 'Histórico já sincronizado'];
  if (demo) return { label: 'Modo demonstração', tone: 'warn', detail: 'Respostas simuladas; nada é executado.', works: local, unavailable: [] };
  if (state.gateway === 'unpaired') {
    return { label: 'Nenhum computador vinculado', tone: 'off', detail: 'Vincule o MARVIN do PC para conversar.', works: local, unavailable: ['Conversa com o MARVIN', 'Biblioteca', 'Ações no computador'] };
  }
  if (state.network === 'offline') {
    return { label: 'Sem rede', tone: 'off', detail: 'O celular está sem Wi-Fi/dados.', works: local, unavailable: ['Conversa', 'Sincronização', 'Biblioteca', 'Ações no PC'] };
  }
  if (state.gateway === 'unauthorized') {
    return { label: 'Acesso revogado', tone: 'off', detail: state.gatewayMessage ?? '', works: local, unavailable: ['Tudo que depende do PC'] };
  }
  if (state.gateway === 'unreachable') {
    return { label: 'Servidor MARVIN indisponível', tone: 'off', detail: 'O PC não respondeu: está ligado, na mesma rede/VPN e com o gateway aberto?', works: local, unavailable: ['Conversa', 'Sincronização', 'Biblioteca', 'Ações no PC'] };
  }
  if (state.gateway === 'checking') return { label: 'Conectando…', tone: 'warn', detail: '', works: local, unavailable: [] };
  const unavailable: string[] = [];
  if (state.desktop !== 'online') unavailable.push('Ações no computador');
  if (state.vault !== 'ok') unavailable.push('Memórias no cofre e biblioteca');
  if (state.assistant === 'unavailable') unavailable.push('Conversa');
  const works = ['Conversa com o MARVIN do PC', ...local];
  if (state.desktop !== 'online') {
    return { label: 'Computador desconectado', tone: 'warn', detail: state.desktopReason ?? 'Servidor ativo, mas o agente do PC não está.', works, unavailable };
  }
  if (state.vault !== 'ok') {
    return { label: 'PC conectado · cofre fechado', tone: 'warn', detail: state.vaultMessage ?? '', works, unavailable };
  }
  return { label: 'PC conectado', tone: 'ok', detail: state.latencyMs != null ? `${state.latencyMs} ms` : '', works: [...works, 'Biblioteca', 'Ações no PC'], unavailable };
}
