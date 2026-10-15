import { getDb } from '../db/database';
import { redact } from './redact';

type Level = 'info' | 'warn' | 'error';
const MAX_ROWS = 600;
let writes = 0;

async function write(level: Level, scope: string, message: string): Promise<void> {
  const clean = redact(message);
  if (__DEV__) console.log(`[${level}] ${scope}: ${clean}`);
  try {
    const db = await getDb();
    await db.runAsync('INSERT INTO logs(at, level, scope, message) VALUES (?, ?, ?, ?)', new Date().toISOString(), level, scope, clean);
    if (++writes % 50 === 0) {
      await db.runAsync('DELETE FROM logs WHERE id <= (SELECT MAX(id) FROM logs) - ?', MAX_ROWS);
    }
  } catch {
    // Logging must never break a user flow.
  }
}

export const log = {
  info: (scope: string, message: string) => void write('info', scope, message),
  warn: (scope: string, message: string) => void write('warn', scope, message),
  error: (scope: string, message: string, error?: unknown) =>
    void write('error', scope, error ? `${message}: ${error instanceof Error ? error.message : String(error)}` : message),
};

export async function recentLogs(limit = 200): Promise<{ at: string; level: string; scope: string; message: string }[]> {
  const db = await getDb();
  return db.getAllAsync('SELECT at, level, scope, message FROM logs ORDER BY id DESC LIMIT ?', limit);
}
