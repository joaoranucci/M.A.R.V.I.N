import { CameraView, useCameraPermissions } from 'expo-camera';
import { router, useLocalSearchParams } from 'expo-router';
import { useRef, useState } from 'react';
import { Linking, ScrollView, StyleSheet, Text, View } from 'react-native';
import { Banner, Button, Card, Field, Segmented } from '../components/ui';
import { MarvinNative } from '../../modules/marvin-native';
import { parsePairingUrl, validHost, type PairingPayload } from '../features/assistant/nlp/pairing';
import { displayFingerprint } from '../features/assistant/nlp/text';
import { pairWith } from '../features/gateway/pairing';
import { colors, radius, space, type } from '../theme/tokens';

export default function Pair() {
  // The QR payload can also arrive as a marvin://pair link; it is never used without confirmation.
  const params = useLocalSearchParams<Record<string, string>>();
  const linked = params.h
    ? parsePairingUrl('marvin://pair?' + Object.entries(params).map(([key, value]) => `${key}=${encodeURIComponent(String(value))}`).join('&'))
    : null;
  const [mode, setMode] = useState<'qr' | 'manual'>('qr');
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [done, setDone] = useState(false);

  const run = async (payload: PairingPayload) => {
    setBusy(true);
    setError(null);
    try {
      await pairWith(payload);
      setDone(true);
      setTimeout(() => router.back(), 900);
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Falha ao vincular.');
    } finally {
      setBusy(false);
    }
  };

  return (
    <ScrollView style={{ backgroundColor: colors.bg }} contentContainerStyle={styles.content} keyboardShouldPersistTaps="handled">
      <Text style={type.bodySecondary}>
        No computador, execute <Text style={{ color: colors.cyan }}>PAREAR_CELULAR.bat</Text> (ou “python -m marvin.gateway pair”). Ele mostra um QR Code e um código de 6 dígitos válido por 5 minutos.
      </Text>
      <Segmented value={mode} onChange={setMode} options={[{ value: 'qr', label: 'Ler QR Code' }, { value: 'manual', label: 'Digitar código' }]} />
      {done && <Banner tone="ok" text="Computador vinculado." />}
      {error && <Banner tone="error" text={error} />}
      {linked && !done && (
        <Card tone="amber">
          <Text style={type.label}>Vincular a “{linked.serverName}”?</Text>
          <Text style={type.bodySecondary}>
            {linked.host}:{linked.port} · impressão digital {displayFingerprint(linked.pin)}
          </Text>
          <Text style={type.caption}>Confirme que é o seu computador e que a impressão digital é a mesma mostrada nele.</Text>
          <Button label="Vincular este computador" icon="link" variant="amber" loading={busy} onPress={() => void run(linked)} />
        </Card>
      )}
      {mode === 'qr' ? <Scanner onPayload={run} busy={busy} /> : <Manual onPayload={run} busy={busy} />}
      <Text style={type.caption}>
        Use o endereço do PC na rede local (ex.: 192.168.0.10) ou na VPN. “localhost” no celular é o próprio celular, não o computador. A conexão é criptografada (TLS) e aceita apenas o certificado deste PC.
      </Text>
    </ScrollView>
  );
}

function Scanner({ onPayload, busy }: { onPayload: (p: PairingPayload) => void; busy: boolean }) {
  const [permission, requestPermission] = useCameraPermissions();
  const handled = useRef(false);
  const [invalid, setInvalid] = useState(false);
  if (!permission) return null;
  if (!permission.granted) {
    return (
      <Card>
        <Text style={type.body}>A câmera é usada apenas para ler o QR Code de vinculação.</Text>
        {permission.canAskAgain ? (
          <Button label="Permitir câmera" icon="camera-outline" variant="primary" onPress={() => void requestPermission()} />
        ) : (
          <Button label="Abrir configurações" onPress={() => void Linking.openSettings()} />
        )}
      </Card>
    );
  }
  return (
    <View style={styles.cameraWrap}>
      <CameraView
        style={StyleSheet.absoluteFill}
        facing="back"
        barcodeScannerSettings={{ barcodeTypes: ['qr'] }}
        onBarcodeScanned={
          busy || handled.current
            ? undefined
            : ({ data }) => {
                const payload = parsePairingUrl(data);
                if (!payload) {
                  setInvalid(true);
                  return;
                }
                handled.current = true;
                onPayload(payload);
                setTimeout(() => (handled.current = false), 4000);
              }
        }
      />
      <View style={styles.frame} pointerEvents="none" />
      {invalid && (
        <View style={styles.cameraNote}>
          <Text style={type.caption}>Esse QR Code não é de vinculação do MARVIN.</Text>
        </View>
      )}
    </View>
  );
}

function Manual({ onPayload, busy }: { onPayload: (p: PairingPayload) => void; busy: boolean }) {
  const [host, setHost] = useState('');
  const [port, setPort] = useState('8770');
  const [code, setCode] = useState('');
  const [probe, setProbe] = useState<{ pin: string; subject: string } | null>(null);
  const [checking, setChecking] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const portNumber = Number(port);
  const valid = validHost(host) && Number.isInteger(portNumber) && portNumber > 0 && portNumber < 65536 && /^\d{6}$/.test(code);

  const check = async () => {
    setError(null);
    setChecking(true);
    try {
      const result = await MarvinNative.probeCertificate(host.trim(), portNumber);
      setProbe({ pin: result.pin, subject: result.subject });
    } catch (e) {
      setError(`Não consegui alcançar ${host}:${port}. ${e instanceof Error ? e.message : ''}`);
    } finally {
      setChecking(false);
    }
  };

  return (
    <Card>
      <Field label="Endereço do computador" value={host} onChangeText={(v) => { setHost(v); setProbe(null); }} placeholder="192.168.0.10" autoCapitalize="none" autoCorrect={false} keyboardType="url" />
      <Field label="Porta" value={port} onChangeText={(v) => { setPort(v); setProbe(null); }} keyboardType="number-pad" />
      <Field label="Código de 6 dígitos" value={code} onChangeText={setCode} keyboardType="number-pad" maxLength={6} />
      {host.trim() && !validHost(host) && <Text style={[type.caption, { color: colors.amber }]}>Use o IP ou nome do PC na rede, não localhost.</Text>}
      {error && <Banner tone="error" text={error} />}
      {!probe ? (
        <Button label="Verificar computador" icon="shield-checkmark-outline" onPress={() => void check()} loading={checking} disabled={!valid} />
      ) : (
        <>
          <Banner tone="warn" text="Compare esta impressão digital com a mostrada no PC. Só continue se forem idênticas.">
            <Text style={styles.fingerprint} selectable>
              {displayFingerprint(probe.pin)}
            </Text>
          </Banner>
          <Button
            label="São iguais · vincular"
            icon="link"
            variant="primary"
            loading={busy}
            onPress={() => onPayload({ host: host.trim(), port: portNumber, code, pin: probe.pin, serverName: 'PC', serverId: '' })}
          />
        </>
      )}
    </Card>
  );
}

const styles = StyleSheet.create({
  content: { padding: space.xl, gap: space.lg, paddingBottom: space.xxxl },
  cameraWrap: { height: 320, borderRadius: radius.lg, overflow: 'hidden', backgroundColor: '#000', alignItems: 'center', justifyContent: 'center' },
  frame: { width: 220, height: 220, borderWidth: 2, borderColor: colors.cyan, borderRadius: radius.lg },
  cameraNote: { position: 'absolute', bottom: 12, backgroundColor: 'rgba(0,0,0,0.7)', padding: 8, borderRadius: 8 },
  fingerprint: { fontFamily: 'monospace', fontSize: 16, color: colors.text },
});
