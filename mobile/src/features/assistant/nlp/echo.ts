import { tokens } from './text.ts';

/**
 * Half-duplex safety net: a transcript that mostly repeats what MARVIN just said is
 * treated as its own voice leaking into the microphone, not as a new instruction.
 */
export interface SpokenRecord {
  text: string;
  until: number;
}

export function looksLikeEcho(transcript: string, recent: SpokenRecord[], now: number = Date.now()): boolean {
  const heard = tokens(transcript);
  if (heard.length === 0) return false;
  for (const record of recent) {
    if (record.until < now) continue;
    const spoken = new Set(tokens(record.text));
    if (spoken.size === 0) continue;
    const overlap = heard.filter((t) => spoken.has(t)).length / heard.length;
    if ((heard.length >= 3 && overlap >= 0.7) || (heard.length < 3 && overlap === 1 && spoken.size <= 4)) return true;
  }
  return false;
}
