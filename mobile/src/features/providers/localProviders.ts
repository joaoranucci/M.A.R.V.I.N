import type { AssistantProvider } from './types';

/** No model: explains what still works without the PC. Never pretends to answer. */
export const localProvider: AssistantProvider = {
  id: 'local',
  label: 'Somente no celular',
  async send() {
    return {
      state: 'offline',
      text:
        'Estou sem conexão com o MARVIN do seu computador, então não consigo conversar livremente agora. ' +
        'Posso guardar memórias, criar tarefas, lembretes e notas aqui mesmo; tudo sincroniza quando o PC voltar.',
    };
  },
};

const DEMO_REPLIES: [RegExp, string][] = [
  [/(oi|ola|bom dia|boa tarde|boa noite)/i, 'Olá, João. Este é o modo demonstração: minhas respostas são simuladas.'],
  [/(tempo|clima|chover)/i, 'No modo demonstração eu não consulto serviços externos. Conecte o PC para respostas reais.'],
];

/** Explicitly labeled simulation for showing the interface without a server. */
export const demoProvider: AssistantProvider = {
  id: 'demo',
  label: 'Demonstração',
  async send(request) {
    await new Promise((resolve, reject) => {
      const timer = setTimeout(resolve, 1200);
      request.signal.addEventListener('abort', () => {
        clearTimeout(timer);
        reject(new Error('Cancelado.'));
      });
    });
    const reply = DEMO_REPLIES.find(([pattern]) => pattern.test(request.text))?.[1]
      ?? `[Demonstração] Recebi: “${request.text}”. Com o computador conectado, o MARVIN responderia de verdade.`;
    return { state: 'completed', text: reply, engine: 'demo' };
  },
};
