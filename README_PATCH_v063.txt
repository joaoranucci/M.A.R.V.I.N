MARVIN PATCH v0.6.3 — ARQUIVOS, MEMÓRIA E AUTOCÓDIGO COM CONFIRMAÇÃO

1. Feche o MARVIN.
2. Faça uma cópia de segurança dos arquivos .env e data/marvin.db.
3. Extraia TODO o ZIP do patch NA MESMA PASTA onde estão C MARVIN.bat e INICIAR.bat.
4. Aceite a substituição dos arquivos existentes.
5. Não é necessário reinstalar os pacotes Python se a v0.6.2 já funcionava.
6. Execute C MARVIN.bat.
7. Teste via caixa de texto antes do microfone:
   Marvin, crie um projeto chamado celular virtual em HTML com uma tela interativa,
   crie a pasta, escreva index.html e abra o resultado.
8. Clique ABRIR PROJETOS para conferir os arquivos em seu PC.

MEMÓRIA
Use: Marvin, lembre que eu prefiro soluções gratuitas.
Veja as notas salvas pelo botão MEMÓRIA.

ALTERAR O PRÓPRIO MARVIN
Use: Marvin, examine seu módulo de comandos e proponha uma melhoria.
Depois clique REVISAR CÓDIGO para inspecionar as diferenças e aprovar, se desejar.
O backup fica em data/code_backups. O MARVIN nunca aplica a proposta sozinho.

LIMITES
O agente não recebe acesso indiscriminado a pastas do Windows nem execução
arbitrária de terminal. Projetos novos são criados em %USERPROFILE%\MARVIN_Projetos.
O UI-TARS continua disponível em separado para tarefas de mouse/teclado.

TESTADO: 70 testes automatizados + inicialização gráfica em Linux (Xvfb).
NÃO TESTADO: Gemini real, voz e controle de Windows nesta versão.
