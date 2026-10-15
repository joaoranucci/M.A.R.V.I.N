import type { TransportRequest, TransportResponse } from './types';

export async function transport(_request: TransportRequest): Promise<TransportResponse> {
  throw new Error('O gateway seguro exige uma build nativa para Android ou iOS.');
}
