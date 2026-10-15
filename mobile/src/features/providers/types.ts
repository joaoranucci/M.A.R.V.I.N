import type { Reference } from '../conversation/repo';

/**
 * AI provider adapters. `gateway` = MARVIN on the PC (with whatever model the PC is
 * configured for, local or external). `local` = deterministic rules, no model.
 * `demo` = explicitly labeled simulation. An on-device model is a future adapter:
 * it must not be advertised before one is installed and validated.
 */
export interface ProviderReply {
  text: string;
  state: 'completed' | 'failed' | 'cancelled' | 'waiting_user' | 'needs_reconciliation' | 'offline';
  taskId?: string;
  engine?: string;
  refs?: Reference[];
}

export interface ProviderRequest {
  clientId: string;
  text: string;
  source: 'voice' | 'text';
  signal: AbortSignal;
  onQueued?: (taskId: string) => void;
  onProgress?: (message: string) => void;
}

export interface AssistantProvider {
  id: 'gateway' | 'local' | 'demo';
  label: string;
  send(request: ProviderRequest): Promise<ProviderReply>;
  cancel?(taskId: string): Promise<void>;
}
