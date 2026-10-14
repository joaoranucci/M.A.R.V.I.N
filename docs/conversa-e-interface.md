# Conversa, pesquisa e interface — 13/10/2026

## Uso

- Abra C MARVIN.bat. O painel mostra uma esfera 3D projetada, animada a 20 FPS,
  com estados de atividade. A animação não exige GPU nem navegador.
- Deixe **Ativar com Marvin** e **Interromper ao falar** ligados. Durante a
  reprodução, fale seu novo pedido; não é necessário repetir a palavra Marvin.
- O detector WebRTC exige aproximadamente 180 ms de fala sustentada acima do
  limiar. Há até 400 ms de áudio anterior para preservar o início do comando.
- O cancelamento da voz não cancela a tarefa já concluída. Um novo pedido fica
  na fila se a tarefa anterior ainda estiver finalizando.
- Fones são recomendados. Não foi implementado cancelamento acústico de eco:
  a voz reproduzida pelas caixas pode ser captada como fala. Ajuste o limiar
  no painel; um valor maior reduz falsas interrupções, mas exige voz mais alta.
- Privacidade interrompe a captura. Esc continua cancelando áudio e tarefa.

## Voz

Antônio Neural é a seleção principal configurada nesta instalação. A prévia
foi sintetizada em `data/voice-preview.mp3`, com 35.568 bytes. Edge TTS 7.2.8
retornou HTTP 403; a atualização para 7.3.1 resolveu a síntese no teste real.
Piper Faber permanece como alternativa offline, com parâmetros de ritmo e
variação ajustados. A agradabilidade e a audibilidade dependem da avaliação
do usuário; o teste não mediu a resposta acústica do microfone.

## Raciocínio

Rápido usa pensamento minimal; profundo usa high. Equilibrado usa minimal
para perguntas simples e medium para explicações, comparações e problemas.
Conversas simples dispensam a declaração de todas as ferramentas locais.
Pedidos sobre ações/projetos continuam com ferramentas, autorizações e ledger.
O contexto inclui lembranças relevantes. Não houve benchmark de latência nem
troca para outro provedor de LLM; estes modos usam Gemini.

## Pesquisa

`Pesquise por ...` retorna resposta com fontes dentro do aplicativo.
`Abra o Google e pesquise por ...` continua abrindo o navegador.

- Google: grounding Gemini com a chave já configurada. Sem fontes retornadas,
  o MARVIN informa que não conseguiu confirmar a pesquisa.
- Brave: `BRAVE_SEARCH_API_KEY` no .env. Resultados limitados e cache de 120 s.
- SearXNG: `SEARXNG_URL` para uma instância que aceite `/search?format=json`.
  Não foi instalado nem escolhido um servidor público automaticamente.

Google e Brave têm cotas/custos; uma instância SearXNG também depende da
disponibilidade e limites dos mecanismos consultados. Não há promessa de
consultas gratuitas ilimitadas. O teste real do Google retornou **HTTP 429**;
o código da integração foi validado com respostas simuladas, mas a consulta
real está bloqueada pela cota do projeto. Nenhuma cobrança foi habilitada.
Brave e SearXNG não foram testados contra contas/instâncias reais.

## Validação

- 178 testes executados: OK, 2 pulados por permissões de links simbólicos.
- Testes novos exercitam fala sustentada versus ruído curto, cancelamento
  separado da tarefa, captura após interrupção sem palavra de ativação,
  cache Brave, filtragem de URLs e exigência de fontes Google.
- `pip check`: nenhuma dependência quebrada.
- A aplicação foi reiniciada sem tarefa em execução, com logs em
  `data/logs/startup-v071-final.*.log`.
- A inspeção da interface por captura de janela não foi concluída: o helper
  retornou timeout de aprovação e depois `FrameArrived timed out`.
  Os testes reais de Tkinter passaram; isso não substitui inspeção visual.
- A interrupção acústica real requer teste com o microfone/saída do usuário.

Referências dos provedores:

- https://ai.google.dev/gemini-api/docs/google-search
- https://ai.google.dev/gemini-api/docs/thinking
- https://brave.com/search/api/
