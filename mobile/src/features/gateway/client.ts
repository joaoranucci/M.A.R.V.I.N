import type { z } from 'zod';
import { connectionInfo } from '../../core/security/credentials';
import { log } from '../../core/logging/logger';
import { ErrorEnvelope } from './schemas';
import { transport } from './transport';
import { gatewayUrl } from './transport/policy';
import type { GatewayUpload, TransportResponse } from './transport/types';

/**
 * One contract and error model over two native, pinned transports.
 * Tokens, request bodies and search queries never reach logs.
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
  upload?: GatewayUpload;
  schema?: z.ZodType<T>;
  timeoutMs?: number;
  auth?: boolean;
  headers?: Record<string, string>;
  signal?: AbortSignal;
  binary?: boolean;
  base?: { host: string; port: number; pin: string };
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
  const { method = 'GET', body, upload, schema, timeoutMs = 15000, auth = true, headers = {}, signal, binary } = options;
  const { connection, token } = connectionInfo();
  const target = options.base ?? connection;
  if (!target || (auth && !token)) throw new GatewayError('not_paired', 'Nenhum computador vinculado.');
  if (auth && options.base && (!connection || target.host !== connection.host || target.port !== connection.port || target.pin !== connection.pin)) {
    throw new GatewayError('not_paired', 'Destino diferente do computador vinculado.');
  }
  if (signal?.aborted) throw new GatewayError('aborted', 'Cancelado.');
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);
  const onAbort = () => controller.abort();
  signal?.addEventListener('abort', onAbort, { once: true });
  const finalHeaders: Record<string, string> = { Accept: binary ? '*/*' : 'application/json', ...headers };
  if (auth) finalHeaders.Authorization = 'Bearer ' + token;
  let payload: string | undefined;
  if (body !== undefined) {
    payload = JSON.stringify(body);
    finalHeaders['Content-Type'] = 'application/json';
  }
  let response: TransportResponse;
  let text = '';
  const logPath = path.split('?')[0];
  try {
    response = await transport({
      url: gatewayUrl(target.host, target.port, path), pin: target.pin, method,
      headers: finalHeaders, body: payload, upload, binary, timeoutMs, signal: controller.signal,
    });
    // The timeout covers the complete response, including uploads and long polling.
    if (binary && response.ok) return (await response.arrayBuffer()) as T;
    text = await response.text();
  } catch {
    if (signal?.aborted) throw new GatewayError('aborted', 'Cancelado.');
    if (controller.signal.aborted) throw new GatewayError('timeout', 'O computador demorou demais para responder.');
    log.warn('gateway', method + ' ' + logPath + ' falhou no transporte seguro.');
    throw new GatewayError('network', 'Não consegui conectar com segurança. Confira rede, permissão de rede local, endereço e certificado do PC.');
  } finally {
    clearTimeout(timer);
    signal?.removeEventListener('abort', onAbort);
  }
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
    log.warn('gateway', `${method} ${logPath} → ${response.status} ${code}`);
    if (response.status === 401) throw new GatewayError('unauthorized', message, 401, code);
    const { code: _c, message: _m, ...extra } = parsed.success ? parsed.data.error : { code: '', message: '' };
    throw new GatewayError('http', message, response.status, code, extra as Record<string, unknown>);
  }
  if (!schema) return json as T;
  const result = schema.safeParse(json);
  if (!result.success) {
    log.error('gateway', `${method} ${logPath} resposta fora do contrato: ${result.error.issues[0]?.path.join('.')}`);
    throw new GatewayError('invalid_response', 'O computador respondeu em um formato inesperado. Atualize o MARVIN do PC.');
  }
  return result.data;
}
