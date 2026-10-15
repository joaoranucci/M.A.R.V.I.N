import { useEffect, useState } from 'react';
import { ActivityIndicator, Linking, ScrollView, StyleSheet, Switch, Text, View } from 'react-native';
import { Banner, Button, Chip, Row, Segmented, SectionTitle } from '../../components/ui';
import { useConnectivity } from '../../core/net/connectivity';
import { useSettings } from '../../core/settings';
import { recognitionAvailability } from '../../features/voice/stt';
import { stopSpeaking, testVoice } from '../../features/voice/tts';
import { listDeviceVoices, preferredDeviceVoice, type DeviceVoice } from '../../features/voice/voices';
import { colors, space, type } from '../../theme/tokens';

const RATES = [0.85, 1.0, 1.15, 1.3];
const VOLUMES = [0.6, 0.8, 1.0];
const SILENCE = [1000, 1400, 2200];

export default function VoiceSettings() {
  const s = useSettings();
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
    return () => stopSpeaking();
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
    <ScrollView style={{ backgroundColor: colors.bg }} contentContainerStyle={styles.content}>
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
        <Banner tone="warn" text="Não identifiquei uma voz masculina em português do Brasil neste aparelho. O Android não informa o gênero: teste as vozes abaixo, use a voz do PC ou instale vozes no mecanismo de texto para fala.">
          <Button label="Configurações de texto para fala" compact onPress={() => void Linking.sendIntent('com.android.settings.TTS_SETTINGS').catch(() => Linking.openSettings())} style={{ alignSelf: 'flex-start' }} />
        </Banner>
      )}
      {voices && voices.length === 0 && <Text style={type.caption}>Nenhuma voz em português instalada.</Text>}
      {voices?.map((v) => (
        <Row
          key={v.id}
          title={v.name}
          subtitle={`${v.language}${v.network ? ' · requer internet' : ' · no aparelho'}${v.likelyMale ? ' · provavelmente masculina' : ''}`}
          icon={s.deviceVoiceId === v.id ? 'radio-button-on' : 'radio-button-off'}
          onPress={() => void s.update({ deviceVoiceId: v.id })}
          right={<Button label="Testar" compact loading={testing === `device:${v.id}`} onPress={() => void test('device', v.id)} />}
        />
      ))}

      <SectionTitle>Velocidade e volume</SectionTitle>
      <Segmented value={String(s.speechRate)} onChange={(v) => void s.update({ speechRate: Number(v) })} options={RATES.map((r) => ({ value: String(r), label: `${r.toFixed(2).replace('.', ',')}×` }))} />
      <Segmented value={String(s.speechVolume)} onChange={(v) => void s.update({ speechVolume: Number(v) })} options={VOLUMES.map((r) => ({ value: String(r), label: `${Math.round(r * 100)}%` }))} />

      <SectionTitle>Reconhecimento de fala</SectionTitle>
      {!recognition.available && <Banner tone="warn" text={recognition.reason ?? 'Reconhecimento indisponível.'} />}
      <Row
        title="Processar a fala no aparelho"
        subtitle={recognition.onDevice ? 'Mais privado; exige o pacote de português offline. Desligado, o Android pode usar o serviço online do Google.' : 'Este aparelho não oferece reconhecimento offline para o app.'}
        right={<Switch value={s.onDeviceRecognition && recognition.onDevice} disabled={!recognition.onDevice} onValueChange={(v) => void s.update({ onDeviceRecognition: v })} trackColor={{ true: colors.cyan, false: colors.surfaceSolid }} thumbColor={colors.text} />}
      />
      <Text style={type.caption}>Pausa para encerrar a fala automaticamente</Text>
      <Segmented value={String(s.silenceMs)} onChange={(v) => void s.update({ silenceMs: Number(v) })} options={SILENCE.map((ms) => ({ value: String(ms), label: `${(ms / 1000).toFixed(1).replace('.', ',')} s` }))} />
      <Text style={type.caption}>
        O microfone nunca fica aberto enquanto o MARVIN fala, e frases parecidas com a última resposta dele são ignoradas para não virarem instruções.
      </Text>
    </ScrollView>
  );
}

const styles = StyleSheet.create({ content: { padding: space.xl, gap: space.sm, paddingBottom: space.xxxl } });
