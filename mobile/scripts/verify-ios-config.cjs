const assert = require('node:assert/strict');
const fs = require('node:fs');
const { execFileSync } = require('node:child_process');

const path = process.argv[2] || 'ios/MARVIN/Info.plist';
const info = JSON.parse(execFileSync('plutil', ['-convert', 'json', '-o', '-', path], { encoding: 'utf8' }));
for (const key of ['NSMicrophoneUsageDescription', 'NSSpeechRecognitionUsageDescription', 'NSCameraUsageDescription', 'NSLocalNetworkUsageDescription']) {
  assert.ok(typeof info[key] === 'string' && info[key].length > 0, key);
}
assert.equal(info.NSAppTransportSecurity.NSAllowsArbitraryLoads, false);
assert.equal(info.NSAppTransportSecurity.NSAllowsLocalNetworking, true);
assert.ok(info.CFBundleURLTypes.some((item) => item.CFBundleURLSchemes.includes('marvin')));
assert.ok(fs.readFileSync('ios/Podfile.lock', 'utf8').includes('MarvinNative'), 'The Swift module must be autolinked.');
console.log('Generated iOS permissions, TLS policy, scheme and native pod verified.');
