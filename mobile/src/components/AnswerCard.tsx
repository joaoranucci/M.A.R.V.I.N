import { router } from 'expo-router';
import { Pressable, StyleSheet, Text } from 'react-native';
import type { TAskResult } from '../features/gateway/schemas';
import { colors, space, type } from '../theme/tokens';
import { Banner, Card } from './ui';

/** Answer from the library with its references; document text is displayed, never executed. */
export function AnswerCard({ answer }: { answer: TAskResult }) {
  return (
    <Card tone="cyan">
      {answer.generated ? (
        <>
          <Text style={type.body} selectable>
            {answer.answer}
          </Text>
          {answer.model && <Text style={type.caption}>Gerado por {answer.model} no PC</Text>}
        </>
      ) : (
        <Banner tone="warn" text={`Resposta gerada indisponível: ${answer.llm_unavailable_reason ?? 'modelo local ausente'}. Veja os trechos encontrados.`} />
      )}
      {answer.document_id && answer.sources_in_document === 0 && (
        <Text style={[type.caption, { color: colors.amber }]}>Nenhuma fonte veio do documento escolhido; as referências abaixo são de outros documentos da mesma categoria.</Text>
      )}
      <Text style={type.section}>REFERÊNCIAS</Text>
      {answer.sources.length === 0 && <Text style={type.caption}>Sem fontes.</Text>}
      {answer.sources.map((source, i) => (
        <Pressable
          key={`${source.chunk_id}-${i}`}
          disabled={!source.chunk_id}
          onPress={() => source.chunk_id && router.push({ pathname: '/reference/[chunkId]', params: { chunkId: source.chunk_id } })}
          accessibilityRole="link"
          style={styles.source}
        >
          <Text style={[type.label, { color: colors.cyan }]}>
            [{i + 1}] {source.filename} · parte {source.part}
          </Text>
          {!!source.excerpt && (
            <Text style={type.caption} numberOfLines={3}>
              {source.excerpt}
            </Text>
          )}
        </Pressable>
      ))}
    </Card>
  );
}


const styles = StyleSheet.create({ source: { gap: 2, paddingVertical: space.xs, minHeight: 44 } });
