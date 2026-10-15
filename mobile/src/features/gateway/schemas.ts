import { z } from 'zod';

// Every gateway response is validated before use (contract: docs/mobile/API_GATEWAY.md).
const nullableString = z.string().nullable().optional();

export const ServerInfo = z.object({
  server_id: z.string(),
  name: z.string(),
  version: z.string(),
  api_version: z.number(),
});

export const Health = ServerInfo.extend({
  ok: z.literal(true),
  service: z.literal('marvin-gateway'),
  server_time: z.string(),
});

export const PairResponse = z.object({ device_id: z.string(), token: z.string().min(20), server: ServerInfo });

export const ErrorEnvelope = z.object({
  error: z.object({
    code: z.string(),
    message: z.string(),
    preview: z.object({ title: z.string(), description: z.string(), risk: z.string() }).optional(),
    server_item: z.unknown().optional(),
  }),
});

export const Engine = z.object({
  id: z.enum(['marvin', 'ollama']),
  label: z.string(),
  available: z.boolean(),
  provider: z.string(),
  model: nullableString,
  local_model: z.boolean(),
  tools: z.boolean(),
  note: z.string(),
  llm_configured: z.boolean().optional(),
});

export const DesktopAction = z.object({
  id: z.string(),
  label: z.string(),
  description: z.string(),
  params: z.record(z.string(), z.unknown()),
  requires_confirmation: z.boolean(),
  risk: z.string(),
  verifiable: z.boolean(),
  preview: z.string(),
  available: z.boolean(),
});

export const ServerVoice = z.object({
  id: z.string(),
  label: z.string(),
  gender: z.string(),
  locale: z.string(),
  local: z.boolean(),
  engine: z.string(),
  note: z.string(),
  available: z.boolean(),
  reason: nullableString,
});

export const Capabilities = z.object({
  api_version: z.number(),
  server: ServerInfo,
  events: z.object({ transport: z.string(), max_wait_seconds: z.number() }),
  conversation: z.object({ engines: z.array(Engine), cancel: z.boolean(), history: z.boolean(), streaming: z.boolean() }),
  memories: z.object({ backend: z.string(), search: z.string() }),
  documents: z.object({
    formats: z.array(z.string()),
    max_bytes: z.number(),
    ocr: z.boolean(),
    async_indexing: z.boolean(),
    document_scoped_ask: z.string(),
  }),
  items: z.object({ kinds: z.array(z.string()) }),
  desktop: z.object({ online: z.boolean(), actions: z.array(DesktopAction) }),
  speech: z.object({ voices: z.array(ServerVoice) }),
});

export const Status = z.object({
  server_time: z.string(),
  assistant: z.object({ state: z.string(), queue: z.number().optional(), phase: z.string().optional(), reason: nullableString }),
  vault: z.object({ state: z.string(), code: nullableString, message: nullableString, version: nullableString }),
  desktop_agent: z.object({ state: z.string(), reason: nullableString }),
  approval_pending: z.boolean(),
});

export const GatewayEvent = z.object({ seq: z.number(), type: z.string(), time: z.string(), data: z.unknown() });
export const EventsBatch = z.object({
  events: z.array(GatewayEvent),
  last_seq: z.number(),
  reset: z.boolean(),
  server_time: z.string(),
});

export const SendMessageResponse = z.object({
  task_id: z.string(),
  engine: z.string(),
  duplicate: z.boolean(),
  state: z.string(),
});

export const AssistantTask = z.object({
  id: z.string(),
  engine: z.string(),
  objective: z.string(),
  state: z.string(),
  answer: nullableString,
  created_at: z.string(),
  updated_at: z.string(),
  origin: z.string().optional(),
});

export const HistoryMessage = z.object({
  id: z.number(),
  role: z.enum(['user', 'assistant']),
  text: z.string(),
  created_at: nullableString,
});

export const MemoryOrigin = z.enum(['user_request', 'assistant_inference', 'imported']);
export const Memory = z.object({
  id: z.string(),
  content: z.string(),
  category: z.string(),
  origin: MemoryOrigin,
  source: z.string(),
  client_id: nullableString,
  created_at: z.string(),
  updated_at: z.string(),
  duplicate: z.boolean().optional(),
});

export const Document = z.object({
  document_id: z.string(),
  filename: z.string(),
  category: z.string(),
  chunks: z.number().nullable().optional(),
  created_at: nullableString,
});

export const Upload = z.object({
  upload_id: z.string(),
  filename: z.string(),
  category: z.string(),
  size: z.number(),
  state: z.enum(['received', 'processing', 'available', 'failed']),
  message: z.string(),
  document_id: nullableString,
  chunks: z.number().nullable().optional(),
  created_at: z.string(),
  updated_at: z.string(),
  duplicate: z.boolean().optional(),
});

export const SearchHit = z.object({
  chunk_id: z.string(),
  document_id: z.string(),
  filename: z.string(),
  part: z.number(),
  category: z.string(),
  score: z.number(),
  excerpt: z.string(),
});

export const Source = z.object({
  document_id: nullableString,
  filename: nullableString,
  part: z.number().nullable().optional(),
  chunk_id: nullableString,
  excerpt: z.string(),
  score: z.number().optional(),
});

export const AskResult = z.object({
  answer: z.string(),
  generated: z.boolean(),
  model: nullableString,
  sources: z.array(Source),
  document_id: nullableString,
  sources_in_document: z.number(),
  llm_unavailable_reason: nullableString,
});

export const Chunk = z.object({
  chunk_id: z.string(),
  document_id: nullableString,
  filename: z.string(),
  part: z.number().nullable().optional(),
  total: z.number().nullable().optional(),
  category: z.string(),
  text: z.string(),
});

export const Item = z.object({
  id: z.string(),
  kind: z.enum(['task', 'reminder', 'note']),
  title: z.string(),
  notes: z.string(),
  due_at: nullableString,
  done: z.boolean(),
  deleted: z.boolean(),
  rev: z.number(),
  created_at: z.string(),
  updated_at: z.string(),
  updated_by: z.string(),
});
export const ItemList = z.object({ items: z.array(Item), server_time: z.string() });
export const ItemPut = z.object({ status: z.string(), item: Item });

export const DesktopCommand = z.object({
  command_id: z.string(),
  action: z.string(),
  params: z.record(z.string(), z.unknown()),
  state: z.string(),
  message: z.string(),
  verified: z.boolean(),
  result: z.unknown().nullable().optional(),
  created_at: z.string(),
  expires_at: z.string(),
  started_at: nullableString,
  finished_at: nullableString,
  updated_at: z.string(),
  duplicate: z.boolean().optional(),
});

export const LinkedDevice = z.object({
  id: z.string(),
  name: z.string(),
  platform: z.string(),
  app_version: z.string(),
  created_at: z.string(),
  last_seen_at: nullableString,
  revoked_at: nullableString,
  current: z.boolean(),
});

export const Approval = z.object({ id: z.string(), title: z.string(), details: z.record(z.string(), z.unknown()) });

export type TCapabilities = z.infer<typeof Capabilities>;
export type TStatus = z.infer<typeof Status>;
export type TGatewayEvent = z.infer<typeof GatewayEvent>;
export type TMemory = z.infer<typeof Memory>;
export type TUpload = z.infer<typeof Upload>;
export type TSearchHit = z.infer<typeof SearchHit>;
export type TAskResult = z.infer<typeof AskResult>;
export type TChunk = z.infer<typeof Chunk>;
export type TItem = z.infer<typeof Item>;
export type TDesktopCommand = z.infer<typeof DesktopCommand>;
export type TDesktopAction = z.infer<typeof DesktopAction>;
export type TServerVoice = z.infer<typeof ServerVoice>;
export type TApproval = z.infer<typeof Approval>;
export type TLinkedDevice = z.infer<typeof LinkedDevice>;
export type TAssistantTask = z.infer<typeof AssistantTask>;
export type TEngine = z.infer<typeof Engine>;
