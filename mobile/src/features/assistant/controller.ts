import * as Haptics from 'expo-haptics';
import { AppState, Platform } from 'react-native';
import { create } from 'zustand';
import { onEvent, onResync } from '../../core/events/eventStream';
import { log } from '../../core/logging/logger';
import { useConnectivity } from '../../core/net/connectivity';
import { settings } from '../../core/settings';
import { upsertActivity } from '../activities/repo';
import { addMessage, updateMessage, type Reference } from '../conversation/repo';
import { needsPreview, onCommandUpdate, queueCommandUntilOnline, sendCommand, type CommandRequest } from '../devices/desktop';
import { gateway } from '../gateway/api';
import { GatewayError } from '../gateway/client';
import { Approval, type TApproval } from '../gateway/schemas';
import { createMemory, recall } from '../memory/service';
import { gatewayProvider } from '../providers/gatewayProvider';
import { demoProvider, localProvider } from '../providers/localProviders';
import type { AssistantProvider } from '../providers/types';
import { loadItems, saveItem } from '../tasks/service';
import { onInterruption, type InterruptionReason } from '../voice/audioSession';
import { acquireFocus, releaseFocus } from '../voice/audioSession';
import { setLevel } from '../voice/level';
import {
  abortRecognition,
  activeMode,
  finishRecognition,
  micPermission,
  recognitionAvailability,
  startRecognition,
  sttErrorMessage,
} from '../voice/stt';
import { isSpeaking, speak, stopSpeaking } from '../voice/tts';
import { looksLikeEcho, type SpokenRecord } from './nlp/echo';
import { formatWhen } from './nlp/dates';
import { parseIntent, type Intent } from './nlp/intents';

export type Phase = 'idle' | 'listening' | 'processing' | 'speaking' | 'executing' | 'awaiting' | 'offline';
export type NoticeAction = 'open-settings' | 'keyboard' | 'memories' | 'queue-command' | 'pair';

export interface Notice {
  tone: 'info' | 'warn' | 'error';
  text: string;
  action?: NoticeAction;
}

interface AssistantState {
  phase: Phase;
  status: string;
  partial: string;
  lastReply: { text: string; refs: Reference[]; at: string; local: boolean } | null;
  notice: Notice | null;
  keyboardOpen: boolean;
  approval: TApproval | null;
  commandPreview: (CommandRequest & { title: string; description: string; risk: string }) | null;
  offlineCommand: CommandRequest | null;
  mic: 'unknown' | 'granted' | 'denied' | 'blocked';
  wakeListening: boolean;
  activeTaskId: string | null;
}

export const useAssistant = create<AssistantState>(() => ({
  phase: 'idle',
  status: 'Toque no núcleo para falar',
  partial: '',
  lastReply: null,
  notice: null,
  keyboardOpen: false,
  approval: null,
  commandPreview: null,
  offlineCommand: null,
  mic: 'unknown',
  wakeListening: false,
  activeTaskId: null,
}));

const set = (patch: Partial<AssistantState>) => useAssistant.setState(patch);
const get = () => useAssistant.getState();

const recentSpoken: SpokenRecord[] = [];
let inflight: AbortController | null = null;
let wakeTimer: ReturnType<typeof setTimeout> | null = null;
let wakeFailures = 0;

function online(): boolean {
  return useConnectivity.getState().gateway === 'online';
}

function restingPhase(): Phase {
  return online() || settings().demoMode ? 'idle' : 'offline';
}

function rest(status?: string) {
  set({ phase: restingPhase(), status: status ?? 'Toque no núcleo para falar', partial: '', activeTaskId: null });
  setLevel(0);
  scheduleWake(900);
}

function haptic(kind: 'tap' | 'success' | 'warn') {
  try {
    if (kind === 'tap') void Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Light);
    else void Haptics.notificationAsync(kind === 'success' ? Haptics.NotificationFeedbackType.Success : Haptics.NotificationFeedbackType.Warning);
  } catch {
    // no vibrator
  }
}

// ---- speaking ---------------------------------------------------------------------------
async function reply(text: string, options: { refs?: Reference[]; local?: boolean; speakIt?: boolean; spoken?: string } = {}) {
  set({ lastReply: { text, refs: options.refs ?? [], at: new Date().toISOString(), local: !!options.local } });
  if (options.speakIt === false || !settings().speakReplies || AppState.currentState !== 'active') {
    rest();
    return;
  }
  set({ phase: 'speaking', status: 'Falando… toque para interromper' });
  const started = Date.now();
  const said = options.spoken ?? text;
  const result = await speak(said);
  recentSpoken.push({ text: said, until: Date.now() + 6000 });
  while (recentSpoken.length > 3) recentSpoken.shift();
  if (result.error && !result.interrupted) {
    set({ notice: { tone: 'warn', text: `Não consegui reproduzir a voz: ${result.error}` } });
  }
  log.info('voice', `fala ${result.engine} ${result.interrupted ? 'interrompida' : 'concluída'} em ${Date.now() - started} ms`);
  if (get().phase === 'speaking') rest();
}

export function interruptSpeech() {
  if (isSpeaking()) {
    stopSpeaking();
    haptic('tap');
  }
  if (get().phase === 'speaking') rest('Interrompido');
}

// ---- listening --------------------------------------------------------------------------
let requestingListen = false;

export async function startListening(): Promise<void> {
  if (requestingListen) return;
  requestingListen = true;
  try { await beginListening(); }
  finally { requestingListen = false; }
}

async function beginListening(): Promise<void> {
  const phase = get().phase;
  if (phase === 'listening' || phase === 'processing' || phase === 'executing') return;
  stopWake();
  await stopSpeaking();
  const availability = recognitionAvailability();
  if (!availability.available) {
    set({ notice: { tone: 'warn', text: availability.reason ?? 'Reconhecimento de fala indisponível.', action: 'keyboard' } });
    return;
  }
  const permission = await micPermission(true);
  set({ mic: permission });
  if (permission !== 'granted') {
    set({
      notice: {
        tone: 'warn',
        text: permission === 'blocked'
          ? 'O microfone ou o reconhecimento de fala está bloqueado. Permita nos ajustes do aparelho ou use “Digitar”.'
          : 'Preciso do microfone para ouvir você. Você também pode digitar.',
        action: permission === 'blocked' ? 'open-settings' : 'keyboard',
      },
    });
    return;
  }
  if (AppState.currentState !== 'active') return;
  if (!acquireFocus('listen')) {
    set({ notice: { tone: 'warn', text: 'Há uma chamada em andamento. Tente quando ela terminar.' } });
    return;
  }
  haptic('tap');
  set({ phase: 'listening', status: 'Ouvindo… toque em Concluir quando terminar', partial: '', notice: null });
  let finalText = '';
  startRecognition('command', {
    onPartial: (text) => set({ partial: text }),
    onFinal: (text) => {
      finalText = text;
      set({ partial: text });
    },
    onError: (code) => {
      if (finalText) return;
      releaseFocus();
      const action: NoticeAction | undefined = code === 'not-allowed' ? 'open-settings' : code === 'network' || code === 'service-not-allowed' ? 'keyboard' : undefined;
      set({ notice: { tone: code === 'no-speech' || code === 'speech-timeout' ? 'info' : 'warn', text: sttErrorMessage(code), action } });
    },
    onEnd: () => {
      releaseFocus();
      if (get().phase !== 'listening') return;
      if (finalText) void submit(finalText, 'voice');
      else rest();
    },
  });
}

/** "Concluir": stop capturing and use what was heard. */
export function finishListening() {
  if (get().phase === 'listening') {
    set({ status: 'Entendendo…' });
    finishRecognition();
  }
}

export function cancelListening() {
  if (get().phase === 'listening') {
    abortRecognition();
    releaseFocus();
    rest('Escuta cancelada');
  }
}

// ---- main entry --------------------------------------------------------------------------
export function tapCore() {
  const { phase } = get();
  if (phase === 'listening') finishListening();
  else if (phase === 'speaking') interruptSpeech();
  else if (phase === 'idle' || phase === 'offline') void startListening();
}

export async function submit(text: string, source: 'voice' | 'text'): Promise<void> {
  const clean = text.trim();
  if (!clean) {
    rest();
    return;
  }
  if (source === 'voice' && looksLikeEcho(clean, recentSpoken)) {
    log.info('voice', 'transcrição descartada: eco da fala do MARVIN');
    set({ notice: { tone: 'info', text: 'Ignorei o que pareceu ser a minha própria voz. Pode repetir?' } });
    rest();
    return;
  }
  set({ partial: '', keyboardOpen: false });
  const intent = parseIntent(clean);
  try {
    await route(intent, clean, source);
  } catch (error) {
    log.error('assistant', 'falha ao tratar pedido', error);
    set({ notice: { tone: 'error', text: error instanceof Error ? error.message : 'Algo deu errado.' } });
    rest();
  }
}

async function localTurn(userText: string, source: string, answer: string, options: { speakIt?: boolean } = {}) {
  await addMessage({ role: 'user', text: userText, source, engine: 'local' });
  await addMessage({ role: 'assistant', text: answer, source: 'local', engine: 'local' });
  await reply(answer, { local: true, speakIt: options.speakIt });
}

async function route(intent: Intent, text: string, source: 'voice' | 'text') {
  const sourceTag = source === 'voice' ? 'mobile-voice' : 'mobile-text';
  switch (intent.kind) {
    case 'ui.keyboard':
      set({ keyboardOpen: true });
      rest('Digite seu pedido');
      return;
    case 'ui.cancel':
      await cancelCurrent();
      rest('Cancelado');
      return;
    case 'memory.save': {
      set({ phase: 'executing', status: 'Guardando na memória' });
      await createMemory(intent.content, intent.category, 'user_request', sourceTag);
      const sync = settings().demoMode ? ' (demonstração: fica só neste aparelho)' : online() ? '' : ' Sincronizo com o cofre quando o PC estiver disponível.';
      haptic('success');
      await localTurn(text, source, `Guardado na memória: “${intent.content}”.${sync}`);
      return;
    }
    case 'memory.recall': {
      const found = await recall(intent.query);
      const answer = found.length
        ? 'Lembro que: ' + found.slice(0, 3).map((m) => `${m.content}${m.origin === 'assistant_inference' ? ' (inferência minha)' : ''}`).join('; ') + '.'
        : intent.query ? `Não tenho memórias sobre ${intent.query}.` : 'Ainda não tenho memórias guardadas.';
      await localTurn(text, source, answer);
      return;
    }
    case 'memory.forget': {
      const found = await recall(intent.query);
      set({ notice: found.length ? { tone: 'info', text: `${found.length} memória(s) relacionada(s). Revise antes de excluir.`, action: 'memories' } : null });
      await localTurn(text, source, found.length
        ? `Encontrei ${found.length} memória${found.length > 1 ? 's' : ''} sobre isso. Para não apagar nada por engano, confirme a exclusão em Biblioteca, Memórias.`
        : 'Não encontrei memórias sobre isso.');
      return;
    }
    case 'item.create': {
      set({ phase: 'executing', status: 'Criando' });
      const kind = intent.itemKind;
      const result = await saveItem({ kind, title: intent.title, due_at: intent.dueAt });
      haptic('success');
      const label = kind === 'note' ? 'Nota salva' : kind === 'reminder' ? 'Lembrete criado' : 'Tarefa criada';
      const when = intent.dueAt ? ` para ${formatWhen(new Date(intent.dueAt))}` : '';
      const issue = result.notificationIssue ? ` ${result.notificationIssue}` : '';
      await localTurn(text, source, `${label}${when}: ${intent.title}.${issue}`);
      return;
    }
    case 'item.list': {
      const open = (await loadItems()).filter((i) => !i.done && i.kind !== 'note');
      const answer = open.length
        ? `Você tem ${open.length} pendência${open.length > 1 ? 's' : ''}: ` + open.slice(0, 4).map((i) => i.title).join('; ') + '.'
        : 'Nenhuma tarefa pendente.';
      await localTurn(text, source, answer);
      return;
    }
    case 'desktop':
      await desktopTurn({ action: intent.action, params: intent.params, summary: intent.summary }, text, source);
      return;
    case 'conversation':
      await converse(intent.text, source);
      return;
  }
}

function lowerFirst(text: string) {
  return text.charAt(0).toLowerCase() + text.slice(1);
}

// ---- conversation -------------------------------------------------------------------------
function provider(): AssistantProvider {
  if (settings().demoMode) return demoProvider;
  return online() ? gatewayProvider : localProvider;
}

async function converse(text: string, source: 'voice' | 'text') {
  const chosen = provider();
  const user = await addMessage({ role: 'user', text, source, status: chosen.id === 'gateway' ? 'sending' : 'done', engine: chosen.id === 'gateway' ? settings().engine : chosen.id });
  inflight = new AbortController();
  set({ phase: 'processing', status: chosen.id === 'gateway' ? 'Enviando ao MARVIN do PC…' : 'Pensando…' });
  try {
    const answer = await chosen.send({
      clientId: user.id,
      text,
      source,
      signal: inflight.signal,
      onQueued: (taskId) => {
        set({ activeTaskId: taskId, status: 'Pensando…' });
        void updateMessage(user.id, { status: 'sent', task_id: taskId });
        void upsertActivity({ id: taskId, kind: 'assistant', title: text.slice(0, 140), state: 'queued', ref: user.id });
      },
      onProgress: (message) => set({ status: message.slice(0, 80) }),
    });
    inflight = null;
    await addMessage({ role: 'assistant', text: answer.text || '(sem texto)', source: chosen.id, task_id: answer.taskId ?? null, engine: answer.engine ?? chosen.id, status: answer.state === 'offline' ? 'offline' : 'done', refs: answer.refs ? JSON.stringify(answer.refs) : null });
    if (answer.taskId) await upsertActivity({ id: answer.taskId, kind: 'assistant', title: text.slice(0, 140), state: answer.state, detail: answer.text.slice(0, 400) });
    if (chosen.id === 'gateway') await updateMessage(user.id, { status: 'done' });
    await reply(answer.text, { refs: answer.refs, local: chosen.id !== 'gateway' });
  } catch (error) {
    inflight = null;
    if (error instanceof GatewayError && error.kind === 'aborted') {
      await updateMessage(user.id, { status: 'cancelled' });
      rest('Pedido cancelado');
      return;
    }
    const offline = error instanceof GatewayError && (error.retryable || error.kind === 'not_paired');
    await updateMessage(user.id, { status: offline ? 'offline' : 'failed' });
    const message = offline
      ? 'Perdi a conexão com o computador antes da resposta. Sua mensagem ficou no histórico; tente de novo quando o PC voltar.'
      : `O MARVIN do PC não conseguiu responder: ${error instanceof Error ? error.message : 'erro desconhecido'}`;
    await addMessage({ role: 'assistant', text: message, source: 'local', engine: 'local', status: 'failed' });
    await reply(message, { local: true });
  }
}

/** Cancels what is running: capture, a pending answer (also on the PC when supported) or speech. */
export async function cancelCurrent() {
  const { phase, activeTaskId } = get();
  if (phase === 'listening') cancelListening();
  if (isSpeaking()) stopSpeaking();
  if (inflight) {
    inflight.abort();
    inflight = null;
  }
  if (activeTaskId && online() && !settings().demoMode) {
    try {
      const result = await gateway.cancelTask(activeTaskId);
      await upsertActivity({ id: activeTaskId, kind: 'assistant', state: result.state === 'cancelling' ? 'cancelling' : result.state });
    } catch (error) {
      log.warn('assistant', `cancelamento no PC: ${error instanceof Error ? error.message : String(error)}`);
    }
  }
  rest('Cancelado');
}

// ---- PC actions ---------------------------------------------------------------------------
async function desktopTurn(request: CommandRequest, text: string, source: 'voice' | 'text') {
  await addMessage({ role: 'user', text, source, engine: 'desktop' });
  const connectivity = useConnectivity.getState();
  if (!settings().demoMode) {
    if (connectivity.gateway !== 'online') {
      set({ offlineCommand: request, notice: { tone: 'warn', text: 'Computador indisponível. Posso enviar se ele voltar em até 5 minutos.', action: 'queue-command' } });
      await addMessage({ role: 'assistant', text: 'O computador está indisponível; o comando não foi enviado.', source: 'local', engine: 'desktop' });
      await reply('O computador está indisponível. O comando não foi enviado.', { local: true });
      return;
    }
    if (connectivity.desktop !== 'online') {
      const message = 'O servidor responde, mas o agente do computador não está ativo. Nada foi executado.';
      await addMessage({ role: 'assistant', text: message, source: 'local', engine: 'desktop' });
      await reply(message, { local: true });
      return;
    }
  }
  if (needsPreview(request.action) && !settings().demoMode) {
    const info = useConnectivity.getState().capabilities?.desktop.actions.find((a) => a.id === request.action);
    set({
      phase: 'awaiting',
      status: 'Aguardando sua decisão',
      commandPreview: { ...request, title: info?.label ?? request.summary, description: info?.preview || info?.description || request.summary, risk: info?.risk ?? 'low' },
    });
    haptic('warn');
    return;
  }
  await executeCommand(request, false);
}

export async function confirmCommand(approved: boolean) {
  const preview = get().commandPreview;
  set({ commandPreview: null });
  if (!preview) return;
  if (!approved) {
    await addMessage({ role: 'assistant', text: `Ok, não vou ${lowerFirst(preview.summary)}.`, source: 'local', engine: 'desktop' });
    rest('Ação descartada');
    return;
  }
  await executeCommand({ action: preview.action, params: preview.params, summary: preview.summary }, true);
}

export async function queueOfflineCommand() {
  const request = get().offlineCommand;
  set({ offlineCommand: null, notice: null });
  if (!request) return;
  await queueCommandUntilOnline(request, false);
  set({ notice: { tone: 'info', text: 'Guardei o comando por até 5 minutos. Se o PC não voltar, peço sua confirmação de novo.' } });
}

function waitForFinal(commandId: string, timeoutMs: number): Promise<{ state: string; message: string } | null> {
  const final = new Set(['completed', 'dispatched', 'failed', 'expired', 'cancelled', 'rejected', 'needs_reconciliation']);
  return new Promise((resolve) => {
    const timer = setTimeout(() => {
      unsubscribe();
      resolve(null);
    }, timeoutMs);
    const unsubscribe = onCommandUpdate((record) => {
      if (record.command_id === commandId && final.has(record.state)) {
        clearTimeout(timer);
        unsubscribe();
        resolve({ state: record.state, message: record.message });
      }
    });
  });
}

async function executeCommand(request: CommandRequest, confirmed: boolean) {
  set({ phase: 'executing', status: 'Enviando ao computador…' });
  const outcome = await sendCommand(request, confirmed);
  if (outcome.needsConfirmation) {
    set({ phase: 'awaiting', status: 'Aguardando sua decisão', commandPreview: { ...request, ...outcome.needsConfirmation } });
    return;
  }
  let final: { state: string; message: string } | null = { state: outcome.state, message: outcome.message };
  if (outcome.state === 'received' || outcome.state === 'started') {
    set({ status: 'Pedido recebido pelo PC · executando' });
    final = await waitForFinal(outcome.commandId, 30000);
  }
  const answer = !final
    ? 'O PC recebeu o pedido, mas ainda não informou o resultado. Acompanhe em Atividades.'
    : final.state === 'completed'
      ? `Feito. ${final.message}`
      : final.state === 'dispatched'
        ? `Pedi ao Windows: ${lowerFirst(request.summary)}. Não consigo confirmar visualmente o resultado.`
        : final.state === 'simulated'
          ? 'Demonstração: nada foi executado no computador.'
          : `Não foi executado. ${final.message}`;
  if (final?.state === 'completed') haptic('success');
  await addMessage({ role: 'assistant', text: answer, source: 'local', engine: 'desktop' });
  // Details (paths, window lists) stay on screen; the voice gives the short outcome.
  const spoken = final?.state === 'completed' ? `Feito: ${lowerFirst(request.summary)}.` : undefined;
  await reply(answer, { local: true, spoken });
}

// ---- approvals from the PC runtime --------------------------------------------------------
export async function decideApproval(accepted: boolean) {
  const approval = get().approval;
  if (!approval) return;
  set({ approval: null });
  try {
    await gateway.decide(approval.id, accepted);
  } catch (error) {
    set({ notice: { tone: 'warn', text: error instanceof Error ? error.message : 'A autorização expirou.' } });
  }
  if (get().phase === 'awaiting') set({ phase: 'processing', status: accepted ? 'Continuando no PC' : 'Ação recusada' });
}

onEvent('approval.requested', (event) => {
  const parsed = Approval.safeParse(event.data);
  if (!parsed.success) return;
  set({ approval: parsed.data, phase: 'awaiting', status: 'Uma decisão sua para continuar' });
  haptic('warn');
});

onEvent('approval.resolved', (event) => {
  const id = (event.data as { id?: string }).id;
  if (get().approval?.id === id) {
    set({ approval: null });
    if (get().phase === 'awaiting') set({ phase: 'processing', status: 'Continuando' });
  }
});

onResync(async () => {
  if (settings().demoMode || !online()) return;
  const pending = await gateway.approvals();
  set({ approval: pending[0] ?? null });
});

// ---- interruptions (calls, focus loss, headphones) ---------------------------------------
const interruptionText: Record<InterruptionReason, string> = {
  call: 'Chamada ou interrupção do sistema: pausei a voz e a escuta.',
  focus_lost: 'Outro app assumiu o áudio: interrompi.',
  headphones_removed: 'Fone desconectado: interrompi a fala para não tocar no alto-falante.',
};

onInterruption((reason) => {
  const { phase } = get();
  if (phase === 'listening') {
    abortRecognition();
    releaseFocus();
    rest();
    set({ notice: { tone: 'warn', text: interruptionText[reason] } });
  } else if (phase === 'speaking' || isSpeaking()) {
    stopSpeaking();
    rest();
    set({ notice: { tone: 'warn', text: interruptionText[reason] } });
  }
  stopWake();
});

useConnectivity.subscribe((state, previous) => {
  if (state.gateway === previous.gateway) return;
  const { phase } = get();
  if (phase === 'idle' || phase === 'offline') set({ phase: restingPhase() });
});

AppState.addEventListener('change', (state) => {
  if (state !== 'active') {
    stopWake();
    if (get().phase === 'listening') cancelListening();
    if (isSpeaking()) {
      stopSpeaking();
      rest();
    }
  } else scheduleWake(800);
});

// ---- wake word ("Marvin") — foreground only, explicit toggle, visible indicator -----------
export interface WakeSupport {
  supported: boolean;
  reason: string | null;
}

export function wakeWordSupport(): WakeSupport {
  if (Platform.OS === 'ios') return { supported: false, reason: 'No iPhone, toque no núcleo para falar. Esta versão não mantém escuta por “Marvin” em segundo plano nem com o app encerrado.' };
  const availability = recognitionAvailability();
  if (!availability.available) return { supported: false, reason: availability.reason };
  if (!availability.onDevice) {
    return { supported: false, reason: 'Exige reconhecimento de fala no próprio aparelho (Android 13+ com o pacote de português instalado).' };
  }
  return { supported: true, reason: null };
}

function stopWake() {
  if (wakeTimer) clearTimeout(wakeTimer);
  wakeTimer = null;
  if (activeMode() === 'wake') abortRecognition();
  if (get().wakeListening) set({ wakeListening: false });
}

function scheduleWake(delay: number) {
  if (wakeTimer) clearTimeout(wakeTimer);
  wakeTimer = setTimeout(() => void runWake(), delay);
}

async function runWake() {
  wakeTimer = null;
  const { phase } = get();
  if (!settings().wakeWordEnabled || AppState.currentState !== 'active') return stopWake();
  if ((phase !== 'idle' && phase !== 'offline') || activeMode() || isSpeaking()) return;
  if (!wakeWordSupport().supported) return;
  if ((await micPermission(false)) !== 'granted') return;
  set({ wakeListening: true });
  let triggered = false;
  const onText = (text: string) => {
    if (triggered) return;
    const match = /\bmarvin\b[\s,.:!]*(.*)$/i.exec(text);
    if (!match) return;
    triggered = true;
    wakeFailures = 0;
    abortRecognition();
    set({ wakeListening: false });
    const rest = match[1].trim();
    if (rest.split(/\s+/).length >= 2) void submit(rest, 'voice');
    else void startListening();
  };
  startRecognition('wake', {
    onPartial: onText,
    onFinal: onText,
    onError: (code) => {
      if (code === 'language-not-supported' || code === 'service-not-allowed' || code === 'not-allowed') {
        void settings().update({ wakeWordEnabled: false });
        set({ notice: { tone: 'warn', text: `Escuta por “Marvin” desativada: ${sttErrorMessage(code)}` } });
      } else if (code !== 'no-speech' && code !== 'speech-timeout') wakeFailures++;
    },
    onEnd: () => {
      if (get().wakeListening) set({ wakeListening: false });
      if (!triggered && settings().wakeWordEnabled) scheduleWake(wakeFailures > 3 ? 8000 : 500);
    },
  });
}

export function setWakeWord(enabled: boolean) {
  if (enabled && !wakeWordSupport().supported) return;
  void settings().update({ wakeWordEnabled: enabled });
  if (enabled) scheduleWake(200);
  else stopWake();
}
