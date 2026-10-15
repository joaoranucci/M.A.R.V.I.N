import * as Speech from 'expo-speech';

/**
 * Android does not expose voice gender. A voice is marked "provavelmente masculina"
 * only from known engine identifiers; the user confirms by testing it.
 */
export interface DeviceVoice {
  id: string;
  name: string;
  language: string;
  enhanced: boolean;
  network: boolean;
  likelyMale: boolean;
}

const MALE_HINTS = [/-ptd-/i, /smtm\d/i, /\bmale\b/i, /masc/i, /antonio/i, /fabio/i, /humberto/i, /donato/i, /julio/i];

export async function listDeviceVoices(): Promise<DeviceVoice[]> {
  let voices = await Speech.getAvailableVoicesAsync();
  if (!voices.length) {
    // Some engines populate the list only after the first query.
    await new Promise((resolve) => setTimeout(resolve, 600));
    voices = await Speech.getAvailableVoicesAsync();
  }
  return voices
    .filter((v) => v.language.toLowerCase().startsWith('pt'))
    .map((v) => ({
      id: v.identifier,
      name: v.name,
      language: v.language,
      enhanced: v.quality === Speech.VoiceQuality.Enhanced,
      network: /network/i.test(v.identifier),
      likelyMale: MALE_HINTS.some((hint) => hint.test(v.identifier) || hint.test(v.name)),
    }))
    .sort((a, b) => {
      const br = (v: DeviceVoice) => (/pt[-_]br/i.test(v.language) ? 0 : 1);
      return br(a) - br(b) || Number(b.likelyMale) - Number(a.likelyMale) || Number(a.network) - Number(b.network) || a.id.localeCompare(b.id);
    });
}

export function preferredDeviceVoice(voices: DeviceVoice[]): DeviceVoice | null {
  return voices.find((v) => v.likelyMale && /pt[-_]br/i.test(v.language) && !v.network)
    ?? voices.find((v) => v.likelyMale && /pt[-_]br/i.test(v.language))
    ?? null;
}
