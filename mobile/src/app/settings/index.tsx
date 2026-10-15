import * as Application from 'expo-application';
import { router } from 'expo-router';
import { useEffect, useState } from 'react';
import { Alert, ScrollView, StyleSheet, Switch, Text, View } from 'react-native';
import { Button, Field, Row, Segmented, SectionTitle } from '../../components/ui';
import { reloadLocalData } from '../../core/bootstrap';
import { useConnectionInfo } from '../../core/security/credentials';
import { useSettings, type ReduceMotion } from '../../core/settings';
import { setWakeWord, wakeWordSupport } from '../../features/assistant/controller';
import { downloadOfflinePortuguese, offlinePortuguese } from '../../features/voice/stt';
import { colors, space, type } from '../../theme/tokens';

export default function SettingsIndex() {
  const s = useSettings();
  const connection = useConnectionInfo((c) => c.connection);
  const wake = wakeWordSupport();
  const [name, setName] = useState(s.userName);
  const [offline, setOffline] = useState<'installed' | 'missing' | 'unsupported' | null>(null);
  const [downloadNote, setDownloadNote] = useState<string | null>(null);
  useEffect(() => {
    void offlinePortuguese().then(setOffline);
  }, []);
  const wakeReady = wake.supported && offline === 'installed';

  const toggleDemo = (value: boolean) => {
    const apply = async () => {
      await s.update({ demoMode: value });
      await reloadLocalData();
    };
    if (value) {
      Alert.alert('Ativar modo demonstração?', 'Respostas passam a ser simuladas e identificadas. Nenhuma ação é enviada ao computador e os dados de demonstração ficam separados dos reais.', [
        { text: 'Cancelar', style: 'cancel' },
        { text: 'Ativar', onPress: () => void apply() },
      ]);
    } else void apply();
  };

  return (
    <ScrollView contentInsetAdjustmentBehavior="automatic" automaticallyAdjustKeyboardInsets keyboardShouldPersistTaps="handled" style={{ backgroundColor: colors.bg }} contentContainerStyle={styles.content}>
      <Row icon="volume-high-outline" title="Voz e fala" subtitle="Voz masculina, velocidade, volume, reconhecimento" onPress={() => router.push('/settings/voice')} />
      <Row icon="link-outline" title="Conexão com o PC" subtitle={connection ? `${connection.serverName} · ${connection.host}:${connection.port}` : 'Nenhum computador vinculado'} onPress={() => router.push('/settings/connection')} />
      <Row icon="shield-outline" title="Dados e privacidade" subtitle="Armazenamento local, histórico, sessão" onPress={() => router.push('/settings/storage')} />
      <Row icon="pulse-outline" title="Diagnóstico" subtitle="Estado técnico, permissões e registros" onPress={() => router.push('/settings/diagnostics')} />

      <SectionTitle>Escuta por “Marvin”</SectionTitle>
      <Row
        icon="mic-outline"
        title="Ativar com “Marvin” (experimental)"
        subtitle={
          !wake.supported
            ? wake.reason
            : offline === 'missing'
              ? 'Falta o pacote offline de português do reconhecimento de fala.'
              : 'Somente com o app aberto e em primeiro plano. Um aviso mostra quando o microfone está ativo.'
        }
        right={<Switch value={s.wakeWordEnabled && wakeReady} disabled={!wakeReady} onValueChange={setWakeWord} trackColor={{ true: colors.cyan, false: colors.surfaceSolid }} thumbColor={colors.text} accessibilityLabel="Ativar com Marvin" />}
      />
      {offline === 'missing' && (
        <Button
          label="Baixar pacote de português"
          icon="download-outline"
          compact
          onPress={() =>
            void downloadOfflinePortuguese()
              .then(setDownloadNote)
              .catch((e: unknown) => setDownloadNote(e instanceof Error ? e.message : 'Não foi possível iniciar o download.'))
          }
          style={{ alignSelf: 'flex-start' }}
        />
      )}
      {downloadNote && <Text style={type.caption}>{downloadNote}</Text>}
      <Text style={type.caption}>
        Escuta com o app fechado ou em segundo plano ainda não está implementada (exige serviço em primeiro plano com notificação permanente e detecção local). No iOS não há suporte equivalente nesta versão.
      </Text>

      <SectionTitle>Preferências</SectionTitle>
      <Field label="Como o MARVIN chama você" value={name} onChangeText={setName} onEndEditing={() => void s.update({ userName: name.trim() || 'João' })} />
      <Text style={type.caption}>Reduzir movimento do núcleo</Text>
      <Segmented<ReduceMotion>
        value={s.reduceMotion}
        onChange={(v) => void s.update({ reduceMotion: v })}
        options={[{ value: 'system', label: 'Sistema' }, { value: 'on', label: 'Reduzir' }, { value: 'off', label: 'Completo' }]}
      />
      <Row
        title="Confirmar também ações comuns no PC"
        subtitle="Abrir navegador, pastas e apps passam a mostrar prévia. Ações destrutivas sempre pedem confirmação."
        right={<Switch value={s.confirmCommonDesktopActions} onValueChange={(v) => void s.update({ confirmCommonDesktopActions: v })} trackColor={{ true: colors.cyan, false: colors.surfaceSolid }} thumbColor={colors.text} />}
      />
      <Row
        title="Modo demonstração"
        subtitle="Dados e respostas simulados, sempre identificados. Nada é executado."
        right={<Switch value={s.demoMode} onValueChange={toggleDemo} trackColor={{ true: colors.amber, false: colors.surfaceSolid }} thumbColor={colors.text} />}
      />

      <View style={{ marginTop: space.xl }}>
        <Text style={type.caption}>MARVIN Mobile {Application.nativeApplicationVersion ?? '0.1.0'} ({Application.nativeBuildVersion ?? '1'})</Text>
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({ content: { padding: space.xl, gap: space.sm, paddingBottom: space.xxxl } });
