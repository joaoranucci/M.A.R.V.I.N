import * as SQLite from 'expo-sqlite';

// Versioned, additive migrations. Conversation history is NOT memory: separate table, own retention.
const MIGRATIONS: string[][] = [
  [
    `CREATE TABLE kv (key TEXT PRIMARY KEY, value TEXT NOT NULL)`,
    `CREATE TABLE messages (id TEXT PRIMARY KEY, role TEXT NOT NULL, text TEXT NOT NULL, created_at TEXT NOT NULL,
      status TEXT NOT NULL, source TEXT NOT NULL, origin TEXT NOT NULL DEFAULT 'mobile', task_id TEXT, server_id INTEGER,
      engine TEXT, refs TEXT, demo INTEGER NOT NULL DEFAULT 0)`,
    `CREATE INDEX messages_created ON messages(created_at)`,
    `CREATE INDEX messages_task ON messages(task_id)`,
    `CREATE TABLE memories (id TEXT PRIMARY KEY, server_id TEXT UNIQUE, content TEXT NOT NULL, category TEXT NOT NULL,
      origin TEXT NOT NULL, source TEXT NOT NULL, created_at TEXT NOT NULL, updated_at TEXT NOT NULL,
      server_updated_at TEXT, sync_state TEXT NOT NULL, conflict TEXT, demo INTEGER NOT NULL DEFAULT 0)`,
    `CREATE TABLE items (id TEXT PRIMARY KEY, kind TEXT NOT NULL, title TEXT NOT NULL, notes TEXT NOT NULL DEFAULT '',
      due_at TEXT, done INTEGER NOT NULL DEFAULT 0, deleted INTEGER NOT NULL DEFAULT 0, rev INTEGER NOT NULL DEFAULT 0,
      created_at TEXT NOT NULL, updated_at TEXT NOT NULL, sync_state TEXT NOT NULL, notification_id TEXT, conflict TEXT,
      demo INTEGER NOT NULL DEFAULT 0)`,
    `CREATE TABLE activities (id TEXT PRIMARY KEY, kind TEXT NOT NULL, title TEXT NOT NULL, state TEXT NOT NULL,
      detail TEXT, ref TEXT, created_at TEXT NOT NULL, updated_at TEXT NOT NULL, payload TEXT, demo INTEGER NOT NULL DEFAULT 0)`,
    `CREATE INDEX activities_updated ON activities(updated_at)`,
    `CREATE TABLE documents (id TEXT PRIMARY KEY, filename TEXT NOT NULL, category TEXT NOT NULL, chunks INTEGER,
      created_at TEXT, state TEXT NOT NULL, upload_id TEXT, message TEXT, updated_at TEXT NOT NULL, demo INTEGER NOT NULL DEFAULT 0)`,
    `CREATE TABLE outbox (id TEXT PRIMARY KEY, kind TEXT NOT NULL, payload TEXT NOT NULL, created_at TEXT NOT NULL,
      attempts INTEGER NOT NULL DEFAULT 0, last_error TEXT, expires_at TEXT, state TEXT NOT NULL DEFAULT 'pending')`,
    `CREATE TABLE logs (id INTEGER PRIMARY KEY AUTOINCREMENT, at TEXT NOT NULL, level TEXT NOT NULL, scope TEXT NOT NULL,
      message TEXT NOT NULL)`,
  ],
];

let database: SQLite.SQLiteDatabase | null = null;
let opening: Promise<SQLite.SQLiteDatabase> | null = null;

async function migrate(db: SQLite.SQLiteDatabase): Promise<void> {
  await db.execAsync('PRAGMA journal_mode = WAL; PRAGMA foreign_keys = ON;');
  const row = await db.getFirstAsync<{ user_version: number }>('PRAGMA user_version');
  const current = row?.user_version ?? 0;
  for (let version = current; version < MIGRATIONS.length; version++) {
    await db.withExclusiveTransactionAsync(async (txn) => {
      for (const statement of MIGRATIONS[version]) await txn.execAsync(statement);
      await txn.execAsync(`PRAGMA user_version = ${version + 1}`);
    });
  }
}

export function getDb(): Promise<SQLite.SQLiteDatabase> {
  if (database) return Promise.resolve(database);
  if (!opening) {
    opening = SQLite.openDatabaseAsync('marvin.db').then(async (db) => {
      await migrate(db);
      database = db;
      return db;
    });
  }
  return opening;
}

export async function kvGet(key: string): Promise<string | null> {
  const db = await getDb();
  const row = await db.getFirstAsync<{ value: string }>('SELECT value FROM kv WHERE key = ?', key);
  return row?.value ?? null;
}

export async function kvSet(key: string, value: string): Promise<void> {
  const db = await getDb();
  await db.runAsync('INSERT INTO kv(key, value) VALUES (?, ?) ON CONFLICT(key) DO UPDATE SET value = excluded.value', key, value);
}

export async function kvDelete(key: string): Promise<void> {
  const db = await getDb();
  await db.runAsync('DELETE FROM kv WHERE key = ?', key);
}

/** "Apagar dados locais": every table, keeping the schema. */
export async function wipeAll(): Promise<void> {
  const db = await getDb();
  await db.withExclusiveTransactionAsync(async (txn) => {
    for (const table of ['kv', 'messages', 'memories', 'items', 'activities', 'documents', 'outbox', 'logs']) {
      await txn.execAsync(`DELETE FROM ${table}`);
    }
  });
}
