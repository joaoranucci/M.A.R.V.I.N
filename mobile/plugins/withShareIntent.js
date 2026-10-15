// Registers MARVIN in the Android share sheet for the formats the Vault library accepts.
// The native module (modules/marvin-native) copies received files into the app cache.
const { withAndroidManifest, AndroidConfig } = require('expo/config-plugins');

const MIME_TYPES = [
  'text/*',
  'application/pdf',
  'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
  'application/json',
  'application/xml',
  'application/x-yaml',
  'application/octet-stream',
];

function filter(action) {
  return {
    action: [{ $: { 'android:name': action } }],
    category: [{ $: { 'android:name': 'android.intent.category.DEFAULT' } }],
    data: MIME_TYPES.map((mimeType) => ({ $: { 'android:mimeType': mimeType } })),
  };
}

module.exports = function withShareIntent(config) {
  return withAndroidManifest(config, (mod) => {
    const activity = AndroidConfig.Manifest.getMainActivityOrThrow(mod.modResults);
    const filters = activity['intent-filter'] || [];
    const has = (action) => filters.some((f) => (f.action || []).some((a) => a.$['android:name'] === action));
    for (const action of ['android.intent.action.SEND', 'android.intent.action.SEND_MULTIPLE']) {
      if (!has(action)) filters.push(filter(action));
    }
    activity['intent-filter'] = filters;
    return mod;
  });
};
