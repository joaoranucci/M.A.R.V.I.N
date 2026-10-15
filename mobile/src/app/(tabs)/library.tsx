import { router, useLocalSearchParams } from 'expo-router';
import { useCallback, useEffect, useMemo, useState } from 'react';
import { Platform, ActivityIndicator, Pressable, RefreshControl, ScrollView, StyleSheet, Text, View } from 'react-native';
import { useSafeAreaInsets } from 'react-native-safe-area-context';
import { AnswerCard } from '../../components/AnswerCard';
import { Banner, Button, Card, Chip, EmptyState, Field, Segmented, SectionTitle } from '../../components/ui';
import { useConnectivity } from '../../core/net/connectivity';
import { useSettings } from '../../core/settings';
import { syncNow } from '../../core/sync/syncEngine';
import { uploadStateLabel } from '../../features/activities/repo';
import { acceptedFormats, pickDocument, uploadDocument, useDocuments, type LibraryDocument } from '../../features/documents/service';
import { gateway } from '../../features/gateway/api';
import type { TAskResult, TSearchHit } from '../../features/gateway/schemas';
import { CATEGORIES, loadMemories, originLabel, useMemories, type Memory } from '../../features/memory/service';
import { colors, space, type } from '../../theme/tokens';

type Tab = 'documents' | 'memories' | 'search';

export default function Library() {
  const params = useLocalSearchParams<{ tab?: Tab }>();
  return <LibraryContent key={params.tab ?? 'documents'} initialTab={params.tab ?? 'documents'} />;
}

function LibraryContent({ initialTab }: { initialTab: Tab }) {
  const [tab, setTab] = useState<Tab>(initialTab);
  const insets = useSafeAreaInsets();
  return (
    <View style={[styles.screen, { paddingTop: insets.top + space.md }]}>
      <Text style={[type.title, styles.title]} accessibilityRole="header">
        Biblioteca
      </Text>
      <View style={{ paddingHorizontal: space.xl, marginBottom: space.md }}>
        <Segmented
          value={tab}
          onChange={setTab}
          options={[
            { value: 'documents', label: 'Documentos' },
            { value: 'memories', label: 'Memórias' },
            { value: 'search', label: 'Pesquisa' },
          ]}
        />
      </View>
      {tab === 'documents' && <Documents />}
      {tab === 'memories' && <Memories />}
      {tab === 'search' && <Search />}
    </View>
  );
}

function stateTone(state: string): 'cyan' | 'amber' | 'danger' | 'success' | 'default' {
  return state === 'available' ? 'success' : state === 'failed' ? 'danger' : state === 'queued_offline' ? 'amber' : 'cyan';
}

function useRefresh() {
  const [refreshing, setRefreshing] = useState(false);
  const onRefresh = useCallback(async () => {
    setRefreshing(true);
    await syncNow('manual');
    setRefreshing(false);
  }, []);
  return { refreshing, onRefresh };
}

function Documents() {
  const docs = useDocuments((s) => s.items);
  const connectivity = useConnectivity();
  const caps = connectivity.capabilities;
  const demo = useSettings((s) => s.demoMode);
  const [category, setCategory] = useState('geral');
  const [busy, setBusy] = useState(false);
  const [message, setMessage] = useState<{ tone: 'info' | 'warn' | 'error' | 'ok'; text: string } | null>(null);
  const refresh = useRefresh();

  const send = async () => {
    setMessage(null);
    const file = await pickDocument();
    if (!file) return;
    setBusy(true);
    const result = await uploadDocument(file, category);
    setBusy(false);
    if (result.error) setMessage({ tone: 'warn', text: result.error });
    else if (result.queued) setMessage({ tone: 'info', text: 'Sem conexão com o PC: o arquivo será enviado automaticamente quando ele voltar.' });
    else setMessage({ tone: 'ok', text: 'Enviado. O PC ainda vai extrair e indexar o texto; acompanhe o estado abaixo.' });
  };

  return (
    <ScrollView contentInsetAdjustmentBehavior="automatic" automaticallyAdjustKeyboardInsets contentContainerStyle={styles.list} refreshControl={<RefreshControl {...refresh} tintColor={colors.cyan} />}>
      <Card>
        <Text style={type.label}>Enviar documento</Text>
        <Text style={type.caption}>
          {caps
            ? `Formatos aceitos pelo PC: ${acceptedFormats().join(' ')} · até ${Math.round(caps.documents.max_bytes / 1048576)} MB.${caps.documents.ocr ? '' : ' PDF digitalizado (imagem) não funciona: o PC não tem OCR.'}`
            : 'Conecte ao PC uma vez para carregar os formatos aceitos.'}
        </Text>
        <Text style={type.caption}>{Platform.OS === 'ios' ? 'Use “Escolher arquivo” para escolher um arquivo no app Arquivos ou no iCloud Drive.' : 'Você também pode compartilhar um arquivo com o MARVIN pelo menu do Android.'}</Text>
        <View style={styles.chips}>
          {['geral', 'estudos', 'trabalho', 'projetos', 'pessoal'].map((c) => (
            <Pressable key={c} onPress={() => setCategory(c)} accessibilityRole="radio" accessibilityState={{ checked: category === c }}>
              <Chip label={c} tone={category === c ? 'cyan' : 'default'} />
            </Pressable>
          ))}
        </View>
        <Button label="Escolher arquivo" icon="document-attach-outline" variant="primary" loading={busy} disabled={demo || !caps} onPress={() => void send()} />
        {demo && <Text style={type.caption}>Envio desativado no modo demonstração.</Text>}
      </Card>
      {message && <Banner tone={message.tone} text={message.text} />}
      <SectionTitle>{`Documentos (${docs.length})`}</SectionTitle>
      {docs.length === 0 ? (
        <EmptyState icon="library-outline" title="Biblioteca vazia" text="Envie PDFs com texto, Word, Markdown ou arquivos de texto para consultar e perguntar sobre eles." />
      ) : (
        docs.map((doc) => <DocumentRow key={doc.id} doc={doc} />)
      )}
    </ScrollView>
  );
}

function DocumentRow({ doc }: { doc: LibraryDocument }) {
  const open = doc.state === 'available' && !doc.id.startsWith('local-');
  return (
    <Pressable
      disabled={!open}
      onPress={() => router.push({ pathname: '/document/[id]', params: { id: doc.id, name: doc.filename } })}
      accessibilityRole="button"
      accessibilityLabel={`${doc.filename}, ${uploadStateLabel[doc.state] ?? doc.state}`}
      style={({ pressed }) => [styles.item, pressed && { backgroundColor: colors.surfacePressed }]}
    >
      <Text style={type.label} numberOfLines={2}>
        {doc.filename}
      </Text>
      <View style={styles.chips}>
        <Chip label={uploadStateLabel[doc.state] ?? doc.state} tone={stateTone(doc.state)} />
        <Chip label={doc.category} />
        {doc.chunks ? <Chip label={`${doc.chunks} trechos`} tone="muted" /> : null}
      </View>
      {!!doc.message && doc.state !== 'available' && <Text style={type.caption}>{doc.message}</Text>}
    </Pressable>
  );
}

function syncLabel(m: Memory): { label: string; tone: 'success' | 'amber' | 'danger' | 'muted' } {
  if (m.sync_state === 'synced') return { label: 'No cofre', tone: 'success' };
  if (m.sync_state === 'conflict') return { label: 'Conflito', tone: 'danger' };
  if (m.sync_state === 'local_only') return { label: 'Só neste aparelho', tone: 'muted' };
  return { label: 'Aguardando sincronizar', tone: 'amber' };
}

function Memories() {
  const all = useMemories((s) => s.items);
  const [query, setQuery] = useState('');
  const [category, setCategory] = useState<string | null>(null);
  const refresh = useRefresh();
  useEffect(() => {
    void loadMemories();
  }, []);
  const visible = useMemo(() => {
    const q = query.trim().toLowerCase();
    return all.filter((m) => (!category || m.category === category) && (!q || m.content.toLowerCase().includes(q)));
  }, [all, query, category]);
  const categories = useMemo(() => [...new Set([...CATEGORIES, ...all.map((m) => m.category)])], [all]);
  return (
    <ScrollView contentInsetAdjustmentBehavior="automatic" automaticallyAdjustKeyboardInsets contentContainerStyle={styles.list} refreshControl={<RefreshControl {...refresh} tintColor={colors.cyan} />} keyboardShouldPersistTaps="handled">
      <Field label="Buscar memórias" value={query} onChangeText={setQuery} placeholder="ex.: estudar" returnKeyType="search" />
      <ScrollView contentInsetAdjustmentBehavior="automatic" automaticallyAdjustKeyboardInsets horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.chips}>
        <Pressable onPress={() => setCategory(null)}>
          <Chip label="todas" tone={category === null ? 'cyan' : 'default'} />
        </Pressable>
        {categories.map((c) => (
          <Pressable key={c} onPress={() => setCategory(c === category ? null : c)}>
            <Chip label={c} tone={category === c ? 'cyan' : 'default'} />
          </Pressable>
        ))}
      </ScrollView>
      <Button label="Nova memória" icon="add" onPress={() => router.push({ pathname: '/memory/[id]', params: { id: 'new' } })} />
      <Text style={type.caption}>Diga “Marvin, lembre que…” para guardar por voz. A conversa não vira memória sozinha.</Text>
      {visible.length === 0 ? (
        <EmptyState icon="sparkles-outline" title={all.length ? 'Nada encontrado' : 'Nenhuma memória ainda'} text={all.length ? 'Tente outro termo ou categoria.' : 'Peça ao MARVIN para lembrar de preferências, rotinas e decisões.'} />
      ) : (
        visible.map((m) => {
          const sync = syncLabel(m);
          return (
            <Pressable
              key={m.id}
              onPress={() => router.push({ pathname: '/memory/[id]', params: { id: m.id } })}
              accessibilityRole="button"
              style={({ pressed }) => [styles.item, pressed && { backgroundColor: colors.surfacePressed }]}
            >
              <Text style={type.body} numberOfLines={3}>
                {m.content}
              </Text>
              <View style={styles.chips}>
                <Chip label={m.category} />
                <Chip label={originLabel[m.origin]} tone={m.origin === 'assistant_inference' ? 'amber' : 'cyan'} />
                <Chip label={sync.label} tone={sync.tone} />
              </View>
            </Pressable>
          );
        })
      )}
    </ScrollView>
  );
}

function Search() {
  const online = useConnectivity((s) => s.gateway === 'online' && s.vault === 'ok');
  const [query, setQuery] = useState('');
  const [hits, setHits] = useState<TSearchHit[] | null>(null);
  const [answer, setAnswer] = useState<TAskResult | null>(null);
  const [busy, setBusy] = useState<'search' | 'ask' | null>(null);
  const [error, setError] = useState<string | null>(null);
  const run = async (mode: 'search' | 'ask') => {
    const q = query.trim();
    if (q.length < 3) return;
    setBusy(mode);
    setError(null);
    try {
      if (mode === 'search') {
        setAnswer(null);
        setHits(await gateway.search(q));
      } else {
        setHits(null);
        setAnswer(await gateway.ask(q));
      }
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Falha na consulta.');
    } finally {
      setBusy(null);
    }
  };
  return (
    <ScrollView contentInsetAdjustmentBehavior="automatic" automaticallyAdjustKeyboardInsets contentContainerStyle={styles.list} keyboardShouldPersistTaps="handled">
      {!online && <Banner tone="warn" text="A pesquisa usa a biblioteca do PC: conecte ao computador com o cofre aberto." />}
      <Field label="Pesquisar nos documentos" value={query} onChangeText={setQuery} placeholder="ex.: como o SQLite é protegido" onSubmitEditing={() => void run('search')} returnKeyType="search" />
      <View style={{ flexDirection: 'row', gap: space.md }}>
        <Button label="Buscar trechos" icon="search" onPress={() => void run('search')} loading={busy === 'search'} disabled={!online} style={{ flex: 1 }} />
        <Button label="Perguntar" icon="help-circle-outline" variant="primary" onPress={() => void run('ask')} loading={busy === 'ask'} disabled={!online} style={{ flex: 1 }} />
      </View>
      <Text style={type.caption}>Busca por palavras (BM25), não semântica. Respostas geradas usam o modelo local do PC quando disponível; confira sempre as fontes.</Text>
      {error && <Banner tone="error" text={error} />}
      {busy && <ActivityIndicator color={colors.cyan} />}
      {answer && <AnswerCard answer={answer} />}
      {hits && (hits.length === 0 ? <EmptyState icon="search-outline" title="Nenhum trecho" text="Tente outras palavras: a busca é lexical." /> : hits.map((hit) => <HitRow key={hit.chunk_id} hit={hit} />))}
    </ScrollView>
  );
}

function HitRow({ hit }: { hit: TSearchHit }) {
  return (
    <Pressable
      onPress={() => router.push({ pathname: '/reference/[chunkId]', params: { chunkId: hit.chunk_id } })}
      accessibilityRole="link"
      style={({ pressed }) => [styles.item, pressed && { backgroundColor: colors.surfacePressed }]}
    >
      <Text style={[type.label, { color: colors.cyan }]}>
        {hit.filename} · parte {hit.part}
      </Text>
      <Text style={type.bodySecondary} numberOfLines={4}>
        {hit.excerpt}
      </Text>
    </Pressable>
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
    borderRadius: 16,
    padding: space.lg,
    gap: space.sm,
  },
  source: { gap: 2, paddingVertical: space.xs, minHeight: 44 },
});

