// Pure: removes credentials from anything that may reach logs or diagnostics exports.
const PATTERNS: [RegExp, string][] = [
  [/(authorization\s*[:=]\s*)(bearer\s+)?[^\s,"']+/gi, '$1[redigido]'],
  [/bearer\s+[A-Za-z0-9._~+/=-]{8,}/gi, 'Bearer [redigido]'],
  [/("?(?:token|password|senha|secret|api[_-]?key|code|codigo)"?\s*[:=]\s*"?)[^"\s,}]+/gi, '$1[redigido]'],
  [/([?&](?:c|code|k|token)=)[^&\s]+/gi, '$1[redigido]'],
  [/[A-Za-z0-9+/]{40,}={0,2}/g, '[longo-redigido]'],
];

export function redact(input: string): string {
  let text = input;
  for (const [pattern, replacement] of PATTERNS) text = text.replace(pattern, replacement);
  return text.length > 2000 ? text.slice(0, 2000) + '…' : text;
}
