/** Shared, fail-closed URL policy. No token can be sent to a URL supplied by a deep link. */
export function gatewayUrl(host: string, port: number, path: string): string {
  if (!host || host.length > 253 || /[\s/?#@\\%]/.test(host)) throw new Error('Endereço do gateway inválido.');
  if (!Number.isInteger(port) || port < 1 || port > 65535) throw new Error('Porta inválida.');
  if (!path.startsWith('/v1/') || /[\r\n\\#]/.test(path) || /(?:^|\/)\.{1,2}(?:\/|[?]|$)/.test(path)) {
    throw new Error('Rota do gateway inválida.');
  }
  const literal = host.includes(':') && !host.startsWith('[') ? '[' + host + ']' : host;
  const value = new URL('https://' + literal + ':' + port + path);
  if (value.protocol !== 'https:' || value.username || value.password || !value.pathname.startsWith('/v1/')) throw new Error('Gateway requer HTTPS.');
  return value.toString();
}

export function requirePin(pin: string): void {
  if (!/^[A-Za-z0-9+/]{43}=$/.test(pin)) throw new Error('Impressão digital inválida. Vincule novamente pelo PC.');
}

export function decodeBase64(value: string): ArrayBuffer {
  const raw = atob(value);
  const bytes = new Uint8Array(raw.length);
  for (let i = 0; i < raw.length; i++) bytes[i] = raw.charCodeAt(i);
  return bytes.buffer;
}
