# Validação v0.7.0

## Base e correções

Na auditoria inicial, a execução pelo Python 3.14 contabilizou 63 testes e oito erros: import ausente no patch v0.6.4 e conexões SQLite abertas. A pasta também misturava identificação v0.6.3 e arquivos v0.6.4. Esses problemas foram corrigidos e receberam regressões.

O bloqueio inicial da `.venv` foi posteriormente identificado como restrição do ambiente de execução, não instalação inválida. A `.venv` usa Python 3.12.10 e os imports das nove dependências principais passaram.

## Evidência automática

O relatório `validation-results.json` registra 173 testes aprovados, zero falhas, zero erros e zero testes pulados em Python 3.12.10 / google-genai 2.30.0. A execução adicional em Python 3.14.5 / google-genai 2.8.0 está em `validation-python314.json`. Os testes incluem:

- schemas, autorização, negação e comandos citados;
- geração por function calling simulado com arquivos reais;
- construção de objetos com SDK Gemini real, incluindo o ID de FunctionResponse;
- resultado gravado antes de serialização, erro de API e proibição de replay;
- SQLite, migração, backup, rollback, concorrência, reinício e conexão fechada;
- lembretes/fuso, claim/ack, expiração e nova entrega após interrupção;
- caminhos, links, hash, conflito durante aprovação, patch e backups;
- subprocessos reais com testes, timeout, cancelamento e ambiente filtrado;
- propostas multiarquivo, alteração concorrente, conteúdo adulterado e rollback;
- janela Tk real oculta, fila, memória pela UI, encerramento e áudio obsoleto;
- reprodução cancelável com driver simulado, sem teste acústico;
- leitura web com transporte simulado, DNS/redirects/endereço privado e limites;
- protocolo Link simulado com fragmentação, reconexão, cancelamento e replay.

`node --check ui_tars_bridge/runner.mjs` valida sintaxe, sem executar cliques.

## Jornada de engenharia demonstrada

`EXECUTAR.bat -m marvin.demo` cria uma saudação Python e um teste com erro conhecido, executa o teste (exit 1), aplica patch com hash/backup e executa novamente (exit 0). O contexto persiste em um banco separado. Arquivos e subprocessos são reais; a sequência é programada e não usa Gemini. O primeiro ensaio da demonstração descobriu zero testes por faltar `tests/__init__.py`; a estrutura foi corrigida e a jornada passou.

## Serviço e hardware

Leitura local confirmou i5-11500, 15,7 GiB RAM utilizável e RTX 3060 com 12.288 MiB de VRAM. Não houve seleção/download de modelo novo. Hardware informado no documento mestre era uma hipótese anterior.

Não foram executados nesta entrega: chamadas remotas de Gemini usando a chave pessoal, tarefa real de UI-TARS, ativação por microfone, síntese/audibilidade física, instalação limpa, teste prolongado de horas ou Bluetooth físico. Mocks e simuladores não comprovam esses itens.

## Roteiro manual

1. Abra C MARVIN.bat e use um pedido por texto; confirme estado e etapas em TAREFAS.
2. Salve uma lembrança, reinicie e consulte; edite/exclua pelo painel e confirme a recuperação.
3. Crie lembrete para daqui a um minuto e mantenha o PC acordado; confira entrega e ausência de repetição após ack.
4. Teste áudio primeiro por botão. Selecione microfone/saída, confirme audibilidade e depois diga Marvin. Registre ambiente silencioso/ruído.
5. Use Esc durante a fala; confirme interrupção e ausência de reprodução antiga. Não confundir com interrupção por voz full duplex.
6. TESTAR GOOGLE: confira modelo/cota e mensagem real. Crie projeto simples, verifique os arquivos e abra o resultado.
7. Altere um arquivo entre leitura e aprovação; confirme conflito e preservação da versão externa.
8. Autorize teste de projeto conhecido, cancele e confira processo/resultado. Código executado usa sua conta.
9. Para UI-TARS, inicie o servidor local e faça tarefa não sensível; confira resultado, timeout e cancelamento.
10. Para cada capacidade futura de rádio, use o plano separado de marvin-link.md; não use resultado simulado como medição física.

Não há números de melhoria percentual ou promessa de latência acústica nesta entrega.
