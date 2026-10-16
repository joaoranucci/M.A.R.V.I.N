import assert from 'node:assert/strict';
import test from 'node:test';
import { decodeBase64, gatewayUrl, requirePin } from './policy.ts';

test('gateway destinations are HTTPS and stay inside the API namespace', () => {
  assert.equal(gatewayUrl('192.168.1.12', 8770, '/v1/events?after=1&wait=25'), 'https://192.168.1.12:8770/v1/events?after=1&wait=25');
  assert.equal(gatewayUrl('fd00::1', 8770, '/v1/health'), 'https://[fd00::1]:8770/v1/health');
  for (const host of ['user@evil', 'pc/path', 'pc\\path', 'pc%2fpath']) assert.throws(() => gatewayUrl(host, 8770, '/v1/health'));
  for (const port of [0, -1, 65536, 1.5]) assert.throws(() => gatewayUrl('pc.local', port, '/v1/health'));
  for (const path of ['https://evil/', '//evil/v1/', '/v2/health', '/v1/../secret', '/v1/%2e%2e/secret', '/v1/health#x', '/v1/health\r\nX: y']) {
    assert.throws(() => gatewayUrl('pc.local', 8770, path), path);
  }
});

test('missing pins fail closed and binary audio/document bytes survive the bridge', () => {
  assert.doesNotThrow(() => requirePin('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA='));
  for (const pin of ['', 'sha256/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=', 'x'.repeat(44)]) assert.throws(() => requirePin(pin));
  assert.deepEqual(Array.from(new Uint8Array(decodeBase64('AAECA/r7/P3+/w=='))), [0, 1, 2, 3, 250, 251, 252, 253, 254, 255]);
});
