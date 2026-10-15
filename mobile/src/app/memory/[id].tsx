import { router, useLocalSearchParams } from 'expo-router';
import { useEffect, useState } from 'react';
import { Alert, Pressable, ScrollView, StyleSheet, Text, View } from 'react-native';
import { Banner, Button, Chip, Field, SectionTitle } from '../../components/ui';
import { getDb } from '../../core/db/database';
import type { TMemory } from '../../features/gateway/schemas';
import {
  CATEGORIES,
  createMemory,
  deleteMemory,
  originLabel,
  resolveConflict,
  updateMemory,
  type Memory,
  type MemoryOrigin,
} from '../../features/memory/service';
import { colors, space, type } from '../../theme/tokens';

const SOURCE_LABEL: Record<string, string> = {
  'mobile-voice': 'por voz no celular',
  'mobile-text': 'digitada no celular',
  desktop: 'no MARVIN do PC',
  vault: 'no cofre',
};

export default function MemoryScreen() {
  const { id } = useLocalSearchParams<{ id: string }>();
  const isNew = id === 'new';
  const [memory, setMemory] = useState<Memory | null>(null);
  const [content, setContent] = useState('');
  const [category, setCategory] = useState('geral');
  const [origin, setOrigin] = useState<MemoryOrigin>('user_request');

  useEffect(() => {
    if (isNew) return;
    void getDb()
      .then((db) => db.getFirstAsync<Memory>('SELECT * FROM memories WHERE id = ?', id))
      .then((m) => {
        if (!m) return;
        setMemory(m);
        setContent(m.content);
        setCategory(m.category);
        setOrigin(m.origin);
      });
  }, [id, isNew]);

  const save = async () => {
    if (!content.trim()) return;
    if (isNew) await createMemory(content, category, 'user_request', 'mobile-text');
    else await updateMemory(id, { content, category, origin });
    router.back();
  };

  const remove = () =>
    Alert.alert('Excluir memória?', 'Ela será removida deste celular e do cofre no PC.', [
      { text: 'Cancelar', style: 'cancel' },
      {
        text: 'Excluir',
        style: 'destructive',
        onPress: async () => {
          await deleteMemory(id);
          router.back();
        },
      },
    ]);

  const server = memory?.conflict ? (JSON.parse(memory.conflict) as TMemory | null) : null;

  return (
    <ScrollView style={{ backgroundColor: colors.bg }} contentContainerStyle={styles.content} keyboardShouldPersistTaps="handled">
      {memory?.sync_state === 'conflict' && (
        <Banner tone="warn" text={`Alterada em outro dispositivo: “${server?.content ?? '?'}”. Qual versão manter?`}>
          <View style={{ flexDirection: 'row', gap: space.sm }}>
            <Button label="A deste celular" compact onPress={() => void resolveConflict(id, 'mine').then(() => router.back())} />
            <Button label="A do outro" compact onPress={() => void resolveConflict(id, 'server').then(() => router.back())} />
          </View>
        </Banner>
      )}
      <Field label="Conteúdo" value={content} onChangeText={setContent} multiline style={{ minHeight: 120, textAlignVertical: 'top', paddingTop: 12 }} maxLength={20000} />
      <SectionTitle>Categoria</SectionTitle>
      <View style={styles.chips}>
        {[...new Set([...CATEGORIES, category])].map((c) => (
          <Pressable key={c} onPress={() => setCategory(c)} accessibilityRole="radio" accessibilityState={{ checked: c === category }}>
            <Chip label={c} tone={c === category ? 'cyan' : 'default'} />
          </Pressable>
        ))}
      </View>
      {!isNew && memory && (
        <>
          <SectionTitle>Origem</SectionTitle>
          <View style={styles.chips}>
            {(['user_request', 'assistant_inference'] as MemoryOrigin[]).map((o) => (
              <Pressable key={o} onPress={() => setOrigin(o)} accessibilityRole="radio" accessibilityState={{ checked: origin === o }}>
                <Chip label={originLabel[o]} tone={origin === o ? (o === 'assistant_inference' ? 'amber' : 'cyan') : 'default'} />
              </Pressable>
            ))}
            {memory.origin === 'imported' && <Chip label={originLabel.imported} tone="muted" />}
          </View>
          <Text style={type.caption}>
            Registrada {SOURCE_LABEL[memory.source] ?? memory.source} em {new Date(memory.created_at).toLocaleString('pt-BR')}. Última alteração {new Date(memory.updated_at).toLocaleString('pt-BR')}.
            {memory.origin === 'assistant_inference' ? ' É uma inferência: confirme ou corrija.' : ''}
          </Text>
        </>
      )}
      <Button label="Salvar" icon="checkmark" variant="primary" onPress={() => void save()} disabled={!content.trim()} />
      {!isNew && <Button label="Excluir" icon="trash-outline" variant="danger" onPress={remove} />}
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  content: { padding: space.xl, gap: space.md, paddingBottom: space.xxxl },
  chips: { flexDirection: 'row', flexWrap: 'wrap', gap: space.sm },
});
