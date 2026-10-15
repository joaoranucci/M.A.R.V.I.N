import { Directory, Paths } from 'expo-file-system';
import * as Notifications from 'expo-notifications';
import { useCallback, useEffect, useState } from 'react';
import { Alert, ScrollView, StyleSheet, Text } from 'react-native';
import { Banner, Button, Row, Segmented, SectionTitle } from '../../components/ui';
import { reloadLocalData } from '../../core/bootstrap';
import { getDb, wipeAll } from '../../core/db/database';
import { resetEventCursor } from '../../core/events/eventStream';
import { useConnectionInfo } from '../../core/security/credentials';
import { useSettings } from '../../core/settings';
import { dropOutbox, outboxRows, syncNow, useSync, type OutboxRow } from '../../core/sync/syncEngine';
import { clearConversation } from '../../features/conversation/repo';
import { signOut } from '../../features/gateway/pairing';
import { cleanupTempAudio } from '../../features/voice/tts';
import { colors, space, type } from '../../theme/tokens';

const KIND_LABEL: Record<string, string> = {
  'memory.create': 'Nova memória',
  'memory.update': 'Edição de memória',
  'memory.delete': 'Exclusão de memória',
  'item.put': 'Tarefa/lembrete',
  'document.upload': 'Envio de documento',
  'desktop.command': 'Comando para o PC',
};

export default function StorageSettings() {
  const s = useSettings();
  const sync = useSync();
  const [counts, setCounts] = useState<Record<string, number>>({});
  const [outbox, setOutbox] = useState<OutboxRow[]>([]);

  const load = useCallback(async () => {
    const db = await getDb();
    const result: Record<string, number> = {};
    for (const table of ['messages', 'memories', 'items', 'activities', 'documents']) {
      const row = await db.getFirstAsync<{ n: number }>(`SELECT COUNT(*) AS n FROM ${table}`);
      result[table] = row?.n ?? 0;
    }
    setCounts(result);
    setOutbox(await outboxRows());
  }, []);

  useEffect(() => {
    void load();
  }, [load, sync.pending, sync.lastSyncAt]);

  const wipe = () =>
    Alert.alert(
      'Apagar todos os dados locais?',
      'Remove conversa, memórias, tarefas, documentos em cache, fila de sincronização e credenciais deste celular. O que já está no PC não é apagado.',
      [
        { text: 'Cancelar', style: 'cancel' },
        {
          text: 'Apagar',
          style: 'destructive',
          onPress: async () => {
            if (useConnectionInfo.getState().connection) await signOut();
            await Notifications.cancelAllScheduledNotificationsAsync();
            await wipeAll();
            cleanupTempAudio();
            for (const dir of ['upload-outbox']) {
              const d = new Directory(Paths.document, dir);
              if (d.exists) d.delete();
            }
            resetEventCursor();
            await s.load();
            await reloadLocalData();
            await load();
            Alert.alert('Pronto', 'Os dados locais foram apagados.');
          },
        },
      ],
    );

  const pendingRows = outbox.filter((r) => r.state === 'pending');
  const stuck = outbox.filter((r) => r.state !== 'pending');

  return (
    <ScrollView style={{ backgroundColor: colors.bg }} contentContainerStyle={styles.content}>
      <SectionTitle>Neste celular</SectionTitle>
      <Row title="Mensagens da conversa" subtitle={String(counts.messages ?? 0)} icon="chatbubbles-outline" />
      <Row title="Memórias" subtitle={String(counts.memories ?? 0)} icon="sparkles-outline" />
      <Row title="Tarefas, lembretes e notas" subtitle={String(counts.items ?? 0)} icon="checkbox-outline" />
      <Row title="Atividades registradas" subtitle={String(counts.activities ?? 0)} icon="pulse-outline" />
      <Text style={type.caption}>Dados guardados no SQLite do app. O token de acesso ao PC fica no armazenamento seguro do Android.</Text>

      <SectionTitle>Histórico de conversa</SectionTitle>
      <Text style={type.caption}>A conversa não vira memória permanente. Mensagens mais antigas que o prazo são apagadas deste celular.</Text>
      <Segmented
        value={String(s.historyRetentionDays)}
        onChange={(v) => void s.update({ historyRetentionDays: Number(v) })}
        options={[{ value: '7', label: '7 dias' }, { value: '30', label: '30 dias' }, { value: '90', label: '90 dias' }, { value: '0', label: 'Manter' }]}
      />
      <Button
        label="Apagar conversa deste celular"
        icon="trash-outline"
        onPress={() =>
          Alert.alert('Apagar conversa?', 'O histórico do PC não é alterado.', [
            { text: 'Cancelar', style: 'cancel' },
            { text: 'Apagar', style: 'destructive', onPress: () => void clearConversation().then(load) },
          ])
        }
      />

      <SectionTitle>Sincronização</SectionTitle>
      <Row title="Pendentes de envio" subtitle={`${pendingRows.length}${sync.lastSyncAt ? ` · última sincronização ${new Date(sync.lastSyncAt).toLocaleTimeString('pt-BR')}` : ''}`} icon="sync-outline" />
      <Button label="Sincronizar agora" icon="refresh" onPress={() => void syncNow('manual').then(load)} loading={sync.running} />
      {stuck.map((row) => (
        <Banner key={row.id} tone={row.state === 'expired' ? 'warn' : 'error'} text={`${KIND_LABEL[row.kind] ?? row.kind}: ${row.state === 'expired' ? 'perdeu a validade' : 'recusado'} — ${row.last_error ?? ''}`}>
          <Button label="Descartar" compact onPress={() => void dropOutbox(row.id).then(load)} style={{ alignSelf: 'flex-start' }} />
        </Banner>
      ))}

      <SectionTitle>Apagar</SectionTitle>
      <Button label="Apagar todos os dados locais" icon="nuclear-outline" variant="danger" onPress={wipe} />
    </ScrollView>
  );
}

const styles = StyleSheet.create({ content: { padding: space.xl, gap: space.sm, paddingBottom: space.xxxl } });
