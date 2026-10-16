import { useEffect, useState } from 'react';
import { ActivityIndicator, Linking, Platform, ScrollView, StyleSheet, Switch, Text, View } from 'react-native';
import { Banner, Button, Chip, Row, Segmented, SectionTitle } from '../../components/ui';
import { useConnectivity } from '../../core/net/connectivity';
import { useSettings } from '../../core/settings';
import { preferredAudioRoute, routeLabel, selectAudioRoute, useAudioSession } from '../../features/voice/audioSession';
import { recognitionAvailability } from '../../features/voice/stt';
import { stopSpeaking, testVoice } from '../../features/voice/tts';
import { listDeviceVoices, preferredDeviceVoice, type DeviceVoice } from '../../features/voice/voices';
import { colors, space, type } from '../../theme/tokens';

const RATES = [0.85, 1.0, 1.15, 1.3];
const VOLUMES = [0.6, 0.8, 1.0];
const SILENCE = [1000, 1400, 2200];

export default function VoiceSettings() {
  const s = useSettings();
  const route = useAudioSession((a) => a.route);
  const [preferred, setPreferred] = useState(preferredAudioRoute());
  const [routeError, setRouteError] = useState<string | null>(null);
  const caps = useConnectivity((c) => c.capabilities);
  const online = useConnectivity((c) => c.gateway === 'online');
  const [voices, setVoices] = useState<DeviceVoice[] | null>(null);
  const [testing, setTesting] = useState<string | null>(null);
  const recognition = recognitionAvailability();
  const serverVoices = caps?.speech.voices ?? [];

  useEffect(() => {
    listDeviceVoices()
      .then((list) => {
        setVoices(list);
        if (!s.deviceVoiceId) {
          const preferred = preferredDeviceVoice(list);
          if (preferred) void s.update({ deviceVoiceId: preferred.id });
        }
      })
      .catch(() => setVoices([]));
    return () => { void stopSpeaking(); };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const test = async (kind: 'device' | 'server', id: string) => {
    setTesting(`${kind}:${id}`);
    await testVoice(kind, id);
    setTesting(null);
  };

  const ptBr = voices?.filter((v) => /pt[-_]br/i.test(v.language)) ?? [];
  const hasMale = ptBr.some((v) => v.likelyMale);

  return (
    <ScrollView contentInsetAdjustmentBehavior="automatic" automaticallyAdjustKeyboardInsets style={{ backgroundColor: colors.bg }} contentContainerStyle={styles.content}>
      <Row
        title="Responder em voz alta"
        subtitle="Com isso desligado, as respostas aparecem só na tela."
        right={<Switch value={s.speakReplies} onValueChange={(v) => void s.update({ speakReplies: v })} trackColor={{ true: colors.cyan, false: colors.surfaceSolid }} thumbColor={colors.text} />}
      />
      <Text style={type.caption}>Origem da voz</Text>
      <Segmented
        value={s.voiceProvider}
        onChange={(v) => void s.update({ voiceProvider: v })}
        options={[{ value: 'server', label: 'Voz do PC' }, { value: 'device', label: 'Voz do aparelho' }]}
      />
      <Text style={type.caption}>
        Voz do PC: gerada no computador (Faber é local; Antônio usa um serviço online da Microsoft). Sem conexão, o MARVIN usa a voz do aparelho automaticamente.
      </Text>

      <SectionTitle>Vozes do PC</SectionTitle>
      {!online && <Text style={type.caption}>Conecte ao PC para listar e testar.</Text>}
      {serverVoices.map((v) => (
        <Row
          key={v.id}
          title={v.label}
          subtitle={v.available ? v.note : v.reason ?? 'Indisponível'}
          icon={s.serverVoiceId === v.id && s.voiceProvider === 'server' ? 'radio-button-on' : 'radio-button-off'}
          onPress={v.available ? () => void s.update({ serverVoiceId: v.id, voiceProvider: 'server' }) : undefined}
          right={
            <View style={{ alignItems: 'flex-end', gap: 4 }}>
              <Chip label={v.gender === 'male' ? 'masculina' : v.gender} tone="cyan" />
              <Button label="Testar" compact disabled={!v.available || !online} loading={testing === `server:${v.id}`} onPress={() => void test('server', v.id)} />
            </View>
          }
        />
      ))}

      <SectionTitle>Vozes do aparelho (português)</SectionTitle>
      {voices === null && <ActivityIndicator color={colors.cyan} />}
      {voices && !hasMale && (
        <Banner tone="warn" text={Platform.OS === 'ios' ? 'Teste as vozes em português abaixo. O iPhone não informa o gênero nesta API. Outras vozes podem ser instaladas em Ajustes › Acessibilidade › Conteúdo Falado.' : 'Não identifiquei uma voz masculina em português do Brasil. Teste as vozes abaixo ou instale outras no mecanismo de texto para fala.'}>
          <Button label="Abrir ajustes de voz" compact onPress={() => void (Platform.OS === 'android' ? Linking.sendIntent('com.android.settings.TTS_SETTINGS').catch(() => Linking.openSettings()) : Linking.openSettings())} style={{ alignSelf: 'flex-start' }} />
        </Banner>
      )}
      {voices && voices.length === 0 && <Text style={type.caption}>Nenhuma voz em português instalada.</Text>}
      {voices?.map((v) => (
        <Row
          key={v.id}
          title={v.name}
          subtitle={`${v.language}${v.network ? ' · requer internet' : Platform.OS === 'ios' ? ' · voz do sistema' : ' · no aparelho'}${v.likelyMale ? ' · provavelmente masculina' : ''}`}
          icon={s.deviceVoiceId === v.id ? 'radio-button-on' : 'radio-button-off'}
          onPress={() => void s.update({ deviceVoiceId: v.id })}
          right={<Button label="Testar" compact loading={testing === `device:${v.id}`} onPress={() => void test('device', v.id)} />}
        />
      ))}

      {Platform.OS === 'ios' && (
        <>
          <SectionTitle>Saída de áudio</SectionTitle>
          <Text style={type.caption}>Saída atual: {routeLabel[route]}. Escolha fones Bluetooth e AirPlay pela Central de Controle do iPhone.</Text>
          <Segmented value={preferred} options={[{ value: 'system', label: 'Automática' }, { value: 'speaker', label: 'Alto-falante' }, { value: 'earpiece', label: 'Auricular' }]}
            onChange={(value) => {
              if (selectAudioRoute(value)) { setPreferred(value); setRouteError(null); }
              else setRouteError('Não foi possível trocar a saída. Encerre a chamada ou selecione a saída na Central de Controle.');
            }} />
          {routeError && <Banner tone="warn" text={routeError} />}
        </>
      )}
      <SectionTitle>Velocidade e volume</SectionTitle>
      <Segmented value={String(s.speechRate)} onChange={(v) => void s.update({ speechRate: Number(v) })} options={RATES.map((r) => ({ value: String(r), label: `${r.toFixed(2).replace('.', ',')}×` }))} />
      <Segmented value={String(s.speechVolume)} onChange={(v) => void s.update({ speechVolume: Number(v) })} options={VOLUMES.map((r) => ({ value: String(r), label: `${Math.round(r * 100)}%` }))} />

      <SectionTitle>Reconhecimento de fala</SectionTitle>
      {!recognition.available && <Banner tone="warn" text={recognition.reason ?? 'Reconhecimento indisponível.'} />}
      <Row
        title="Processar a fala no aparelho"
        subtitle={recognition.onDevice ? 'Mais privado; exige português offline. Desligado, o sistema pode enviar o áudio ao serviço de reconhecimento da Apple ou do Google.' : 'Este aparelho não oferece reconhecimento offline para o app.'}
        right={<Switch value={s.onDeviceRecognition} disabled={!recognition.onDevice && !s.onDeviceRecognition} onValueChange={(v) => void s.update({ onDeviceRecognition: v })} trackColor={{ true: colors.cyan, false: colors.surfaceSolid }} thumbColor={colors.text} />}
      />
      {Platform.OS === 'android' && <Text style={type.caption}>Pausa para encerrar a fala automaticamente</Text>}
      {Platform.OS === 'android' && <Segmented value={String(s.silenceMs)} onChange={(v) => void s.update({ silenceMs: Number(v) })} options={SILENCE.map((ms) => ({ value: String(ms), label: `${(ms / 1000).toFixed(1).replace('.', ',')} s` }))} />}
      {Platform.OS === 'ios' && <Text style={type.caption}>No iPhone, toque no núcleo para falar e em Concluir para enviar. O iOS controla o encerramento automático da captura. Não há escuta por “Marvin” com o app encerrado.</Text>}
      <Text style={type.caption}>
        O microfone nunca fica aberto enquanto o MARVIN fala, e frases parecidas com a última resposta dele são ignoradas para não virarem instruções.
      </Text>
    </ScrollView>
  );
}

const styles = StyleSheet.create({ content: { padding: space.xl, gap: space.sm, paddingBottom: space.xxxl } });
