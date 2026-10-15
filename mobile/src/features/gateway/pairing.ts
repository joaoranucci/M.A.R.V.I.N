import * as Application from 'expo-application';
import * as Device from 'expo-device';
import { MarvinNative } from '../../../modules/marvin-native';
import { resetEventCursor } from '../../core/events/eventStream';
import { log } from '../../core/logging/logger';
import { refreshCapabilities, refreshConnectivity } from '../../core/net/connectivity';
import { connectionInfo, useConnectionInfo } from '../../core/security/credentials';
import { syncNow } from '../../core/sync/syncEngine';
import type { PairingPayload } from '../assistant/nlp/pairing';
import { gateway } from './api';
import { GatewayError } from './client';

export function deviceName(): string {
  return `MARVIN Mobile · ${Device.modelName ?? 'Android'}`.slice(0, 80);
}

/**
 * Pins the certificate received out-of-band, checks the server identity and exchanges
 * the one-time code for a device token stored in the secure store.
 */
export async function pairWith(payload: PairingPayload): Promise<void> {
  const previous = connectionInfo().connection;
  const base = { host: payload.host, port: payload.port };
  MarvinNative.setPinnedKeys(previous ? [previous.pin, payload.pin] : [payload.pin]);
  try {
    const health = await gateway.health(base);
    if (payload.serverId && health.server_id !== payload.serverId) {
      throw new GatewayError('http', 'O servidor nesse endereço não é o computador do QR Code.');
    }
    const result = await gateway.pair(base, payload.code, deviceName(), Application.nativeApplicationVersion ?? '0.1.0');
    await useConnectionInfo.getState().save(
      {
        host: payload.host,
        port: payload.port,
        pin: payload.pin,
        serverId: result.server.server_id,
        serverName: result.server.name,
        deviceId: result.device_id,
        pairedAt: new Date().toISOString(),
      },
      result.token,
    );
    log.info('pairing', `vinculado a ${result.server.name}`);
    resetEventCursor();
    await refreshConnectivity();
    await refreshCapabilities();
    void syncNow('pareamento');
  } catch (error) {
    MarvinNative.setPinnedKeys(previous ? [previous.pin] : []);
    if (error instanceof GatewayError && error.kind === 'network') {
      throw new GatewayError('network', 'Não alcancei o PC. Confira o endereço, se estão na mesma rede/VPN e se o firewall do Windows permite a porta.');
    }
    if (error instanceof GatewayError && error.status === 401) throw new GatewayError('http', 'Código inválido ou expirado. Gere outro no PC.', 401);
    if (error instanceof GatewayError && error.status === 429) throw new GatewayError('http', error.message, 429);
    throw error;
  }
}

/** Ends this phone's session: revoked on the PC when reachable, credentials always removed here. */
export async function signOut(): Promise<{ revokedRemotely: boolean }> {
  let revokedRemotely = false;
  try {
    await gateway.revokeDevice('self');
    revokedRemotely = true;
  } catch (error) {
    log.warn('pairing', `revogação remota falhou: ${error instanceof Error ? error.message : String(error)}`);
  }
  await useConnectionInfo.getState().clear();
  resetEventCursor();
  await refreshConnectivity();
  return { revokedRemotely };
}
