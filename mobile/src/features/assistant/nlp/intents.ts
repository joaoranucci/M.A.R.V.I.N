import { parseDate } from './dates.ts';
import { fold, normalize, slugify } from './text.ts';

/**
 * Deterministic pt-BR intent router. Runs on the phone before any model call:
 * memories, tasks and UI commands work offline; PC actions become structured commands.
 * Anything else is a conversation turn for the assistant.
 */
export type ItemKind = 'task' | 'reminder' | 'note';

export type Intent =
  | { kind: 'ui.keyboard' }
  | { kind: 'ui.cancel' }
  | { kind: 'memory.save'; content: string; category: string }
  | { kind: 'memory.recall'; query: string | null }
  | { kind: 'memory.forget'; query: string }
  | { kind: 'item.create'; itemKind: ItemKind; title: string; dueAt: string | null; hasTime: boolean }
  | { kind: 'item.list' }
  | { kind: 'desktop'; action: string; params: Record<string, string>; summary: string }
  | { kind: 'conversation'; text: string };

const PC = String.raw`(?:\s+(?:no|do|pelo|na)\s+(?:meu\s+)?(?:computador|pc|notebook|desktop))`;
const FOLDERS: Record<string, string> = {
  downloads: 'downloads', download: 'downloads', documentos: 'documentos', documento: 'documentos',
  'area de trabalho': 'area de trabalho', desktop: 'area de trabalho', imagens: 'imagens', fotos: 'imagens',
  musicas: 'musicas', videos: 'videos',
};

export function stripWakeWord(text: string): string {
  return text
    .trim()
    .replace(/^(?:(?:ei|hey|oi|ok|ola|olá)[,\s]+)?marvin[,.:!\s]*/i, '')
    .replace(/^(?:por favor[,\s]+|você pode\s+|voce pode\s+|pode\s+)/i, '')
    .trim();
}

export function inferCategory(content: string): string {
  const n = normalize(content);
  if (/\b(prefiro|gosto|nao gosto|odeio|adoro|curto|favorit)/.test(n)) return 'preferencia';
  if (/\b(trabalho|reuniao|chefe|empresa|cliente|expediente)\b/.test(n)) return 'trabalho';
  if (/\b(estud|faculdade|curso|prova|aula)/.test(n)) return 'estudos';
  if (/\b(saude|remedio|medico|alergi|treino|academia)/.test(n)) return 'saude';
  if (/\b(projeto|marvin|oculos|pulseira|codigo)\b/.test(n)) return 'projetos';
  return 'geral';
}

function cleanTitle(original: string, start: number, end: number): string {
  const title = (original.slice(0, start) + ' ' + original.slice(end))
    .replace(/\s+(?:de|para|pra|que)\s*$/i, '')
    .replace(/^\s*(?:de|para|pra|que)\s+/i, '')
    .replace(/\s+/g, ' ')
    .replace(/[\s,.;:]+$/g, '')
    .trim();
  return title.charAt(0).toUpperCase() + title.slice(1);
}

function itemIntent(itemKind: ItemKind, original: string, now: Date): Intent {
  const match = itemKind === 'note' ? null : parseDate(original, now);
  if (!match) {
    const title = cleanTitle(original, 0, 0);
    return { kind: 'item.create', itemKind: itemKind === 'reminder' ? 'task' : itemKind, title, dueAt: null, hasTime: false };
  }
  return {
    kind: 'item.create',
    itemKind: itemKind === 'task' ? 'task' : 'reminder',
    title: cleanTitle(original, match.start, match.end),
    dueAt: match.date.toISOString(),
    hasTime: match.hasTime,
  };
}

function desktop(n: string, original: string): Intent | null {
  let m: RegExpExecArray | null;
  if ((m = new RegExp(String.raw`^(?:abra|abre|abrir|abra pra mim)\s+(?:o\s+|um\s+)?(?:navegador|browser|google|chrome|edge|firefox)${PC}?$`).exec(n))) {
    return { kind: 'desktop', action: 'open_browser', params: {}, summary: 'Abrir o navegador no computador' };
  }
  if ((m = new RegExp(String.raw`^(?:pesquise|pesquisa|procure|procura|busque|busca)\s+(?:por\s+|sobre\s+)?(.+?)(?:${PC}|\s+no\s+navegador)$`).exec(n))) {
    return { kind: 'desktop', action: 'web_search', params: { query: m[1] }, summary: `Pesquisar “${m[1]}” no navegador do PC` };
  }
  if ((m = new RegExp(String.raw`^(?:abra|abre|abrir|mostre)\s+(?:a\s+)?(?:minha\s+)?(?:pasta\s+)?(?:de\s+)?(downloads?|documentos?|area de trabalho|desktop|imagens|fotos|musicas|videos)${PC}?$`).exec(n))) {
    const folder = FOLDERS[m[1]];
    return { kind: 'desktop', action: 'open_folder', params: { folder }, summary: `Abrir a pasta ${folder} no PC` };
  }
  if ((m = new RegExp(String.raw`^(?:crie|criar|cria|faca|faz)\s+(?:uma\s+)?(?:nova\s+)?pasta\s+(?:(?:para|pro|pra|do|de)\s+(?:o\s+|meu\s+)?projeto\s+|(?:chamada|com o nome)\s+)?(.+?)${PC}?$`).exec(n))) {
    const name = slugify(m[1].replace(/^(?:o|a|meu|minha)\s+/, ''));
    if (name) return { kind: 'desktop', action: 'create_project_folder', params: { name }, summary: `Criar a pasta de projeto “${name}” no PC` };
  }
  if (new RegExp(String.raw`^(?:continue|continua|continuar|retome|retomar)\s+(?:a\s+|o\s+)?(?:ultima\s+)?(?:tarefa|trabalho)(?:\s+que\s+(?:eu\s+)?comecei)?${PC}?$`).test(n)) {
    return { kind: 'desktop', action: 'continue_task', params: {}, summary: 'Continuar a última tarefa do PC' };
  }
  if (/^(?:bloqueie|bloquear|bloqueia|trave|trava)\s+(?:o\s+|meu\s+|a\s+tela\s+do\s+)?(?:computador|pc|notebook)$/.test(n)) {
    return { kind: 'desktop', action: 'lock_screen', params: {}, summary: 'Bloquear o computador' };
  }
  if (/^(?:desligue|desliga|desligar)\s+(?:o\s+|meu\s+)?(?:computador|pc|notebook)(?:\s+agora)?$/.test(n)) {
    return { kind: 'desktop', action: 'shutdown', params: {}, summary: 'Desligar o computador' };
  }
  if ((m = new RegExp(String.raw`^(aumente|aumenta|suba|sobe|abaixe|abaixa|diminua|diminui|baixe|baixa)\s+o\s+(?:som|volume)${PC}$`).exec(n))) {
    const up = /^(aument|sub|sobe)/.test(m[1]);
    return { kind: 'desktop', action: 'volume', params: { direction: up ? 'up' : 'down' }, summary: up ? 'Aumentar o volume do PC' : 'Diminuir o volume do PC' };
  }
  if (/^(?:silencie|silencia|mute|muta|tire o som d[oa])\s+(?:o\s+)?(?:meu\s+)?(?:computador|pc|notebook)$/.test(n)) {
    return { kind: 'desktop', action: 'volume', params: { direction: 'mute' }, summary: 'Silenciar o PC' };
  }
  if (new RegExp(String.raw`^(?:liste|lista|quais|mostre)\s+(?:sao\s+)?(?:as\s+)?janelas(?:\s+abertas)?${PC}?$`).test(n)) {
    return { kind: 'desktop', action: 'list_windows', params: {}, summary: 'Listar as janelas abertas no PC' };
  }
  if ((m = new RegExp(String.raw`^(?:abra|abre|abrir|inicie|inicia|execute)\s+(?:o\s+|a\s+)?(?:aplicativo\s+|app\s+|programa\s+)?(.+?)${PC}$`).exec(n))) {
    const name = m[1].trim();
    if (name && !/[;&|<>`]/.test(name)) return { kind: 'desktop', action: 'open_app', params: { name }, summary: `Abrir ${name} no PC` };
  }
  return null;
}

export function parseIntent(input: string, now: Date = new Date()): Intent {
  const original = stripWakeWord(input);
  const n = normalize(original);
  if (!n) return { kind: 'conversation', text: input.trim() };

  if (/^(?:digitar|teclado|abrir teclado|abra o teclado|abre o teclado|quero digitar|modo texto|vou digitar)$/.test(n)) return { kind: 'ui.keyboard' };
  if (/^(?:cancelar|cancele|cancela|pare|para|parar|esquece|deixa pra la|nada nao)$/.test(n)) return { kind: 'ui.cancel' };

  // Questions and negations are conversation, never effects.
  const isQuestion = /^(?:como|por que|porque|o que significa|explique|me explique|qual|quais|quando|onde)\b/.test(n) && !/^(?:quais\s+(?:sao\s+)?(?:as\s+)?(?:minhas\s+tarefas|janelas))/.test(n);
  if (/^(?:nao|não)\s/.test(n)) return { kind: 'conversation', text: original };

  let m: RegExpExecArray | null;
  const folded = fold(original);
  if ((m = /^(?:me lembre|me lembra|lembre-me|lembre me|crie um lembrete|cria um lembrete|agende um lembrete|novo lembrete)(?:\s+(?:de|que|para|pra))?\s+/.exec(folded))) {
    return itemIntent('reminder', original.slice(m[0].length), now);
  }
  if ((m = /^(?:lembre|lembra|memorize|memoriza|guarde|guarda|grave|grava|saiba)(?:\s+de)?\s+que\s+/.exec(folded))) {
    const content = original.slice(m[0].length).trim().replace(/[.!]+$/, '');
    const pretty = content.charAt(0).toUpperCase() + content.slice(1);
    return { kind: 'memory.save', content: pretty, category: inferCategory(content) };
  }
  if ((m = /^(?:o que (?:voce )?(?:sabe|lembra)|do que (?:voce )?(?:se )?lembra)(?:\s+(?:sobre|de|a respeito de))?\s*(.*)$/.exec(n))) {
    const query = m[1].replace(/^(?:mim|eu)$/, '').trim();
    return { kind: 'memory.recall', query: query || null };
  }
  if ((m = /^(?:esqueca|esquece|apague a memoria|apague a lembranca|apaga a memoria)\s+(?:de\s+)?(?:que\s+)?(.+)$/.exec(n))) {
    return { kind: 'memory.forget', query: m[1] };
  }
  if ((m = /^(?:crie|cria|adicione|adiciona|anote|nova)\s+(?:uma\s+)?tarefa(?:\s+(?:de|para|pra))?[:\s]+/.exec(folded))) {
    return itemIntent('task', original.slice(m[0].length), now);
  }
  if ((m = /^(?:anote|anota|crie uma nota|cria uma nota|nova nota|tome nota)(?:\s+(?:que|de))?[:\s]+/.exec(folded))) {
    return itemIntent('note', original.slice(m[0].length), now);
  }
  if (/^(?:minhas tarefas|quais (?:sao )?(?:as )?minhas tarefas|o que (?:eu )?tenho (?:pra|para) fazer|mostre (?:as |minhas )?tarefas|meus lembretes)$/.test(n)) {
    return { kind: 'item.list' };
  }
  if (!isQuestion) {
    const command = desktop(n, original);
    if (command) return command;
  }
  return { kind: 'conversation', text: original || input.trim() };
}
