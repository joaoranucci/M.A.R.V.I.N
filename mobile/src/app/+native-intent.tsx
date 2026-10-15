import { normalizePairingLink } from '../features/assistant/nlp/pairing';

export function redirectSystemPath({ path }: { path: string; initial: boolean }): string {
  return normalizePairingLink(path);
}
