MARVIN PATCH v0.6.4 — CORREÇÃO GEMINI 503 / MICROFONE -9999

1. Feche o MARVIN.
2. Extraia todo o patch na mesma pasta onde estão INICIAR.bat e C MARVIN.bat.
3. Substitua os arquivos existentes. Preserve .env, data e seus projetos.
4. Execute DIAGNOSTICO_MICROFONE.bat.
5. Se o microfone falhar, abra LISTAR_MICROFONES.bat e no .env escolha
   um dispositivo WASAPI válido via MARVIN_MIC_DEVICE=NUMERO.
6. No .env, use MARVIN_MIC_RATE=auto (opcional).
7. Execute C MARVIN.bat e tente dizer apenas Marvin.
8. Teste novamente a criação do Celular Virtual por texto.

GEMINI
- Em HTTP 503 antes de executar ações, alterna entre os modelos grátis configurados.
- O SDK oficial do Google já tem tentativas automáticas em alguns erros; o
  patch não cria loop infinito de requisições.
- Se os modelos falharem com 503, o pedido 'crie um celular virtual' poderá
  gerar um protótipo offline pré-programado, com index.html, style.css e app.js.
- Se uma ação já foi executada e a API cai, MARVIN não a repete automaticamente.
- HTTP 503 não indica chave inválida; HTTP 429 significa cotas/limites.

TESTES
Os testes automatizados não confirmam áudio nem API reais no seu Windows.
A chamada Gemini pode continuar a falhar caso o serviço siga indisponível.
