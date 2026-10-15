import * as Application from 'expo-application';
import { Camera } from 'expo-camera';
import * as Device from 'expo-device';
import { File, Paths } from 'expo-file-system';
import * as Notifications from 'expo-notifications';
import * as Sharing from 'expo-sharing';
import { useCallback, useEffect, useState } from 'react';
import { Platform, ScrollView, StyleSheet, Text, View } from 'react-native';
import { isNativeAvailable, MarvinNative } from '../../../modules/marvin-native';
import { Button, Card, SectionTitle } from '../../components/ui';
import { recentLogs } from '../../core/logging/logger';
import { redact } from '../../core/logging/redact';
import { refreshCapabilities, refreshConnectivity, useConnectivity } from '../../core/net/connectivity';
import { useConnectionInfo } from '../../core/security/credentials';
import { useSync } from '../../core/sync/syncEngine';
import { displayFingerprint } from '../../features/assistant/nlp/text';
import { micPermission, recognitionAvailability } from '../../features/voice/stt';
import { listDeviceVoices } from '../../features/voice/voices';
import { colors, space, type } from '../../theme/tokens';

interface Line {
  k: string;
  v: string;
}

export default function Diagnostics() {
  const connectivity = useConnectivity();
  const connection = useConnectionInfo((s) => s.connection);
  const sync = useSync();
  const [lines, setLines] = useState<Line[]>([]);
  const [logs, setLogs] = useState<{ at: string; level: string; scope: string; message: string }[]>([]);
  const [busy, setBusy] = useState(false);

  const collect = useCallback(async () => {
    const recognition = recognitionAvailability();
    const voices = await listDeviceVoices().catch(() => []);
    const audio = MarvinNative.getAudioState();
    const [mic, cam, notif] = await Promise.all([
      micPermission(false).catch(() => 'desconhecido'),
      Camera.getCameraPermissionsAsync().then((p) => p.status).catch(() => 'desconhecido'),
      Notifications.getPermissionsAsync().then((p) => p.status).catch(() => 'desconhecido'),
    ]);
    setLines([
      { k: 'App', v: `${Application.nativeApplicationVersion} (${Application.nativeBuildVersion})` },
      { k: 'Aparelho', v: `${Device.manufacturer ?? ''} ${Device.modelName ?? ''} · ${Device.osName ?? Platform.OS} ${Device.osVersion ?? '?'}` },
      { k: 'Módulo nativo', v: isNativeAvailable ? 'ativo' : 'ausente (TLS do gateway e áudio indisponíveis)' },
      { k: 'Transporte do gateway', v: MarvinNative.hasSecureTransport(Platform.OS === 'ios' ? 'ios' : 'android') ? 'pin verificado por requisição' : 'indisponível; atualize a build' },
      { k: 'Certificados fixados', v: String(MarvinNative.getPinnedKeys().length) },
      { k: 'Computador', v: connection ? `${connection.serverName} · ${connection.host}:${connection.port}` : 'não vinculado' },
      { k: 'Impressão digital', v: connection ? displayFingerprint(connection.pin) : '-' },
      { k: 'Rede do celular', v: `${connectivity.network}${connectivity.internet === false ? ' · sem internet' : ''}` },
      { k: 'Gateway', v: `${connectivity.gateway}${connectivity.latencyMs != null ? ` · ${connectivity.latencyMs} ms` : ''}${connectivity.gatewayMessage ? ` · ${connectivity.gatewayMessage}` : ''}` },
      { k: 'Assistente no PC', v: `${connectivity.assistant}${connectivity.assistantReason ? ` · ${connectivity.assistantReason}` : ''}` },
      { k: 'Cofre (Vault)', v: `${connectivity.vault}${connectivity.vaultMessage ? ` · ${connectivity.vaultMessage}` : ''}` },
      { k: 'Agente do PC', v: `${connectivity.desktop}${connectivity.desktopReason ? ` · ${connectivity.desktopReason}` : ''}` },
      { k: 'API do PC', v: connectivity.capabilities ? `v${connectivity.capabilities.api_version} · gateway ${connectivity.capabilities.server.version}` : '-' },
      { k: 'Sincronização', v: `${sync.pending} pendente(s)${sync.lastError ? ` · erro: ${sync.lastError}` : ''}` },
      { k: 'Microfone', v: String(mic) },
      { k: 'Câmera', v: String(cam) },
      { k: 'Notificações', v: String(notif) },
      { k: 'Reconhecimento de fala', v: `${recognition.available ? 'disponível' : 'indisponível'} · offline: ${recognition.onDevice ? 'sim' : 'não'}` },
      { k: 'Vozes pt no aparelho', v: `${voices.length} (${voices.filter((v) => v.likelyMale).length} provavelmente masculinas)` },
      { k: 'Saída de áudio', v: `${audio.route} · ${audio.inCall ? 'em chamada' : 'livre'}` },
    ]);
    setLogs(await recentLogs(120));
  }, [connectivity, connection, sync.pending, sync.lastError]);

  useEffect(() => {
    let active = true;
    void Promise.resolve().then(() => { if (active) return collect(); });
    return () => { active = false; };
  }, [collect]);

  const test = async () => {
    setBusy(true);
    await refreshConnectivity();
    await refreshCapabilities();
    await collect();
    setBusy(false);
  };

  const share = async () => {
    const text = redact(
      ['MARVIN Mobile · diagnóstico', new Date().toISOString(), '', ...lines.map((l) => `${l.k}: ${l.v}`), '', ...logs.map((l) => `${l.at} ${l.level} ${l.scope}: ${l.message}`)].join('\n'),
    );
    const file = new File(Paths.cache, 'marvin-diagnostico.txt');
    file.create({ overwrite: true });
    file.write(text);
    if (await Sharing.isAvailableAsync()) await Sharing.shareAsync(file.uri, { mimeType: 'text/plain', dialogTitle: 'Diagnóstico do MARVIN' });
  };

  return (
    <ScrollView contentInsetAdjustmentBehavior="automatic" automaticallyAdjustKeyboardInsets style={{ backgroundColor: colors.bg }} contentContainerStyle={styles.content}>
      <View style={{ flexDirection: 'row', gap: space.md }}>
        <Button label="Testar conexão" icon="refresh" onPress={() => void test()} loading={busy} style={{ flex: 1 }} />
        <Button label="Compartilhar" icon="share-outline" onPress={() => void share()} style={{ flex: 1 }} />
      </View>
      <Text style={type.caption}>Sem tokens, senhas ou códigos: o texto exportado passa por um filtro de credenciais.</Text>
      <Card>
        {lines.map((line) => (
          <View key={line.k} style={styles.line}>
            <Text style={[type.caption, { width: 130 }]}>{line.k}</Text>
            <Text style={[type.caption, { flex: 1, color: colors.text }]} selectable>
              {line.v}
            </Text>
          </View>
        ))}
      </Card>
      <SectionTitle>Registros recentes</SectionTitle>
      {logs.map((log, i) => (
        <Text key={i} style={[styles.log, log.level === 'error' ? { color: colors.danger } : log.level === 'warn' ? { color: colors.amber } : null]} selectable>
          {log.at.slice(11, 19)} {log.scope}: {log.message}
        </Text>
      ))}
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  content: { padding: space.xl, gap: space.md, paddingBottom: space.xxxl },
  line: { flexDirection: 'row', gap: space.sm },
  log: { fontFamily: 'monospace', fontSize: 11, color: colors.textSecondary },
});
