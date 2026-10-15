import { Ionicons } from '@expo/vector-icons';
import { router } from 'expo-router';
import { useCallback, useEffect, useState } from 'react';
import { Alert, RefreshControl, ScrollView, StyleSheet, Text, View } from 'react-native';
import { useSafeAreaInsets } from 'react-native-safe-area-context';
import { Banner, Button, Card, Chip, Dot, Row, SectionTitle } from '../../components/ui';
import { describeAvailability, refreshCapabilities, refreshConnectivity, useConnectivity } from '../../core/net/connectivity';
import { useConnectionInfo } from '../../core/security/credentials';
import { useSettings } from '../../core/settings';
import { createSimulatedWearable } from '../../features/devices/wearables/simulator';
import { registerWearable, registeredWearables, unregisterWearable, useWearables } from '../../features/devices/wearables/hub';
import type { WearableKind } from '../../features/devices/wearables/types';
import { gateway } from '../../features/gateway/api';
import type { TLinkedDevice } from '../../features/gateway/schemas';
import { colors, radius, space, type } from '../../theme/tokens';

export default function Devices() {
  const insets = useSafeAreaInsets();
  const connectivity = useConnectivity();
  const connection = useConnectionInfo((s) => s.connection);
  const demo = useSettings((s) => s.demoMode);
  const availability = describeAvailability(connectivity, demo);
  const [devices, setDevices] = useState<TLinkedDevice[]>([]);
  const [refreshing, setRefreshing] = useState(false);

  const loadDevices = useCallback(async () => {
    if (connectivity.gateway !== 'online') return;
    try {
      setDevices(await gateway.devices());
    } catch {
      // Keep the last known list during a transient network failure.
    }
  }, [connectivity.gateway]);

  useEffect(() => {
    let active = true;
    void Promise.resolve().then(() => { if (active) return loadDevices(); });
    return () => { active = false; };
  }, [loadDevices]);

  const refresh = async () => {
    setRefreshing(true);
    await refreshConnectivity();
    await refreshCapabilities();
    await loadDevices();
    setRefreshing(false);
  };

  const revoke = (device: TLinkedDevice) =>
    Alert.alert('Revogar acesso?', `${device.name} deixará de acessar o MARVIN do PC.`, [
      { text: 'Cancelar', style: 'cancel' },
      {
        text: 'Revogar',
        style: 'destructive',
        onPress: async () => {
          try {
            await gateway.revokeDevice(device.current ? 'self' : device.id);
            if (device.current) await useConnectionInfo.getState().clear();
            await refresh();
          } catch (error) {
            Alert.alert('Falha', error instanceof Error ? error.message : '');
          }
        },
      },
    ]);

  const actions = connectivity.capabilities?.desktop.actions ?? [];
  const dot = availability.tone === 'ok' ? colors.success : availability.tone === 'warn' ? colors.amber : colors.slate;

  return (
    <View style={[styles.screen, { paddingTop: insets.top + space.md }]}>
      <Text style={[type.title, styles.title]} accessibilityRole="header">
        Dispositivos
      </Text>
      <ScrollView contentInsetAdjustmentBehavior="automatic" automaticallyAdjustKeyboardInsets contentContainerStyle={styles.list} refreshControl={<RefreshControl refreshing={refreshing} onRefresh={() => void refresh()} tintColor={colors.cyan} />}>
        <Card tone={availability.tone === 'ok' ? 'cyan' : undefined}>
          <View style={styles.headerRow}>
            <View style={styles.pcIcon}>
              <Ionicons name="desktop-outline" size={26} color={colors.cyan} />
            </View>
            <View style={{ flex: 1, gap: 2 }}>
              <Text style={type.label}>{connection?.serverName ?? 'Computador'}</Text>
              <View style={{ flexDirection: 'row', alignItems: 'center', gap: space.sm }}>
                <Dot color={dot} />
                <Text style={type.caption}>{availability.label}</Text>
              </View>
            </View>
          </View>
          {!!availability.detail && <Text style={type.caption}>{availability.detail}</Text>}
          {connection ? (
            <>
              <View style={styles.chips}>
                <Chip label={connectivity.assistant === 'ok' || connectivity.assistant === 'busy' ? 'Conversa disponível' : 'Conversa indisponível'} tone={connectivity.assistant === 'unavailable' || connectivity.assistant === 'unknown' ? 'muted' : 'success'} />
                <Chip label={connectivity.vault === 'ok' ? 'Cofre aberto' : 'Cofre fechado'} tone={connectivity.vault === 'ok' ? 'success' : 'amber'} />
                <Chip label={connectivity.desktop === 'online' ? 'Agente ativo' : 'Agente inativo'} tone={connectivity.desktop === 'online' ? 'success' : 'amber'} />
              </View>
              {connectivity.capabilities?.conversation.engines.map((engine) => (
                <Text key={engine.id} style={type.caption}>
                  {engine.label}: {engine.available ? `${engine.provider}${engine.model ? ' · ' + engine.model : ''}` : 'indisponível'} — {engine.note}
                </Text>
              ))}
              <Button label="Conexão e vinculação" icon="link-outline" onPress={() => router.push('/settings/connection')} />
            </>
          ) : (
            <Button label="Vincular computador" icon="qr-code-outline" variant="primary" onPress={() => router.push('/pair')} />
          )}
        </Card>

        {connection && (
          <>
            <SectionTitle>Recursos do computador</SectionTitle>
            {actions.length === 0 && <Text style={type.caption}>Conecte ao PC para ver os recursos oferecidos.</Text>}
            {actions.map((action) => (
              <Row
                key={action.id}
                title={action.label}
                subtitle={action.description}
                icon={action.risk === 'destructive' ? 'warning-outline' : 'flash-outline'}
                right={
                  <View style={{ alignItems: 'flex-end', gap: 4 }}>
                    <Chip label={action.available ? 'disponível' : 'indisponível'} tone={action.available ? 'success' : 'muted'} />
                    {action.requires_confirmation && <Chip label="pede confirmação" tone="amber" />}
                    {action.verifiable && <Chip label="verificável" tone="cyan" />}
                  </View>
                }
              />
            ))}

            <SectionTitle>Celulares vinculados</SectionTitle>
            {connectivity.gateway !== 'online' && <Text style={type.caption}>Disponível com o PC conectado.</Text>}
            {devices.map((device) => (
              <Row
                key={device.id}
                title={`${device.name}${device.current ? ' (este)' : ''}`}
                subtitle={device.revoked_at ? `Revogado em ${new Date(device.revoked_at).toLocaleDateString('pt-BR')}` : `Visto ${device.last_seen_at ? new Date(device.last_seen_at).toLocaleString('pt-BR') : 'nunca'}`}
                icon="phone-portrait-outline"
                right={device.revoked_at ? <Chip label="revogado" tone="muted" /> : <Button label="Revogar" compact variant="danger" onPress={() => revoke(device)} />}
              />
            ))}
          </>
        )}

        <SectionTitle>Wearables</SectionTitle>
        <Wearable kind="bracelet" title="Pulseira MARVIN" text="Software principal do wearable. Acionamento, estado e bateria aparecerão aqui quando o hardware fornecer." demo={demo} />
        <Wearable kind="glasses" title="Óculos inteligentes" text="Conectados à pulseira por Bluetooth. Áudio e comandos usarão canais separados." demo={demo} />
        <Text style={type.caption}>A integração física ainda não existe: perfis BLE, áudio e protocolo estão documentados para definição com o hardware.</Text>
      </ScrollView>
    </View>
  );
}

function Wearable({ kind, title, text, demo }: { kind: WearableKind; title: string; text: string; demo: boolean }) {
  const status = useWearables((s) => s.devices[kind]);
  const simulated = registeredWearables().find((w) => w.kind === kind && w.simulated) as (ReturnType<typeof createSimulatedWearable> | undefined);
  return (
    <Card>
      <View style={styles.headerRow}>
        <Ionicons name={kind === 'bracelet' ? 'watch-outline' : 'glasses-outline'} size={24} color={status?.link === 'connected' ? colors.cyan : colors.textMuted} />
        <Text style={[type.label, { flex: 1 }]}>{title}</Text>
        <Chip label={status ? `${status.link === 'connected' ? 'conectado' : status.link}${status.simulated ? ' · simulado' : ''}` : 'não conectado'} tone={status?.link === 'connected' ? (status.simulated ? 'amber' : 'success') : 'muted'} />
      </View>
      <Text style={type.caption}>{text}</Text>
      {status?.battery != null && <Text style={type.caption}>Bateria informada: {Math.round(status.battery * 100)}%{status.simulated ? ' (simulada)' : ''}</Text>}
      {demo && (
        <View style={{ flexDirection: 'row', gap: space.sm, flexWrap: 'wrap' }}>
          {!simulated ? (
            <Button label="Simular conexão" compact onPress={() => void registerWearable(createSimulatedWearable(kind))} />
          ) : (
            <>
              <Button label="Simular acionamento" compact variant="amber" onPress={() => simulated.emit({ type: 'trigger', source: kind, gesture: 'press' })} />
              <Button label="Desconectar" compact onPress={() => void unregisterWearable(simulated.id)} />
            </>
          )}
        </View>
      )}
      {!demo && <Banner tone="info" text="Sem hardware conectado. O simulador fica disponível no modo demonstração." />}
    </Card>
  );
}

const styles = StyleSheet.create({
  screen: { flex: 1, backgroundColor: colors.bg },
  title: { paddingHorizontal: space.xl, marginBottom: space.md },
  list: { paddingHorizontal: space.xl, paddingBottom: space.xxxl, gap: space.md },
  headerRow: { flexDirection: 'row', alignItems: 'center', gap: space.md },
  pcIcon: { width: 48, height: 48, borderRadius: radius.md, backgroundColor: colors.cyanSoft, alignItems: 'center', justifyContent: 'center' },
  chips: { flexDirection: 'row', flexWrap: 'wrap', gap: space.sm },
});
