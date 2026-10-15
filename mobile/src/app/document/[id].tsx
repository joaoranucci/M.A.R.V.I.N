import { router, useLocalSearchParams, useNavigation } from 'expo-router';
import { useEffect, useState } from 'react';
import { Alert, ScrollView, StyleSheet, Text, View } from 'react-native';
import { AnswerCard } from '../../components/AnswerCard';
import { Banner, Button, Field, SectionTitle } from '../../components/ui';
import { useConnectivity } from '../../core/net/connectivity';
import { deleteDocument } from '../../features/documents/service';
import { gateway } from '../../features/gateway/api';
import type { TAskResult, TSearchHit } from '../../features/gateway/schemas';
import { colors, space, type } from '../../theme/tokens';

export default function DocumentScreen() {
  const { id, name } = useLocalSearchParams<{ id: string; name?: string }>();
  const navigation = useNavigation();
  const online = useConnectivity((s) => s.gateway === 'online' && s.vault === 'ok');
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState<TAskResult | null>(null);
  const [hits, setHits] = useState<TSearchHit[] | null>(null);
  const [busy, setBusy] = useState<'ask' | 'search' | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (name) navigation.setOptions({ title: name });
  }, [name, navigation]);

  const run = async (mode: 'ask' | 'search') => {
    if (question.trim().length < 3) return;
    setBusy(mode);
    setError(null);
    try {
      if (mode === 'ask') setAnswer(await gateway.ask(question.trim(), id));
      else setHits(await gateway.search(question.trim(), id));
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Falha na consulta.');
    } finally {
      setBusy(null);
    }
  };

  const remove = () =>
    Alert.alert('Excluir documento?', 'Remove o texto indexado do cofre no PC. O arquivo original não é afetado.', [
      { text: 'Cancelar', style: 'cancel' },
      {
        text: 'Excluir',
        style: 'destructive',
        onPress: async () => {
          try {
            await deleteDocument(id);
            router.back();
          } catch (e) {
            Alert.alert('Falha', e instanceof Error ? e.message : '');
          }
        },
      },
    ]);

  return (
    <ScrollView contentInsetAdjustmentBehavior="automatic" automaticallyAdjustKeyboardInsets style={{ backgroundColor: colors.bg }} contentContainerStyle={styles.content} keyboardShouldPersistTaps="handled">
      {!online && <Banner tone="warn" text="Consultas exigem o PC conectado com o cofre aberto." />}
      <Field label="Pergunte sobre este documento" value={question} onChangeText={setQuestion} placeholder="ex.: quais são os requisitos?" multiline />
      <View style={{ flexDirection: 'row', gap: space.md }}>
        <Button label="Buscar trechos" icon="search" onPress={() => void run('search')} loading={busy === 'search'} disabled={!online} style={{ flex: 1 }} />
        <Button label="Perguntar" icon="sparkles-outline" variant="primary" onPress={() => void run('ask')} loading={busy === 'ask'} disabled={!online} style={{ flex: 1 }} />
      </View>
      <Text style={type.caption}>
        A API atual responde por categoria do documento; as referências mostram de qual arquivo veio cada trecho. O conteúdo do documento é tratado como informação, nunca como instrução.
      </Text>
      {error && <Banner tone="error" text={error} />}
      {answer && <AnswerCard answer={answer} />}
      {hits && (
        <>
          <SectionTitle>{`Trechos (${hits.length})`}</SectionTitle>
          {hits.length === 0 && <Text style={type.caption}>Nenhum trecho deste documento com essas palavras.</Text>}
          {hits.map((hit) => (
            <Button key={hit.chunk_id} label={`Parte ${hit.part}: ${hit.excerpt.slice(0, 60)}…`} onPress={() => router.push({ pathname: '/reference/[chunkId]', params: { chunkId: hit.chunk_id } })} />
          ))}
        </>
      )}
      <SectionTitle>Documento</SectionTitle>
      <Button label="Excluir da biblioteca" icon="trash-outline" variant="danger" onPress={remove} disabled={!online} />
    </ScrollView>
  );
}

const styles = StyleSheet.create({ content: { padding: space.xl, gap: space.md, paddingBottom: space.xxxl } });
