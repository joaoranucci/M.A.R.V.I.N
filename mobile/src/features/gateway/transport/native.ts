import { MarvinNative } from '../../../../modules/marvin-native';
import { decodeBase64, requirePin } from './policy';
import type { TransportRequest, TransportResponse } from './types';

let sequence = 0;

/** iOS uses URLSession; Android uses an explicitly pinned OkHttp client, never global fetch. */
export function createNativeTransport(platform: 'ios' | 'android') {
  return async (request: TransportRequest): Promise<TransportResponse> => {
    requirePin(request.pin);
    if (!MarvinNative.hasSecureTransport(platform)) {
      throw new Error('Esta build não inclui o transporte seguro. Instale a nova build de desenvolvimento do MARVIN.');
    }
    const aborted = () => new Error('Requisição cancelada.');
    if (request.signal?.aborted) throw aborted();
    const id = Date.now().toString(36) + '-' + (++sequence);
    let rejectAbort: (error: Error) => void = () => {};
    const cancelled = new Promise<never>((_, reject) => { rejectAbort = reject; });
    const onAbort = () => {
      MarvinNative.cancelRequest(id);
      rejectAbort(aborted());
    };
    request.signal?.addEventListener('abort', onAbort, { once: true });
    try {
      const { signal: _signal, ...options } = request;
      const response = await Promise.race([MarvinNative.gatewayRequest({ ...options, id }), cancelled]);
      return {
        status: response.status,
        ok: response.status >= 200 && response.status < 300,
        text: async () => response.body,
        arrayBuffer: async () => {
          if (!response.binary) throw new Error('Resposta binária inválida.');
          return decodeBase64(response.body);
        },
      };
    } finally {
      request.signal?.removeEventListener('abort', onAbort);
    }
  };
}
