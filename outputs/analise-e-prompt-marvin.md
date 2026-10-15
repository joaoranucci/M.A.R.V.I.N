# MARVIN — análise-base e prompt de implementação

## Limite desta análise

O texto do anexo não chegou a esta conversa e não está acessível no caminho informado. Portanto, esta é uma **análise-base do repositório**, não uma avaliação específica da funcionalidade desejada. O prompt abaixo contém um campo para inserir o requisito original; sem preenchê-lo, não se deve iniciar uma implementação de funcionalidade.

## Diagnóstico do projeto

O MARVIN é um assistente local para Windows, versão documentada como **v0.7.0**, com interface Tkinter, fluxo de tarefas persistido em SQLite, integração Gemini, ferramentas locais autorizadas, memória, lembretes, voz opcional, leitura de URL pública e ponte visual opcional UI-TARS.

### O que já existe — não recriar sem necessidade

- Fluxo de tarefas com etapas persistentes, cancelamento, pausa em checkpoints e registro antes/depois das ações.
- Proteção contra repetição cega de efeitos incertos após interrupção; esses casos passam para reconciliação explícita.
- Ferramentas locais com escopos/autorização, workspace controlado, escrita atômica, hashes, backups e execução de verificações com aprovação.
- Memória local, lembretes únicos, leitura limitada de URLs públicas e simulador do MARVIN Link.
- Testes automatizados para persistência, interface, áudio simulado, workspace, autorização e leitores web.

### Lacunas documentadas que podem ser relevantes

| Prioridade-base | Lacuna | Observação |
|---|---|---|
| P0 — depende do requisito | Definir comportamento esperado, fluxo, limites e critérios de aceitação da funcionalidade solicitada | O texto que permitiria priorizar isto não foi recebido. |
| Alta — validação | Exercitar Gemini, voz, microfone e UI-TARS em uso real | A documentação registra limites de cota/HTTP 429 para pesquisa Google e ausência de validação física completa dessas integrações. Mocks não provam funcionamento real. |
| Alta — confiabilidade | Melhorar retomada assistida de tarefas e reconciliação de efeitos | A retomada é parcial; efeitos incertos não são reproduzidos automaticamente, por segurança. Não há editor persistente de plano/DAG. |
| Média | Confirmar visualmente que a janela ou ação solicitada ocorreu | O aceite do Windows, por si só, não comprova que a janela pretendida foi observada. |
| Média | Pesquisa por assunto com recuperação/resumo confiável de fontes | Há caminho parcial por provedores, mas os resultados reais dependem de credenciais, cota e disponibilidade. |
| Média | Rotinas recorrentes e calendários externos | Lembretes de ocorrência única existem; rotinas gerais e integração externa estão pendentes. |
| Média/baixa — por escopo | OCR/percepção geral de documentos; full duplex e cancelamento de eco; Link físico seguro | São capacidades ausentes ou não validadas; não devem entrar automaticamente no escopo. Link é simulado, não transporte físico validado. |

### Qualidade da evidência e riscos

- A validação automatizada documenta uma suíte ampla, mas os números não são consistentes entre documentos: `docs/validation.md` registra **173** testes e `docs/conversa-e-interface.md` registra **178**. Confirmar a contagem real antes de atualizar relatórios.
- Existem diferenças explícitas entre testes simulados e validação real de serviços/dispositivos; relatar cada uma sem apresentar simulação como prova de produção.
- A execução aprovada de checks roda com a conta do usuário e não é sandbox do sistema operacional.
- O estado local já continha `M .env.example` e um `package-lock.json` não rastreado na raiz. **Preservar ambos**: não reverter, sobrescrever, limpar ou incluir no escopo sem autorização explícita.
- Não ler, imprimir, registrar ou alterar segredos de `.env`.

## Prompt reutilizável

Copie o prompt abaixo para um agente de programação e substitua o campo entre colchetes pelo texto original do requisito.

```text
Você é um engenheiro sênior trabalhando no repositório local do MARVIN, um assistente para Windows (Python, Tkinter, SQLite, Gemini e ferramentas locais autorizadas).

REQUISITO ORIGINAL
[COLE AQUI O TEXTO INTEGRAL DO PEDIDO/ANEXO]

Objetivo: comparar o requisito com o estado real do repositório, identificar o mínimo que falta e implementar somente o necessário, com testes e evidências. Não assuma que uma capacidade está ausente: inspecione código, documentação e testes antes de propor mudanças.

Método
1. Leia README.md, docs/architecture.md, docs/capabilities.md e os documentos diretamente relacionados ao requisito. Inspecione os módulos e testes relevantes; procure instruções locais do projeto.
2. Faça um diagnóstico curto separando: já implementado, parcialmente implementado, ausente, e dependente de credenciais/hardware/serviço externo. Cite arquivos e símbolos concretos.
3. Converta o requisito em critérios de aceitação observáveis. Identifique ambiguidades que alterem materialmente comportamento, permissões ou dados; não invente escolhas nesses casos.
4. Proponha uma sequência mínima de implementação. Preserve a arquitetura, interfaces e compatibilidade existentes. Não reescreva módulos nem amplie o escopo sem necessidade.
5. Implemente o escopo aprovado no próprio pedido, com testes focados de sucesso, erro, cancelamento/retomada e regressão quando aplicável. Execute os checks relevantes e informe exatamente comandos e resultados. Se uma validação depender de serviço ou hardware indisponível, marque-a como não validada — não fabrique sucesso.
6. Atualize documentação somente onde o comportamento observável realmente mudar.

Restrições do projeto
- Preserve autorizações, escopos e confirmações existentes; não execute ações externas, destrutivas ou de alto impacto sem a autorização exigida.
- Nunca repita automaticamente efeitos incertos nem alegue garantia de execução exatamente uma vez. Use reconciliação explícita quando o resultado externo for desconhecido.
- Não leia, mostre, registre ou altere segredos de `.env`; não habilite faturamento, instale dependências ou troque credenciais por conta própria.
- Respeite o workspace delimitado, hashes, backups, publicação atômica e mecanismos existentes de aprovação.
- Não confunda mocks/simuladores com validação real de Gemini, voz, UI-TARS ou hardware.
- Preserve alterações preexistentes do usuário. Neste checkout, não sobrescreva nem reverta a modificação local em `.env.example` nem o `package-lock.json` não rastreado na raiz; não os inclua no commit.
- Não crie commit, não altere configurações Git globais e não limpe arquivos/dados fora do escopo.

Entrega
- Resumo da diferença entre requisito e projeto atual.
- Lista curta do que foi implementado e arquivos alterados.
- Testes executados, resultado e limitações de validação.
- Pendências restantes, riscos e decisões que precisam do usuário.
- Se o requisito já estiver atendido, não faça alterações: demonstre onde está implementado e como validar.
```

## Conclusão

O repositório já tem uma base funcional e mecanismos de segurança que devem ser preservados. As pendências gerais documentadas não são, por si só, justificativa para implementá-las todas. **A prioridade correta depende do requisito original**, que precisa ser colado no campo acima para transformar esta análise-base em uma lista específica de implementação.
