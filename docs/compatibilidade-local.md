# Execução local — 13/10/2026

O ambiente anterior usava Python 3.15.0, Tk 9 e não tinha pip. Foi preservado
em `.venv.backup-*`. A nova `.venv` usa o Python 3.12.10 já instalado em
`%LocalAppData%\Programs\Python\Python312` e as dependências de requirements.txt.

O launcher verifica a versão e Tkinter e também procura essa instalação de
Python 3.12 quando o ambiente local estiver indisponível. O instalador verifica
pip e rejeita Python 3.15 ou superior para evitar reutilizar ambientes ainda
não validados com as bibliotecas nativas. tzdata foi incluído no núcleo para
disponibilizar o fuso IANA no Windows.

O roteador deixou de executar apenas o primeiro fragmento de pedidos compostos:
isso truncava a pesquisa no Google e aceitava parcialmente entradas com ponto
e vírgula. Esses casos são cobertos pelos testes existentes.

Validação no Windows, Python 3.12.10:

- `python -m unittest discover -s tests -q`: 173 testes, OK, 2 pulados
  (criação de links simbólicos indisponível para a conta).
- `python -m pip check`: nenhuma dependência quebrada.
- `node --check ui_tars_bridge/runner.mjs`: sintaxe válida.
- Janela `MARVIN — 0.7.0` aberta e respondendo, confirmada via Windows.

O aplicativo foi iniciado usando main.py. Logs ficam em
`data/logs/startup.stdout.log` e `data/logs/startup.stderr.log`.
Vosk iniciou, mas informou que a palavra `vin` de uma variante de ativação
não pertence ao vocabulário. A qualidade acústica não foi medida.
Gemini requer teste de acesso/cota pela interface; o servidor e SDK UI-TARS
não foram configurados nesta execução.

Para abrir novamente, use `C MARVIN.bat` ou `INICIAR.bat`.
