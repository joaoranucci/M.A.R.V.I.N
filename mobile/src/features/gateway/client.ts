import type { z } from 'zod';
import { connectionInfo } from '../../core/security/credentials';
import { log } from '../../core/logging/logger';
import { ErrorEnvelope } from './schemas';

/**
 * Isolated HTTP adapter for the MARVIN Mobile Gateway.
 * Uses React Native's fetch, which goes through the OkHttp client with the pinned
 * gateway certificate (modules/marvin-native). Never logs tokens or bodies.
 */
export type GatewayErrorKind = 'not_paired' | 'network' | 'timeout' | 'unauthorized' | 'http' | 'invalid_response' | 'aborted';

export class GatewayError extends Error {
  constructor(
    readonly kind: GatewayErrorKind,
    message: string,
    readonly status = 0,
    readonly code = '',
    readonly extra: Record<string, unknown> = {},
  ) {
    super(message);
  }
  get retryable(): boolean {
    return this.kind === 'network' || this.kind === 'timeout' || (this.kind === 'http' && this.status >= 502);
  }
}

interface RequestOptions<T> {
  method?: 'GET' | 'POST' | 'PUT' | 'DELETE';
  body?: unknown;
  form?: FormData;
  schema?: z.ZodType<T>;
  timeoutMs?: number;
  auth?: boolean;
  headers?: Record<string, string>;
  signal?: AbortSignal;
  binary?: boolean;
  base?: { host: string; port: number };
}

let clockOffsetMs = 0;

/** Server time estimate, used to compute command expiry in the server's clock. */
export const serverNow = (): Date => new Date(Date.now() + clockOffsetMs);

export function noteServerTime(serverTime: string, requestStarted: number): void {
  const parsed = Date.parse(serverTime);
  if (!Number.isNaN(parsed)) {
    const midpoint = (requestStarted + Date.now()) / 2;
    clockOffsetMs = parsed - midpoint;
  }
}

export function baseUrl(host: string, port: number): string {
  const literal = host.includes(':') && !host.startsWith('[') ? `[${host}]` : host;
  return `https://${literal}:${port}`;
}

export async function request<T = unknown>(path: string, options: RequestOptions<T> = {}): Promise<T> {
  const { method = 'GET', body, form, schema, timeoutMs = 15000, auth = true, headers = {}, signal, binary } = options;
  const { connection, token } = connectionInfo();
  const target = options.base ?? connection;
  if (!target) throw new GatewayError('not_paired', 'Nenhum computador vinculado.');
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);
  const onAbort = () => controller.abort();
  signal?.addEventListener('abort', onAbort);
  const finalHeaders: Record<string, string> = { Accept: binary ? '*/*' : 'application/json', ...headers };
  if (auth) {
    if (!token) throw new GatewayError('not_paired', 'Nenhum computador vinculado.');
    finalHeaders.Authorization = `Bearer ${token}`;
  }
  let payload: string | FormData | undefined;
  if (form) payload = form;
  else if (body !== undefined) {
    payload = JSON.stringify(body);
    finalHeaders['Content-Type'] = 'application/json';
  }
  let response: Response;
  try {
    response = await fetch(baseUrl(target.host, target.port) + path, {
      method,
      headers: finalHeaders,
      body: payload,
      signal: controller.signal,
    });
  } catch (error) {
    if (signal?.aborted) throw new GatewayError('aborted', 'Cancelado.');
    if (controller.signal.aborted) throw new GatewayError('timeout', 'O computador demorou demais para responder.');
    log.warn('gateway', `${method} ${path} falhou na rede: ${error instanceof Error ? error.message : String(error)}`);
    throw new GatewayError('network', 'Não consegui alcançar o computador. Confira a rede ou a VPN.');
  } finally {
    clearTimeout(timer);
    signal?.removeEventListener('abort', onAbort);
  }
  if (binary && response.ok) return (await response.arrayBuffer()) as T;
  const text = await response.text();
  let json: unknown = undefined;
  if (text) {
    try {
      json = JSON.parse(text);
    } catch {
      throw new GatewayError('invalid_response', 'Resposta inválida do computador.', response.status);
    }
  }
  if (!response.ok) {
    const parsed = ErrorEnvelope.safeParse(json);
    const code = parsed.success ? parsed.data.error.code : '';
    const message = parsed.success ? parsed.data.error.message : `Falha no computador (HTTP ${response.status}).`;
    log.warn('gateway', `${method} ${path} → ${response.status} ${code}`);
    if (response.status === 401) throw new GatewayError('unauthorized', message, 401, code);
    const { code: _c, message: _m, ...extra } = parsed.success ? parsed.data.error : { code: '', message: '' };
    throw new GatewayError('http', message, response.status, code, extra as Record<string, unknown>);
  }
  if (!schema) return json as T;
  const result = schema.safeParse(json);
  if (!result.success) {
    log.error('gateway', `${method} ${path} resposta fora do contrato: ${result.error.issues[0]?.path.join('.')}`);
    throw new GatewayError('invalid_response', 'O computador respondeu em um formato inesperado. Atualize o MARVIN do PC.');
  }
  return result.data;
}
