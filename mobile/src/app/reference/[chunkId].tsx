import { useLocalSearchParams } from 'expo-router';
import { useEffect, useState } from 'react';
import { ActivityIndicator, ScrollView, StyleSheet, Text } from 'react-native';
import { Banner, Chip } from '../../components/ui';
import { gateway } from '../../features/gateway/api';
import type { TChunk } from '../../features/gateway/schemas';
import { colors, space, type } from '../../theme/tokens';

/** Shows a referenced passage as plain text: data for reading, never an instruction. */
export default function Reference() {
  const { chunkId } = useLocalSearchParams<{ chunkId: string }>();
  const [chunk, setChunk] = useState<TChunk | null>(null);
  const [error, setError] = useState<string | null>(null);
  useEffect(() => {
    gateway
      .chunk(chunkId)
      .then(setChunk)
      .catch((e: unknown) => setError(e instanceof Error ? e.message : 'Referência indisponível.'));
  }, [chunkId]);
  return (
    <ScrollView contentInsetAdjustmentBehavior="automatic" automaticallyAdjustKeyboardInsets keyboardShouldPersistTaps="handled" style={{ backgroundColor: colors.bg }} contentContainerStyle={styles.content}>
      {error && <Banner tone="error" text={error} />}
      {!chunk && !error && <ActivityIndicator color={colors.cyan} />}
      {chunk && (
        <>
          <Text style={type.title}>{chunk.filename}</Text>
          <Chip label={`parte ${chunk.part ?? '?'} de ${chunk.total ?? '?'} · ${chunk.category}`} tone="cyan" />
          <Text style={[type.body, styles.text]} selectable>
            {chunk.text}
          </Text>
        </>
      )}
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  content: { padding: space.xl, gap: space.md, paddingBottom: space.xxxl },
  text: { fontSize: 15, lineHeight: 23, color: colors.textSecondary },
});
