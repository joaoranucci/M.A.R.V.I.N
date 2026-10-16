export interface GatewayUpload {
  file: { uri: string; name: string; mimeType: string };
  fields: { client_id: string; category: string };
}

export interface TransportRequest {
  url: string;
  pin: string;
  method: 'GET' | 'POST' | 'PUT' | 'DELETE';
  headers: Record<string, string>;
  body?: string;
  upload?: GatewayUpload;
  binary?: boolean;
  timeoutMs: number;
  signal?: AbortSignal;
}

export interface TransportResponse {
  status: number;
  ok: boolean;
  text(): Promise<string>;
  arrayBuffer(): Promise<ArrayBuffer>;
}
