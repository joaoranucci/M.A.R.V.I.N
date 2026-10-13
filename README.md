# MARVIN v0.7.0

Assistente pessoal para Windows com voz opcional, conversa Gemini, projetos locais e registro persistente de tarefas. Esta versão implementa uma etapa funcional da evolução JARVIS; visão autônoma completa, conversa simultânea à própria voz e hardware vestível ainda não estão validados.

## Iniciar

Abra **C MARVIN.bat** ou **INICIAR.bat**. A instalação existente não precisa ser refeita se abrir normalmente. O launcher usa a `.venv` válida e tenta o Python do sistema se ela estiver indisponível. Sem bibliotecas opcionais, texto, memória e comandos locais continuam acessíveis quando o Python/Tkinter está disponível.

Para uma instalação nova, use Python 3.12 x64 e **INSTALAR.bat**. Para instalar apenas texto e Gemini: `INSTALAR.bat --core-only`. O instalador preserva `.env`, `data`, modelos e projetos; um ambiente inválido é renomeado antes de criar outro. Instalação limpa e downloads não foram repetidos nesta entrega.

**DIAGNOSTICO.bat** informa versões, hardware e capacidades sem capturar áudio nem chamar APIs. **TESTAR.bat** executa os testes automatizados. O botão **TESTAR GOOGLE** faz uma listagem e geração curta usando a cota do projeto configurado.

## O que mudou

- Cada pedido registra tarefa e etapas em SQLite. A intenção é gravada antes da ação e o resultado antes de retornar ao modelo.
- Cancelamento, pausa entre etapas, fila limitada, histórico de tarefas e preservação de resultados após erro.
- Referências ao projeto ativo, memória local consultável/editável e lembretes persistentes.
- Arquivos escritos atomicamente, hashes para detectar conflitos, backups e verificação estática.
- Testes Python e scripts npm conhecidos podem ser executados após aprovação do comando concreto, com ambiente filtrado, limite de saída, timeout e cancelamento.
- Compatibilidade da resposta de função Gemini em SDKs diferentes sem repetir a ação.
- Propostas de alteração do MARVIN com vários arquivos, diff, backup e recuperação.
- Leitura de URLs públicas explícitas com URL/data de consulta. Pesquisa por assunto ainda abre o navegador; não equivale a leitura de fontes.
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

A palavra de ativação continua sendo **Marvin**. **ÁUDIO** permite selecionar dispositivos; nomes resistem melhor a renumeração que índices. **Ctrl+Espaço** inicia captura manual. Piper é a voz local principal; Edge TTS é uma alternativa online. Os modelos de voz podem precisar do primeiro download.

O reconhecimento fica pausado durante TTS; esta versão não promete full duplex nem interrupção por voz enquanto fala. Use Esc. Continuidade opcional após a resposta: `MARVIN_CONTINUITY_SECONDS=0..30` (padrão 0). **Privacidade** desativa captura e tarefas visuais; lembretes continuam no painel.

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
