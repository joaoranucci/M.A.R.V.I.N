# Matriz de capacidades

| Capacidade | Estado nesta entrega | Evidência / limite |
| --- | --- | --- |
| Inicialização e texto Tkinter | Testado automaticamente | Janela criada/encerrada e fila exercitada com dados temporários |
| Memória e contexto persistentes | Implementado e testado | Migração, recuperação, edição/exclusão e conexão fechada |
| Comandos básicos sem API | Implementado | Roteador preservado; ações físicas dependem do Windows |
| Lembretes de ocorrência única | Implementado e testado | Relativos, amanhã com hora, ISO; lease/ack e recuperação |
| Rotinas recorrentes, calendários externos | Pendente | Sem scheduler de rotinas gerais/integração de contas |
| Gemini e function calling | Adaptador testado | SDKs reais, respostas simuladas; conta/API remota não validada nesta entrega |
| Tarefas, etapas e cancelamento | Implementado e testado | Sem replay cego; pausa em checkpoints |
| Continuação automática após reinício | Parcial | Revisão assistida de etapas; não retoma efeitos incertos |
| Contexto “último projeto” | Implementado e testado | Entidades persistidas; resolução livre continua limitada |
| Criação/patch/hash/backup | Implementado e testado | Workspace configurado; não acesso geral ao computador |
| Python unittest / npm test/build | Implementado | Processo aprovado; timeout, saída limitada e env filtrado |
| Projetos completos via pedidos naturais | Depende de Gemini | Demonstração programada não prova raciocínio do serviço |
| Autoprogramação multiarquivo | Implementado e testado | Sintaxe e transação; execução dos testes da proposta ainda manual |
| Microfone/Vosk/Piper/Edge | Integrados | Imports validados; audibilidade/ativação física pendentes |
| Interrupção de reprodução por botão | Implementado e teste do adaptador | Latência acústica real não medida |
| Full duplex / interrupção acústica | Implementado com testes simulados | Detecção durante TTS; sem cancelamento de eco; validação acústica física pendente |
| Pesquisa por assunto | Implementado; validação remota pendente | Gemini grounding, Brave ou SearXNG; comandos explícitos de navegador continuam abrindo Google |
| Ler URL pública explícita | Implementado e testado com transporte simulado | Sem sessão de conta, JS, PDF ou scraping universal |
| UI-TARS local | Opcional | SDK/runtime/pesos existentes; tarefa visual real não validada |
| OCR / percepção geral de documentos | Pendente | Sem novo pipeline OCR/documentos nesta entrega |
| MARVIN Link | Simulado e testado | Sem rádio, criptografia de transporte ou hardware físico |
| Instalação e recuperação | Scripts entregues e recuperação testada | Instalação nova/clean room pendente |
| Hardware real detectado | Validado por leitura local | i5-11500, 15,7 GiB RAM utilizável, RTX 3060 12 GiB |

## Relação com as prioridades do documento mestre

P0 e fundamentos de P1 foram implementados; P2 recebeu memória, lembretes e controles de áudio. P3 recebeu leitura de URL explícita e limites adicionais na ponte visual. P4 recebeu um simulador de protocolo. P5 recebeu versões fixadas, diagnósticos e recuperação. Isso não representa conclusão integral de todas as metas P0–P5.

Próximas entregas: validar voz real e Gemini na conta; retomar etapas seguras com plano persistente; confirmação por observação de janelas; pesquisa com fontes por assunto; rotinas habilitáveis; gateway autenticado e testes físicos do vestível.

Atualização de 14/10/2026: geração curta real Gemini validada; 187 testes aprovados.
Recarga de configuração e tratamento de respostas vazias adicionados. Detalhes e
pendências atuais em [Desenvolvimento conjunto](joint-development.md).
