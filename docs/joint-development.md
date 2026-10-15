# Desenvolvimento MARVIN — 14/10/2026

Objetivo do usuário: evoluir o assistente pessoal Windows inspirado no JARVIS,
com trabalho conjunto entre Codex e Claude. O MARVIN é uma aplicação que usa
modelos; esta entrega não treina um novo modelo nem comprova superioridade sobre outras LLMs.

## Estado observado e alterações desta rodada

- `.env` e `.venv` existentes; Python 3.12.10 funcional.
- Bibliotecas Gemini, Vosk, sounddevice, Piper, pygame e Edge TTS instaladas.
- Suíte anterior: 178 testes aprovados.
- Recarga explícita da configuração Gemini pela interface, sem trocar banco ou áudio.
- Leitura de `.env` com BOM e aspas; rejeição de chave ausente/de exemplo na recarga.
- Diagnóstico com estado de configuração e orientações, sem valores secretos.
- Respostas vazias não contam como sucesso nem são gravadas como conversa.
- Diagnóstico Google usa o diretório de dados configurado e fecha o cliente.
- Suíte após mudanças: 187 testes aprovados, incluindo testes reais do loop Tk com janela oculta.
- Chamada remota curta: listagem e geração de texto com gemini-3.5-flash-lite bem-sucedidas.

Essas evidências não validam audibilidade, reconhecimento no microfone físico,
ações visuais reais ou projetos completos gerados por linguagem natural.
Uma instância já aberta precisa ser reiniciada para carregar o código novo.

## Coordenação com Claude

A conversa “Conhecer o MARVIN” foi localizada por acessibilidade. Duas tentativas
de focar seu campo de entrada falharam com `coordinate input geometry is unavailable`.
Nenhuma mensagem foi enviada e nenhuma revisão do Claude foi recebida nesta rodada.
Este arquivo registra o ponto de integração para evitar trabalho duplicado.

Proposta de divisão: Codex mantém implementação e regressões; Claude revisa
arquitetura, cenários de uso e lacunas. Antes de editar simultaneamente, combinar
arquivos de responsabilidade. Não compartilhar `.env`, banco pessoal ou logs de conversas.

## Próximas entregas e critérios de aceitação

1. Voz física: confirmar ativação, fala audível, interrupção e cancelamento por Esc
   com fones; registrar latência e falhas reais, sem inferir sucesso de imports.
2. Agente de engenharia: validar uma tarefa pequena com criação, execução aprovada,
   falha, correção e resultado verificável. Manter registro por etapa e não repetir efeitos incertos.
3. Percepção visual: observar a janela após ações e distinguir solicitado, observado
   e concluído. Exigir confirmação para ações de risco; medir cenários reais do desktop.
4. Rotinas recorrentes: persistência, fuso horário, prevenção de duplicatas,
   desativação pelo usuário e testes de reinício antes de ativar proatividade.
5. Documentos e integrações: definir formatos e contas concretas, implementar
   leitura e referências antes de ações externas de escrita.
6. Avaliação de qualidade: conjunto de tarefas com taxa de conclusão, custo,
   latência e regressões; escolher modelos por evidência observada.

Vestíveis, rádio e autonomia geral continuam fora de uma entrega comprovada.
