// QR/deep-link contract produced by python -m marvin.gateway pair.
export interface PairingPayload {
  host: string;
  port: number;
  code: string;
  pin: string;
  serverName: string;
  serverId: string;
}

export function validHost(host: string): boolean {
  const value = host.trim();
  if (!value || value.length > 253 || /[\s/?#@\\%]/.test(value)) return false;
  try {
    const literal = value.includes(':') && !value.startsWith('[') ? '[' + value + ']' : value;
    const url = new URL('https://' + literal + ':8770');
    const normalized = url.hostname.toLowerCase();
    return !['localhost', '[::1]', '0.0.0.0', '[::]'].includes(normalized) && !normalized.startsWith('127.');
  } catch { return false; }
}

export function parsePairingUrl(raw: string): PairingPayload | null {
  if (typeof raw !== 'string' || raw.length > 4096) return null;
  const value = raw.trim();
  const prefix = 'marvin://pair?';
  if (!value.startsWith(prefix) || /[\r\n#]/.test(value)) return null;
  const params: Record<string, string> = Object.create(null);
  try {
    for (const part of value.slice(prefix.length).split('&')) {
      const split = part.indexOf('=');
      if (split < 1) return null;
      const key = decodeURIComponent(part.slice(0, split));
      if (Object.hasOwn(params, key)) return null;
      const encoded = part.slice(split + 1);
      // A raw '+' is part of base64 SPKI, not a form-encoded space.
      params[key] = decodeURIComponent(key === 'k' ? encoded : encoded.replace(/\+/g, ' '));
    }
  } catch { return null; }
  const port = Number(params.p);
  if (params.v !== '1' || !params.h || params.h !== params.h.trim() || !validHost(params.h)) return null;
  if (!/^[0-9]{1,5}$/.test(params.p ?? '') || !Number.isInteger(port) || port < 1 || port > 65535) return null;
  if (!/^\d{6}$/.test(params.c ?? '') || !/^[A-Za-z0-9+/]{43}=$/.test(params.k ?? '')) return null;
  if ((params.n?.length ?? 0) > 120 || (params.s?.length ?? 0) > 128) return null;
  return { host: params.h, port, code: params.c, pin: params.k, serverName: params.n ?? 'PC', serverId: params.s ?? '' };
}

/** Runs before Expo Router parses URL query strings, both on cold and warm launches. */
export function normalizePairingLink(path: string): string {
  try {
    if (path.startsWith('marvin://pair')) {
      return parsePairingUrl(path) ? '/pair?payload=' + encodeURIComponent(path) : '/pair?invalid=1';
    }
    const relative = path.startsWith('pair?') ? '/' + path : path;
    if (relative.startsWith('/pair?') && !/(?:[?&])payload=/.test(relative)) {
      const original = 'marvin:/' + relative;
      return parsePairingUrl(original) ? '/pair?payload=' + encodeURIComponent(original) : '/pair?invalid=1';
    }
    return relative;
  } catch { return '/pair?invalid=1'; }
}
