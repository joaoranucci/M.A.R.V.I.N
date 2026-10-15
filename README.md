# MARVIN v0.8.0 — Presença

Assistente pessoal para Windows com voz opcional, conversa Gemini, projetos locais e registro persistente de tarefas. Esta versão implementa uma etapa funcional da evolução JARVIS. A interrupção de fala usa detecção local; visão autônoma completa e hardware vestível continuam fora desta entrega.

## AIML API

O MARVIN aceita `MARVIN_LLM_PROVIDER=aiml`, `AIML_API_KEY` e
`AIML_MODEL=openai/gpt-5-5` no `.env`. A integração usa
`https://api.aimlapi.com/v1/chat/completions` para conversa e chamadas de
ferramentas, preservando confirmações e registro das ações. A chave não deve
incluir os delimitadores `<` e `>`. Não há troca automática para outro provedor.

Reabra o programa após atualizar o código. Alterações posteriores no `.env`
podem ser aplicadas por **RECARREGAR IA** no modo clássico. Na interface Presença, reabra o programa. Use **TESTAR IA** ou
**DIAGNOSTICO_IA.bat** para uma geração curta que usa o saldo/cota do provedor.
`DIAGNOSTICO_GOOGLE.bat` permanece como atalho legado e também testa o provedor
selecionado. Para voltar ao Gemini, configure `MARVIN_LLM_PROVIDER=gemini`.

Pesquisa Google grounding permanece exclusiva do Gemini. Com AIML, selecione
Brave ou SearXNG e configure as credenciais/URL correspondentes. Conversa e
ferramentas locais não dependem de um provedor de pesquisa.

Validação em 14/10/2026: o teste remoto AIML com o modelo solicitado respondeu
HTTP 403 (acesso negado). Isso não confirma validade da chave nem acesso ao
modelo; é necessário conferir permissões da chave/conta no painel AIML.
Contrato usado: [documentação AIML de ferramentas](https://docs.aimlapi.com/capabilities/function-calling).



## Interface Presença

Execute **INICIAR_PRESENCA.bat**. Os atalhos habituais também usam a nova interface quando compilada; `EXECUTAR.bat main.py --legacy` abre a interface clássica.

Para instalar em outro computador: Python 3.12 x64, Node.js 22.12+ e Microsoft Edge WebView2 Runtime; execute **INSTALAR_INTERFACE.bat** após configurar o núcleo. React + Three.js renderizam o núcleo 3D, FastAPI conecta memória, projetos, tarefas e áudio por WebSocket. A janela nativa usa pywebview/WebView2. Tauri não foi compilado: esta máquina não tem Rust/Cargo nem as ferramentas C++ necessárias.

- Voz como entrada principal. Diga “Marvin, abrir teclado” ou use **Ctrl+Espaço** para digitar; o campo se recolhe ao enviar um pedido.
- **MARVIN Focus**: “vamos trabalhar no projeto dos óculos” abre um projeto existente. Arquivos, documentação, tarefas e contexto são reais. O visualizador de código é de leitura; alterações e verificações passam pelo núcleo e suas autorizações.
- **Ctrl+Shift+M** ou “Marvin, modo compacto” recolhe para uma janela pequena sempre no topo. “Marvin, expandir” restaura a janela. Os atalhos precisam da janela em foco; a palavra de ativação funciona em segundo plano.
- A esfera reage ao nível de entrada e à amplitude do áudio reproduzido; partículas indicam pensamento, fontes aparecem como conexões e autorizações mudam o núcleo para âmbar.
- Agenda e memória são locais. Não há sincronização com calendário externo. Painéis vazios aguardam seus dados; não mostram compromissos ou progresso fictícios.
- O servidor escuta apenas em 127.0.0.1, com sessão aleatória e validação de origem. Não publique essa porta na rede.
- Consultas Google/Gemini e Brave dependem de chave e cota; SearXNG depende de uma instância configurada. Nenhum provedor é apresentado como ilimitado.

Desenvolvimento: `cd desktop`, `npm ci`, `npm run build`; depois `python -m marvin.desktop`. `--browser` abre no navegador; `--no-audio` permite testar sem microfone. O build fica em `desktop/dist` e não é versionado.

## Iniciar (núcleo e modo clássico)

Abra **C MARVIN.bat** ou **INICIAR.bat**. A instalação existente não precisa ser refeita se abrir normalmente. O launcher usa a `.venv` válida e tenta o Python do sistema se ela estiver indisponível. Sem bibliotecas opcionais, texto, memória e comandos locais continuam acessíveis quando o Python/Tkinter está disponível.

Para uma instalação nova, use Python 3.12 x64 e **INSTALAR.bat**. Para instalar apenas texto e Gemini: `INSTALAR.bat --core-only`. O instalador preserva `.env`, `data`, modelos e projetos; um ambiente inválido é renomeado antes de criar outro. Instalação limpa e downloads não foram repetidos nesta entrega.

**DIAGNOSTICO.bat** informa versões, hardware e capacidades sem capturar áudio nem chamar APIs. **TESTAR.bat** executa os testes automatizados. O botão **TESTAR GOOGLE** faz uma listagem e geração curta usando a cota do projeto configurado.

Se editar a chave no `.env` com o programa aberto, clique em **RECARREGAR IA** e depois **TESTAR GOOGLE**. A recarga só é permitida sem tarefa em andamento, substitui a conexão Gemini e mantém memória, diretórios e controles de áudio. Arquivos UTF-8 com BOM e chaves entre aspas são aceitos. Uma chave ausente ou de exemplo não substitui a configuração em uso.

O diagnóstico local agora mostra a existência do `.env`, o ambiente Python ativo e próximos passos, sem mostrar a chave. Uma resposta vazia do Gemini não é registrada como conversa bem-sucedida; outro candidato configurado é tentado.

## O que mudou

- Cada pedido registra tarefa e etapas em SQLite. A intenção é gravada antes da ação e o resultado antes de retornar ao modelo.
- Cancelamento, pausa entre etapas, fila limitada, histórico de tarefas e preservação de resultados após erro.
- Referências ao projeto ativo, memória local consultável/editável e lembretes persistentes.
- Arquivos escritos atomicamente, hashes para detectar conflitos, backups e verificação estática.
- Testes Python e scripts npm conhecidos podem ser executados após aprovação do comando concreto, com ambiente filtrado, limite de saída, timeout e cancelamento.
- Compatibilidade da resposta de função Gemini em SDKs diferentes sem repetir a ação.
- Propostas de alteração do MARVIN com vários arquivos, diff, backup e recuperação.
- Leitura de URLs públicas explícitas com URL/data de consulta. Pesquisa por assunto usa Google/Gemini, Brave ou SearXNG, conforme configuração e disponibilidade.
- Simulador local MARVIN Link com fragmentação, reconexão e proteção contra repetição de comandos.

## Experimente

- `Marvin, lembre que eu prefiro projetos em Python.`
- `O que você lembra de mim?`
- `Me lembre daqui a 10 minutos de beber água.`
- `Me lembre amanhã às 09:30 de revisar o projeto.`
- `Crie um projeto chamado loja, escreva uma página index.html e verifique os arquivos.`
- `Agora verifique esse projeto.`
- `Abra o último projeto.`
- `Leia https://docs.python.org/3/library/sqlite3.html e explique o fechamento das conexões.`

Criação geral em linguagem natural exige Gemini configurado e disponível. Sem API, o exemplo específico `crie um celular virtual` pode gerar um template identificado como tal. Comandos básicos e memória não dependem de LLM.

Durante o trabalho, digite `status`, `espere`, `continue` ou `cancele`. **Esc/CANCELAR** também interrompe a saída de voz e solicita parar subprocessos. A pausa aguarda um checkpoint; uma chamada de API em andamento pode terminar antes de ceder. A fila aceita até oito pedidos, além do atual.

## Voz e privacidade

A palavra de ativação continua sendo **Marvin**. **ÁUDIO** permite selecionar dispositivos; nomes resistem melhor a renumeração que índices. **Ctrl+Espaço** inicia captura manual no modo clássico e abre o teclado na interface Presença. Antônio (Edge TTS) é a voz padrão online; Piper Faber é a alternativa local. Os modelos de voz podem precisar do primeiro download.

Com **Ativar com Marvin** e **Interromper ao falar** ligados, o microfone permanece ativo durante a reprodução. Um detector WebRTC com limiar de volume corta a fala após cerca de 180 ms de voz sustentada e preserva até 400 ms do início do comando. O novo comando não precisa começar por Marvin. Não há cancelamento acústico de eco: prefira fones; com caixas de som, ajuste o limiar no painel. Esc continua disponível. Continuidade opcional após a resposta: `MARVIN_CONTINUITY_SECONDS=0..30` (padrão 0). **Privacidade** desativa captura e tarefas visuais; lembretes continuam no painel.

A voz principal agora é Antônio Neural (online), com Piper Faber local como alternativa. O painel inclui uma esfera 3D projetada e animada e estados de atividade. **Raciocínio** seleciona os níveis minimal, medium ou high do Gemini. Conversas simples usam um caminho sem declarações de ferramentas; pedidos de ações mantêm autorização e registro de etapas.

`Pesquise ...` consulta fontes dentro do MARVIN. `Abra o Google e pesquise ...` continua abrindo o navegador. O provedor Google usa grounding Gemini e depende da cota do projeto. Brave exige `BRAVE_SEARCH_API_KEY`; SearXNG exige `SEARXNG_URL` com JSON habilitado. Nenhum provedor é prometido como gratuito ou ilimitado. As fontes aparecem como links clicáveis; ausência de fontes não é apresentada como pesquisa confirmada.

## Dados e limites

`.env` foi preservado. Conversas e fatos antigos mantêm suas tabelas. Migrações adicionam tabelas e fazem backup em `data/backups`. Projetos continuam no workspace configurado, por padrão `%USERPROFILE%\MARVIN_Projetos`. Preferências da interface ficam em `data/preferences.json`.

O registro de tarefas contém objetivos, argumentos e resultados. Os logs operacionais separados contêm somente metadados. Excluir uma lembrança do banco ativo não exclui backups antigos ou registros de tarefas; revise-os antes de compartilhar a pasta `data`.

Abrir app/arquivo gera uma solicitação ao Windows; quando a janela não foi observada, a tarefa indica **needs_reconciliation**. Não é sucesso visual comprovado. Lembretes requerem aplicativo aberto e PC acordado. Sem `tzdata`, o diagnóstico informa o fallback UTC−03; use dados IANA para regras históricas/futuras.

A execução aprovada de testes **não é uma sandbox do sistema operacional**: o código do projeto roda com a sua conta. Não há ferramenta genérica de shell, instalação autônoma ou elevação de privilégios. O programa não habilita faturamento. Elegibilidade de modelo gratuito não comprova configuração de cobrança/cota da conta Google.

## Evidências e recuperação

- [Validação executada e roteiro manual](docs/validation.md)
- [Capacidades reais e pendências](docs/capabilities.md)
- [Arquitetura e decisões](docs/architecture.md)
- [Diagnóstico e recuperação](docs/diagnostics.md)
- [MARVIN Link: simulador e limites físicos](docs/marvin-link.md)
- [Mudanças observáveis](CHANGELOG.md)

Demonstração com arquivos e testes reais: `EXECUTAR.bat -m marvin.demo`. Ela cria um projeto separado em `data/engineering_demo`, reproduz um erro e corrige. A sequência é programada e identificada como demonstração, sem LLM ou controle de desktop. Simulador de rádio **sem rádio real**: **SIMULAR_LINK.bat**.

A versão anterior do código está em `data/upgrade_backups/pre_v070`. Para recuperação, feche o MARVIN e consulte o procedimento em `docs/diagnostics.md`. Não substitua seu banco atual por um backup antigo sem considerar as informações gravadas depois dele.

### Teste visual da Presença

Inicie `python -m marvin.desktop --no-open --no-audio --data-dir data/presence-test --workspace data/presence-test/projects`; em outro terminal, execute `cd desktop` e `node smoke.mjs` (requer Edge instalado). O teste cria somente o projeto `interface-validada` nessa pasta isolada e salva capturas em `data`. Os testes de API ficam em `tests/test_presence_v080.py`.

### Desligar o computador

Diga **“Marvin, desligue meu computador”** (também aceita “desliga o PC” ou “desligar meu notebook”). Esse pedido explícito envia diretamente `shutdown.exe /s /t 0`, sem confirmação adicional do MARVIN, sem depender da IA e sem `/f`. O Windows pode impedir o encerramento se algum aplicativo tiver trabalho não salvo. Não há contagem regressiva. Menções, explicações e negações não acionam esse comando. Os testes simulam o processo; não desligam a máquina.
