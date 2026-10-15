import { router } from 'expo-router';
import { useState } from 'react';
import { Pressable, ScrollView, StyleSheet, Text, View } from 'react-native';
import { Banner, Button, Card, Chip } from '../components/ui';
import { useShare } from '../core/bootstrap';
import { saveItem } from '../features/tasks/service';
import { checkFile, uploadDocument } from '../features/documents/service';
import { colors, space, type } from '../theme/tokens';

function formatSize(bytes: number): string {
  if (bytes < 1024) return `${bytes} B`;
  if (bytes < 1048576) return `${(bytes / 1024).toFixed(1).replace('.', ',')} KB`;
  return `${(bytes / 1048576).toFixed(1).replace('.', ',')} MB`;
}

/** Files shared from Android: the user confirms before anything is sent to the library. */
export default function Share() {
  const payload = useShare((s) => s.payload);
  const [category, setCategory] = useState('geral');
  const [busy, setBusy] = useState(false);
  const [result, setResult] = useState<string | null>(null);

  const close = () => {
    useShare.setState({ payload: null });
    router.back();
  };

  if (!payload) {
    return (
      <View style={styles.screen}>
        <Text style={type.bodySecondary}>Nada para enviar.</Text>
      </View>
    );
  }

  const files = payload.files.map((f) => ({ ...f, problem: f.error ?? (f.uri ? checkFile(f.name, f.size) : 'Não foi possível ler o arquivo.') }));
  const sendable = files.filter((f) => !f.problem && f.uri);

  const send = async () => {
    setBusy(true);
    let queued = 0;
    for (const file of sendable) {
      const outcome = await uploadDocument({ uri: file.uri!, name: file.name, size: file.size, mimeType: file.mimeType }, category);
      if (outcome.queued) queued++;
    }
    if (payload.text && !sendable.length) await saveItem({ kind: 'note', title: payload.text.slice(0, 300), notes: payload.text });
    setBusy(false);
    setResult(queued ? 'Guardado: será enviado quando o PC estiver disponível.' : 'Enviado. A indexação continua no PC — acompanhe em Biblioteca.');
    setTimeout(close, 1400);
  };

  return (
    <ScrollView contentInsetAdjustmentBehavior="automatic" automaticallyAdjustKeyboardInsets keyboardShouldPersistTaps="handled" style={{ backgroundColor: colors.bg }} contentContainerStyle={styles.content}>
      {files.map((file) => (
        <Card key={file.name + file.size}>
          <Text style={type.label}>{file.name}</Text>
          <Text style={type.caption}>{formatSize(file.size)}</Text>
          {file.problem ? <Chip label={file.problem} tone="amber" /> : <Chip label="pronto para a biblioteca" tone="success" />}
        </Card>
      ))}
      {payload.text && !files.length && (
        <Card>
          <Text style={type.label}>Texto compartilhado</Text>
          <Text style={type.bodySecondary} numberOfLines={8}>
            {payload.text}
          </Text>
          <Text style={type.caption}>Será salvo como nota. Não é tratado como comando.</Text>
        </Card>
      )}
      {sendable.length > 0 && (
        <View style={styles.chips}>
          {['geral', 'estudos', 'trabalho', 'projetos', 'pessoal'].map((c) => (
            <Pressable key={c} onPress={() => setCategory(c)} accessibilityRole="radio" accessibilityState={{ checked: c === category }}>
              <Chip label={c} tone={c === category ? 'cyan' : 'default'} />
            </Pressable>
          ))}
        </View>
      )}
      {result && <Banner tone="ok" text={result} />}
      <Button
        label={sendable.length ? `Enviar ${sendable.length} para a biblioteca` : payload.text ? 'Salvar como nota' : 'Nada compatível'}
        variant="primary"
        icon="cloud-upload-outline"
        loading={busy}
        disabled={!sendable.length && !payload.text}
        onPress={() => void send()}
      />
      <Button label="Cancelar" onPress={close} />
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  screen: { flex: 1, backgroundColor: colors.bg, padding: space.xl },
  content: { padding: space.xl, gap: space.md, paddingBottom: space.xxxl },
  chips: { flexDirection: 'row', flexWrap: 'wrap', gap: space.sm },
});
