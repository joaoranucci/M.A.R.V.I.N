import { Ionicons } from '@expo/vector-icons';
import { useCallback, useEffect, useState } from 'react';
import { Alert, Linking, Pressable, RefreshControl, ScrollView, StyleSheet, Text, View } from 'react-native';
import { useSafeAreaInsets } from 'react-native-safe-area-context';
import { Banner, Button, Chip, EmptyState, Field, Segmented, SectionTitle } from '../../components/ui';
import { useConnectivity } from '../../core/net/connectivity';
import { syncNow } from '../../core/sync/syncEngine';
import {
  assistantStateLabel,
  desktopStateLabel,
  isFinal,
  uploadStateLabel,
  useActivities,
  type Activity,
} from '../../features/activities/repo';
import { formatWhen, parseDate } from '../../features/assistant/nlp/dates';
import { cancelCommand, sendCommand } from '../../features/devices/desktop';
import { gateway } from '../../features/gateway/api';
import {
  loadItems,
  notificationStatus,
  removeItem,
  resolveItemConflict,
  saveItem,
  setDone,
  useItems,
  type Item,
  type ItemKind,
} from '../../features/tasks/service';
import { colors, radius, space, type } from '../../theme/tokens';

type Tab = 'personal' | 'ai' | 'desktop';

export default function Activities() {
  const insets = useSafeAreaInsets();
  const [tab, setTab] = useState<Tab>('personal');
  const [refreshing, setRefreshing] = useState(false);
  const onRefresh = useCallback(async () => {
    setRefreshing(true);
    await syncNow('manual');
    await loadItems();
    setRefreshing(false);
  }, []);
  return (
    <View style={[styles.screen, { paddingTop: insets.top + space.md }]}>
      <Text style={[type.title, styles.title]} accessibilityRole="header">
        Atividades
      </Text>
      <View style={{ paddingHorizontal: space.xl, marginBottom: space.md }}>
        <Segmented
          value={tab}
          onChange={setTab}
          options={[
            { value: 'personal', label: 'Minhas tarefas' },
            { value: 'ai', label: 'Pedidos à IA' },
            { value: 'desktop', label: 'Computador' },
          ]}
        />
      </View>
      <ScrollView
        contentContainerStyle={styles.list}
        refreshControl={<RefreshControl refreshing={refreshing} onRefresh={onRefresh} tintColor={colors.cyan} />}
        keyboardShouldPersistTaps="handled"
      >
        {tab === 'personal' && <Personal />}
        {tab === 'ai' && <AiRequests />}
        {tab === 'desktop' && <DesktopActions />}
      </ScrollView>
    </View>
  );
}

const KIND_LABEL: Record<ItemKind, string> = { task: 'Tarefa', reminder: 'Lembrete', note: 'Nota' };

function Personal() {
  const { items, notifications } = useItems();
  const [title, setTitle] = useState('');
  const [kind, setKind] = useState<ItemKind>('task');
  const [when, setWhen] = useState('');
  const [message, setMessage] = useState<string | null>(null);
  useEffect(() => {
    void notificationStatus(false);
  }, []);
  const add = async () => {
    if (!title.trim()) return;
    const match = when.trim() ? parseDate(when) : null;
    if (when.trim() && !match) {
      setMessage('Não entendi a data. Exemplos: “amanhã às 9”, “daqui a 30 minutos”, “sexta às 14:30”.');
      return;
    }
    const result = await saveItem({ kind: match && kind === 'task' ? 'reminder' : kind, title, due_at: match ? match.date.toISOString() : null });
    setTitle('');
    setWhen('');
    setMessage(result.notificationIssue);
  };
  const open = items.filter((i) => !i.done);
  const done = items.filter((i) => i.done);
  return (
    <>
      <Field label="Nova tarefa, lembrete ou nota" value={title} onChangeText={setTitle} placeholder="ex.: revisar o projeto dos óculos" />
      <Segmented value={kind} onChange={setKind} options={[{ value: 'task', label: 'Tarefa' }, { value: 'reminder', label: 'Lembrete' }, { value: 'note', label: 'Nota' }]} />
      {kind !== 'note' && <Field label="Quando (opcional)" value={when} onChangeText={setWhen} placeholder="amanhã às 9 · daqui a 20 minutos" />}
      <Button label="Adicionar" icon="add" variant="primary" onPress={() => void add()} disabled={!title.trim()} />
      {message && <Banner tone="warn" text={message} />}
      {notifications === 'denied' && (
        <Banner tone="warn" text="Notificações desativadas: lembretes só aparecem dentro do app. O sistema pode limitar ou adiar avisos conforme suas configurações.">
          <Button label="Abrir configurações" compact onPress={() => void Linking.openSettings()} style={{ alignSelf: 'flex-start' }} />
        </Banner>
      )}
      <SectionTitle>{`Pendentes (${open.length})`}</SectionTitle>
      {open.length === 0 ? (
        <EmptyState icon="checkmark-done-outline" title="Tudo em dia" text="Crie por aqui ou diga: “Marvin, me lembre de beber água daqui a 30 minutos”." />
      ) : (
        open.map((item) => <ItemRow key={item.id} item={item} />)
      )}
      {done.length > 0 && <SectionTitle>{`Concluídas (${done.length})`}</SectionTitle>}
      {done.slice(0, 20).map((item) => (
        <ItemRow key={item.id} item={item} />
      ))}
    </>
  );
}

function ItemRow({ item }: { item: Item }) {
  const due = item.due_at ? new Date(item.due_at) : null;
  const overdue = due && !item.done && due.getTime() < Date.now();
  const remove = () =>
    Alert.alert('Excluir?', item.title, [
      { text: 'Cancelar', style: 'cancel' },
      { text: 'Excluir', style: 'destructive', onPress: () => void removeItem(item) },
    ]);
  return (
    <View style={styles.item}>
      <View style={{ flexDirection: 'row', gap: space.md, alignItems: 'flex-start' }}>
        {item.kind !== 'note' ? (
          <Pressable
            accessibilityRole="checkbox"
            accessibilityState={{ checked: !!item.done }}
            accessibilityLabel={`Concluir ${item.title}`}
            onPress={() => void setDone(item, !item.done)}
            hitSlop={10}
            style={[styles.check, item.done ? styles.checkOn : null]}
          >
            {item.done ? <Ionicons name="checkmark" size={18} color="#03121A" /> : null}
          </Pressable>
        ) : (
          <Ionicons name="document-text-outline" size={22} color={colors.cyan} />
        )}
        <View style={{ flex: 1, gap: space.xs }}>
          <Text style={[type.body, item.done ? { textDecorationLine: 'line-through', color: colors.textMuted } : null]}>{item.title}</Text>
          <View style={styles.chips}>
            <Chip label={KIND_LABEL[item.kind]} />
            {due && <Chip label={formatWhen(due)} tone={overdue ? 'amber' : 'cyan'} icon="time-outline" />}
            {item.kind === 'reminder' && !item.notification_id && !item.done && due && due.getTime() > Date.now() && <Chip label="sem notificação" tone="amber" />}
            {item.sync_state === 'pending' && <Chip label="aguardando sincronizar" tone="muted" />}
            {item.sync_state === 'local_only' && <Chip label="só neste aparelho" tone="muted" />}
          </View>
        </View>
        <Pressable onPress={remove} accessibilityRole="button" accessibilityLabel={`Excluir ${item.title}`} hitSlop={10} style={{ padding: 4 }}>
          <Ionicons name="trash-outline" size={20} color={colors.textMuted} />
        </Pressable>
      </View>
      {item.sync_state === 'conflict' && (
        <Banner tone="warn" text="Este item foi alterado em outro dispositivo. Qual versão manter?">
          <View style={{ flexDirection: 'row', gap: space.sm }}>
            <Button label="A deste celular" compact onPress={() => void resolveItemConflict(item.id, 'mine')} />
            <Button label="A do outro" compact onPress={() => void resolveItemConflict(item.id, 'server')} />
          </View>
        </Banner>
      )}
    </View>
  );
}

function ActivityRow({ activity, labels, onCancel, onRetry }: { activity: Activity; labels: Record<string, string>; onCancel?: () => void; onRetry?: () => void }) {
  const final = isFinal(activity.kind, activity.state);
  const tone = ['completed', 'available'].includes(activity.state)
    ? 'success'
    : ['failed', 'rejected', 'expired', 'needs_decision'].includes(activity.state)
      ? 'danger'
      : ['dispatched', 'needs_reconciliation', 'awaiting_confirmation', 'queued_offline', 'simulated', 'waiting_user'].includes(activity.state)
        ? 'amber'
        : 'cyan';
  return (
    <View style={styles.item}>
      <Text style={type.label} numberOfLines={2}>
        {activity.title}
      </Text>
      <View style={styles.chips}>
        <Chip label={labels[activity.state] ?? activity.state} tone={tone} />
        <Chip label={new Date(activity.updated_at).toLocaleString('pt-BR', { dateStyle: 'short', timeStyle: 'short' })} tone="muted" />
      </View>
      {!!activity.detail && (
        <Text style={type.caption} numberOfLines={4} selectable>
          {activity.detail}
        </Text>
      )}
      {(onCancel || onRetry) && (
        <View style={{ flexDirection: 'row', gap: space.sm }}>
          {onCancel && !final && <Button label="Cancelar" compact icon="close" onPress={onCancel} />}
          {onRetry && <Button label="Decidir de novo" compact icon="refresh" onPress={onRetry} />}
        </View>
      )}
    </View>
  );
}

function AiRequests() {
  const items = useActivities((s) => s.items);
  const online = useConnectivity((s) => s.gateway === 'online');
  const ai = items.filter((a) => a.kind === 'assistant');
  const uploads = items.filter((a) => a.kind === 'upload');
  const cancel = async (activity: Activity) => {
    try {
      await gateway.cancelTask(activity.id);
      await syncNow('cancel');
    } catch (error) {
      Alert.alert('Não foi possível cancelar', error instanceof Error ? error.message : '');
    }
  };
  return (
    <>
      <Text style={type.caption}>Pedidos processados pelo MARVIN do PC. Você pode fechar o app: o andamento fica registrado aqui.</Text>
      {ai.length === 0 && uploads.length === 0 && <EmptyState icon="sparkles-outline" title="Nenhum pedido ainda" text="Converse com o MARVIN na tela principal." />}
      {ai.map((a) => (
        <ActivityRow key={a.id} activity={a} labels={assistantStateLabel} onCancel={online ? () => void cancel(a) : undefined} />
      ))}
      {uploads.length > 0 && <SectionTitle>Documentos</SectionTitle>}
      {uploads.map((a) => (
        <ActivityRow key={a.id} activity={a} labels={uploadStateLabel} />
      ))}
    </>
  );
}

function DesktopActions() {
  const items = useActivities((s) => s.items).filter((a) => a.kind === 'desktop');
  const connectivity = useConnectivity();
  const [reminders, setReminders] = useState<{ id?: string; message?: string; due_at?: string }[]>([]);
  useEffect(() => {
    if (connectivity.gateway === 'online') {
      gateway.desktopReminders().then(setReminders).catch(() => setReminders([]));
    }
  }, [connectivity.gateway]);
  const retry = async (activity: Activity) => {
    const payload = activity.payload ? (JSON.parse(activity.payload) as { request?: { action: string; params: Record<string, string>; summary: string } }) : {};
    if (!payload.request) return;
    Alert.alert('Executar agora?', payload.request.summary, [
      { text: 'Não', style: 'cancel' },
      { text: 'Executar', onPress: () => void sendCommand(payload.request!, true) },
    ]);
  };
  return (
    <>
      {connectivity.desktop !== 'online' && <Banner tone="warn" text={connectivity.gateway === 'online' ? 'Agente do computador inativo: ações não serão executadas.' : 'Computador indisponível.'} />}
      <Text style={type.caption}>
        “Enviada ao Windows” significa que o pedido foi aceito, mas o resultado na tela não pôde ser verificado. Comandos vencidos nunca são executados depois.
      </Text>
      {items.length === 0 && <EmptyState icon="desktop-outline" title="Nenhuma ação no PC" text="Experimente: “Marvin, crie uma pasta para o projeto óculos”." />}
      {items.map((a) => (
        <ActivityRow
          key={a.id}
          activity={a}
          labels={desktopStateLabel}
          onCancel={a.state === 'received' ? () => void cancelCommand(a.id).catch(() => undefined) : undefined}
          onRetry={a.state === 'needs_decision' ? () => void retry(a) : undefined}
        />
      ))}
      {reminders.length > 0 && (
        <>
          <SectionTitle>Lembretes do PC</SectionTitle>
          {reminders.map((r, i) => (
            <View key={r.id ?? i} style={styles.item}>
              <Text style={type.body}>{r.message}</Text>
              {r.due_at && <Text style={type.caption}>{new Date(r.due_at).toLocaleString('pt-BR')}</Text>}
            </View>
          ))}
        </>
      )}
    </>
  );
}

const styles = StyleSheet.create({
  screen: { flex: 1, backgroundColor: colors.bg },
  title: { paddingHorizontal: space.xl, marginBottom: space.md },
  list: { paddingHorizontal: space.xl, paddingBottom: space.xxxl, gap: space.md },
  chips: { flexDirection: 'row', flexWrap: 'wrap', gap: space.sm },
  item: {
    backgroundColor: colors.surface,
    borderColor: colors.border,
    borderWidth: StyleSheet.hairlineWidth,
    borderRadius: radius.lg,
    padding: space.lg,
    gap: space.sm,
  },
  check: {
    width: 28,
    height: 28,
    borderRadius: 8,
    borderWidth: 2,
    borderColor: colors.cyan,
    alignItems: 'center',
    justifyContent: 'center',
    marginTop: 2,
  },
  checkOn: { backgroundColor: colors.cyan },
});
