# v0.7.0 — 13/10/2026

- Pedidos passam pelo coordenador independente da interface; texto e voz usam o mesmo fluxo.
- Tarefas, etapas, estados e resultados sobrevivem a reinício. Efeitos incertos exigem revisão, sem replay automático.
- Corrigido fechamento de conexões SQLite que deixava arquivos presos no Windows.
- Corrigidos fallback temporário do Gemini e serialização de respostas de função com ID em SDKs distintos.
- Adicionadas validação de argumentos e classificação de efeitos das ferramentas. Negação e texto citado têm regressões cobertas por testes.
- Escrita de projetos passou a usar publicação atômica, hash, detecção de alteração concorrente e backup protegido.
- Adicionados busca/listagem de projetos, patch textual, verificação estática e execução aprovada de checks Python/npm.
- Memórias podem ser editadas/excluídas/exportadas; notas e lembretes básicos funcionam localmente.
- Interface ganhou fila, estado de tarefas, pausa, cancelar/Esc, painéis de diagnóstico e seleção de áudio.
- Reprodução pode ser interrompida; transcrições obsoletas não viram comandos novos.
- Propostas do próprio código podem coordenar até vinte arquivos existentes com hashes, backup e rollback de falha parcial.
- Leitor de páginas públicas explícitas limita dados/tempo e revalida redirecionamentos.
- Ponte visual recebeu timeout, cancelamento antes de iniciar e ambiente filtrado.
- Adicionados simulador Link, scripts de testes/diagnóstico, versões de dependências validadas e recuperação de código.

Não foram habilitados faturamento, captura contínua de tela, envio autônomo de mensagens ou acesso indiscriminado a pastas externas. O núcleo continua usando o workspace escolhido pelo usuário.
