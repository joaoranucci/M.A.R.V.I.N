// Pure text helpers shared by intents, echo guard and speech. No React Native imports.

/** Lowercase and remove diacritics char-by-char, keeping indexes aligned with the input. */
export function fold(text: string): string {
  let out = '';
  for (const char of text) {
    const base = char.normalize('NFD')[0] ?? char;
    out += base.length === char.length ? base.toLowerCase() : char.toLowerCase();
  }
  return out;
}

export function normalize(text: string): string {
  return fold(text)
    .replace(/[“”"'!?¿¡.,;:()\[\]]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

export function tokens(text: string): string[] {
  return normalize(text)
    .split(' ')
    .filter((t) => t.length > 1);
}

/** Text suitable for TTS: no markdown, links read as their label, no code blocks. */
export function spokenText(text: string): string {
  return text
    .replace(/```[\s\S]*?```/g, ' ')
    .replace(/`([^`]+)`/g, '$1')
    .replace(/!\[[^\]]*\]\([^)]*\)/g, ' ')
    .replace(/\[([^\]]+)\]\((https?:[^)]+)\)/g, '$1')
    .replace(/https?:\/\/\S+/g, 'link')
    .replace(/^\s{0,3}#{1,6}\s*/gm, '')
    .replace(/^\s*[-*•]\s+/gm, '')
    .replace(/\*\*([^*]+)\*\*/g, '$1')
    .replace(/\*([^*]+)\*/g, '$1')
    .replace(/_{1,2}([^_]+)_{1,2}/g, '$1')
    .replace(/\[FONTE (\d+)\]/gi, 'fonte $1')
    .replace(/\s+/g, ' ')
    .trim();
}

/** Short, human-comparable fingerprint; must match marvin/gateway/tls.py display_fingerprint. */
export function displayFingerprint(pinBase64: string): string {
  const binary = atob(pinBase64);
  let hex = '';
  for (let i = 0; i < Math.min(10, binary.length); i++) hex += binary.charCodeAt(i).toString(16).padStart(2, '0');
  hex = hex.toUpperCase();
  return hex.match(/.{1,4}/g)?.join('-') ?? hex;
}

export function slugify(text: string): string {
  return fold(text)
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '')
    .slice(0, 60);
}
