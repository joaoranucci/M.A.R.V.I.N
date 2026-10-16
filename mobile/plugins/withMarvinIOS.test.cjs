const assert = require('node:assert/strict');
const test = require('node:test');
const { applyIOSInfoPlist } = require('./withMarvinIOS.js');
const { expo } = require('../app.json');

test('CNG produces all privacy descriptions even after camera removes microphone access text', () => {
  const plist = applyIOSInfoPlist({ NSCameraUsageDescription: 'camera', CFBundleDisplayName: 'MARVIN' });
  for (const key of ['NSCameraUsageDescription', 'NSMicrophoneUsageDescription', 'NSSpeechRecognitionUsageDescription', 'NSLocalNetworkUsageDescription']) {
    assert.ok(typeof plist[key] === 'string' && plist[key].length > 30, key);
  }
  assert.equal(plist.CFBundleDisplayName, 'MARVIN');
  assert.deepEqual(applyIOSInfoPlist(plist), plist);
  assert.equal(plist.NSAppTransportSecurity.NSAllowsArbitraryLoads, false);
  assert.equal(plist.NSAppTransportSecurity.NSAllowsLocalNetworking, true);
  assert.equal(plist.UIBackgroundModes, undefined);
  assert.equal(plist.NSBonjourServices, undefined);
});

test('app identity, scheme and last-plugin permission precedence remain stable', () => {
  assert.equal(expo.ios.bundleIdentifier, 'dev.marvin.mobile');
  assert.equal(expo.android.package, 'dev.marvin.mobile');
  assert.equal(expo.scheme, 'marvin');
  assert.equal(expo.plugins.at(-1), './plugins/withMarvinIOS.js');
});
