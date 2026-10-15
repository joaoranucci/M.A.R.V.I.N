import { z } from 'zod';
import { noteServerTime, request } from './client';
import * as S from './schemas';

export const gateway = {
  async health(base?: { host: string; port: number }) {
    const started = Date.now();
    const data = await request('/v1/health', { schema: S.Health, auth: false, base, timeoutMs: 6000 });
    noteServerTime(data.server_time, started);
    return data;
  },
  pair: (base: { host: string; port: number }, code: string, deviceName: string, appVersion: string) =>
    request('/v1/pair', {
      method: 'POST',
      base,
      auth: false,
      body: { code, device_name: deviceName, platform: 'android', app_version: appVersion },
      schema: S.PairResponse,
    }),
  capabilities: () => request('/v1/capabilities', { schema: S.Capabilities }),
  async status() {
    const started = Date.now();
    const data = await request('/v1/status', { schema: S.Status, timeoutMs: 8000 });
    noteServerTime(data.server_time, started);
    return data;
  },
  events: (after: number, wait: number, signal?: AbortSignal) =>
    request(`/v1/events?after=${after}&wait=${wait}`, { schema: S.EventsBatch, timeoutMs: (wait + 10) * 1000, signal }),
  devices: () => request('/v1/devices', { schema: z.array(S.LinkedDevice) }),
  revokeDevice: (id: string) => request(`/v1/devices/${encodeURIComponent(id)}`, { method: 'DELETE' }),

  sendMessage: (body: { client_id: string; text: string; engine: string; source: 'voice' | 'text' }) =>
    request('/v1/conversation/messages', { method: 'POST', body, schema: S.SendMessageResponse, timeoutMs: 15000 }),
  history: (afterId: number, limit = 200) =>
    request(`/v1/conversation/history?after_id=${afterId}&limit=${limit}`, { schema: z.array(S.HistoryMessage) }),
  task: (id: string, wait = 0, signal?: AbortSignal) =>
    request(`/v1/assistant/tasks/${encodeURIComponent(id)}?wait=${wait}`, {
      schema: S.AssistantTask,
      timeoutMs: (wait + 10) * 1000,
      signal,
    }),
  tasks: () => request('/v1/assistant/tasks?limit=60', { schema: z.array(S.AssistantTask) }),
  cancelTask: (id: string) =>
    request(`/v1/assistant/tasks/${encodeURIComponent(id)}/cancel`, {
      method: 'POST',
      schema: z.object({ task_id: z.string(), state: z.string() }),
    }),
  approvals: () => request('/v1/approvals', { schema: z.array(S.Approval) }),
  decide: (id: string, accepted: boolean) =>
    request(`/v1/approvals/${encodeURIComponent(id)}`, { method: 'POST', body: { accepted } }),

  memories: (q = '') => request(`/v1/memories${q ? `?q=${encodeURIComponent(q)}` : ''}`, { schema: z.array(S.Memory), timeoutMs: 20000 }),
  createMemory: (body: { client_id: string; content: string; category: string; origin: string; source: string }) =>
    request('/v1/memories', { method: 'POST', body, schema: S.Memory }),
  updateMemory: (id: string, body: { content: string; category: string; origin: string; base_updated_at: string | null }) =>
    request(`/v1/memories/${encodeURIComponent(id)}`, { method: 'PUT', body, schema: S.Memory }),
  deleteMemory: (id: string) => request(`/v1/memories/${encodeURIComponent(id)}`, { method: 'DELETE' }),

  documents: () => request('/v1/documents', { schema: z.array(S.Document), timeoutMs: 20000 }),
  upload: (form: FormData) =>
    request('/v1/documents', { method: 'POST', form, schema: S.Upload, timeoutMs: 180000 }),
  uploadState: (id: string) => request(`/v1/documents/uploads/${encodeURIComponent(id)}`, { schema: S.Upload }),
  deleteDocument: (id: string) =>
    request(`/v1/documents/${encodeURIComponent(id)}`, { method: 'DELETE', headers: { 'X-Confirm-Delete': 'yes' } }),
  search: (q: string, documentId = '') =>
    request(`/v1/knowledge/search?q=${encodeURIComponent(q)}&top_k=8${documentId ? `&document_id=${encodeURIComponent(documentId)}` : ''}`, {
      schema: z.array(S.SearchHit),
      timeoutMs: 60000,
    }),
  ask: (question: string, documentId?: string) =>
    request('/v1/knowledge/ask', {
      method: 'POST',
      body: { question, document_id: documentId ?? null },
      schema: S.AskResult,
      timeoutMs: 210000,
    }),
  chunk: (id: string) => request(`/v1/knowledge/chunks/${encodeURIComponent(id)}`, { schema: S.Chunk }),

  items: (since?: string) => request(`/v1/items${since ? `?since=${encodeURIComponent(since)}` : ''}`, { schema: S.ItemList }),
  putItem: (id: string, body: Record<string, unknown>) =>
    request(`/v1/items/${encodeURIComponent(id)}`, { method: 'PUT', body, schema: S.ItemPut }),

  desktopActions: () => request('/v1/desktop/actions', { schema: z.object({ online: z.boolean(), actions: z.array(S.DesktopAction) }) }),
  sendCommand: (body: { command_id: string; action: string; params: Record<string, string>; expires_at: string; confirmed: boolean }) =>
    request('/v1/desktop/commands', { method: 'POST', body, schema: S.DesktopCommand }),
  commands: () => request('/v1/desktop/commands?limit=60', { schema: z.array(S.DesktopCommand) }),
  command: (id: string) => request(`/v1/desktop/commands/${encodeURIComponent(id)}`, { schema: S.DesktopCommand }),
  cancelCommand: (id: string) =>
    request(`/v1/desktop/commands/${encodeURIComponent(id)}/cancel`, { method: 'POST', schema: S.DesktopCommand }),

  desktopReminders: () =>
    request('/v1/desktop/reminders', { schema: z.array(z.object({ id: z.string().optional(), message: z.string().optional(), due_at: z.string().optional() }).passthrough()) }),
  voices: () => request('/v1/voice/voices', { schema: z.array(S.ServerVoice) }),
  speech: (text: string, voice: string, rate: number, signal?: AbortSignal) =>
    request<ArrayBuffer>('/v1/voice/speech', { method: 'POST', body: { text, voice, rate }, binary: true, timeoutMs: 40000, signal }),
};
