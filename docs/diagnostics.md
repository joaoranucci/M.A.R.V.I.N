# Diagnóstico e recuperação

1. Abra `DIAGNOSTICO.bat` para versões/capacidades/hardware. Não envia arquivos nem testa microfone automaticamente.
2. Abra `C MARVIN.bat`. Texto deve funcionar mesmo se recursos opcionais faltarem.
3. Para áudio, abra ÁUDIO e selecione a entrada; `DIAGNOSTICO_MICROFONE.bat` captura brevemente quando executado explicitamente.
4. TESTAR VOZ separa a mensagem de reprodução da confirmação humana de audibilidade.
5. TESTAR GOOGLE faz uma geração pequena. 403/404/429/503 têm tratamentos separados; não há ativação de cobrança ou troca de contas.
6. TAREFAS mostra o objetivo, etapas e resultados reais. `needs_reconciliation` exige conferir o efeito, não repetir automaticamente.

## Ambiente

Referência validada: Python 3.12.10 na `.venv`; Python 3.14.5 foi usado para testes adicionais do núcleo. A primeira tentativa restrita de iniciar a `.venv` foi negada pelo ambiente de execução do Codex; execução fora dessa restrição confirmou que a instalação funciona. Não é necessário reconstruí-la só por causa dessa tentativa.

`INSTALAR.bat` usa `setup_marvin.py` e não atualiza indiscriminadamente o pip. Um ambiente inválido é preservado com outro nome; dados/configuração não são removidos. `--core-only` instala somente as dependências de texto/IA. As versões de primeiro nível em requirements foram importadas no ambiente existente; instalação do zero continua sujeita a disponibilidade dos pacotes e compatibilidade do Python.

A base de fuso IANA é opcional (`tzdata`). Sem ela, aparece fallback UTC−03 para São Paulo. Não use esse fallback para validar datas históricas ou mudanças futuras de regra civil.

## Backups

- `data/upgrade_backups/pre_v070`: código anterior a esta evolução.
- `data/backups`: cópias SQLite antes de migrações.
- `<projeto>/.marvin_versions`: versões de arquivos sobrescritos com aprovação.
- `data/code_backups/<id>`: transações de autoprogramação com journal e originais.

Backups podem conter informações posteriormente excluídas do banco ativo. Nenhum backup é compartilhado automaticamente.

## Restaurar código

Feche o MARVIN. Use o Python disponível da instalação:

```bat
EXECUTAR.bat -m marvin.maintenance snapshot
EXECUTAR.bat -m marvin.maintenance restore-code --snapshot data\upgrade_backups\pre_v070
```

A restauração pede `RESTAURAR`, salva primeiro o código atual e restaura somente arquivos de código/documentação reconhecidos. `.env`, bancos, modelos e projetos ficam preservados. Módulos extras que não existiam no snapshot não são removidos. Não restaura dependências da `.venv`.

As migrações v0.7 são aditivas e mantêm o schema legado; voltar ao código anterior não requer excluir as tabelas novas. Se houver corrupção do banco, feche o aplicativo, preserve uma cópia do banco atual e restaure manualmente a cópia SQLite escolhida de `data/backups`. Isso perde alterações posteriores àquela cópia; faça essa escolha conscientemente.

Em falha de uma proposta multiarquivo, consulte `transaction.json` no backup correspondente. `SourceEditor.rollback_reviewed(id)` só deve ser chamado após revisão; ele recusa sobrescrever um arquivo que mudou novamente.

## Remover

Encerre o aplicativo e os servidores que iniciou. A instalação é uma pasta local, sem serviço de sistema novo ou inicialização automática adicionada. Preserve/exporte `data`, `.env` e `MARVIN_Projetos` antes de remover a pasta. Modelos e `.venv` podem ocupar bastante espaço. O projeto não remove automaticamente programas Python/Node instalados separadamente.
