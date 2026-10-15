// Parses the QR payload produced by `python -m marvin.gateway pair`.
export interface PairingPayload {
  host: string;
  port: number;
  code: string;
  pin: string;
  serverName: string;
  serverId: string;
}

export function parsePairingUrl(raw: string): PairingPayload | null {
  const value = raw.trim();
  if (!value.startsWith('marvin://pair?')) return null;
  const params: Record<string, string> = {};
  for (const part of value.slice('marvin://pair?'.length).split('&')) {
    const [key, ...rest] = part.split('=');
    if (key) params[key] = decodeURIComponent(rest.join('=').replace(/\+/g, ' '));
  }
  const port = Number(params.p);
  if (params.v !== '1' || !params.h || !Number.isInteger(port) || port < 1 || port > 65535) return null;
  if (!/^\d{6}$/.test(params.c ?? '') || !/^[A-Za-z0-9+/]{43}=$/.test(params.k ?? '')) return null;
  if (/[\s/?#@]/.test(params.h)) return null;
  return { host: params.h, port, code: params.c, pin: params.k, serverName: params.n ?? 'PC', serverId: params.s ?? '' };
}

export function validHost(host: string): boolean {
  const value = host.trim();
  if (!value || value.length > 253 || /[\s/?#@]/.test(value)) return false;
  return value !== 'localhost' && !value.startsWith('127.');
}
