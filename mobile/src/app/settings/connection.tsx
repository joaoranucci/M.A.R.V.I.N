import { router } from 'expo-router';
import { useState } from 'react';
import { Alert, ScrollView, StyleSheet, Text, View } from 'react-native';
import { Banner, Button, Card, Chip, Field, Row, Segmented, SectionTitle } from '../../components/ui';
import { describeAvailability, refreshCapabilities, refreshConnectivity, useConnectivity } from '../../core/net/connectivity';
import { useConnectionInfo } from '../../core/security/credentials';
import { useSettings, type Engine } from '../../core/settings';
import { validHost } from '../../features/assistant/nlp/pairing';
import { displayFingerprint } from '../../features/assistant/nlp/text';
import { signOut } from '../../features/gateway/pairing';
import { colors, space, type } from '../../theme/tokens';

export default function ConnectionSettings() {
  const connection = useConnectionInfo((s) => s.connection);
  const connectivity = useConnectivity();
  const s = useSettings();
  const availability = describeAvailability(connectivity, s.demoMode);
  const [host, setHost] = useState(connection?.host ?? '');
  const [port, setPort] = useState(String(connection?.port ?? 8770));
  const [testing, setTesting] = useState(false);
  const engines = connectivity.capabilities?.conversation.engines ?? [];

  const test = async () => {
    setTesting(true);
    await refreshConnectivity();
    await refreshCapabilities();
    setTesting(false);
  };

  const saveAddress = async () => {
    const p = Number(port);
    if (!validHost(host) || !Number.isInteger(p)) return Alert.alert('Endereço inválido', 'Use o IP do PC na rede local ou na VPN.');
    await useConnectionInfo.getState().updateAddress(host.trim(), p);
    await test();
  };

  const endSession = () =>
    Alert.alert('Encerrar sessão?', 'Este celular será desvinculado do PC e as credenciais serão apagadas. Seus dados locais permanecem.', [
      { text: 'Cancelar', style: 'cancel' },
      {
        text: 'Encerrar',
        style: 'destructive',
        onPress: async () => {
          const { revokedRemotely } = await signOut();
          Alert.alert('Sessão encerrada', revokedRemotely ? 'O acesso foi revogado no PC.' : 'Credenciais apagadas aqui. O PC estava inacessível: revogue também por DISPOSITIVOS_CELULAR.bat.');
        },
      },
    ]);

  if (!connection) {
    return (
      <ScrollView contentInsetAdjustmentBehavior="automatic" automaticallyAdjustKeyboardInsets style={{ backgroundColor: colors.bg }} contentContainerStyle={styles.content}>
        <Banner tone="info" text="Nenhum computador vinculado. Sem vínculo, memórias, tarefas e notas funcionam só neste aparelho." />
        <Button label="Vincular computador" icon="qr-code-outline" variant="primary" onPress={() => router.push('/pair')} />
      </ScrollView>
    );
  }

  return (
    <ScrollView contentInsetAdjustmentBehavior="automatic" automaticallyAdjustKeyboardInsets style={{ backgroundColor: colors.bg }} contentContainerStyle={styles.content} keyboardShouldPersistTaps="handled">
      <Card tone={availability.tone === 'ok' ? 'cyan' : availability.tone === 'warn' ? 'amber' : undefined}>
        <Text style={type.label}>{availability.label}</Text>
        {!!availability.detail && <Text style={type.caption}>{availability.detail}</Text>}
        <Text style={type.caption}>Funciona agora:</Text>
        <View style={styles.chips}>
          {availability.works.map((w) => (
            <Chip key={w} label={w} tone="success" />
          ))}
        </View>
        {availability.unavailable.length > 0 && (
          <>
            <Text style={type.caption}>Indisponível:</Text>
            <View style={styles.chips}>
              {availability.unavailable.map((w) => (
                <Chip key={w} label={w} tone="muted" />
              ))}
            </View>
          </>
        )}
        <Button label="Testar conexão" icon="refresh" onPress={() => void test()} loading={testing} />
      </Card>

      <SectionTitle>Computador vinculado</SectionTitle>
      <Row title={connection.serverName} subtitle={`Vinculado em ${new Date(connection.pairedAt).toLocaleString('pt-BR')}`} icon="desktop-outline" />
      <Row title="Impressão digital do certificado" subtitle={displayFingerprint(connection.pin)} icon="finger-print-outline" />
      <Field label="Endereço do PC (rede local ou VPN)" value={host} onChangeText={setHost} autoCapitalize="none" autoCorrect={false} />
      <Field label="Porta" value={port} onChangeText={setPort} keyboardType="number-pad" />
      <Button label="Salvar endereço" onPress={() => void saveAddress()} disabled={host === connection.host && port === String(connection.port)} />
      <Text style={type.caption}>Se o IP do PC mudar, atualize aqui: o certificado continua o mesmo e não é preciso vincular de novo.</Text>

      <SectionTitle>Motor de conversa</SectionTitle>
      <Segmented<Engine>
        value={s.engine}
        onChange={(v) => void s.update({ engine: v })}
        options={[{ value: 'marvin', label: 'MARVIN do PC' }, { value: 'ollama', label: 'Ollama no PC' }]}
      />
      {engines.map((e) => (
        <Text key={e.id} style={type.caption}>
          {e.label}: {e.available ? `${e.provider}${e.model ? ' · ' + e.model : ''}${e.local_model ? ' (local)' : ''}` : 'indisponível'} — {e.note}
        </Text>
      ))}
      {s.engine === 'ollama' && !engines.find((e) => e.id === 'ollama')?.available && <Banner tone="warn" text="Nenhum modelo do Ollama disponível no PC: as mensagens vão falhar até você voltar ao MARVIN do PC." />}
      <Text style={type.caption}>Chaves de provedores ficam no PC. O celular não guarda chaves de IA.</Text>

      <SectionTitle>Sessão</SectionTitle>
      <Button label="Vincular outro computador" icon="swap-horizontal" onPress={() => router.push('/pair')} />
      <Button label="Encerrar sessão neste celular" icon="log-out-outline" variant="danger" onPress={endSession} />
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  content: { padding: space.xl, gap: space.md, paddingBottom: space.xxxl },
  chips: { flexDirection: 'row', flexWrap: 'wrap', gap: space.sm },
});
