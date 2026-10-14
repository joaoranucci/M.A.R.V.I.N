"""Roteamento determinístico de comandos de voz locais do MARVIN v0.5.

Nenhuma string de usuário é passada como código para shell, PowerShell ou cmd.
Suporta comandos compostos/sequenciais, sinônimos expandidos e melhor reconhecimento de entidades.
"""
from __future__ import annotations
from dataclasses import dataclass
import re
import unicodedata
import webbrowser
from datetime import datetime
from urllib.parse import quote_plus

from .windows_control import CATALOG, desktop_action, list_apps, open_known_folder


@dataclass(frozen=True)
class Command:
    kind: str
    value: str


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKD", text.lower())
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return re.sub(r"\s+", " ", text).strip(" .,!?:\n\t")


def detect_single(n: str, original: str) -> Command:
    if n in {"que horas sao", "me diga as horas", "qual e a hora", "que dia e hoje", "data de hoje", "horas"}:
        return Command("local", "relogio")

    if n in {"atualize aplicativos", "atualiza aplicativos", "atualizar aplicativos",
             "escaneie aplicativos", "procure aplicativos instalados", "reescaneie aplicativos"}:
        return Command("local", "refresh-apps")
    if n in {"liste os aplicativos", "listar aplicativos", "mostre aplicativos", "quais aplicativos tenho",
             "quais programas tenho", "liste apps", "mostre os aplicativos instalados", "lista de aplicativos"}:
        return Command("local", "list-apps")
    if n in {"liste as janelas", "quais janelas estao abertas", "quais programas estao abertos",
             "mostre janelas abertas", "liste janelas abertas", "janelas abertas"}:
        return Command("local", "desktop:list-windows")

    keyboard = {
        "alt tab": "alt-tab", "troque de janela": "alt-tab", "alternar janela": "alt-tab", "mudar de janela": "alt-tab",
        "mostre a area de trabalho": "show-desktop", "mostrar area de trabalho": "show-desktop", "desktop": "show-desktop",
        "minimize a janela": "minimize", "minimiza a janela": "minimize", "minimizar": "minimize",
        "maximize a janela": "maximize", "maximiza a janela": "maximize", "maximizar": "maximize",
        "capture a tela": "screenshot", "tire um print": "screenshot", "tira um print": "screenshot",
        "captura de tela": "screenshot", "print da tela": "screenshot", "print": "screenshot",
        "copie": "copy", "copiar": "copy", "cole": "paste", "colar": "paste",
        "salve": "save", "salvar": "save", "selecionar tudo": "select-all", "selecione tudo": "select-all",
        "pressione enter": "enter", "aperte enter": "enter", "aperte a tecla enter": "enter", "enter": "enter",
        "pressione escape": "escape", "aperte esc": "escape", "esc": "escape",
        "aumente o volume": "volume-up", "aumenta o volume": "volume-up", "aumentar volume": "volume-up",
        "diminua o volume": "volume-down", "diminui o volume": "volume-down", "diminuir volume": "volume-down",
        "silencie o computador": "volume-mute", "deixe sem som": "volume-mute", "mutar": "volume-mute", "mudo": "volume-mute",
        "bloqueie a tela": "lock", "bloquear a tela": "lock", "bloquear": "lock",
        "feche a janela": "close", "fecha a janela": "close", "fechar janela": "close", "fechar": "close",
    }
    if n in keyboard:
        return Command("local", "desktop:" + keyboard[n])

    focus = re.match(r"^(?:mude|troque|alterna|foque|va|trazer|focar) (?:para |na |no |a |o )?(?:janela |programa |app |aplicativo )?(?:do |da |de )?(.+)$", n)
    if focus and len(focus.group(1).strip()) > 1:
        return Command("local", "desktop:focus:" + focus.group(1).strip())

    folder = re.match(r"^(?:abra|abre|abrir|mostre|mostra|acesse|acessar) (?:a |o |minha |meu )?(?:pasta |diretorio )?(downloads?|documentos?|area de trabalho|desktop|imagens|fotos|musicas|videos)$", n)
    if folder:
        return Command("local", "folder:" + folder.group(1))

    search_open = re.match(r"^(?:abra|abre|abrir) (?:o |a )?(?:google|navegador|browser) e (?:pesquise|pesquisa|procure|busque) (?:por |sobre )?(.+)$", n)
    if search_open:
        return Command("local", "google-browser:" + search_open.group(1))

    search = re.match(r"^(?:pesquise|pesquisa|procure|busque|pesquisar|pesquisa na internet|pesquise na internet) (?:no google )?(?:por |sobre )?(.+)$", n)
    if search:
        return Command("local", "google-browser:" + search.group(1).strip())

    opener = re.match(r"^(?:abra|abre|abrir|inicie|inicia|iniciar|execute|executa|abre pra mim|iniciar o) (?:o |a |um |uma |meu |minha )?(?:app |aplicativo |programa )?(.*)$", n)
    if opener:
        target = opener.group(1).strip(" .,!?:")
        if target in {"google", "pagina do google"}:
            return Command("local", "google")
        if target in {"navegador", "browser", "internet", "edge", "chrome"}:
            return Command("local", "browser")
        if re.match(r"^(?:pesquise|pesquisa|procure|busque) (?:no google )?(?:por |sobre )?(.+)$", target):
            match = re.match(r"^(?:pesquise|pesquisa|procure|busque) (?:no google )?(?:por |sobre )?(.+)$", target)
            return Command("local", "google-browser:" + match.group(1))
        if (not target or len(target) > 100 or
            re.search(r"[;&|<>`\n\r]", target) or
            re.search(r"\b(?:apagar|deletar|excluir|formatar|remover arquivos|kill|sudo|pip install)\b", target) or
            re.match(r"^(?:powershell|cmd|terminal)\s+\S+", target)):
            return Command("ask", original)
        return Command("local", "open-app:" + target)

    return Command("ask", original)


def detect(text: str) -> Command:
    original = text.strip()
    n = normalize(original)
    n = re.sub(r"^(?:(?:c|ce|se|si|ei|hey|ola|ok) )?marvin(?:[,: ]+|$)", "", n).strip()
    n = re.sub(r"^(?:por favor[, ]*|pode (?:por favor )?|voce pode |quero que voce )", "", n).strip()

    return detect_single(n, original)


def looks_current(text: str) -> bool:
    n = normalize(text)
    return any(k in n for k in ("hoje", "agora", "ultimas", "ultima noticia", "noticias",
                              "atualizado", "atualmente", "esta semana", "cotacao", "preco atual", "resultado de hoje"))


def execute_local(value: str) -> str:
    if value == "relogio":
        return "Agora são " + datetime.now().strftime("%H:%M") + ", de " + datetime.now().strftime("%d/%m/%Y") + "."
    if value == "list-apps":
        return list_apps()
    if value == "refresh-apps":
        number = len(CATALOG.refresh())
        return f"Atualizei o catálogo. Encontrei {number} aplicativos e atalhos."
    if value.startswith("open-app:"):
        return CATALOG.launch(value.partition(":")[2])
    if value.startswith("folder:"):
        return open_known_folder(value.partition(":")[2])
    if value.startswith("desktop:"):
        parts = value.split(":", 2)
        return desktop_action(parts[1], parts[2] if len(parts) > 2 else "")
    if value in ("browser", "google"):
        webbrowser.open("https://www.google.com")
        return "Abrindo o Google." if value == "google" else "Abrindo o navegador."
    if value.startswith("google-browser:"):
        webbrowser.open("https://www.google.com/search?q=" + quote_plus(value.partition(":")[2]))
        return "Abrindo os resultados da pesquisa no Google no navegador."
    raise ValueError("Ação não autorizada.")
