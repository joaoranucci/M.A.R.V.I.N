import * as DocumentPicker from 'expo-document-picker';
import { Directory, File, Paths } from 'expo-file-system';
import { create } from 'zustand';
import { getDb } from '../../core/db/database';
import { onEvent } from '../../core/events/eventStream';
import { newId, nowIso } from '../../core/ids';
import { log } from '../../core/logging/logger';
import { useConnectivity } from '../../core/net/connectivity';
import { settings } from '../../core/settings';
import { enqueue, registerProcessor, registerPuller } from '../../core/sync/syncEngine';
import { upsertActivity } from '../activities/repo';
import { gateway } from '../gateway/api';
import { GatewayError } from '../gateway/client';
import { Upload, type TUpload } from '../gateway/schemas';

/**
 * Library documents. States are the server's: received (upload done) is NOT
 * "available": indexing happens afterwards (processing) and may fail.
 * Document text is shown as data only — it never reaches the intent router.
 */
export type DocState = 'queued_offline' | 'uploading' | 'received' | 'processing' | 'available' | 'failed';

export interface LibraryDocument {
  id: string;
  filename: string;
  category: string;
  chunks: number | null;
  created_at: string | null;
  state: DocState;
  upload_id: string | null;
  message: string | null;
  updated_at: string;
  demo: number;
}

export const useDocuments = create<{ items: LibraryDocument[] }>(() => ({ items: [] }));
const outboxDir = new Directory(Paths.document, 'upload-outbox');

const MIME_BY_EXT: Record<string, string> = {
  '.pdf': 'application/pdf',
  '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
  '.json': 'application/json',
  '.xml': 'application/xml',
  '.html': 'text/html',
  '.htm': 'text/html',
  '.csv': 'text/csv',
  '.md': 'text/markdown',
};

export function extensionOf(name: string): string {
  const match = /\.[A-Za-z0-9]+$/.exec(name);
  return match ? match[0].toLowerCase() : '';
}

export function acceptedFormats(): string[] {
  return useConnectivity.getState().capabilities?.documents.formats ?? [];
}

export function maxBytes(): number {
  return useConnectivity.getState().capabilities?.documents.max_bytes ?? 20 * 1024 * 1024;
}

export function checkFile(name: string, size: number): string | null {
  const formats = acceptedFormats();
  const ext = extensionOf(name);
  if (!formats.length) return 'Conecte ao computador uma vez para saber quais formatos a biblioteca aceita.';
  if (!formats.includes(ext)) return `${ext || 'Sem extensão'}: formato não aceito pela biblioteca. Aceitos: ${formats.join(' ')}`;
  if (size > maxBytes()) return 'Arquivo acima de 20 MB.';
  if (size === 0) return 'Arquivo vazio.';
  return null;
}

export async function loadDocuments(): Promise<LibraryDocument[]> {
  const db = await getDb();
  const rows = await db.getAllAsync<LibraryDocument>(
    'SELECT * FROM documents WHERE demo = ? ORDER BY COALESCE(created_at, updated_at) DESC',
    settings().demoMode ? 1 : 0,
  );
  useDocuments.setState({ items: rows });
  return rows;
}

async function saveDoc(doc: LibraryDocument) {
  const db = await getDb();
  await db.runAsync(
    `INSERT INTO documents(id, filename, category, chunks, created_at, state, upload_id, message, updated_at, demo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
     ON CONFLICT(id) DO UPDATE SET filename = excluded.filename, category = excluded.category, chunks = excluded.chunks,
       created_at = COALESCE(excluded.created_at, documents.created_at), state = excluded.state, upload_id = excluded.upload_id,
       message = excluded.message, updated_at = excluded.updated_at`,
    doc.id, doc.filename, doc.category, doc.chunks, doc.created_at, doc.state, doc.upload_id, doc.message, doc.updated_at, doc.demo,
  );
}

async function applyUpload(localId: string, upload: TUpload) {
  const db = await getDb();
  // Events can arrive before the POST response: converge on a single row per upload.
  const rows = await db.getAllAsync<LibraryDocument>('SELECT * FROM documents WHERE id = ? OR upload_id = ?', localId, upload.upload_id);
  const keep = rows.find((r) => r.id === localId) ?? rows[0];
  const finalId = upload.state === 'available' && upload.document_id ? upload.document_id : keep?.id ?? localId;
  await db.runAsync('DELETE FROM documents WHERE (upload_id = ? OR id = ?) AND id != ?', upload.upload_id, keep?.id ?? localId, finalId);
  await saveDoc({
    id: finalId, filename: upload.filename, category: upload.category, chunks: upload.chunks ?? null,
    created_at: keep?.created_at ?? upload.created_at, state: upload.state, upload_id: upload.upload_id, message: upload.message,
    updated_at: nowIso(), demo: 0,
  });
  await upsertActivity({ id: `upload-${upload.upload_id}`, kind: 'upload', title: upload.filename, state: upload.state, detail: upload.message, ref: upload.document_id ?? null });
  await loadDocuments();
}

export interface PickedFile {
  uri: string;
  name: string;
  size: number;
  mimeType: string | null;
}

export async function pickDocument(): Promise<PickedFile | null> {
  const formats = acceptedFormats();
  const result = await DocumentPicker.getDocumentAsync({
    type: formats.length ? [...new Set(formats.map((ext) => MIME_BY_EXT[ext] ?? 'text/*')), 'application/octet-stream'] : '*/*',
    copyToCacheDirectory: true,
    multiple: false,
  });
  if (result.canceled || !result.assets?.[0]) return null;
  const asset = result.assets[0];
  return { uri: asset.uri, name: asset.name, size: asset.size ?? new File(asset.uri).size, mimeType: asset.mimeType ?? null };
}

/** Upload is idempotent (client id); when offline the file is kept and sent later. */
export async function uploadDocument(file: PickedFile, category: string): Promise<{ queued: boolean; error: string | null }> {
  const problem = checkFile(file.name, file.size);
  if (problem) return { queued: false, error: problem };
  const clientId = newId();
  const localId = `local-${clientId}`;
  await saveDoc({ id: localId, filename: file.name, category, chunks: null, created_at: nowIso(), state: 'uploading', upload_id: null, message: 'Enviando ao PC…', updated_at: nowIso(), demo: 0 });
  if (!outboxDir.exists) outboxDir.create({ intermediates: true });
  const keptDir = new Directory(outboxDir, clientId);
  keptDir.create({ intermediates: true });
  const kept = new File(keptDir, file.name);
  new File(file.uri).copy(kept);
  await loadDocuments();
  const online = useConnectivity.getState().gateway === 'online';
  if (!online) {
    await saveDoc({ id: localId, filename: file.name, category, chunks: null, created_at: nowIso(), state: 'queued_offline', upload_id: null, message: 'Será enviado quando o PC estiver disponível.', updated_at: nowIso(), demo: 0 });
    await loadDocuments();
  }
  await enqueue('document.upload', { clientId, localId, uri: kept.uri, name: file.name, category, mimeType: file.mimeType }, { id: `upload-${clientId}` });
  return { queued: !online, error: null };
}

registerProcessor('document.upload', async (payload: { clientId: string; localId: string; uri: string; name: string; category: string; mimeType: string | null }) => {
  const form = new FormData();
  form.append('client_id', payload.clientId);
  form.append('category', payload.category);
  // The global fetch in SDK 57 is Expo's: it accepts expo-file-system File (a Blob), named after the kept copy.
  const file = new File(payload.uri);
  if (!file.exists) {
    const db = await getDb();
    await db.runAsync("UPDATE documents SET state = 'failed', message = ?, updated_at = ? WHERE id = ?", 'A cópia local do arquivo não existe mais. Envie novamente.', nowIso(), payload.localId);
    await loadDocuments();
    return;
  }
  form.append('file', file);
  try {
    const upload = await gateway.upload(form);
    await applyUpload(payload.localId, upload);
  } catch (error) {
    if (error instanceof GatewayError && !error.retryable && error.kind === 'http') {
      const db = await getDb();
      await db.runAsync("UPDATE documents SET state = 'failed', message = ?, updated_at = ? WHERE id = ?", error.message, nowIso(), payload.localId);
      await loadDocuments();
      cleanupKept(payload.clientId);
      return;
    }
    throw error;
  }
  cleanupKept(payload.clientId);
});

function cleanupKept(clientId: string) {
  try {
    const dir = new Directory(outboxDir, clientId);
    if (dir.exists) dir.delete();
  } catch (error) {
    log.warn('documents', `limpeza: ${error instanceof Error ? error.message : String(error)}`);
  }
}

export async function deleteDocument(id: string): Promise<void> {
  await gateway.deleteDocument(id);
  const db = await getDb();
  await db.runAsync('DELETE FROM documents WHERE id = ?', id);
  await loadDocuments();
}

registerPuller('documents', async () => {
  if (settings().demoMode) return;
  const remote = await gateway.documents();
  const db = await getDb();
  const ids = new Set(remote.map((d) => d.document_id));
  for (const d of remote) {
    await saveDoc({
      id: d.document_id, filename: d.filename, category: d.category, chunks: d.chunks ?? null, created_at: d.created_at ?? null,
      state: 'available', upload_id: null, message: null, updated_at: nowIso(), demo: 0,
    });
  }
  // Removed on the PC: drop available entries that no longer exist; keep in-flight uploads.
  const local = await db.getAllAsync<LibraryDocument>("SELECT * FROM documents WHERE demo = 0 AND state = 'available'");
  for (const doc of local) if (!ids.has(doc.id)) await db.runAsync('DELETE FROM documents WHERE id = ?', doc.id);
  // Refresh uploads still in progress (events may have been missed while closed).
  const pending = await db.getAllAsync<LibraryDocument>("SELECT * FROM documents WHERE demo = 0 AND upload_id IS NOT NULL AND state IN ('received', 'processing')");
  for (const doc of pending) {
    try {
      await applyUpload(doc.id, await gateway.uploadState(doc.upload_id as string));
    } catch (error) {
      log.warn('documents', `estado do envio: ${error instanceof Error ? error.message : String(error)}`);
    }
  }
  await loadDocuments();
});

onEvent('document.upload', async (event) => {
  const parsed = Upload.safeParse(event.data);
  if (parsed.success) await applyUpload(`upload-${parsed.data.upload_id}`, parsed.data);
});

onEvent('document.deleted', async (event) => {
  const id = (event.data as { document_id?: string }).document_id;
  if (!id) return;
  const db = await getDb();
  await db.runAsync('DELETE FROM documents WHERE id = ?', id);
  await loadDocuments();
});
