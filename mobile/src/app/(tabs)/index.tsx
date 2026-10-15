import { Ionicons } from '@expo/vector-icons';
import { router } from 'expo-router';
import { useEffect, useRef, useState } from 'react';
import {
  KeyboardAvoidingView,
  Linking,
  Platform,
  Pressable,
  ScrollView,
  StyleSheet,
  Text,
  TextInput,
  View,
  useWindowDimensions,
} from 'react-native';
import { useSafeAreaInsets } from 'react-native-safe-area-context';
import { Orb } from '../../components/Orb';
import { Banner, Button, Card, Chip, Dot, IconButton } from '../../components/ui';
import { describeAvailability, useConnectivity } from '../../core/net/connectivity';
import { useSettings } from '../../core/settings';
import { useReduceMotion } from '../../core/useReduceMotion';
import {
  cancelCurrent,
  cancelListening,
  confirmCommand,
  decideApproval,
  finishListening,
  interruptSpeech,
  queueOfflineCommand,
  setWakeWord,
  submit,
  tapCore,
  useAssistant,
  type Phase,
} from '../../features/assistant/controller';
import { useConversation } from '../../features/conversation/repo';
import { colors, fonts, radius, space, type } from '../../theme/tokens';

const ORB_LABEL: Record<Phase, string> = {
  idle: 'Falar com o MARVIN',
  offline: 'Falar com o MARVIN (sem conexão com o PC)',
  listening: 'Concluir e enviar o que foi dito',
  processing: 'MARVIN está pensando',
  speaking: 'Interromper a fala do MARVIN',
  executing: 'MARVIN está executando',
  awaiting: 'MARVIN aguarda sua decisão',
};

function greeting(name: string): string {
  const hour = new Date().getHours();
  const part = hour < 5 ? 'Boa noite' : hour < 12 ? 'Bom dia' : hour < 18 ? 'Boa tarde' : 'Boa noite';
  return `${part}, ${name}.`;
}

export default function Home() {
  const insets = useSafeAreaInsets();
  const { width, height } = useWindowDimensions();
  const assistant = useAssistant();
  const connectivity = useConnectivity();
  const { demoMode, userName } = useSettings();
  const reduceMotion = useReduceMotion();
  const availability = describeAvailability(connectivity, demoMode);
  const lastAssistant = useConversation((s) => {
    for (let i = s.messages.length - 1; i >= 0; i--) if (s.messages[i].role === 'assistant') return s.messages[i];
    return undefined;
  });
  const [expanded, setExpanded] = useState(false);
  const orbSize = Math.min(width * 0.78, height * 0.36, 340);
  const dotColor = availability.tone === 'ok' ? colors.success : availability.tone === 'warn' ? colors.amber : colors.slate;
  const busy = assistant.phase === 'processing' || assistant.phase === 'executing';
  const reply = assistant.lastReply?.text ?? lastAssistant?.text ?? null;

  return (
    <View style={[styles.screen, { paddingTop: insets.top }]}>
      <View style={styles.header}>
        <Text style={styles.wordmark} accessibilityRole="header">
          MARVIN
        </Text>
        <Pressable
          style={styles.pill}
          accessibilityRole="button"
          accessibilityLabel={`Conexão: ${availability.label}. ${availability.detail}`}
          onPress={() => router.push('/settings/connection')}
        >
          <Dot color={dotColor} />
          <Text style={styles.pillText} numberOfLines={1}>
            {availability.label}
          </Text>
        </Pressable>
        <IconButton icon="settings-outline" label="Configurações" onPress={() => router.push('/settings')} />
      </View>

      {demoMode && <Banner tone="warn" text="Modo demonstração: respostas simuladas e nenhuma ação real no computador." />}
      {assistant.wakeListening && (
        <View style={styles.micIndicator} accessibilityLiveRegion="polite">
          <Ionicons name="mic" size={16} color={colors.cyan} />
          <Text style={styles.micText}>Microfone ativo · aguardando “Marvin”</Text>
          <Pressable accessibilityRole="button" accessibilityLabel="Desativar escuta por Marvin" onPress={() => setWakeWord(false)} hitSlop={10}>
            <Text style={styles.micOff}>Desativar</Text>
          </Pressable>
        </View>
      )}

      <ScrollView contentContainerStyle={styles.content} keyboardShouldPersistTaps="handled">
        <View style={styles.greeting}>
          <Text style={type.hero}>{greeting(userName)}</Text>
          <Text style={[type.bodySecondary, styles.status]} accessibilityLiveRegion="polite">
            {assistant.status}
          </Text>
        </View>

        <View style={[styles.orbArea, { minHeight: orbSize + 40 }]}>
          <Pressable
            onPress={tapCore}
            accessibilityRole="button"
            accessibilityLabel={ORB_LABEL[assistant.phase]}
            accessibilityHint={assistant.phase === 'idle' || assistant.phase === 'offline' ? 'Toque para começar a falar' : undefined}
            disabled={busy || assistant.phase === 'awaiting'}
            style={({ pressed }) => [{ transform: [{ scale: pressed ? 0.97 : 1 }] }]}
          >
            <Orb phase={assistant.phase} size={orbSize} reduceMotion={reduceMotion} />
          </Pressable>
          {!!assistant.partial && (
            <Text style={styles.transcript} accessibilityLiveRegion="polite" accessibilityLabel={`Você disse: ${assistant.partial}`}>
              “{assistant.partial}”
            </Text>
          )}
        </View>

        {assistant.notice && (
          <Banner tone={assistant.notice.tone} text={assistant.notice.text}>
            <NoticeActions />
          </Banner>
        )}

        {assistant.approval && (
          <Card tone="amber">
            <Text style={type.label}>O MARVIN do PC pede autorização</Text>
            <Text style={type.body}>{assistant.approval.title}</Text>
            {Object.entries(assistant.approval.details).map(([key, value]) => (
              <Text key={key} style={type.caption} selectable>
                {key}: {typeof value === 'string' ? value : JSON.stringify(value)}
              </Text>
            ))}
            <View style={styles.rowButtons}>
              <Button label="Recusar" icon="close" onPress={() => void decideApproval(false)} style={{ flex: 1 }} />
              <Button label="Permitir" icon="checkmark" variant="amber" onPress={() => void decideApproval(true)} style={{ flex: 1 }} />
            </View>
          </Card>
        )}

        {assistant.commandPreview && (
          <Card tone={assistant.commandPreview.risk === 'destructive' ? 'amber' : 'cyan'}>
            <Chip label={assistant.commandPreview.risk === 'destructive' ? 'Ação sensível no computador' : 'Ação no computador'} tone={assistant.commandPreview.risk === 'destructive' ? 'amber' : 'cyan'} icon="desktop-outline" />
            <Text style={type.label}>{assistant.commandPreview.title}</Text>
            <Text style={type.bodySecondary}>{assistant.commandPreview.description}</Text>
            {Object.entries(assistant.commandPreview.params).map(([key, value]) => (
              <Text key={key} style={type.caption}>
                {key}: {value}
              </Text>
            ))}
            <View style={styles.rowButtons}>
              <Button label="Não executar" onPress={() => void confirmCommand(false)} style={{ flex: 1 }} />
              <Button label="Executar" variant={assistant.commandPreview.risk === 'destructive' ? 'amber' : 'primary'} onPress={() => void confirmCommand(true)} style={{ flex: 1 }} />
            </View>
          </Card>
        )}

        <View style={styles.controls}>
          {assistant.phase === 'listening' && (
            <>
              <Button label="Cancelar" icon="close" onPress={cancelListening} style={{ flex: 1 }} />
              <Button label="Concluir" icon="checkmark" variant="primary" onPress={finishListening} style={{ flex: 1.4 }} accessibilityHint="Para de ouvir e envia o que você disse" />
            </>
          )}
          {assistant.phase === 'speaking' && <Button label="Interromper" icon="stop" variant="primary" onPress={interruptSpeech} style={{ flex: 1 }} />}
          {busy && <Button label="Cancelar pedido" icon="close-circle-outline" onPress={() => void cancelCurrent()} style={{ flex: 1 }} />}
          {(assistant.phase === 'idle' || assistant.phase === 'offline') && (
            <>
              <Button label="Digitar" icon="create-outline" onPress={() => useAssistant.setState({ keyboardOpen: true })} style={{ flex: 1 }} />
              <Button label="Conversa" icon="chatbubbles-outline" onPress={() => router.push('/history')} style={{ flex: 1 }} />
            </>
          )}
        </View>

        {reply && (
          <Pressable
            onPress={() => setExpanded((v) => !v)}
            accessibilityRole="button"
            accessibilityLabel={expanded ? 'Recolher última resposta' : 'Expandir última resposta'}
            style={styles.replyPanel}
          >
            <View style={styles.replyHeader}>
              <Text style={type.section}>ÚLTIMA RESPOSTA</Text>
              {assistant.lastReply?.local && <Chip label="no celular" tone="muted" icon="phone-portrait-outline" />}
              <Ionicons name={expanded ? 'chevron-down' : 'chevron-up'} size={18} color={colors.textMuted} />
            </View>
            <Text style={type.body} numberOfLines={expanded ? undefined : 3} selectable={expanded}>
              {reply}
            </Text>
            {expanded && (assistant.lastReply?.refs.length ?? 0) > 0 && (
              <View style={{ gap: space.xs }}>
                <Text style={type.caption}>Fontes</Text>
                {assistant.lastReply!.refs.map((ref, i) => (
                  <Pressable key={i} onPress={() => ref.chunk_id && router.push({ pathname: '/reference/[chunkId]', params: { chunkId: ref.chunk_id } })}>
                    <Text style={[type.caption, { color: colors.cyan }]}>
                      {ref.filename} · parte {ref.part}
                    </Text>
                  </Pressable>
                ))}
              </View>
            )}
          </Pressable>
        )}
      </ScrollView>

      {assistant.keyboardOpen && <Composer bottomInset={insets.bottom} />}
    </View>
  );
}

function NoticeActions() {
  const notice = useAssistant((s) => s.notice);
  if (!notice?.action) return <Button label="Ok" compact variant="ghost" onPress={() => useAssistant.setState({ notice: null })} style={{ alignSelf: 'flex-start' }} />;
  const close = () => useAssistant.setState({ notice: null });
  const actions: Record<string, { label: string; run: () => void }> = {
    'open-settings': { label: 'Abrir configurações', run: () => void Linking.openSettings() },
    keyboard: { label: 'Digitar', run: () => useAssistant.setState({ keyboardOpen: true, notice: null }) },
    memories: { label: 'Ver memórias', run: () => { close(); router.push({ pathname: '/library', params: { tab: 'memories' } }); } },
    'queue-command': { label: 'Enviar se o PC voltar', run: () => void queueOfflineCommand() },
    pair: { label: 'Vincular', run: () => { close(); router.push('/pair'); } },
  };
  const action = actions[notice.action];
  return (
    <View style={{ flexDirection: 'row', gap: space.sm, flexWrap: 'wrap' }}>
      <Button label={action.label} compact variant="secondary" onPress={action.run} />
      <Button label="Fechar" compact variant="ghost" onPress={close} />
    </View>
  );
}

function Composer({ bottomInset }: { bottomInset: number }) {
  const [text, setText] = useState('');
  const input = useRef<TextInput>(null);
  useEffect(() => {
    const t = setTimeout(() => input.current?.focus(), 150);
    return () => clearTimeout(t);
  }, []);
  const send = () => {
    const value = text.trim();
    if (!value) return;
    setText('');
    useAssistant.setState({ keyboardOpen: false });
    void submit(value, 'text');
  };
  return (
    <KeyboardAvoidingView behavior={Platform.OS === 'ios' ? 'padding' : undefined} style={[styles.composer, { paddingBottom: Math.max(bottomInset, space.md) }]}>
      <IconButton icon="chevron-down" label="Fechar teclado" onPress={() => useAssistant.setState({ keyboardOpen: false })} />
      <TextInput
        ref={input}
        value={text}
        onChangeText={setText}
        placeholder="Escreva para o MARVIN"
        placeholderTextColor={colors.textMuted}
        selectionColor={colors.cyan}
        style={styles.composerInput}
        multiline
        maxLength={4000}
        accessibilityLabel="Mensagem para o MARVIN"
        returnKeyType="send"
        onSubmitEditing={send}
        blurOnSubmit
      />
      <IconButton icon="arrow-up-circle" label="Enviar" onPress={send} color={text.trim() ? colors.cyan : colors.textMuted} size={32} />
    </KeyboardAvoidingView>
  );
}

const styles = StyleSheet.create({
  screen: { flex: 1, backgroundColor: colors.bg },
  header: { flexDirection: 'row', alignItems: 'center', paddingHorizontal: space.lg, gap: space.md, minHeight: 56 },
  wordmark: { fontFamily: fonts.display, fontSize: 17, letterSpacing: 4, color: colors.text },
  pill: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    gap: space.sm,
    backgroundColor: colors.surface,
    borderColor: colors.border,
    borderWidth: 1,
    borderRadius: radius.pill,
    paddingHorizontal: space.md,
    minHeight: 36,
  },
  pillText: { color: colors.textSecondary, fontSize: 13, fontWeight: '600', flexShrink: 1 },
  micIndicator: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: space.sm,
    marginHorizontal: space.lg,
    paddingHorizontal: space.md,
    paddingVertical: space.sm,
    borderRadius: radius.pill,
    backgroundColor: colors.cyanSoft,
  },
  micText: { flex: 1, color: colors.cyan, fontWeight: '600', fontSize: 13 },
  micOff: { color: colors.text, fontWeight: '700', fontSize: 13 },
  content: { paddingHorizontal: space.xl, paddingBottom: space.xxxl, gap: space.lg },
  greeting: { marginTop: space.md, gap: space.xs },
  status: { minHeight: 22 },
  orbArea: { alignItems: 'center', justifyContent: 'center', gap: space.md },
  transcript: { ...type.body, color: colors.textSecondary, textAlign: 'center', fontStyle: 'italic', paddingHorizontal: space.md },
  controls: { flexDirection: 'row', gap: space.md },
  rowButtons: { flexDirection: 'row', gap: space.md, marginTop: space.xs },
  replyPanel: {
    backgroundColor: colors.surface,
    borderColor: colors.border,
    borderWidth: StyleSheet.hairlineWidth,
    borderRadius: radius.lg,
    padding: space.lg,
    gap: space.sm,
  },
  replyHeader: { flexDirection: 'row', alignItems: 'center', gap: space.sm, justifyContent: 'space-between' },
  composer: {
    flexDirection: 'row',
    alignItems: 'flex-end',
    gap: space.xs,
    paddingHorizontal: space.sm,
    paddingTop: space.sm,
    backgroundColor: colors.bgRaised,
    borderTopWidth: StyleSheet.hairlineWidth,
    borderTopColor: colors.borderStrong,
  },
  composerInput: {
    flex: 1,
    minHeight: 48,
    maxHeight: 140,
    color: colors.text,
    fontSize: 16,
    backgroundColor: colors.surfaceSolid,
    borderRadius: radius.lg,
    paddingHorizontal: space.lg,
    paddingTop: 13,
    paddingBottom: 13,
  },
});
