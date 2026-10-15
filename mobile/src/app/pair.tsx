import { CameraView, useCameraPermissions } from 'expo-camera';
import { router, useFocusEffect, useLocalSearchParams } from 'expo-router';
import { useCallback, useEffect, useRef, useState } from 'react';
import { Linking, ScrollView, StyleSheet, Text, View } from 'react-native';
import { Banner, Button, Card, Field, Segmented } from '../components/ui';
import { MarvinNative } from '../../modules/marvin-native';
import { parsePairingUrl, validHost, type PairingPayload } from '../features/assistant/nlp/pairing';
import { displayFingerprint } from '../features/assistant/nlp/text';
import { pairWith } from '../features/gateway/pairing';
import { colors, radius, space, type } from '../theme/tokens';

export default function Pair() {
  const params = useLocalSearchParams<Record<string, string | string[]>>();
  const legacy = params.h ? 'marvin://pair?' + Object.entries(params)
    .filter(([key]) => ['v', 'h', 'p', 'c', 'k', 'n', 's'].includes(key))
    .map(([key, value]) => key + '=' + encodeURIComponent(String(value))).join('&') : '';
  const rawLink = typeof params.payload === 'string' ? params.payload : legacy;
  const linked = rawLink ? parsePairingUrl(rawLink) : null;
  const [scanned, setScanned] = useState<PairingPayload | null>(null);
  const [mode, setMode] = useState<'qr' | 'manual'>('qr');
  const [busy, setBusy] = useState(false);
  const busyRef = useRef(false);
  const revision = useRef(0);
  const [error, setError] = useState<string | null>(null);
  const [done, setDone] = useState(false);
  const candidate = linked ?? scanned;

  useEffect(() => {
    revision.current++;
    setScanned(null);
    setDone(false);
    setError(null);
  }, [rawLink]);

  const run = async (payload: PairingPayload) => {
    if (busyRef.current) return;
    const mine = revision.current;
    busyRef.current = true;
    setBusy(true);
    setError(null);
    try {
      await pairWith(payload);
      if (mine === revision.current) setDone(true);
    } catch (e) {
      if (mine === revision.current) setError(e instanceof Error ? e.message : 'Falha ao vincular.');
    } finally {
      busyRef.current = false;
      setBusy(false);
    }
  };

  return (
    <ScrollView style={{ backgroundColor: colors.bg }} contentContainerStyle={styles.content}
      keyboardShouldPersistTaps="handled" contentInsetAdjustmentBehavior="automatic" automaticallyAdjustKeyboardInsets>
      <Text style={type.bodySecondary}>No MARVIN do computador, abra o pareamento do celular e gere o QR Code ou o código de seis dígitos.</Text>
      {!!(params.invalid || (rawLink && !linked)) && <Banner tone="error" text="Link de pareamento inválido. Gere outro QR Code no computador." />}
      {done ? (
        <>
          <Banner tone="ok" text="Computador vinculado." />
          <Button label="Continuar" variant="primary" onPress={() => router.replace('/')} />
        </>
      ) : (
        <>
          {error && <Banner tone="error" text={error} />}
          {candidate ? (
            <Card tone="amber">
              <Text style={type.label}>Vincular a “{candidate.serverName}”?</Text>
              <Text style={type.bodySecondary}>{candidate.host}:{candidate.port}</Text>
              <Text style={styles.fingerprint} selectable>{displayFingerprint(candidate.pin)}</Text>
              <Text style={type.caption}>Compare a impressão digital com a mostrada no seu computador. O código só será enviado depois da sua confirmação.</Text>
              <Button label="São iguais · vincular" icon="link" variant="amber" loading={busy} onPress={() => void run(candidate)} />
              {!linked && <Button label="Ler outro QR Code" disabled={busy} onPress={() => setScanned(null)} />}
            </Card>
          ) : (
            <>
              <Segmented value={mode} onChange={setMode} options={[{ value: 'qr', label: 'Ler QR Code' }, { value: 'manual', label: 'Digitar código' }]} />
              {mode === 'qr' ? <Scanner onPayload={setScanned} busy={busy} /> : <Manual onPayload={run} busy={busy} />}
            </>
          )}
        </>
      )}
      <Text style={type.caption}>Use o endereço do PC na mesma rede local ou VPN. No iPhone, permita acesso à rede local quando solicitado. A conexão exige o certificado e a impressão digital do seu PC.</Text>
    </ScrollView>
  );
}

function Scanner({ onPayload, busy }: { onPayload: (p: PairingPayload) => void; busy: boolean }) {
  const [permission, requestPermission] = useCameraPermissions();
  const handled = useRef(false);
  const [invalid, setInvalid] = useState(false);
  const [focused, setFocused] = useState(false);
  useFocusEffect(useCallback(() => {
    setFocused(true);
    return () => setFocused(false);
  }, []));
  if (!permission || !focused) return null;
  if (!permission.granted) {
    return (
      <Card>
        <Text style={type.body}>A câmera é usada apenas para ler o QR Code de vinculação.</Text>
        {permission.canAskAgain
          ? <Button label="Permitir câmera" icon="camera-outline" variant="primary" onPress={() => void requestPermission()} />
          : <Button label="Abrir configurações" onPress={() => void Linking.openSettings()} />}
      </Card>
    );
  }
  return (
    <View style={styles.cameraWrap}>
      <CameraView style={StyleSheet.absoluteFill} facing="back" barcodeScannerSettings={{ barcodeTypes: ['qr'] }}
        onBarcodeScanned={busy || handled.current ? undefined : ({ data }) => {
          const payload = parsePairingUrl(data);
          if (!payload) { setInvalid(true); return; }
          handled.current = true;
          onPayload(payload);
        }} />
      <View style={styles.frame} pointerEvents="none" />
      {invalid && <View style={styles.cameraNote}><Text style={type.caption}>Esse QR Code não é de vinculação do MARVIN.</Text></View>}
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
      <Field editable={!checking && !busy} label="Endereço do computador" value={host} onChangeText={(v) => { setHost(v); setProbe(null); }} placeholder="192.168.0.10" autoCapitalize="none" autoCorrect={false} keyboardType="url" />
      <Field editable={!checking && !busy} label="Porta" value={port} onChangeText={(v) => { setPort(v); setProbe(null); }} keyboardType="number-pad" />
      <Field editable={!checking && !busy} label="Código de 6 dígitos" value={code} onChangeText={setCode} keyboardType="number-pad" maxLength={6} />
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
