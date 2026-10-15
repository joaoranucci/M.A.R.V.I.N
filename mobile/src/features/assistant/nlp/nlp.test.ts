// Run: node --test src/features/assistant/nlp/nlp.test.ts  (Node 22.18+/24 strips TypeScript types)
import assert from 'node:assert/strict';
import { test } from 'node:test';
import { parseDate } from './dates.ts';
import { looksLikeEcho } from './echo.ts';
import { parseIntent } from './intents.ts';
import { parsePairingUrl, validHost } from './pairing.ts';
import { displayFingerprint, spokenText } from './text.ts';

const NOW = new Date(2026, 9, 15, 14, 0, 0); // quinta, 15/10/2026 14:00 local

test('memória explícita a partir da fala do usuário', () => {
  const intent = parseIntent('Marvin, lembre que prefiro estudar depois do trabalho.', NOW);
  assert.deepEqual(intent, { kind: 'memory.save', content: 'Prefiro estudar depois do trabalho', category: 'preferencia' });
});

test('lembrete com data é tarefa, não memória', () => {
  const intent = parseIntent('Me lembre de revisar o projeto amanhã às 9h30', NOW);
  assert.equal(intent.kind, 'item.create');
  if (intent.kind !== 'item.create') return;
  assert.equal(intent.itemKind, 'reminder');
  assert.equal(intent.title, 'Revisar o projeto');
  const due = new Date(intent.dueAt!);
  assert.equal(due.getDate(), 16);
  assert.equal(due.getHours(), 9);
  assert.equal(due.getMinutes(), 30);
});

test('lembrete relativo e sem horário', () => {
  const rel = parseIntent('me lembra de beber água daqui a 10 minutos', NOW);
  assert.equal(rel.kind === 'item.create' && new Date(rel.dueAt!).getTime() - NOW.getTime(), 10 * 60000);
  const none = parseIntent('me lembre de comprar pão', NOW);
  assert.equal(none.kind === 'item.create' && none.itemKind, 'task');
});

test('ações no computador viram comandos estruturados', () => {
  assert.deepEqual(parseIntent('Marvin, abra o navegador no computador', NOW).kind, 'desktop');
  const folder = parseIntent('Crie uma pasta para meu projeto Óculos Inteligentes', NOW);
  assert.equal(folder.kind === 'desktop' && folder.action, 'create_project_folder');
  assert.equal(folder.kind === 'desktop' && folder.params.name, 'oculos-inteligentes');
  const resume = parseIntent('Continue a tarefa que comecei no PC', NOW);
  assert.equal(resume.kind === 'desktop' && resume.action, 'continue_task');
  const shutdown = parseIntent('desligue o computador', NOW);
  assert.equal(shutdown.kind === 'desktop' && shutdown.action, 'shutdown');
  const app = parseIntent('abra o spotify no computador', NOW);
  assert.equal(app.kind === 'desktop' && app.params.name, 'spotify');
});

test('perguntas, negações e conversa livre não executam nada', () => {
  assert.equal(parseIntent('como abrir o navegador no computador?', NOW).kind, 'conversation');
  assert.equal(parseIntent('não desligue o computador', NOW).kind, 'conversation');
  assert.equal(parseIntent('qual a capital da Austrália?', NOW).kind, 'conversation');
  assert.equal(parseIntent('abra o spotify', NOW).kind, 'conversation'); // sem “no computador”: ambíguo
});

test('comandos de interface', () => {
  assert.equal(parseIntent('Marvin, abrir teclado', NOW).kind, 'ui.keyboard');
  assert.equal(parseIntent('cancelar', NOW).kind, 'ui.cancel');
  assert.deepEqual(parseIntent('o que você lembra sobre trabalho?', NOW), { kind: 'memory.recall', query: 'trabalho' });
});

test('datas pt-BR', () => {
  const evening = parseDate('hoje às 8 da noite', NOW)!;
  assert.equal(evening.date.getHours(), 20);
  const friday = parseDate('sexta-feira às 10:15', NOW)!;
  assert.equal(friday.date.getDay(), 5);
  assert.equal(friday.date.getMinutes(), 15);
  const passed = parseDate('às 9', NOW)!; // 09:00 já passou: amanhã
  assert.equal(passed.date.getDate(), 16);
  assert.equal(parseDate('sem data nenhuma', NOW), null);
});

test('eco da própria voz é descartado', () => {
  const recent = [{ text: 'Guardei que você prefere estudar depois do trabalho.', until: Date.now() + 5000 }];
  assert.equal(looksLikeEcho('você prefere estudar depois do trabalho', recent), true);
  assert.equal(looksLikeEcho('abra o navegador no computador', recent), false);
  assert.equal(looksLikeEcho('você prefere estudar depois do trabalho', [{ ...recent[0], until: Date.now() - 1 }]), false);
});

test('QR de vinculação e endereço do PC', () => {
  const pin = Buffer.alloc(32, 7).toString('base64');
  const url = `marvin://pair?v=1&h=192.168.0.12&p=8770&c=123456&k=${encodeURIComponent(pin)}&n=PC-JOAO&s=abc`;
  assert.deepEqual(parsePairingUrl(url), { host: '192.168.0.12', port: 8770, code: '123456', pin, serverName: 'PC-JOAO', serverId: 'abc' });
  assert.equal(parsePairingUrl(url.replace('c=123456', 'c=12')), null);
  assert.equal(parsePairingUrl('https://evil.test'), null);
  assert.equal(validHost('localhost'), false);
  assert.equal(validHost('10.0.2.2'), true);
});

test('impressão digital igual à do PC e texto falado', () => {
  const pin = Buffer.from('0123456789abcdef0123456789abcdef').toString('base64');
  assert.equal(displayFingerprint(pin), '3031-3233-3435-3637-3839');
  assert.equal(spokenText('Veja **isto** em [docs](https://x.y) [FONTE 1]'), 'Veja isto em docs fonte 1');
});
