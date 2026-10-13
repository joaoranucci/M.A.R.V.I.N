MARVIN v0.6.2 — CORRECAO DO GEMINI (13/10/2026)

ERRO CORRIGIDO:
  O MARVIN dizia 'Chave do Gemini recusada' para qualquer HTTP 403.
  Agora separa erros 401/403/404/429, tenta o outro modelo Flash-Lite
  quando um deles nao esta permitido e faz um teste real no diagnostico.

ATENCAO: CHAVES GOOGLE
  Segundo documentacao do Google, em setembro de 2026, o Gemini API
  passou a rejeitar chaves antigas do tipo STANDARD. Uma chave escrita
  corretamente no .env ainda pode falhar por ser Standard.
  No https://aistudio.google.com/apikey, crie uma chave do tipo AUTH.
  Escolha um projeto sem faturamento, para manter custo zero.

APLICAR PATCH (SEM PERDER HISTORICO)
  1. Feche o MARVIN.
  2. Abra a pasta onde esta o INICIAR.bat (por exemplo C:\MARVIN_v0.6.1).
  3. Extraia o ZIP de PATCH exatamente nessa pasta, substituindo arquivos.
  4. Confira no arquivo .env:
       GEMINI_API_KEY=sua_chave_auth_do_aistudio
       GEMINI_MODEL=gemini-3.1-flash-lite
     Nao coloque aspas, nem compartilhe o .env ou a chave em prints.
  5. Execute DIAGNOSTICO_GOOGLE.bat e depois INICIAR.bat.
  6. Se o diagnostico acusar 401 ou 403, verifique o tipo da chave no AI Studio.

O PATCH NAO ALTERA .env, data, arquivos UI-TARS ou instalacao local.
O TESTE DE DIAGNOSTICO ENVIA UMA MENSAGEM CURTA PARA O GEMINI.
NAO USE UMA CHAVE DE UM PROJETO COM FATURAMENTO HABILITADO.

O teste automatizado dos codigos Python passou (58 testes).
Ainda precisa validar a chave real no computador do usuario.
