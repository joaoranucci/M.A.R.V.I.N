import assert from 'node:assert/strict';
import test from 'node:test';
import { normalizePairingLink, parsePairingUrl, validHost } from './pairing.ts';

const pin = '+/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=';
const link = 'marvin://pair?v=1&h=192.168.1.12&p=8770&c=123456&k=' + pin + '&n=Meu+PC&s=pc-1';

test('SPKI base64 survives raw plus, slash, padding and encoded URLs', () => {
  assert.equal(pin.length, 44);
  assert.equal(parsePairingUrl(link)?.pin, pin);
  assert.equal(parsePairingUrl(link.replace(pin, encodeURIComponent(pin)))?.pin, pin);
  assert.equal(parsePairingUrl(link)?.serverName, 'Meu PC');
});

test('malformed or ambiguous pairing links are data errors, never startup exceptions', () => {
  for (const raw of [
    link + '&k=' + pin, link + '&h=outro', link.replace('pc-1', '%E0%A4%A'),
    link.replace('8770', '0'), link.replace('8770', '65536'), link.replace('8770', '8e3'),
    link.replace('192.168.1.12', 'pc%40evil'), link.replace('192.168.1.12', 'localhost'),
    link.replace('123456', '12345'), link.replace('v=1', 'v=2'), link + '#fragment',
    link.replace('marvin:', 'https:'), link.replace('pair?', 'pair/usuario?'),
  ]) assert.equal(parsePairingUrl(raw), null, raw);
});

test('cold and warm native routing preserve the complete payload until confirmation', () => {
  for (const initial of [true, false]) {
    const path = normalizePairingLink(link);
    assert.equal(path, '/pair?payload=' + encodeURIComponent(link), String(initial));
    const payload = new URL(path, 'https://router.invalid').searchParams.get('payload');
    assert.equal(parsePairingUrl(payload!)?.pin, pin);
    assert.equal(normalizePairingLink(path), path);
  }
  assert.equal(normalizePairingLink('/pair?' + link.split('?')[1]), '/pair?payload=' + encodeURIComponent(link));
  assert.equal(normalizePairingLink('marvin://pair?k=%broken'), '/pair?invalid=1');
  assert.equal(normalizePairingLink('/settings/voice'), '/settings/voice');
});

test('manual hosts accept LAN/VPN/IPv6 and reject authority injection and loopback', () => {
  for (const host of ['192.168.1.12', 'pc.local', '100.65.1.2', 'fd00::123', '[fd00::123]']) assert.equal(validHost(host), true, host);
  for (const host of ['localhost', '127.0.0.1', '::1', 'pc/arquivo', 'pc@evil', 'pc\\evil', 'pc%2Fevil', 'https://pc', 'pc:8770']) assert.equal(validHost(host), false, host);
});
