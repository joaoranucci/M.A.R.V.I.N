import { router } from 'expo-router';
import { useEffect, useMemo } from 'react';
import { Alert, FlatList, Pressable, StyleSheet, Text, View } from 'react-native';
import { Chip, EmptyState } from '../components/ui';
import { syncNow } from '../core/sync/syncEngine';
import { parseRefs, useConversation, type ChatMessage } from '../features/conversation/repo';
import { createMemory } from '../features/memory/service';
import { inferCategory } from '../features/assistant/nlp/intents';
import { colors, radius, space, type } from '../theme/tokens';

const STATUS: Partial<Record<ChatMessage['status'], string>> = {
  sending: 'enviando',
  sent: 'aguardando resposta',
  failed: 'falhou',
  cancelled: 'cancelada',
  offline: 'sem conexão',
};

export default function History() {
  const messages = useConversation((s) => s.messages);
  // Inverted list: newest at the bottom without a scroll jump.
  const newestFirst = useMemo(() => [...messages].reverse(), [messages]);
  useEffect(() => {
    void syncNow('histórico');
  }, []);

  const keepAsMemory = (message: ChatMessage) =>
    Alert.alert(
      'Guardar como memória?',
      message.role === 'assistant'
        ? 'Será registrada como inferência do MARVIN (você pode corrigir depois).'
        : 'Será registrada como algo que você pediu para guardar.',
      [
        { text: 'Cancelar', style: 'cancel' },
        {
          text: 'Guardar',
          onPress: () =>
            void createMemory(message.text.slice(0, 2000), inferCategory(message.text), message.role === 'assistant' ? 'assistant_inference' : 'user_request', 'mobile-text'),
        },
      ],
    );

  if (!messages.length) {
    return (
      <View style={styles.screen}>
        <EmptyState icon="chatbubbles-outline" title="Nenhuma conversa ainda" text="Toque no núcleo e fale com o MARVIN. Conversas feitas no PC aparecem aqui quando ele estiver conectado." />
      </View>
    );
  }

  return (
    <FlatList
      inverted
      style={styles.screen}
      contentContainerStyle={styles.content}
      data={newestFirst}
      keyExtractor={(m) => m.id}
      renderItem={({ item }) => {
        const mine = item.role === 'user';
        const refs = parseRefs(item);
        return (
          <Pressable
            onLongPress={() => keepAsMemory(item)}
            accessibilityHint="Toque longo para guardar como memória"
            style={[styles.bubble, mine ? styles.mine : styles.theirs]}
          >
            <Text style={type.body} selectable>
              {item.text}
            </Text>
            <View style={styles.meta}>
              <Text style={type.caption}>{new Date(item.created_at).toLocaleString('pt-BR', { dateStyle: 'short', timeStyle: 'short' })}</Text>
              {item.origin === 'desktop' && <Chip label="no PC" tone="muted" icon="desktop-outline" />}
              {item.engine === 'local' && <Chip label="no celular" tone="muted" />}
              {item.engine === 'demo' && <Chip label="demonstração" tone="amber" />}
              {STATUS[item.status] && <Chip label={STATUS[item.status]!} tone={item.status === 'failed' || item.status === 'offline' ? 'amber' : 'muted'} />}
            </View>
            {refs.map((ref, i) => (
              <Pressable key={i} onPress={() => ref.chunk_id && router.push({ pathname: '/reference/[chunkId]', params: { chunkId: ref.chunk_id } })}>
                <Text style={[type.caption, { color: colors.cyan }]}>
                  [{i + 1}] {ref.filename} · parte {ref.part}
                </Text>
              </Pressable>
            ))}
          </Pressable>
        );
      }}
    />
  );
}

const styles = StyleSheet.create({
  screen: { flex: 1, backgroundColor: colors.bg },
  content: { padding: space.lg, gap: space.md, paddingBottom: space.xxxl },
  bubble: { maxWidth: '88%', padding: space.md, borderRadius: radius.lg, gap: space.xs },
  mine: { alignSelf: 'flex-end', backgroundColor: colors.blueSoft, borderBottomRightRadius: 6 },
  theirs: { alignSelf: 'flex-start', backgroundColor: colors.surface, borderBottomLeftRadius: 6, borderWidth: StyleSheet.hairlineWidth, borderColor: colors.border },
  meta: { flexDirection: 'row', flexWrap: 'wrap', gap: space.sm, alignItems: 'center' },
});
