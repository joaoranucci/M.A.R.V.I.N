# DESENVOLVA_JOGOS_COM_HTML5_CANVAS_E_JAVA

Arquivo original: more_papers_by_thyago_louiz/DESENVOLVA_JOGOS_COM_HTML5_CANVAS_E_JAVA.pdf
SHA-256 do original: 591d24af0ec11f24b4a17e8d9e1090e7dd42b582961ac75aa863b8e762f27c06

Texto extraido para consulta. As paginas abaixo usam a ordem do arquivo PDF, incluindo capas.
Parte preparada: 1/1


[PAGINA 1]


[PAGINA 2]
Casa do Código




Introdução

Se você chegou até este livro, é porque está interessado em desenvolver jo-
gos. Aqui focarei no desenvolvimento de jogos para a web, usando a tec-
nologia Canvas, presente na especificação do HTML5 e suportada por to-
dos os maiores browsers modernos, em suas versões mais atualizadas. Pre-
tendo mostrar que desenvolver jogos é uma tarefa na realidade simples, e que
não exige grandes curvas de aprendizados com frameworks monstruosos —
o básico oferecido pelo ambiente do navegador é o suficiente para começar!
    Tudo o que você precisará é de um browser atualizado e um bom edi-
tor de textos. Em ambiente Windows, é muito comum o uso do Notepad++
(http://notepad-plus-plus.org) . Caso você use Linux, é bem provável que sua
distribuição já venha com um editor que suporte coloração de sintaxe para
várias linguagens (GEdit, KWrite, etc.). No entanto, eu recomendo veemente-
mente o uso do Brackets (http://brackets.io) , que foi onde eu criei os códigos.
É multiplataforma (funciona em Windows, Linux, Mac OS X) e realiza auto-
completar em código JavaScript de forma bastante eficiente.
    O jogo que você vai criar já está disponível na web. Você pode jogá-lo a
qualquer momento em:
    http://gamecursos.com.br/livro/jogo
    Estarei sempre presente e atuante no seguinte grupo do Google Groups,
como forma de interagir com meus leitores:
    http://groups.google.com/forum/#!forum/livro-jogos-html5-canvas
    Por fim, todos os códigos e imagens estão disponíveis em (embora eu
aconselhe você a digitar os códigos e usar os prontos no download apenas
para referência em caso de dúvidas):
    http://github.com/EdyKnopfler/games-js/archive/master.zip

                                                                               i


[PAGINA 3]
                   Casa do Código


     Bom estudo!




ii


[PAGINA 4]
Casa do Código                                                               Sumário




Sumário

1   Fundamentos                                                                   1
    1.1   Introdução ao HTML5 Canvas . . . . . . . . . . . . . . . . . .          3
    1.2   Começando a desenhar . . . . . . . . . . . . . . . . . . . . . .        6
    1.3   Animações com requestAnimationFrame . . . . . . . . . . . .            22
    1.4   Orientação a objetos com JavaScript . . . . . . . . . . . . . .        26

2   O loop de animação                                                           35
    2.1   Introdução e sprites . . . . . . . . . . . . . . . . . . . . . . . .   35
    2.2   Teste para a classe Animacao . . . . . . . . . . . . . . . . . . .     38
    2.3   Desenvolva a classe Animacao . . . . . . . . . . . . . . . . . .       41
    2.4   Implemente a classe Bola . . . . . . . . . . . . . . . . . . . . .     45

3   A interação com o jogador — leitura apurada do teclado                       49
    3.1   EventListeners e os eventos keydown e keyup . . . . . . . . .          50
    3.2   Detectando se uma tecla está ou não pressionada . . . . . . .          55
    3.3   Efetuando disparos — detectando somente o primeiro keydown 58

4 Folhas de sprites — spritesheets                                               69
    4.1   Conceito e abordagem utilizada . . . . . . . . . . . . . . . . .       69
    4.2   Carregando imagens e fazendo recortes (clipping) . . . . . .           72
    4.3   Animações de sprite — a classe Spritesheet . . . . . . . . . .         75
    4.4   Controle o herói pelo teclado e veja sua animação . . . . . .          80

                                                                                 iii


[PAGINA 5]
Sumário                                                                 Casa do Código


5    Detecção de colisões                                                           87
     5.1   Colisão entre retângulos . . . . . . . . . . . . . . . . . . . . .        87
     5.2   Teste da classe Colisor . . . . . . . . . . . . . . . . . . . . . . .    90
     5.3   A classe Colisor . . . . . . . . . . . . . . . . . . . . . . . . . .      93
     5.4   Criando um sprite colidível . . . . . . . . . . . . . . . . . . . .       95
     5.5   Melhorando o código . . . . . . . . . . . . . . . . . . . . . . .        98

6 Iniciando o desenvolvimento do jogo                                               107
     6.1   Animação de fundo com efeito parallax . . . . . . . . . . . .            107
     6.2   Controle da nave na horizontal e na vertical . . . . . . . . . .         118
     6.3   Efetuando disparos . . . . . . . . . . . . . . . . . . . . . . . .       123

7    Criando inimigos                                                               129
     7.1   Primeiro teste com nave e inimigos . . . . . . . . . . . . . . .         130
     7.2   A classe Ovni . . . . . . . . . . . . . . . . . . . . . . . . . . . .    134
     7.3   Adicionando fundo em parallax . . . . . . . . . . . . . . . . .          135
     7.4   Adicionando colisão . . . . . . . . . . . . . . . . . . . . . . . .      139
     7.5   Estamos experimentando lentidão! . . . . . . . . . . . . . . .           145
     7.6   Excluindo os objetos desnecessários . . . . . . . . . . . . . . .        151

8    Incorpore animações, sons, pausa e vidas extras ao jogo                        155
     8.1   Organizando o código . . . . . . . . . . . . . . . . . . . . . . .       156
     8.2   Animação cronometrada . . . . . . . . . . . . . . . . . . . . .          162
     8.3   Animando a nave com spritesheets . . . . . . . . . . . . . . .           165
     8.4   Criando explosões . . . . . . . . . . . . . . . . . . . . . . . . .      169
     8.5   Pausando o jogo . . . . . . . . . . . . . . . . . . . . . . . . . .      175
     8.6   Sons e música de fundo . . . . . . . . . . . . . . . . . . . . . .       179
     8.7   Tela de loading . . . . . . . . . . . . . . . . . . . . . . . . . . .    181
     8.8   Vidas extras . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   186
     8.9   Pontuação (score) . . . . . . . . . . . . . . . . . . . . . . . . .      190
     8.10 Tela de Game Over . . . . . . . . . . . . . . . . . . . . . . . .         192

iv


[PAGINA 6]
Casa do Código                                                        Sumário



9 Publique seu jogo e torne-o conhecido                                   197
  9.1 Hospede-o em um serviço gratuito . . . . . . . . . . . . . . .      197
  9.2 Linkando com as redes sociais . . . . . . . . . . . . . . . . . .   203

Bibliografia                                                              213




                                                                           v


[PAGINA 7]


[PAGINA 8]
Capítulo 1

Fundamentos
Aqui começa uma fascinante jornada pelos segredos de uma tecnologia que,
na verdade, não possui segredo algum. Trata-se do Canvas, uma das maravil-
has do HTML5.
    O Canvas é uma área retangular em uma página web onde podemos
criar desenhos programaticamente, usando JavaScript (a linguagem de pro-
gramação normal das páginas HTML). Com esta tecnologia, podemos criar
trabalhos artísticos, animações e jogos, que é o assunto central deste livro.
    Com o Canvas, ao longo dos capítulos, iremos desenvolver o jogo da
figura 1.1:


[PAGINA 9]
                                                                 Casa do Código




               Figura 1.1: Jogo desenvolvido ao longo do livro


    Este livro é composto pelos seguintes capítulos:
    1. Fundamentos: neste capítulo, aprenda como funciona o Canvas, como
criar animações via programação e também noções de Orientação a obje-
tos em JavaScript, para que nossos códigos se tornem mais organizados e
reaproveitáveis;
    2. O loop de animação: controle a animação de seus jogos de forma efi-
ciente. Conheça o conceito de sprites e aprenda a gerenciá-los em uma ani-
mação;
    3. A interação com o jogador — leitura apurada do teclado: saiba como
capturar eventos do teclado de maneira eficiente para jogos;
    4. Folhas de sprites — spritesheets: anime os elementos de seu jogo indi-
vidualmente usando imagens contendo todos os quadros de uma animação;
    5. Detecção de colisões: aprenda a detectar quando os elementos de um
jogo “tocam” uns aos outros na tela e execute as ações adequadas;
    6. Iniciando o desenvolvimento do jogo: um joguinho de nave começará
a tomar forma usando todos os elementos aprendidos até então;
    7. Criando inimigos: adicione verdadeira emoção ao seu jogo, dando

2


[PAGINA 10]
Casa do Código                                           Capítulo 1. Fundamentos



ao herói alguém a quem enfrentar. Usaremos intensivamente a detecção de
colisões;
    8. Incorpore animações, sons, pausa e vidas extras ao jogo: com todos os
conceitos aprendidos e bem fixados, você verá como é fácil estender o jogo e
adicionar novos elementos. Ao fim do capítulo, você terá sugestões de mel-
horias que você mesmo poderá tentar realizar, como exercício;
    9. Publique seu jogo e torne-o conhecido: um passo a passo de como
publicar seu jogo na web e divulgá-lo nas redes sociais.
    Importante: preparei um pacote de arquivos contendo todos os códigos,
imagens e sons utilizados. Em cada novo arquivo que criarmos, indicarei o
nome do respectivo arquivo nesse pacote. Realize seu download no endereço:
    http://github.com/EdyKnopfler/games-js/archive/master.zip
    Antes de começarmos a desenvolver um jogo em específico, é importante
nos habituarmos a algumas funções da tecnologia Canvas. O que está es-
perando? Vamos começar o aprendizado!


1.1   Introdução ao HTML5 Canvas
Para criar um Canvas em uma página HTML, utilizamos a tag <canvas>. Os
atributos width e height informam a largura e a altura, respectivamente,
da área de desenho. É importante também informar um id para podermos
trabalhar com ele no código JavaScript:
❁❝❛♥✈❛s ✐❞❂✧♥♦♠❡❴❝❛♥✈❛s✧ ✇✐❞t❤❂✧❧❛r❣✉r❛✧ ❤❡✐❣❤t❂✧❛❧t✉r❛✧❃
❁✴❝❛♥✈❛s❃

    Entre as tags de abertura e fechamento, podemos colocar alguma men-
sagem indicando que o browser não suporta essa tecnologia. Caso o browser
a suporte, esse conteúdo é ignorado:
❁❝❛♥✈❛s ✐❞❂✧♠❡✉❴❝❛♥✈❛s✧ ✇✐❞t❤❂✧✸✵✵✧ ❤❡✐❣❤t❂✧✸✵✵✧❃
   ❙❡✉ ♥❛✈❡❣❛❞♦r ♥ã♦ s✉♣♦rt❛ ♦ ❈❛♥✈❛s ❞♦ ❍❚▼▲✺✳ ❁❜r❃
   Pr♦❝✉r❡ ❛t✉❛❧✐③á✲❧♦✳
❁✴❝❛♥✈❛s❃

    Os atributos width e height da tag <canvas> são obrigatórios, pois
são os valores usados na geração da imagem. O Canvas pode receber dimen-

                                                                              3


[PAGINA 11]
1.1. Introdução ao HTML5 Canvas                                Casa do Código


sões diferentes via CSS, no entanto, seu processamento sempre será feito us-
ando as dimensões informadas na tag. Se as dimensões no CSS forem difer-
entes, o browser amplia ou reduz a imagem gerada para deixá-la de acordo
com a folha de estilo.
    Dado um Canvas com dimensões 100x100 pixels:

❁❝❛♥✈❛s ✐❞❂✧♠❡✉❴❝❛♥✈❛s✧ ✇✐❞t❤❂✧✶✵✵✧ ❤❡✐❣❤t❂✧✶✵✵✧❃❁✴❝❛♥✈❛s❃

    A seguinte formatação CSS fará a imagem ser ampliada:

★♠❡✉❴❝❛♥✈❛s ④
   ✇✐❞t❤✿ ✷✵✵♣①❀
   ❤❡✐❣❤t✿ ✷✵✵♣①❀
⑥

Contexto gráfico
    Para desenhar no Canvas, é preciso executar um script após ele ter sido
carregado. Neste script, obteremos o contexto gráfico, que é o objeto que re-
aliza de fato as tarefas de desenho no Canvas.
    Uma maneira é criar uma tag <script> após a tag <canvas>:

❁✦❉❖❈❚❨P❊ ❤t♠❧❃
❁❤t♠❧❃

❁❤❡❛❞❃
   ❁t✐t❧❡❃Pr♦❝❡ss❛♥❞♦ ♦ ❈❛♥✈❛s ❛♣ós ❛ t❛❣❁✴t✐t❧❡❃
❁✴❤❡❛❞❃

❁❜♦❞②❃
   ❁❝❛♥✈❛s ✐❞❂✧♠❡✉❴❝❛♥✈❛s✧ ✇✐❞t❤❂✧✷✵✵✧ ❤❡✐❣❤t❂✧✷✵✵✧❃❁✴❝❛♥✈❛s❃
   ❁s❝r✐♣t❃
      ✴✴ ❆q✉✐ ♦❜t❡r❡♠♦s ♦ ❝♦♥t❡①t♦ ❣rá❢✐❝♦ ❡ tr❛❜❛❧❤❛r❡♠♦s ❝♦♠ ♦
      ✴✴ ❈❛♥✈❛s
   ❁✴s❝r✐♣t❃
❁✴❜♦❞②❃

❁✴❤t♠❧❃


4


[PAGINA 12]
Casa do Código                                          Capítulo 1. Fundamentos



    Também é muito comum desenharmos em eventos que ocorrem após a
página ter sido carregada. Isto é útil caso queiramos colocar os scripts na
seção <head> do documento HTML:

❁✦❉❖❈❚❨P❊ ❤t♠❧❃
❁❤t♠❧❃

❁❤❡❛❞❃
   ❁t✐t❧❡❃Pr♦❝❡ss❛♥❞♦ ♦ ❈❛♥✈❛s ♥❛ s❡çã♦ ❍❊❆❉❁✴t✐t❧❡❃
   ❁s❝r✐♣t❃
      ✇✐♥❞♦✇✳♦♥❧♦❛❞ ❂ ❢✉♥❝t✐♦♥✭✮ ④
         ✴✴ ❆q✉✐ tr❛❜❛❧❤❛r❡♠♦s ❝♦♠ ♦ ❈❛♥✈❛s
      ⑥
   ❁✴s❝r✐♣t❃
❁✴❤❡❛❞❃

❁❜♦❞②❃
   ❁❝❛♥✈❛s ✐❞❂✧♠❡✉❴❝❛♥✈❛s✧ ✇✐❞t❤❂✧✷✵✵✧ ❤❡✐❣❤t❂✧✷✵✵✧❃❁✴❝❛♥✈❛s❃
❁✴❜♦❞②❃

❁✴❤t♠❧❃

    No código, nós referenciamos o Canvas e obtemos o contexto gráfico. O
Canvas é referenciado como qualquer elemento em uma página; o contexto
é obtido pelo método getContext do Canvas. Como parâmetro, passamos
uma string identificando o contexto desejado. Neste livro, usaremos o con-
texto 2d (“d” em minúsculo!):

❁❝❛♥✈❛s ✐❞❂✧♠❡✉❴❝❛♥✈❛s✧ ✇✐❞t❤❂✧✷✵✵✧ ❤❡✐❣❤t❂✧✷✵✵✧❃❁✴❝❛♥✈❛s❃
❁s❝r✐♣t❃
   ✴✴ ❘❡❢❡r❡♥❝✐❛♥❞♦ ♦ ❈❛♥✈❛s
   ✈❛r ❝❛♥✈❛s ❂ ❞♦❝✉♠❡♥t✳❣❡t❊❧❡♠❡♥t❇②■❞✭✬♠❡✉❴❝❛♥✈❛s✬✮❀

   ✴✴ ❖❜t❡♥❞♦ ♦ ❝♦♥t❡①t♦ ❣rá❢✐❝♦
   ✈❛r ❝♦♥t❡①t ❂ ❝❛♥✈❛s✳❣❡t❈♦♥t❡①t✭✬✷❞✬✮❀
❁✴s❝r✐♣t❃




                                                                             5


[PAGINA 13]
1.2. Começando a desenhar                                         Casa do Código


O sistema de coordenadas do Canvas
   Para posicionarmos os desenhos no Canvas, pensamos nele como um
enorme conjunto de pontos. Cada ponto possui uma posição horizontal (x)
e uma vertical (y).
   O ponto (0, 0) (lê-se: zero em x e zero em y) corresponde ao canto
superior esquerdo do Canvas:




                  Figura 1.2: Sistema de coordenadas do Canvas



1.2 Começando a desenhar

Métodos fillRect e strokeRect
Uma vez obtido o contexto gráfico, podemos configurar várias propriedades e
chamar nele os métodos de desenho. Por exemplo, para desenhar retângulos,
podemos usar os métodos:

    • fillRect(x, y, largura, altura): pinta completamente uma
      área retangular;

    • strokeRect(x, y, largura, altura): desenha um contorno
      do retângulo.

    Os valores x e y corresponderão à posição do canto superior esquerdo
do retângulo. A partir daí, o retângulo vai para a direita (largura) e para baixo
(altura).

6


[PAGINA 14]
Casa do Código                                             Capítulo 1. Fundamentos



   Veja um exemplo de código para desenhar um retângulo no Canvas,
nosso primeiro exemplo prático completo:
❁✦✲✲ ❛rq✉✐✈♦✿ r❡t❛♥❣✉❧♦s✲✶✳❤t♠❧ ✲✲❃
❁✦✲✲ ❡st❡ ❝ó❞✐❣♦ ✈❛✐ ❞❡♥tr♦ ❞♦ ❜♦❞② ✲✲❃
❁❝❛♥✈❛s ✐❞❂✧♠❡✉❴❝❛♥✈❛s✧ ✇✐❞t❤❂✧✷✵✵✧ ❤❡✐❣❤t❂✧✷✵✵✧❃❁✴❝❛♥✈❛s❃
❁s❝r✐♣t❃
   ✴✴ ❈❛♥✈❛s ❡ ❝♦♥t❡①t♦
   ✈❛r ❝❛♥✈❛s ❂ ❞♦❝✉♠❡♥t✳❣❡t❊❧❡♠❡♥t❇②■❞✭✬♠❡✉❴❝❛♥✈❛s✬✮❀
   ✈❛r ❝♦♥t❡①t ❂ ❝❛♥✈❛s✳❣❡t❈♦♥t❡①t✭✬✷❞✬✮❀

   ✴✴ ❉❡s❡♥❤❛r ✉♠ r❡tâ♥❣✉❧♦
   ❝♦♥t❡①t✳❢✐❧❧❘❡❝t✭✺✵✱ ✺✵✱ ✶✵✵✱ ✶✵✵✮❀
❁✴s❝r✐♣t❃

    Não é simples de fazer? O resultado será um simples retângulo preto. Seu
canto superior esquerdo localiza-se no ponto (50, 50), e ele possui 100 pixels
de largura por 100 pixels de altura:




                  Figura 1.3: Retângulo desenhado com fillRect


    Se trocarmos fillRect por strokeRect, veremos apenas o contorno:




                 Figura 1.4: Retângulo desenhado com strokeRect




                                                                                7


[PAGINA 15]
1.2. Começando a desenhar                                     Casa do Código


Propriedades fillStyle, strokeStyle e lineWidth
    Podemos configurar algumas propriedades do contexto, de forma a escol-
her as cores e espessuras:

    • fillStyle: cor do preenchimento

    • strokeStyle: cor da linha

    • lineWidth: espessura da linha em pixels

❁✦✲✲ ❛rq✉✐✈♦✿ r❡t❛♥❣✉❧♦s✲✷✳❤t♠❧ ✲✲❃
❁❝❛♥✈❛s ✐❞❂✧♠❡✉❴❝❛♥✈❛s✧ ✇✐❞t❤❂✧✷✵✵✧ ❤❡✐❣❤t❂✧✷✵✵✧❃❁✴❝❛♥✈❛s❃
❁s❝r✐♣t❃
   ✴✴ ❈❛♥✈❛s ❡ ❝♦♥t❡①t♦
   ✈❛r ❝❛♥✈❛s ❂ ❞♦❝✉♠❡♥t✳❣❡t❊❧❡♠❡♥t❇②■❞✭✬♠❡✉❴❝❛♥✈❛s✬✮❀
   ✈❛r ❝♦♥t❡①t ❂ ❝❛♥✈❛s✳❣❡t❈♦♥t❡①t✭✬✷❞✬✮❀

    ✴✴ Pr❡❡♥❝❤✐♠❡♥t♦ ✈❡r♠❡❧❤♦
    ❝♦♥t❡①t✳❢✐❧❧❙t②❧❡ ❂ ✬r❡❞✬❀
    ❝♦♥t❡①t✳❢✐❧❧❘❡❝t✭✺✵✱ ✺✵✱ ✶✵✵✱ ✶✵✵✮❀

   ✴✴ ❈♦♥t♦r♥♦ ❛③✉❧✱ ❝♦♠ ❡s♣❡ss✉r❛ ❞❡ ✸♣①
   ❝♦♥t❡①t✳❧✐♥❡❲✐❞t❤ ❂ ✸❀
   ❝♦♥t❡①t✳str♦❦❡❙t②❧❡ ❂ ✬❜❧✉❡✬❀
   ❝♦♥t❡①t✳str♦❦❡❘❡❝t✭✺✵✱ ✺✵✱ ✶✵✵✱ ✶✵✵✮❀
❁✴s❝r✐♣t❃




Figura 1.5: Configurando as propriedades do preenchimento (fillStyle) e con-
torno (strokeStyle)




8


[PAGINA 16]
Casa do Código                                              Capítulo 1. Fundamentos



Paths (caminhos)
    Desenhos mais complexos podem ser desenhados como paths (camin-
hos). Um path é um conjunto de comandos de desenho que ficam registrados
na memória, aguardando os métodos fill (preencher) ou stroke (contornar)
serem chamados.
    Porém, antes de tudo, devemos chamar o método beginPath (iniciar cam-
inho) para apagar os traçados feitos previamente. Se não fizermos isso, eles fi-
carão na memória e serão desenhados novamente junto com o próximo path:

✴✴ ❊①❡♠♣❧♦ t❡ór✐❝♦
✴✴ P❛ss♦ ❛ ♣❛ss♦ ♣❛r❛ ❝r✐❛r ✉♠ ♣❛t❤✿

✴✴ ■♥✐❝✐❛r ♥♦✈♦ ♣❛t❤ ✭❛♣❛❣❛♥❞♦ ❞❡s❡♥❤♦s ❛♥t❡r✐♦r❡s✮
❝♦♥t❡①t✳❜❡❣✐♥P❛t❤✭✮❀

✴✴ ❆q✉✐ ❢❛ç♦ ♠❡✉ ❞❡s❡♥❤♦
✴✴ ✳✳✳

✴✴ Pr❡❡♥❝❤❡r t♦❞❛ ❛ ár❡❛ ❞❡s❡♥❤❛❞❛
❝♦♥t❡①t✳❢✐❧❧✭✮❀

✴✴ ❈♦♥t♦r♥❛r ❛ ár❡❛ ❞❡s❡♥❤❛❞❛
❝♦♥t❡①t✳str♦❦❡✭✮❀

    Por exemplo, podemos desenhar uma estrela usando os seguintes coman-
dos:

    • moveTo(x, y): posiciona a caneta virtual em um determinado
      ponto;

    • lineTo(x, y): traça uma linha do ponto atual até o ponto indicado.




                                                                                 9


[PAGINA 17]
1.2. Começando a desenhar                                           Casa do Código




                Figura 1.6: Estrela criada usando moveTo e lineTo


    Esses comandos não desenham as linhas imediatamente, apenas ar-
mazenam as informações no path. Devemos chamar o método stroke para
desenhá-las de fato no Canvas:

❁✦✲✲ ❛rq✉✐✈♦✿ ❝❛♠✐♥❤♦s✳❤t♠❧ ✲✲❃
❁❝❛♥✈❛s ✐❞❂✧♠❡✉❴❝❛♥✈❛s✧ ✇✐❞t❤❂✧✸✵✵✧ ❤❡✐❣❤t❂✧✸✵✵✧❃❁✴❝❛♥✈❛s❃
❁s❝r✐♣t❃
   ✴✴ ❈❛♥✈❛s ❡ ❝♦♥t❡①t♦
   ✈❛r ❝❛♥✈❛s ❂ ❞♦❝✉♠❡♥t✳❣❡t❊❧❡♠❡♥t❇②■❞✭✬♠❡✉❴❝❛♥✈❛s✬✮❀
   ✈❛r ❝♦♥t❡①t ❂ ❝❛♥✈❛s✳❣❡t❈♦♥t❡①t✭✬✷❞✬✮❀

     ✴✴ ■♥✐❝✐❛r ♦ ❝❛♠✐♥❤♦ ✭❛♣❛❣❛ ❞❡s❡♥❤♦s ❛♥t❡r✐♦r❡s✮
     ❝♦♥t❡①t✳❜❡❣✐♥P❛t❤✭✮❀

     ✴✴ ❉❡s❡♥❤❛r ✉♠❛ ❡str❡❧❛
     ❝♦♥t❡①t✳♠♦✈❡❚♦✭✼✺✱ ✷✺✵✮❀ ✴✴ P♦♥t♦ ✐♥✐❝✐❛❧
     ❝♦♥t❡①t✳❧✐♥❡❚♦✭✶✺✵✱ ✺✵✮❀
     ❝♦♥t❡①t✳❧✐♥❡❚♦✭✷✷✺✱ ✷✺✵✮❀
     ❝♦♥t❡①t✳❧✐♥❡❚♦✭✺✵✱ ✶✷✵✮❀
     ❝♦♥t❡①t✳❧✐♥❡❚♦✭✷✺✵✱ ✶✷✵✮❀
     ❝♦♥t❡①t✳❧✐♥❡❚♦✭✼✺✱ ✷✺✵✮❀

     ✴✴ ❈♦♥❢✐❣✉r❛r ❛ ❧✐♥❤❛
     ❝♦♥t❡①t✳❧✐♥❡❲✐❞t❤ ❂ ✷❀
     ❝♦♥t❡①t✳str♦❦❡❙t②❧❡ ❂ ✬r❡❞✬❀

     ✴✴ ❚r❛ç❛r ❛s ❧✐♥❤❛s ❞♦ ❝❛♠✐♥❤♦
     ❝♦♥t❡①t✳str♦❦❡✭✮❀

10


[PAGINA 18]
Casa do Código                                              Capítulo 1. Fundamentos



❁✴s❝r✐♣t❃

Circunferências e arcos
    São criados com o mesmo método, arc. Um arco é uma parte de uma
circunferência, e serve para criar linhas curvas. Uma circunferência, para o
Canvas, é nada mais que um arco de 360 graus.
    O método arc recebe os seguintes parâmetros:

    • x, y: as coordenadas do ponto central da circunferência;

    • raio da circunferência em pixels;

    • ângulo inicial em radianos;

    • ângulo final em radianos;

    • sentido: aqui você pode passar false (sentido anti-horário) ou true
      (sentido horário). Este parâmetro é opcional; se omitido, o desenho é
      feito no sentido anti-horário.




Figura 1.7: Localização do ponto central, ângulos inicial e final e o ponto zero


    Os ângulos podem estar em qualquer posição na circunferência e têm
de ser informados em radianos, não em graus. Lembra-se das aulas de
trigonometria? Eu também não, mas sabemos que pi radianos é meia
volta (180 graus), portanto 2 pi vale uma volta completa (360 graus). Para

                                                                                11


[PAGINA 19]
1.2. Começando a desenhar                                    Casa do Código


nossa sorte, o JavaScript possui a constante Math.PI, que nos dá o valor
3.141592653589793!


     Convertendo de graus para radianos

       A fórmula é muito simples:

     ✈❛r ❣r❛✉s ❂ ✳✳✳ ❀
     ✈❛r r❛❞✐❛♥♦s ❂ ❣r❛✉s ✯ ▼❛t❤✳P■ ✴ ✶✽✵❀



    Importante: o método arc é usado em um path, ou seja, não desenha o
arco ou círculo na hora.
    O primeiro arco da figura 1.7 pode então ser desenhado com o comando:

✴✴ ❊①❡♠♣❧♦ t❡ór✐❝♦
❝♦♥t❡①t✳❛r❝✭
   ✺✵✱              ✴✴ ❳ ✭❝❡♥tr♦✮
   ✺✵✱              ✴✴ ❨ ✭❝❡♥tr♦✮
   ✹✵✱              ✴✴ ❘❛✐♦
   ✾✵✯▼❛t❤✳P■✴✶✽✵✱ ✴✴ ■♥í❝✐♦✿ ✾✵ ❣r❛✉s
   ✷✼✵✯▼❛t❤✳P■✴✶✽✵✱ ✴✴ ❚ér♠✐♥♦✿ ✷✼✵ ❣r❛✉s
   ❢❛❧s❡            ✴✴ ❙❡♥t✐❞♦ ❛♥t✐✲❤♦rár✐♦
✮❀

    Para fazer o outro arco, basta escrevermos true no último parâmetro.
    Vamos experimentar na prática! Primeiro, vamos inicializar as variáveis
e configurar o contexto com a aparência desejada:

❁✦✲✲ ❛rq✉✐✈♦✿ ❛r❝♦s✳❤t♠❧ ✲✲❃
❁❝❛♥✈❛s ✐❞❂✧♠❡✉❴❝❛♥✈❛s✧ ✇✐❞t❤❂✧✸✵✵✧ ❤❡✐❣❤t❂✧✸✵✵✧❃❁✴❝❛♥✈❛s❃
❁s❝r✐♣t❃
   ✴✴ ❈❛♥✈❛s ❡ ❝♦♥t❡①t♦
   ✈❛r ❝❛♥✈❛s ❂ ❞♦❝✉♠❡♥t✳❣❡t❊❧❡♠❡♥t❇②■❞✭✬♠❡✉❴❝❛♥✈❛s✬✮❀
   ✈❛r ❝♦♥t❡①t ❂ ❝❛♥✈❛s✳❣❡t❈♦♥t❡①t✭✬✷❞✬✮❀

      ✴✴ ❈♦r❡s ❡ ❡s♣❡ss✉r❛ ❞❛ ❧✐♥❤❛
      ❝♦♥t❡①t✳❢✐❧❧❙t②❧❡ ❂ ✬❣r❛②✬❀

12


[PAGINA 20]
Casa do Código                                           Capítulo 1. Fundamentos



   ❝♦♥t❡①t✳str♦❦❡❙t②❧❡ ❂ ✬❜❧❛❝❦✬❀
   ❝♦♥t❡①t✳❧✐♥❡❲✐❞t❤ ❂ ✷❀

   ✴✴ ❝♦♥t✐♥✉❛✳✳✳
❁✴s❝r✐♣t❃

    Para fazer um arco, devemos iniciar um path, chamar o método arc
e depois fazer fill e stroke (ou somente um destes dois, se quisermos
somente preenchimento ou somente contorno):

✴✴ Pr✐♠❡✐r♦ ❛r❝♦✿
✴✴ ◆♦✈♦ ♣❛t❤
❝♦♥t❡①t✳❜❡❣✐♥P❛t❤✭✮❀
✴✴ ❉❡s❡♥❤❛
❝♦♥t❡①t✳❛r❝✭✺✵✱ ✺✵✱ ✹✵✱ ✾✵✯▼❛t❤✳P■✴✶✽✵✱ ✷✼✵✯▼❛t❤✳P■✴✶✽✵✱
   ❢❛❧s❡✮❀
✴✴ Pr❡❡♥❝❤✐♠❡♥t♦
❝♦♥t❡①t✳❢✐❧❧✭✮❀
✴✴ ❈♦♥t♦r♥♦
❝♦♥t❡①t✳str♦❦❡✭✮❀

✴✴ ❝♦♥t✐♥✉❛✳✳✳

    Se quisermos fazer outro arco, temos que iniciar mais um path; do con-
trário, o desenho formado ficará estranho (figura 1.8). Repare que a posição
x foi deslocada para desenharmos à direita do anterior:

✴✴ ❙❡❣✉♥❞♦ ❛r❝♦
❝♦♥t❡①t✳❜❡❣✐♥P❛t❤✭✮❀
❝♦♥t❡①t✳❛r❝✭✶✺✵✱ ✺✵✱ ✹✵✱ ✾✵✯▼❛t❤✳P■✴✶✽✵✱ ✷✼✵✯▼❛t❤✳P■✴✶✽✵✱
   tr✉❡✮❀
❝♦♥t❡①t✳❢✐❧❧✭✮❀
❝♦♥t❡①t✳str♦❦❡✭✮❀

✴✴ ❝♦♥t✐♥✉❛ ✳✳✳




                                                                             13


[PAGINA 21]
1.2. Começando a desenhar                                      Casa do Código




Figura 1.8: Dois arcos desenhados juntos no mesmo path: um é a continuação
do outro!


    Faça também uma circunferência completa. Não precisa se preocupar em
converter 360 graus para radianos, basta fazer o arco de zero até 2 pi. Vamos
omitir o último parâmetro, pois tanto faz fazermos no sentido horário ou
anti-horário (já que vamos começar e finalizar no mesmo ponto):

✴✴ ❈✐r❝✉♥❢❡rê♥❝✐❛ ❝♦♠♣❧❡t❛
❝♦♥t❡①t✳❜❡❣✐♥P❛t❤✭✮❀
❝♦♥t❡①t✳❛r❝✭✷✺✵✱ ✺✵✱ ✹✵✱ ✵✱ ✷✯▼❛t❤✳P■✮❀
❝♦♥t❡①t✳❢✐❧❧✭✮❀
❝♦♥t❡①t✳str♦❦❡✭✮❀

     Pronto! Temos os seguintes desenhos na página:




Figura 1.9: Arco em sentido anti-horário, arco em sentido horário e circun-
ferência completa, com preenchimento e contorno



Desenhando imagens
    Se você já está ficando preocupado, pensando se todos os gráficos em um
jogo são criados via programação, eu tenho uma boa notícia para você: não


14


[PAGINA 22]
Casa do Código                                         Capítulo 1. Fundamentos



são. A grande maioria vem de imagens já prontas, elaboradas em programas
gráficos.
    Para desenhar imagens pré-elaboradas em um Canvas, primeiro temos de
carregar o arquivo de imagem. O objeto Image do JavaScript é equivalente a
um elemento <img> na página, porém somente em memória. Após criá-lo,
apontamos seu atributo src para o arquivo desejado:

✴✴ ❊①❡♠♣❧♦ t❡ór✐❝♦

✴✴ ❈❛rr❡❣❛♥❞♦ ✉♠❛ ✐♠❛❣❡♠ ♣r♦❣r❛♠❛t✐❝❛♠❡♥t❡
✈❛r ✐♠❛❣❡♠ ❂ ♥❡✇ ■♠❛❣❡✭✮❀
✐♠❛❣❡♠✳sr❝ ❂ ✬♠✐♥❤❛✲✐♠❛❣❡♠✳♣♥❣✬❀ ✴✴ ❣✐❢✱ ❥♣❣✳✳✳

✴✴ ❖❜t❡♥❞♦ ❞❡ ✉♠❛ ✐♠❛❣❡♠ ♥❛ ♣á❣✐♥❛
✈❛r ✐♠❛❣❡♠ ❂ ❞♦❝✉♠❡♥t✳❣❡t❊❧❡♠❡♥t❇②■❞✭✬✐❞❴❞❛❴t❛❣❴✐♠❣✬✮❀

   Convém aguardar a imagem ser carregada antes de desenhá-la. O objeto
Image possui o evento onload, que será disparado automaticamente pelo
browser quando o carregamento estiver completo:

✴✴ ❊①❡♠♣❧♦ t❡ór✐❝♦
✐♠❛❣❡♠✳♦♥❧♦❛❞ ❂ ❢✉♥❝t✐♦♥✭✮ ④
   ✴✴ ❆q✉✐ tr❛❜❛❧❤❛♠♦s ❝♦♠ ❛ ✐♠❛❣❡♠
⑥

    Estando carregada, a imagem pode ser desenhada através do método
drawImage do context. Este método pode ser chamado de duas formas:

    • drawImage(imagem, x, y, largura, altura): desenha a im-
      agem inteira, na posição e tamanho especificados;

    • drawImage(imagem, xOrigem, yOrigem, larguraOrigem,
      alturaOrigem, xDestino, yDestino, larguraDestino,
      alturaDestino): desenha parte da imagem.

    Vamos experimentar a primeira forma. No pacote de download, na pasta
deste capítulo ( 01), está presente uma subpasta de nome img, contendo
o arquivo ovni.png. Este será posteriormente o inimigo que a nave irá

                                                                           15


[PAGINA 23]
1.2. Começando a desenhar                                   Casa do Código


enfrentar em nosso jogo. A imagem possui 64 pixels de largura por 32 de
altura (64x32). Vamos criar uma página com um Canvas e carregá-la:
❁✦✲✲ ❛rq✉✐✈♦✿ ✐♠❛❣❡♥s✲✶✳❤t♠❧ ✲✲❃
❁❝❛♥✈❛s ✐❞❂✧♠❡✉❴❝❛♥✈❛s✧ ✇✐❞t❤❂✧✺✵✵✧ ❤❡✐❣❤t❂✧✶✵✵✧❃❁✴❝❛♥✈❛s❃
❁s❝r✐♣t❃
   ✴✴ ❈❛♥✈❛s ❡ ❝♦♥t❡①t♦
   ✈❛r ❝❛♥✈❛s ❂ ❞♦❝✉♠❡♥t✳❣❡t❊❧❡♠❡♥t❇②■❞✭✬♠❡✉❴❝❛♥✈❛s✬✮❀
   ✈❛r ❝♦♥t❡①t ❂ ❝❛♥✈❛s✳❣❡t❈♦♥t❡①t✭✬✷❞✬✮❀

   ✴✴ ❈❛rr❡❣❛r ❛ ✐♠❛❣❡♠
   ✈❛r ✐♠❛❣❡♠ ❂ ♥❡✇ ■♠❛❣❡✭✮❀
   ✐♠❛❣❡♠✳sr❝ ❂ ✬✐♠❣✴♦✈♥✐✳♣♥❣✬❀
   ✐♠❛❣❡♠✳♦♥❧♦❛❞ ❂ ❢✉♥❝t✐♦♥✭✮ ④
      ✴✴ ❆q✉✐ ✉s❛r❡♠♦s ❞r❛✇■♠❛❣❡
   ⑥
❁✴s❝r✐♣t❃

    No evento onload, fazemos um loop para desenhar cinco OVNIs, um
ao lado do outro. A variável x indica a posição de cada desenho:
✐♠❛❣❡♠✳♦♥❧♦❛❞ ❂ ❢✉♥❝t✐♦♥✭✮ ④
   ✴✴ ❈♦♠❡ç❛r ♥❛ ♣♦s✐çã♦ ✷✵
   ✈❛r ① ❂ ✷✵❀

     ✴✴ ❉❡s❡♥❤❛r ❛s ✐♠❛❣❡♥s
     ❢♦r ✭✈❛r ✐ ❂ ✶❀ ✐ ❁❂ ✺❀ ✐✰✰✮ ④
        ❝♦♥t❡①t✳❞r❛✇■♠❛❣❡✭✐♠❛❣❡♠✱ ①✱ ✷✵✱ ✻✹✱ ✸✷✮❀
        ① ✰❂ ✼✵❀
     ⑥
⑥




                Figura 1.10: Desenhando imagens com drawImage


16


[PAGINA 24]
Casa do Código                                            Capítulo 1. Fundamentos



  Se quiséssemos desenhar as imagens ampliadas ou reduzidas, bastaria
modificar a largura e a altura:

✴✴ ❘❡❞✉③✐♥❞♦ ♣❛r❛ ♠❡t❛❞❡ ❞♦ t❛♠❛♥❤♦
❝♦♥t❡①t✳❞r❛✇■♠❛❣❡✭✐♠❛❣❡♠✱ ①✱ ✷✵✱ ✸✷✱ ✶✻✮❀

✴✴ ❆♠♣❧✐❛♥❞♦ ♣❛r❛ ♦ ❞♦❜r♦ ❞♦ t❛♠❛♥❤♦
❝♦♥t❡①t✳❞r❛✇■♠❛❣❡✭✐♠❛❣❡♠✱ ①✱ ✷✵✱ ✶✷✽✱ ✻✹✮❀

    Vamos experimentar a segunda forma, a que recebe oito valores! Na pasta
img, temos o arquivo explosao.png, que também será usado no jogo.
Esta imagem contém uma sequência de animação (spritesheet), da qual de-
senhamos uma parte por vez:




                 Figura 1.11: Explosão usada no jogo do livro


    A técnica de clipping consite em selecionar uma área da imagem original
para ser desenhada:




   Figura 1.12: Selecionando uma área da imagem para recorte (clipping)


    Os quatro primeiros valores passados ao drawImage indicam o retân-
gulo da área enquadrada; os outros quatro representam a posição e o tamanho
do desenho no Canvas:

                                                                              17


[PAGINA 25]
1.2. Começando a desenhar                                         Casa do Código


❁✦✲✲ ❛rq✉✐✈♦✿ ✐♠❛❣❡♥s✲✷✳❤t♠❧ ✲✲❃
❁❝❛♥✈❛s ✐❞❂✧♠❡✉❴❝❛♥✈❛s✧ ✇✐❞t❤❂✧✸✵✵✧ ❤❡✐❣❤t❂✧✸✵✵✧❃❁✴❝❛♥✈❛s❃
❁s❝r✐♣t❃
   ✴✴ ❈❛♥✈❛s ❡ ❝♦♥t❡①t♦
   ✈❛r ❝❛♥✈❛s ❂ ❞♦❝✉♠❡♥t✳❣❡t❊❧❡♠❡♥t❇②■❞✭✬♠❡✉❴❝❛♥✈❛s✬✮❀
   ✈❛r ❝♦♥t❡①t ❂ ❝❛♥✈❛s✳❣❡t❈♦♥t❡①t✭✬✷❞✬✮❀

   ✴✴ ❈❛rr❡❣❛r ❛ ✐♠❛❣❡♠
   ✈❛r ✐♠❛❣❡♠ ❂ ♥❡✇ ■♠❛❣❡✭✮❀
   ✐♠❛❣❡♠✳sr❝ ❂ ✬✐♠❣✴❡①♣❧♦s❛♦✳♣♥❣✬❀
   ✐♠❛❣❡♠✳♦♥❧♦❛❞ ❂ ❢✉♥❝t✐♦♥✭✮ ④
      ❝♦♥t❡①t✳❞r❛✇■♠❛❣❡✭
         ✐♠❛❣❡♠✱
         ✽✵✱ ✶✵✱ ✻✵✱ ✻✺✱ ✴✴ ➪r❡❛ ❞❡ r❡❝♦rt❡ ✭❝❧✐♣♣✐♥❣✮
         ✷✵✱ ✷✵✱ ✻✵✱ ✻✺   ✴✴ ❉❡s❡♥❤♦ ♥♦ ❈❛♥✈❛s
      ✮❀
   ⑥
❁✴s❝r✐♣t❃




                   Figura 1.13: Resultado do clipping no Canvas


     No capítulo 4, faremos uso intensivo do clipping para criar animações.

Métodos save e restore
    Um recurso do context que considero de extrema importância é poder
facilmente guardar configurações e retornar a elas mais tarde. É uma exce-
lente prática que cada função ou método guarde as configurações atuais e as
restaure antes de retornar. Desta forma, um não afeta o trabalho do outro!
    Mas já imaginou ter que salvar cada propriedade em uma variável?

18


[PAGINA 26]
Casa do Código                                           Capítulo 1. Fundamentos



✴✴ ❊①❡♠♣❧♦ t❡ór✐❝♦
✴✴ ◆ã♦ ❢❛ç❛ ✐st♦✦
❢✉♥❝t✐♦♥ ❞❡s❡♥❤❛r◗✉❛❧q✉❡r❈♦✐s❛✭✮ ④
   ✴✴ ●✉❛r❞♦ ❛s ❝♦♥❢✐❣✉r❛çõ❡s
   ✈❛r ❢✐❧❧❆♥t❡r✐♦r ❂ ❝♦♥t❡①t✳❢✐❧❧❙t②❧❡❀ ✴✴ str♦❦❡❙t②❧❡✱ ❡t❝✳

    ✴✴ ▼♦❞✐❢✐❝♦ ❝♦♥❢♦r♠❡ ♣r❡❝✐s♦
    ❝♦♥t❡①t✳❢✐❧❧❙t②❧❡ ❂ ✬♣✐♥❦✬❀

    ✴✴ ❉❡s❡♥❤♦
    ✴✴ ✳✳✳

    ✴✴ ❉❡✈♦❧✈♦ ❛s ❝♦♥❢✐❣✉r❛çõ❡s ❛♥t❡r✐♦r❡s
    ❝♦♥t❡①t✳❢✐❧❧❙t②❧❡ ❂ ❢✐❧❧❆♥t❡r✐♦r❀
⑥

    Para nossa sorte, o context possui o método save. Este método em-
pilha configurações, fazendo uma cópia de todas as configurações atuais para
o próximo nível. Pense em cada nível como um “andar” nessa pilha. Nós sem-
pre trabalhamos no nível mais alto, de modo que configurações que ficaram
em níveis inferiores permanecem inalteradas:




             Figura 1.14: Método save empilhando configurações


   Quando queremos retornar às configurações anteriores, chamamos o
método restore. Ele volta para o nível imediatamente abaixo:




                                                                             19


[PAGINA 27]
1.2. Começando a desenhar                                       Casa do Código




        Figura 1.15: Voltando para configurações anteriores com restore


    Como exemplo prático, começamos desenhando um quadrado verde. Em
seguida, subimos na pilha com save e fazemos um quadrado roxo. Depois
que retornamos com restore, nossa cor atual passa a ser o verde nova-
mente:

❁✦✲✲ ❛rq✉✐✈♦✿ s❛✈❡✲❡✲r❡st♦r❡✳❤t♠❧ ✲✲❃
❁❝❛♥✈❛s ✐❞❂✧♠❡✉❴❝❛♥✈❛s✧ ✇✐❞t❤❂✧✷✵✵✧ ❤❡✐❣❤t❂✧✷✵✵✧❃❁✴❝❛♥✈❛s❃
❁s❝r✐♣t❃
   ✴✴ ❈❛♥✈❛s ❡ ❝♦♥t❡①t♦
   ✈❛r ❝❛♥✈❛s ❂ ❞♦❝✉♠❡♥t✳❣❡t❊❧❡♠❡♥t❇②■❞✭✬♠❡✉❴❝❛♥✈❛s✬✮❀
   ✈❛r ❝♦♥t❡①t ❂ ❝❛♥✈❛s✳❣❡t❈♦♥t❡①t✭✬✷❞✬✮❀

     ✴✴ ❯♠ ♣❡q✉❡♥♦ q✉❛❞r❛❞♦ ✈❡r❞❡
     ❝♦♥t❡①t✳❢✐❧❧❙t②❧❡ ❂ ✬❣r❡❡♥✬❀
     ❝♦♥t❡①t✳❢✐❧❧❘❡❝t✭✺✵✱ ✺✵✱ ✷✺✱ ✷✺✮❀

     ✴✴ ❙❛❧✈❛♠♦s ❛ ❝♦♥❢✐❣✉r❛çã♦ ❡ s✉❜✐♠♦s ♥❛ ♣✐❧❤❛
     ❝♦♥t❡①t✳s❛✈❡✭✮❀

     ✴✴ ❆❣♦r❛ ✉♠ q✉❛❞r❛❞♦ r♦①♦
     ❝♦♥t❡①t✳❢✐❧❧❙t②❧❡ ❂ ✬♣✉r♣❧❡✬❀
     ❝♦♥t❡①t✳❢✐❧❧❘❡❝t✭✶✵✵✱ ✺✵✱ ✷✺✱ ✷✺✮❀

     ✴✴ ❱♦❧t❛♠♦s ♣❛r❛ ♦ ♥í✈❡❧ ❛♥t❡r✐♦r ♥❛ ♣✐❧❤❛
     ❝♦♥t❡①t✳r❡st♦r❡✭✮❀

     ✴✴ ❱♦❧t♦✉ ♣❛r❛ ♦ ✈❡r❞❡✦

20


[PAGINA 28]
Casa do Código                                            Capítulo 1. Fundamentos



   ❝♦♥t❡①t✳❢✐❧❧❘❡❝t✭✶✺✵✱ ✺✵✱ ✷✺✱ ✷✺✮❀
❁✴s❝r✐♣t❃




Figura 1.16: Salvamos a cor verde na pilha (save), mudamos para roxo e volta-
mos para o verde (restore)



  Referências sobre o Canvas

     Neste tópico, não quis nem de longe esgotar os recursos do Canvas,
  mas dar uma base para iniciarmos o desenvolvimento de jogos. Indico-
  lhe algumas referências para você aprimorar seus conhecimentos e ter
  ideias, muitas ideias, para implementar em seus jogos:

      • W3Schools[3] (http://www.w3schools.com/tags/ref_canvas.asp) :
        recomendo todos os tutoriais deles, por serem simples e por você
        poder rodar os exemplos na hora;

      • Core HTML5 Canvas[1] (http://corehtml5canvas.com) : excelente
        livro de David Geary, bem aprofundado, foi a minha principal
        fonte para aprender sobre o Canvas. O autor discute não somente
        os recursos da ferramenta, mas técnicas e algoritmos extrema-
        mente avançados e úteis para jogos;

      • HTML5 2D game development: Introducing Snail Bait[2] (http:
        //goo.gl/Ojvi9T - URL encurtada): do mesmo autor do Core
        HTML5 Canvas, este é o primeiro de uma série de artigos na qual
        somos guiados na criação de um jogo de plataforma.




                                                                              21


[PAGINA 29]
1.3. Animações com requestAnimationFrame                        Casa do Código


1.3     Animações com requestAnimationFrame
Tradicionalmente, quando queremos executar tarefas periódicas
em páginas web, usamos os métodos                window.setTimeout ou
window.setInterval, passando a função desejada e o intervalo em
milissegundos. Os resultados são satisfatórios para tarefas simples, no
entanto, o controle do tempo pelo browser não é totalmente preciso. É
preciso lembrar que os sistemas operacionais modernos são multitarefa, e
mesmo os browsers podem ter várias guias abertas. Não é possível garantir
que a CPU esteja sempre disponível no momento exato desejado, portanto o
intervalo informado sempre será aproximado.
    A solução para jogos e outras aplicações que requerem animações mais
precisas é trabalhar com ciclos mais curtos, aproveitando cada momento em
que a CPU está disponível para nosso aplicativo, e nesse momento fazer
o cálculo do tempo. Para isso, a especificação do HTML5 traz o método
window.requestAnimationFrame, que delega para o browser a tarefa de
executar sua animação o mais rápido possível, assim que os recursos do sis-
tema estiverem disponíveis. Para este método, passamos como parâmetro a
função que fará os desenhos no Canvas. Temos que chamá-lo de forma cíclica,
uma vez após a outra, da mesma forma que faríamos caso usássemos o con-
hecido setTimeout:
✴✴ ❊①❡♠♣❧♦ t❡ór✐❝♦

✴✴ ❙♦❧✐❝✐t♦ ❛ ❡①❡❝✉çã♦ ❞❡ ✉♠❛ ❢✉♥çã♦
✴✴ ◆ã♦ é ♣r❡❝✐s♦ q✉❛❧✐❢✐❝❛r ♦ ✧✇✐♥❞♦✇✧ ✿❉
r❡q✉❡st❆♥✐♠❛t✐♦♥❋r❛♠❡✭♠✐♥❤❛❋✉♥❝❛♦✮❀

✴✴ ❋✉♥çã♦ ❞❡ ❛♥✐♠❛çã♦
❢✉♥❝t✐♦♥ ♠✐♥❤❛❋✉♥❝❛♦✭✮ ④
   ✴✴ ❋❛ç♦ ✉♠ ❞❡s❡♥❤♦ q✉❛❧q✉❡r
   ✴✴ ✳✳✳

      ✴✴ ❙♦❧✐❝✐t♦ ♦ ♣ró①✐♠♦ ❝✐❝❧♦
      r❡q✉❡st❆♥✐♠❛t✐♦♥❋r❛♠❡✭♠✐♥❤❛❋✉♥❝❛♦✮❀
⑥

      Para demonstrar na prática, façamos uma bolinha se deslocando pela tela.

22


[PAGINA 30]
Casa do Código                                          Capítulo 1. Fundamentos



Obtemos as referências do Canvas e do contexto gráfico, definimos a posição
inicial da bola e seu raio e, em seguida, mandamos uma animação iniciar,
chamando a função mexerBola:

❁✦✲✲ ❛rq✉✐✈♦✿ r❡q✉❡st❛♥✐♠❛t✐♦♥❢r❛♠❡✳❤t♠❧ ✲✲❃
❁❝❛♥✈❛s ✐❞❂✧♠❡✉❴❝❛♥✈❛s✧ ✇✐❞t❤❂✧✸✵✵✧ ❤❡✐❣❤t❂✧✸✵✵✧❃❁✴❝❛♥✈❛s❃
❁s❝r✐♣t❃
   ✴✴ ❈❛♥✈❛s ❡ ❝♦♥t❡①t♦
   ❝❛♥✈❛s ❂ ❞♦❝✉♠❡♥t✳❣❡t❊❧❡♠❡♥t❇②■❞✭✬♠❡✉❴❝❛♥✈❛s✬✮❀
   ❝♦♥t❡①t ❂ ❝❛♥✈❛s✳❣❡t❈♦♥t❡①t✭✬✷❞✬✮❀

   ✴✴ ❉❛❞♦s ❞❛ ❜♦❧❛
   ✈❛r ① ❂ ✷✵❀
   ✈❛r ② ❂ ✶✵✵❀
   ✈❛r r❛✐♦ ❂ ✺❀

   ✴✴ ■♥✐❝✐❛r ❛ ❛♥✐♠❛çã♦
   r❡q✉❡st❆♥✐♠❛t✐♦♥❋r❛♠❡✭♠❡①❡r❇♦❧❛✮❀

   ✴✴ ❋✉♥çã♦ ❞❡ ❛♥✐♠❛çã♦
   ❢✉♥❝t✐♦♥ ♠❡①❡r❇♦❧❛✭✮ ④
      ✴✴ ❆q✉✐ ✉♠❛ ❜♦❧✐♥❤❛ s❡ ❞❡s❧♦❝❛rá
   ⑥
❁✴s❝r✐♣t❃

    Nessa função, primeiro limpamos o Canvas com o método clearRect
do contexto, que serve para limpar uma área (equivale a desenhar um retân-
gulo branco). Fazemos isso para apagar rastros anteriores da bolinha. Em
seguida, nós a desenhamos em sua posição atual, alteramos sua posição x e
solicitamos a execução do próximo ciclo de animação:

❢✉♥❝t✐♦♥ ♠❡①❡r❇♦❧❛✭✮ ④
   ✴✴ ▲✐♠♣❛r ♦ ❈❛♥✈❛s
   ❝♦♥t❡①t✳❝❧❡❛r❘❡❝t✭✵✱ ✵✱ ❝❛♥✈❛s✳✇✐❞t❤✱ ❝❛♥✈❛s✳❤❡✐❣❤t✮❀

   ✴✴ ❉❡s❡♥❤❛r ❛ ❜♦❧❛
   ❝♦♥t❡①t✳❜❡❣✐♥P❛t❤✭✮❀
   ❝♦♥t❡①t✳❛r❝✭①✱ ②✱ r❛✐♦✱ ✵✱ ▼❛t❤✳P■✯✷✮❀
   ❝♦♥t❡①t✳❢✐❧❧✭✮❀

                                                                            23


[PAGINA 31]
1.3. Animações com requestAnimationFrame                          Casa do Código




     ✴✴ ❉❡s❧♦❝❛r ✷✵ ♣✐①❡❧s ♣❛r❛ ❛ ❞✐r❡✐t❛
     ① ✰❂ ✷✵❀

     ✴✴ ❈❤❛♠❛r ♦ ♣ró①✐♠♦ ❝✐❝❧♦ ❞❛ ❛♥✐♠❛çã♦
     r❡q✉❡st❆♥✐♠❛t✐♦♥❋r❛♠❡✭♠❡①❡r❇♦❧❛✮❀
⑥

     Faça experiências! Você pode:

     • mexer para a direita: some um valor a x (veja a figura 1.2);

     • mexer para a esquerda: subtraia um valor de x;

     • mexer para baixo: some um valor a y;

     • mexer para cima: subtraia um valor de y;

     • mexer na diagonal: altere as posições tanto de x quanto de y. Você
       pode somar ou subtrair, usar valores diferentes para cada um etc.

Controlando o tempo da animação
     Repare que a bolinha anda bem depressa.            Isto ocorre porque o
requestAnimationFrame trabalha com ciclos curtos, aproveitando o
primeiro momento em que a CPU e o browser puderem executar o processa-
mento da função de animação.
    Podemos ler o relógio do computador em cada ciclo para controlar o
movimento da bolinha. Sabemos que o JavaScript possui o objeto Date, que
obtém a data e a hora atuais, e que esse objeto possui o método getTime(),
que devolve esse instante exato em milissegundos. Para saber quanto tempo
demorou entre um ciclo e outro (lembre-se de que esse tempo é sempre var-
iável), bastaria tirar a diferença entre o instante atual e o anterior. Sabendo o
intervalo decorrido, é possível calcular quanto a bola deve se deslocar nesse
tempo:

✴✴ ❊①❡♠♣❧♦ t❡ór✐❝♦

✴✴ ❖❜t❡r ♦ ✐♥st❛♥t❡ ❛t✉❛❧

24


[PAGINA 32]
Casa do Código                                            Capítulo 1. Fundamentos



✈❛r ❛❣♦r❛ ❂ ♥❡✇ ❉❛t❡✭✮✳❣❡t❚✐♠❡✭✮❀

✴✴ ❖ ✐♥st❛♥t❡ ❛♥t❡r✐♦r t❡♠ ❞❡ t❡r s✐❞♦ ♣r❡s❡r✈❛❞♦ ❛♥t❡r✐♦r♠❡♥t❡
✈❛r ❛♥t❡r✐♦r ❂ ❛❣♦r❛❀ ✴✴ ❋♦✐ ❢❡✐t♦ ❛♥t❡s

✴✴ ❚❡♠♣♦ ❞❡❝♦rr✐❞♦ ❂ ❞✐❢❡r❡♥ç❛
✈❛r ❞❡❝♦rr✐❞♦ ❂ ❛❣♦r❛ ✲ ❛♥t❡r✐♦r❀

✴✴ ❉❡s❧♦❝❛♠❡♥t♦ ❞❛ ❜♦❧✐♥❤❛
✈❛r ✈❡❧♦❝✐❞❛❞❡ ❂ ✷✵❀ ✴✴ ❊♠ ♣✐①❡❧s ♣♦r s❡❣✉♥❞♦
① ✰❂ ✈❡❧♦❝✐❞❛❞❡ ✯ ❞❡❝♦rr✐❞♦ ✴ ✶✵✵✵❀

    Vamos colocar isto em prática. Primeiro, guarde o momento inicial antes
de chamar a função de animação pela primeira vez:
✴✴ ▼♦♠❡♥t♦ ✐♥✐❝✐❛❧
✈❛r ❛♥t❡r✐♦r ❂ ♥❡✇ ❉❛t❡✭✮✳❣❡t❚✐♠❡✭✮❀

✴✴ ■♥✐❝✐❛r ❛ ❛♥✐♠❛çã♦
r❡q✉❡st❆♥✐♠❛t✐♦♥❋r❛♠❡✭♠❡①❡r❇♦❧❛✮❀

✴✴ ❋✉♥çã♦ ❞❡ ❛♥✐♠❛çã♦
❢✉♥❝t✐♦♥ ♠❡①❡r❇♦❧❛✭✮ ④
   ✴✴ ✳✳✳
⑥

    No início da função, obtenha o instante atual e calcule o tempo decorrido
entre eles:
❢✉♥❝t✐♦♥ ♠❡①❡r❇♦❧❛✭✮ ④
   ✴✴ ▼♦♠❡♥t♦ ❛t✉❛❧
   ✈❛r ❛❣♦r❛ ❂ ♥❡✇ ❉❛t❡✭✮✳❣❡t❚✐♠❡✭✮❀

    ✴✴ ❉✐❢❡r❡♥ç❛
    ✈❛r ❞❡❝♦rr✐❞♦ ❂ ❛❣♦r❛ ✲ ❛♥t❡r✐♦r❀

    ✴✴ ✳✳✳
⑥

    Ao final da função, antes de chamar o próximo ciclo, guarde o momento
do ciclo anterior:

                                                                              25


[PAGINA 33]
1.4. Orientação a objetos com JavaScript                      Casa do Código


❢✉♥❝t✐♦♥ ♠❡①❡r❇♦❧❛✭✮ ④
   ✴✴ ✳✳✳

     ✴✴ ●✉❛r❞❛♠♦s ♦ ✐♥st❛♥t❡ ♣❛r❛ ♦ ♣ró①✐♠♦ ❝✐❝❧♦
     ❛♥t❡r✐♦r ❂ ❛❣♦r❛❀
     r❡q✉❡st❆♥✐♠❛t✐♦♥❋r❛♠❡✭♠❡①❡r❇♦❧❛✮❀
⑥

   Agora podemos calcular o desclocamento da bola! Apague a linha que
aumenta x em 20 pixels:

✴✴ ❆♣❛❣✉❡ ❡st❛ ❧✐♥❤❛
✴✴ ❉❡s❧♦❝❛r ✷✵ ♣✐①❡❧s ♣❛r❛ ❛ ❞✐r❡✐t❛
① ✰❂ ✷✵❀

    No lugar, calcule o deslocamento a partir da velocidade de 20 pixels por
segundo (ou outra que preferir):

✴✴ ❉❡s❧♦❝❛r ✷✵ ♣✐①❡❧s ♣♦r s❡❣✉♥❞♦
✈❛r ✈❡❧♦❝✐❞❛❞❡ ❂ ✷✵❀
① ✰❂ ✈❡❧♦❝✐❞❛❞❡ ✯ ❞❡❝♦rr✐❞♦ ✴ ✶✵✵✵❀

    A bola agora move-se mais lentamente, pois agora estamos trabalhando
com pixels por segundo (antes eram 20 pixels por ciclo, e tínhamos inúmeros
ciclos em um segundo). Para fazê-la mover-se mais rápido, basta aumentar o
valor.


1.4 Orientação a objetos com JavaScript

Conceitos básicos
Não é intenção deste livro ensinar a teoria da orientação a objetos (O.O.),
mas vou dar-lhe uma base para podermos usá-la com JavaScript. Esta não
é uma linguagem puramente O.O., no entanto, o jogo que criaremos, está
projetado dessa forma. Diferenciamos aqui projeto orientado a objetos (apli-
cado em nosso jogo) de linguagem orientada a objetos, que dá suporte total
ao paradigma (não é o caso do JavaScript).

26


[PAGINA 34]
Casa do Código                                                Capítulo 1. Fundamentos



     Imagine um jogo de carros de corrida. Todos os carros são padronizados
nas suas características, embora elas possam variar (dentro desse padrão).
Por exemplo, todos os carros possuem cor, velocidade máxima e velocidade
atual. Contudo, em um dado momento, cada carro possui valores diferentes
para estas características. O carro do jogador é vermelho, está a 150km/h e
pode alcançar até 200km/h. Seu rival é azul, está a 170km/h e pode alcançar
até 220km/h. As características que definem um carro no jogo são as mesmas,
mas cada uma está preenchida com valores diferentes para cada carro.
     Esse conjunto de características comuns a todo carro é o que chamamos
de classe. Quando falamos carro, referindo-nos a carros em geral, estamos
falando de uma classe. A classe é o molde para a criação de objetos.
     Cada carro é uma instância da classe. A instância é o objeto em si, um
objeto que pertence a uma classe. Quando falo do meu carro, estou falando de
uma instância específica da classe carro. O carro do vizinho é outra instância.
     Cor, velocidade atual e velocidade máxima são os atributos da classe, ou
seja, todas as instâncias os têm, mas cada uma possui valores próprios para
esses atributos.
     Cada carro executa as tarefas de acelerar, frear e virar. Estas tarefas são os
métodos. Em programas orientados a objeto, é nos métodos que escrevemos
os códigos que realizam as tarefas fundamentais do programa. Eles trabalham
com os dados nos atributos e podem alterar o estado do objeto.


  Resumo de conceitos básicos de O.O.



      • Classe: um tipo de objetos determinado, composto por atributos
        e métodos definidos;

      • Instância: cada objeto pertencente a uma determinada classe;

      • Atributo: cada propriedade dos objetos listada em uma classe;

      • Método: cada tarefa que um objeto de uma classe pode executar.



                                                                                  27


[PAGINA 35]
1.4. Orientação a objetos com JavaScript                     Casa do Código


Funções construtoras
    Em linguagens O.O., como Java e C#, definimos classes explicitamente
(usando a palavra-chave class). Em JavaScript não há classes, mas pode-
mos usar funções construtoras para criar os objetos seguindo as classes que
projetamos.
    Uma função construtora é uma função normal do JavaScript, porém us-
ada com o propósito de criar objetos. No exemplo a seguir, a palavra-chave
this recebe os atributos de um carro. A palavra cor, sozinha, se refere ao
parâmetro recebido pela função, mas a construção this.cor cria um atrib-
uto cor no objeto:

❁✦✲✲ ❛rq✉✐✈♦✿ ♦r✐❡♥t❛❝❛♦✲♦❜❥❡t♦s✳❤t♠❧ ✲✲❃
❁❜♦❞②❃
   ❁s❝r✐♣t❃
      ❢✉♥❝t✐♦♥ ❈❛rr♦✭❝♦r✱ ✈❡❧♦❝▼❛①✐♠❛✮ ④
         t❤✐s✳❝♦r ❂ ❝♦r❀
         t❤✐s✳✈❡❧♦❝▼❛①✐♠❛ ❂ ✈❡❧♦❝▼❛①✐♠❛❀
         t❤✐s✳✈❡❧♦❝❆t✉❛❧ ❂ ✵❀
      ⑥

      ✴✴ ❝♦♥t✐♥✉❛✳✳✳
   ❁✴s❝r✐♣t❃
❁✴❜♦❞②❃

     Nós não podemos criar um carro simplesmente chamando:

✴✴ ❊①❡♠♣❧♦ t❡ór✐❝♦
✴✴ ◆ã♦ ❢❛ç❛ ✐st♦✿
❈❛rr♦✭✬✈❡r❞❡✬✱ ✸✵✵✮❀

    Quando chamamos uma função sem qualificar um objeto, o JavaScript
entende que estamos usando o objeto window. Assim, a palavra this no
corpo da função criará ou modificará os atributos neste objeto.
    Para criar novos objetos temos de usar a palavra-chave new. Após a
função construtora, crie as variáveis meuCarro e oponente para referen-
ciar os novos objetos:


28


[PAGINA 36]
Casa do Código                                         Capítulo 1. Fundamentos



✴✴ ■♥st❛♥❝✐❛♥❞♦ ♦❜❥❡t♦s ❞❛ ❝❧❛ss❡ ❈❛rr♦
✈❛r ♠❡✉❈❛rr♦ ❂ ♥❡✇ ❈❛rr♦✭✬✈❡r♠❡❧❤♦✬✱ ✷✺✵✮❀
✈❛r ♦♣♦♥❡♥t❡ ❂ ♥❡✇ ❈❛rr♦✭✬❛③✉❧✬✱ ✸✵✵✮❀

    A expressão new Carro('vermelho', 250) cria um novo objeto e
executa nele a função construtora. Agora a palavra this se referirá a esse
objeto!
    Já os métodos, em JavaScript, são apenas atributos que referenciam
funções. Podemos, por exemplo, criar um método acelerar que aumenta
em 10 unidades a velocidade do carro:

❢✉♥❝t✐♦♥ ❈❛rr♦✭❝♦r✱ ✈❡❧♦❝▼❛①✐♠❛✮ ④
   ✴✴ ❈r✐❛♥❞♦ ♦s ❛tr✐❜✉t♦s
   t❤✐s✳❝♦r ❂ ❝♦r❀
   t❤✐s✳✈❡❧♦❝▼❛①✐♠❛ ❂ ✈❡❧♦❝▼❛①✐♠❛❀
   t❤✐s✳✈❡❧♦❝❆t✉❛❧ ❂ ✵❀

    ✴✴ ❈r✐❛♥❞♦ ✉♠ ♠ét♦❞♦
    t❤✐s✳❛❝❡❧❡r❛r ❂ ❢✉♥❝t✐♦♥✭✮ ④
       t❤✐s✳✈❡❧♦❝❆t✉❛❧ ✰❂ ✶✵❀
    ⑥
⑥

✴✴ ✳✳✳

     Chamando o método acelerar através da variável meuCarro criada
anteriormente, esse método vai alterar o atributo velocAtual dessa instân-
cia, e não da instância oponente:

✴✴ ❈❤❛♠❛♥❞♦ ✉♠ ♠ét♦❞♦ s♦♠❡♥t❡ ❡♠ ✉♠ ♦❜❥❡t♦
♠❡✉❈❛rr♦✳❛❝❡❧❡r❛r✭✮❀

   Por último, mande exibir as velocidades dos dois carros criados. O
primeiro acelerou, e o outro não!

✴✴ ❱❡r✐❢✐❝❛♥❞♦ ❛s ✈❡❧♦❝✐❞❛❞❡s
❞♦❝✉♠❡♥t✳✇r✐t❡✭♠❡✉❈❛rr♦✳❝♦r ✰ ✬✿ ✬ ✰ ♠❡✉❈❛rr♦✳✈❡❧♦❝❆t✉❛❧✮❀
❞♦❝✉♠❡♥t✳✇r✐t❡✭✬❁❜r❃✬✮❀
❞♦❝✉♠❡♥t✳✇r✐t❡✭♦♣♦♥❡♥t❡✳❝♦r ✰ ✬✿ ✬ ✰ ♦♣♦♥❡♥t❡✳✈❡❧♦❝❆t✉❛❧✮❀

                                                                           29


[PAGINA 37]
1.4. Orientação a objetos com JavaScript                         Casa do Código


     A saída desse código é:

✈❡r♠❡❧❤♦✿ ✶✵
❛③✉❧✿ ✵


    Sintaxe de ponto e de colchetes

       Para referenciarmos atributos de um objeto em JavaScript, o mais
    usual é usarmos a sintaxe de ponto, ou seja, usar um ponto entre o nome
    do objeto e do atributo:

    ♠❡✉❖❜❥❡t♦✳❛tr✐❜✉t♦

        Também é possível usar a sintaxe de colchetes, na qual podemos usar
    strings para representar os atributos. O objeto torna-se uma espécie de
    array associativo, sendo que cada elemento (atributo) é associado a uma
    string específica, e não a um índice de posição:

    ♠❡✉❖❜❥❡t♦❬✬❛tr✐❜✉t♦✬❪




Objetos sem função construtora
     O JavaScript oferece a sintaxe de chaves ( { e }) para criar objetos:

✈❛r ♠❡✉❖❜❥❡t♦ ❂ ④
   ❛tr✐❜✉t♦✶✿ ✈❛❧♦r✱
   ❛tr✐❜✉t♦✷✿ ✈❛❧♦r✱
   ♠❡t♦❞♦✶✿ ❢✉♥❝t✐♦♥✭✮ ④

     ⑥✱
     ♠❡t♦❞♦✷✿ ❢✉♥❝t✐♦♥✭✮ ④

     ⑥
⑥

     Por exemplo, poderíamos criar um carro da seguinte forma:


30


[PAGINA 38]
Casa do Código                                             Capítulo 1. Fundamentos



✈❛r ♠❡✉❈❛rr♦ ❂ ④
   ❝♦r✿ ✬❛③✉❧✬✱
   ✈❡❧♦❝✐❞❛❞❡✿ ✵✱
   ❛❝❡❧❡r❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
      t❤✐s✳✈❡❧♦❝✐❞❛❞❡ ✰❂ ✶✵❀
   ⑥
⑥

    Nós usaremos essa forma algumas vezes no desenvolvimento do jogo.
Como, porém, seu projeto é orientado a objetos, pensando em classes, com
atributos e métodos definidos, daremos maior preferência às funções con-
strutoras.

O prototype (protótipo)
     Declarar métodos como funções anônimas dentro das construtoras tem
um preço: maior consumo de memória. Cada vez que executamos o constru-
tor, uma cópia da função anônima é criada na memória e cada instância terá
sua cópia não somente do atributo, mas também da função:

❢✉♥❝t✐♦♥ ❈❛rr♦✭❝♦r✱ ✈❡❧♦❝▼❛①✐♠❛✮ ④
   ✴✴ ✳✳✳

    ✴✴ ❈r✐❛♥❞♦ ♠ét♦❞♦ ❝♦♠ ❢✉♥çã♦ ❛♥ô♥✐♠❛
    t❤✐s✳❛❝❡❧❡r❛r ❂ ❢✉♥❝t✐♦♥✭✮ ④
       t❤✐s✳✈❡❧♦❝❆t✉❛❧ ✰❂ ✶✵❀
    ⑥
⑥

    Pensando nisso, o JavaScript traz o recurso do prototype (protótipo), que é
um objeto associado a uma função construtora. Colocando os métodos neste
objeto, todas as instâncias usarão as mesmas cópias de cada método.
    Vamos nos habituar a colocar a função construtora e o prototype de
uma classe em um arquivo separado, com extensão .js. A palavra-chave
prototype funciona como se fosse um atributo da função construtora:

✴✴ ❛rq✉✐✈♦✿ ❝❛rr♦✳❥s



                                                                               31


[PAGINA 39]
1.4. Orientação a objetos com JavaScript                     Casa do Código


✴✴ ❋✉♥çã♦ ❝♦♥str✉t♦r❛
❢✉♥❝t✐♦♥ ❈❛rr♦✭❝♦r✱ ✈❡❧♦❝▼❛①✐♠❛✮ ④
   t❤✐s✳❝♦r ❂ ❝♦r❀
   t❤✐s✳✈❡❧♦❝▼❛①✐♠❛ ❂ ✈❡❧♦❝▼❛①✐♠❛❀
   t❤✐s✳✈❡❧♦❝❆t✉❛❧ ❂ ✵❀
⑥

✴✴ Pr♦t♦t②♣❡ ❝♦♠ ♦s ♠ét♦❞♦s
❈❛rr♦✳♣r♦t♦t②♣❡ ❂ ④
   ❛❝❡❧❡r❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
      t❤✐s✳✈❡❧♦❝❆t✉❛❧ ✰❂ ✶✵❀
   ⑥
⑥

    Escrevemos um pouco mais de código, porém até ganhamos um pouco
mais de legibilidade e organização: conseguimos “enxugar” a função constru-
tora, e podemos ter o funcionamento completo de um carro em seu arquivo
específico — para isto servem as classes! Para utilizar essa classe em uma
página HTML, basta usar a tag <script> com o atributo src, referen-
ciando o arquivo carro.js:

❁✦✲✲ ❛rq✉✐✈♦ ♣r♦t♦t②♣❡✳❤t♠❧ ✲✲❃
❁✦❉❖❈❚❨P❊ ❤t♠❧❃
❁❤t♠❧❃

❁❤❡❛❞❃
   ❁t✐t❧❡❃❖ ♣r♦t♦t②♣❡❁✴t✐t❧❡❃
   ❁s❝r✐♣t sr❝❂✧❝❛rr♦✳❥s✧❃❁✴s❝r✐♣t❃
❁✴❤❡❛❞❃

❁❜♦❞②❃
   ❁s❝r✐♣t❃
      ✈❛r ♠❡✉❈❛rr♦ ❂ ♥❡✇ ❈❛rr♦✭✬✈❡r♠❡❧❤♦✬✱ ✷✺✵✮❀
      ♠❡✉❈❛rr♦✳❛❝❡❧❡r❛r✭✮❀
      ❞♦❝✉♠❡♥t✳✇r✐t❡✭♠❡✉❈❛rr♦✳❝♦r ✰ ✬✿ ✬ ✰ ♠❡✉❈❛rr♦✳✈❡❧♦❝❆t✉❛❧✮❀
   ❁✴s❝r✐♣t❃
❁✴❜♦❞②❃

❁✴❤t♠❧❃

32


[PAGINA 40]
Casa do Código                                          Capítulo 1. Fundamentos



    É isso! Com estes conceitos básicos bem fixados, vamos começar a apren-
der conceitos específicos de jogos. No próximo capítulo, vamos aprender uma
das bases de um jogo, que consiste no loop de animação e nos sprites.




                                                                            33


[PAGINA 41]


[PAGINA 42]
Capítulo 2

O loop de animação
2.1 Introdução e sprites
Chegou a hora de avançarmos um passo além de apenas desenhar no Canvas
e movimentar alguns objetos. Vamos desenvolver pequenos aplicativos e criar
pequenas peças que, em algum momento, irão se juntar e tomar a forma de
um jogo!
   Nossa abordagem será a seguinte:

    • Primeiro, sempre codificamos o “aplicativo principal”, que realiza um
      teste nas classes a serem criadas.

    Isso é importante para chegarmos a códigos claros e bem estruturados.
Ao desenvolver, sempre procuramos focar em um aspecto por momento e
abstrair (“deixar para lá”) os outros. O aplicativo de teste determina o que
esperamos de nossas classes.


[PAGINA 43]
2.1. Introdução e sprites                                      Casa do Código


      • Em seguida, codificamos as classes e tentamos fazê-las responder como
        queremos.

    Nessa etapa, sempre surgirão modificações na forma como planejamos
inicialmente, o que vemos como algo natural. Refatorações (mudanças na es-
trutura do código sem alterar seu comportamento) serão rotina para nós.


        Mais do que ensinar como se faz, pretendo apresentá-lo a uma forma
     de trabalhar que deixará o resultado muito mais claro e organizado no
     final. Você me agradecerá, garanto-lhe.

    Temos de começar por algum lugar, então escolhi o que é mais comum a
todo jogo: o loop de animação. Criaremos uma classe responsável por con-
trolar esse loop.
    Antes de começar, vamos ter em mente que problemas ela resolverá. “Mas
fazer um loop de animação não é só chamar o método repetidamente?”, você
dirá. Depende do que você quer fazer. Em um jogo:

      • a animação tem que ser parada e reiniciada em diversos momentos;

      • vários objetos serão animados em cada ciclo;

      • objetos podem ser incluídos e excluídos da animação.

Conceito de sprites
    Aos objetos trabalhados dentro de um loop de animação, damos o nome
de sprites. Pense em um sprite como sendo uma imagem com fundo trans-
parente, que pode ser animada. Dessa forma, eles podem ser inseridos sobre
o fundo principal do cenário.




36


[PAGINA 44]
Casa do Código                                       Capítulo 2. O loop de animação




                             Figura 2.1: Sprites


     Sprites são criados e destruídos a todo momento. Por “destruídos”, en-
tenda não apenas morto, aniquilado, atingido, mas destruídos na memória
do computador. Por exemplo, um inimigo ou item que saiu da tela pode ser
destruído e recriado caso o herói retorne àquele ponto. Em JavaScript, não
fazemos destruição de objetos (em outras linguagens isso é possível), apenas
anulamos as variáveis que se referem a ele e o deixamos livres para o garbage
collector apagá-lo da memória automaticamente.
     Chega de conceitos! É hora de pôr a mão na massa.




                                                                                37


[PAGINA 45]
2.2. Teste para a classe Animacao                                Casa do Código


2.2 Teste para a classe Animacao




               Figura 2.2: Animação controlada por classe JavaScript


Como prometemos, faremos um pequeno aplicativo de teste no qual defin-
imos como queremos “mandar” nas classes que criaremos. Como estamos
desenvolvendo para a web, nosso aplicativo será uma pequena página HTML
com alguns códigos JavaScript.
     A página referencia dois arquivos JavaScript: animacao.js, que conterá
a classe que controlará o loop de animação, e bola.js, onde definiremos um
sprite (uma bola que quica na tela).

❁✦✲✲ ❛rq✉✐✈♦✿ ❛♥✐♠❛❝❛♦✲t❡st❡✳❤t♠❧ ✲✲❃
❁✦❉❖❈❚❨P❊ ❤t♠❧❃
❁❤t♠❧❃

❁❤❡❛❞❃
   ❁t✐t❧❡❃Pr✐♠❡✐r♦ ❚❡st❡✿ ▲♦♦♣ ❞❡ ❆♥✐♠❛çã♦ ❝♦♠ ❙♣r✐t❡s❁✴t✐t❧❡❃
   ❁s❝r✐♣t sr❝❂✧❛♥✐♠❛❝❛♦✳❥s✧❃❁✴s❝r✐♣t❃
   ❁s❝r✐♣t sr❝❂✧❜♦❧❛✳❥s✧❃❁✴s❝r✐♣t❃

38


[PAGINA 46]
Casa do Código                                       Capítulo 2. O loop de animação



❁✴❤❡❛❞❃

❁❜♦❞②❃
   ❁❝❛♥✈❛s ✐❞❂✧❝❛♥✈❛s❴❛♥✐♠❛❝❛♦✧ ✇✐❞t❤❂✧✺✵✵✧ ❤❡✐❣❤t❂✧✺✵✵✧❃
   ❁✴❝❛♥✈❛s❃
   ❁s❝r✐♣t❃
      ✴✴ ❆q✉✐ ✈❛✐ ❛ ✐♥✐❝✐❛❧✐③❛çã♦ ❞♦ ❛♣❧✐❝❛t✐✈♦
   ❁✴s❝r✐♣t❃
❁✴❜♦❞②❃

❁✴❤t♠❧❃

    Após o Canvas, a página executará um script de inicialização, cujo código
vem a seguir. Como aprendemos no capítulo anterior, tópico 1.1, primeiro
temos de recuperar o Canvas e seu contexto 2d. Depois, criamos os primeiros
sprites b1 e b2 para as bolas, indicando suas coordenadas na tela, e outras
características como velocidade, cor e raio.

✴✴ ❘❡❢❡rê♥❝✐❛s ♣❛r❛ ♦ ❈❛♥✈❛s
✈❛r ❝❛♥✈❛s ❂ ❞♦❝✉♠❡♥t✳❣❡t❊❧❡♠❡♥t❇②■❞✭✬❝❛♥✈❛s❴❛♥✐♠❛❝❛♦✬✮❀
✈❛r ❝♦♥t❡①t ❂ ❝❛♥✈❛s✳❣❡t❈♦♥t❡①t✭✬✷❞✬✮❀

✴✴ ❈r✐❛♥❞♦ ❛❧❣✉♥s s♣r✐t❡s
✈❛r ❜✶ ❂ ♥❡✇ ❇♦❧❛✭❝♦♥t❡①t✮❀
❜✶✳① ❂ ✶✵✵❀
❜✶✳② ❂ ✷✵✵❀
❜✶✳✈❡❧♦❝✐❞❛❞❡❳ ❂ ✷✵❀
❜✶✳✈❡❧♦❝✐❞❛❞❡❨ ❂ ✲✶✵❀
❜✶✳❝♦r ❂ ✬r❡❞✬❀
❜✶✳r❛✐♦ ❂ ✷✵❀

✈❛r ❜✷ ❂ ♥❡✇ ❇♦❧❛✭❝♦♥t❡①t✮❀
❜✷✳① ❂ ✷✵✵❀
❜✷✳② ❂ ✶✵✵❀
❜✷✳✈❡❧♦❝✐❞❛❞❡❳ ❂ ✲✶✵❀
❜✷✳✈❡❧♦❝✐❞❛❞❡❨ ❂ ✷✵❀
❜✷✳❝♦r ❂ ✬❜❧✉❡✬❀
❜✷✳r❛✐♦ ❂ ✸✵❀


                                                                                39


[PAGINA 47]
2.2. Teste para a classe Animacao                              Casa do Código


    Em seguida, vamos criar a nossa animação hipotética, incluir nela os
sprites e ligá-la, fazendo com que se inicie imediatamente:

✴✴ ❈r✐❛♥❞♦ ♦ ❧♦♦♣ ❞❡ ❛♥✐♠❛çã♦
✈❛r ❛♥✐♠❛❝❛♦ ❂ ♥❡✇ ❆♥✐♠❛❝❛♦✭✮❀
❛♥✐♠❛❝❛♦✳♥♦✈♦❙♣r✐t❡✭❜✶✮❀
❛♥✐♠❛❝❛♦✳♥♦✈♦❙♣r✐t❡✭❜✷✮❀

✴✴ ✧▲✐❣❛r✧ ❛ ❛♥✐♠❛çã♦
❛♥✐♠❛❝❛♦✳❧✐❣❛r✭✮❀

    Claro que, ao tentar abrir esta página no navegador, ela ainda não fun-
ciona. Tecle Ctrl+Shift+J no Google Chrome, ou Ctrl+Shift+K no
Firefox, e delicie-se com estas mensagens:




 Figura 2.3: Erros no Console do Google Chrome na fase de escrita do teste


    A razão é que não temos ainda os arquivos animacao.js e bola.js.
Nós apenas definimos como queremos interagir com as classes que ainda não
saíram do ovo.
    E como queremos mandar nessas classes? Quanto à Bola, quero poder
criar quantas desejar, configurar posição, velocidades horizontal e vertical,
raio e cor. Quanto à Animacao, no código estou dizendo que quero poder
incluir sprites à vontade e mandar iniciá-la no momento que eu achar opor-
tuno.




40


[PAGINA 48]
Casa do Código                                      Capítulo 2. O loop de animação



2.3 Desenvolva a classe Animacao
O “grosso” do trabalho começa aqui. Já temos bem definido o que queremos
da classe neste ponto, mas agora falta explicitar como. Por mais desafiador
que pareça, vamos por etapas bem pequenas ("baby steps”), e logo teremos
um resultado concreto.
    Primeiro, faremos o esqueleto da classe, com sua função construtora e os
métodos que imaginamos no teste:
✴✴ ❆rq✉✐✈♦✿ ❛♥✐♠❛❝❛♦✳❥s
❢✉♥❝t✐♦♥ ❆♥✐♠❛❝❛♦✭✮ ④

⑥
❆♥✐♠❛❝❛♦✳♣r♦t♦t②♣❡ ❂ ④
   ♥♦✈♦❙♣r✐t❡✿ ❢✉♥❝t✐♦♥✭s♣r✐t❡✮ ④

    ⑥✱
    ❧✐❣❛r✿ ❢✉♥❝t✐♦♥✭✮ ④

    ⑥
⑥

   Para incluir um sprite na animação, podemos iniciar um array vazio no
construtor e incluir nele os sprites:
❢✉♥❝t✐♦♥ ❆♥✐♠❛❝❛♦✭✮ ④
  t❤✐s✳s♣r✐t❡s ❂ ❬❪❀
⑥
❆♥✐♠❛❝❛♦✳♣r♦t♦t②♣❡ ❂ ④
   ♥♦✈♦❙♣r✐t❡✿ ❢✉♥❝t✐♦♥✭s♣r✐t❡✮ ④
      t❤✐s✳s♣r✐t❡s✳♣✉s❤✭s♣r✐t❡✮❀
   ⑥✱
   ❧✐❣❛r✿ ❢✉♥❝t✐♦♥✭✮ ④

    ⑥
⑥

   Agora vamos criar o atributo ligado, que definirá se a animação pode
ou não correr. Aproveitando o ensejo, já criaremos também o método
desligar:

                                                                               41


[PAGINA 49]
2.3. Desenvolva a classe Animacao                          Casa do Código


❢✉♥❝t✐♦♥ ❆♥✐♠❛❝❛♦✭✮ ④
   t❤✐s✳s♣r✐t❡s ❂ ❬❪❀
   t❤✐s✳❧✐❣❛❞♦ ❂ ❢❛❧s❡❀
⑥

❆♥✐♠❛❝❛♦✳♣r♦t♦t②♣❡ ❂ ④
   ♥♦✈♦❙♣r✐t❡✿ ❢✉♥❝t✐♦♥✭s♣r✐t❡✮ ④
      t❤✐s✳s♣r✐t❡s✳♣✉s❤✭s♣r✐t❡✮❀
   ⑥✱

     ❧✐❣❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
        t❤✐s✳❧✐❣❛❞♦ ❂ tr✉❡❀
        t❤✐s✳♣r♦①✐♠♦❋r❛♠❡✭✮❀
     ⑥✱
     ✴✴ ◆ã♦ ❡sq✉❡❝❡r ❞❡st❛ ✈ír❣✉❧❛ s❡♠♣r❡ q✉❡
     ✴✴ ❢♦r ❝r✐❛r ✉♠ ♥♦✈♦ ♠ét♦❞♦✦

     ❞❡s❧✐❣❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
        t❤✐s✳❧✐❣❛❞♦ ❂ ❢❛❧s❡❀
     ⑥
⑥

    Em ligar, chamo um novo método, proximoFrame, que será o
coração da classe Animacao. Este método verifica se pode continuar e, se
puder, realiza um ciclo da animação e chama a si mesmo novamente (usando
o requestAnimationFrame do HTML5).

♣r♦①✐♠♦❋r❛♠❡✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✴✴ P♦ss♦ ❝♦♥t✐♥✉❛r❄
   ✐❢ ✭ ✦ t❤✐s✳❧✐❣❛❞♦ ✮ r❡t✉r♥❀

     ✴✴ ❆ ❝❛❞❛ ❝✐❝❧♦✱ ❧✐♠♣❛♠♦s ❛ t❡❧❛ ♦✉ ❞❡s❡♥❤❛♠♦s ✉♠ ❢✉♥❞♦
     t❤✐s✳❧✐♠♣❛r❚❡❧❛✭✮❀

     ✴✴ ❆t✉❛❧✐③❛♠♦s ♦ ❡st❛❞♦ ❞♦s s♣r✐t❡s
     ❢♦r ✭✈❛r ✐ ✐♥ t❤✐s✳s♣r✐t❡s✮
        t❤✐s✳s♣r✐t❡s❬✐❪✳❛t✉❛❧✐③❛r✭✮❀

     ✴✴ ❉❡s❡♥❤❛♠♦s ♦s s♣r✐t❡s

42


[PAGINA 50]
Casa do Código                                         Capítulo 2. O loop de animação



    ❢♦r ✭✈❛r ✐ ✐♥ t❤✐s✳s♣r✐t❡s✮
       t❤✐s✳s♣r✐t❡s❬✐❪✳❞❡s❡♥❤❛r✭✮❀

    ✴✴ ❈❤❛♠❛♠♦s ♦ ♣ró①✐♠♦ ❝✐❝❧♦
    ✈❛r ❛♥✐♠❛❝❛♦ ❂ t❤✐s❀
    r❡q✉❡st❆♥✐♠❛t✐♦♥❋r❛♠❡✭❢✉♥❝t✐♦♥✭✮ ④
       ❛♥✐♠❛❝❛♦✳♣r♦①✐♠♦❋r❛♠❡✭✮❀
    ⑥✮❀
⑥

   Aqui temos muitas coisas acontecendo. A cada ciclo de animação, deve-
mos:

    • limpar a tela: se não fizermos isso, a bola deixará um rastro (figura 2.4).
      É preciso apagar os desenhos do ciclo anterior para desenhar a bola em
      seu novo estado, na nova posição que vai atualizar e desenhar logo em
      seguida. O método limparTela será implementado em breve;

    • atualizar o estado dos sprites: cada sprite será responsável por se posi-
      cionar e realizar seus próprios comportamentos. Deixamos a cargo da
      Bola a função de calcular sua trajetória;

    • desenhar os sprites: somente depois que todos estiverem atualizados;

    • chamar o próximo ciclo da animação.




                                                                                  43


[PAGINA 51]
2.3. Desenvolva a classe Animacao                              Casa do Código




Figura 2.4: Rastro deixado pela bola se não limparmos a tela a cada ciclo da
animação



      Temos uma implicação importante: todo objeto que quiser partici-
  par do loop de animação (ou seja, que quiser ser um sprite), terá que
  implementar os métodos atualizar e desenhar. Este é o conceito
  de interface da Orientação a objetos: um conjunto de métodos que uma
  classe deve implementar para poder interagir com outra.

     Para chamar o próximo ciclo, não podemos simplesmente fazer:
r❡q✉❡st❆♥✐♠❛t✐♦♥❋r❛♠❡✭t❤✐s✳♣r♦①✐♠♦❋r❛♠❡✮❀

    A função de animação é chamada pelo JavaScript como uma função co-
mum, não como um método de objeto — não podemos usar o this den-
tro dela, e fizemos isso várias vezes! Juro, quando fui fazer isto, quebrei a
cabeça para descobrir por que não funcionava. A solução é referenciar o ob-
jeto em uma variável e chamar uma função anônima, que por sua vez chama
proximoFrame como um verdadeiro método do objeto:

44


[PAGINA 52]
Casa do Código                                        Capítulo 2. O loop de animação



✈❛r ❛♥✐♠❛❝❛♦ ❂ t❤✐s❀
r❡q✉❡st❆♥✐♠❛t✐♦♥❋r❛♠❡✭❢✉♥❝t✐♦♥✭✮ ④
   ❛♥✐♠❛❝❛♦✳♣r♦①✐♠♦❋r❛♠❡✭✮❀
⑥✮❀

    Temos agora que implementar o método limparTela:

❧✐♠♣❛r❚❡❧❛✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✈❛r ❝t① ❂ t❤✐s✳❝♦♥t❡①t❀ ✴✴ ❙ó ♣❛r❛ ❢❛❝✐❧✐t❛r ❛ ❡s❝r✐t❛ ❀✮
   ❝t①✳❝❧❡❛r❘❡❝t✭✵✱ ✵✱ ❝t①✳❝❛♥✈❛s✳✇✐❞t❤✱ ❝t①✳❝❛♥✈❛s✳❤❡✐❣❤t✮❀
⑥

   Este método requer um objeto context do HTML5 Canvas, portanto
vamos recebê-lo no construtor:

❢✉♥❝t✐♦♥ ❆♥✐♠❛❝❛♦✭❝♦♥t❡①t✮ ④
   t❤✐s✳❝♦♥t❡①t ❂ ❝♦♥t❡①t❀
   t❤✐s✳s♣r✐t❡s ❂ ❬❪❀
   t❤✐s✳❧✐❣❛❞♦ ❂ ❢❛❧s❡❀
⑥

    Temos então que passá-lo no código do aplicativo:

✴✴ ❈r✐❛♥❞♦ ♦ ❧♦♦♣ ❞❡ ❛♥✐♠❛çã♦
✈❛r ❛♥✐♠❛❝❛♦ ❂ ♥❡✇ ❆♥✐♠❛❝❛♦✭❝♦♥t❡①t✮❀


      Procure fazer com que uma classe receba de fora e guarde em atribu-
  tos tudo que ela precisa para executar seu trabalho, de forma que ela fique
  completamente desacoplada do meio externo. Depender diretamente da
  variável context do aplicativo é mau negócio! Este princípio chama-se
  injeção de dependências.


2.4    Implemente a classe Bola
Esta classe implementará a interface de sprites, portanto deverá ter os méto-
dos atualizar e desenhar:



                                                                                 45


[PAGINA 53]
2.4. Implemente a classe Bola                                     Casa do Código


✴✴ ❆rq✉✐✈♦✿ ❜♦❧❛✳❥s
❢✉♥❝t✐♦♥ ❇♦❧❛✭❝♦♥t❡①t✮ ④
   t❤✐s✳❝♦♥t❡①t ❂ ❝♦♥t❡①t❀
   t❤✐s✳① ❂ ✵❀
   t❤✐s✳② ❂ ✵❀
   t❤✐s✳✈❡❧♦❝✐❞❛❞❡❳ ❂ ✵❀
   t❤✐s✳✈❡❧♦❝✐❞❛❞❡❨ ❂ ✵❀

     ✴✴ ❆tr✐❜✉t♦s ❞❡ ❞❡s❡♥❤♦ ♣❛❞rã♦
     t❤✐s✳❝♦r ❂ ✬❜❧❛❝❦✬❀
     t❤✐s✳r❛✐♦ ❂ ✶✵❀
⑥
❇♦❧❛✳♣r♦t♦t②♣❡ ❂ ④
   ❛t✉❛❧✐③❛r✿ ❢✉♥❝t✐♦♥✭✮ ④

     ⑥✱
     ❞❡s❡♥❤❛r✿ ❢✉♥❝t✐♦♥✭✮ ④

     ⑥
⑥

    Em atualizar, colocamos o algoritmo que quica a bola nas bordas do
Canvas. Repare que sempre temos que descontar o raio da bola, pois as co-
ordenadas x e y se referirão ao seu centro (figura 2.5). Se o centro estiver fora
do limite estabelecido, invertemos o sinal da velocidade (multiplicamos por
-1) para que a bola passe a ir em sentido contrário, tanto na vertical quanto
na horizontal:

❛t✉❛❧✐③❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✈❛r ❝t① ❂ t❤✐s✳❝♦♥t❡①t❀

     ✐❢ ✭t❤✐s✳① ❁ t❤✐s✳r❛✐♦ ⑤⑤ t❤✐s✳① ❃
           ❝t①✳❝❛♥✈❛s✳✇✐❞t❤ ✲ t❤✐s✳r❛✐♦✮
        t❤✐s✳✈❡❧♦❝✐❞❛❞❡❳ ✯❂ ✲✶❀

     ✐❢ ✭t❤✐s✳② ❁ t❤✐s✳r❛✐♦ ⑤⑤ t❤✐s✳② ❃
           ❝t①✳❝❛♥✈❛s✳❤❡✐❣❤t ✲ t❤✐s✳r❛✐♦✮
        t❤✐s✳✈❡❧♦❝✐❞❛❞❡❨ ✯❂ ✲✶❀


46


[PAGINA 54]
Casa do Código                                       Capítulo 2. O loop de animação



     t❤✐s✳① ✰❂ t❤✐s✳✈❡❧♦❝✐❞❛❞❡❳❀
     t❤✐s✳② ✰❂ t❤✐s✳✈❡❧♦❝✐❞❛❞❡❨❀
⑥✱




Figura 2.5: A posição da bola é calculada pelo seu centro, portanto os limites
para quicá-la têm que descontar o raio.


    Em desenhar, usamos o método arc do context. Também usamos
os métodos save e restore para poder configurá-lo com a cor da bola
e depois retorná-lo ao estado original. Caso não se lembre destes métodos,
reveja a seção 1.2.
❞❡s❡♥❤❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✈❛r ❝t① ❂ t❤✐s✳❝♦♥t❡①t❀

     ✴✴ ●✉❛r❞❛r ❝♦♥❢✐❣✉r❛çõ❡s ❛t✉❛✐s ❞♦ ❝♦♥t❡①t♦
     ❝t①✳s❛✈❡✭✮❀

     ✴✴ ❈♦♥❢✐❣✉r❛r ♦ ❝♦♥t❡①t♦ ❞❡ ❛❝♦r❞♦ ❝♦♠ ❛ ❜♦❧❛
     ❝t①✳❢✐❧❧❙t②❧❡ ❂ t❤✐s✳❝♦r❀

     ✴✴ ❉❡s❡♥❤❛r
     ❝t①✳❜❡❣✐♥P❛t❤✭✮❀
     ❝t①✳❛r❝✭t❤✐s✳①✱ t❤✐s✳②✱ t❤✐s✳r❛✐♦✱ ✵✱ ✷ ✯ ▼❛t❤✳P■✱ ❢❛❧s❡✮❀
     ❝t①✳❢✐❧❧✭✮❀

     ✴✴ ❱♦❧t❛r às ❝♦♥❢✐❣✉r❛çõ❡s ❛♥t❡r✐♦r❡s
     ❝t①✳r❡st♦r❡✭✮❀
⑥

                                                                                47


[PAGINA 55]
2.4. Implemente a classe Bola                                Casa do Código


    O aplicativo está pronto! Abra-o no navegador. Se estiver usando o
Chrome, pressione Ctrl+Shift+J e digite no Console (para fazer isso no
Firefox, você deve instalar um plugin como o Firebug):

❛♥✐♠❛❝❛♦✳❞❡s❧✐❣❛r✭✮❀

     A animação para! Agora faça:

❛♥✐♠❛❝❛♦✳❧✐❣❛r✭✮❀

    Não é fantástico? Como exercício, crie mais objetos Bola com tamanhos,
cores e velocidades diferentes, e acrescente-os à animação. Você pode fazer
isso no arquivo HTML ou diretamente no Console!
    Aqui nós criamos uma primeira base para nosso jogo, que é o loop de
animação. No próximo capítulo, vamos aprender como é possível criar a in-
teração do usuário com o jogo.




48


[PAGINA 56]
Capítulo 3

A interação com o jogador —
leitura apurada do teclado
Neste tópico, vamos tratar da interação do usuário com o jogo. Tratar eventos
de teclado em JavaScript não é uma tarefa difícil, no entanto, há aspectos que
precisam ser considerados, em se tratando de jogos.
    Faremos uma revisão sobre os eventos de teclado e, em seguida, tratare-
mos dois tipos especiais de interações:

    • o jogador mantém uma tecla pressionada: muito comum com as setas
      de movimentação, mas não se limita a estas. O jogo deve responder de
      determinada maneira (por exemplo, movimentando o herói) enquanto
      a tecla está pressionada e parar quando o jogador solta a tecla;

    • o jogador pressiona e solta rapidamente a tecla: são as teclas de disparo,


[PAGINA 57]
3.1. EventListeners e os eventos keydown e keyup                Casa do Código


        com as quais a ação deve ocorrer uma única vez, no momento exato do
        pressionamento. Se a tecla continuar pressionada, o jogo deve ignorar
        seu estado.

    Isto tudo parece muito óbvio mas, como veremos, o modelo de eventos
do teclado em JavaScript é voltado para a digitação de caracteres (lembre-se, a
linguagem foi criada para páginas da web) e não nos permite tratar interações
comuns em jogos com apenas um comando. Porém, a coisa também não é tão
complicada, requerendo apenas alguma codificação manual.


3.1      EventListeners e os eventos keydown e
         keyup
Qualquer elemento em uma página da web pode ter “ouvintes” (listeners) de
eventos. No caso dos eventos do teclado, o elemento deve ter o foco:




Figura 3.1: Cursor do teclado piscando no campo de busca. O foco do teclado
pertence a ele neste momento.




50


[PAGINA 58]
Casa do Código            Capítulo 3. A interação com o jogador — leitura apurada do teclado




Figura 3.2: Após alguns toques na tecla Tab, o foco vai para o botão Pesquisa
Google e este fica destacado. O browser aguarda o usuário teclar Enter ou
espaço para acionar o botão.


   Um listener é uma função JavaScript que executa uma ação em resposta a
um evento. Essa função pode receber um parâmetro que é preenchido auto-
maticamente com dados sobre o evento ocorrido.
   Para associar um listener a um elemento da página, usamos o método
addEventListener:

✴✴ ❊①❡♠♣❧♦ t❡ór✐❝♦
✈❛r ❝❛♠♣♦ ❂ ❞♦❝✉♠❡♥t✳❣❡t❊❧❡♠❡♥t❇②■❞✭✬❝❛♠♣♦✬✮❀
❝❛♠♣♦✳❛❞❞❊✈❡♥t▲✐st❡♥❡r✭✬♥♦♠❡❞♦❡✈❡♥t♦✬✱
   ❢✉♥❝t✐♦♥✭♣❛r❛♠❡tr♦❊✈❡♥t♦✮ ④
      ✴✴ ❆çõ❡s ❞❡ r❡s♣♦st❛ ❛♦ ❡✈❡♥t♦ ✈ã♦ ❛q✉✐
   ⑥✮❀

    Em JavaScript, são três os eventos associados ao teclado:

    • keydown: ocorre quando uma tecla é pressionada (abaixada). Se o
      usuário a mantiver segurando, o evento é disparado repetidamente.

    • keypress: ocorre logo após keydown, no caso de a tecla ser de carac-
      tere. Se a tecla continuar pressionada, o browser dispara os eventos
      alternadamente: keydown-keypress-keydown-keypress-etc.

    • keyup: ocorre uma única vez, quando uma tecla é solta.

                                                                                         51


[PAGINA 59]
3.1. EventListeners e os eventos keydown e keyup                Casa do Código




Figura 3.3: Tecla mantida pressionada. O computador produz um caractere,
faz uma pausa, e dispara outros em sequência.




         Para o desenvolvimento de jogos, somente os eventos keydown e
     keyup serão necessários. Tudo o que nós precisaremos saber serão os
     momentos quando uma tecla é pressionada e quando é solta, para poder
     disparar ações ao pressionar ou detectar se uma tecla está ou não pres-
     sionada. O evento keypress é específico para tratar digitação de carac-
     teres.


     Seria tudo muito maravilhoso se pudéssemos codificar nossas ações dire-
tamente no evento keydown! No entanto, o resultado ficaria horrível. O mod-
elo de eventos para a digitação de caracteres (figura 3.3) não serve para movi-
mentar personagens. Já vi alguns joguinhos de tutoriais na internet serem
feitos dessa maneira. Faça um teste e comprove por si mesmo:

❁✦✲✲ ❛rq✉✐✈♦ t❡❝❧❛❞♦✲t❡st❡✲✶✳❤t♠❧ ✲✲❃
❁✦❉❖❈❚❨P❊ ❤t♠❧❃
❁❤t♠❧❃

❁❤❡❛❞❃
   ❁t✐t❧❡❃▼♦✈✐♠❡♥t❛♥❞♦ ♣❡rs♦♥❛❣❡♠ ❝♦♠ ❦❡②❞♦✇♥❁✴t✐t❧❡❃
❁✴❤❡❛❞❃

❁❜♦❞②❃
   ❁❝❛♥✈❛s ✐❞❂✧❝❛♥✈❛s❴t❡❝❧❛❞♦❴✶✧ ✇✐❞t❤❂✧✺✵✵✧ ❤❡✐❣❤t❂✧✺✵✵✧❃
   ❁✴❝❛♥✈❛s❃
   ❁s❝r✐♣t❃
      ✴✴ ■♥t❡r❛çã♦ ❝♦♠ ♦ t❡❝❧❛❞♦ ✈❛✐ ❛q✉✐
   ❁✴s❝r✐♣t❃
❁✴❜♦❞②❃


52


[PAGINA 60]
Casa do Código            Capítulo 3. A interação com o jogador — leitura apurada do teclado




❁✴❤t♠❧❃

    Agora iremos criar um listener para o evento keydown, que desloca um
“personagem” para a direita ou para a esquerda. As teclas de seta são recon-
hecidas através da propriedade keyCode do objeto evento, recebido como
parâmetro.
    Na tag <script>, que vem logo após o Canvas, digite:

✴✴ ❘❡❢❡rê♥❝✐❛s ❞♦ ❈❛♥✈❛s
✈❛r ❝❛♥✈❛s ❂ ❞♦❝✉♠❡♥t✳❣❡t❊❧❡♠❡♥t❇②■❞✭✬❝❛♥✈❛s❴t❡❝❧❛❞♦❴✶✬✮❀
✈❛r ❝♦♥t❡①t ❂ ❝❛♥✈❛s✳❣❡t❈♦♥t❡①t✭✬✷❞✬✮❀

✴✴ P♦s✐çã♦ ✐♥✐❝✐❛❧ ❞♦ ♣❡rs♦♥❛❣❡♠
✈❛r ♣♦s✐❝❛♦ ❂ ✵❀
❞❡s❡♥❤❛rP❡rs♦♥❛❣❡♠✭✮❀

❞♦❝✉♠❡♥t✳❛❞❞❊✈❡♥t▲✐st❡♥❡r✭✬❦❡②❞♦✇♥✬✱ ❢✉♥❝t✐♦♥✭❡✈❡♥t♦✮ ④
   ✐❢ ✭❡✈❡♥t♦✳❦❡②❈♦❞❡ ❂❂ ✸✼✮ ④ ✴✴ ❙❡t❛ ♣❛r❛ ❡sq✉❡r❞❛
      ♣♦s✐❝❛♦ ✲❂ ✶✵❀
      ❞❡s❡♥❤❛rP❡rs♦♥❛❣❡♠✭✮❀
   ⑥
   ❡❧s❡ ✐❢ ✭❡✈❡♥t♦✳❦❡②❈♦❞❡ ❂❂ ✸✾✮ ④ ✴✴ ❙❡t❛ ♣❛r❛ ❞✐r❡✐t❛
      ♣♦s✐❝❛♦ ✰❂ ✶✵❀
      ❞❡s❡♥❤❛rP❡rs♦♥❛❣❡♠✭✮❀
   ⑥
⑥✮❀

✴✴ ❯♠ ♣❡rs♦♥❛❣❡♠ ♥ã♦ ♠✉✐t♦ s✐♠♣át✐❝♦✱ ♠❛s✳✳✳
❢✉♥❝t✐♦♥ ❞❡s❡♥❤❛rP❡rs♦♥❛❣❡♠✭✮ ④
   ❝♦♥t❡①t✳❝❧❡❛r❘❡❝t✭✵✱ ✵✱ ❝❛♥✈❛s✳✇✐❞t❤✱ ❝❛♥✈❛s✳❤❡✐❣❤t✮❀
   ❝♦♥t❡①t✳❢✐❧❧❘❡❝t✭♣♦s✐❝❛♦✱ ✶✵✵✱ ✷✵✱ ✺✵✮❀
⑥

   Abra a página no browser e mova o retângulo com as setas direita e es-
querda. Perceba que, ao iniciar o movimento para algum lado, ocorre uma
pausa após o primeiro deslocamento, para depois ele ocorrer normalmente.



                                                                                         53


[PAGINA 61]
3.1. EventListeners e os eventos keydown e keyup                     Casa do Código




                  Figura 3.4: Nosso herói parece que está manco...


   Não ficou bom, não é verdade? Mas podemos aprender muitas coisas
debruçando-se sobre este trecho:
❞♦❝✉♠❡♥t✳❛❞❞❊✈❡♥t▲✐st❡♥❡r✭✬❦❡②❞♦✇♥✬✱ ❢✉♥❝t✐♦♥✭❡✈❡♥t♦✮ ④
   ✐❢ ✭❡✈❡♥t♦✳❦❡②❈♦❞❡ ❂❂ ✸✼✮ ④ ✴✴ ❙❡t❛ ♣❛r❛ ❡sq✉❡r❞❛
      ♣♦s✐❝❛♦ ✲❂ ✶✵❀
      ❞❡s❡♥❤❛rP❡rs♦♥❛❣❡♠✭✮❀
   ⑥
   ❡❧s❡ ✐❢ ✭❡✈❡♥t♦✳❦❡②❈♦❞❡ ❂❂ ✸✾✮ ④ ✴✴ ❙❡t❛ ♣❛r❛ ❞✐r❡✐t❛
      ♣♦s✐❝❛♦ ✰❂ ✶✵❀
      ❞❡s❡♥❤❛rP❡rs♦♥❛❣❡♠✭✮❀
   ⑥
⑥✮❀

     • Primeiro, quero ouvir eventos do teclado ocorridos em todo o docu-
       mento. Portanto, adiciono o listener ao elemento document.

     • A function recebeu um parâmetro de nome evento (posso dar
       qualquer nome para ele). Esse parâmetro recebeu do JavaScript auto-
       maticamente um objeto com propriedades relacionadas ao evento.

     • A propriedade keyCode desse objeto contém um valor único para
       cada tecla. Não é difícil descobrir os códigos fazendo uma rápida
       pesquisa na internet, ou criando um pequeno programa para esse fim.

54


[PAGINA 62]
Casa do Código             Capítulo 3. A interação com o jogador — leitura apurada do teclado



3.2 Detectando se uma tecla está ou não pres-
    sionada
Como aprendemos (e comprovamos, caso você tenha digitado o código an-
terior), o modelo de eventos de teclado do JavaScript é eficaz para tratar dig-
itação, mas completamente bizarro para jogos. Como não há nenhum co-
mando para eu perguntar: “a tecla tal está pressionada?”, tenho que manter
um registro de teclas pressionadas manualmente. Para facilitar, seguiremos o
modelo de criar uma classe para tratar deste problema.

Teste da classe Teclado
   Criemos uma página semelhante à anterior, mas onde nosso corajoso
herói será controlado de maneira mais eficiente. Imagine podermos fazer:

✴✴ ❊①❡♠♣❧♦ t❡ór✐❝♦
✈❛r t❡❝❧❛❞♦ ❂ ♥❡✇ ❚❡❝❧❛❞♦✭❞♦❝✉♠❡♥t✮❀

✐❢ ✭t❡❝❧❛❞♦✳♣r❡ss✐♦♥❛❞❛✭❙❊❚❆❴❉■❘❊■❚❆✮✮
   ♣♦s✐❝❛♦ ✰❂ ✶✵❀

    Bem, então... façamos! Repare na simplicidade com que queremos con-
trolar o teclado. Delegamos à classe Teclado a responsabilidade de saber se
determinada tecla está ou não pressionada.

❁✦✲✲ ❛rq✉✐✈♦ t❡st❡✲t❡❝❧❛❞♦✲✷✳❤t♠❧ ✲✲❃
❁✦❉❖❈❚❨P❊ ❤t♠❧❃
❁❤t♠❧❃

❁❤❡❛❞❃
   ❁t✐t❧❡❃▼♦✈✐♠❡♥t❛♥❞♦ ♣❡rs♦♥❛❣❡♠ ❝♦♠ ❝❧❛ss❡ ❏❛✈❛❙❝r✐♣t❁✴t✐t❧❡❃
   ❁s❝r✐♣t sr❝❂✧t❡❝❧❛❞♦✳❥s✧❃❁✴s❝r✐♣t❃
❁✴❤❡❛❞❃

❁❜♦❞②❃
   ❁❝❛♥✈❛s ✐❞❂✧❝❛♥✈❛s❴t❡❝❧❛❞♦❴✷✧ ✇✐❞t❤❂✧✺✵✵✧ ❤❡✐❣❤t❂✧✺✵✵✧❃
   ❁✴❝❛♥✈❛s❃
   ❁s❝r✐♣t❃


                                                                                          55


[PAGINA 63]
3.2. Detectando se uma tecla está ou não pressionada         Casa do Código


      ✴✴ ❆q✉✐ ✈✐rá ✉♠ ❝♦♥tr♦❧❡ ❞❡ t❡❝❧❛❞♦ ♠❛✐s ❛♣✉r❛❞♦
   ❁✴s❝r✐♣t❃
❁✴❜♦❞②❃

❁✴❤t♠❧❃

   O JavaScript conterá partes bem parecidas com o do exemplo anterior,
mas introduzimos aqui um loop de animação. É ele que vai avaliar constan-
temente o estado de determinadas teclas.
   Primeiro referenciamos o Canvas normalmente:
✈❛r ❝❛♥✈❛s ❂ ❞♦❝✉♠❡♥t✳❣❡t❊❧❡♠❡♥t❇②■❞✭✬❝❛♥✈❛s❴t❡❝❧❛❞♦❴✷✬✮❀
✈❛r ❝♦♥t❡①t ❂ ❝❛♥✈❛s✳❣❡t❈♦♥t❡①t✭✬✷❞✬✮❀

   Em seguida, definimos a posição inicial do personagem e mandamos de-
senhar:
✈❛r ♣♦s✐❝❛♦ ❂ ✵❀
❞❡s❡♥❤❛rP❡rs♦♥❛❣❡♠✭✮❀

   Agora vamos criar o controlador do teclado. Quero passar para ele o ele-
mento da página onde os eventos serão ouvidos (no caso, document):
✈❛r t❡❝❧❛❞♦ ❂ ♥❡✇ ❚❡❝❧❛❞♦✭❞♦❝✉♠❡♥t✮❀

    O loop de animação será bem básico, por enquanto através de uma sim-
ples função. Nesta função, primeiro lemos o estado das teclas que queremos
e mudamos a posição do personagem de acordo. Em seguida, nós o desen-
hamos e chamamos o próximo ciclo:
r❡q✉❡st❆♥✐♠❛t✐♦♥❋r❛♠❡✭❛♥✐♠❛r✮❀

❢✉♥❝t✐♦♥ ❛♥✐♠❛r✭✮ ④
   ✐❢ ✭t❡❝❧❛❞♦✳♣r❡ss✐♦♥❛❞❛✭❙❊❚❆❴❊❙◗❯❊❘❉❆✮✮
      ♣♦s✐❝❛♦ ✲❂ ✶✵❀
   ❡❧s❡ ✐❢ ✭t❡❝❧❛❞♦✳♣r❡ss✐♦♥❛❞❛✭❙❊❚❆❴❉■❘❊■❚❆✮✮
      ♣♦s✐❝❛♦ ✰❂ ✶✵❀

     ❞❡s❡♥❤❛rP❡rs♦♥❛❣❡♠✭✮❀
     r❡q✉❡st❆♥✐♠❛t✐♦♥❋r❛♠❡✭❛♥✐♠❛r✮❀
⑥

56


[PAGINA 64]
Casa do Código            Capítulo 3. A interação com o jogador — leitura apurada do teclado



    A função desenharPersonagem é a mesma criada anteriormente:
✴✴ ◆♦ss♦ ❤❡ró✐ ❝♦♥t✐♥✉❛ ❡s❜❛♥❥❛♥❞♦ ❝❤❛r♠❡✦ ✿❉
❢✉♥❝t✐♦♥ ❞❡s❡♥❤❛rP❡rs♦♥❛❣❡♠✭✮ ④
   ❝♦♥t❡①t✳❝❧❡❛r❘❡❝t✭✵✱ ✵✱ ❝❛♥✈❛s✳✇✐❞t❤✱ ❝❛♥✈❛s✳❤❡✐❣❤t✮❀
   ❝♦♥t❡①t✳❢✐❧❧❘❡❝t✭♣♦s✐❝❛♦✱ ✶✵✵✱ ✷✵✱ ✺✵✮❀
⑥

A classe Teclado
    Esta classe recebe um elemento qualquer da página no construtor e atribui
a ele os eventos que vão registrar o estado das teclas em um array. O método
pressionada devolve o valor true caso a tecla conste como pressionada
no momento:
✴✴ ❛rq✉✐✈♦✿ t❡❝❧❛❞♦✳❥s
✴✴ ❈ó❞✐❣♦s ❞❡ t❡❝❧❛s ✲ ❛q✉✐ ✈ã♦ t♦❞♦s ♦s q✉❡ ❢♦r❡♠ ♥❡❝❡ssár✐♦s
✈❛r ❙❊❚❆❴❊❙◗❯❊❘❉❆ ❂ ✸✼❀
✈❛r ❙❊❚❆❴❉■❘❊■❚❆ ❂ ✸✾❀

❢✉♥❝t✐♦♥ ❚❡❝❧❛❞♦✭❡❧❡♠❡♥t♦✮ ④
   t❤✐s✳❡❧❡♠❡♥t♦ ❂ ❡❧❡♠❡♥t♦❀

   ✴✴ ❆rr❛② ❞❡ t❡❝❧❛s ♣r❡ss✐♦♥❛❞❛s
   t❤✐s✳♣r❡ss✐♦♥❛❞❛s ❂ ❬❪❀

   ✴✴ ❘❡❣✐str❛♥❞♦ ♦ ❡st❛❞♦ ❞❛s t❡❝❧❛s ♥♦ ❛rr❛②
   ✈❛r t❡❝❧❛❞♦ ❂ t❤✐s❀
   ❡❧❡♠❡♥t♦✳❛❞❞❊✈❡♥t▲✐st❡♥❡r✭✬❦❡②❞♦✇♥✬✱ ❢✉♥❝t✐♦♥✭❡✈❡♥t♦✮ ④
      t❡❝❧❛❞♦✳♣r❡ss✐♦♥❛❞❛s❬❡✈❡♥t♦✳❦❡②❈♦❞❡❪ ❂ tr✉❡❀
   ⑥✮❀
   ❡❧❡♠❡♥t♦✳❛❞❞❊✈❡♥t▲✐st❡♥❡r✭✬❦❡②✉♣✬✱ ❢✉♥❝t✐♦♥✭❡✈❡♥t♦✮ ④
      t❡❝❧❛❞♦✳♣r❡ss✐♦♥❛❞❛s❬❡✈❡♥t♦✳❦❡②❈♦❞❡❪ ❂ ❢❛❧s❡❀
   ⑥✮❀
⑥
❚❡❝❧❛❞♦✳♣r♦t♦t②♣❡ ❂ ④
   ♣r❡ss✐♦♥❛❞❛✿ ❢✉♥❝t✐♦♥✭t❡❝❧❛✮ ④
      r❡t✉r♥ t❤✐s✳♣r❡ss✐♦♥❛❞❛s❬t❡❝❧❛❪❀
   ⑥
⑥

                                                                                         57


[PAGINA 65]
3.3. Efetuando disparos — detectando somente o primeiro keydown   Casa do Código


   Abra a página e veja que o “personagem” move-se com muito mais suavi-
dade e fluência!


3.3 Efetuando disparos — detectando somente
    o primeiro keydown
Vamos dar um superpoder ao herói: atirar. Neste ponto, para facilitar a nossa
vida, vamos usar a classe Animacao e o conceito de sprites aprendidos ante-
riormente.
    Que tal poder mandar o herói atirar da forma mostrada a seguir? Se a
classe Teclado sabe se uma tecla está pressionada, ela também pode saber
disparar uma ação única no momento do pressionamento!

✴✴ ❊①❡♠♣❧♦ t❡ór✐❝♦
t❡❝❧❛❞♦✳❞✐s♣❛r♦✉✭❊❙P❆❈❖✱ ❢✉♥❝t✐♦♥✭✮ ④
   ❤❡r♦✐✳❛t✐r❛r✭✮❀
⑥✮❀




                               Figura 3.5: Herói atirando


    Vamos criar uma nova página. Os scripts bola.js e animacao.js
são os mesmos já criados. Certifique-se de ter uma cópia deles na pasta deste
teste (ou linká-los corretamente em seu computador).


58


[PAGINA 66]
Casa do Código            Capítulo 3. A interação com o jogador — leitura apurada do teclado



❁✦✲✲ ❛rq✉✐✈♦✿ t❡st❡✲t❡❝❧❛❞♦✲✸✳❤t♠❧ ✲✲❃
❁✦❉❖❈❚❨P❊ ❤t♠❧❃
❁❤t♠❧❃

❁❤❡❛❞❃
   ❁t✐t❧❡❃❯♠ ❤❡ró✐ q✉❡ ❛t✐r❛❁✴t✐t❧❡❃
   ❁s❝r✐♣t sr❝❂✧t❡❝❧❛❞♦✳❥s✧❃❁✴s❝r✐♣t❃
   ❁s❝r✐♣t sr❝❂✧❤❡r♦✐✳❥s✧❃❁✴s❝r✐♣t❃
   ❁s❝r✐♣t sr❝❂✧❜♦❧❛✳❥s✧❃❁✴s❝r✐♣t❃
   ❁s❝r✐♣t sr❝❂✧❛♥✐♠❛❝❛♦✳❥s✧❃❁✴s❝r✐♣t❃
❁✴❤❡❛❞❃

❁❜♦❞②❃
   ❁❝❛♥✈❛s ✐❞❂✧❝❛♥✈❛s❴t❡❝❧❛❞♦❴✸✧ ✇✐❞t❤❂✧✺✵✵✧ ❤❡✐❣❤t❂✧✺✵✵✧❃
   ❁✴❝❛♥✈❛s❃
   ❁s❝r✐♣t❃
      ✴✴ ■st♦ ✈❛✐ ❝♦♠❡ç❛r ❛ ♣❛r❡❝❡r ✉♠ ❥♦❣♦✦
   ❁✴s❝r✐♣t❃
❁✴❜♦❞②❃

❁✴❤t♠❧❃

    Veja como o script do teste é simples e conciso. Nesta altura, eu espero
sinceramente que você esteja entendendo o porquê de estarmos fazendo dessa
forma. Criar uma nova ação, um novo personagem, um novo inimigo deverá
ser cada vez mais simples a partir de agora:

✈❛r ❝❛♥✈❛s ❂ ❞♦❝✉♠❡♥t✳❣❡t❊❧❡♠❡♥t❇②■❞✭✬❝❛♥✈❛s❴t❡❝❧❛❞♦❴✸✬✮❀
✈❛r ❝♦♥t❡①t ❂ ❝❛♥✈❛s✳❣❡t❈♦♥t❡①t✭✬✷❞✬✮❀

✈❛r t❡❝❧❛❞♦ ❂ ♥❡✇ ❚❡❝❧❛❞♦✭❞♦❝✉♠❡♥t✮❀
✈❛r ❛♥✐♠❛❝❛♦ ❂ ♥❡✇ ❆♥✐♠❛❝❛♦✭❝♦♥t❡①t✮❀

✴✴ ❯♠ s♣r✐t❡ ♣♦❞❡ ❧❡r ♦ t❡❝❧❛❞♦ ♣❛r❛ s❛❜❡r
✴✴ ❝♦♠♦ s❡ ❝♦♠♣♦rt❛r
✈❛r ❤❡r♦✐ ❂ ♥❡✇ ❍❡r♦✐✭❝♦♥t❡①t✱ t❡❝❧❛❞♦✮❀
❤❡r♦✐✳① ❂ ✵❀
❤❡r♦✐✳② ❂ ✶✵✵❀
❛♥✐♠❛❝❛♦✳♥♦✈♦❙♣r✐t❡✭❤❡r♦✐✮❀

                                                                                         59


[PAGINA 67]
3.3. Efetuando disparos — detectando somente o primeiro keydown   Casa do Código




t❡❝❧❛❞♦✳❞✐s♣❛r♦✉✭❊❙P❆❈❖✱ ❢✉♥❝t✐♦♥✭✮ ④
   ❤❡r♦✐✳❛t✐r❛r✭✮❀
⑥✮❀

❛♥✐♠❛❝❛♦✳❧✐❣❛r✭✮❀

     Precisamos criar o método disparou na classe Teclado. Para que
ele funcione corretamente, é preciso registrar que determinada tecla foi dis-
parada (para que os eventos keydown subsequentes não provoquem o disparo
novamente). Criamos mais dois arrays, um para registrar os disparos e outro
para guardar as funções a serem executadas:
✴✴ ❈ó❞✐❣♦s ❞❡ t❡❝❧❛s ✲ ❛q✉✐ ✈ã♦ t♦❞♦s ♦s q✉❡ ❢♦r❡♠ ♥❡❝❡ssár✐♦s
✈❛r ❙❊❚❆❴❊❙◗❯❊❘❉❆ ❂ ✸✼❀
✈❛r ❙❊❚❆❴❉■❘❊■❚❆ ❂ ✸✾❀
✈❛r ❊❙P❆❈❖ ❂ ✸✷❀

❢✉♥❝t✐♦♥ ❚❡❝❧❛❞♦✭❡❧❡♠❡♥t♦✮ ④
   t❤✐s✳❡❧❡♠❡♥t♦ ❂ ❡❧❡♠❡♥t♦❀

     ✴✴ ❆rr❛② ❞❡ t❡❝❧❛s ♣r❡ss✐♦♥❛❞❛s
     t❤✐s✳♣r❡ss✐♦♥❛❞❛s ❂ ❬❪❀

     ✴✴ ❆rr❛② ❞❡ t❡❝❧❛s ❞✐s♣❛r❛❞❛s
     t❤✐s✳❞✐s♣❛r❛❞❛s ❂ ❬❪❀

     ✴✴ ❋✉♥çõ❡s ❞❡ ❞✐s♣❛r♦
     t❤✐s✳❢✉♥❝♦❡s❉✐s♣❛r♦ ❂ ❬❪❀

     ✴✴ ❝♦♥t✐♥✉❛✳✳✳
⑥

    No evento keydown, verificamos se a tecla pressionada possui uma
função de disparo associada e se seu disparo já foi processado. A instrução
this.funcoesDisparo[tecla] () ; executa a função guardada no ar-
ray devido aos parênteses no final:
✈❛r t❡❝❧❛❞♦ ❂ t❤✐s❀


60


[PAGINA 68]
Casa do Código           Capítulo 3. A interação com o jogador — leitura apurada do teclado



❡❧❡♠❡♥t♦✳❛❞❞❊✈❡♥t▲✐st❡♥❡r✭✬❦❡②❞♦✇♥✬✱ ❢✉♥❝t✐♦♥✭❡✈❡♥t♦✮ ④
   ✈❛r t❡❝❧❛ ❂ ❡✈❡♥t♦✳❦❡②❈♦❞❡❀ ✴✴ ❚♦r♥❛♥❞♦ ♠❛✐s ❧❡❣í✈❡❧ ❀✮
   t❡❝❧❛❞♦✳♣r❡ss✐♦♥❛❞❛s❬t❡❝❧❛❪ ❂ tr✉❡❀

   ✴✴ ❉✐s♣❛r❛r s♦♠❡♥t❡ s❡ ❢♦r ♦ ♣r✐♠❡✐r♦ ❦❡②❞♦✇♥ ❞❛ t❡❝❧❛
   ✐❢ ✭t❡❝❧❛❞♦✳❢✉♥❝♦❡s❉✐s♣❛r♦❬t❡❝❧❛❪ ✫✫
       ✦ t❡❝❧❛❞♦✳❞✐s♣❛r❛❞❛s❬t❡❝❧❛❪✮ ④

        t❡❝❧❛❞♦✳❞✐s♣❛r❛❞❛s❬t❡❝❧❛❪ ❂ tr✉❡❀
        t❡❝❧❛❞♦✳❢✉♥❝♦❡s❉✐s♣❛r♦❬t❡❝❧❛❪ ✭✮ ❀
   ⑥
⑥✮❀

    No evento keyup setamos o estado “disparada” para false, de modo a
tornar possíveis novos disparos:

❡❧❡♠❡♥t♦✳❛❞❞❊✈❡♥t▲✐st❡♥❡r✭✬❦❡②✉♣✬✱ ❢✉♥❝t✐♦♥✭❡✈❡♥t♦✮ ④
   t❡❝❧❛❞♦✳♣r❡ss✐♦♥❛❞❛s❬❡✈❡♥t♦✳❦❡②❈♦❞❡❪ ❂ ❢❛❧s❡❀
   t❡❝❧❛❞♦✳❞✐s♣❛r❛❞❛s❬❡✈❡♥t♦✳❦❡②❈♦❞❡❪ ❂ ❢❛❧s❡❀
⑥✮❀

    Enfim, o método disparou necessita apenas guardar uma função de
disparo para uma tecla. O evento keydown está cuidando de tudo!

❞✐s♣❛r♦✉✿ ❢✉♥❝t✐♦♥✭t❡❝❧❛✱ ❝❛❧❧❜❛❝❦✮ ④
   t❤✐s✳❢✉♥❝♦❡s❉✐s♣❛r♦❬t❡❝❧❛❪ ❂ ❝❛❧❧❜❛❝❦❀
⑥

    Em caso de dúvidas, veja o novo código completo da classe Teclado:

✴✴ ❛rq✉✐✈♦ t❡❝❧❛❞♦✳❥s ✲ ✈❡rsã♦ ❢✐♥❛❧
✴✴ ❈ó❞✐❣♦s ❞❡ t❡❝❧❛s ✲ ❛q✉✐ ✈ã♦ t♦❞♦s ♦s q✉❡ ❢♦r❡♠ ♥❡❝❡ssár✐♦s
✈❛r ❙❊❚❆❴❊❙◗❯❊❘❉❆ ❂ ✸✼❀
✈❛r ❙❊❚❆❴❉■❘❊■❚❆ ❂ ✸✾❀
✈❛r ❊❙P❆❈❖ ❂ ✸✷❀

❢✉♥❝t✐♦♥ ❚❡❝❧❛❞♦✭❡❧❡♠❡♥t♦✮ ④
   t❤✐s✳❡❧❡♠❡♥t♦ ❂ ❡❧❡♠❡♥t♦❀

   ✴✴ ❆rr❛② ❞❡ t❡❝❧❛s ♣r❡ss✐♦♥❛❞❛s

                                                                                        61


[PAGINA 69]
3.3. Efetuando disparos — detectando somente o primeiro keydown   Casa do Código


     t❤✐s✳♣r❡ss✐♦♥❛❞❛s ❂ ❬❪❀

     ✴✴ ❆rr❛② ❞❡ t❡❝❧❛s ❞✐s♣❛r❛❞❛s
     t❤✐s✳❞✐s♣❛r❛❞❛s ❂ ❬❪❀

     ✴✴ ❋✉♥çõ❡s ❞❡ ❞✐s♣❛r♦
     t❤✐s✳❢✉♥❝♦❡s❉✐s♣❛r♦ ❂ ❬❪❀

     ✈❛r t❡❝❧❛❞♦ ❂ t❤✐s❀

     ❡❧❡♠❡♥t♦✳❛❞❞❊✈❡♥t▲✐st❡♥❡r✭✬❦❡②❞♦✇♥✬✱ ❢✉♥❝t✐♦♥✭❡✈❡♥t♦✮ ④
        ✈❛r t❡❝❧❛ ❂ ❡✈❡♥t♦✳❦❡②❈♦❞❡❀ ✴✴ ❚♦r♥❛♥❞♦ ♠❛✐s ❧❡❣í✈❡❧ ❀✮
        t❡❝❧❛❞♦✳♣r❡ss✐♦♥❛❞❛s❬t❡❝❧❛❪ ❂ tr✉❡❀

         ✴✴ ❉✐s♣❛r❛r s♦♠❡♥t❡ s❡ ❢♦r ♦ ♣r✐♠❡✐r♦ ❦❡②❞♦✇♥ ❞❛ t❡❝❧❛
         ✐❢ ✭t❡❝❧❛❞♦✳❢✉♥❝♦❡s❉✐s♣❛r♦❬t❡❝❧❛❪ ✫✫
             ✦ t❡❝❧❛❞♦✳❞✐s♣❛r❛❞❛s❬t❡❝❧❛❪✮ ④

               t❡❝❧❛❞♦✳❞✐s♣❛r❛❞❛s❬t❡❝❧❛❪ ❂ tr✉❡❀
               t❡❝❧❛❞♦✳❢✉♥❝♦❡s❉✐s♣❛r♦❬t❡❝❧❛❪ ✭✮ ❀
        ⑥
     ⑥✮❀

     ❡❧❡♠❡♥t♦✳❛❞❞❊✈❡♥t▲✐st❡♥❡r✭✬❦❡②✉♣✬✱ ❢✉♥❝t✐♦♥✭❡✈❡♥t♦✮ ④
        t❡❝❧❛❞♦✳♣r❡ss✐♦♥❛❞❛s❬❡✈❡♥t♦✳❦❡②❈♦❞❡❪ ❂ ❢❛❧s❡❀
        t❡❝❧❛❞♦✳❞✐s♣❛r❛❞❛s❬❡✈❡♥t♦✳❦❡②❈♦❞❡❪ ❂ ❢❛❧s❡❀
     ⑥✮❀
⑥
❚❡❝❧❛❞♦✳♣r♦t♦t②♣❡ ❂ ④
   ♣r❡ss✐♦♥❛❞❛✿ ❢✉♥❝t✐♦♥✭t❡❝❧❛✮ ④
      r❡t✉r♥ t❤✐s✳♣r❡ss✐♦♥❛❞❛s❬t❡❝❧❛❪❀
   ⑥✱
   ❞✐s♣❛r♦✉✿ ❢✉♥❝t✐♦♥✭t❡❝❧❛✱ ❝❛❧❧❜❛❝❦✮ ④
      t❤✐s✳❢✉♥❝♦❡s❉✐s♣❛r♦❬t❡❝❧❛❪ ❂ ❝❛❧❧❜❛❝❦❀
   ⑥
⑥

    É bastante abstrato, mas se conseguirmos programar de maneira mais
geral agora, teremos um game engine bastante robusto e prático para criar

62


[PAGINA 70]
Casa do Código            Capítulo 3. A interação com o jogador — leitura apurada do teclado



novos jogos de maneira extremamente veloz!

Crie a classe Heroi como um sprite
    Para nosso código funcionar, temos que criar o sprite do herói. Como
o sprite é responsável pelo seu próprio comportamento, ele deve receber o
objeto que controla o teclado para poder decidir o que vai fazer em cada ciclo
da animação.
    O herói também deve ter o método atirar, chamado no teste.
✴✴ ❛rq✉✐✈♦✿ ❤❡r♦✐✳❥s
❢✉♥❝t✐♦♥ ❍❡r♦✐✭❝♦♥t❡①t✱ t❡❝❧❛❞♦✮ ④
   t❤✐s✳❝♦♥t❡①t ❂ ❝♦♥t❡①t❀
   t❤✐s✳t❡❝❧❛❞♦ ❂ t❡❝❧❛❞♦❀
   t❤✐s✳① ❂ ✵❀
   t❤✐s✳② ❂ ✵❀
⑥
❍❡r♦✐✳♣r♦t♦t②♣❡ ❂ ④
   ❛t✉❛❧✐③❛r✿ ❢✉♥❝t✐♦♥✭✮ ④

    ⑥✱
    ❞❡s❡♥❤❛r✿ ❢✉♥❝t✐♦♥✭✮ ④

    ⑥✱
    ❛t✐r❛r✿ ❢✉♥❝t✐♦♥✭✮ ④

    ⑥
⑥

    No método atualizar, lemos o estado do teclado e movemos o person-
agem de acordo. Também não custa nada impedir que ultrapasse as bordas
da tela:
❛t✉❛❧✐③❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✐❢ ✭t❤✐s✳t❡❝❧❛❞♦✳♣r❡ss✐♦♥❛❞❛✭❙❊❚❆❴❊❙◗❯❊❘❉❆✮ ✫✫ t❤✐s✳① ❃ ✵✮
      t❤✐s✳① ✲❂ ✶✵❀
   ❡❧s❡ ✐❢ ✭t❤✐s✳t❡❝❧❛❞♦✳♣r❡ss✐♦♥❛❞❛✭❙❊❚❆❴❉■❘❊■❚❆✮ ✫✫
            t❤✐s✳① ❁ t❤✐s✳❝♦♥t❡①t✳❝❛♥✈❛s✳✇✐❞t❤ ✲ ✷✵✮
      t❤✐s✳① ✰❂ ✶✵❀
⑥✱

                                                                                         63


[PAGINA 71]
3.3. Efetuando disparos — detectando somente o primeiro keydown   Casa do Código


    No método desenhar... bem, eu vou continuar mantendo as coisas simples
e fazer um simples retângulo. No capítulo sobre spritesheets (4) a coisa vai
ficar mais interessante, prometo!

❞❡s❡♥❤❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   t❤✐s✳❝♦♥t❡①t✳❢✐❧❧❘❡❝t✭t❤✐s✳①✱ t❤✐s✳②✱ ✷✵✱ ✺✵✮❀
⑥✱

    Agora, a parte mais interessante: fazê-lo atirar. Neste ponto, devemos ler
novamente o estado do teclado para saber para que lado o tiro vai. Vamos
aproveitar a classe Bola que já temos:

❛t✐r❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✈❛r t✐r♦ ❂ ♥❡✇ ❇♦❧❛✭t❤✐s✳❝♦♥t❡①t✮❀
   t✐r♦✳① ❂ t❤✐s✳① ✰ ✶✵❀
   t✐r♦✳② ❂ t❤✐s✳② ✰ ✶✵❀
   t✐r♦✳r❛✐♦ ❂ ✷❀
   t✐r♦✳❝♦r ❂ ✬r❡❞✬❀

     ✐❢ ✭t❤✐s✳t❡❝❧❛❞♦✳♣r❡ss✐♦♥❛❞❛✭❙❊❚❆❴❊❙◗❯❊❘❉❆✮✮
        t✐r♦✳✈❡❧♦❝✐❞❛❞❡❳ ❂ ✲✷✵❀
     ❡❧s❡
        t✐r♦✳✈❡❧♦❝✐❞❛❞❡❳ ❂ ✷✵❀

     ✴✴ ◆ã♦ t❡♥❤♦ ❝♦♠♦ ✐♥❝❧✉✐r ♥❛❞❛ ♥❛ ❛♥✐♠❛çã♦✦
     t❤✐s✳❛♥✐♠❛❝❛♦✳♥♦✈♦❙♣r✐t❡✭t✐r♦✮❀
⑥

    Como o herói vai acrescentar um tiro à animação sem uma referência a
ela? Vamos recebê-la também no construtor:

❢✉♥❝t✐♦♥ ❍❡r♦✐✭❝♦♥t❡①t✱ t❡❝❧❛❞♦✱ ❛♥✐♠❛❝❛♦✮ ④
   t❤✐s✳❝♦♥t❡①t ❂ ❝♦♥t❡①t❀
   t❤✐s✳t❡❝❧❛❞♦ ❂ t❡❝❧❛❞♦❀
   t❤✐s✳❛♥✐♠❛❝❛♦ ❂ ❛♥✐♠❛❝❛♦❀
   t❤✐s✳① ❂ ✵❀
   t❤✐s✳② ❂ ✵❀
⑥

     E passá-la no aplicativo de teste:

64


[PAGINA 72]
Casa do Código             Capítulo 3. A interação com o jogador — leitura apurada do teclado



✈❛r ❤❡r♦✐ ❂ ♥❡✇ ❍❡r♦✐✭❝♦♥t❡①t✱ t❡❝❧❛❞♦✱ ❛♥✐♠❛❝❛♦✮❀

     Faça o teste. Se você fez tudo correto, o herói deve atirar ao teclarmos
espaço. Mas ainda temos dois pequenos problemas:

1) a classe Bola está programada para quicar, portanto não vemos os tiros
   sumirem da tela (figura 3.6);

2) quando parado, o herói atira sempre para a direita.




       Figura 3.6: Os tiros ficam quicando na tela, ao invés de sumirem


    Para resolver o primeiro problema, vamos mudar o algoritmo do método
atualizar da classe Bola. Recomendo que este teste referencie sua própria
cópia do arquivo bola.js, para não alterar o comportamento dos testes
anteriores.

❛t✉❛❧✐③❛r✿ ❢✉♥❝t✐♦♥✭✮ ④

     ✴✴ ❚✐r❛♠♦s ♦s t❡st❡s q✉❡ q✉✐❝❛♠ ❛ ❜♦❧❛ ♥❛ ❜♦r❞❛ ❞♦ ❈❛♥✈❛s

     t❤✐s✳① ✰❂ t❤✐s✳✈❡❧♦❝✐❞❛❞❡❳❀
     t❤✐s✳② ✰❂ t❤✐s✳✈❡❧♦❝✐❞❛❞❡❨❀
⑥✱

                                                                                          65


[PAGINA 73]
3.3. Efetuando disparos — detectando somente o primeiro keydown   Casa do Código


    Quanto à direção do tiro, criamos no Heroi um atributo que guarda a
sua direção:

✴✴ ❈ó❞✐❣♦s ú♥✐❝♦s ♣❛r❛ ❛s ❞✐r❡çõ❡s
✈❛r ❉■❘❊❈❆❖❴❊❙◗❯❊❘❉❆ ❂ ✶❀
✈❛r ❉■❘❊❈❆❖❴❉■❘❊■❚❆ ❂ ✷❀

❢✉♥❝t✐♦♥ ❍❡r♦✐✭❝♦♥t❡①t✱ t❡❝❧❛❞♦✱ ❛♥✐♠❛❝❛♦✮ ④
   t❤✐s✳❝♦♥t❡①t ❂ ❝♦♥t❡①t❀
   t❤✐s✳t❡❝❧❛❞♦ ❂ t❡❝❧❛❞♦❀
   t❤✐s✳❛♥✐♠❛❝❛♦ ❂ ❛♥✐♠❛❝❛♦❀
   t❤✐s✳① ❂ ✵❀
   t❤✐s✳② ❂ ✵❀

     ✴✴ ❉✐r❡çã♦ ♣❛❞rã♦
     t❤✐s✳❞✐r❡❝❛♦ ❂ ❉■❘❊❈❆❖❴❉■❘❊■❚❆❀
⑥

   Desta forma, ao movimentar o herói, guardamos a direção em que ele se
encontra nesse atributo:

❛t✉❛❧✐③❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✐❢ ✭t❤✐s✳t❡❝❧❛❞♦✳♣r❡ss✐♦♥❛❞❛✭❙❊❚❆❴❊❙◗❯❊❘❉❆✮
         ✫✫ t❤✐s✳① ❃ ✵✮ ④
      t❤✐s✳❞✐r❡❝❛♦ ❂ ❉■❘❊❈❆❖❴❊❙◗❯❊❘❉❆❀
      t❤✐s✳① ✲❂ ✶✵❀
   ⑥
   ❡❧s❡ ✐❢ ✭t❤✐s✳t❡❝❧❛❞♦✳♣r❡ss✐♦♥❛❞❛✭❙❊❚❆❴❉■❘❊■❚❆✮ ✫✫
            t❤✐s✳① ❁ t❤✐s✳❝♦♥t❡①t✳❝❛♥✈❛s✳✇✐❞t❤ ✲ ✷✵✮ ④
      t❤✐s✳❞✐r❡❝❛♦ ❂ ❉■❘❊❈❆❖❴❉■❘❊■❚❆❀
      t❤✐s✳① ✰❂ ✶✵❀
   ⑥
⑥✱

   Por fim, basta ler essa direção ao soltar o tiro, em vez do estado de deter-
minada tecla:

❛t✐r❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✴✴ ✳✳✳


66


[PAGINA 74]
Casa do Código            Capítulo 3. A interação com o jogador — leitura apurada do teclado



    ✴✴ ▲❡♥❞♦ ❛ ❞✐r❡çã♦ ❛t✉❛❧
    ✐❢ ✭t❤✐s✳❞✐r❡❝❛♦ ❂❂ ❉■❘❊❈❆❖❴❊❙◗❯❊❘❉❆✮
       t✐r♦✳✈❡❧♦❝✐❞❛❞❡❳ ❂ ✲✷✵❀
    ❡❧s❡
       t✐r♦✳✈❡❧♦❝✐❞❛❞❡❳ ❂ ✷✵❀

    ✴✴ ✳✳✳
⑥

    Pronto! Temos um herói que se movimenta e atira dentro de um loop
de animação. Embora ainda esteja muito básico, é preciso que os conceitos
aprendidos fiquem bem fixados para seguirmos para as próximas etapas. Pro-
cure reler e refazer os códigos de cada capítulo diversas vezes. Tente tam-
bém fazer algumas coisas diferentes, como mover ou atirar na vertical!
Para isso, os códigos de teclas são 38 (acima) e 40 (abaixo), e as alterações
na posição y dos sprites serão as mesmas já feitas para x, somente incremen-
tando a partir da velocidadeY. Experimente!
    No próximo capítulo, introduzirei as folhas de sprites (spritesheets), que
nos permitirão animar nosso herói a partir de imagens.




                                                                                        67


[PAGINA 75]


[PAGINA 76]
Capítulo 4

Folhas de sprites — spritesheets
4.1 Conceito e abordagem utilizada
Um pequeno game engine está começando a tomar forma. Já temos um modo
robusto de controlar o loop de animação e capturar a entrada do usuário no
teclado de uma maneira eficiente para jogos.
    Neste capítulo, avançaremos um pouco além e faremos algo muito inter-
essante e fundamental: as spritesheets (folhas de sprites). Um sprite, como
você aprendeu no capítulo 2.1, é cada elemento controlado pelo loop de an-
imação (o herói, um inimigo, um bloco ou plataforma etc.). Uma folha de
sprites é uma imagem contendo várias partes de uma animação. Essas partes
são alternadas constantemente para produzir o movimento de um ou mais
sprites.


[PAGINA 77]
4.1. Conceito e abordagem utilizada                                  Casa do Código




                        Figura 4.1: Folha de sprites (spritesheet)


    É uma boa prática carregar imagens maiores contendo uma porção de
outras menores, em vez de ter cada pequena imagem em seu próprio arquivo.
Lembre-se de que, em ambiente web, cada imagem requer nova conexão do
browser com o servidor.
    Programar animações com spritesheets pode ser tão simples ou tão tra-
balhoso quanto você desejar ou precisar, dependendo da abordagem uti-
lizada. No livro Core HTML5 Canvas[1], de David Geary, as posições de
cada figurinha (x, y, largura e altura) dentro da spritesheet são chumbadas
em grandes arrays:

✈❛r s♣r✐t❡ ❂ ❬ ❬✵✱ ✼✶✱ ✾✵✱ ✽✵❪✱
               ❬✹✵✱ ✼✶✱ ✽✵✱ ✽✺❪✱ ✳✳✳ ❪❀ ✴✴ ❈♦♥t✐♥✉❛✳✳✳

    Essa abordagem é bastante econômica em termos do espaço ocupado
pelas imagens, mas gera muito trabalho extra para coletar a posição de
cada imagem e, principalmente, para enquadrá-las adequadamente. Aqui,
adotaremos uma abordagem bastante sistematizada:

     • cada spritesheet será dividida em espaços iguais, por isso as imagens
       devem estar corretamente distribuídas;

     • cada linha da spritesheet corresponderá a um estado do sprite (ex.:
       parado, correndo para a direita, correndo para a esquerda);

     • a animação de um estado usará somente as figuras na sua linha própria.



70


[PAGINA 78]
Casa do Código                               Capítulo 4. Folhas de sprites — spritesheets



     Isso gera grande quantidade de espaço vazio na imagem, aumentando o
tamanho do arquivo, mas certamente facilitará muito a programação. Tenha
em mente que esta não é a única abordagem válida, mas para fins didáticos
é a que iremos utilizar V convenhamos, o modo mais econômico descrito no
livro Core HTML5 Canvas é totalmente improdutivo, em especial quando o
foco é o aprendizado das técnicas de programação, não de enquadramento de
imagens.




Figura 4.2: Spritesheet dividida em partes iguais e organizando os estados por
linhas



     O CorelDraw possui a ferramenta Papel Gráfico, que cria um quadric-
  ulado dividindo uma área em partes iguais. Neste programa e também
  no Photoshop, Illustrator e em outros, podemos usar as réguas e linhas-
  guia. Se você não conhece estes recursos, sugiro que pesquise a respeito.
  Sugestões:
     http://coreldrawtips.com/site/using-the-graph-paper-tool-in-coreldraw
     http://helpx.adobe.com/br/photoshop/using/grid-guides.html




                                                                                      71


[PAGINA 79]
4.2. Carregando imagens e fazendo recortes (clipping)        Casa do Código


4.2      Carregando imagens e fazendo recortes
         (clipping)
Carregar uma imagem do servidor pelo JavaScript é bastante simples.
Primeiro instanciamos um objeto Image, em seguida, setamos seu atributo
src para o caminho da imagem:

✈❛r ✐♠❣❙♦♥✐❝ ❂ ♥❡✇ ■♠❛❣❡✭✮❀
✐♠❣❙♦♥✐❝✳sr❝ ❂ ✬s♣r✐t❡s❤❡❡t✳♣♥❣✬❀

   A imagem possui o evento onload, que é disparado quando o carrega-
mento da imagem está completo:

✐♠❣❙♦♥✐❝✳♦♥❧♦❛❞ ❂ ❢✉♥❝t✐♦♥✭✮ ④ ✳✳✳ ⑥

    Quando tivermos muitas imagens, o evento onload de cada uma pode
incrementar uma porcentagem ou barrinha de “carregando”. Isso ficará para
outra hora!
    Vamos agora fazer o clipping (enquadramento), que é o recorte da parte
exata da spritesheet que queremos. Por exemplo, suponha que queremos a
figurinha na linha 2, coluna 7 (contados a partir de zero). Na hora de pro-
gramar as animações, ficará muito mais fácil expressar dessa maneira. No
entanto, precisaremos calcular a posição (x, y) do recorte da imagem.

❁✦✲✲ ❛rq✉✐✈♦✿ ❝❧✐♣♣✐♥❣✳❤t♠❧ ✲✲❃
❁✦❉❖❈❚❨P❊ ❤t♠❧❃
❁❤t♠❧❃

❁❤❡❛❞❃
   ❁t✐t❧❡❃
      ❙♣r✐t❡s❤❡❡t ✲ r❡❝♦rt❡ ❡ ❡♥q✉❛❞r❛♠❡♥t♦ ✭❝❧✐♣♣✐♥❣✮
   ❁✴t✐t❧❡❃
❁✴❤❡❛❞❃

❁❜♦❞②❃
   ❁❝❛♥✈❛s ✐❞❂✧❝❛♥✈❛s❴❝❧✐♣♣✐♥❣✧ ✇✐❞t❤❂✧✺✵✵✧ ❤❡✐❣❤t❂✧✺✵✵✧❃
   ❁✴❝❛♥✈❛s❃
   ❁s❝r✐♣t❃

72


[PAGINA 80]
Casa do Código                             Capítulo 4. Folhas de sprites — spritesheets



      ✈❛r ✐♠❣❙♦♥✐❝ ❂ ♥❡✇ ■♠❛❣❡✭✮❀
      ✐♠❣❙♦♥✐❝✳sr❝ ❂ ✬s♣r✐t❡s❤❡❡t✳♣♥❣✬❀
      ✐♠❣❙♦♥✐❝✳♦♥❧♦❛❞ ❂ ❢✉♥❝t✐♦♥✭✮ ④
         ✴✴ ❆q✉✐ ❢❛r❡♠♦s ♦ ❝❧✐♣♣✐♥❣✦
      ⑥
   ❁✴s❝r✐♣t❃
❁✴❜♦❞②❃

❁✴❤t♠❧❃

    No evento onload da imagem, calcularemos as posições x e y do recorte.
Como estamos considerando quadros de tamanhos iguais, basta dividir a
largura total pelo número de colunas para obter a largura de um quadro. De-
pois basta multiplicar este valor pela coluna desejada, e temos a posição x
onde o recorte se inicia. Para a posição y, o processo é análogo a partir da
altura total e número de linhas:

✐♠❣❙♦♥✐❝✳♦♥❧♦❛❞ ❂ ❢✉♥❝t✐♦♥✭✮ ④
   ✴✴ P❛ss♦ ❡st❡s ✈❛❧♦r❡s ❝♦♥❢♦r♠❡ ❛ ♠✐♥❤❛ s♣r✐t❡s❤❡❡t
   ✈❛r ❧✐♥❤❛s ❂ ✸❀
   ✈❛r ❝♦❧✉♥❛s ❂ ✽❀

    ✴✴ ❉✐♠❡♥sã♦ ❞❡ ❝❛❞❛ q✉❛❞r♦
    ✈❛r ❧❛r❣✉r❛ ❂ ✐♠❣❙♦♥✐❝✳✇✐❞t❤ ✴ ❝♦❧✉♥❛s❀
    ✈❛r ❛❧t✉r❛ ❂ ✐♠❣❙♦♥✐❝✳❤❡✐❣❤t ✴ ❧✐♥❤❛s❀

    ✴✴ ◗✉❛❞r♦ q✉❡ ❡✉ q✉❡r♦ ✭❡①♣r❡ss♦ ❡♠ ❧✐♥❤❛ ❡ ❝♦❧✉♥❛✮
    ✈❛r q✉❡r♦▲✐♥❤❛ ❂ ✷❀
    ✈❛r q✉❡r♦❈♦❧✉♥❛ ❂ ✼❀

    ✴✴ P♦s✐çã♦ ❞❡ r❡❝♦rt❡
    ✈❛r ① ❂ ❧❛r❣✉r❛ ✯ q✉❡r♦❈♦❧✉♥❛❀
    ✈❛r ② ❂ ❛❧t✉r❛ ✯ q✉❡r♦▲✐♥❤❛❀

    ✴✴ ❈♦♥t✐♥✉❛✳✳✳
⑥

   Tendo calculado x, y, largura e altura, basta lembrarmos do método
drawImage do context (veja o capítulo 1.2). Este método pode ser chamado

                                                                                    73


[PAGINA 81]
4.2. Carregando imagens e fazendo recortes (clipping)   Casa do Código


de duas maneiras:

     • Desenhando uma imagem inteira:

❝♦♥t❡①t✳❞r❛✇■♠❛❣❡✭✐♠❛❣❡♠✱ ①✱ ②✱ ❧❛r❣✉r❛✱ ❛❧t✉r❛✮❀

     • Fazendo clipping:

❝♦♥t❡①t✳❞r❛✇■♠❛❣❡✭
   ✐♠❛❣❡♠✱
   ①❖r✐❣❡♠✱
   ②❖r✐❣❡♠✱
   ❧❛r❣✉r❛❖r✐❣❡♠✱
   ❛❧t✉r❛❖r✐❣❡♠✱
   ①❉❡st✐♥♦✱
   ②❉❡st✐♥♦✱
   ❧❛r❣✉r❛❉❡st✐♥♦✱
   ❛❧t✉r❛❉❡st✐♥♦
✮❀

     Finalizemos, então, o nosso código:

✈❛r ❝♦♥t❡①t ❂
    ❞♦❝✉♠❡♥t✳❣❡t❊❧❡♠❡♥t❇②■❞✭✬❝❛♥✈❛s❴❝❧✐♣♣✐♥❣✬✮✳❣❡t❈♦♥t❡①t✭✬✷❞✬✮❀
❝♦♥t❡①t✳❞r❛✇■♠❛❣❡✭
   ✐♠❣❙♦♥✐❝✱
   ①✱
   ②✱
   ❧❛r❣✉r❛✱
   ❛❧t✉r❛✱
   ✶✵✵✱ ✴✴ P♦s✐çã♦ ♥♦ ❝❛♥✈❛s ♦♥❞❡ q✉❡r♦ ❞❡s❡♥❤❛r
   ✶✵✵✱
   ❧❛r❣✉r❛✱
   ❛❧t✉r❛
✮❀

     Veja o resultado no browser:




74


[PAGINA 82]
Casa do Código                                Capítulo 4. Folhas de sprites — spritesheets




  Figura 4.3: Fazendo clipping na spritesheet (quadro na linha 2, coluna 7)



4.3      Animações de sprite — a classe Spritesheet
Daremos prosseguimento à confecção do nosso game engine. A classe
Spritesheet será responsável por:

      • Avançar a animação, escolhendo qual o quadro a ser desenhado no mo-
        mento;

      • Calcular as posições de recorte e realizar o clipping, dados os números
        de linhas e colunas;

      • Gerenciar o tempo entre um quadro e outro.

    Como de costume, escreveremos primeiro um código de teste, com o qual
tentamos manter a interface da classe o mais enxuta possível. Inicialmente,
faremos o Sonic correr para a direita. Cada quadro terá a duração de 60 milis-
segundos, podendo ser ajustado posteriormente.



                                                                                       75


[PAGINA 83]
4.3. Animações de sprite — a classe Spritesheet                  Casa do Código




                            Figura 4.4: Sonic correndo na tela


    Dessa forma, a classe Spritesheet deverá alternar para nós os quadros
da segunda linha (índice 1, contado a partir de zero — veja figura 4.2). Ainda
não usaremos a classe Animacao, apenas uma função simples que servirá
como game loop.

❁✦✲✲ ❛rq✉✐✈♦✿ t❡st❡✲s♣r✐t❡s❤❡❡t✲✶✳❤t♠❧ ✲✲❃
❁✦❉❖❈❚❨P❊ ❤t♠❧❃
❁❤t♠❧❃

❁❤❡❛❞❃
   ❁t✐t❧❡❃❚❡st❛♥❞♦ ❛ ❝❧❛ss❡ ❙♣r✐t❡s❤❡❡t❁✴t✐t❧❡❃
   ❁s❝r✐♣t sr❝❂✧s♣r✐t❡s❤❡❡t✳❥s✧❃❁✴s❝r✐♣t❃
❁✴❤❡❛❞❃

❁❜♦❞②❃
   ❁❝❛♥✈❛s ✐❞❂✧❝❛♥✈❛s❴s♣r✐t❡s❤❡❡t❴✶✧ ✇✐❞t❤❂✧✺✵✵✧ ❤❡✐❣❤t❂✧✺✵✵✧❃
   ❁✴❝❛♥✈❛s❃
   ❁s❝r✐♣t❃
      ✴✴ ❱❛♠♦s t❡♥t❛r ♠❛♥❞❛r ♥❛ ❙♣r✐t❡s❤❡❡t
      ✴✴ ❞❛ ♠❛♥❡✐r❛ ♠❛✐s s✐♠♣❧❡s✦

76


[PAGINA 84]
Casa do Código                            Capítulo 4. Folhas de sprites — spritesheets



   ❁✴s❝r✐♣t❃
❁✴❜♦❞②❃

❁✴❤t♠❧❃

    No JavaScript, queremos dizer à classe Spritesheet os números de lin-
has e colunas, e escolhemos qual linha queremos animar. As colunas deverão
ser alternadas automaticamente.
    Também passamos no construtor o context do Canvas e a imagem a ser
desenhada:

✈❛r ❝♦♥t❡①t ❂ ❞♦❝✉♠❡♥t✳❣❡t❊❧❡♠❡♥t❇②■❞✭✬❝❛♥✈❛s❴s♣r✐t❡s❤❡❡t❴✶✬✮
              ✳❣❡t❈♦♥t❡①t✭✬✷❞✬✮❀

✈❛r ✐♠❣❙♦♥✐❝ ❂ ♥❡✇ ■♠❛❣❡✭✮❀
✐♠❣❙♦♥✐❝✳sr❝ ❂ ✬s♣r✐t❡s❤❡❡t✳♣♥❣✬❀

✴✴ ◗✉❡r♦ ♣❛ss❛r✿ ❝♦♥t❡①t✱ ✐♠❛❣❡♠✱ ❧✐♥❤❛s✱ ❝♦❧✉♥❛s
✈❛r s❤❡❡t ❂ ♥❡✇ ❙♣r✐t❡s❤❡❡t✭❝♦♥t❡①t✱ ✐♠❣❙♦♥✐❝✱ ✸✱ ✽✮❀

✴✴ ❉✉r❛çã♦ ❞❡ ❝❛❞❛ q✉❛❞r♦
s❤❡❡t✳✐♥t❡r✈❛❧♦ ❂ ✻✵❀

✴✴ ✧❝♦rr❡♥❞♦ ♣❛r❛ ❞✐r❡✐t❛✧
s❤❡❡t✳❧✐♥❤❛ ❂ ✶❀

✴✴ ❆♥✐♠❛çã♦
✐♠❣❙♦♥✐❝✳♦♥❧♦❛❞ ❂ ❣❛♠❡▲♦♦♣❀

    Na função gameLoop, ordeno à Spritesheet que avance um quadro
e que desenhe o quadro atual na posição que eu mandar:

❢✉♥❝t✐♦♥ ❣❛♠❡▲♦♦♣✭✮ ④
   ❝♦♥t❡①t✳❝❧❡❛r❘❡❝t✭✵✱ ✵✱ ❝♦♥t❡①t✳❝❛♥✈❛s✳✇✐❞t❤✱
         ❝♦♥t❡①t✳❝❛♥✈❛s✳❤❡✐❣❤t✮❀

   ✴✴ ❆✈❛♥ç❛r ♥❛ ❛♥✐♠❛çã♦
   s❤❡❡t✳♣r♦①✐♠♦◗✉❛❞r♦✭✮❀


                                                                                  77


[PAGINA 85]
4.3. Animações de sprite — a classe Spritesheet               Casa do Código


     ✴✴ ❖♥❞❡ ❞❡s❡♥❤❛r ♦ q✉❛❞r♦ ❛t✉❛❧
     s❤❡❡t✳❞❡s❡♥❤❛r✭✶✵✵✱ ✶✵✵✮❀

     r❡q✉❡st❆♥✐♠❛t✐♦♥❋r❛♠❡✭❣❛♠❡▲♦♦♣✮❀
⑥

     Teste pronto, passemos ao esboço da classe Spritesheet:

❢✉♥❝t✐♦♥ ❙♣r✐t❡s❤❡❡t✭❝♦♥t❡①t✱ ✐♠❛❣❡♠✱ ❧✐♥❤❛s✱ ❝♦❧✉♥❛s✮ ④
   t❤✐s✳❝♦♥t❡①t ❂ ❝♦♥t❡①t❀
   t❤✐s✳✐♠❛❣❡♠ ❂ ✐♠❛❣❡♠❀
   t❤✐s✳♥✉♠▲✐♥❤❛s ❂ ❧✐♥❤❛s❀
   t❤✐s✳♥✉♠❈♦❧✉♥❛s ❂ ❝♦❧✉♥❛s❀
   t❤✐s✳✐♥t❡r✈❛❧♦ ❂ ✵❀
   t❤✐s✳❧✐♥❤❛ ❂ ✵❀
   t❤✐s✳❝♦❧✉♥❛ ❂ ✵❀
⑥
❙♣r✐t❡s❤❡❡t✳♣r♦t♦t②♣❡ ❂ ④
   ♣r♦①✐♠♦◗✉❛❞r♦✿ ❢✉♥❝t✐♦♥✭✮ ④

     ⑥✱
     ❞❡s❡♥❤❛r✿ ❢✉♥❝t✐♦♥✭①✱ ②✮ ④

     ⑥
⑥

    O cálculo do quadro atual é bem simples, bastando incrementar a coluna
atual e voltar para zero quando exceder o número de colunas:

♣r♦①✐♠♦◗✉❛❞r♦✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✐❢ ✭t❤✐s✳❝♦❧✉♥❛ ❁ t❤✐s✳♥✉♠❈♦❧✉♥❛s ✲ ✶✮
      t❤✐s✳❝♦❧✉♥❛✰✰❀
   ❡❧s❡
      t❤✐s✳❝♦❧✉♥❛ ❂ ✵❀
⑥✱

    Mas há um porém: como temos um intervalo de tempo definido para a
mudança de quadro, temos que levá-lo em conta! Isso não é difícil: vamos
manter um registro da última mudança e, a cada ciclo, verificar se já passou
o tempo especificado:

78


[PAGINA 86]
Casa do Código                              Capítulo 4. Folhas de sprites — spritesheets



♣r♦①✐♠♦◗✉❛❞r♦✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✴✴ ▼♦♠❡♥t♦ ❛t✉❛❧
   ✈❛r ❛❣♦r❛ ❂ ♥❡✇ ❉❛t❡✭✮✳❣❡t❚✐♠❡✭✮❀

     ✴✴ ❙❡ ❛✐♥❞❛ ♥ã♦ t❡♠ ú❧t✐♠♦ t❡♠♣♦ ♠❡❞✐❞♦
     ✐❢ ✭✦ t❤✐s✳✉❧t✐♠♦❚❡♠♣♦✮ t❤✐s✳✉❧t✐♠♦❚❡♠♣♦ ❂ ❛❣♦r❛❀

     ✴✴ ❏á é ❤♦r❛ ❞❡ ♠✉❞❛r ❞❡ ❝♦❧✉♥❛❄
     ✐❢ ✭❛❣♦r❛ ✲ t❤✐s✳✉❧t✐♠♦❚❡♠♣♦ ❁ t❤✐s✳✐♥t❡r✈❛❧♦✮ r❡t✉r♥❀

     ✐❢ ✭t❤✐s✳❝♦❧✉♥❛ ❁ t❤✐s✳♥✉♠❈♦❧✉♥❛s ✲ ✶✮
        t❤✐s✳❝♦❧✉♥❛✰✰❀
     ❡❧s❡
        t❤✐s✳❝♦❧✉♥❛ ❂ ✵❀

     ✴✴ ●✉❛r❞❛r ❤♦r❛ ❞❛ ú❧t✐♠❛ ♠✉❞❛♥ç❛
     t❤✐s✳✉❧t✐♠♦❚❡♠♣♦ ❂ ❛❣♦r❛❀
⑥✱

     No método desenhar, basta fazer o clipping como aprendemos:
❞❡s❡♥❤❛r✿ ❢✉♥❝t✐♦♥✭①✱ ②✮ ④
   ✈❛r ❧❛r❣✉r❛◗✉❛❞r♦ ❂ t❤✐s✳✐♠❛❣❡♠✳✇✐❞t❤ ✴ t❤✐s✳♥✉♠❈♦❧✉♥❛s❀
   ✈❛r ❛❧t✉r❛◗✉❛❞r♦ ❂ t❤✐s✳✐♠❛❣❡♠✳❤❡✐❣❤t ✴ t❤✐s✳♥✉♠▲✐♥❤❛s❀

     t❤✐s✳❝♦♥t❡①t✳❞r❛✇■♠❛❣❡✭
        t❤✐s✳✐♠❛❣❡♠✱
        ❧❛r❣✉r❛◗✉❛❞r♦ ✯ t❤✐s✳❝♦❧✉♥❛✱
        ❛❧t✉r❛◗✉❛❞r♦ ✯ t❤✐s✳❧✐♥❤❛✱
        ❧❛r❣✉r❛✱
        ❛❧t✉r❛✱
        ①✱
        ②✱
        ❧❛r❣✉r❛✱
        ❛❧t✉r❛
     ✮❀
⑥

    Neste ponto, já temos o Sonic correndo na tela, mas ainda sem alterar sua
posição.

                                                                                    79


[PAGINA 87]
4.4. Controle o herói pelo teclado e veja sua animação          Casa do Código


4.4 Controle o herói pelo teclado e veja sua
    animação
Chegou a hora de juntar a Spritesheet com as outras classes criadas an-
teriormente ( Animacao e Teclado). Vamos controlar o Sonic correndo!
    O sprite do Sonic terá sa funções de:

     • Configurar sua respectiva spritesheet;

     • Ler o estado das teclas de seta e mudar o estado do sprite;

     • Selecionar a linha na spritesheet correspondente ao estado desejado;

     • Responder ao loop de animação, implementando os velhos métodos
       atualizar e desenhar.

❁✦✲✲ ❛rq✉✐✈♦✿ t❡st❡✲s♣r✐t❡s❤❡❡t✲✷✳❤t♠❧ ✲✲❃
❁✦❉❖❈❚❨P❊ ❤t♠❧❃
❁❤t♠❧❃

❁❤❡❛❞❃
   ❁t✐t❧❡❃P❡rs♦♥❛❣❡♠ ❝♦♥tr♦❧á✈❡❧ ❡ ❛♥✐♠❛❞♦❁✴t✐t❧❡❃
   ❁s❝r✐♣t sr❝❂✧s♣r✐t❡s❤❡❡t✳❥s✧❃❁✴s❝r✐♣t❃
   ❁s❝r✐♣t sr❝❂✧❛♥✐♠❛❝❛♦✳❥s✧❃❁✴s❝r✐♣t❃
   ❁s❝r✐♣t sr❝❂✧t❡❝❧❛❞♦✳❥s✧❃❁✴s❝r✐♣t❃
   ❁s❝r✐♣t sr❝❂✧s♦♥✐❝✳❥s✧❃❁✴s❝r✐♣t❃
❁✴❤❡❛❞❃

❁❜♦❞②❃
   ❁❝❛♥✈❛s ✐❞❂✧❝❛♥✈❛s❴s♦♥✐❝✧ ✇✐❞t❤❂✧✺✵✵✧ ❤❡✐❣❤t❂✧✺✵✵✧❃❁✴❝❛♥✈❛s❃
   ❁s❝r✐♣t❃
      ✴✴ ▼♦✈❡r ✉♠ ♣❡rs♦♥❛❣❡♠ ♥✉♥❝❛ ❢♦✐ tã♦ ❢á❝✐❧✦
   ❁✴s❝r✐♣t❃
❁✴❜♦❞②❃

❁✴❤t♠❧❃

    Primeiro, façamos as referências do Canvas, como de costume. Depois,
criamos os controles de teclado, de animação e o Sonic. Este precisará ler o

80


[PAGINA 88]
Casa do Código                               Capítulo 4. Folhas de sprites — spritesheets



teclado para movimentar-se. Espero que você esteja percebendo que pratica-
mente tudo que criaremos seguirá este padrão:
✈❛r ❝❛♥✈❛s ❂ ❞♦❝✉♠❡♥t✳❣❡t❊❧❡♠❡♥t❇②■❞✭✬❝❛♥✈❛s❴s♦♥✐❝✬✮❀
✈❛r ❝♦♥t❡①t ❂ ❝❛♥✈❛s✳❣❡t❈♦♥t❡①t✭✬✷❞✬✮❀

✈❛r t❡❝❧❛❞♦ ❂ ♥❡✇ ❚❡❝❧❛❞♦✭❞♦❝✉♠❡♥t✮❀
✈❛r ❛♥✐♠❛❝❛♦ ❂ ♥❡✇ ❆♥✐♠❛❝❛♦✭❝♦♥t❡①t✮❀

✈❛r s♦♥✐❝ ❂ ♥❡✇ ❙♦♥✐❝✭❝♦♥t❡①t✱ t❡❝❧❛❞♦✮❀
s♦♥✐❝✳① ❂ ✵❀
s♦♥✐❝✳② ❂ ✷✵✵❀
❛♥✐♠❛❝❛♦✳♥♦✈♦❙♣r✐t❡✭s♦♥✐❝✮❀

❛♥✐♠❛❝❛♦✳❧✐❣❛r✭✮❀

Crie a classe Sonic
   Pelos comandos dados ao Sonic anteriormente, seu esqueleto conterá so-
mente o context, o teclado, a posição (x, y) e os métodos de sprite:
✴✴ ❛rq✉✐✈♦✿ s♦♥✐❝✳❥s
❢✉♥❝t✐♦♥ ❙♦♥✐❝✭❝♦♥t❡①t✱ t❡❝❧❛❞♦✮ ④
   t❤✐s✳❝♦♥t❡①t ❂ ❝♦♥t❡①t❀
   t❤✐s✳t❡❝❧❛❞♦ ❂ t❡❝❧❛❞♦❀
   t❤✐s✳① ❂ ✵❀
   t❤✐s✳② ❂ ✵❀
⑥
❙♦♥✐❝✳♣r♦t♦t②♣❡ ❂ ④
   ❛t✉❛❧✐③❛r✿ ❢✉♥❝t✐♦♥✭✮ ④

    ⑥✱
    ❞❡s❡♥❤❛r✿ ❢✉♥❝t✐♦♥✭✮ ④

    ⑥
⑥

     Uma das funções da classe Sonic é controlar sua spritesheet, portanto va-
mos criá-la no construtor. Optei por sempre receber as imagens pelo constru-
tor, pois assim o aplicativo principal terá controle sobre seu evento onload

                                                                                      81


[PAGINA 89]
4.4. Controle o herói pelo teclado e veja sua animação        Casa do Código


(por exemplo, para animar uma tela de loading que será criada posterior-
mente).

❢✉♥❝t✐♦♥ ❙♦♥✐❝✭❝♦♥t❡①t✱ t❡❝❧❛❞♦✱ ✐♠❛❣❡♠✮ ④
   t❤✐s✳❝♦♥t❡①t ❂ ❝♦♥t❡①t❀
   t❤✐s✳t❡❝❧❛❞♦ ❂ t❡❝❧❛❞♦❀
   t❤✐s✳① ❂ ✵❀
   t❤✐s✳② ❂ ✵❀

     ✴✴ ❈r✐❛♥❞♦ ❛ s♣r✐t❡s❤❡❡t ❛ ♣❛rt✐r ❞❛ ✐♠❛❣❡♠ r❡❝❡❜✐❞❛
     t❤✐s✳s❤❡❡t ❂ ♥❡✇ ❙♣r✐t❡s❤❡❡t✭❝♦♥t❡①t✱ ✐♠❛❣❡♠✱ ✸✱ ✽✮❀
     t❤✐s✳s❤❡❡t✳✐♥t❡r✈❛❧♦ ❂ ✻✵❀
⑥

     Arrumemos o teste para fornecer a imagem:

✈❛r ✐♠❣❙♦♥✐❝ ❂ ♥❡✇ ■♠❛❣❡✭✮❀
✐♠❣❙♦♥✐❝✳sr❝ ❂ ✬s♣r✐t❡s❤❡❡t✳♣♥❣✬❀

✈❛r s♦♥✐❝ ❂ ♥❡✇ ❙♦♥✐❝✭❝♦♥t❡①t✱ t❡❝❧❛❞♦✱ ✐♠❣❙♦♥✐❝✮❀

     Vamos também ligar a animação no onload:

✴✴ ◆♦ ❢✐♥❛❧ ❞♦ s❝r✐♣t
✐♠❣❙♦♥✐❝✳♦♥❧♦❛❞ ❂ ❢✉♥❝t✐♦♥✭✮ ④
   ❛♥✐♠❛❝❛♦✳❧✐❣❛r✭✮❀
⑥

Estados do sprite
    Já sabemos movimentar um sprite na tela a partir do teclado. No entanto,
o sprite do Sonic só deverá ser animado se alguma seta estiver pressionada;
do contrário, a animação de sprites não deve ocorrer. E ele deve ser animado
na direção correta. Aí entra a necessidade de termos bem definidos quais os
estados possíveis para o sprite Sonic.




82


[PAGINA 90]
Casa do Código                               Capítulo 4. Folhas de sprites — spritesheets




       Na teoria da Orientação a objetos, um estado é uma forma em que
    um objeto se encontra e que determina seu comportamento. Em esta-
    dos diferentes, a mesma mensagem (chamada de método) enviada a um
    objeto pode produzir comportamentos diferentes.
       Os estados são definidos a partir de um ou mais atributos de um
    objeto. Por exemplo, uma conta bancária pode estar em um estado
    NO_VERMELHO caso o saldo seja menor que zero.


    O estado do Sonic dependerá de dois atributos: direcao e andando.
Estando parado ou andando, ele pode estar virado para a direita ou para a
esquerda. Dessa forma, temos quatro estados possíveis para selecionar as im-
agens e animar (ou não) a partir da spritesheet.
    Vamos definir os as direções do Sonic com valores únicos e iniciar o es-
tado atual no construtor:

✈❛r ❙❖◆■❈❴❉■❘❊■❚❆ ❂ ✶❀
✈❛r ❙❖◆■❈❴❊❙◗❯❊❘❉❆ ❂ ✷❀

❢✉♥❝t✐♦♥ ❙♦♥✐❝✭❝♦♥t❡①t✱ t❡❝❧❛❞♦✱ ✐♠❛❣❡♠✮ ④
   t❤✐s✳❝♦♥t❡①t ❂ ❝♦♥t❡①t❀
   t❤✐s✳t❡❝❧❛❞♦ ❂ t❡❝❧❛❞♦❀
   t❤✐s✳① ❂ ✵❀
   t❤✐s✳② ❂ ✵❀

     ✴✴ ❈r✐❛♥❞♦ ❛ s♣r✐t❡s❤❡❡t ❛ ♣❛rt✐r ❞❛ ✐♠❛❣❡♠ r❡❝❡❜✐❞❛
     t❤✐s✳s❤❡❡t ❂ ♥❡✇ ❙♣r✐t❡s❤❡❡t✭❝♦♥t❡①t✱ ✐♠❛❣❡♠✱ ✸✱ ✽✮❀
     t❤✐s✳s❤❡❡t✳✐♥t❡r✈❛❧♦ ❂ ✻✵❀

     ✴✴ ❊st❛❞♦ ✐♥✐❝✐❛❧
     t❤✐s✳❛♥❞❛♥❞♦ ❂ ❢❛❧s❡❀
     t❤✐s✳❞✐r❡❝❛♦ ❂ ❙❖◆■❈❴❉■❘❊■❚❆❀
⑥

   Quero agora testar a seta para direita e movimentar o Sonic de acordo.
Caso o Sonic já não esteja nesse estado, eu tenho que iniciar a respectiva an-
imação na spritesheet. Ao disparar uma mudança de estado, sempre pode-

                                                                                      83


[PAGINA 91]
4.4. Controle o herói pelo teclado e veja sua animação         Casa do Código


mos checar o estado anterior e tomar as medidas necessárias. No método
atualizar, fazemos:

✐❢ ✭t❤✐s✳t❡❝❧❛❞♦✳♣r❡ss✐♦♥❛❞❛✭❙❊❚❆❴❉■❘❊■❚❆✮✮ ④
   ✴✴ ❙❡ ❥á ♥ã♦ ❡st❛✈❛ ♥❡st❡ ❡st❛❞♦✳✳✳
   ✐❢ ✭✦ t❤✐s✳❛♥❞❛♥❞♦ ⑤⑤ t❤✐s✳❞✐r❡❝❛♦ ✦❂ ❙❖◆■❈❴❉■❘❊■❚❆✮ ④
      ✴✴ ❙❡❧❡❝✐♦♥♦ ♦ q✉❛❞r♦ ❞❛ s♣r✐t❡s❤❡❡t
      t❤✐s✳s❤❡❡t✳❧✐♥❤❛ ❂ ✶❀
      t❤✐s✳s❤❡❡t✳❝♦❧✉♥❛ ❂ ✵❀
   ⑥

     ✴✴ ❝♦♥t✐♥✉❛ ✳✳✳
⑥

    Posicionamos a nossa spritesheet na primeira coluna (zero), da linha rel-
ativa ao Sonic indo para a direita. Ainda dentro do primeiro if, devemos
então definir o estado atual, animar a spritesheet e deslocar o Sonic:
✐❢ ✭t❤✐s✳t❡❝❧❛❞♦✳♣r❡ss✐♦♥❛❞❛✭❙❊❚❆❴❉■❘❊■❚❆✮✮ ④

     ✴✴ ✳✳✳

     ✴✴ ❈♦♥❢✐❣✉r♦ ♦ ❡st❛❞♦ ❛t✉❛❧
     t❤✐s✳❛♥❞❛♥❞♦ ❂ tr✉❡❀
     t❤✐s✳❞✐r❡❝❛♦ ❂ ❙❖◆■❈❴❉■❘❊■❚❆❀

     ✴✴ ◆❡st❡ ❡st❛❞♦✱ ❛ ❛♥✐♠❛çã♦ ❞❛ s♣r✐t❡s❤❡❡t ❞❡✈❡ r♦❞❛r
     t❤✐s✳s❤❡❡t✳♣r♦①✐♠♦◗✉❛❞r♦✭✮❀

     ✴✴ ❉❡s❧♦❝♦ ♦ ❙♦♥✐❝
     t❤✐s✳① ✰❂ t❤✐s✳✈❡❧♦❝✐❞❛❞❡❀
⑥

   Usamos um novo atributo, velocidade. Vamos iniciá-lo com um valor
padrão no construtor:
✴✴ P♦❞❡ s❡r ❛♦ ❢✐♥❛❧ ❞♦ ❝♦♥str✉t♦r
t❤✐s✳✈❡❧♦❝✐❞❛❞❡ ❂ ✶✵❀

   O mesmo raciocínio será usado para tratar a movimentação para a es-
querda. Continuando o método atualizar:

84


[PAGINA 92]
Casa do Código                               Capítulo 4. Folhas de sprites — spritesheets



❡❧s❡ ✐❢ ✭t❤✐s✳t❡❝❧❛❞♦✳♣r❡ss✐♦♥❛❞❛✭❙❊❚❆❴❊❙◗❯❊❘❉❆✮✮ ④
   ✐❢ ✭✦ t❤✐s✳❛♥❞❛♥❞♦ ⑤⑤ t❤✐s✳❞✐r❡❝❛♦ ✦❂ ❙❖◆■❈❴❊❙◗❯❊❘❉❆✮ ④
      t❤✐s✳s❤❡❡t✳❧✐♥❤❛ ❂ ✷❀ ✴✴ ❆t❡♥çã♦✱ ❛q✉✐ s❡rá ✷✦
      t❤✐s✳s❤❡❡t✳❝♦❧✉♥❛ ❂ ✵❀
   ⑥

    t❤✐s✳❛♥❞❛♥❞♦ ❂ tr✉❡❀
    t❤✐s✳❞✐r❡❝❛♦ ❂ ❙❖◆■❈❴❊❙◗❯❊❘❉❆❀
    t❤✐s✳s❤❡❡t✳♣r♦①✐♠♦◗✉❛❞r♦✭✮❀
    t❤✐s✳① ✲❂ t❤✐s✳✈❡❧♦❝✐❞❛❞❡❀ ✴✴ ❊ ❛q✉✐ é s✐♥❛❧ ❞❡ ♠❡♥♦s✦
⑥

    Finalmente, se nenhuma tecla de movimentação estiver pressionada, o
Sonic está parado. Devemos, no entanto, checar sua direção atual para saber
qual imagem do Sonic parado devemos usar, se virado para a esquerda ou
para a direita. Também não chamamos o método proximoQuadro, pois
neste estado não há animação.

❡❧s❡ ④
   ✐❢ ✭t❤✐s✳❞✐r❡❝❛♦ ❂❂ ❙❖◆■❈❴❉■❘❊■❚❆✮
       t❤✐s✳s❤❡❡t✳❝♦❧✉♥❛ ❂ ✵❀
   ❡❧s❡ ✐❢ ✭t❤✐s✳❞✐r❡❝❛♦ ❂❂ ❙❖◆■❈❴❊❙◗❯❊❘❉❆✮
       t❤✐s✳s❤❡❡t✳❝♦❧✉♥❛ ❂ ✶❀

    t❤✐s✳s❤❡❡t✳❧✐♥❤❛ ❂ ✵❀
    t❤✐s✳❛♥❞❛♥❞♦ ❂ ❢❛❧s❡❀
⑥

    Todo este processamento está ocorrendo, mas sequer podemos ver o re-
sultado: o método desenhar não foi implementado! Aqui, podemos sim-
plesmente chamar o desenhar da classe Spritesheet:

❞❡s❡♥❤❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   t❤✐s✳s❤❡❡t✳❞❡s❡♥❤❛r✭t❤✐s✳①✱ t❤✐s✳②✮❀
⑥

    Isso é tudo! Divirta-se controlando o Sonic para os lados. Ele começa ini-
cialmente parado e virado para a direita, pois assim definimos no construtor,
como estado inicial.

                                                                                      85


[PAGINA 93]
4.4. Controle o herói pelo teclado e veja sua animação              Casa do Código


     No próximo capítulo, falarei sobre detecção de colisões, um aspecto fun-
damental da grande maioria dos jogos. Seja para golpear um inimigo, ou para
coletar argolas, a interação do sprite do personagem com os outros (inimigos,
blocos, plataformas) se dará através da colisão entre as áreas que ocupam na
tela.




                       Figura 4.5: Sprite controlado pelo teclado




86


[PAGINA 94]
Capítulo 5

Detecção de colisões
Chegou a hora de detectarmos colisões, ou seja, saber quando um elemento
toca outro na tela. Isso tornará possível saber quando um inimigo atacou o
herói ou foi atingido, ou quando o herói coletou um item. A partir de colisões,
disparamos inúmeros acontecimentos que são a base dos jogos, em especial
os de aventura e ação.


5.1 Colisão entre retângulos
Um dos métodos mais simples para detectar colisões é criar uma caixa delim-
itadora (bounding box) ao redor de cada sprite e verificar a intersecção entre
os retângulos:


[PAGINA 95]
5.1. Colisão entre retângulos                                        Casa do Código




Figura 5.1: Sprites colidindo: retângulos (bounding boxes) apresentam inter-
secção




                       Figura 5.2: Sem intersecção, não há colisão


   Mas, quem dera que tudo fosse perfeito! Isso pode nos trazer alguns prob-
lemas devido às áreas vazias dos sprites:




88


[PAGINA 96]
Casa do Código                                      Capítulo 5. Detecção de colisões




Figura 5.3: Retângulos intersectando sem haver a colisão real desejada. O
dragão colide com uma área vazia do sprite do herói.


    A abordagem que adotaremos para resolver este problema é a seguinte:
cada sprite poderá ter vários retângulos de colisão, demarcando suas princi-
pais áreas:




    Figura 5.4: Definindo vários bounding boxes para objetos irregulares


     Nosso controle agora ficará muito mais preciso e com qualidade bastante
satisfatória para a maioria dos casos. Colisão em pequenas áreas vazias serão
imperceptíveis devido à velocidade com que ocorrem as animações (e sempre
poderemos definir mais um retângulo onde acharmos necessário).
     Ganhamos também um bônus: na figura 5.4, temos uma ação de ataque (o
herói tentando socar o dragão). Podemos diferenciar quem conseguiu atacar
quem através de qual retângulo do herói colidiu com o retângulo do dragão.




                                                                                89


[PAGINA 97]
5.2. Teste da classe Colisor                                           Casa do Código


Interseção de retângulos




                               Figura 5.5: Intersecção de retângulos


      Pela geometria, dois retângulos se intersectam se:

      • (x1 + largura1) > x2 E

      • x1 < (x2 + largura2) E

      • (y1 + altura1) > y2 E

      • y1 < (y2 + altura2)

    No próximo tópico, iniciaremos o desenvolvimento de uma classe que
aplica essas fórmulas para detectar colisões entre sprites.


5.2       Teste da classe Colisor
Iniciaremos o desenvolvimento da classe responsável por colidir objetos.
Como de costume, iniciaremos por um pequeno aplicativo de teste onde
definimos como queremos interagir com a classe.


90


[PAGINA 98]
Casa do Código                                      Capítulo 5. Detecção de colisões



    Criaremos uma classe para essa nova funcionalidade. Começaremos
criando o aplicativo de teste, onde definimos de que forma queremos interagir
com a classe Colisor:

❁✦✲✲ ❛rq✉✐✈♦✿ t❡st❡✲❝♦❧✐s❛♦✲✶✳❤t♠❧ ✲✲❃
❁✦❉❖❈❚❨P❊ ❤t♠❧❃
❁❤t♠❧❃

❁❤❡❛❞❃
   ❁t✐t❧❡❃❉❡t❡❝çã♦ ❞❡ ❝♦❧✐sõ❡s❁✴t✐t❧❡❃
   ❁s❝r✐♣t sr❝❂✧❝♦❧✐s♦r✳❥s✧❃❁✴s❝r✐♣t❃
   ❁s❝r✐♣t sr❝❂✧❜♦❧❛✳❥s✧❃❁✴s❝r✐♣t❃
❁✴❤❡❛❞❃

❁❜♦❞②❃
   ❁❝❛♥✈❛s ✐❞❂✧❝❛♥✈❛s❴❝♦❧✐s❛♦✧ ✇✐❞t❤❂✧✺✵✵✧ ❤❡✐❣❤t❂✧✺✵✵✧❃
   ❁✴❝❛♥✈❛s❃
   ❁s❝r✐♣t❃
      ✴✴ ❆s ❜♦❧✐♥❤❛s✱ ❛❧é♠ ❞❡ q✉✐❝❛r✱ ❜❛t❡rã♦ ✉♠❛s ♥❛s ♦✉tr❛s
   ❁✴s❝r✐♣t❃
❁✴❜♦❞②❃

❁✴❤t♠❧❃

    No JavaScript, obtemos o canvas e seu context, e criamos algumas bolin-
has:

✈❛r ❝❛♥✈❛s ❂ ❞♦❝✉♠❡♥t✳❣❡t❊❧❡♠❡♥t❇②■❞✭✬❝❛♥✈❛s❴❝♦❧✐s❛♦✬✮❀
✈❛r ❝♦♥t❡①t ❂ ❝❛♥✈❛s✳❣❡t❈♦♥t❡①t✭✬✷❞✬✮❀

✈❛r ❜✶ ❂ ♥❡✇ ❇♦❧❛✭❝♦♥t❡①t✮❀
❜✶✳① ❂ ✷✵✵❀
❜✶✳② ❂ ✷✵✵❀
❜✶✳✈❡❧♦❝✐❞❛❞❡❳ ❂ ✶✵❀
❜✶✳✈❡❧♦❝✐❞❛❞❡❨ ❂ ✲✺❀
❜✶✳❝♦r ❂ ✬❜❧✉❡✬❀
❜✶✳r❛✐♦ ❂ ✷✵❀

✈❛r ❜✷ ❂ ♥❡✇ ❇♦❧❛✭❝♦♥t❡①t✮❀


                                                                                 91


[PAGINA 99]
5.2. Teste da classe Colisor                                  Casa do Código


❜✷✳① ❂ ✸✵✵❀
❜✷✳② ❂ ✸✵✵❀
❜✷✳✈❡❧♦❝✐❞❛❞❡❳ ❂ ✲✺❀
❜✷✳✈❡❧♦❝✐❞❛❞❡❨ ❂ ✶✵❀
❜✷✳❝♦r ❂ ✬r❡❞✬❀
❜✷✳r❛✐♦ ❂ ✸✵❀

     O próximo passo é criar o objeto Colisor e colocar nele os sprites:

✈❛r ❝♦❧✐s♦r ❂ ♥❡✇ ❈♦❧✐s♦r✭✮❀
❝♦❧✐s♦r✳♥♦✈♦❙♣r✐t❡✭❜✶✮❀
❝♦❧✐s♦r✳♥♦✈♦❙♣r✐t❡✭❜✷✮❀

    Agora, façamos o loop de animação. Por enquanto, este loop será uma
simples função. Perceba que, a cada ciclo, apenas realizamos as tarefas que
nossos loops já fazem e, em seguida, mandamos o colisor realizar seu pro-
cessamento. O colisor se encarregará de enviar mensagens aos objetos que
colidirem.

r❡q✉❡st❆♥✐♠❛t✐♦♥❋r❛♠❡✭❛♥✐♠❛r✮❀

❢✉♥❝t✐♦♥ ❛♥✐♠❛r✭✮ ④
   ✴✴ ▲✐♠♣❛♥❞♦ ❛ t❡❧❛
   ❝♦♥t❡①t✳❝❧❡❛r❘❡❝t✭✵✱ ✵✱ ❝❛♥✈❛s✳✇✐❞t❤✱ ❝❛♥✈❛s✳❤❡✐❣❤t✮❀

     ✴✴ ❆t✉❛❧✐③❛♥❞♦ ♦s s♣r✐t❡s
     ❜✶✳❛t✉❛❧✐③❛r✭✮❀
     ❜✷✳❛t✉❛❧✐③❛r✭✮❀

     ✴✴ ❉❡s❡♥❤❛♥❞♦
     ❜✶✳❞❡s❡♥❤❛r✭✮❀
     ❜✷✳❞❡s❡♥❤❛r✭✮❀

     ✴✴ Pr♦❝❡ss❛r ❝♦❧✐sõ❡s
     ❝♦❧✐s♦r✳♣r♦❝❡ss❛r✭✮❀

     r❡q✉❡st❆♥✐♠❛t✐♦♥❋r❛♠❡✭❛♥✐♠❛r✮❀
⑥



92


[PAGINA 100]
Casa do Código                                      Capítulo 5. Detecção de colisões



5.3     A classe Colisor
A classe Colisor, como definimos antes, terá inicialmente 2 métodos:
novoSprite e processar. Manteremos um array de sprites, da mesma
forma que a classe Animacao:
❢✉♥❝t✐♦♥ ❈♦❧✐s♦r✭✮ ④
   t❤✐s✳s♣r✐t❡s ❂ ❬❪❀
⑥
❈♦❧✐s♦r✳♣r♦t♦t②♣❡ ❂ ④
   ♥♦✈♦❙♣r✐t❡✿ ❢✉♥❝t✐♦♥✭s♣r✐t❡✮ ④
      t❤✐s✳s♣r✐t❡s✳♣✉s❤✭s♣r✐t❡✮❀
   ⑥✱
   ♣r♦❝❡ss❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
      ✴✴ ❆q✉✐ ❢❛r❡♠♦s ❛ ✈❡r✐❢✐❝❛çã♦ ❞❡ ❝♦❧✐sã♦
   ⑥
⑥

    O coração da classe é o método processar. Aqui, precisamos testar
quais sprites estão colidindo entre si. Faremos um algoritmo do tipo “todos
contra todos” no array de sprites, usando dois loops for aninhados. Para
cada elemento no array (primeiro loop), é testada sua colisão contra todos os
outros (segundo loop). Note que ainda estamos abstraindo a lógica de cálculo
da colisão:
♣r♦❝❡ss❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   ❢♦r ✭✈❛r ✐ ✐♥ t❤✐s✳s♣r✐t❡s✮ ④
      ❢♦r ✭✈❛r ❥ ✐♥ t❤✐s✳s♣r✐t❡s✮ ④
         ✴✴ ◆ã♦ ❝♦❧✐❞✐r ✉♠ s♣r✐t❡ ❝♦♠ ❡❧❡ ♠❡s♠♦
         ✐❢ ✭✐ ❂❂ ❥✮ ❝♦♥t✐♥✉❡❀

            ✴✴ ❆❜str❛✐r ❛ ❝♦❧✐sã♦
            t❤✐s✳t❡st❛r❈♦❧✐s❛♦✭t❤✐s✳s♣r✐t❡s❬✐❪✱ t❤✐s✳s♣r✐t❡s❬❥❪✮❀
        ⑥
    ⑥
⑥

    O novo método testarColisao irá fazer mais um “todos contra to-
dos”, agora entre os retângulos do primeiro sprite e os do segundo. Lembre-
se de que cada sprite poderá definir mais de um retângulo (figura 5.4). Dessa

                                                                                 93


[PAGINA 101]
5.3. A classe Colisor                                          Casa do Código


forma, criamos um label colisoes para podermos parar os dois loops logo
na primeira colisão entre retângulos detectada:

t❡st❛r❈♦❧✐s❛♦✿ ❢✉♥❝t✐♦♥✭s♣r✐t❡✶✱ s♣r✐t❡✷✮ ④
   ✴✴ ❖❜t❡r ♦s r❡tâ♥❣✉❧♦s ❞❡ ❝♦❧✐sã♦ ❞❡ ❝❛❞❛ s♣r✐t❡
   ✈❛r r❡ts✶ ❂ s♣r✐t❡✶✳r❡t❛♥❣✉❧♦s❈♦❧✐s❛♦✭✮❀
   ✈❛r r❡ts✷ ❂ s♣r✐t❡✷✳r❡t❛♥❣✉❧♦s❈♦❧✐s❛♦✭✮❀

     ✴✴ ❚❡st❛r ❛s ❝♦❧✐sõ❡s ❡♥tr❡ ❡❧❡s
     ❝♦❧✐s♦❡s✿
     ❢♦r ✭✈❛r ✐ ✐♥ r❡ts✶✮ ④
        ❢♦r ✭✈❛r ❥ ✐♥ r❡ts✷✮ ④
           ✴✴ ❆✐♥❞❛ ❛❜str❛✐♥❞♦ ❛ ❢ór♠✉❧❛✦
           ✐❢ ✭t❤✐s✳r❡t❛♥❣✉❧♦s❈♦❧✐❞❡♠✭r❡ts✶❬✐❪✱ r❡ts✷❬❥❪✮✮ ④
               ✴✴ ❊❧❡s ❝♦❧✐❞❡♠✱ ✈❛♠♦s ♥♦t✐❢✐❝á✲❧♦s
               s♣r✐t❡✶✳❝♦❧✐❞✐✉❈♦♠✭s♣r✐t❡✷✮❀
               s♣r✐t❡✷✳❝♦❧✐❞✐✉❈♦♠✭s♣r✐t❡✶✮❀

                    ✴✴ ◆ã♦ ♣r❡❝✐s❛ t❡r♠✐♥❛r ❞❡ ✈❡r t♦❞♦s ♦s r❡tâ♥❣✉❧♦s
                    ❜r❡❛❦ ❝♦❧✐s♦❡s❀
               ⑥
          ⑥
     ⑥
⑥

    Esta parte é muito importante, pois definimos uma nova interface que os
sprites deverão seguir para poderem participar do colisor. Essa interface é
formada por dois métodos:

     • retangulosColisao: deve devolver um array com os dados de cada
       retângulo;

     • colidiuCom(sprite): recebe a notificação de que o sprite colidiu
       com outro (recebido como parâmetro)

     Nós abstraímos mais um pouco, deixando para o final a função que veri-
fica se dois retângulos colidem. Considero uma excelente prática ir isolando
as partes “difíceis” ou que não têm muito a ver com o algoritmo sendo criado:


94


[PAGINA 102]
Casa do Código                                      Capítulo 5. Detecção de colisões



r❡t❛♥❣✉❧♦s❈♦❧✐❞❡♠✿ ❢✉♥❝t✐♦♥✭r❡t✶✱ r❡t✷✮ ④
   ✴✴ ❋ór♠✉❧❛ ❞❡ ✐♥t❡rs❡çã♦ ❞❡ r❡tâ♥❣✉❧♦s
   r❡t✉r♥ ✭r❡t✶✳① ✰ r❡t✶✳❧❛r❣✉r❛✮ ❃ r❡t✷✳① ✫✫
          r❡t✶✳① ❁ ✭r❡t✷✳① ✰ r❡t✷✳❧❛r❣✉r❛✮ ✫✫
          ✭r❡t✶✳② ✰ r❡t✶✳❛❧t✉r❛✮ ❃ r❡t✷✳② ✫✫
          r❡t✶✳② ❁ ✭r❡t✷✳② ✰ r❡t✷✳❛❧t✉r❛✮❀
⑥


5.4 Criando um sprite colidível
Agora que temos nosso Colisor, vamos criar uma nova versão da classe
Bola seguindo a interface exigida por este, além da interface de animação já
vista anteriormente:
❢✉♥❝t✐♦♥ ❇♦❧❛✭❝♦♥t❡①t✮ ④
   t❤✐s✳❝♦♥t❡①t ❂ ❝♦♥t❡①t❀
   t❤✐s✳① ❂ ✵❀
   t❤✐s✳② ❂ ✵❀
   t❤✐s✳✈❡❧♦❝✐❞❛❞❡❳ ❂ ✵❀
   t❤✐s✳✈❡❧♦❝✐❞❛❞❡❨ ❂ ✵❀
   t❤✐s✳❝♦r ❂ ✬❜❧❛❝❦✬❀
   t❤✐s✳r❛✐♦ ❂ ✶✵❀
⑥
❇♦❧❛✳♣r♦t♦t②♣❡ ❂ ④
   ✴✴ ■♥t❡r❢❛❝❡ ❞❡ ❛♥✐♠❛çã♦
   ❛t✉❛❧✐③❛r✿ ❢✉♥❝t✐♦♥✭✮ ④

    ⑥✱
    ❞❡s❡♥❤❛r✿ ❢✉♥❝t✐♦♥✭✮ ④

    ⑥✱
    ✴✴ ■♥t❡r❢❛❝❡ ❞❡ ❝♦❧✐sã♦
    r❡t❛♥❣✉❧♦s❈♦❧✐s❛♦✿ ❢✉♥❝t✐♦♥✭✮ ④

    ⑥✱
    ❝♦❧✐❞✐✉❈♦♠✿ ❢✉♥❝t✐♦♥✭s♣r✐t❡✮ ④

    ⑥
⑥

                                                                                 95


[PAGINA 103]
5.4. Criando um sprite colidível                               Casa do Código


    Os métodos atualizar e desenhar não mudaram em nada. O
método atualizar muda a posição da bola de acordo com suas veloci-
dades horizontal e vertical e inverte as velocidades quando ela está quicando
no Canvas. O método desenhar usa a API do contexto “2d” para desen-
har a bola em sua posição, com a cor e o raio definidos. Em caso de dúvida,
consulte a seção 2.4:

❛t✉❛❧✐③❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✈❛r ❝t① ❂ t❤✐s✳❝♦♥t❡①t❀

     ✐❢ ✭t❤✐s✳① ❁ t❤✐s✳r❛✐♦ ⑤⑤ t❤✐s✳① ❃
           ❝t①✳❝❛♥✈❛s✳✇✐❞t❤ ✲ t❤✐s✳r❛✐♦✮
        t❤✐s✳✈❡❧♦❝✐❞❛❞❡❳ ✯❂ ✲✶❀

     ✐❢ ✭t❤✐s✳② ❁ t❤✐s✳r❛✐♦ ⑤⑤ t❤✐s✳② ❃
           ❝t①✳❝❛♥✈❛s✳❤❡✐❣❤t ✲ t❤✐s✳r❛✐♦✮
        t❤✐s✳✈❡❧♦❝✐❞❛❞❡❨ ✯❂ ✲✶❀

     t❤✐s✳① ✰❂ t❤✐s✳✈❡❧♦❝✐❞❛❞❡❳❀
     t❤✐s✳② ✰❂ t❤✐s✳✈❡❧♦❝✐❞❛❞❡❨❀
⑥✱
❞❡s❡♥❤❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✈❛r ❝t① ❂ t❤✐s✳❝♦♥t❡①t❀
   ❝t①✳s❛✈❡✭✮❀
   ❝t①✳❢✐❧❧❙t②❧❡ ❂ t❤✐s✳❝♦r❀
   ❝t①✳❜❡❣✐♥P❛t❤✭✮❀
   ❝t①✳❛r❝✭t❤✐s✳①✱ t❤✐s✳②✱ t❤✐s✳r❛✐♦✱ ✵✱ ✷ ✯ ▼❛t❤✳P■✱ ❢❛❧s❡✮❀
   ❝t①✳❢✐❧❧✭✮❀
   ❝t①✳r❡st♦r❡✭✮❀
⑥

    Para a bola, o método retangulosColisao, criará um único retân-
gulo que, mesmo assim, deve estar contido em um array. Só para lembrar,
em JavaScript, os colchetes delimitam arrays e as chaves delimitam objetos.
Temos, portanto, um objeto dentro de um array:

r❡t❛♥❣✉❧♦s❈♦❧✐s❛♦✿ ❢✉♥❝t✐♦♥✭✮ ④
   r❡t✉r♥ ❬
      ④

96


[PAGINA 104]
Casa do Código                                        Capítulo 5. Detecção de colisões



              ①✿ t❤✐s✳① ✲ t❤✐s✳r❛✐♦✱ ✴✴ t❤✐s✳① é ♦ ❝❡♥tr♦ ❞❛ ❜♦❧❛
              ②✿ t❤✐s✳② ✲ t❤✐s✳r❛✐♦✱ ✴✴ t❤✐s✳② ✐❞❡♠
              ❧❛r❣✉r❛✿ t❤✐s✳r❛✐♦ ✯ ✷✱
              ❛❧t✉r❛✿ t❤✐s✳r❛✐♦ ✯ ✷
          ⑥
     ❪❀
⑥✱

    Como a posição (x,y) da bola define seu centro, descontamos o raio
para achar a posição do seu retângulo circundante, que na realidade é um
quadrado. O lado desse quadrado é igual ao dobro do raio da bola:




                    Figura 5.6: Retângulo circundante da bola


   Falta agora o método colidiuCom. Por enquanto, vamos mostrar uma
mensagem de alerta:

❝♦❧✐❞✐✉❈♦♠✿ ❢✉♥❝t✐♦♥✭s♣r✐t❡✮ ④
   ❛❧❡rt✭✬P➪✦✬✮❀
⑥

     Faça o teste e veja se a mensagem aparece:




                                                                                  97


[PAGINA 105]
5.5. Melhorando o código                                       Casa do Código




                           Figura 5.7: Colisão detectada


      No entanto, a mensagem aparece muitas vezes pelos seguintes motivos:

      • Estamos detectando colisões repetidas. Testamos A e vimos que colidiu
        com B. Ao testar B, não precisamos colidi-lo com A novamente!

      • São duas bolinhas dando a mesma resposta à colisão, então tudo isso
        ocorre em dobro!

      • Resultado: quatro “PÁ!” por colisão.

      • Fora o fato de as bolinhas continuarem seu trajeto normalmente,
        fazendo com que passem uma “dentro” da outra e provoquem novas
        colisões.


5.5     Melhorando o código

Resolvendo a detecção repetida
Do jeito que estamos programando, cada colisão é detectada duas vezes. Fize-
mos a seguinte sequência de ações:

      • Pegamos o primeiro sprite (vamos chamá-lo de A);

98


[PAGINA 106]
Casa do Código                                       Capítulo 5. Detecção de colisões



    • Fazemos um loop em todos os outros e testamos contra A;

    • Detectamos uma colisão com outro sprite (que chamaremos de B);

    • Enviamos uma mensagem para A e para B.

    Mas o processo não para aí, chegou a vez de testar B!

    • Testamos B contra os outros;

    • Detectamos sua colisão com A (que já foi detectada anteriormente);

    • Enviamos as mensagens novamente para A e para B.

     Para resolver o primeiro problema, vamos manter um registro de colisões
já testadas. Isto pode ser feito de diversas formas, mas queimando neurônios
eu achei mais fácil usar um objeto associativo contendo arrays, onde eu asso-
cio um sprite aos outros com quem ele já colidiu. Veja:

✴✴ ❊①❡♠♣❧♦ t❡ór✐❝♦

✴✴ ❈r✐♦ ✉♠ ♦❜❥❡t♦ ✈❛③✐♦
✈❛r ❥❛❚❡st❛❞♦s ❂ ♥❡✇ ❖❜❥❡❝t✭✮❀

✴✴ ❆ss♦❝✐♦ ✉♠ s♣r✐t❡ ❛ ✉♠ ❛rr❛② ❞❡ ♦✉tr♦s
✴✴ ❊st♦✉ ❞✐③❡♥❞♦ q✉❡ ❛ ♥❛✈❡ ❥á ❝♦❧✐❞✐✉ ❝♦♠ ♦ ♠❡t❡♦r♦ ❡ ♦ ✐t❡♠
✈❛r ❥❛❚❡st❛❞♦s❬♥❛✈❡❪ ❂ ❬♠❡t❡♦r♦✱ ✐t❡♠❪❀

    Infelizmente, os elementos de jaTestados não podem ser outros ob-
jetos. Nesse código, nave deve ser uma string, pois as propriedades de um
objeto podem ser expressas por strings usando a sintaxe de [colchetes] (veja a
seção 1.4).
    Preste bastante atenção ao exemplo teórico a seguir. Se gerarmos uma
string única para cada sprite, podemos associar cada uma a um array den-
tro desse objeto associativo. Tendo as strings devidamente armazenadas no
objeto, podemos verificar se a colisão já foi testada:




                                                                                 99


[PAGINA 107]
5.5. Melhorando o código                                     Casa do Código


✴✴ ❊①❡♠♣❧♦ t❡ór✐❝♦
✴✴ ❆ ❝❛❞❛ ❝✐❝❧♦ ❞♦ ❧♦♦♣ ❡st❛♠♦s t❡st❛♥❞♦ ✷ s♣r✐t❡s

✴✴ ❈r✐❛r ❛s ✐❞❡♥t✐❢✐❝❛çõ❡s
✈❛r ✐❞✶ ❂ str✐♥❣❯♥✐❝❛✭s♣r✐t❡✶✮❀
✈❛r ✐❞✷ ❂ str✐♥❣❯♥✐❝❛✭s♣r✐t❡✷✮❀

✴✴ ❈r✐❛r ♦s ❛rr❛②s s❡ ♥ã♦ ❡①✐st✐r❡♠
✐❢ ✭✦ ❥❛❚❡st❛❞♦s❬✐❞✶❪✮ ❥❛❚❡st❛❞♦s❬✐❞✶❪ ❂ ❬❪❀
✐❢ ✭✦ ❥❛❚❡st❛❞♦s❬✐❞✷❪✮ ❥❛❚❡st❛❞♦s❬✐❞✷❪ ❂ ❬❪❀

✴✴ ❚❡st❛r ❛ ❝♦❧✐sã♦ s❡ ❥á ♥ã♦ ❢♦✐ t❡st❛❞♦ ✐❞✶ ❝♦♠ ✐❞✷
t❡st❛r❙❡◆❛♦❘❡♣❡t✐❞♦✭✐❞✶✱ ✐❞✷✮❀

✴✴ ❘❡❣✐str❛♥❞♦ ♦ t❡st❡ ♣❛r❛ ❡✈✐t❛r r❡♣❡t✐çã♦
❥❛❚❡st❛❞♦s❬✐❞✶❪✳♣✉s❤✭✐❞✷✮❀
❥❛❚❡st❛❞♦s❬✐❞✷❪✳♣✉s❤✭✐❞✶✮❀

    Para verificar se o teste atual não é repetido, podemos usar o método
indexOf dos arrays. Por exemplo, jaTestados[id1].indexOf(id2)
devolve a posição da string id2 dentro do array associado à id1 no objeto,
ou o valor -1 caso ainda não exista:

✴✴ ❊①❡♠♣❧♦ t❡ór✐❝♦ ✭♣❛rt❡ ❢✐♥❛❧✮
✴✴ ❱❡r✐❢✐❝❛r s❡ ✐❞✶ ❝♦♠ ✐❞✷ ❥á ❢♦✐ t❡st❛❞♦
✐❢ ✭✦ ✭❥❛❚❡st❛❞♦s❬✐❞✶❪✳✐♥❞❡①❖❢✭✐❞✷✮ ❃❂ ✵ ⑤⑤
       ❥❛❚❡st❛❞♦s❬✐❞✷❪✳✐♥❞❡①❖❢✭✐❞✶✮ ❃❂ ✵✮ ✮ ④

      ✴✴ ❆q✉✐ t❡st❛♠♦s ❛ ❝♦❧✐sã♦
⑥

    Vamos, finalmente, para a parte prática. Primeiro, crie o método
stringUnica, que gerará uma string para o sprite a partir dos dados de seus
retângulos de colisão:

str✐♥❣❯♥✐❝❛✿ ❢✉♥❝t✐♦♥✭s♣r✐t❡✮ ④
   ✈❛r str ❂ ✬✬❀
   ✈❛r r❡t❛♥❣✉❧♦s ❂ s♣r✐t❡✳r❡t❛♥❣✉❧♦s❈♦❧✐s❛♦✭✮❀



100


[PAGINA 108]
Casa do Código                                      Capítulo 5. Detecção de colisões



    ❢♦r ✭✈❛r ✐ ✐♥ r❡t❛♥❣✉❧♦s✮ ④
       str ✰❂ ✬①✿✬ ✰ r❡t❛♥❣✉❧♦s❬✐❪✳① ✰ ✬✱✬ ✰
              ✬②✿✬ ✰ r❡t❛♥❣✉❧♦s❬✐❪✳② ✰ ✬✱✬ ✰
              ✬❧✿✬ ✰ r❡t❛♥❣✉❧♦s❬✐❪✳❧❛r❣✉r❛ ✰ ✬✱✬ ✰
              ✬❛✿✬ ✰ r❡t❛♥❣✉❧♦s❬✐❪✳❛❧t✉r❛ ✰ ✬❭♥✬❀
    ⑥

    r❡t✉r♥ str❀
⑥

     Acompanhe a nova implementação do método processar, acrescen-
tando os novos testes. Iniciamos com um objeto vazio e, a cada verificação,
geramos uma string para cada sprite, verificamos se seus arrays já existem e
se já foi testada essa colisão. Caso não, nós a testamos e a registramos:

♣r♦❝❡ss❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✴✴ ■♥✐❝✐♦ ❝♦♠ ✉♠ ♦❜❥❡t♦ ✈❛③✐♦
   ✈❛r ❥❛❚❡st❛❞♦s ❂ ♥❡✇ ❖❜❥❡❝t✭✮❀

    ❢♦r ✭✈❛r ✐ ✐♥ t❤✐s✳s♣r✐t❡s✮ ④
       ❢♦r ✭✈❛r ❥ ✐♥ t❤✐s✳s♣r✐t❡s✮ ④
          ✴✴ ◆ã♦ ❝♦❧✐❞✐r ✉♠ s♣r✐t❡ ❝♦♠ ❡❧❡ ♠❡s♠♦
          ✐❢ ✭✐ ❂❂ ❥✮ ❝♦♥t✐♥✉❡❀

           ✴✴ ●❡r❛r str✐♥❣s ú♥✐❝❛s ♣❛r❛ ♦s ♦❜❥❡t♦s
           ✈❛r ✐❞✶ ❂ t❤✐s✳str✐♥❣❯♥✐❝❛✭t❤✐s✳s♣r✐t❡s❬✐❪✮❀
           ✈❛r ✐❞✷ ❂ t❤✐s✳str✐♥❣❯♥✐❝❛✭t❤✐s✳s♣r✐t❡s❬❥❪✮❀

           ✴✴ ❈r✐❛r ♦s ❛rr❛②s s❡ ♥ã♦ ❡①✐st✐r❡♠
           ✐❢ ✭✦ ❥❛❚❡st❛❞♦s❬✐❞✶❪✮ ❥❛❚❡st❛❞♦s❬✐❞✶❪ ❂ ❬❪❀
           ✐❢ ✭✦ ❥❛❚❡st❛❞♦s❬✐❞✷❪✮ ❥❛❚❡st❛❞♦s❬✐❞✷❪ ❂ ❬❪❀

           ✴✴ ❚❡st❡ ❞❡ r❡♣❡t✐çã♦
           ✐❢ ✭✦ ✭❥❛❚❡st❛❞♦s❬✐❞✶❪✳✐♥❞❡①❖❢✭✐❞✷✮ ❃❂ ✵ ⑤⑤
                  ❥❛❚❡st❛❞♦s❬✐❞✷❪✳✐♥❞❡①❖❢✭✐❞✶✮ ❃❂ ✵✮ ✮ ④

                 ✴✴ ❆❜str❛✐r ❛ ❝♦❧✐sã♦
                 t❤✐s✳t❡st❛r❈♦❧✐s❛♦✭t❤✐s✳s♣r✐t❡s❬✐❪✱
                                   t❤✐s✳s♣r✐t❡s❬❥❪✮❀

                                                                               101


[PAGINA 109]
5.5. Melhorando o código                                    Casa do Código




                  ✴✴ ❘❡❣✐str❛♥❞♦ ♦ t❡st❡
                  ❥❛❚❡st❛❞♦s❬✐❞✶❪✳♣✉s❤✭✐❞✷✮❀
                  ❥❛❚❡st❛❞♦s❬✐❞✷❪✳♣✉s❤✭✐❞✶✮❀
              ⑥
          ⑥
      ⑥
⑥✱

    Se você rodar o programa agora, verá que reduzimos para dois “PÁ!” por
colisão, pois são duas bolinhas respondendo.

Um tratador geral de colisões
    Por que somente as bolinhas (sprites) podem responder à colisão? Há
casos, por exemplo, em que eu quero uma resposta única e não é necessário
que os dois objetos respondam. Que tal poder fazer:
✴✴ ❊①❡♠♣❧♦ t❡ór✐❝♦
❝♦❧✐s♦r✳❛♦❈♦❧✐❞✐r ❂ ❢✉♥❝t✐♦♥✭s♣r✐t❡✶✱ s♣r✐t❡✷✮ ④
   ✴✴ ❘❡s♣♦st❛ ú♥✐❝❛
⑥❀

    O atributo aoColidir seria uma função de callback executada em toda
e qualquer colisão. Esta função receberia como parâmetros os sprites que
colidiram.
    No construtor da classe Colisor, inicie o atributo aoColidir com
null, somente para documentá-lo:
❢✉♥❝t✐♦♥ ❈♦❧✐s♦r✭✮ ④
   t❤✐s✳s♣r✐t❡s ❂ ❬❪❀
   t❤✐s✳❛♦❈♦❧✐❞✐r ❂ ♥✉❧❧❀
⑥

     No método testarColisao, no ponto em que as mensagens são envi-
adas, acrescente a chamada a esse callback. Usamos um if para verificar se
foi atribuída uma função:
✴✴✳✳✳


102


[PAGINA 110]
Casa do Código                                       Capítulo 5. Detecção de colisões



✐❢ ✭t❤✐s✳r❡t❛♥❣✉❧♦s❈♦❧✐❞❡♠✭r❡ts✶❬✐❪✱ r❡ts✷❬❥❪✮✮ ④
   ✴✴ ❊❧❡s ❝♦❧✐❞❡♠✱ ✈❛♠♦s ♥♦t✐❢✐❝á✲❧♦s
   s♣r✐t❡✶✳❝♦❧✐❞✐✉❈♦♠✭s♣r✐t❡✷✮❀
   s♣r✐t❡✷✳❝♦❧✐❞✐✉❈♦♠✭s♣r✐t❡✶✮❀

    ✴✴ ❚r❛t❛❞♦r ❣❡r❛❧
    ✐❢ ✭t❤✐s✳❛♦❈♦❧✐❞✐r✮ t❤✐s✳❛♦❈♦❧✐❞✐r✭s♣r✐t❡✶✱ s♣r✐t❡✷✮❀

    ✴✴ ◆ã♦ ♣r❡❝✐s❛ t❡r♠✐♥❛r ❞❡ ✈❡r t♦❞♦s ♦s r❡tâ♥❣✉❧♦s
    ❜r❡❛❦ ❝♦❧✐s♦❡s❀
⑥

✴✴✳✳✳

    No aplicativo de teste, logo após a criação do colisor, podemos atribuir a
seguinte função:

✈❛r ❝♦❧✐s♦r ❂ ♥❡✇ ❈♦❧✐s♦r✭✮❀
❝♦❧✐s♦r✳♥♦✈♦❙♣r✐t❡✭❜✶✮❀
❝♦❧✐s♦r✳♥♦✈♦❙♣r✐t❡✭❜✷✮❀

❝♦❧✐s♦r✳❛♦❈♦❧✐❞✐r ❂ ❢✉♥❝t✐♦♥✭s✶✱ s✷✮ ④
   ❛❧❡rt✭✬P➪✬✮❀
⑥❀

   E o método colidiuCom da Bola ficará com o corpo vazio (por en-
quanto):

❝♦❧✐❞✐✉❈♦♠✿ ❢✉♥❝t✐♦♥✭s♣r✐t❡✮ ④

⑥

    Neste ponto, temos apenas um “PÁ!” para cada deslocamento. Lembre-se
de que as bolinhas continuam sua trajetória em linha reta e provocam novas
colisões enquanto passam uma pela outra.

Fazendo os sprites quicarem
   Se fizermos as bolinhas quicarem uma na outra, resolvemos completa-
mente o problema do excesso de colisões. O segredo, aqui, é verificar qual

                                                                                103


[PAGINA 111]
5.5. Melhorando o código                                        Casa do Código


bolinha está em que lado, e fazer com que passe a ir nesse sentido (não im-
porta em que sentido esteja indo). A figura 5.8 representa isso na horizontal:




Figura 5.8: O sprite que está à esquerda vai para a esquerda, e o que está à
direita vai para a direita


      O mesmo vale para a vertical:




Figura 5.9: O sprite que está acima vai para cima, e o que está abaixo vai para
baixo



104


[PAGINA 112]
Casa do Código                                      Capítulo 5. Detecção de colisões



    Faremos isto no método colidiuCom da classe Bola. Para forçar a
bola a ir para um determinado lado, obtemos os módulos das velocidades
com Math.abs e colocamos um sinal negativo nos casos em que a velocidade
passa a ser negativa (para esquerda e para cima):

❝♦❧✐❞✐✉❈♦♠✿ ❢✉♥❝t✐♦♥✭s♣r✐t❡✮ ④
   ✐❢ ✭t❤✐s✳① ❁ s♣r✐t❡✳①✮ ✴✴ ❊st♦✉ ♥❛ ❡sq✉❡r❞❛
      t❤✐s✳✈❡❧♦❝✐❞❛❞❡❳ ❂ ✲▼❛t❤✳❛❜s✭t❤✐s✳✈❡❧♦❝✐❞❛❞❡❳✮❀ ✴✴ ✲
   ❡❧s❡
      t❤✐s✳✈❡❧♦❝✐❞❛❞❡❳ ❂ ▼❛t❤✳❛❜s✭t❤✐s✳✈❡❧♦❝✐❞❛❞❡❳✮❀ ✴✴ ✰

    ✐❢ ✭t❤✐s✳② ❁ s♣r✐t❡✳②✮ ✴✴ ❊st♦✉ ❛❝✐♠❛
       t❤✐s✳✈❡❧♦❝✐❞❛❞❡❨ ❂ ✲▼❛t❤✳❛❜s✭t❤✐s✳✈❡❧♦❝✐❞❛❞❡❨✮❀ ✴✴ ✲
    ❡❧s❡
       t❤✐s✳✈❡❧♦❝✐❞❛❞❡❨ ❂ ▼❛t❤✳❛❜s✭t❤✐s✳✈❡❧♦❝✐❞❛❞❡❨✮❀ ✴✴ ✰
⑥

   Temos agora uma única mensagem “PÁ!” por colisão. Se você quiser ver
apenas as bolinhas quicarem, basta comentar o alert ou simplesmente re-
mover o tratador geral:

✴✴ ❘❡♠♦✈❛ ❡st❡ ❝ó❞✐❣♦ ♦✉ ❝♦♠❡♥t❡ ♦ ❝♦r♣♦ ❞❛ ❢✉♥çã♦✿
❝♦❧✐s♦r✳❛♦❈♦❧✐❞✐r ❂ ❢✉♥❝t✐♦♥✭s✶✱ s✷✮ ④
   ✴✴❛❧❡rt✭✬P➪✬✮❀
⑥❀

    Aqui, as possibilidades são infinitas. No decorrer do desenvolvimento de
nosso jogo, faremos os objetos atingidos por tiros sumirem, criaremos novos
sprites (explosões), aumentamos indicadores na tela (coleta de item) etc.
    No próximo capítulo, faremos as primeiras experiências para o jogo de
nave ilustrado no primeiro capítulo.




                                                                               105


[PAGINA 113]


[PAGINA 114]
Capítulo 6

Iniciando o desenvolvimento do
jogo
A partir deste ponto daremos início ao desenvolvimento de nosso jogo de
nave. O game engine ainda terá muitos acréscimos e melhorias, conforme
formos precisando de novos recursos. Em algum momento, ele ficará maduro
e pronto para uso, mas minha ideia é mostrar como ele pode sempre continuar
evoluindo conforme vamos desenvolvendo jogos com ele.


6.1   Animação de fundo com efeito parallax
A primeira coisa que faremos é o fundo. Se você ainda não fez o download
dos arquivos deste livro, faça em http://github.com/EdyKnopfler/games-js/
archive/master.zip, pois usaremos as imagens contidas ali.


[PAGINA 115]
6.1. Animação de fundo com efeito parallax                       Casa do Código


    O cenário do jogo terá o seguinte aspecto, em resolução de 500 por 500
pixels:




                          Figura 6.1: Cenário do jogo de nave


    O fundo, no entanto, será composto por 3 imagens separadas: uma para
o gradiente, outra para as estrelas e outra para as nuvens. Estas duas últi-
mas terão fundo transparente, para podermos encaixar umas sobre as outras,
como camadas:




                  Figura 6.2: Combinando os elementos do fundo


108


[PAGINA 116]
Casa do Código                           Capítulo 6. Iniciando o desenvolvimento do jogo



    Cada imagem possui 500 pixels de largura por 1000 pixels de altura (por-
tanto, o dobro da área do jogo). Elas rolarão pelo cenário a velocidades difer-
entes, criando um efeito denominado parallax (paralaxe):




     Figura 6.3: Os elementos do fundo rolam a velocidades diferentes




                                                                                   109


[PAGINA 117]
6.1. Animação de fundo com efeito parallax                     Casa do Código




  Paralaxe

      Um avião no céu parece voar a uma velocidade incrivelmente lenta.
  No entanto, se estivéssemos lá em cima e ele passasse por nós, o veríamos
  a toda velocidade.
      Da mesma forma, viajando por uma estrada, o mato diante do meio-
  fio e as placas passam velozmente, enquanto a serra ao longe se afasta
  devagar.
      Esse efeito de velocidade aparente, na Física, é denominado par-
  alaxe. Quanto mais distante está um objeto, menor será sua veloci-
  dade percebida por nós.
      O livro Core HTML5 Canvas, de David Geary, traz um exemplo muito
  bem feito, que pode ser conferido aqui:
      http://corehtml5canvas.com/code-live/ch05/example-5.17/example.
  html
      Obs.: entre desenvolvedores de jogos, o mais comum é nos referir-
  mos ao efeito pelo nome em inglês (parallax), razão pela qual usarei esta
  forma daqui para frente.


    Durante a rolagem, cada imagem deverá ser desenhada no mínimo duas
vezes, de forma a cobrir toda a área de desenho durante a rolagem (figura
6.4). Se fosse uma imagem menor, teríamos que desenhá-la mais vezes. A
cada ciclo, nós emendamos os desenhos a uma altura diferente (marcada com
uma linha vermelha):




110


[PAGINA 118]
Casa do Código                         Capítulo 6. Iniciando o desenvolvimento do jogo




Figura 6.4: Cada imagem de fundo é desenhada quantas vezes forem
necessárias para cobrir a área do jogo. Com imagens maiores que o Canvas,
duas vezes são suficientes


    Repare que os pontos inicial e final do gradiente têm de possuir a mesma
cor para serem emendados (lembre-se disso ao criar as imagens em seu pro-
grama gráfico predileto). Da mesma forma, os extremos das outras figuras
precisam encaixar-se perfeitamente! Por exemplo, para criar as nuvens, pode-
mos proceder da maneira descrita nas figuras 6.5 e 6.6:




                                                                                  111


[PAGINA 119]
6.1. Animação de fundo com efeito parallax                      Casa do Código




                  Figura 6.5: Quebramos uma nuvem pelo centro




Figura 6.6: Viramos cada metade de cabeça para baixo e encaixamos nas bor-
das da imagem


      Tomando esses cuidados ao produzir as imagens de fundo de seus games,

112


[PAGINA 120]
Casa do Código                         Capítulo 6. Iniciando o desenvolvimento do jogo



a programação ficará muito fácil. Vamos criar a classe Fundo, que será basi-
camente um sprite como todos os outros.

Teste para a classe Fundo
   Para a criação deste teste, crie uma pasta de nome img na mesma pasta
onde o HTML será salvo, e copie nela os arquivos fundo-espaco.png,
fundo-estrelas.png e fundo-nuvens.png do pacote que você baixou.
Você pode criar ou procurar outras imagens com fundo transparente tam-
bém, mas certifique-se de recortá-las ou dimensioná-las para 500x1000.




     Figura 6.7: Crie uma pasta junto ao HTML e copie as imagens nela


    O HTML para o teste não tem nada de especial:

❁✦✲✲ ❛rq✉✐✈♦✿ t❡st❡✲❢✉♥❞♦✳❤t♠❧ ✲✲❃
❁✦❉❖❈❚❨P❊ ❤t♠❧❃
❁❤t♠❧❃

❁❤❡❛❞❃
   ❁t✐t❧❡❃❋✉♥❞♦s r♦❧❛♥❞♦ ❡♠ P❛r❛❧❧❛①❁✴t✐t❧❡❃
   ❁s❝r✐♣t sr❝❂✧❛♥✐♠❛❝❛♦✳❥s✧❃❁✴s❝r✐♣t❃
   ❁s❝r✐♣t sr❝❂✧❢✉♥❞♦✳❥s✧❃❁✴s❝r✐♣t❃
❁✴❤❡❛❞❃



                                                                                  113


[PAGINA 121]
6.1. Animação de fundo com efeito parallax                    Casa do Código


❁❜♦❞②❃
   ❁❝❛♥✈❛s ✐❞❂✧❝❛♥✈❛s❴❢✉♥❞♦✧ ✇✐❞t❤❂✧✺✵✵✧ ❤❡✐❣❤t❂✧✺✵✵✧❃❁✴❝❛♥✈❛s❃
   ❁s❝r✐♣t❃
      ✴✴ Pr✐♠❡✐r♦ t❡♠♦s q✉❡ ❝❛rr❡❣❛r ❛s ✐♠❛❣❡♥s
   ❁✴s❝r✐♣t❃
❁✴❜♦❞②❃

❁✴❤t♠❧❃


  Observação

       Ao   incluir arquivos já criados anteriormente (no caso,
  animacao.js), pegue sempre o do capítulo mais recente. Neste
  caso, a versão mais recente da classe Animacao é do capítulo 4. A cada
  capítulo ou tópico, o game engine poderá sofrer alterações.


      No JavaScript, inicialmente mandamos carregar as imagens:

✈❛r ✐♠❣❊s♣❛❝♦ ❂ ♥❡✇ ■♠❛❣❡✭✮❀
✐♠❣❊s♣❛❝♦✳sr❝ ❂ ✬✐♠❣✴❢✉♥❞♦✲❡s♣❛❝♦✳♣♥❣✬❀

✈❛r ✐♠❣❊str❡❧❛s ❂ ♥❡✇ ■♠❛❣❡✭✮❀
✐♠❣❊str❡❧❛s✳sr❝ ❂ ✬✐♠❣✴❢✉♥❞♦✲❡str❡❧❛s✳♣♥❣✬❀

✈❛r ✐♠❣◆✉✈❡♥s ❂ ♥❡✇ ■♠❛❣❡✭✮❀
✐♠❣◆✉✈❡♥s✳sr❝ ❂ ✬✐♠❣✴❢✉♥❞♦✲♥✉✈❡♥s✳♣♥❣✬❀

   Em seguida, temos que esperar todas serem carregadas. Como já apren-
demos, isto é feito através do evento onload. Mantemos um contador de
quantas já estão carregadas e, quando todas estiverem prontas, a aplicação
pode de fato “iniciar":

✈❛r ❝❛rr❡❣❛❞❛s ❂ ✵❀
✈❛r t♦t❛❧ ❂ ✸❀

✐♠❣❊s♣❛❝♦✳♦♥❧♦❛❞ ❂ ❝❛rr❡❣❛♥❞♦❀
✐♠❣❊str❡❧❛s✳♦♥❧♦❛❞ ❂ ❝❛rr❡❣❛♥❞♦❀

114


[PAGINA 122]
Casa do Código                          Capítulo 6. Iniciando o desenvolvimento do jogo



✐♠❣◆✉✈❡♥s✳♦♥❧♦❛❞ ❂ ❝❛rr❡❣❛♥❞♦❀

❢✉♥❝t✐♦♥ ❝❛rr❡❣❛♥❞♦✭✮ ④
   ❝❛rr❡❣❛❞❛s✰✰❀
   ✐❢ ✭❝❛rr❡❣❛❞❛s ❂❂ t♦t❛❧✮ ✐♥✐❝✐❛r✭✮❀
⑥

    Na função iniciar, fazemos as operações habituais: inicializamos o
Canvas, criamos os sprites (que aqui serão os fundos rolando) e os incluímos
no objeto animador:
❢✉♥❝t✐♦♥ ✐♥✐❝✐❛r✭✮ ④
   ✈❛r ❝❛♥✈❛s ❂ ❞♦❝✉♠❡♥t✳❣❡t❊❧❡♠❡♥t❇②■❞✭✬❝❛♥✈❛s❴❢✉♥❞♦✬✮❀
   ✈❛r ❝♦♥t❡①t ❂ ❝❛♥✈❛s✳❣❡t❈♦♥t❡①t✭✬✷❞✬✮❀

    ✴✴ P❛ss♦ ♦ ❝♦♥t❡①t ❡ ❛ ✐♠❛❣❡♠ ♣❛r❛ ♦s ♦❜❥❡t♦s ❋✉♥❞♦
    ✈❛r ❢✉♥❞♦❊s♣❛❝♦ ❂ ♥❡✇ ❋✉♥❞♦✭❝♦♥t❡①t✱ ✐♠❣❊s♣❛❝♦✮❀
    ✈❛r ❢✉♥❞♦❊str❡❧❛s ❂ ♥❡✇ ❋✉♥❞♦✭❝♦♥t❡①t✱ ✐♠❣❊str❡❧❛s✮❀
    ✈❛r ❢✉♥❞♦◆✉✈❡♥s ❂ ♥❡✇ ❋✉♥❞♦✭❝♦♥t❡①t✱ ✐♠❣◆✉✈❡♥s✮❀

    ✴✴ ❈❛❞❛ ✉♠ ❛ ✉♠❛ ✈❡❧♦❝✐❞❛❞❡ ❞✐❢❡r❡♥t❡
    ❢✉♥❞♦❊s♣❛❝♦✳✈❡❧♦❝✐❞❛❞❡ ❂ ✸❀
    ❢✉♥❞♦❊str❡❧❛s✳✈❡❧♦❝✐❞❛❞❡ ❂ ✼❀
    ❢✉♥❞♦◆✉✈❡♥s✳✈❡❧♦❝✐❞❛❞❡ ❂ ✶✵❀

    ✈❛r ❛♥✐♠❛❝❛♦ ❂ ♥❡✇ ❆♥✐♠❛❝❛♦✭❝♦♥t❡①t✮❀
    ❛♥✐♠❛❝❛♦✳♥♦✈♦❙♣r✐t❡✭❢✉♥❞♦❊s♣❛❝♦✮❀
    ❛♥✐♠❛❝❛♦✳♥♦✈♦❙♣r✐t❡✭❢✉♥❞♦❊str❡❧❛s✮❀
    ❛♥✐♠❛❝❛♦✳♥♦✈♦❙♣r✐t❡✭❢✉♥❞♦◆✉✈❡♥s✮❀
    ❛♥✐♠❛❝❛♦✳❧✐❣❛r✭✮❀
⑥

Iniciando a classe Fundo
    A próxima etapa é iniciar a classe Fundo. Sempre adotamos a prática
de receber as imagens pelo construtor, para permitir que a aplicação controle
quando todas estão carregadas:
✴✴ ❛rq✉✐✈♦✿ ❢✉♥❞♦✳❥s
❢✉♥❝t✐♦♥ ❋✉♥❞♦✭❝♦♥t❡①t✱ ✐♠❛❣❡♠✮ ④

                                                                                   115


[PAGINA 123]
6.1. Animação de fundo com efeito parallax                   Casa do Código


      t❤✐s✳❝♦♥t❡①t ❂ ❝♦♥t❡①t❀
      t❤✐s✳✐♠❛❣❡♠ ❂ ✐♠❛❣❡♠❀
      t❤✐s✳✈❡❧♦❝✐❞❛❞❡ ❂ ✵❀
⑥
❋✉♥❞♦✳♣r♦t♦t②♣❡ ❂ ④
   ❛t✉❛❧✐③❛r✿ ❢✉♥❝t✐♦♥✭✮ ④

      ⑥✱
      ❞❡s❡♥❤❛r✿ ❢✉♥❝t✐♦♥✭✮ ④

      ⑥
⑥

   Lembre-se de que cada fundo deve ser desenhado duas vezes, emenda-
dos pelas extremidades em posições diferentes (figura 6.4). Crie o atributo
posicaoEmenda e o inicialize no construtor com o valor zero:

❢✉♥❝t✐♦♥ ❋✉♥❞♦✭❝♦♥t❡①t✱ ✐♠❛❣❡♠✮ ④
   t❤✐s✳❝♦♥t❡①t ❂ ❝♦♥t❡①t❀
   t❤✐s✳✐♠❛❣❡♠ ❂ ✐♠❛❣❡♠❀
   t❤✐s✳✈❡❧♦❝✐❞❛❞❡ ❂ ✵❀
   t❤✐s✳♣♦s✐❝❛♦❊♠❡♥❞❛ ❂ ✵❀
⑥

   No método desenhar, desenhamos as duas cópias da imagem emen-
dadas nessa posição:
❞❡s❡♥❤❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✈❛r ✐♠❣ ❂ t❤✐s✳✐♠❛❣❡♠❀ ✴✴ P❛r❛ ❢❛❝✐❧✐t❛r ❛ ❡s❝r✐t❛ ✿❉

      ✴✴ Pr✐♠❡✐r❛ ❝ó♣✐❛
      ✈❛r ♣♦s✐❝❛♦❨ ❂ t❤✐s✳♣♦s✐❝❛♦❊♠❡♥❞❛ ✲ ✐♠❣✳❤❡✐❣❤t❀
      t❤✐s✳❝♦♥t❡①t✳❞r❛✇■♠❛❣❡✭✐♠❣✱ ✵✱ ♣♦s✐❝❛♦❨✱ ✐♠❣✳✇✐❞t❤✱
         ✐♠❣✳❤❡✐❣❤t✮❀

      ✴✴ ❙❡❣✉♥❞❛ ❝ó♣✐❛
      ♣♦s✐❝❛♦❨ ❂ t❤✐s✳♣♦s✐❝❛♦❊♠❡♥❞❛❀
      t❤✐s✳❝♦♥t❡①t✳❞r❛✇■♠❛❣❡✭✐♠❣✱ ✵✱ ♣♦s✐❝❛♦❨✱ ✐♠❣✳✇✐❞t❤✱
         ✐♠❣✳❤❡✐❣❤t✮❀
⑥

116


[PAGINA 124]
Casa do Código                         Capítulo 6. Iniciando o desenvolvimento do jogo



    No método atualizar, incrementamos a posição da emenda e a volta-
mos para zero caso a imagem de cima desça mais que o início do Canvas. A
figura 6.8 adiante ilustra o que acontece:

❛t✉❛❧✐③❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✴✴ ❆t✉❛❧✐③❛r ❛ ♣♦s✐çã♦ ❞❡ ❡♠❡♥❞❛
   t❤✐s✳♣♦s✐❝❛♦❊♠❡♥❞❛ ✰❂ t❤✐s✳✈❡❧♦❝✐❞❛❞❡❀

     ✴✴ ❊♠❡♥❞❛ ♣❛ss♦✉ ❞❛ ♣♦s✐çã♦
     ✐❢ ✭t❤✐s✳♣♦s✐❝❛♦❊♠❡♥❞❛ ❃ t❤✐s✳✐♠❛❣❡♠✳❤❡✐❣❤t✮
        t❤✐s✳♣♦s✐❝❛♦❊♠❡♥❞❛ ❂ ✵❀
⑥✱




        Figura 6.8: Imagens desceram muito, hora de reposicioná-las


                                                                                  117


[PAGINA 125]
6.2. Controle da nave na horizontal e na vertical                Casa do Código


      Já estamos viajando pelo espaço sideral!




                  Figura 6.9: Imagens de fundo rolando em parallax



6.2       Controle da nave na horizontal e na verti-
          cal
Vamos criar uma nave controlável, inicialmente em um novo teste em branco,
e depois juntando com o fundo em parallax. No pacote de download do livro,
existe o arquivo nave.png (figura 6.10), com dimensões de 36 por 48 pixels.
Você pode procurar ou criar outra imagem, mas certifique-se de que tenha
fundo transparente.




118


[PAGINA 126]
Casa do Código                            Capítulo 6. Iniciando o desenvolvimento do jogo




                   Figura 6.10: Nave espacial controlável


    Crie uma nova página para testarmos o controle da nave. Esta página
usará as classes Animacao, Teclado e Nave (a ser criada):

❁✦✲✲ ❛rq✉✐✈♦✿ t❡st❡✲♥❛✈❡✳❤t♠❧ ✲✲❃
❁✦❉❖❈❚❨P❊ ❤t♠❧❃
❁❤t♠❧❃

❁❤❡❛❞❃
   ❁t✐t❧❡❃◆❛✈❡ ❊s♣❛❝✐❛❧ ❈♦♥tr♦❧á✈❡❧❁✴t✐t❧❡❃
   ❁s❝r✐♣t sr❝❂✧❛♥✐♠❛❝❛♦✳❥s✧❃❁✴s❝r✐♣t❃
   ❁s❝r✐♣t sr❝❂✧t❡❝❧❛❞♦✳❥s✧❃❁✴s❝r✐♣t❃
   ❁s❝r✐♣t sr❝❂✧♥❛✈❡✳❥s✧❃❁✴s❝r✐♣t❃
❁✴❤❡❛❞❃

❁❜♦❞②❃
   ❁❝❛♥✈❛s ✐❞❂✧❝❛♥✈❛s❴♥❛✈❡✧ ✇✐❞t❤❂✧✺✵✵✧ ❤❡✐❣❤t❂✧✺✵✵✧❃❁✴❝❛♥✈❛s❃
   ❁s❝r✐♣t❃
      ✴✴ ❆ ♥❛✈❡ ❛♥❞❛rá ♣♦r t♦❞❛ ❛ t❡❧❛✦
   ❁✴s❝r✐♣t❃
❁✴❜♦❞②❃

❁✴❤t♠❧❃

    No JavaScript, temos o que já fizemos muitas vezes:

    • referenciar o canvas e o context;

    • instanciar as classes do game engine;

    • instanciar o sprite (no caso, a nave) e sua imagem;

    • aguardar a imagem carregar;

                                                                                     119


[PAGINA 127]
6.2. Controle da nave na horizontal e na vertical              Casa do Código


      • iniciar a animação com a nave como sprite.

✴✴ ❈❛♥✈❛s ❡ ❝♦♥t❡①t♦
✈❛r ❝❛♥✈❛s ❂ ❞♦❝✉♠❡♥t✳❣❡t❊❧❡♠❡♥t❇②■❞✭✬❝❛♥✈❛s❴♥❛✈❡✬✮❀
✈❛r ❝♦♥t❡①t ❂ ❝❛♥✈❛s✳❣❡t❈♦♥t❡①t✭✬✷❞✬✮❀

✴✴ ❚❡❝❧❛❞♦ ❡ ❛♥✐♠❛çã♦ ✭❣❛♠❡ ❡♥❣✐♥❡✮
✈❛r t❡❝❧❛❞♦ ❂ ♥❡✇ ❚❡❝❧❛❞♦✭❞♦❝✉♠❡♥t✮❀
✈❛r ❛♥✐♠❛❝❛♦ ❂ ♥❡✇ ❆♥✐♠❛❝❛♦✭❝♦♥t❡①t✮❀

✴✴ ❙♣r✐t❡ ❞❛ ♥❛✈❡ ❡ s✉❛ ✐♠❛❣❡♠
✈❛r ✐♠❣◆❛✈❡ ❂ ♥❡✇ ■♠❛❣❡✭✮❀
✐♠❣◆❛✈❡✳sr❝ ❂ ✬✐♠❣✴♥❛✈❡✳♣♥❣✬❀
✈❛r ♥❛✈❡ ❂ ♥❡✇ ◆❛✈❡✭❝♦♥t❡①t✱ t❡❝❧❛❞♦✱ ✐♠❣◆❛✈❡✮❀
❛♥✐♠❛❝❛♦✳♥♦✈♦❙♣r✐t❡✭♥❛✈❡✮❀

✴✴ ◗✉❛♥❞♦ ❝❛rr❡❣❛r ❛ ✐♠❛❣❡♠✱ ✐♥✐❝✐❛r ❛ ❛♥✐♠❛çã♦
✐♠❣◆❛✈❡✳♦♥❧♦❛❞ ❂ ❢✉♥❝t✐♦♥✭✮ ④
   ❛♥✐♠❛❝❛♦✳❧✐❣❛r✭✮❀
⑥

     A classe Nave receberá no construtor o context, o controlador do teclado
e a imagem para desenho:

✴✴ ❛rq✉✐✈♦✿ ♥❛✈❡✳❥s
❢✉♥❝t✐♦♥ ◆❛✈❡✭❝♦♥t❡①t✱ t❡❝❧❛❞♦✱ ✐♠❛❣❡♠✮ ④
   t❤✐s✳❝♦♥t❡①t ❂ ❝♦♥t❡①t❀
   t❤✐s✳t❡❝❧❛❞♦ ❂ t❡❝❧❛❞♦❀
   t❤✐s✳✐♠❛❣❡♠ ❂ ✐♠❛❣❡♠❀
⑥
◆❛✈❡✳♣r♦t♦t②♣❡ ❂ ④
   ❛t✉❛❧✐③❛r✿ ❢✉♥❝t✐♦♥✭✮ ④

      ⑥✱
      ❞❡s❡♥❤❛r✿ ❢✉♥❝t✐♦♥✭✮ ④

      ⑥
⑥

      No método atualizar, lemos o estado de cada seta do teclado e move-

120


[PAGINA 128]
Casa do Código                           Capítulo 6. Iniciando o desenvolvimento do jogo



mos a nave de acordo. Para as setas à direita e abaixo, tivemos que considerar
o tamanho do canvas e descontar o tamanho da nave, para que não ultrapas-
sasse a borda:

❛t✉❛❧✐③❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✐❢ ✭t❤✐s✳t❡❝❧❛❞♦✳♣r❡ss✐♦♥❛❞❛✭❙❊❚❆❴❊❙◗❯❊❘❉❆✮ ✫✫ t❤✐s✳① ❃ ✵✮
      t❤✐s✳① ✲❂ t❤✐s✳✈❡❧♦❝✐❞❛❞❡❀

   ✐❢ ✭t❤✐s✳t❡❝❧❛❞♦✳♣r❡ss✐♦♥❛❞❛✭❙❊❚❆❴❉■❘❊■❚❆✮ ✫✫
t❤✐s✳① ❁ t❤✐s✳❝♦♥t❡①t✳❝❛♥✈❛s✳✇✐❞t❤ ✲ t❤✐s✳✐♠❛❣❡♠✳✇✐❞t❤✮
      t❤✐s✳① ✰❂ t❤✐s✳✈❡❧♦❝✐❞❛❞❡❀

   ✐❢ ✭t❤✐s✳t❡❝❧❛❞♦✳♣r❡ss✐♦♥❛❞❛✭❙❊❚❆❴❆❈■▼❆✮ ✫✫ t❤✐s✳② ❃ ✵✮
      t❤✐s✳② ✲❂ t❤✐s✳✈❡❧♦❝✐❞❛❞❡❀

   ✐❢ ✭t❤✐s✳t❡❝❧❛❞♦✳♣r❡ss✐♦♥❛❞❛✭❙❊❚❆❴❆❇❆■❳❖✮ ✫✫
t❤✐s✳② ❁ t❤✐s✳❝♦♥t❡①t✳❝❛♥✈❛s✳❤❡✐❣❤t ✲ t❤✐s✳✐♠❛❣❡♠✳❤❡✐❣❤t✮
      t❤✐s✳② ✰❂ t❤✐s✳✈❡❧♦❝✐❞❛❞❡❀
⑥


  Observação

     Aqui usamos quatro if, sem o uso do else, para permitir que mais
  de uma seta possam estar pressionadas ao mesmo tempo. Isto nos per-
  mitirá mover a nave na diagonal!


    A nossa necessidade criou três atributos: x, y e velocidade. Vamos
iniciá-los no construtor:

❢✉♥❝t✐♦♥ ◆❛✈❡✭❝♦♥t❡①t✱ t❡❝❧❛❞♦✱ ✐♠❛❣❡♠✮ ④
   t❤✐s✳❝♦♥t❡①t ❂ ❝♦♥t❡①t❀
   t❤✐s✳t❡❝❧❛❞♦ ❂ t❡❝❧❛❞♦❀
   t❤✐s✳✐♠❛❣❡♠ ❂ ✐♠❛❣❡♠❀
   t❤✐s✳① ❂ ✵❀
   t❤✐s✳② ❂ ✵❀
   t❤✐s✳✈❡❧♦❝✐❞❛❞❡ ❂ ✵❀
⑥

                                                                                    121


[PAGINA 129]
6.2. Controle da nave na horizontal e na vertical                  Casa do Código


    E setar valores adequados no código de teste, no evento onload da im-
agem, pois calcularemos a posição a partir das medidas da imagem e, por-
tanto, ela deve estar carregada:

✴✴ ◗✉❛♥❞♦ ❝❛rr❡❣❛r ❛ ✐♠❛❣❡♠✱ ✐♥✐❝✐❛r ❛ ❛♥✐♠❛çã♦
✐♠❣◆❛✈❡✳♦♥❧♦❛❞ ❂ ❢✉♥❝t✐♦♥✭✮ ④
   ✴✴ ❈❡♥tr❛❧✐③❛❞❛ ♥❛ ❤♦r✐③♦♥t❛❧✱
   ✴✴ ❛❧✐♥❤❛❞❛ ❡♠❜❛✐①♦ ♥❛ ✈❡rt✐❝❛❧
   ♥❛✈❡✳① ❂ ❝❛♥✈❛s✳✇✐❞t❤ ✴ ✷ ✲ ✐♠❣◆❛✈❡✳✇✐❞t❤ ✴ ✷❀
   ♥❛✈❡✳② ❂ ❝❛♥✈❛s✳❤❡✐❣❤t ✲ ✐♠❣◆❛✈❡✳❤❡✐❣❤t❀
   ♥❛✈❡✳✈❡❧♦❝✐❞❛❞❡ ❂ ✺❀
   ❛♥✐♠❛❝❛♦✳❧✐❣❛r✭✮❀
⑥

    No método               desenhar,          copiaremos a imagem da nave sem
redimensioná-la:

❞❡s❡♥❤❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   t❤✐s✳❝♦♥t❡①t✳❞r❛✇■♠❛❣❡✭t❤✐s✳✐♠❛❣❡♠✱ t❤✐s✳①✱ t❤✐s✳②✱
         t❤✐s✳✐♠❛❣❡♠✳✇✐❞t❤✱ t❤✐s✳✐♠❛❣❡♠✳❤❡✐❣❤t✮❀
⑥

    Por último, certifique-se de que, no arquivo teclado.js, temos os códi-
gos de todas as teclas de que precisamos:

✴✴ ❈ó❞✐❣♦s ❞❡ t❡❝❧❛s ✲ ❛q✉✐ ✈ã♦ t♦❞♦s ♦s q✉❡ ❢♦r❡♠ ♥❡❝❡ssár✐♦s
✈❛r ❙❊❚❆❴❊❙◗❯❊❘❉❆ ❂ ✸✼❀
✈❛r ❙❊❚❆❴❆❈■▼❆ ❂ ✸✽❀
✈❛r ❙❊❚❆❴❉■❘❊■❚❆ ❂ ✸✾❀
✈❛r ❙❊❚❆❴❆❇❆■❳❖ ❂ ✹✵❀
✈❛r ❊❙P❆❈❖ ❂ ✸✷❀

     Voilà! Nossa nave move-se em todas as direções, sem ultrapassar os lim-
ites do Canvas!




122


[PAGINA 130]
Casa do Código                          Capítulo 6. Iniciando o desenvolvimento do jogo




            Figura 6.11: Controlando a nave pelas setas do teclado



6.3    Efetuando disparos
Agora a coisa vai começar a ficar divertida: nossa nave já se mexe, é hora de
fazê-la disparar tiros!




                                                                                   123


[PAGINA 131]
6.3. Efetuando disparos                                        Casa do Código




                          Figura 6.12: Fazendo a nave atirar


    Faça uma cópia do arquivo do teste anterior ( teste-nave.html) e
renomeie-a para teste-tiros.html. Logo antes do evento onload
da imagem, coloque o código que manda a nave atirar ao disparar a tecla
Espaço:

✴✴ ◆✉♥❝❛ ❢♦✐ tã♦ ❢á❝✐❧ ♠❛♥❞❛r ✉♠❛ ♥❛✈❡ ❛t✐r❛r✦
t❡❝❧❛❞♦✳❞✐s♣❛r♦✉✭❊❙P❆❈❖✱ ❢✉♥❝t✐♦♥✭✮ ④
   ♥❛✈❡✳❛t✐r❛r✭✮❀
⑥✮❀

✴✴ ◗✉❛♥❞♦ ❝❛rr❡❣❛r ❛ ✐♠❛❣❡♠✱ ✐♥✐❝✐❛r ❛ ❛♥✐♠❛çã♦
✐♠❣◆❛✈❡✳♦♥❧♦❛❞ ❂ ❢✉♥❝t✐♦♥✭✮ ④
   ✳✳✳
⑥

    Agora vamos criar o método atirar na classe Nave. Criar um tiro é
fácil, o problema é incluí-lo na animação de sprites. Não temos nenhuma
referência ao objeto animacao!


124


[PAGINA 132]
Casa do Código                            Capítulo 6. Iniciando o desenvolvimento do jogo



⑥✱
✴✴ ◆ã♦ ❡sq✉❡ç❛ ❞❛ ✈ír❣✉❧❛ ♥♦ ú❧t✐♠♦ ♠ét♦❞♦ q✉❛♥❞♦ ❝r✐❛r ♦✉tr♦
❛t✐r❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✈❛r t ❂ ♥❡✇ ❚✐r♦✭t❤✐s✳❝♦♥t❡①t✮❀

    ✴✴ ❈♦♠♦ ✐♥❝❧✉✐r ♦ ♥♦✈♦ t✐r♦ ♥❛ ❛♥✐♠❛çã♦❄
⑥

    Se você fez a lição de casa direitinho, poderia pensar: recebo pelo constru-
tor! Sim, é uma grande ideia, e eu apoio. Receber as coisas pelo construtor é
bem melhor do que fazer referência à variável animacao do aplicativo dire-
tamente. E se eu tento reaproveitar esta classe onde não tenho esta variável?
Receber pelo construtor forçaria o aplicativo a fornecer uma animação para
a nave.
    No entanto, pensando um pouco mais além, pode ser que eu tenha
dezenas (ou centenas) de variedades de sprites que precisam criar outros na
animação. Por que não damos a todos eles uma referência à animacao? Basta
abrir a classe Animacao e modificar seu método novoSprite:

♥♦✈♦❙♣r✐t❡✿ ❢✉♥❝t✐♦♥✭s♣r✐t❡✮ ④
   t❤✐s✳s♣r✐t❡s✳♣✉s❤✭s♣r✐t❡✮❀
   s♣r✐t❡✳❛♥✐♠❛❝❛♦ ❂ t❤✐s❀
⑥✱

    Agora qualquer sprite incluído tem uma referência ao objeto que controla
a animação! Não é legal?
    Podemos voltar ao método atirar da Nave e usar o objeto que ele
recebeu:

❛t✐r❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✈❛r t ❂ ♥❡✇ ❚✐r♦✭t❤✐s✳❝♦♥t❡①t✮❀
   t❤✐s✳❛♥✐♠❛❝❛♦✳♥♦✈♦❙♣r✐t❡✭t✮❀
⑥

    Enfim, vamos criar o esqueleto da classe Tiro:

✴✴ ❛rq✉✐✈♦✿ t✐r♦✳❥s
❢✉♥❝t✐♦♥ ❚✐r♦✭❝♦♥t❡①t✮ ④

                                                                                     125


[PAGINA 133]
6.3. Efetuando disparos                                        Casa do Código


      t❤✐s✳❝♦♥t❡①t ❂ ❝♦♥t❡①t❀
⑥
❚✐r♦✳♣r♦t♦t②♣❡ ❂ ④
   ❛t✉❛❧✐③❛r✿ ❢✉♥❝t✐♦♥✭✮ ④

      ⑥✱
      ❞❡s❡♥❤❛r✿ ❢✉♥❝t✐♦♥✭✮ ④

      ⑥
⑥

    Onde o tiro vai aparecer? Na ponta da nave, você vai pensar. Dessa forma,
é interessante recebermos a nave pelo construtor:

❢✉♥❝t✐♦♥ ❚✐r♦✭❝♦♥t❡①t✱ ♥❛✈❡✮ ④
   t❤✐s✳❝♦♥t❡①t ❂ ❝♦♥t❡①t❀
   t❤✐s✳♥❛✈❡ ❂ ♥❛✈❡❀
⑥

      No método atirar, a nave passa a si mesma para o tiro se posicionar:

❛t✐r❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✈❛r t ❂ ♥❡✇ ❚✐r♦✭t❤✐s✳❝♦♥t❡①t✱ t❤✐s✮❀
   t❤✐s✳❛♥✐♠❛❝❛♦✳♥♦✈♦❙♣r✐t❡✭t✮❀
⑥

    Tendo uma referência à nave, podemos posicionar o tiro. Faremos isso
no próprio construtor:

❢✉♥❝t✐♦♥ ❚✐r♦✭❝♦♥t❡①t✱ ♥❛✈❡✮ ④
   t❤✐s✳❝♦♥t❡①t ❂ ❝♦♥t❡①t❀
   t❤✐s✳♥❛✈❡ ❂ ♥❛✈❡❀

      ✴✴ P♦s✐❝✐♦♥❛r ♦ t✐r♦ ♥♦ ❜✐❝♦ ❞❛ ♥❛✈❡
      t❤✐s✳❧❛r❣✉r❛ ❂ ✹❀
      t❤✐s✳❛❧t✉r❛ ❂ ✷✵❀
      t❤✐s✳① ❂ ♥❛✈❡✳① ✰ ♥❛✈❡✳✐♠❛❣❡♠✳✇✐❞t❤ ✴ ✷ ✲ t❤✐s✳❧❛r❣✉r❛ ✴ ✷❀
      t❤✐s✳② ❂ ♥❛✈❡✳② ✲ t❤✐s✳❛❧t✉r❛❀
      t❤✐s✳✈❡❧♦❝✐❞❛❞❡ ❂ ✶✵❀
⑥

126


[PAGINA 134]
Casa do Código                         Capítulo 6. Iniciando o desenvolvimento do jogo



    Para atualizar o tiro na animação, apenas o faremos subir na tela, sub-
traindo sua posição y:

❛t✉❛❧✐③❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   t❤✐s✳② ✲❂ t❤✐s✳✈❡❧♦❝✐❞❛❞❡❀
⑥✱

    Para desenhá-lo, faremos um pequeno retângulo. Criamos um novo
atributo, cor, para que possa ser alterado a gosto:

❞❡s❡♥❤❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✈❛r ❝t① ❂ t❤✐s✳❝♦♥t❡①t❀
   ❝t①✳s❛✈❡✭✮❀
   ❝t①✳❢✐❧❧❙t②❧❡ ❂ t❤✐s✳❝♦r❀
   ❝t①✳❢✐❧❧❘❡❝t✭t❤✐s✳①✱ t❤✐s✳②✱ t❤✐s✳❧❛r❣✉r❛✱ t❤✐s✳❛❧t✉r❛✮❀
   ❝t①✳r❡st♦r❡✭✮❀
⑥

   No construtor, vamos inicializar cor com uma cor mais escura, pois a
nave ainda está em fundo branco:

✴✴ ❊s❝♦❧❤❛ s✉❛ ❝♦r✦
t❤✐s✳❝♦r ❂ ✬r❡❞✬❀

    Por último, não se esqueça de colocar a referência ao arquivo tiro.js
na página HTML:

❁❤❡❛❞❃
   ❁t✐t❧❡❃◆❛✈❡ ❊s♣❛❝✐❛❧ ◗✉❡ ❆t✐r❛❁✴t✐t❧❡❃
   ❁s❝r✐♣t sr❝❂✧❛♥✐♠❛❝❛♦✳❥s✧❃❁✴s❝r✐♣t❃
   ❁s❝r✐♣t sr❝❂✧t❡❝❧❛❞♦✳❥s✧❃❁✴s❝r✐♣t❃
   ❁s❝r✐♣t sr❝❂✧♥❛✈❡✳❥s✧❃❁✴s❝r✐♣t❃
   ❁s❝r✐♣t sr❝❂✧t✐r♦✳❥s✧❃❁✴s❝r✐♣t❃
❁✴❤❡❛❞❃

   Divirta-se! No próximo capítulo, iremos criar inimigos para o nosso
herói.




                                                                                  127


[PAGINA 135]
6.3. Efetuando disparos                                          Casa do Código




  Exercícios:

      Se você entendeu bem os conceitos, as tarefas a seguir não deverão
  ser tão difíceis assim:

        • Tente integrar o fundo em parallax com a nave se mexendo e ati-
          rando.

        • Tente também atirar para os lados e para a diagonal. Isto requererá
          ler o estado das teclas de direção e dar velocidade horizontal ao
          tiro.

       Comece a brincar e a experimentar!




128


[PAGINA 136]
Capítulo 7

Criando inimigos
Chegou a hora de adicionarmos um pouco de emoção verdadeira em nosso
game. De nada adianta termos um jogo e não termos quem combater, não
é mesmo? Portanto, criaremos agora os primeiros inimigos. Neste capítulo,
utilizaremos bastante a classe Colisor para detectar quando os inimigos
colidirem com os tiros e com a nave.
     No pacote de arquivos do livro, está presente a imagem ovni.png. Nosso
objetivo será fazer OVNIs caírem do alto da tela, em velocidades e posições x
diferentes.


[PAGINA 137]
7.1. Primeiro teste com nave e inimigos                           Casa do Código




                             Figura 7.1: OVNIs cairão na tela!



7.1 Primeiro teste com nave e inimigos
Como de costume, vamos começar com a página contendo o aplicativo de
teste. Veja como a quantidade de tags <script> está crescendo! Nosso
protótipo está cada vez mais perto de um jogo 100% funcional.




                     Figura 7.2: Cena com OVNIs e nave do herói


❁✦✲✲ ❛rq✉✐✈♦✿ t❡st❡✲✐♥✐♠✐❣♦s✳❤t♠❧ ✲✲❃
❁✦❉❖❈❚❨P❊ ❤t♠❧❃

❁❤t♠❧❃

130


[PAGINA 138]
Casa do Código                                         Capítulo 7. Criando inimigos




❁❤❡❛❞❃
   ❁t✐t❧❡❃■♥✐♠✐❣♦s❁✴t✐t❧❡❃
   ❁s❝r✐♣t sr❝❂✧❛♥✐♠❛❝❛♦✳❥s✧❃❁✴s❝r✐♣t❃
   ❁s❝r✐♣t sr❝❂✧t❡❝❧❛❞♦✳❥s✧❃❁✴s❝r✐♣t❃
   ❁s❝r✐♣t sr❝❂✧♥❛✈❡✳❥s✧❃❁✴s❝r✐♣t❃
   ❁s❝r✐♣t sr❝❂✧t✐r♦✳❥s✧❃❁✴s❝r✐♣t❃
   ❁s❝r✐♣t sr❝❂✧❝♦❧✐s♦r✳❥s✧❃❁✴s❝r✐♣t❃
   ❁s❝r✐♣t sr❝❂✧♦✈♥✐✳❥s✧❃❁✴s❝r✐♣t❃
❁✴❤❡❛❞❃

❁❜♦❞②❃
   ❁❝❛♥✈❛s ✐❞❂✧❝❛♥✈❛s❴✐♥✐♠✐❣♦s✧ ✇✐❞t❤❂✧✺✵✵✧ ❤❡✐❣❤t❂✧✺✵✵✧❃
   ❁✴❝❛♥✈❛s❃
   ❁s❝r✐♣t❃
      ✴✴ ■♥✐♠✐❣♦s t❡rrí✈❡✐s t❡♥t❛rã♦ ❞❡str✉í✲❧♦✦
   ❁✴s❝r✐♣t❃
❁✴❜♦❞②❃

❁✴❤t♠❧❃

    Para começar o JavaScript, vamos carregar as imagens, pois os sprites pre-
cisarão recebê-las pelos construtores. Como são duas, usaremos uma função
carregando para detectar quando elas estiverem prontas:

✴✴ ■♠❛❣❡♥s
✈❛r ✐♠❣◆❛✈❡ ❂ ♥❡✇ ■♠❛❣❡✭✮❀
✐♠❣◆❛✈❡✳sr❝ ❂ ✬✐♠❣✴♥❛✈❡✳♣♥❣✬❀
✐♠❣◆❛✈❡✳♦♥❧♦❛❞ ❂ ❝❛rr❡❣❛♥❞♦❀

✈❛r ✐♠❣❖✈♥✐ ❂ ♥❡✇ ■♠❛❣❡✭✮❀
✐♠❣❖✈♥✐✳sr❝ ❂ ✬✐♠❣✴♦✈♥✐✳♣♥❣✬❀
✐♠❣❖✈♥✐✳♦♥❧♦❛❞ ❂ ❝❛rr❡❣❛♥❞♦❀

   Em seguida, a criação dos objetos básicos: canvas e contexto, teclado, an-
imação, sprite da nave e colisor. Também configuramos o disparo pela tecla
Espaço. Pode parecer repetitivo, mas a ideia é essa mesmo: tornar o negócio
padronizado (e dessa forma você fixa melhor os conceitos)!


                                                                               131


[PAGINA 139]
7.1. Primeiro teste com nave e inimigos                   Casa do Código


✴✴ ■♥✐❝✐❛❧✐③❛çã♦ ❞♦s ♦❜❥❡t♦s
✈❛r ❝❛♥✈❛s ❂ ❞♦❝✉♠❡♥t✳❣❡t❊❧❡♠❡♥t❇②■❞✭✬❝❛♥✈❛s❴✐♥✐♠✐❣♦s✬✮❀
✈❛r ❝♦♥t❡①t ❂ ❝❛♥✈❛s✳❣❡t❈♦♥t❡①t✭✬✷❞✬✮❀

✈❛r t❡❝❧❛❞♦ ❂ ♥❡✇ ❚❡❝❧❛❞♦✭❞♦❝✉♠❡♥t✮❀
✈❛r ❛♥✐♠❛❝❛♦ ❂ ♥❡✇ ❆♥✐♠❛❝❛♦✭❝♦♥t❡①t✮❀

✈❛r ♥❛✈❡ ❂ ♥❡✇ ◆❛✈❡✭❝♦♥t❡①t✱ t❡❝❧❛❞♦✱ ✐♠❣◆❛✈❡✮❀
❛♥✐♠❛❝❛♦✳♥♦✈♦❙♣r✐t❡✭♥❛✈❡✮❀

✈❛r ❝♦❧✐s♦r ❂ ♥❡✇ ❈♦❧✐s♦r✭✮❀
❝♦❧✐s♦r✳♥♦✈♦❙♣r✐t❡✭♥❛✈❡✮❀

t❡❝❧❛❞♦✳❞✐s♣❛r♦✉✭❊❙P❆❈❖✱ ❢✉♥❝t✐♦♥✭✮ ④
   ♥❛✈❡✳❛t✐r❛r✭✮❀
⑥✮❀

    Agora crie as funções carregando, que monitora o carregamento das
imagens, e iniciar, chamada por carregando quando todas as imagens
estiverem prontas. Na função iniciar, posicionamos a nave, iniciamos a
animação e definimos que a cada 1000 milissegundos um novo inimigo será
criado na tela, usando a função setInterval do JavaScript:

✴✴ ❈❛rr❡❣❛♠❡♥t♦ ❡ ✐♥✐❝✐❛❧✐③❛çã♦
✈❛r ❝❛rr❡❣❛❞❛s ❂ ✵❀

❢✉♥❝t✐♦♥ ❝❛rr❡❣❛♥❞♦✭✮ ④
   ❝❛rr❡❣❛❞❛s✰✰❀
   ✐❢ ✭❝❛rr❡❣❛❞❛s ❂❂ ✷✮ ✐♥✐❝✐❛r✭✮❀
⑥

❢✉♥❝t✐♦♥ ✐♥✐❝✐❛r✭✮ ④
   ♥❛✈❡✳① ❂ ❝❛♥✈❛s✳✇✐❞t❤ ✴ ✷ ✲ ✐♠❣◆❛✈❡✳✇✐❞t❤ ✴ ✷❀
   ♥❛✈❡✳② ❂ ❝❛♥✈❛s✳❤❡✐❣❤t ✲ ✐♠❣◆❛✈❡✳❤❡✐❣❤t❀
   ♥❛✈❡✳✈❡❧♦❝✐❞❛❞❡ ❂ ✺❀
   ❛♥✐♠❛❝❛♦✳❧✐❣❛r✭✮❀

      s❡t■♥t❡r✈❛❧✭♥♦✈♦❖✈♥✐✱ ✶✵✵✵✮❀
⑥

132


[PAGINA 140]
Casa do Código                                         Capítulo 7. Criando inimigos



    Quem criará o inimigo é a função novoOvni. Sabendo que a imagem
possui 64x32 pixels, nós a posicionamos acima da área visível do jogo, de-
scontando 32 pixels de altura. Para dar um pouco de emoção ao game, a
posição horizontal e a velocidade são definidas aleatoriamente para cada novo
inimigo, com o auxílio de Math.random e Math.floor. Também é preciso
colocar o inimigo no colisor:

✴✴ ❈r✐❛çã♦ ❞♦s ✐♥✐♠✐❣♦s
❢✉♥❝t✐♦♥ ♥♦✈♦❖✈♥✐✭✮ ④
   ✈❛r ♦✈♥✐ ❂ ♥❡✇ ❖✈♥✐✭❝♦♥t❡①t✱ ✐♠❣❖✈♥✐✮❀

    ✴✴ ▼í♥✐♠♦✿ ✺❀ ♠á①✐♠♦✿ ✷✵
    ♦✈♥✐✳✈❡❧♦❝✐❞❛❞❡ ❂
       ▼❛t❤✳❢❧♦♦r✭ ✺ ✰ ▼❛t❤✳r❛♥❞♦♠✭✮ ✯ ✭✷✵ ✲ ✺ ✰ ✶✮ ✮❀

    ✴✴ ▼í♥✐♠♦✿ ✵❀
    ✴✴ ♠á①✐♠♦✿ ❧❛r❣✉r❛ ❞♦ ❝❛♥✈❛s ✲ ❧❛r❣✉r❛ ❞♦ ♦✈♥✐
    ♦✈♥✐✳① ❂
       ▼❛t❤✳❢❧♦♦r✭▼❛t❤✳r❛♥❞♦♠✭✮ ✯
                  ✭❝❛♥✈❛s✳✇✐❞t❤ ✲ ✐♠❣❖✈♥✐✳✇✐❞t❤ ✰ ✶✮ ✮❀

    ✴✴ ❉❡s❝♦♥t❛r ❛ ❛❧t✉r❛
    ♦✈♥✐✳② ❂ ✲✐♠❣❖✈♥✐✳❤❡✐❣❤t❀

    ❛♥✐♠❛❝❛♦✳♥♦✈♦❙♣r✐t❡✭♦✈♥✐✮❀
    ❝♦❧✐s♦r✳♥♦✈♦❙♣r✐t❡✭♦✈♥✐✮❀
⑥




                                                                               133


[PAGINA 141]
7.2. A classe Ovni                                                Casa do Código




   Combinando Math.random e Math.floor

       O método random retorna um número aleatório fracionário, entre 0
   e 1. Para gerar um número aleatório inteiro, usamos a fórmula:

   ❢✉♥❝t✐♦♥ ❛❧❡❛t♦r✐♦✭♠✐♥✱ ♠❛①✮ ④
       r❡t✉r♥ ♠✐♥ ✰ ▼❛t❤✳❢❧♦♦r✭▼❛t❤✳r❛♥❞♦♠✭✮ ✯ ✭♠❛① ✲ ♠✐♥ ✰ ✶✮✮❀
   ⑥

      O método floor descarta a parte fracionária do resultado,
   arredondando-o para o inteiro de menor valor (não o mais próximo).




   Padronizando a codificação

      Vamos sempre adotar a seguinte sequência de codificação ao criar
   novos aplicativos:

        • Primeiro, carregamos as imagens, pois os objetos do jogo depen-
          dem delas;

        • Em seguida, instanciamos os objetos do game engine (animação,
          teclado, colisor) e os sprites, usando as imagens quando necessário;

        • Por último, criamos as funções de inicialização, que só devem ex-
          ecutar quando as imagens estiverem completamente carregadas.




7.2 A classe Ovni
Vamos criar a classe Ovni, inicialmente sem se preocupar com a interface de
colisão. Como de costume, começamos construindo um esqueleto a partir do
que idealizamos para a classe na página HTML:



134


[PAGINA 142]
Casa do Código                                      Capítulo 7. Criando inimigos



✴✴ ❛rq✉✐✈♦✿ ♦✈♥✐✳❥s
❢✉♥❝t✐♦♥ ❖✈♥✐✭❝♦♥t❡①t✱ ✐♠❛❣❡♠✮ ④
   t❤✐s✳❝♦♥t❡①t ❂ ❝♦♥t❡①t❀
   t❤✐s✳✐♠❛❣❡♠ ❂ ✐♠❛❣❡♠❀
   t❤✐s✳① ❂ ✵❀
   t❤✐s✳② ❂ ✵❀
   t❤✐s✳✈❡❧♦❝✐❞❛❞❡ ❂ ✵❀
⑥
❖✈♥✐✳♣r♦t♦t②♣❡ ❂ ④
   ❛t✉❛❧✐③❛r✿ ❢✉♥❝t✐♦♥✭✮ ④

    ⑥✱
    ❞❡s❡♥❤❛r✿ ❢✉♥❝t✐♦♥✭✮ ④

    ⑥
⑥

   Se o objetivo é fazer o inimigo descer pela tela, o método atualizar
tem de incrementar a posição y:
❛t✉❛❧✐③❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   t❤✐s✳② ✰❂ t❤✐s✳✈❡❧♦❝✐❞❛❞❡❀
⑥✱

   Já o método desenhar apenas desenha a imagem que foi recebida no
construtor:
❞❡s❡♥❤❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✈❛r ❝t① ❂ t❤✐s✳❝♦♥t❡①t❀
   ✈❛r ✐♠❣ ❂ t❤✐s✳✐♠❛❣❡♠❀
   ❝t①✳❞r❛✇■♠❛❣❡✭✐♠❣✱ t❤✐s✳①✱ t❤✐s✳②✱ ✐♠❣✳✇✐❞t❤✱ ✐♠❣✳❤❡✐❣❤t✮❀
⑥

    Já temos uma nave que atira (programada no capítulo anterior) e OVNIs
descendo no mesmo aplicativo (figura 7.2)!


7.3 Adicionando fundo em parallax
No capítulo anterior, criamos um fundo consistindo de várias imagens
em movimento, cada uma em velocidade diferente, criando um efeito que

                                                                            135


[PAGINA 143]
7.3. Adicionando fundo em parallax                           Casa do Código


chamamos parallax. Chegou a hora de integrar esse fundo ao nosso game.
    Primeiro, faça uma cópia do arquivo teste-inimigos.html, dando-
lhe o nome teste-inimigos-e-fundo.html. Iremos fazer algumas al-
terações em determinados pontos.
    No início do código, onde carregamos as imagens, adicione o carrega-
mento das três imagens de fundo:
✴✴ ■♠❛❣❡♥s
✈❛r ✐♠❣❊s♣❛❝♦ ❂ ♥❡✇ ■♠❛❣❡✭✮❀
✐♠❣❊s♣❛❝♦✳sr❝ ❂ ✬✐♠❣✴❢✉♥❞♦✲❡s♣❛❝♦✳♣♥❣✬❀
✐♠❣❊s♣❛❝♦✳♦♥❧♦❛❞ ❂ ❝❛rr❡❣❛♥❞♦❀

✈❛r ✐♠❣❊str❡❧❛s ❂ ♥❡✇ ■♠❛❣❡✭✮❀
✐♠❣❊str❡❧❛s✳sr❝ ❂ ✬✐♠❣✴❢✉♥❞♦✲❡str❡❧❛s✳♣♥❣✬❀
✐♠❣❊str❡❧❛s✳♦♥❧♦❛❞ ❂ ❝❛rr❡❣❛♥❞♦❀

✈❛r ✐♠❣◆✉✈❡♥s ❂ ♥❡✇ ■♠❛❣❡✭✮❀
✐♠❣◆✉✈❡♥s✳sr❝ ❂ ✬✐♠❣✴❢✉♥❞♦✲♥✉✈❡♥s✳♣♥❣✬❀
✐♠❣◆✉✈❡♥s✳♦♥❧♦❛❞ ❂ ❝❛rr❡❣❛♥❞♦❀

✴✴ ■♠❛❣❡♥s ❞❛ ♥❛✈❡ ❡ ❞♦s ♦✈♥✐s✳✳✳

    Agora temos cinco imagens no total, portanto temos que alterar a função
carregando para contar até 5. Uma variável total nos permitirá alterar
este parâmetro mais facilmente:
✴✴ ❈❛rr❡❣❛♠❡♥t♦ ❡ ✐♥✐❝✐❛❧✐③❛çã♦
✈❛r ❝❛rr❡❣❛❞❛s ❂ ✵❀
✈❛r t♦t❛❧ ❂ ✺❀

❢✉♥❝t✐♦♥ ❝❛rr❡❣❛♥❞♦✭✮ ④
   ❝❛rr❡❣❛❞❛s✰✰❀
   ✐❢ ✭❝❛rr❡❣❛❞❛s ❂❂ t♦t❛❧✮ ✐♥✐❝✐❛r✭✮❀
⑥

    Precisamos adicionar os fundos à animação antes dos outros sprites, de
forma que eles sejam desenhados primeiro. Na seção onde inicializamos os
objetos do game engine e os sprites, antes da criação da nave, adicione o
código:

136


[PAGINA 144]
Casa do Código                                  Capítulo 7. Criando inimigos



✴✴ Pr✐♠❡✐r♦ ♦s ♦❜❥❡t♦s ❞♦ ❣❛♠❡ ❡♥❣✐♥❡
✈❛r ❝❛♥✈❛s ❂ ✳✳✳
✈❛r ❝♦♥t❡①t ❂ ✳✳✳
✈❛r t❡❝❧❛❞♦ ❂ ✳✳✳
✈❛r ❛♥✐♠❛❝❛♦ ❂ ✳✳✳

✴✴ ❊♠ s❡❣✉✐❞❛ ❛s ✐♠❛❣❡♥s ❞❡ ❢✉♥❞♦
✈❛r ❢✉♥❞♦✶ ❂ ♥❡✇ ❋✉♥❞♦✭❝♦♥t❡①t✱ ✐♠❣❊s♣❛❝♦✮❀
❢✉♥❞♦✶✳✈❡❧♦❝✐❞❛❞❡ ❂ ✸❀
❛♥✐♠❛❝❛♦✳♥♦✈♦❙♣r✐t❡✭❢✉♥❞♦✶✮❀

✈❛r ❢✉♥❞♦✷ ❂ ♥❡✇ ❋✉♥❞♦✭❝♦♥t❡①t✱ ✐♠❣❊str❡❧❛s✮❀
❢✉♥❞♦✷✳✈❡❧♦❝✐❞❛❞❡ ❂ ✼❀
❛♥✐♠❛❝❛♦✳♥♦✈♦❙♣r✐t❡✭❢✉♥❞♦✷✮❀

✈❛r ❢✉♥❞♦✸ ❂ ♥❡✇ ❋✉♥❞♦✭❝♦♥t❡①t✱ ✐♠❣◆✉✈❡♥s✮❀
❢✉♥❞♦✸✳✈❡❧♦❝✐❞❛❞❡ ❂ ✶✵❀
❛♥✐♠❛❝❛♦✳♥♦✈♦❙♣r✐t❡✭❢✉♥❞♦✸✮❀

✴✴ ❉❡♣♦✐s ❞♦ ❢✉♥❞♦✱ ❛ ♥❛✈❡ ❡ ♦✉tr♦s s♣r✐t❡s
✈❛r ♥❛✈❡ ❂ ✳✳✳




                                                                        137


[PAGINA 145]
7.3. Adicionando fundo em parallax                               Casa do Código




    Figura 7.3: Cena com OVNIs, nave do herói e fundo rolando em parallax


     Neste ponto, o fundo já se movimenta juntamente com a nave e os inimi-
gos (figura 7.3). A partir de agora, como trabalharemos sempre com um fundo
rolando, não é preciso mais realizar a limpeza de tela a cada ciclo da animação,
bastando apenas desenhar o fundo para cobrir a tela. Isso não trará efeitos
práticos mas economizará algum processamento. Por isso, vamos comentar
a linha que limpa a tela no método proximoFrame da classe Animacao.
♣r♦①✐♠♦❋r❛♠❡✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✴✴ P♦ss♦ ❝♦♥t✐♥✉❛r❄
   ✐❢ ✭ ✦ t❤✐s✳❧✐❣❛❞♦ ✮ r❡t✉r♥❀

      ✴✴ ❈♦♠❡♥t❡ ♦ ❝♦♠❛♥❞♦ q✉❡ ❧✐♠♣❛ ❛ t❡❧❛
      ✴✴ t❤✐s✳❧✐♠♣❛r❚❡❧❛✭✮❀

      ✴✴ ✳✳✳
⑥

      Obs.: recomendo que você faça uma cópia do arquivo animacao.js

138


[PAGINA 146]
Casa do Código                                           Capítulo 7. Criando inimigos



especialmente para este tópico. Do contrário, testes anteriores serão afetados
(figura 7.4). Para os próximos capítulos, você poderá usar a nova versão desse
arquivo.




Figura 7.4: Mantenha a limpeza de tela para os testes anteriores, caso contrário
serão prejudicados.


   Experimente rodar o aplicativo. Já temos um protótipo de jogo quase
pronto!


7.4    Adicionando colisão
A parte que falta para termos um protótipo funcional é detectar a colisão entre
os sprites — mais exatamente, entre o inimigo e a nave (causando a morte do
herói) e entre os inimigos e o tiro (causando a destruição do inimigo).
    Precisamos, em algum ponto de nosso programa, chamar o método
processar do Colisor. Que tal se a Animacao chamar o colisor em
cada ciclo? Assim, teremos um controle mais geral, que ocorre em conjunto
com o processamento dos ciclos de animação.


                                                                                 139


[PAGINA 147]
7.4. Adicionando colisão                                   Casa do Código


    Indo mais além, a Animacao poderia manter uma lista de processamen-
tos a executar, dos quais um é o Colisor. Mais adiante, podemos adicionar
Gravidade, TelaMovel e por aí vai. Façamos isto!
    No construtor da classe Animacao, adicione o comando que inicia um
array vazio processamentos:
t❤✐s✳♣r♦❝❡ss❛♠❡♥t♦s ❂ ❬❪❀

    Crie o método novoProcessamento, para inserir novos processamen-
tos no array:
♥♦✈♦Pr♦❝❡ss❛♠❡♥t♦✿ ❢✉♥❝t✐♦♥✭♣r♦❝❡ss❛♠❡♥t♦✮ ④
   t❤✐s✳♣r♦❝❡ss❛♠❡♥t♦s✳♣✉s❤✭♣r♦❝❡ss❛♠❡♥t♦✮❀
   ♣r♦❝❡ss❛♠❡♥t♦✳❛♥✐♠❛❝❛♦ ❂ t❤✐s❀
⑥

      No método proximoFrame, vamos executar estes processamentos:
♣r♦①✐♠♦❋r❛♠❡✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✴✴ P♦ss♦ ❝♦♥t✐♥✉❛r❄
   ✐❢ ✭ ✦ t❤✐s✳❧✐❣❛❞♦ ✮ r❡t✉r♥❀

      ✴✴ ❆t✉❛❧✐③❛♠♦s ♦ ❡st❛❞♦ ❞♦s s♣r✐t❡s
      ❢♦r ✭✈❛r ✐ ✐♥ t❤✐s✳s♣r✐t❡s✮
         t❤✐s✳s♣r✐t❡s❬✐❪✳❛t✉❛❧✐③❛r✭✮❀

      ✴✴ ❉❡s❡♥❤❛♠♦s ♦s s♣r✐t❡s
      ❢♦r ✭✈❛r ✐ ✐♥ t❤✐s✳s♣r✐t❡s✮
         t❤✐s✳s♣r✐t❡s❬✐❪✳❞❡s❡♥❤❛r✭✮❀

      ✴✴ Pr♦❝❡ss❛♠❡♥t♦s ❣❡r❛✐s
      ❢♦r ✭✈❛r ✐ ✐♥ t❤✐s✳♣r♦❝❡ss❛♠❡♥t♦s✮
         t❤✐s✳♣r♦❝❡ss❛♠❡♥t♦s❬✐❪✳♣r♦❝❡ss❛r✭✮❀

      ✴✴ ❈❤❛♠❛♠♦s ♦ ♣ró①✐♠♦ ❝✐❝❧♦
      ✈❛r ❛♥✐♠❛❝❛♦ ❂ t❤✐s❀
      r❡q✉❡st❆♥✐♠❛t✐♦♥❋r❛♠❡✭❢✉♥❝t✐♦♥✭✮ ④
         ❛♥✐♠❛❝❛♦✳♣r♦①✐♠♦❋r❛♠❡✭✮❀
      ⑥✮❀
⑥✱

140


[PAGINA 148]
Casa do Código                                         Capítulo 7. Criando inimigos



Iniciando o teste
    Já temos o arquivo        teste-inimigos-e-fundo.html, com
tudo o que foi feito até aqui.        Faça uma cópia e dê o nome
teste-colisao-inimigos.html. Localize o ponto onde o colisor
é criado e acrescente-o como um processamento da animação:

✈❛r ❝♦❧✐s♦r ❂ ♥❡✇ ❈♦❧✐s♦r✭✮❀
❝♦❧✐s♦r✳♥♦✈♦❙♣r✐t❡✭♥❛✈❡✮❀
❛♥✐♠❛❝❛♦✳♥♦✈♦Pr♦❝❡ss❛♠❡♥t♦✭❝♦❧✐s♦r✮❀

    Os inimigos já estão sendo adicionados no colisor, porém faltam os tiros.
Eles são criados no método atirar da Nave. Modifique-o para que o tiro
criado seja incluído no colisor:

❛t✐r❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✈❛r t ❂ ♥❡✇ ❚✐r♦✭t❤✐s✳❝♦♥t❡①t✱ t❤✐s✮❀
   t❤✐s✳❛♥✐♠❛❝❛♦✳♥♦✈♦❙♣r✐t❡✭t✮❀
   t❤✐s✳❝♦❧✐s♦r✳♥♦✈♦❙♣r✐t❡✭t✮❀
⑥

    Mas... a nave tem referência ao colisor? Seria bom que cada sprite adi-
cionado no colisor tivesse uma referência a este (assim como a Animacao já
faz). Modifique o método novoSprite do Colisor para fazer isso:

♥♦✈♦❙♣r✐t❡✿ ❢✉♥❝t✐♦♥✭s♣r✐t❡✮ ④
   t❤✐s✳s♣r✐t❡s✳♣✉s❤✭s♣r✐t❡✮❀
   s♣r✐t❡✳❝♦❧✐s♦r ❂ t❤✐s❀
⑥✱




                                                                               141


[PAGINA 149]
7.4. Adicionando colisão                                      Casa do Código




  Referências cruzadas

      Vamos adotar a prática de, em qualquer objeto que agregue e processe
  vários outros objetos ( Animacao, Colisor etc.), colocar neles uma
  referência ao objeto agregador. Por exemplo:

  ✴✴ ❆❞✐❝✐♦♥♦ ✉♠ s♣r✐t❡ ❛♦ ❝♦❧✐s♦r
  ❝♦❧✐s♦r✳♥♦✈♦❙♣r✐t❡✭❝❛rr♦✮❀

  ✴✴ ❖ ❝♦❧✐s♦r ❛❞✐❝✐♦♥❛✲s❡ ❛ s✐ ♠❡s♠♦ ♥♦ s♣r✐t❡
  ♥♦✈♦❙♣r✐t❡✿ ❢✉♥❝t✐♦♥✭s♣r✐t❡✮ ④
     t❤✐s✳s♣r✐t❡s✳♣✉s❤✭s♣r✐t❡✮❀
     s♣r✐t❡✳❝♦❧✐s♦r ❂ t❤✐s❀
  ⑥✱




Adaptando os sprites à interface do colisor
   Neste ponto, se tentarmos rodar o aplicativo, a animação irá parar abrup-
tamente e teremos a seguinte mensagem no console ( Ctrl+Shift+J no
Google Chrome, Ctrl+Shift+K no Firefox):




       Figura 7.5: Tentando chamar um método que não existe no objeto


    Isso ocorreu porque agora o colisor está sendo chamado, e este, por sua
vez, chama os métodos retanguloColisao e colidiuCom. Precisamos
implementá-los nas classes Nave, Tiro, e Ovni. Faça isto nas três, por
enquanto deixando os corpos dos métodos vazios:

r❡t❛♥❣✉❧♦s❈♦❧✐s❛♦✿ ❢✉♥❝t✐♦♥✭✮ ④



142


[PAGINA 150]
Casa do Código                                          Capítulo 7. Criando inimigos



⑥✱
❝♦❧✐❞✐✉❈♦♠✿ ❢✉♥❝t✐♦♥✭♦✉tr♦✮ ④

⑥

     Agora o aplicativo voltou a funcionar como a versão anterior. Vamos
definir os retângulos de colisão dos sprites. O mais fácil é o do Tiro, que
já é retangular:

r❡t❛♥❣✉❧♦s❈♦❧✐s❛♦✿ ❢✉♥❝t✐♦♥✭✮ ④
   r❡t✉r♥ ❬ ④①✿ t❤✐s✳①✱ ②✿ t❤✐s✳②✱ ❧❛r❣✉r❛✿ t❤✐s✳❧❛r❣✉r❛✱
         ❛❧t✉r❛✿ t❤✐s✳❛❧t✉r❛⑥ ❪❀
⑥✱

    Para a nave, vamos fazer três retângulos, para o corpo e as duas asas
(figura 7.6). Não há uma regra fixa de quantos retângulos usar, você define
a partir do formato de seu objeto. No caso de objetos mais complexos, é in-
teressante desenhar os retângulos na tela, a fim de podermos ajustar os valores
das posições mais facilmente:

r❡t❛♥❣✉❧♦s❈♦❧✐s❛♦✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✴✴ ❊st❡s ✈❛❧♦r❡s ✈ã♦ s❡♥❞♦ ❛❥✉st❛❞♦s ❛♦s ♣♦✉❝♦s
   ✈❛r r❡ts ❂
   ❬
      ④①✿ t❤✐s✳①✰✷✱ ②✿ t❤✐s✳②✰✶✾✱ ❧❛r❣✉r❛✿ ✾✱ ❛❧t✉r❛✿ ✶✸⑥✱
      ④①✿ t❤✐s✳①✰✶✸✱ ②✿ t❤✐s✳②✰✸✱ ❧❛r❣✉r❛✿ ✶✵✱ ❛❧t✉r❛✿ ✸✸⑥✱
      ④①✿ t❤✐s✳①✰✷✺✱ ②✿ t❤✐s✳②✰✶✾✱ ❧❛r❣✉r❛✿ ✾✱ ❛❧t✉r❛✿ ✶✸⑥
   ❪❀

    ✴✴ ❉❡s❡♥❤❛♥❞♦ ♦s r❡tâ♥❣✉❧♦s ♣❛r❛ ✈✐s✉❛❧✐③❛çã♦
    ✈❛r ❝t① ❂ t❤✐s✳❝♦♥t❡①t❀

    ❢♦r ✭✈❛r ✐ ✐♥ r❡ts✮ ④
       ❝t①✳s❛✈❡✭✮❀
       ❝t①✳str♦❦❡❙t②❧❡ ❂ ✬②❡❧❧♦✇✬❀
       ❝t①✳str♦❦❡❘❡❝t✭r❡ts❬✐❪✳①✱ r❡ts❬✐❪✳②✱ r❡ts❬✐❪✳❧❛r❣✉r❛✱
                      r❡ts❬✐❪✳❛❧t✉r❛✮❀
       ❝t①✳r❡st♦r❡✭✮❀
    ⑥

                                                                               143


[PAGINA 151]
7.4. Adicionando colisão                                           Casa do Código




      r❡t✉r♥ r❡ts❀
⑥✱




                       Figura 7.6: Retângulos de colisão da nave


    Para analisar os retângulos de sprites em movimento, facilita muito abrir
o console ( Ctrl+Shift+J no Chrome; no Firefox instale o plugin Firebug)
e chamar o comando: animacao.desligar():




Figura 7.7: Pare a animação pelo console para analisar os retângulos de colisão


      Para o OVNI, também usei três retângulos:

r❡t❛♥❣✉❧♦s❈♦❧✐s❛♦✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✈❛r r❡ts ❂
   ❬
      ④①✿ t❤✐s✳①✰✷✵✱ ②✿ t❤✐s✳②✰✶✱ ❧❛r❣✉r❛✿ ✷✺✱ ❛❧t✉r❛✿ ✶✵⑥✱
      ④①✿ t❤✐s✳①✰✷✱ ②✿ t❤✐s✳②✰✶✶✱ ❧❛r❣✉r❛✿ ✻✵✱ ❛❧t✉r❛✿ ✶✷⑥✱
      ④①✿ t❤✐s✳①✰✷✵✱ ②✿ t❤✐s✳②✰✷✸✱ ❧❛r❣✉r❛✿ ✷✺✱ ❛❧t✉r❛✿ ✼⑥✱
   ❪❀


144


[PAGINA 152]
Casa do Código                                       Capítulo 7. Criando inimigos




      ✴✴ ❉❡s❡♥❤♦ ❞♦s r❡tâ♥❣✉❧♦s ✳✳✳
⑥




                 Figura 7.8: Retângulos de colisão do OVNI


   Rode o aplicativo e dê alguns tiros. Você rapidamente perceberá um prob-
lema...


7.5     Estamos experimentando lentidão!
Nosso jogo chegou em um ponto em que muitos objetos estão sendo criados,
mas não estão sendo destruídos! Agora, além do loop de animação, eles
também devem responder às chamadas do colisor. Isso, claro, está sobrecar-
regando o aplicativo.




                                                                            145


[PAGINA 153]
7.5. Estamos experimentando lentidão!                          Casa do Código




    Figura 7.9: Experimente dar muitos tiros: nosso jogo ficará bem lento!


    Nosso game engine, embora tenha funcionado perfeitamente até aqui,
carece de algo bem básico: não é possível excluir objetos, tanto da animação
quanto do colisor. Estamos sempre criando novos tiros e inimigos, mas não
os destruímos quando estes deixam a tela. Resultado: continuam sendo pro-
cessados.
    O que precisamos para excluir tiros e inimigos que já se foram da tela?
    Importante: siga este tópico com bastante atenção, pois faremos alter-
ações delicadas no game engine. Procure sempre fazer backups de todos os
arquivos.

Problema na exclusão de elementos
     Antes de criar o método excluirSprite nas classes Animacao e
Colisor, preciso contar-lhe uma coisa. Quando estava desenvolvendo o
protótipo de jogo para este livro, ao implementar a exclusão de itens dos ar-
rays, eu inocentemente mandei excluir o elemento tão logo que ele saía da
tela:
✴✴ ❊①❡♠♣❧♦ t❡ór✐❝♦

146


[PAGINA 154]
Casa do Código                                       Capítulo 7. Criando inimigos



✴✴ ◆ã♦ ❢❛ç❛ ✐st♦✦

❛t✉❛❧✐③❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✴✴ ❙♣r✐t❡ s✉♠✐✉ ❞❛ t❡❧❛
   ✐❢ ✭t❤✐s✳② ❃ t❤✐s✳❝♦♥t❡①t✳❝❛♥✈❛s✳❤❡✐❣❤t✮ ④
      t❤✐s✳❛♥✐♠❛❝❛♦✳❡①❝❧✉✐r❙♣r✐t❡✭t❤✐s✮❀
      t❤✐s✳❝♦❧✐s♦r✳❡①❝❧✉✐r❙♣r✐t❡✭t❤✐s✮❀
   ⑥
⑥

    É um código simples e claro, mas que provocou um bug que levei horas
para descobrir o que era. Normalmente eu tenho deixado os bugs aparecerem
para discutir a solução no próprio caminhar do livro, mas desta vez não vou
fazer isso com você. Vou poupá-lo deste aqui.
    A explicação é que estamos excluindo elementos de um array dentro do
loop que percorre esse array! Mas onde está esse loop? Na classe Animacao,
método proximoFrame, temos vários loops que chamam os métodos
atualizar, desenhar e o processar do colisor, sendo que este faz outro
loop em seu array!

✴✴ ❚r❡❝❤♦ ❞♦ ♠ét♦❞♦ ♣r♦①✐♠♦❋r❛♠❡ ❞❛ ❝❧❛ss❡ ❆♥✐♠❛❝❛♦

✴✴ ❆t✉❛❧✐③❛♠♦s ♦ ❡st❛❞♦ ❞♦s s♣r✐t❡s
❢♦r ✭✈❛r ✐ ✐♥ t❤✐s✳s♣r✐t❡s✮
   t❤✐s✳s♣r✐t❡s❬✐❪✳❛t✉❛❧✐③❛r✭✮❀

✴✴ ❉❡s❡♥❤❛♠♦s ♦s s♣r✐t❡s
❢♦r ✭✈❛r ✐ ✐♥ t❤✐s✳s♣r✐t❡s✮
   t❤✐s✳s♣r✐t❡s❬✐❪✳❞❡s❡♥❤❛r✭✮❀

✴✴ Pr♦❝❡ss❛♠❡♥t♦s ❣❡r❛✐s
❢♦r ✭✈❛r ✐ ✐♥ t❤✐s✳♣r♦❝❡ss❛♠❡♥t♦s✮
   t❤✐s✳♣r♦❝❡ss❛♠❡♥t♦s❬✐❪✳♣r♦❝❡ss❛r✭✮❀

    Se, por exemplo, eu mando excluir um item de dentro do método
atualizar, o loop que chama o atualizar ficará órfão daquele item!
Como regra geral, você não deve excluir itens de um array dentro do loop
que o percorre:

                                                                            147


[PAGINA 155]
7.5. Estamos experimentando lentidão!                          Casa do Código


✴✴ ❊①❡♠♣❧♦ t❡ór✐❝♦
✴✴ ❱♦❝ê ♥ã♦ ❞❡✈❡ ❢❛③❡r ✐st♦

✴✴ ❈r✐❛r ✉♠ ❛rr❛②
✈❛r ♠❡✉❆rr❛② ❂ ❬✬❜❛♥❛♥❛✬✱ ✬❧❛r❛♥❥❛✬✱ ✬❧✐♠ã♦✬❪❀

✴✴ ❋❛③❡r ✉♠ ❧♦♦♣
❢♦r ✭✈❛r ✐ ✐♥ ♠❡✉❆rr❛②✮ ④
   ✴✴ ❋♦rç❛r ✉♠❛ ❡①❝❧✉sã♦ ❞❡♥tr♦ ❞♦ ❧♦♦♣
   ✐❢ ✭♠❡✉❆rr❛②❬✐❪ ❂❂ ✬❧❛r❛♥❥❛✬✮
      ❡①❝❧✉✐r❊❧❡♠❡♥t♦✭♠❡✉❆rr❛②❬✐❪✱ ♠❡✉❆rr❛②✮❀

      ✴✴ ❋❛③❡r ❛❧❣✉♠❛ t❛r❡❢❛ ❝♦♠ ♦ ❛rr❛②
      ❞♦❝✉♠❡♥t✳✇r✐t❡✭♠❡✉❆rr❛②❬✐❪ ✰ ✬❁❜r❃✬✮❀
⑥

    A solução? Manter uma lista de objetos a excluir, e excluí-los somente ao
fim do ciclo de animação!

Excluindo elementos dos arrays
    Vamos então implementar a exclusão de elementos com bastante calma.
Desta forma, eliminamos o problema da lentidão e poderemos, enfim, tratar
as colisões, fazendo o inimigo e o tiro sumirem quando se chocarem, por
exemplo.
    Temos que iniciar as listas de elementos a serem excluídos. No construtor
da classe Colisor, faça:
t❤✐s✳s♣r✐t❡s❊①❝❧✉✐r ❂ ❬❪❀

      Para a classe Animacao, há dois arrays:
t❤✐s✳s♣r✐t❡s❊①❝❧✉✐r ❂ ❬❪❀
t❤✐s✳♣r♦❝❡ss❛♠❡♥t♦s❊①❝❧✉✐r ❂ ❬❪❀

   O método excluirSprite apenas incluirá o sprite nessa lista. No
Colisor, temos:

❡①❝❧✉✐r❙♣r✐t❡✿ ❢✉♥❝t✐♦♥✭s♣r✐t❡✮ ④
   t❤✐s✳s♣r✐t❡s❊①❝❧✉✐r✳♣✉s❤✭s♣r✐t❡✮❀
⑥

148


[PAGINA 156]
Casa do Código                                           Capítulo 7. Criando inimigos



     Na   Animacao,   temos            que     ter      excluirSprite              e
excluirProcessamento:

❡①❝❧✉✐r❙♣r✐t❡✿ ❢✉♥❝t✐♦♥✭s♣r✐t❡✮ ④
   t❤✐s✳s♣r✐t❡s❊①❝❧✉✐r✳♣✉s❤✭s♣r✐t❡✮❀
⑥✱
❡①❝❧✉✐rPr♦❝❡ss❛♠❡♥t♦✿ ❢✉♥❝t✐♦♥✭♣r♦❝❡ss❛♠❡♥t♦✮ ④
   t❤✐s✳♣r♦❝❡ss❛♠❡♥t♦s❊①❝❧✉✐r✳♣✉s❤✭♣r♦❝❡ss❛♠❡♥t♦✮❀
⑥

   No fim do método processar do Colisor, colocamos uma chamada
a processarExclusoes:

♣r♦❝❡ss❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✴✴ ✳✳✳

     t❤✐s✳♣r♦❝❡ss❛r❊①❝❧✉s♦❡s✭✮❀
⑥✱

     E vamos criar esse método processarExclusoes. Como pode haver
vários sprites a serem eliminados, vamos na verdade montar um novo array
contendo todos os elementos, menos aqueles que foram excluídos. O array
antigo poderá ser descartado e ficará livre para o coletor de lixo (garbage col-
lector) do JavaScript apagá-lo da memória:

♣r♦❝❡ss❛r❊①❝❧✉s♦❡s✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✴✴ ❈r✐❛r ✉♠ ♥♦✈♦ ❛rr❛②
   ✈❛r ♥♦✈♦❆rr❛② ❂ ❬❪❀

     ✴✴ ❆❞✐❝✐♦♥❛r s♦♠❡♥t❡ ♦s ❡❧❡♠❡♥t♦s ♥ã♦ ❡①❝❧✉í❞♦s
     ❢♦r ✭✈❛r ✐ ✐♥ t❤✐s✳s♣r✐t❡s✮ ④
        ✐❢ ✭t❤✐s✳s♣r✐t❡s❊①❝❧✉✐r✳✐♥❞❡①❖❢✭t❤✐s✳s♣r✐t❡s❬✐❪✮ ❂❂ ✲✶✮
           ♥♦✈♦❆rr❛②✳♣✉s❤✭t❤✐s✳s♣r✐t❡s❬✐❪✮❀
     ⑥

     ✴✴ ▲✐♠♣❛r ♦ ❛rr❛② ❞❡ ❡①❝❧✉sõ❡s
     t❤✐s✳s♣r✐t❡s❊①❝❧✉✐r ❂ ❬❪❀

     ✴✴ ❙✉❜st✐t✉✐r ♦ ❛rr❛② ✈❡❧❤♦ ♣❡❧♦ ♥♦✈♦

                                                                                149


[PAGINA 157]
7.5. Estamos experimentando lentidão!                      Casa do Código


      t❤✐s✳s♣r✐t❡s ❂ ♥♦✈♦❆rr❛②❀
⑥

   Para a Animacao, o procedimento é muito semelhante. No fim do
método proximoFrame, logo antes da chamada do próximo ciclo, chame
também o método processarExclusoes:

♣r♦①✐♠♦❋r❛♠❡✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✴✴ ✳✳✳

      ✴✴ Pr♦❝❡ss❛♠❡♥t♦ ❞❡ ❡①❝❧✉sõ❡s
      t❤✐s✳♣r♦❝❡ss❛r❊①❝❧✉s♦❡s✭✮❀

      ✴✴ ❈❤❛♠❛♠♦s ♦ ♣ró①✐♠♦ ❝✐❝❧♦
      ✈❛r ❛♥✐♠❛❝❛♦ ❂ t❤✐s❀
      r❡q✉❡st❆♥✐♠❛t✐♦♥❋r❛♠❡✭❢✉♥❝t✐♦♥✭✮ ④
         ❛♥✐♠❛❝❛♦✳♣r♦①✐♠♦❋r❛♠❡✭✮❀
      ⑥✮❀
⑥✱

    E vamos criar esse método. Ele segue o mesmo algoritmo de seu equiva-
lente no Colisor, só é um pouco maior porque estamos lidando com dois
arrays.

♣r♦❝❡ss❛r❊①❝❧✉s♦❡s✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✴✴ ❈r✐❛r ♥♦✈♦s ❛rr❛②s
   ✈❛r ♥♦✈♦❙♣r✐t❡s ❂ ❬❪❀
   ✈❛r ♥♦✈♦Pr♦❝❡ss❛♠❡♥t♦s ❂ ❬❪❀

      ✴✴ ❆❞✐❝✐♦♥❛r s♦♠❡♥t❡ s❡ ♥ã♦ ❝♦♥st❛r ♥♦ ❛rr❛② ❞❡ ❡①❝❧✉í❞♦s
      ❢♦r ✭✈❛r ✐ ✐♥ t❤✐s✳s♣r✐t❡s✮ ④
         ✐❢ ✭t❤✐s✳s♣r✐t❡s❊①❝❧✉✐r✳✐♥❞❡①❖❢✭t❤✐s✳s♣r✐t❡s❬✐❪✮ ❂❂ ✲✶✮
            ♥♦✈♦❙♣r✐t❡s✳♣✉s❤✭t❤✐s✳s♣r✐t❡s❬✐❪✮❀
      ⑥

      ❢♦r ✭✈❛r ✐ ✐♥ t❤✐s✳♣r♦❝❡ss❛♠❡♥t♦s✮ ④
         ✐❢ ✭t❤✐s✳♣r♦❝❡ss❛♠❡♥t♦s❊①❝❧✉✐r✳✐♥❞❡①❖❢
             ✭t❤✐s✳♣r♦❝❡ss❛♠❡♥t♦s❬✐❪✮ ❂❂ ✲✶✮
            ♥♦✈♦Pr♦❝❡ss❛♠❡♥t♦s✳♣✉s❤✭t❤✐s✳♣r♦❝❡ss❛♠❡♥t♦s❬✐❪✮❀

150


[PAGINA 158]
Casa do Código                                       Capítulo 7. Criando inimigos



     ⑥

     ✴✴ ▲✐♠♣❛r ♦s ❛rr❛②s ❞❡ ❡①❝❧✉sõ❡s
     t❤✐s✳s♣r✐t❡s❊①❝❧✉✐r ❂ ❬❪❀
     t❤✐s✳♣r♦❝❡ss❛♠❡♥t♦s❊①❝❧✉✐r ❂ ❬❪❀

     ✴✴ ❙✉❜st✐t✉✐r ♦s ❛rr❛②s ✈❡❧❤♦s ♣❡❧♦s ♥♦✈♦s
     t❤✐s✳s♣r✐t❡s ❂ ♥♦✈♦❙♣r✐t❡s❀
     t❤✐s✳♣r♦❝❡ss❛♠❡♥t♦s ❂ ♥♦✈♦Pr♦❝❡ss❛♠❡♥t♦s❀
⑥

    A exclusão está implementada! Esta parte foi fogo, não foi? Mas agora
podemos facilmente mandar excluir objetos que estão sobrando na memória,
para que eles não provoquem mais lentidão!


7.6      Excluindo os objetos desnecessários
Vamos começar pelo Tiro. Quando sumir da tela, ele deve ser excluído. Em
seu método atualizar, verificamos sua posição y e o tiramos da animação
e do colisor quando sua posição for negativa (excedendo a borda do Canvas):

❛t✉❛❧✐③❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   t❤✐s✳② ✲❂ t❤✐s✳✈❡❧♦❝✐❞❛❞❡❀

     ✴✴ ❊①❝❧✉✐r ♦ t✐r♦ q✉❛♥❞♦ s✉♠✐r ❞❛ t❡❧❛
     ✐❢ ✭t❤✐s✳② ❁ ✲t❤✐s✳❛❧t✉r❛✮ ④
        t❤✐s✳❛♥✐♠❛❝❛♦✳❡①❝❧✉✐r❙♣r✐t❡✭t❤✐s✮❀
        t❤✐s✳❝♦❧✐s♦r✳❡①❝❧✉✐r❙♣r✐t❡✭t❤✐s✮❀
     ⑥
⑥✱

    O Ovni também deve ser excluído, mas como seu movimento é em sen-
tido contrário, ele deve passar da altura do Canvas:

❛t✉❛❧✐③❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   t❤✐s✳② ✰❂ t❤✐s✳✈❡❧♦❝✐❞❛❞❡❀

     ✐❢ ✭t❤✐s✳② ❃ t❤✐s✳❝♦♥t❡①t✳❝❛♥✈❛s✳❤❡✐❣❤t✮ ④
        t❤✐s✳❛♥✐♠❛❝❛♦✳❡①❝❧✉✐r❙♣r✐t❡✭t❤✐s✮❀

                                                                             151


[PAGINA 159]
7.6. Excluindo os objetos desnecessários                         Casa do Código


          t❤✐s✳❝♦❧✐s♦r✳❡①❝❧✉✐r❙♣r✐t❡✭t❤✐s✮❀
      ⑥
⑥✱

    Também, tanto o Tiro quanto o Ovni devem ser excluídos em caso de
colisão entre eles. Afinal, esta é uma regra de negócio óbvia de nosso jogo!
Podemos implementar isto no método colidiuCom de qualquer uma destas
classes. Escolhi a classe Ovni, conferindo se o outro objeto é um Tiro:
❝♦❧✐❞✐✉❈♦♠✿ ❢✉♥❝t✐♦♥✭♦✉tr♦✮ ④
   ✴✴ ❙❡ ❝♦❧✐❞✐✉ ❝♦♠ ✉♠ ❚✐r♦✱ ♦s ❞♦✐s ❞❡s❛♣❛r❡❝❡♠
   ✐❢ ✭♦✉tr♦ ✐♥st❛♥❝❡♦❢ ❚✐r♦✮ ④
      t❤✐s✳❛♥✐♠❛❝❛♦✳❡①❝❧✉✐r❙♣r✐t❡✭t❤✐s✮❀
      t❤✐s✳❝♦❧✐s♦r✳❡①❝❧✉✐r❙♣r✐t❡✭t❤✐s✮❀
      t❤✐s✳❛♥✐♠❛❝❛♦✳❡①❝❧✉✐r❙♣r✐t❡✭♦✉tr♦✮❀
      t❤✐s✳❝♦❧✐s♦r✳❡①❝❧✉✐r❙♣r✐t❡✭♦✉tr♦✮❀
   ⑥
⑥

   Por último, a colisão entre a Nave e o Ovni. Nosso herói, que era in-
vencível, agora pode morrer! Programe na classe Nave:
❝♦❧✐❞✐✉❈♦♠✿ ❢✉♥❝t✐♦♥✭♦✉tr♦✮ ④
   ✴✴ ❙❡ ❝♦❧✐❞✐✉ ❝♦♠ ✉♠ ❖✈♥✐✳✳✳
   ✐❢ ✭♦✉tr♦ ✐♥st❛♥❝❡♦❢ ❖✈♥✐✮ ④
      ✴✴ ❋✐♠ ❞❡ ❥♦❣♦✦
      t❤✐s✳❛♥✐♠❛❝❛♦✳❞❡s❧✐❣❛r✭✮❀
      ❛❧❡rt✭✬●❆▼❊ ❖❱❊❘✬✮❀
   ⑥
⑥

    Este é um momento para se comemorar! Se você fez todas as tarefas até
aqui com calma e atenção, você tem agora um game engine maduro para uso
e um exemplo de jogo totalmente funcional, embora ainda não esteja pronto.
    Experimente jogar. Já é possível destruir os inimigos e ser atingido por
eles. No próximo capítulo, realizaremos este e outros diversos ajustes que
deixarão nosso jogo com aspecto profisisonal.
    Exercício: tente fazer a nave sofrer 3 colisões antes de ser destruída. Para
isso, basta criar um atributo (sugestões de nome: energia, pontosVida)

152


[PAGINA 160]
Casa do Código                                      Capítulo 7. Criando inimigos



e ir decrementando seu valor a cada colisão. Quando chegar a zero... GAME
OVER!




                                                                            153


[PAGINA 161]


[PAGINA 162]
Capítulo 8

Incorpore animações, sons,
pausa e vidas extras ao jogo
Uma boa notícia: neste capítulo, nosso jogo de nave será concluído! Já temos
um protótipo totalmente funcional, mas ainda há muito o que ser melhorado
para dar-lhe um aspecto profissional. Serão feitas as seguintes melhorias:

    • Organização do código: nosso jogo está crescendo e, por isso, a
      página inicial vai começar a ficar um pouco longa e desorganizada.
      Faremos algumas refatorações para acomodar mais facilmente as mu-
      danças que estão por vir.

    • Animação cronometrada: para a animação correr a velocidades con-
      stantes, e não no ritmo da CPU (do jeito que está, a velocidade da ani-
      mação poderá oscilar muito).


[PAGINA 163]
8.1. Organizando o código                                      Casa do Código


      • Uso de spritesheets: nós aprendemos como usá-las no capítulo 4, mas
        não aplicamos ainda em nosso jogo! Com elas, criaremos explosões
        e daremos animação à nave, deixando nosso jogo muito mais interes-
        sante.

      • Pausa: como seria a experiência de jogar um jogo sem poder pausá-lo?
        Péssima, não é mesmo?

      • Som e música de fundo: você não estava sentindo a falta disto, não?

      • Telas de loading e Game Over: um jogo utiliza muitas imagens.
        Quando você hospedá-lo na internet, não vai querer que o usuário veja
        uma tela parada enquanto as imagens carregam, não é verdade? Um
        aviso “Carregando...” e uma barrinha aumentando na tela farão com
        que o internauta não desista do seu jogo; ao contrário, aumentará sua
        expectativa! E uma tela que indica quando o jogo acabou, cairá muito
        bem.

      • Vidas extras: por que o jogo tem que acabar na primeira colisão da
        nave? Vamos dar mais chances ao jogador!

      • Pontuação (score): esta simples regra de negócio será bem fácil de
        implementar.

   Primeiro, vamos organizar todo o nosso trabalho. Será uma excelente
oportunidade de revisão. Mãos à obra!


8.1     Organizando o código
No capítulo anterior, o código da página HTML de nosso jogo ficou um
tanto extenso, pois juntamos quase tudo o que aprendemos em um único ar-
quivo funcional. Considero esta uma boa hora para refatorar esse código (e
praticar um pouco também), deixando-o um pouco mais organizado e fácil
para acrescentar as melhorias que estão por vir.
    Crie uma nova página HTML. Os arquivos de script devem ser copiados
de suas versões mais atualizadas.


156


[PAGINA 164]
Casa do Código            Capítulo 8. Incorpore animações, sons, pausa e vidas extras ao jogo



❁✦✲✲ ❛rq✉✐✈♦✿ ❥♦❣♦✲❞❡❢✐♥✐t✐✈♦✳❤t♠❧ ✲✲❃
❁✦❉❖❈❚❨P❊ ❤t♠❧❃
❁❤t♠❧❃

❁❤❡❛❞❃
   ❁t✐t❧❡❃❏♦❣♦ ❞❡ ◆❛✈❡❁✴t✐t❧❡❃
   ❁s❝r✐♣t sr❝❂✧❛♥✐♠❛❝❛♦✳❥s✧❃❁✴s❝r✐♣t❃
   ❁s❝r✐♣t sr❝❂✧t❡❝❧❛❞♦✳❥s✧❃❁✴s❝r✐♣t❃
   ❁s❝r✐♣t sr❝❂✧❝♦❧✐s♦r✳❥s✧❃❁✴s❝r✐♣t❃
   ❁s❝r✐♣t sr❝❂✧❢✉♥❞♦✳❥s✧❃❁✴s❝r✐♣t❃
   ❁s❝r✐♣t sr❝❂✧♥❛✈❡✳❥s✧❃❁✴s❝r✐♣t❃
   ❁s❝r✐♣t sr❝❂✧♦✈♥✐✳❥s✧❃❁✴s❝r✐♣t❃
   ❁s❝r✐♣t sr❝❂✧t✐r♦✳❥s✧❃❁✴s❝r✐♣t❃
❁✴❤❡❛❞❃

❁❜♦❞②❃
   ❁❝❛♥✈❛s ✐❞❂✧❝❛♥✈❛s❴❛♥✐♠❛❝❛♦✧ ✇✐❞t❤❂✧✺✵✵✧ ❤❡✐❣❤t❂✧✺✵✵✧❃
   ❁✴❝❛♥✈❛s❃
   ❁s❝r✐♣t❃
      ✴✴ ❱❛♠♦s ♦r❣❛♥✐③❛r ✉♠ ♣♦✉❝♦ ❡st❡ ❛♣❧✐❝❛t✐✈♦✦
   ❁✴s❝r✐♣t❃
❁✴❜♦❞②❃

❁✴❤t♠❧❃

    Vamos continuar executando as tarefas nesta ordem: carregar as imagens,
iniciar os objetos, iniciar a animação. Que tal criar funções separadas? No
JavaScript, faça:

✴✴ ❈❛♥✈❛s ❡ ❈♦♥t❡①t
✈❛r ❝❛♥✈❛s ❂ ❞♦❝✉♠❡♥t✳❣❡t❊❧❡♠❡♥t❇②■❞✭✬❝❛♥✈❛s❴❛♥✐♠❛❝❛♦✬✮❀
✈❛r ❝♦♥t❡①t ❂ ❝❛♥✈❛s✳❣❡t❈♦♥t❡①t✭✬✷❞✬✮❀

✴✴ ❱❛r✐á✈❡✐s ♣r✐♥❝✐♣❛✐s
✈❛r ✐♠❛❣❡♥s✱ ❛♥✐♠❛❝❛♦✱ t❡❝❧❛❞♦✱ ❝♦❧✐s♦r✱
      ♥❛✈❡✱ ❝r✐❛❞♦r■♥✐♠✐❣♦s❀
✈❛r t♦t❛❧■♠❛❣❡♥s ❂ ✵✱ ❝❛rr❡❣❛❞❛s ❂ ✵❀

✴✴ ❈♦♠❡ç❛ ❝❛rr❡❣❛♥❞♦ ❛s ✐♠❛❣❡♥s

                                                                                        157


[PAGINA 165]
8.1. Organizando o código                                      Casa do Código


❝❛rr❡❣❛r■♠❛❣❡♥s✭✮❀

    Na função carregarImagens, facilita muito carregar um objeto ou ar-
ray com os nomes das imagens e fazer um loop nele. Optei por usar um ob-
jeto, pois assim posso associar cada imagem a seu nome (em vez de usar um
número sem significado). Após carregar cada imagem, o nome é substituído
pelo objeto da imagem:

❢✉♥❝t✐♦♥ ❝❛rr❡❣❛r■♠❛❣❡♥s✭✮ ④
   ✴✴ ❖❜❥❡t♦ ❝♦♥t❡♥❞♦ ♦s ♥♦♠❡s ❞❛s ✐♠❛❣❡♥s
   ✐♠❛❣❡♥s ❂ ④
      ❡s♣❛❝♦✿ ✬❢✉♥❞♦✲❡s♣❛❝♦✳♣♥❣✬✱
      ❡str❡❧❛s✿ ✬❢✉♥❞♦✲❡str❡❧❛s✳♣♥❣✬✱
      ♥✉✈❡♥s✿ ✬❢✉♥❞♦✲♥✉✈❡♥s✳♣♥❣✬✱
      ♥❛✈❡✿     ✬♥❛✈❡✳♣♥❣✬✱
      ♦✈♥✐✿     ✬♦✈♥✐✳♣♥❣✬
   ⑥❀

      ✴✴ ❈❛rr❡❣❛r t♦❞❛s
      ❢♦r ✭✈❛r ✐ ✐♥ ✐♠❛❣❡♥s✮ ④
         ✈❛r ✐♠❣ ❂ ♥❡✇ ■♠❛❣❡✭✮❀
         ✐♠❣✳sr❝ ❂ ✬✐♠❣✴✬ ✰ ✐♠❛❣❡♥s❬✐❪❀
         ✐♠❣✳♦♥❧♦❛❞ ❂ ❝❛rr❡❣❛♥❞♦❀
         t♦t❛❧■♠❛❣❡♥s✰✰❀

          ✴✴ ❙✉❜st✐t✉✐r ♦ ♥♦♠❡ ♣❡❧❛ ✐♠❛❣❡♠
          ✐♠❛❣❡♥s❬✐❪ ❂ ✐♠❣❀
      ⑥
⑥

    Temos então que criar a já conhecida função carregando, que vai moni-
torar o carregamento das imagens e iniciar a criação dos objetos quando todas
estiverem prontas:

❢✉♥❝t✐♦♥ ❝❛rr❡❣❛♥❞♦✭✮ ④
   ❝❛rr❡❣❛❞❛s✰✰❀
   ✐❢ ✭❝❛rr❡❣❛❞❛s ❂❂ t♦t❛❧■♠❛❣❡♥s✮ ✐♥✐❝✐❛r❖❜❥❡t♦s✭✮❀
⑥


158


[PAGINA 166]
Casa do Código           Capítulo 8. Incorpore animações, sons, pausa e vidas extras ao jogo



   A função iniciarObjetos iniciará os principais objetos do jogo, da
forma como você já está acostumado a fazer:

❢✉♥❝t✐♦♥ ✐♥✐❝✐❛r❖❜❥❡t♦s✭✮ ④
   ✴✴ ❖❜❥❡t♦s ♣r✐♥❝✐♣❛✐s
   ❛♥✐♠❛❝❛♦ ❂ ♥❡✇ ❆♥✐♠❛❝❛♦✭❝♦♥t❡①t✮❀
   t❡❝❧❛❞♦ ❂ ♥❡✇ ❚❡❝❧❛❞♦✭❞♦❝✉♠❡♥t✮❀
   ❝♦❧✐s♦r ❂ ♥❡✇ ❈♦❧✐s♦r✭✮❀
   ❡s♣❛❝♦ ❂ ♥❡✇ ❋✉♥❞♦✭❝♦♥t❡①t✱ ✐♠❛❣❡♥s✳❡s♣❛❝♦✮❀
   ❡str❡❧❛s ❂ ♥❡✇ ❋✉♥❞♦✭❝♦♥t❡①t✱ ✐♠❛❣❡♥s✳❡str❡❧❛s✮❀
   ♥✉✈❡♥s ❂ ♥❡✇ ❋✉♥❞♦✭❝♦♥t❡①t✱ ✐♠❛❣❡♥s✳♥✉✈❡♥s✮❀
   ♥❛✈❡ ❂ ♥❡✇ ◆❛✈❡✭❝♦♥t❡①t✱ t❡❝❧❛❞♦✱ ✐♠❛❣❡♥s✳♥❛✈❡✮❀

    ✴✴ ▲✐❣❛çõ❡s ❡♥tr❡ ♦❜❥❡t♦s
    ❛♥✐♠❛❝❛♦✳♥♦✈♦❙♣r✐t❡✭❡s♣❛❝♦✮❀
    ❛♥✐♠❛❝❛♦✳♥♦✈♦❙♣r✐t❡✭❡str❡❧❛s✮❀
    ❛♥✐♠❛❝❛♦✳♥♦✈♦❙♣r✐t❡✭♥✉✈❡♥s✮❀
    ❛♥✐♠❛❝❛♦✳♥♦✈♦❙♣r✐t❡✭♥❛✈❡✮❀

    ❝♦❧✐s♦r✳♥♦✈♦❙♣r✐t❡✭♥❛✈❡✮❀
    ❛♥✐♠❛❝❛♦✳♥♦✈♦Pr♦❝❡ss❛♠❡♥t♦✭❝♦❧✐s♦r✮❀

    ❝♦♥❢✐❣✉r❛❝♦❡s■♥✐❝✐❛✐s✭✮❀
⑥

    Foi chamada a função configuracoesIniciais, que configura as
velocidades dos fundos, posiciona a nave, configura o disparo pela tecla
Espaço e inicia a animação:

❢✉♥❝t✐♦♥ ❝♦♥❢✐❣✉r❛❝♦❡s■♥✐❝✐❛✐s✭✮ ④
   ✴✴ ❋✉♥❞♦s
   ❡s♣❛❝♦✳✈❡❧♦❝✐❞❛❞❡ ❂ ✸❀
   ❡str❡❧❛s✳✈❡❧♦❝✐❞❛❞❡ ❂ ✺❀
   ♥✉✈❡♥s✳✈❡❧♦❝✐❞❛❞❡ ❂ ✶✵❀

    ✴✴ ◆❛✈❡
    ♥❛✈❡✳① ❂ ❝❛♥✈❛s✳✇✐❞t❤ ✴ ✷ ✲ ✐♠❛❣❡♥s✳♥❛✈❡✳✇✐❞t❤ ✴ ✷❀
    ♥❛✈❡✳② ❂ ❝❛♥✈❛s✳❤❡✐❣❤t ✲ ✐♠❛❣❡♥s✳♥❛✈❡✳❤❡✐❣❤t❀
    ♥❛✈❡✳✈❡❧♦❝✐❞❛❞❡ ❂ ✺❀


                                                                                       159


[PAGINA 167]
8.1. Organizando o código                                         Casa do Código




      ✴✴ ❚✐r♦
      t❡❝❧❛❞♦✳❞✐s♣❛r♦✉✭❊❙P❆❈❖✱ ❢✉♥❝t✐♦♥✭✮ ④
         ♥❛✈❡✳❛t✐r❛r✭✮❀
      ⑥✮❀

      ❛♥✐♠❛❝❛♦✳❧✐❣❛r✭✮❀
⑥

    Faça o teste: neste ponto você já deve ter a nave controlável e atirando, e o
fundo rolando. Vamos agora configurar a criação dos inimigos como um pro-
cessamento da animação. Ao final da função configuracoesIniciais,
acrescente a chamada a criacaoInimigos:
❢✉♥❝t✐♦♥ ❝♦♥❢✐❣✉r❛❝♦❡s■♥✐❝✐❛✐s✭✮ ④
   ✴✴ ✳✳✳

      ❝r✐❛❝❛♦■♥✐♠✐❣♦s✭✮❀
⑥

   E vamos criar essa função. Ela cria um objeto sem construtor, com o
método processar, e o insere como um processamento geral na animação:
❢✉♥❝t✐♦♥ ❝r✐❛❝❛♦■♥✐♠✐❣♦s✭✮ ④
   ❝r✐❛❞♦r■♥✐♠✐❣♦s ❂ ④
      ♣r♦❝❡ss❛r✿ ❢✉♥❝t✐♦♥✭✮ ④

           ⑥
      ⑥❀

      ❛♥✐♠❛❝❛♦✳♥♦✈♦Pr♦❝❡ss❛♠❡♥t♦✭❝r✐❛❞♦r■♥✐♠✐❣♦s✮❀
⑥

    No método processar desse objeto, criaremos um inimigo a cada se-
gundo. Mas, para isso, necessitamos saber o instante em que o último inimigo
foi gerado. Este instante é guardado no atributo ultimoOvni e atualizado
quando o tempo decorrido ultrapassar 1000 milissegundos:
❢✉♥❝t✐♦♥ ❝r✐❛❝❛♦■♥✐♠✐❣♦s✭✮ ④
   ✈❛r ❝r✐❛❞♦r ❂ ④

160


[PAGINA 168]
Casa do Código            Capítulo 8. Incorpore animações, sons, pausa e vidas extras ao jogo



         ✉❧t✐♠♦❖✈♥✐✿ ♥❡✇ ❉❛t❡✭✮✳❣❡t❚✐♠❡✭✮✱

         ♣r♦❝❡ss❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
            ✈❛r ❛❣♦r❛ ❂ ♥❡✇ ❉❛t❡✭✮✳❣❡t❚✐♠❡✭✮❀
            ✈❛r ❞❡❝♦rr✐❞♦ ❂ ❛❣♦r❛ ✲ t❤✐s✳✉❧t✐♠♦❖✈♥✐❀

             ✐❢ ✭❞❡❝♦rr✐❞♦ ❃ ✶✵✵✵✮ ④
                ♥♦✈♦❖✈♥✐✭✮❀
                t❤✐s✳✉❧t✐♠♦❖✈♥✐ ❂ ❛❣♦r❛❀
             ⑥
         ⑥
    ⑥❀

    ❛♥✐♠❛❝❛♦✳♥♦✈♦Pr♦❝❡ss❛♠❡♥t♦✭❝r✐❛❞♦r✮❀
⑥

    Se passar um segundo desde a geração do último inimigo, é chamada a
função novoOvni, que é muito semelhante à do capítulo anterior. Ela gera
inimigos em posições e com velocidades aleatórias. Se não lembra como fazer
isso, consulte o tópico 7.1.

❢✉♥❝t✐♦♥ ♥♦✈♦❖✈♥✐✭✮ ④
   ✈❛r ✐♠❣❖✈♥✐ ❂ ✐♠❛❣❡♥s✳♦✈♥✐❀
   ✈❛r ♦✈♥✐ ❂ ♥❡✇ ❖✈♥✐✭❝♦♥t❡①t✱ ✐♠❣❖✈♥✐✮❀

    ✴✴ ▼í♥✐♠♦✿ ✺❀ ♠á①✐♠♦✿ ✷✵
    ♦✈♥✐✳✈❡❧♦❝✐❞❛❞❡ ❂
       ▼❛t❤✳❢❧♦♦r✭ ✺ ✰ ▼❛t❤✳r❛♥❞♦♠✭✮ ✯ ✭✷✵ ✲ ✺ ✰ ✶✮ ✮❀

    ✴✴ ▼í♥✐♠♦✿ ✵❀
    ✴✴ ♠á①✐♠♦✿ ❧❛r❣✉r❛ ❞♦ ❝❛♥✈❛s ✲ ❧❛r❣✉r❛ ❞♦ ♦✈♥✐
    ♦✈♥✐✳① ❂
       ▼❛t❤✳❢❧♦♦r✭▼❛t❤✳r❛♥❞♦♠✭✮ ✯
                  ✭❝❛♥✈❛s✳✇✐❞t❤ ✲ ✐♠❣❖✈♥✐✳✇✐❞t❤ ✰ ✶✮ ✮❀

    ✴✴ ❉❡s❝♦♥t❛r ❛ ❛❧t✉r❛
    ♦✈♥✐✳② ❂ ✲✐♠❣❖✈♥✐✳❤❡✐❣❤t❀

    ❛♥✐♠❛❝❛♦✳♥♦✈♦❙♣r✐t❡✭♦✈♥✐✮❀

                                                                                         161


[PAGINA 169]
8.2. Animação cronometrada                                     Casa do Código


      ❝♦❧✐s♦r✳♥♦✈♦❙♣r✐t❡✭♦✈♥✐✮❀
⑥

    Agora estamos muito mais organizados, com cada etapa da inicialização
do jogo em uma função específica. Estamos prontos para implementar as
novidades.


8.2 Animação cronometrada
Para dar um aspecto mais profissional a nosso jogo, devemos cronometrar
as animações. Você pode ter notado que, às vezes, a velocidade oscila. Isto é
comum em browsers e jogos que rodam em sistemas operacionais multitarefa:
a CPU pode estar ocupada enquanto o jogo espera o momento de processar
o próximo ciclo.
    Para resolver isso, precisamos primeiro saber o tempo decorrido entre
um ciclo e outro. No construtor da classe Animacao, crie os atributos
ultimoCiclo (para guardar o instante do ciclo anterior, lido do relógio) e
decorrido (para guardar o tempo decorrido entre o ciclo anterior e o atual):

❢✉♥❝t✐♦♥ ❆♥✐♠❛❝❛♦✭❝♦♥t❡①t✮ ④
   ✴✴ ✳✳✳
   t❤✐s✳✉❧t✐♠♦❈✐❝❧♦ ❂ ✵❀
   t❤✐s✳❞❡❝♦rr✐❞♦ ❂ ✵❀
⑥

    Para fazer os cálculos, obtemos o instante atual do relógio do computador
(dado por Date.getTime() em milissegundos) e calculamos a diferença
entre esse instante e o instante do ciclo anterior. Faremos isso no método
proximoFrame, logo antes de processar os sprites:

♣r♦①✐♠♦❋r❛♠❡✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✴✴ P♦ss♦ ❝♦♥t✐♥✉❛r❄
   ✐❢ ✭ ✦ t❤✐s✳❧✐❣❛❞♦ ✮ r❡t✉r♥❀

      ✈❛r ❛❣♦r❛ ❂ ♥❡✇ ❉❛t❡✭✮✳❣❡t❚✐♠❡✭✮❀
      ✐❢ ✭t❤✐s✳✉❧t✐♠♦❈✐❝❧♦ ❂❂ ✵✮ t❤✐s✳✉❧t✐♠♦❈✐❝❧♦ ❂ ❛❣♦r❛❀
      t❤✐s✳❞❡❝♦rr✐❞♦ ❂ ❛❣♦r❛ ✲ t❤✐s✳✉❧t✐♠♦❈✐❝❧♦❀


162


[PAGINA 170]
Casa do Código            Capítulo 8. Incorpore animações, sons, pausa e vidas extras ao jogo




     ✴✴ ✳✳✳
⑥

   No fim do método proximoFrame, atualize o atributo ultimoCiclo,
imediatamente antes de chamar o próximo ciclo:

♣r♦①✐♠♦❋r❛♠❡✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✴✴ ✳✳✳

     ✴✴ ❆t✉❛❧✐③❛r ♦ ✐♥st❛♥t❡ ❞♦ ú❧t✐♠♦ ❝✐❝❧♦
     t❤✐s✳✉❧t✐♠♦❈✐❝❧♦ ❂ ❛❣♦r❛❀

     ✴✴ ❈❤❛♠❛♠♦s ♦ ♣ró①✐♠♦ ❝✐❝❧♦
     ✈❛r ❛♥✐♠❛❝❛♦ ❂ t❤✐s❀
     r❡q✉❡st❆♥✐♠❛t✐♦♥❋r❛♠❡✭❢✉♥❝t✐♦♥✭✮ ④
        ❛♥✐♠❛❝❛♦✳♣r♦①✐♠♦❋r❛♠❡✭✮❀
     ⑥✮❀
⑥✱

    Agora os sprites sabem quanto tempo levou entre um ciclo e outro! Vamos
fazer o Fundo mover-se a uma velocidade constante. Para isso, modifique o
método atualizar:

❛t✉❛❧✐③❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✴✴ ❆t✉❛❧✐③❛r ❛ ♣♦s✐çã♦ ❞❡ ❡♠❡♥❞❛
   t❤✐s✳♣♦s✐❝❛♦❊♠❡♥❞❛ ✰❂
      t❤✐s✳✈❡❧♦❝✐❞❛❞❡ ✯ t❤✐s✳❛♥✐♠❛❝❛♦✳❞❡❝♦rr✐❞♦ ✴ ✶✵✵✵❀

     ✴✴ ✳✳✳
⑥✱




                                                                                        163


[PAGINA 171]
8.2. Animação cronometrada                                     Casa do Código




    Fórmula para animação cronometrada

       O incremento da posição do sprite, em pixels, é dado pela fórmula:
       velocidade * tempoDecorrido / 1000
       Sendo:

        • velocidade em pixels por segundo;

        • tempoDecorrido em segundos (como o tempo dado por
          Date.getTime() é em milissegundos, dividimos esse valor por
          1000).



    Note que agora o fundo move-se em velocidade constante, porém
bem devagar, pois passamos a trabalhar com pixels por segundo.
Podemos ajustar novas velocidades com valores maiores na função
configuracoesIniciais da página HTML. Você pode fazer vários testes
e atribuir os valores que desejar, dependendo da sensação de velocidade
que quer passar. Como as nuvens estão mais próximas, dei a elas a maior
velocidade, mas nada impede que coloquemos as estrelas em primeiro plano,
por exemplo:

❢✉♥❝t✐♦♥ ❝♦♥❢✐❣✉r❛❝♦❡s■♥✐❝✐❛✐s✭✮ ④
   ✴✴ ❋✉♥❞♦s
   ❡s♣❛❝♦✳✈❡❧♦❝✐❞❛❞❡ ❂ ✻✵❀
   ❡str❡❧❛s✳✈❡❧♦❝✐❞❛❞❡ ❂ ✶✺✵❀
   ♥✉✈❡♥s✳✈❡❧♦❝✐❞❛❞❡ ❂ ✺✵✵❀

      ✴✴ ✳✳✳
⑥

   Vamos cronometrar também o movimento da Nave. Aplique a fórmula
em seu método atualizar:

❛t✉❛❧✐③❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✈❛r ✐♥❝r❡♠❡♥t♦ ❂

164


[PAGINA 172]
Casa do Código            Capítulo 8. Incorpore animações, sons, pausa e vidas extras ao jogo



        t❤✐s✳✈❡❧♦❝✐❞❛❞❡ ✯ t❤✐s✳❛♥✐♠❛❝❛♦✳❞❡❝♦rr✐❞♦ ✴ ✶✵✵✵❀

    ✴✴ ❯s❡ ❛ ✈❛r✐á✈❡❧ ✐♥❝r❡♠❡♥t♦ ❡♠ t♦❞❛s ❛s ♠✉❞❛♥ç❛s ❞❡ ① ❡ ②
    ✐❢ ✭t❤✐s✳t❡❝❧❛❞♦✳♣r❡ss✐♦♥❛❞❛✭❙❊❚❆❴❊❙◗❯❊❘❉❆✮ ✫✫ t❤✐s✳① ❃ ✵✮
       t❤✐s✳① ✲❂ ✐♥❝r❡♠❡♥t♦❀

    ✴✴ ✳✳✳
⑥

    Na página HTML, dei a ela a velocidade de 200 pixels por segundo:

✴✴ ◆❛✈❡
♥❛✈❡✳① ❂ ❝❛♥✈❛s✳✇✐❞t❤ ✴ ✷ ✲ ✐♠❛❣❡♥s✳♥❛✈❡✳✇✐❞t❤ ✴ ✷❀
♥❛✈❡✳② ❂ ❝❛♥✈❛s✳❤❡✐❣❤t ✲ ✐♠❛❣❡♥s✳♥❛✈❡✳❤❡✐❣❤t❀
♥❛✈❡✳✈❡❧♦❝✐❞❛❞❡ ❂ ✷✵✵❀

    Exercício: faça você mesmo o ajuste para o Ovni e o Tiro! Dê-lhes as
velocidades que desejar. A do Tiro é configurada no construtor, e as dos
Ovnis, no método novoOvni da página. Dica: no pacote de download, a
página já está com a solução implementada.


8.3 Animando a nave com spritesheets
No pacote de download do livro há o arquivo nave-spritesheet.png
(figura 8.1). Iremos usá-lo para melhorar o aspecto de nossa nave. Conven-
hamos, ela está muito parada... nem o fogo em sua cauda se mexe!




                                                                                        165


[PAGINA 173]
8.3. Animando a nave com spritesheets                            Casa do Código




                           Figura 8.1: Spritesheet para a nave


    No capítulo 4, definimos que as linhas da spritesheet representam difer-
entes estados do sprite. Aqui temos a nave parada, movendo-se para a es-
querda e movendo-se para a direita. Em uma linha, a animação ocorre
avançando as colunas. Em cada uma destas linhas, há duas colunas que ani-
mam o fogo na cauda.

Iniciando o teste
    Para começar a programar com spritesheets, primeiro acrescente a refer-
ência ao arquivo spritesheet.js, criado no capítulo 4:
❁s❝r✐♣t sr❝❂✧s♣r✐t❡s❤❡❡t✳❥s✧❃❁✴s❝r✐♣t❃

   Na função carregarImagens, mude a imagem da nave para o arquivo
nave-spritesheet.png:
✐♠❛❣❡♥s ❂ ④
   ✴✴ ✳✳✳
   ♥❛✈❡✿    ✬♥❛✈❡✲s♣r✐t❡s❤❡❡t✳♣♥❣✬✱
   ✴✴ ✳✳✳
⑥❀

    Agora não podemos mais usar as dimensões da imagem para posicionar
a nave. Em configuracoesIniciais, vamos passar valores absolutos ref-
erentes a cada quadro (considerando que cada nave tem 36x48 pixels):

166


[PAGINA 174]
Casa do Código             Capítulo 8. Incorpore animações, sons, pausa e vidas extras ao jogo



❢✉♥❝t✐♦♥ ❝♦♥❢✐❣✉r❛❝♦❡s■♥✐❝✐❛✐s✭✮ ④
   ✴✴ ✳✳✳

     ✴✴ ◆❛✈❡
     ♥❛✈❡✳① ❂ ❝❛♥✈❛s✳✇✐❞t❤ ✴ ✷ ✲ ✶✽❀             ✴✴ ✸✻ ✴ ✷
     ♥❛✈❡✳② ❂ ❝❛♥✈❛s✳❤❡✐❣❤t ✲ ✹✽❀
     ♥❛✈❡✳✈❡❧♦❝✐❞❛❞❡ ❂ ✺❀

     ✴✴ ✳✳✳
⑥

    No construtor da classe Nave, vamos iniciar o objeto que controla a
spritesheet. Usaremos inicialmente a linha zero, que representa a nave parada.
O intervalo entre um quadro e outro pode ser ajustado aos poucos conforme
o seu gosto:
❢✉♥❝t✐♦♥ ◆❛✈❡✭❝♦♥t❡①t✱ t❡❝❧❛❞♦✱ ✐♠❛❣❡♠✮ ④
   ✴✴ ✳✳✳
   t❤✐s✳s♣r✐t❡s❤❡❡t ❂ ♥❡✇ ❙♣r✐t❡s❤❡❡t✭❝♦♥t❡①t✱ ✐♠❛❣❡♠✱ ✸✱ ✷✮❀
   t❤✐s✳s♣r✐t❡s❤❡❡t✳❧✐♥❤❛ ❂ ✵❀
   t❤✐s✳s♣r✐t❡s❤❡❡t✳✐♥t❡r✈❛❧♦ ❂ ✶✵✵❀
⑥

   Altere agora o método desenhar para usar a spritesheet. Para definir
qual a linha a ser animada, lemos o estado das setas do teclado:
❞❡s❡♥❤❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✐❢ ✭t❤✐s✳t❡❝❧❛❞♦✳♣r❡ss✐♦♥❛❞❛✭❙❊❚❆❴❊❙◗❯❊❘❉❆✮✮
      t❤✐s✳s♣r✐t❡s❤❡❡t✳❧✐♥❤❛ ❂ ✶❀
   ❡❧s❡ ✐❢ ✭t❤✐s✳t❡❝❧❛❞♦✳♣r❡ss✐♦♥❛❞❛✭❙❊❚❆❴❉■❘❊■❚❆✮✮
      t❤✐s✳s♣r✐t❡s❤❡❡t✳❧✐♥❤❛ ❂ ✷❀
   ❡❧s❡
      t❤✐s✳s♣r✐t❡s❤❡❡t✳❧✐♥❤❛ ❂ ✵❀

     t❤✐s✳s♣r✐t❡s❤❡❡t✳❞❡s❡♥❤❛r✭t❤✐s✳①✱ t❤✐s✳②✮❀
     t❤✐s✳s♣r✐t❡s❤❡❡t✳♣r♦①✐♠♦◗✉❛❞r♦✭✮❀
⑥✱

    Também precisamos alterar o método atualizar, pois ele também
está usando as dimensões da imagem para não deixá-la passar da borda

                                                                                         167


[PAGINA 175]
8.3. Animando a nave com spritesheets                        Casa do Código


do Canvas. Nós substituímos as referências a this.imagem.width e
this.imagem.height pelos valores absolutos 36 e 48, respectivamente:

❛t✉❛❧✐③❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✴✴ ✳✳✳

      ✐❢ ✭t❤✐s✳t❡❝❧❛❞♦✳♣r❡ss✐♦♥❛❞❛✭❙❊❚❆❴❉■❘❊■❚❆✮ ✫✫
               t❤✐s✳① ❁ t❤✐s✳❝♦♥t❡①t✳❝❛♥✈❛s✳✇✐❞t❤ ✲ ✸✻✮
         t❤✐s✳① ✰❂ t❤✐s✳✈❡❧♦❝✐❞❛❞❡❀

      ✴✴ ✳✳✳

      ✐❢ ✭t❤✐s✳t❡❝❧❛❞♦✳♣r❡ss✐♦♥❛❞❛✭❙❊❚❆❴❆❇❆■❳❖✮ ✫✫
               t❤✐s✳② ❁ t❤✐s✳❝♦♥t❡①t✳❝❛♥✈❛s✳❤❡✐❣❤t ✲ ✹✽✮
         t❤✐s✳② ✰❂ t❤✐s✳✈❡❧♦❝✐❞❛❞❡❀
⑥✱

    Por último, perceba que o tiro sai um pouco deslocado, pois sua posição
é calculada pelo tamanho da imagem antiga. Vamos ajustar para um valor
absoluto, no construtor da classe Tiro. Também aproveitei o momento para
mudar a cor e deixá-lo um pouco menor:

❢✉♥❝t✐♦♥ ❚✐r♦✭❝♦♥t❡①t✱ ♥❛✈❡✮ ④
   t❤✐s✳❝♦♥t❡①t ❂ ❝♦♥t❡①t❀
   t❤✐s✳♥❛✈❡ ❂ ♥❛✈❡❀

      ✴✴ P♦s✐❝✐♦♥❛r ♦ t✐r♦ ♥♦ ❜✐❝♦ ❞❛ ♥❛✈❡
      t❤✐s✳❧❛r❣✉r❛ ❂ ✸❀
      t❤✐s✳❛❧t✉r❛ ❂ ✶✵❀
      t❤✐s✳① ❂ ♥❛✈❡✳① ✰ ✶✽❀ ✴✴ ✸✻ ✴ ✷
      t❤✐s✳② ❂ ♥❛✈❡✳② ✲ t❤✐s✳❛❧t✉r❛❀
      t❤✐s✳✈❡❧♦❝✐❞❛❞❡ ❂ ✶✵❀

      t❤✐s✳❝♦r ❂ ✬②❡❧❧♦✇✬❀
⑥

   Experimente jogar e perceba que o movimento da nave ganhou mais di-
namismo!


168


[PAGINA 176]
Casa do Código           Capítulo 8. Incorpore animações, sons, pausa e vidas extras ao jogo



8.4     Criando explosões
Vamos aproveitar o embalo das spritesheets e criar explosões. Usaremos o
arquivo explosao.png, que contém a spritesheet na figura 8.2:




                  Figura 8.2: Spritesheet para explosão


    Também será preciso acrescentar               uma       referência       ao     script
explosao.js, a ser criado logo mais:

❁s❝r✐♣t sr❝❂✧❡①♣❧♦s❛♦✳❥s✧❃❁✴s❝r✐♣t❃

    Na função carregarImagens, acrescente a imagem da explosão:

✐♠❛❣❡♥s ❂ ④
   ✴✴ ✳✳✳
   ♦✈♥✐✿     ✬♦✈♥✐✳♣♥❣✬✱ ✴✴ ✉♠❛ ✈ír❣✉❧❛ ❛q✉✐
   ❡①♣❧♦s❛♦✿ ✬❡①♣❧♦s❛♦✳♣♥❣✬
⑥❀

   No método colidiuCom da classe Ovni, onde este é destruído pelo
Tiro, vamos criar uma explosão:

❝♦❧✐❞✐✉❈♦♠✿ ❢✉♥❝t✐♦♥✭♦✉tr♦✮ ④
   ✴✴ ❙❡ ❝♦❧✐❞✐✉ ❝♦♠ ✉♠ ❚✐r♦✱ ♦s ❞♦✐s ❞❡s❛♣❛r❡❝❡♠
   ✐❢ ✭♦✉tr♦ ✐♥st❛♥❝❡♦❢ ❚✐r♦✮ ④
      ✴✴ ✳✳✳

        ✈❛r ❡①♣❧♦s❛♦ ❂ ♥❡✇ ❊①♣❧♦s❛♦✭t❤✐s✳❝♦♥t❡①t✱
           t❤✐s✳✐♠❣❊①♣❧♦s❛♦✱ t❤✐s✳①✱ t❤✐s✳②✮❀
        t❤✐s✳❛♥✐♠❛❝❛♦✳♥♦✈♦❙♣r✐t❡✭❡①♣❧♦s❛♦✮❀
    ⑥
⑥

                                                                                       169


[PAGINA 177]
8.4. Criando explosões                                     Casa do Código


   Os objetos que explodem precisam receber a imagem da explosão, para
poder criar os sprites. Mude o construtor do Ovni:

❢✉♥❝t✐♦♥ ❖✈♥✐✭❝♦♥t❡①t✱ ✐♠❛❣❡♠✱ ✐♠❣❊①♣❧♦s❛♦✮ ④
   ✴✴ ✳✳✳
   t❤✐s✳✐♠❣❊①♣❧♦s❛♦ ❂ ✐♠❣❊①♣❧♦s❛♦❀
⑥

      E passe a imagem na função novoOvni da página HTML:

✈❛r ♦✈♥✐ ❂ ♥❡✇ ❖✈♥✐✭❝♦♥t❡①t✱ ✐♠❣❖✈♥✐✱ ✐♠❛❣❡♥s✳❡①♣❧♦s❛♦✮❀

      Agora, crie a classe Explosao no arquivo explosao.js:

❢✉♥❝t✐♦♥ ❊①♣❧♦s❛♦✭❝♦♥t❡①t✱ ✐♠❛❣❡♠✱ ①✱ ②✮ ④
   t❤✐s✳❝♦♥t❡①t ❂ ❝♦♥t❡①t❀
   t❤✐s✳✐♠❛❣❡♠ ❂ ✐♠❛❣❡♠❀
   t❤✐s✳s♣r✐t❡s❤❡❡t ❂ ♥❡✇ ❙♣r✐t❡s❤❡❡t✭❝♦♥t❡①t✱ ✐♠❛❣❡♠✱ ✶✱ ✺✮❀
   t❤✐s✳s♣r✐t❡s❤❡❡t✳✐♥t❡r✈❛❧♦ ❂ ✼✺❀
   t❤✐s✳① ❂ ①❀
   t❤✐s✳② ❂ ②❀
⑥
❊①♣❧♦s❛♦✳♣r♦t♦t②♣❡ ❂ ④
   ❛t✉❛❧✐③❛r✿ ❢✉♥❝t✐♦♥✭✮ ④

      ⑥✱
      ❞❡s❡♥❤❛r✿ ❢✉♥❝t✐♦♥✭✮ ④

      ⑥
⑥

    No método desenhar, nós desenhamos o quadro atual e animamos a
spritesheet:

❞❡s❡♥❤❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   t❤✐s✳s♣r✐t❡s❤❡❡t✳❞❡s❡♥❤❛r✭t❤✐s✳①✱ t❤✐s✳②✮❀
   t❤✐s✳s♣r✐t❡s❤❡❡t✳♣r♦①✐♠♦◗✉❛❞r♦✭✮❀
⑥

   Mas assim a explosão ficará piscando na tela eternamente! O que quer-
emos é que, quando todos os quadros forem exibidos, a explosão termine.

170


[PAGINA 178]
Casa do Código           Capítulo 8. Incorpore animações, sons, pausa e vidas extras ao jogo



Mas como saber se a spritesheet chegou ao último quadro? Vamos criar
nela uma funcionalidade com a qual ela própria avisa isto. No construtor
da Explosao, crie um callback que recebe esse aviso:
❢✉♥❝t✐♦♥ ❊①♣❧♦s❛♦✭❝♦♥t❡①t✱ ✐♠❛❣❡♠✱ ①✱ ②✮ ④
   ✴✴ ✳✳✳
   ✈❛r ❡①♣❧♦s❛♦ ❂ t❤✐s❀
   t❤✐s✳s♣r✐t❡s❤❡❡t✳❢✐♠❉♦❈✐❝❧♦ ❂ ❢✉♥❝t✐♦♥✭✮ ④
      ❡①♣❧♦s❛♦✳❛♥✐♠❛❝❛♦✳❡①❝❧✉✐r❙♣r✐t❡✭❡①♣❧♦s❛♦✮❀
   ⑥
⑥

     Agora crie o atributo fimDoCiclo no construtor da Spritesheet:
❢✉♥❝t✐♦♥ ❙♣r✐t❡s❤❡❡t✭❝♦♥t❡①t✱ ✐♠❛❣❡♠✱ ❧✐♥❤❛s✱ ❝♦❧✉♥❛s✮ ④
   ✴✴ ✳✳✳
   t❤✐s✳❢✐♠❉♦❈✐❝❧♦ ❂ ♥✉❧❧❀
⑥

   E modifique o método proximoQuadro() para chamar esse callback
quando voltar ao quadro zero:
♣r♦①✐♠♦◗✉❛❞r♦✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✴✴ ✳✳✳

     ✐❢ ✭t❤✐s✳❝♦❧✉♥❛ ❁ t❤✐s✳♥✉♠❈♦❧✉♥❛s ✲ ✶✮ ④
        t❤✐s✳❝♦❧✉♥❛✰✰❀
     ⑥
     ❡❧s❡ ④
        t❤✐s✳❝♦❧✉♥❛ ❂ ✵❀

         ✴✴ ❆✈✐s❛r q✉❡ ❛❝❛❜♦✉ ✉♠ ❝✐❝❧♦✦
         ✐❢ ✭t❤✐s✳❢✐♠❉♦❈✐❝❧♦✮ t❤✐s✳❢✐♠❉♦❈✐❝❧♦✭✮❀
     ⑥

     ✴✴ ✳✳✳
⑥✱

   Experimente jogar! O Ovni já explode ao ser atingido pelo tiro. Agora
vamos explodir tanto a Nave quanto o Ovni quando eles colidirem. No
método colidiuCom da Nave, vamos criar duas explosões:

                                                                                        171


[PAGINA 179]
8.4. Criando explosões                                     Casa do Código


❝♦❧✐❞✐✉❈♦♠✿ ❢✉♥❝t✐♦♥✭♦✉tr♦✮ ④
   ✴✴ ❙❡ ❝♦❧✐❞✐✉ ❝♦♠ ✉♠ ❖✈♥✐✳✳✳
   ✐❢ ✭♦✉tr♦ ✐♥st❛♥❝❡♦❢ ❖✈♥✐✮ ④
      t❤✐s✳❛♥✐♠❛❝❛♦✳❡①❝❧✉✐r❙♣r✐t❡✭t❤✐s✮❀
      t❤✐s✳❛♥✐♠❛❝❛♦✳❡①❝❧✉✐r❙♣r✐t❡✭♦✉tr♦✮❀
      t❤✐s✳❝♦❧✐s♦r✳❡①❝❧✉✐r❙♣r✐t❡✭t❤✐s✮❀
      t❤✐s✳❝♦❧✐s♦r✳❡①❝❧✉✐r❙♣r✐t❡✭♦✉tr♦✮❀

          ✈❛r ❡①♣✶ ❂ ♥❡✇ ❊①♣❧♦s❛♦✭t❤✐s✳❝♦♥t❡①t✱ t❤✐s✳✐♠❣❊①♣❧♦s❛♦✱
                                  t❤✐s✳①✱ t❤✐s✳②✮❀
          ✈❛r ❡①♣✷ ❂ ♥❡✇ ❊①♣❧♦s❛♦✭t❤✐s✳❝♦♥t❡①t✱ t❤✐s✳✐♠❣❊①♣❧♦s❛♦✱
                                  ♦✉tr♦✳①✱ ♦✉tr♦✳②✮❀

          t❤✐s✳❛♥✐♠❛❝❛♦✳♥♦✈♦❙♣r✐t❡✭❡①♣✶✮❀
          t❤✐s✳❛♥✐♠❛❝❛♦✳♥♦✈♦❙♣r✐t❡✭❡①♣✷✮❀

          ✴✴ P♦r ❡♥q✉❛♥t♦ t✐r❡ ♦ tér♠✐♥♦ ❞❛ ❛♥✐♠❛çã♦
      ⑥
⑥

    Claro, a Nave também precisará receber a imagem da explosão no con-
strutor:

❢✉♥❝t✐♦♥ ◆❛✈❡✭❝♦♥t❡①t✱ t❡❝❧❛❞♦✱ ✐♠❛❣❡♠✱ ✐♠❣❊①♣❧♦s❛♦✮ ④
   ✴✴ ✳✳✳
   t❤✐s✳✐♠❣❊①♣❧♦s❛♦ ❂ ✐♠❣❊①♣❧♦s❛♦❀
⑥

  Portanto, passe-a ao criar a nave (método iniciarObjetos da página
HTML):

♥❛✈❡ ❂ ♥❡✇ ◆❛✈❡✭❝♦♥t❡①t✱ t❡❝❧❛❞♦✱ ✐♠❛❣❡♥s✳♥❛✈❡✱
                ✐♠❛❣❡♥s✳❡①♣❧♦s❛♦✮❀

    A Nave e o Ovni já explodem juntos. Gostaríamos de parar a ani-
mação e dar a mensagem “GAME OVER” somente quando essas explosões
finalizarem. Portanto, o sprite Explosao também poderia receber um call-
back. Complete o colidiuCom da Nave para passar esse callback:



172


[PAGINA 180]
Casa do Código           Capítulo 8. Incorpore animações, sons, pausa e vidas extras ao jogo



❝♦❧✐❞✐✉❈♦♠✿ ❢✉♥❝t✐♦♥✭♦✉tr♦✮ ④
   ✴✴ ❙❡ ❝♦❧✐❞✐✉ ❝♦♠ ✉♠ ❖✈♥✐✳✳✳
   ✐❢ ✭♦✉tr♦ ✐♥st❛♥❝❡♦❢ ❖✈♥✐✮ ④
      ✴✴ ✳✳✳

        ❡①♣✶✳❢✐♠❉❛❊①♣❧♦s❛♦ ❂ ❢✉♥❝t✐♦♥✭✮ ④
           ❛♥✐♠❛❝❛♦✳❞❡s❧✐❣❛r✭✮❀
           ❛❧❡rt✭✬●❆▼❊ ❖❱❊❘✬✮❀
        ⑥
    ⑥
⑥

    E modifique o construtor da Explosao para chamar esse callback ao fim
do ciclo da spritesheet:

❢✉♥❝t✐♦♥ ❊①♣❧♦s❛♦✭❝♦♥t❡①t✱ ✐♠❛❣❡♠✱ ①✱ ②✮ ④
   ✴✴ ✳✳✳

    ✈❛r ❡①♣❧♦s❛♦ ❂ t❤✐s❀
    t❤✐s✳❢✐♠❉❛❊①♣❧♦s❛♦ ❂ ♥✉❧❧❀
    t❤✐s✳s♣r✐t❡s❤❡❡t✳❢✐♠❉♦❈✐❝❧♦ ❂ ❢✉♥❝t✐♦♥✭✮ ④
       ❡①♣❧♦s❛♦✳❛♥✐♠❛❝❛♦✳❡①❝❧✉✐r❙♣r✐t❡✭❡①♣❧♦s❛♦✮❀
       ✐❢ ✭❡①♣❧♦s❛♦✳❢✐♠❉❛❊①♣❧♦s❛♦✮ ❡①♣❧♦s❛♦✳❢✐♠❉❛❊①♣❧♦s❛♦✭✮❀
    ⑥
⑥

    Não é legal? A Spritesheet informa à Explosao quando completou
a animação dos quadros, e a Explosao se retira da animação e notifica a
quem interessar.
    Brinque um pouco, acho que você merece!




                                                                                       173


[PAGINA 181]
8.4. Criando explosões                                               Casa do Código




                         Figura 8.3: Agora as colisões têm emoção!




174


[PAGINA 182]
Casa do Código               Capítulo 8. Incorpore animações, sons, pausa e vidas extras ao jogo



8.5 Pausando o jogo




                 Figura 8.4: Jogo pausado com indicativo na tela


Nós já temos pausa implementada em nosso game engine: os métodos ligar
e desligar da classe Animacao. No entanto, é preciso tratar alguns acon-
tecimentos que estão ocorrendo na animação, ao se pausar o jogo.
    Vamos definir que o jogador pausará o jogo através da tecla Enter, cujo
código é 13 (se preferir usar outra tecla, fique à vontade).
    No início do arquivo teclado.js, acrescente uma variável para guardar
o código do Enter:

✴✴ ❈ó❞✐❣♦s ❞❡ t❡❝❧❛s ✲ ❛q✉✐ ✈ã♦ t♦❞♦s ♦s q✉❡ ❢♦r❡♠ ♥❡❝❡ssár✐♦s
✈❛r ❙❊❚❆❴❊❙◗❯❊❘❉❆ ❂ ✸✼❀
✈❛r ❙❊❚❆❴❆❈■▼❆ ❂ ✸✽❀
✈❛r ❙❊❚❆❴❉■❘❊■❚❆ ❂ ✸✾❀
✈❛r ❙❊❚❆❴❆❇❆■❳❖ ❂ ✹✵❀


                                                                                           175


[PAGINA 183]
8.5. Pausando o jogo                                            Casa do Código


✈❛r ❊❙P❆❈❖ ❂ ✸✷❀
✈❛r ❊◆❚❊❘ ❂ ✶✸❀

   Agora, no método configuracoesIniciais, configure a ação da tecla
Enter:

✴✴ P❛✉s❛
t❡❝❧❛❞♦✳❞✐s♣❛r♦✉✭❊◆❚❊❘✱ ♣❛✉s❛r❏♦❣♦✮❀

      E crie a função pausarJogo, que é quem fará o trabalho:
❢✉♥❝t✐♦♥ ♣❛✉s❛r❏♦❣♦✭✮ ④
   ✐❢ ✭❛♥✐♠❛❝❛♦✳❧✐❣❛❞♦✮
      ❛♥✐♠❛❝❛♦✳❞❡s❧✐❣❛r✭✮❀
   ❡❧s❡
      ❛♥✐♠❛❝❛♦✳❧✐❣❛r✭✮❀
⑥

    Faça o teste: neste ponto o jogo já deve pausar e despausar. No entanto,
você poderá notar alguns bugs. Primeiro, pause enquanto um disco voador
está na tela, e em seguida despause: ele some! Isso ocorre porque sua ani-
mação está cronometrada, e o tempo da pausa está sendo contado para cal-
cular seu movimento. Quando a animação reinicia, o disco já deve estar longe,
e assim o jogo o posiciona.
    Para resolver isso, na classe Animacao, no método ligar, reinicie o
atributo ultimoCiclo para zero. Isto fará a contagem de tempo ser reinici-
ada:
❧✐❣❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   t❤✐s✳✉❧t✐♠♦❈✐❝❧♦ ❂ ✵❀
   t❤✐s✳❧✐❣❛❞♦ ❂ tr✉❡❀
   t❤✐s✳♣r♦①✐♠♦❋r❛♠❡✭✮❀
⑥✱

    Um outro problema é: funções de disparo (no caso, o tiro) continuam
sendo possíveis! Isto não ocorre com a movimentação pelas setas, pois são
lidas no método atualizar da Nave, dentro do loop de animação (que
estaria pausado).
    Modifiquemos a função para desativar ou reativar a tecla Espaço (tiro)
conforme pausamos e despausamos o jogo:

176


[PAGINA 184]
Casa do Código             Capítulo 8. Incorpore animações, sons, pausa e vidas extras ao jogo



❢✉♥❝t✐♦♥ ♣❛✉s❛r❏♦❣♦✭✮ ④
   ✐❢ ✭❛♥✐♠❛❝❛♦✳❧✐❣❛❞♦✮ ④
      ❛♥✐♠❛❝❛♦✳❞❡s❧✐❣❛r✭✮❀
      ❛t✐✈❛r❚✐r♦✭❢❛❧s❡✮❀
   ⑥
   ❡❧s❡ ④
      ❛♥✐♠❛❝❛♦✳❧✐❣❛r✭✮❀
      ❛t✐✈❛r❚✐r♦✭tr✉❡✮❀
   ⑥
⑥

   A função ativarTiro vai modificar os eventos do teclado, configu-
rando a tecla Espaço:

❢✉♥❝t✐♦♥ ❛t✐✈❛r❚✐r♦✭❛t✐✈❛r✮ ④
   ✐❢ ✭❛t✐✈❛r✮ ④
      t❡❝❧❛❞♦✳❞✐s♣❛r♦✉✭❊❙P❆❈❖✱ ❢✉♥❝t✐♦♥✭✮ ④
         ♥❛✈❡✳❛t✐r❛r✭✮❀
      ⑥✮❀
   ⑥
   ❡❧s❡
      t❡❝❧❛❞♦✳❞✐s♣❛r♦✉✭❊❙P❆❈❖✱ ♥✉❧❧✮❀
⑥

    Para         não
                ficarmos    com       código                         repetido,           em
configuracoesIniciais, remova as linhas:

✴✴ ❘❡♠♦✈❛ ❡st❛s ❧✐♥❤❛s
✴✴ ❚✐r♦
t❡❝❧❛❞♦✳❞✐s♣❛r♦✉✭❊❙P❆❈❖✱ ❢✉♥❝t✐♦♥✭✮ ④
   ♥❛✈❡✳❛t✐r❛r✭✮❀
⑥✮❀

    E coloque esta no lugar:

✴✴ ❚✐r♦
❛t✐✈❛r❚✐r♦✭tr✉❡✮❀

    Também ocorre que um inimigo é gerado imediatamente após a despausa,
pois estamos gerando um inimigo por segundo e a pausa faz esse tempo se

                                                                                         177


[PAGINA 185]
8.5. Pausando o jogo                                          Casa do Código


exceder. Antes de ligar a animação, reinicie o momento da geração do último
inimigo para o instante atual, para evitar que isso ocorra:
❢✉♥❝t✐♦♥ ♣❛✉s❛r❏♦❣♦✭✮ ④
   ✴✴ ✳✳✳

      ❡❧s❡ ④
         ❝r✐❛❞♦r■♥✐♠✐❣♦s✳✉❧t✐♠♦❖✈♥✐ ❂ ♥❡✇ ❉❛t❡✭✮✳❣❡t❚✐♠❡✭✮❀
         ❛♥✐♠❛❝❛♦✳❧✐❣❛r✭✮❀
         ❛t✐✈❛r❚✐r♦✭tr✉❡✮❀
      ⑥
⑥

    Quantos detalhes uma simples pausa nos obriga a tratar! Para ficar mais
interessante, vamos exibir o texto “Pausado” na tela:
❢✉♥❝t✐♦♥ ♣❛✉s❛r❏♦❣♦✭✮ ④
   ✐❢ ✭❛♥✐♠❛❝❛♦✳❧✐❣❛❞♦✮ ④
      ❛♥✐♠❛❝❛♦✳❞❡s❧✐❣❛r✭✮❀
      ❛t✐✈❛r❚✐r♦✭❢❛❧s❡✮❀

         ✴✴ ❊s❝r❡✈❡r ✧P❛✉s❛❞♦✧
         ❝♦♥t❡①t✳s❛✈❡✭✮❀
         ❝♦♥t❡①t✳❢✐❧❧❙t②❧❡ ❂ ✬✇❤✐t❡✬❀
         ❝♦♥t❡①t✳str♦❦❡❙t②❧❡ ❂ ✬❜❧❛❝❦✬❀
         ❝♦♥t❡①t✳❢♦♥t ❂ ✬✺✵♣① s❛♥s✲s❡r✐❢✬❀
         ❝♦♥t❡①t✳❢✐❧❧❚❡①t✭✧P❛✉s❛❞♦✧✱ ✶✻✵✱ ✷✵✵✮❀
         ❝♦♥t❡①t✳str♦❦❡❚❡①t✭✧P❛✉s❛❞♦✧✱ ✶✻✵✱ ✷✵✵✮❀
         ❝♦♥t❡①t✳r❡st♦r❡✭✮❀
      ⑥
      ❡❧s❡ ④
         ❝r✐❛❞♦r■♥✐♠✐❣♦s✳✉❧t✐♠♦❖✈♥✐ ❂ ♥❡✇ ❉❛t❡✭✮✳❣❡t❚✐♠❡✭✮❀
         ❛♥✐♠❛❝❛♦✳❧✐❣❛r✭✮❀
         ❛t✐✈❛r❚✐r♦✭tr✉❡✮❀
      ⑥
⑥

    Use sua imaginação! Coloque qualquer imagem, texto, ou combinação
dos dois. Pode até instanciar outra Animacao, colocar alguns sprites especí-
ficos e exibir alguns movimentos durante a pausa.

178


[PAGINA 186]
Casa do Código            Capítulo 8. Incorpore animações, sons, pausa e vidas extras ao jogo



8.6    Sons e música de fundo
Esta parte é muito fácil de implementar. O HTML5, além do Canvas, possui
uma API de áudio muito simples. No pacote de arquivos, na pasta deste capí-
tulo ( 08), há uma subpasta com o nome snd contendo alguns arquivos de
som, em formato MP3.


  Bancos de sons grátis e direitos autorais

     Jamais use sons de terceiros sem a devida autorização! Criadores
  de jogos independentes, sem meios ou conhecimentos para gerar seus
  próprios sons, podem contar com inúmeros bancos de sons gratuitos es-
  palhados pela internet.
     Os sons para o jogo deste livro foram obtidos em http://freesound.org.



    Primeiro, vamos produzir o som dos tiros. Abra o arquivo tiro.js e
coloque as instruções para carregar o som logo no início do arquivo. Instan-
ciamos um objeto Audio (presente na API do HTML5), setamos seu atributo
src para o arquivo tiro.mp3 (presente no pacote de download) e ajustamos
o volume como um valor entre 0 e 1. Por último, chamamos o método load
para iniciar o carregamento do arquivo, evitando que seja carregado somente
no momento da reprodução:

✈❛r ❙❖▼❴❚■❘❖ ❂ ♥❡✇ ❆✉❞✐♦✭✮❀
❙❖▼❴❚■❘❖✳sr❝ ❂ ✬s♥❞✴t✐r♦✳♠♣✸✬❀
❙❖▼❴❚■❘❖✳✈♦❧✉♠❡ ❂ ✵✳✷❀
❙❖▼❴❚■❘❖✳❧♦❛❞✭✮❀

    Depois, vamos reproduzir esse som cada vez que um tiro é criado. No
construtor, rebobinamos o som ajustando o atributo currentTime para
zero. Esse atributo indica o instante atual de reprodução, dado em segundos.
Em seguida, basta chamar o método play:

❢✉♥❝t✐♦♥ ❚✐r♦✭❝♦♥t❡①t✱ ♥❛✈❡✮ ④
   ✴✴ ✳✳✳

                                                                                        179


[PAGINA 187]
8.6. Sons e música de fundo                                Casa do Código




      ❙❖▼❴❚■❘❖✳❝✉rr❡♥t❚✐♠❡ ❂ ✵✳✵❀
      ❙❖▼❴❚■❘❖✳♣❧❛②✭✮❀
⑥

    Os tiros já fazem barulho! Vamos fazer o mesmo procedimento para as
explosões. No início do arquivo explosao.js, coloque as instruções:
✈❛r ❙❖▼❴❊❳P▲❖❙❆❖ ❂ ♥❡✇ ❆✉❞✐♦✭✮❀
❙❖▼❴❊❳P▲❖❙❆❖✳sr❝ ❂ ✬s♥❞✴❡①♣❧♦s❛♦✳♠♣✸✬❀
❙❖▼❴❊❳P▲❖❙❆❖✳✈♦❧✉♠❡ ❂ ✵✳✹❀
❙❖▼❴❊❳P▲❖❙❆❖✳❧♦❛❞✭✮❀

   E no construtor, mande rebobinar e reproduzir, da mesma forma que com
o Tiro:
❢✉♥❝t✐♦♥ ❊①♣❧♦s❛♦✭❝♦♥t❡①t✱ ✐♠❛❣❡♠✱ ①✱ ②✮ ④
   ✴✴ ✳✳✳

      ❙❖▼❴❊❳P▲❖❙❆❖✳❝✉rr❡♥t❚✐♠❡ ❂ ✵✳✵❀
      ❙❖▼❴❊❳P▲❖❙❆❖✳♣❧❛②✭✮❀
⑥

    Vamos também colocar uma música de fundo para dar mais emoção ao
jogo. No início da página HTML, acrescente a variável musicaAcao:
✴✴ ❱❛r✐á✈❡✐s ♣r✐♥❝✐♣❛✐s
✈❛r ✐♠❛❣❡♥s✱ ❛♥✐♠❛❝❛♦✱ t❡❝❧❛❞♦✱ ❝♦❧✐s♦r✱ ♥❛✈❡✱ ❝r✐❛❞♦r■♥✐♠✐❣♦s❀
✈❛r t♦t❛❧■♠❛❣❡♥s ❂ ✵✱ ❝❛rr❡❣❛❞❛s ❂ ✵❀
✈❛r ♠✉s✐❝❛❆❝❛♦❀

   Em seguida, logo após a chamada para carregarImagens, coloque
também uma chamada para carregarMusicas:
✴✴ ❈♦♠❡ç❛ ❝❛rr❡❣❛♥❞♦ ❛s ✐♠❛❣❡♥s ❡ ♠ús✐❝❛s
❝❛rr❡❣❛r■♠❛❣❡♥s✭✮❀
❝❛rr❡❣❛r▼✉s✐❝❛s✭✮❀

   E crie a função carregarMusicas. Aqui, setamos o atributo loop para
true, fazendo com que a música repita incessantemente durante a ação do
jogo.

180


[PAGINA 188]
Casa do Código            Capítulo 8. Incorpore animações, sons, pausa e vidas extras ao jogo



❢✉♥❝t✐♦♥ ❝❛rr❡❣❛r▼✉s✐❝❛s✭✮ ④
   ♠✉s✐❝❛❆❝❛♦ ❂ ♥❡✇ ❆✉❞✐♦✭✮❀
   ♠✉s✐❝❛❆❝❛♦✳sr❝ ❂ ✬s♥❞✴♠✉s✐❝❛✲❛❝❛♦✳♠♣✸✬❀
   ♠✉s✐❝❛❆❝❛♦✳❧♦❛❞✭✮❀
   ♠✉s✐❝❛❆❝❛♦✳✈♦❧✉♠❡ ❂ ✵✳✽❀
   ♠✉s✐❝❛❆❝❛♦✳❧♦♦♣ ❂ tr✉❡❀
   ♠✉s✐❝❛❆❝❛♦✳♣❧❛②✭✮❀
⑥

   Viu como é bem fácil? Divirta-se mais um pouco!
   Dica: você pode parar a música no momento da pausa usando o método
pause.


8.7    Tela de loading




       Figura 8.5: Indique para o jogador que o jogo está carregando




                                                                                         181


[PAGINA 189]
8.7. Tela de loading                                         Casa do Código


Vamos modificar a função carregando da página HTML para incrementar
uma barra conforme as imagens vão sendo carregadas. Primeiro, como vamos
desenhar, guarde a configuração atual do contexto (método save) e crie um
fundo. Aqui, fiz um fundo simples, com a imagem do espaço. Se tiver vontade
faça um desenho mais elaborado. Sinta-se livre!

❢✉♥❝t✐♦♥ ❝❛rr❡❣❛♥❞♦✭✮ ④
   ❝♦♥t❡①t✳s❛✈❡✭✮❀

      ✴✴ ❋✉♥❞♦
      ❝♦♥t❡①t✳❞r❛✇■♠❛❣❡✭✐♠❛❣❡♥s✳❡s♣❛❝♦✱ ✵✱ ✵✱ ❝❛♥✈❛s✳✇✐❞t❤✱
                        ❝❛♥✈❛s✳❤❡✐❣❤t✮❀

      ✴✴ ❝♦♥t✐♥✉❛ ✳✳✳
⑥

      Em seguida, vamos criar o texto “Carregando":

❢✉♥❝t✐♦♥ ❝❛rr❡❣❛♥❞♦✭✮ ④
   ✴✴ ✳✳✳

      ✴✴ ❚❡①t♦ ✧❈❛rr❡❣❛♥❞♦✧
      ❝♦♥t❡①t✳❢✐❧❧❙t②❧❡ ❂ ✬✇❤✐t❡✬❀
      ❝♦♥t❡①t✳str♦❦❡❙t②❧❡ ❂ ✬❜❧❛❝❦✬❀
      ❝♦♥t❡①t✳❢♦♥t ❂ ✬✺✵♣① s❛♥s✲s❡r✐❢✬❀
      ❝♦♥t❡①t✳❢✐❧❧❚❡①t✭✧❈❛rr❡❣❛♥❞♦✳✳✳✧✱ ✶✵✵✱ ✷✵✵✮❀
      ❝♦♥t❡①t✳str♦❦❡❚❡①t✭✧❈❛rr❡❣❛♥❞♦✳✳✳✧✱ ✶✵✵✱ ✷✵✵✮❀

      ✴✴ ❝♦♥t✐♥✉❛ ✳✳✳
⑥

    O próximo passo é desenhar a barra. Neste ponto, precisamos incremen-
tar a variável carregadas, para poder calcular a largura atual da barra:

❢✉♥❝t✐♦♥ ❝❛rr❡❣❛♥❞♦✭✮ ④
   ✴✴ ✳✳✳

      ✴✴ ❇❛rr❛ ❞❡ ❧♦❛❞✐♥❣
      ❝❛rr❡❣❛❞❛s✰✰❀


182


[PAGINA 190]
Casa do Código              Capítulo 8. Incorpore animações, sons, pausa e vidas extras ao jogo



    ✈❛r t❛♠❛♥❤♦❚♦t❛❧ ❂ ✸✵✵❀
    ✈❛r t❛♠❛♥❤♦ ❂ ❝❛rr❡❣❛❞❛s ✴ t♦t❛❧■♠❛❣❡♥s ✯ t❛♠❛♥❤♦❚♦t❛❧❀
    ❝♦♥t❡①t✳❢✐❧❧❙t②❧❡ ❂ ✬②❡❧❧♦✇✬❀
    ❝♦♥t❡①t✳❢✐❧❧❘❡❝t✭✶✵✵✱ ✷✺✵✱ t❛♠❛♥❤♦✱ ✺✵✮❀

    ✴✴ ❝♦♥t✐♥✉❛ ✳✳✳
⑥

    Por último, restauramos as configurações anteriores do contexto (método
restore) e, em vez de iniciar o jogo imediatamente, vamos mostrar um link
“Jogar”, a ser criado logo adiante, para o jogador clicar quando estiver pronto:

❢✉♥❝t✐♦♥ ❝❛rr❡❣❛♥❞♦✭✮ ④
   ✴✴ ✳✳✳

    ❝♦♥t❡①t✳r❡st♦r❡✭✮❀

    ✐❢ ✭❝❛rr❡❣❛❞❛s ❂❂ t♦t❛❧■♠❛❣❡♥s✮ ④
       ✐♥✐❝✐❛r❖❜❥❡t♦s✭✮❀
       ♠♦str❛r▲✐♥❦❏♦❣❛r✭✮❀
    ⑥
⑥

    Como o jogo não vai iniciar automaticamente, tire o comando que inicia
a animação da função configuracoesIniciais:

✴✴ ❘❡♠♦✈❛ ❡st❛ ❧✐♥❤❛
❛♥✐♠❛❝❛♦✳❧✐❣❛r✭✮❀

    E também a chamada ao método play da função carregarMusicas:

✴✴ ❘❡♠♦✈❛ ❡st❛ ❧✐♥❤❛
♠✉s✐❝❛❆❝❛♦✳♣❧❛②✭✮❀

    Crie então um link para iniciar o jogo. Logo após a tag <canvas>, insira
esse link, com uma chamada para a função iniciarJogo:

❁❛ ✐❞❂✧❧✐♥❦❴❥♦❣❛r✧ ❤r❡❢❂✧❥❛✈❛s❝r✐♣t✿ ✐♥✐❝✐❛r❏♦❣♦✭✮✧❃❏♦❣❛r❁✴❛❃



                                                                                          183


[PAGINA 191]
8.7. Tela de loading                                         Casa do Código


    Vamos configurar sua aparência e posição via CSS. Você pode configurar
esse botão da forma que quiser, e não é o foco deste livro ficar detalhando
formatações em CSS. Caso não tenha muita prática, aí está uma formatação
sugerida. No pacote de downloads, existe a imagem botao-jogar.png,
que usei como fundo.
    Na seção <head> do documento (pode ser após os scripts), crie uma tag
<style>. O mais importante é que o botão inicie oculto e tenha posiciona-
mento absoluto, para podermos colocá-lo por cima do Canvas:

❁st②❧❡❃
★❧✐♥❦❴❥♦❣❛r ④
   ✴✯ ■♥✐❝✐❛ ♦❝✉❧t♦ ✯✴
   ❞✐s♣❧❛②✿ ♥♦♥❡❀

      ✴✯ ❈♦r❡s ❡ ❢✉♥❞♦ ✯✴
      ❝♦❧♦r✿ ②❡❧❧♦✇❀
      ❜❛❝❦❣r♦✉♥❞✿ ✉r❧✭✐♠❣✴❜♦t❛♦✲❥♦❣❛r✳♣♥❣✮❀

      ✴✯ ❋♦♥t❡ ✯✴
      ❢♦♥t✲s✐③❡✿ ✷✵♣①❀
      ❢♦♥t✲❢❛♠✐❧②✿ s❛♥s✲s❡r✐❢❀

      ✴✯ ❙❡♠ s✉❜❧✐♥❤❛❞♦ ❡ ❝♦♠ s♦♠❜r❛ ✯✴
      t❡①t✲❞❡❝♦r❛t✐♦♥✿ ♥♦♥❡❀
      t❡①t✲s❤❛❞♦✇✿ ✷♣① ✷♣① ✺♣① ❜❧❛❝❦❀

      ✴✯ P♦s✐❝✐♦♥❛♠❡♥t♦ ✯✴
      ♣♦s✐t✐♦♥✿ ❛❜s♦❧✉t❡❀
      ❧❡❢t✿ ✷✷✵♣①❀
      t♦♣✿ ✸✸✵♣①❀

      ✴✯ ❆ ✐♠❛❣❡♠ ❞♦ ❜♦tã♦ é ✼✷①✼✷✱ ❞❡s❝♦♥t❛♠♦s ♦s ♣❛❞❞✐♥❣s ✯✴
      ✇✐❞t❤✿ ✺✷♣①❀
      ❤❡✐❣❤t✿ ✷✻♣①❀
      ♣❛❞❞✐♥❣✿ ✷✸♣① ✶✵♣①❀
⑥
❁✴st②❧❡❃



184


[PAGINA 192]
Casa do Código             Capítulo 8. Incorpore animações, sons, pausa e vidas extras ao jogo



  E crie a função mostrarLinkJogar, que mandará mostrar esse link,
modificando seu atributo CSS display para o valor block.

❢✉♥❝t✐♦♥ ♠♦str❛r▲✐♥❦❏♦❣❛r✭✮ ④
   ❞♦❝✉♠❡♥t✳❣❡t❊❧❡♠❡♥t❇②■❞✭✬❧✐♥❦❴❥♦❣❛r✬✮✳st②❧❡✳❞✐s♣❧❛② ❂
      ✬❜❧♦❝❦✬❀
⑥

    A função iniciarJogo, chamada pelo link, irá esconder o link “Jogar”,
iniciar a música e ligar a animação:

❢✉♥❝t✐♦♥ ✐♥✐❝✐❛r❏♦❣♦✭✮ ④
   ❞♦❝✉♠❡♥t✳❣❡t❊❧❡♠❡♥t❇②■❞✭✬❧✐♥❦❴❥♦❣❛r✬✮✳st②❧❡✳❞✐s♣❧❛② ❂
      ✬♥♦♥❡✬❀
   ♠✉s✐❝❛❆❝❛♦✳♣❧❛②✭✮❀
   ❛♥✐♠❛❝❛♦✳❧✐❣❛r✭✮❀
⑥

    Faça o teste! Enquanto você estiver testando o jogo em seu computa-
dor, a tela carregará bem rapidamente. No entanto, ela fará (muita) diferença
quando hospedarmos nosso jogo na web.
    Ainda temos um problema: a tecla Enter dá início ao jogo sem fazer
sumir o botão Jogar! Isso ocorre porque ela está despausando o jogo em um
momento em que a animação não está rodando.
    Para corrigir isso, vamos tirar as seguintes linhas de
configuracoesIniciais:

✴✴ ❘❡♠♦✈❛ ❡st❛s ❧✐♥❤❛s
✴✴ ❚✐r♦
❛t✐✈❛r❚✐r♦✭tr✉❡✮❀

✴✴ ❊ ❡st❛s t❛♠❜é♠
✴✴ P❛✉s❛
t❡❝❧❛❞♦✳❞✐s♣❛r♦✉✭❊◆❚❊❘✱ ♣❛✉s❛r❏♦❣♦✮❀

    Vamos ativá-las em iniciarJogo:

❢✉♥❝t✐♦♥ ✐♥✐❝✐❛r❏♦❣♦✭✮ ④
   ✴✴ ❚✐r♦

                                                                                         185


[PAGINA 193]
8.8. Vidas extras                                                Casa do Código


      ❛t✐✈❛r❚✐r♦✭tr✉❡✮❀

      ✴✴ P❛✉s❛
      t❡❝❧❛❞♦✳❞✐s♣❛r♦✉✭❊◆❚❊❘✱ ♣❛✉s❛r❏♦❣♦✮❀

      ✴✴ ✳✳✳
⑥


8.8       Vidas extras




             Figura 8.6: Dê mais chances ao jogador com vidas extras!


Programar vidas extras não é tão complicado, tudo é questão de mexer nos
algoritmos da nave. Para facilitar, vamos criar um atributo de callback onde
a Nave nos informa quando acabaram as vidas. No construtor, crie esse call-
back e o atributo vidasExtras:

❢✉♥❝t✐♦♥ ◆❛✈❡✭❝♦♥t❡①t✱ t❡❝❧❛❞♦✱ ✐♠❛❣❡♠✱ ✐♠❣❊①♣❧♦s❛♦✮ ④
   ✴✴ ✳✳✳
   t❤✐s✳❛❝❛❜❛r❛♠❱✐❞❛s ❂ ♥✉❧❧❀
   t❤✐s✳✈✐❞❛s❊①tr❛s ❂ ✸❀
⑥

    No método colidiuCom, onde detectamos sua colisão mortal, retire as
linhas que mandam finalizar o jogo:

✴✴ ❘❡t✐r❡ ❡st❛s ❧✐♥❤❛s✿
❡①♣✶✳❢✐♠❉❛❊①♣❧♦s❛♦ ❂ ❢✉♥❝t✐♦♥✭✮ ④
   ❛♥✐♠❛❝❛♦✳❞❡s❧✐❣❛r✭✮❀
   ❛❧❡rt✭✬●❆▼❊ ❖❱❊❘✬✮❀
⑥

   E substitua-as pelo código a seguir. Nós vamos decrementar o atributo
vidasExtras, e verificar se as vidas acabaram (e notificar, se for o caso).

186


[PAGINA 194]
Casa do Código           Capítulo 8. Incorpore animações, sons, pausa e vidas extras ao jogo



Caso o jogo continue, nós recolocamos a nave na animação e no colisor e a
reposicionamos:

✈❛r ♥❛✈❡ ❂ t❤✐s❀
❡①♣✶✳❢✐♠❉❛❊①♣❧♦s❛♦ ❂ ❢✉♥❝t✐♦♥✭✮ ④
   ♥❛✈❡✳✈✐❞❛s❊①tr❛s✲✲❀

    ✐❢ ✭♥❛✈❡✳✈✐❞❛s❊①tr❛s ❁ ✵✮ ④
       ✐❢ ✭♥❛✈❡✳❛❝❛❜❛r❛♠❱✐❞❛s✮ ♥❛✈❡✳❛❝❛❜❛r❛♠❱✐❞❛s✭✮❀
    ⑥
    ❡❧s❡ ④
       ✴✴ ❘❡❝♦❧♦❝❛r ❛ ♥❛✈❡ ♥♦ ❡♥❣✐♥❡
       ♥❛✈❡✳❝♦❧✐s♦r✳♥♦✈♦❙♣r✐t❡✭♥❛✈❡✮❀
       ♥❛✈❡✳❛♥✐♠❛❝❛♦✳♥♦✈♦❙♣r✐t❡✭♥❛✈❡✮❀

        ♥❛✈❡✳♣♦s✐❝✐♦♥❛r✭✮❀
    ⑥
⑥

   O posicionamento da nave é exatamente o que já estamos fazendo na
função configuracoesIniciais da página HTML. Retire as linhas:

✴✴ ◆❛✈❡
✴✴ ❘❡t✐r❡ ❛s ❞✉❛s ❧✐♥❤❛s ❛❜❛✐①♦
♥❛✈❡✳① ❂ ❝❛♥✈❛s✳✇✐❞t❤ ✴ ✷ ✲ ✶✽❀ ✴✴ ✸✻ ✴ ✷
♥❛✈❡✳② ❂ ❝❛♥✈❛s✳❤❡✐❣❤t ✲ ✹✽❀

    E coloque no lugar uma chamada ao método posicionar:

✴✴ ◆❛✈❡
♥❛✈❡✳♣♦s✐❝✐♦♥❛r✭✮❀
♥❛✈❡✳✈❡❧♦❝✐❞❛❞❡ ❂ ✷✵✵❀

    Vamos criar o método na Nave, fazendo essa mesma tarefa:

♣♦s✐❝✐♦♥❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✈❛r ❝❛♥✈❛s ❂ t❤✐s✳❝♦♥t❡①t✳❝❛♥✈❛s❀
   t❤✐s✳① ❂ ❝❛♥✈❛s✳✇✐❞t❤ ✴ ✷ ✲ ✶✽❀ ✴✴ ✸✻ ✴ ✷
   t❤✐s✳② ❂ ❝❛♥✈❛s✳❤❡✐❣❤t ✲ ✹✽❀
⑥

                                                                                       187


[PAGINA 195]
8.8. Vidas extras                                               Casa do Código


    Por fim, em configuracoesIniciais, insira as linhas que finalizam
o jogo, respondendo ao callback acabaramVidas da Nave:
❢✉♥❝t✐♦♥ ❝♦♥❢✐❣✉r❛❝♦❡s■♥✐❝✐❛✐s✭✮ ④
   ✴✴ ✳✳✳

      ✴✴ ●❛♠❡ ❖✈❡r
      ♥❛✈❡✳❛❝❛❜❛r❛♠❱✐❞❛s ❂ ❢✉♥❝t✐♦♥✭✮ ④
         ❛♥✐♠❛❝❛♦✳❞❡s❧✐❣❛r✭✮❀
         ❛❧❡rt✭✬●❆▼❊ ❖❱❊❘✬✮❀
      ⑥
⑥

   Exercício: implemente, através da leitura do teclado, um cheat code que
dê mais vidas ao jogador!

Um mostrador de vidas
   Legal, nossa nave já tem vidas extras! Vamos criar agora o arquivo
painel.js, para mostrar essas vidas extras. Seu esqueleto fica:

✴✴ ❛rq✉✐✈♦✿ ♣❛✐♥❡❧✳❥s
❢✉♥❝t✐♦♥ P❛✐♥❡❧✭❝♦♥t❡①t✱ ♥❛✈❡✮ ④
   t❤✐s✳❝♦♥t❡①t ❂ ❝♦♥t❡①t❀
   t❤✐s✳♥❛✈❡ ❂ ♥❛✈❡❀
⑥
P❛✐♥❡❧✳♣r♦t♦t②♣❡ ❂ ④
   ❛t✉❛❧✐③❛r✿ ❢✉♥❝t✐♦♥✭✮ ④

      ⑥✱
      ❞❡s❡♥❤❛r✿ ❢✉♥❝t✐♦♥✭✮ ④

      ⑥
⑥

      Claro, insira o script na seção <head>:
❁s❝r✐♣t sr❝❂✧♣❛✐♥❡❧✳❥s✧❃❁✴s❝r✐♣t❃

   Na função iniciarObjetos, crie o painel e insira-o na animação.
Optei por deixar a nave por último, para que ela sempre fique acima do painel:

188


[PAGINA 196]
Casa do Código            Capítulo 8. Incorpore animações, sons, pausa e vidas extras ao jogo



❢✉♥❝t✐♦♥ ✐♥✐❝✐❛r❖❜❥❡t♦s✭✮ ④
   ✴✴ ❖❜❥❡t♦s ♣r✐♥❝✐♣❛✐s
   ✴✴ ✳✳✳
   ♣❛✐♥❡❧ ❂ ♥❡✇ P❛✐♥❡❧✭❝♦♥t❡①t✱ ♥❛✈❡✮❀

    ✴✴ ▲✐❣❛çõ❡s ❡♥tr❡ ♦❜❥❡t♦s
    ✴✴ ✳✳✳
    ❛♥✐♠❛❝❛♦✳♥♦✈♦❙♣r✐t❡✭♣❛✐♥❡❧✮❀
    ❛♥✐♠❛❝❛♦✳♥♦✈♦❙♣r✐t❡✭♥❛✈❡✮❀

    ✴✴ ✳✳✳
⑥

    No construtor do Painel, vamos criar uma spritesheet a partir da im-
agem da nave. Nós usaremos somente a primeira imagem, que corresponde
à nave parada:

❢✉♥❝t✐♦♥ P❛✐♥❡❧✭❝♦♥t❡①t✱ ♥❛✈❡✮ ④
   ✴✴ ✳✳✳
   t❤✐s✳s♣r✐t❡s❤❡❡t ❂
      ♥❡✇ ❙♣r✐t❡s❤❡❡t✭❝♦♥t❡①t✱ ♥❛✈❡✳✐♠❛❣❡♠✱ ✸✱ ✷✮❀
   t❤✐s✳s♣r✐t❡s❤❡❡t✳❧✐♥❤❛ ❂ ✵❀
   t❤✐s✳s♣r✐t❡s❤❡❡t✳❝♦❧✉♥❛ ❂ ✵❀
⑥

    No método desenhar, obtemos o número de vidas extras e desenhamos
a imagem esse número de vezes:

❞❡s❡♥❤❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✈❛r ① ❂ ✷✵❀
   ✈❛r ② ❂ ✷✵❀

    ❢♦r ✭✈❛r ✐ ❂ ✶❀ ✐ ❁❂ t❤✐s✳♥❛✈❡✳✈✐❞❛s❊①tr❛s❀ ✐✰✰✮ ④
       t❤✐s✳s♣r✐t❡s❤❡❡t✳❞❡s❡♥❤❛r✭①✱ ②✮❀
       ① ✰❂ ✹✵❀
    ⑥
⑥

   Eu achei que os desenhos das vidas estão muito grandes. Vou usar aqui o
método scale do context para desenhá-los com metade do tamanho:

                                                                                        189


[PAGINA 197]
8.9. Pontuação (score)                                    Casa do Código


❞❡s❡♥❤❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✴✴ ❘❡❞✉③ ♦ ❞❡s❡♥❤♦ ♣❡❧❛ ♠❡t❛❞❡
   t❤✐s✳❝♦♥t❡①t✳s❝❛❧❡✭✵✳✺✱ ✵✳✺✮❀

      ✈❛r ① ❂ ✷✵❀
      ✈❛r ② ❂ ✷✵❀

      ❢♦r ✭✈❛r ✐ ❂ ✶❀ ✐ ❁❂ t❤✐s✳♥❛✈❡✳✈✐❞❛s❊①tr❛s❀ ✐✰✰✮ ④
         t❤✐s✳s♣r✐t❡s❤❡❡t✳❞❡s❡♥❤❛r✭①✱ ②✮❀
         ① ✰❂ ✹✵❀
      ⑥

      ✴✴ ❚♦r♥❛ ❛ ❞♦❜r❛r
      t❤✐s✳❝♦♥t❡①t✳s❝❛❧❡✭✷✱ ✷✮❀
⑥

   Você pode usar o tamanho que preferir, ou mesmo usar um arquivo de
imagem apenas para isso, em tamanho menor. Mas com o scale é bem
mais econômico, não acha?


8.9       Pontuação (score)
Aproveitando que temos um painel mostrador de vidas, podemos criar nele
um atributo pontuacao. Em sua função construtora, coloque a instrução:

t❤✐s✳♣♦♥t✉❛❝❛♦ ❂ ✵❀

    Em configuracoesIniciais, vamos criar um tratador geral de col-
isões que verifica se é um Tiro e um Ovni que estão colidindo. Em caso
positivo, incrementamos essa pontuação no painel:

❢✉♥❝t✐♦♥ ❝♦♥❢✐❣✉r❛❝♦❡s■♥✐❝✐❛✐s✭✮ ④
   ✴✴ ✳✳✳

      ✴✴ P♦♥t✉❛çã♦
      ❝♦❧✐s♦r✳❛♦❈♦❧✐❞✐r ❂ ❢✉♥❝t✐♦♥✭♦✶✱ ♦✷✮ ④
         ✴✴ ❚✐r♦ ❝♦♠ ❖✈♥✐
         ✐❢ ✭ ✭♦✶ ✐♥st❛♥❝❡♦❢ ❚✐r♦ ✫✫ ♦✷ ✐♥st❛♥❝❡♦❢ ❖✈♥✐✮ ⑤⑤
              ✭♦✶ ✐♥st❛♥❝❡♦❢ ❖✈♥✐ ✫✫ ♦✷ ✐♥st❛♥❝❡♦❢ ❚✐r♦✮ ✮

190


[PAGINA 198]
Casa do Código            Capítulo 8. Incorpore animações, sons, pausa e vidas extras ao jogo



           ♣❛✐♥❡❧✳♣♦♥t✉❛❝❛♦ ✰❂ ✶✵❀
           ✴✴ ❯s❡ ♦ ✐♥❝r❡♠❡♥t♦ q✉❡ ❞❡s❡❥❛r
    ⑥
⑥

   Agora, modifique o método desenhar do painel para escrever a pontu-
ação ao lado dos ícones das vidas:

❞❡s❡♥❤❛r✿ ❢✉♥❝t✐♦♥✭✮ ④
   ✴✴ ✳✳✳

    ✴✴ P❛r❛ ❢❛❝✐❧✐t❛r ✉♠ ♣♦✉❝♦✳✳✳
    ✈❛r ❝t① ❂ t❤✐s✳❝♦♥t❡①t❀

    ✴✴ P♦♥t✉❛çã♦
    ❝t①✳s❛✈❡✭✮❀
    ❝t①✳❢✐❧❧❙t②❧❡ ❂ ✬✇❤✐t❡✬❀
    ❝t①✳❢♦♥t ❂ ✬✶✽♣① s❛♥s✲s❡r✐❢✬❀
    ❝t①✳❢✐❧❧❚❡①t✭t❤✐s✳♣♦♥t✉❛❝❛♦✱ ✶✵✵✱ ✷✼✮❀
    ❝t①✳r❡st♦r❡✭✮❀
⑥

    Por último, não se esqueça de zerar o painel cada vez que o jogo inicia,
do contrário a pontuação fica lá para a próxima partida. Em iniciarJogo,
coloque o comando:

♣❛✐♥❡❧✳♣♦♥t✉❛❝❛♦ ❂ ✵❀




                                                                                         191


[PAGINA 199]
8.10. Tela de Game Over                                          Casa do Código


8.10 Tela de Game Over




                          Figura 8.7: Que pena... fim de jogo!


Vamos finalizar nosso jogo criando uma tela de Game Over! Em
configuracoesIniciais, tire aquele alerta horrível e troque por uma
chamada à função gameOver:
❢✉♥❝t✐♦♥ ❝♦♥❢✐❣✉r❛❝♦❡s■♥✐❝✐❛✐s✭✮ ④
   ✴✴ ✳✳✳

      ✴✴ ●❛♠❡ ❖✈❡r
      ♥❛✈❡✳❛❝❛❜❛r❛♠❱✐❞❛s ❂ ❢✉♥❝t✐♦♥✭✮ ④
         ❛♥✐♠❛❝❛♦✳❞❡s❧✐❣❛r✭✮❀
         ❣❛♠❡❖✈❡r✭✮❀
      ⑥
⑥

  Nessa função, vamos desativar as teclas de disparo, parar a música e criar
uma tela mais adequada. O link “Jogar” deve voltar a aparecer, e a nave deve

192


[PAGINA 200]
Casa do Código            Capítulo 8. Incorpore animações, sons, pausa e vidas extras ao jogo



ser recolocada no game engine (pois foi tirada no momento da colisão):

❢✉♥❝t✐♦♥ ❣❛♠❡❖✈❡r✭✮ ④
   ✴✴ ❚✐r♦
   ❛t✐✈❛r❚✐r♦✭❢❛❧s❡✮❀

    ✴✴ P❛✉s❛
    t❡❝❧❛❞♦✳❞✐s♣❛r♦✉✭❊◆❚❊❘✱ ♥✉❧❧✮❀

    ✴✴ P❛r❛r ❛ ♠ús✐❝❛ ❡ r❡❜♦❜✐♥❛r
    ♠✉s✐❝❛❆❝❛♦✳♣❛✉s❡✭✮❀
    ♠✉s✐❝❛❆❝❛♦✳❝✉rr❡♥t❚✐♠❡ ❂ ✵✳✵❀

    ✴✴ ❋✉♥❞♦
    ❝♦♥t❡①t✳❞r❛✇■♠❛❣❡✭✐♠❛❣❡♥s✳❡s♣❛❝♦✱ ✵✱ ✵✱ ❝❛♥✈❛s✳✇✐❞t❤✱
                      ❝❛♥✈❛s✳❤❡✐❣❤t✮❀

    ✴✴ ❚❡①t♦ ✧●❛♠❡ ❖✈❡r✧
    ❝♦♥t❡①t✳s❛✈❡✭✮❀
    ❝♦♥t❡①t✳❢✐❧❧❙t②❧❡ ❂ ✬✇❤✐t❡✬❀
    ❝♦♥t❡①t✳str♦❦❡❙t②❧❡ ❂ ✬❜❧❛❝❦✬❀
    ❝♦♥t❡①t✳❢♦♥t ❂ ✬✼✵♣① s❛♥s✲s❡r✐❢✬❀
    ❝♦♥t❡①t✳❢✐❧❧❚❡①t✭✧●❆▼❊ ❖❱❊❘✧✱ ✹✵✱ ✷✵✵✮❀
    ❝♦♥t❡①t✳str♦❦❡❚❡①t✭✧●❆▼❊ ❖❱❊❘✧✱ ✹✵✱ ✷✵✵✮❀
    ❝♦♥t❡①t✳r❡st♦r❡✭✮❀

    ✴✴ ❱♦❧t❛ ♦ ❧✐♥❦ ✧❏♦❣❛r✧
    ♠♦str❛r▲✐♥❦❏♦❣❛r✭✮❀

    ✴✴ ❘❡st❛✉r❛r ❛s ❝♦♥❞✐çõ❡s ❞❛ ♥❛✈❡
    ♥❛✈❡✳✈✐❞❛s❊①tr❛s ❂ ✸❀
    ♥❛✈❡✳♣♦s✐❝✐♦♥❛r✭✮❀
    ❛♥✐♠❛❝❛♦✳♥♦✈♦❙♣r✐t❡✭♥❛✈❡✮❀
    ❝♦❧✐s♦r✳♥♦✈♦❙♣r✐t❡✭♥❛✈❡✮❀
⑥

    Você perceberá uma coisa: Ovnis que sobraram na animação, continuam
lá para o próximo jogo! Ao fim de gameOver, chame uma nova função,
removerInimigos:


                                                                                        193


[PAGINA 201]
8.10. Tela de Game Over                                     Casa do Código


❢✉♥❝t✐♦♥ ❣❛♠❡❖✈❡r✭✮ ④
   ✴✴ ✳✳✳

      r❡♠♦✈❡r■♥✐♠✐❣♦s✭✮❀
⑥

      Nesta função, nós mandamos excluir todos os Ovnis da animação:

❢✉♥❝t✐♦♥ r❡♠♦✈❡r■♥✐♠✐❣♦s✭✮ ④
   ❢♦r ✭✈❛r ✐ ✐♥ ❛♥✐♠❛❝❛♦✳s♣r✐t❡s✮ ④
      ✐❢ ✭❛♥✐♠❛❝❛♦✳s♣r✐t❡s❬✐❪ ✐♥st❛♥❝❡♦❢ ❖✈♥✐✮
         ❛♥✐♠❛❝❛♦✳❡①❝❧✉✐r❙♣r✐t❡✭❛♥✐♠❛❝❛♦✳s♣r✐t❡s❬✐❪✮❀
   ⑥
⑥

    Finalmente, reinicie o instante da geração de inimigos em
iniciarJogo, para que não surja um Ovni de repente quando o
jogo for reiniciado. Faça isto antes de ligar a animação:

❢✉♥❝t✐♦♥ ✐♥✐❝✐❛r❏♦❣♦✭✮ ④
   ❝r✐❛❞♦r■♥✐♠✐❣♦s✳✉❧t✐♠♦❖✈♥✐ ❂ ♥❡✇ ❉❛t❡✭✮✳❣❡t❚✐♠❡✭✮❀

      ✴✴ ✳✳✳
⑥

   Pode soltar fogos de artifício! Temos um jogo simples, embora completo
em termos de animação, engine e algoritmos.




194


[PAGINA 202]
Casa do Código             Capítulo 8. Incorpore animações, sons, pausa e vidas extras ao jogo




  Exercícios

     Agora ficará por sua conta melhorar o jogo! Aqui estão algumas sug-
  estões do que você pode fazer:

      • Criar novos tipos de inimigos;

      • Fases e cenários diferentes;

      • Tipos diferentes de naves e tiros;

      • Coleta de itens;

      • E o que mais sua imaginação permitir!

     Com os conhecimentos que você adquiriu, essas tarefas não dev-
  erão ser tão árduas assim. Se você sentir que não tem bom domínio do
  game engine, sugiro que refaça a criação do jogo, quantas vezes forem
  necessárias, até sentir-se seguro.




                                                                                         195


[PAGINA 203]


[PAGINA 204]
Capítulo 9

Publique seu jogo e torne-o
conhecido
9.1    Hospede-o em um serviço gratuito
Talvez você, sendo desenvolvedor web, já tenha os meios de ter seu jogo pub-
licado na web. No entanto, para tirar quaisquer eventuais dúvidas, ou caso
você seja iniciante nesta matéria, quero mostrar um meio de você colocar seu
jogo na internet, usando um dos inúmeros serviços de hospedagem gratuita
existentes.
    Nosso jogo não é mais do que uma página web estática, usando apenas
tecnologias do lado cliente (um pouco de HTML e CSS, e muito JavaScript).
Desta forma, pode ser colocado na web como qualquer site comum.
    Escolhi o Hostinger (http://www.hostinger.com.br) , por considerá-lo fá-


[PAGINA 205]
9.1. Hospede-o em um serviço gratuito                            Casa do Código


cil de usar e já estar habituado a ele. No entanto, você pode escolher outro
serviço, se preferir. Acesse o site e clique no link Criar conta:


  Hospedagens gratuitas

       Alguns exemplos de hospedagens gratuitas disponíveis:

        • Hostinger: http://www.hostinger.com.br

        • Hospedagratis.net: http://hospedagratis.net

        • Qlix: http://www.qlix.com.br




                    Figura 9.1: Criando uma conta no Hostinger


    O formulário de cadastro não é muito diferente dos formulários mais
básicos existentes na web:




198


[PAGINA 206]
Casa do Código                          Capítulo 9. Publique seu jogo e torne-o conhecido




                     Figura 9.2: Cadastro no Hostinger


    Após isto, é preciso acessar seu e-mail e clicar no link de ativação en-
viado pela Hostinger. Caso não apareça, confira sua pasta de spam ou lixo
eletrônico.
    Do link, você irá direto para a escolha do plano de hospedagem. Para
pequenos aplicativos, podemos usar o plano gratuito sem medo:




Figura 9.3: Você está ‘comprando’ o plano gratuito pelo incrível preço de zero
reais!


    Em seguida, você tem a opção de usar um subdomínio gratuito, ao invés

                                                                                    199


[PAGINA 207]
9.1. Hospede-o em um serviço gratuito                              Casa do Código


de adquirir um nome de domínio (lembre-se de que, para ter seu endereço
próprio na internet, é preciso pagar a taxa de registro). Foi esta opção que
usei, embora eu imagine que você, como futuro desenvolvedor de jogos, vá
um dia querer ter o domínio www.jogosdo(seunomeaqui).com.br:




                           Figura 9.4: Criando o subdomínio


     A próxima tela será apenas uma confirmação dos dados do domínio. Dig-
ite as letras e aceite os termos como de costume.
     O domínio está criado! Clique em seu nome e em seguida aparecerá o
ícone Gerenciar:




                 Figura 9.5: Abra o domínio e entre em Gerenciar


   Você terá que rolar um pouco a página para encontrar o Gerenciador
de Arquivos:

200


[PAGINA 208]
Casa do Código                           Capítulo 9. Publique seu jogo e torne-o conhecido




                 Figura 9.6: Ícone do Gerenciador de Arquivos


   Se o serviço solicitar uma confirmação para instalar o gerenciador, clique
em Instalar.
   Crie as subpastas do jogo. Use o botão Nova Pasta e crie as pastas img
e snd:




            Figura 9.7: Criando uma nova pasta na hospedagem




                      Figura 9.8: Crie as pastas img e snd


                                                                                     201


[PAGINA 209]
9.1. Hospede-o em um serviço gratuito                            Casa do Código


    Use o botão Fazer Upload e suba os arquivos da pasta principal. Em
seguida, entre nas pastas img e snd e repita o processo. Você pode subir
vários arquivos de uma vez.




                       Figura 9.9: Botão de upload de arquivos


    Renomeie o arquivo jogo-definitivo.html para index.html. É
por esse nome que o servidor reconhece a página inicial de seu site:




           Figura 9.10: A página principal deve se chamar index.html


    Por último, delete a antiga página principal colocada pela Hostinger (ar-
quivo default.php).
    Pronto, pode navegar no site recém-criado e publicar seu URL onde
quiser!




202


[PAGINA 210]
Casa do Código                       Capítulo 9. Publique seu jogo e torne-o conhecido




            Figura 9.11: Jogo publicado em hospedagem gratuita



9.2    Linkando com as redes sociais

Obtendo uma ID do Facebook
Para poder interagir com o Facebook em suas aplicações, você deve possuir
um App ID, que é um código de cadastro no Facebook associado com seu
aplicativo.
    Primeiro, faça o login no Facebook como de costume. Em seguida,
acesse http://developers.facebook.com e abra o menu Aplicativos. Se
você ainda não é desenvolvedor, será apresentada a opção Register as
a Developer:




                                                                                 203


[PAGINA 211]
9.2. Linkando com as redes sociais                                 Casa do Código




            Figura 9.12: Registre-se como desenvolvedor no Facebook


   Sua conta será confirmada como desenvolvedor. Agora você tem a opção
Create a New App:




                  Figura 9.13: Criando um aplicativo no Facebook


     Em seguida, você terá que preencher os dados como o nome, uma iden-
tificação (namespace) que deve ser única para cada aplicativo, a categoria etc.




204


[PAGINA 212]
Casa do Código                        Capítulo 9. Publique seu jogo e torne-o conhecido




                   Figura 9.14: Cadastre seu aplicativo


    Pronto, você já tem uma ID! Guarde o código em algum lugar seguro.




                 Figura 9.15: ID de aplicação no Facebook


     Agora, temos que configurar a URL de nosso site para evitar problemas
de permissão. Vá ao link Configurações e clique no botão Adicionar
Plataforma. Selecione Site e preencha a URL de seu site no campo que
foi aberto:




                                                                                  205


[PAGINA 213]
9.2. Linkando com as redes sociais                                Casa do Código




                       Figura 9.16: Configure a URL de seu site


    Por último, no campo App Domains, insira o endereço que você acabou
de configurar (o Facebook já lista automaticamente as URLs configuradas):




              Figura 9.17: Configure a URL no campo App Domains


    Estamos prontos para inserir funcionalidades do Facebook em nosso
jogo!

Inicializando a API
    O código de inicialização da API pode ser obtido do próprio Facebook, no
endereço http://developers.facebook.com/docs/javascript/quickstart/v2.0. A
própria documentação recomenda que seja colado logo após a abertura da
tag <body>:

❁❜♦❞②❃

      ❁s❝r✐♣t❃
        ✇✐♥❞♦✇✳❢❜❆s②♥❝■♥✐t ❂ ❢✉♥❝t✐♦♥✭✮ ④
          ❋❇✳✐♥✐t✭④
            ✴✴ ❊st❛ é s✉❛ ■❉
            ❛♣♣■❞      ✿ ✬✷✺✻✸✺✶✺✺✹✺✺✵✵✸✶✬✱


206


[PAGINA 214]
Casa do Código                     Capítulo 9. Publique seu jogo e torne-o conhecido



           ①❢❜♠❧       ✿ tr✉❡✱
           ✈❡rs✐♦♥     ✿ ✬✈✷✳✵✬
         ⑥✮❀
       ⑥❀

       ✭❢✉♥❝t✐♦♥✭❞✱ s✱ ✐❞✮④
          ✈❛r ❥s✱ ❢❥s ❂ ❞✳❣❡t❊❧❡♠❡♥ts❇②❚❛❣◆❛♠❡✭s✮❬✵❪❀
          ✐❢ ✭❞✳❣❡t❊❧❡♠❡♥t❇②■❞✭✐❞✮✮ ④r❡t✉r♥❀⑥
          ❥s ❂ ❞✳❝r❡❛t❡❊❧❡♠❡♥t✭s✮❀ ❥s✳✐❞ ❂ ✐❞❀
          ❥s✳sr❝ ❂ ✧❤tt♣✿✴✴❝♦♥♥❡❝t✳❢❛❝❡❜♦♦❦✳♥❡t✴♣t❴❇❘✴s❞❦✳❥s✧❀
          ❢❥s✳♣❛r❡♥t◆♦❞❡✳✐♥s❡rt❇❡❢♦r❡✭❥s✱ ❢❥s✮❀
        ⑥✭❞♦❝✉♠❡♥t✱ ✬s❝r✐♣t✬✱ ✬❢❛❝❡❜♦♦❦✲❥ss❞❦✬✮✮❀
     ❁✴s❝r✐♣t❃

     ✳✳✳

❁✴❜♦❞②❃

Botão Compartilhar
   Em http://developers.facebook.com/docs/plugins/share-button, você
pode gerar um botão “Compartilhar” para sua página. O código gerado é
semelhante ao mostrado a seguir. Coloque-o no local que achar melhor,
dando-lhe bastante destaque na página:

❁❞✐✈ ✐❞❂✧❜♦t❛♦❴❝♦♠♣❛rt✐❧❤❛r✧
     ❝❧❛ss❂✧❢❜✲s❤❛r❡✲❜✉tt♦♥✧
     ❞❛t❛✲❤r❡❢❂✧❤tt♣✿✴✴s✉❛❴❤♦s♣❡❞❛❣❡♠❴❛q✉✐✧
     ❞❛t❛✲t②♣❡❂✧❜✉tt♦♥❴❝♦✉♥t✧❃❁✴❞✐✈❃

Compartilhando a pontuação
    Uma coisa muito interessante é podermos postar qualquer informação
programaticamente. Por exemplo, podemos colocar um link para postar o
score na tela de Game Over!
    Primeiro, criamos esse link:

❁❛ ✐❞❂✧♣♦st❛r❴♣♦♥t✉❛❝❛♦✧ ❤r❡❢❂✧❥❛✈❛s❝r✐♣t✿ ♣♦st❛rP♦♥t✉❛❝❛♦✭✮✧❃
  ❈♦♠♣❛rt✐❧❤❛r P♦♥t✉❛çã♦

                                                                               207


[PAGINA 215]
9.2. Linkando com as redes sociais                       Casa do Código


❁✴❛❃

   Este link deve começar escondido, portanto, crie uma formatação CSS
que o oculte:

❁st②❧❡❃

✳✳✳

★♣♦st❛r❴♣♦♥t✉❛❝❛♦ ④
   ✴✯ ❖❝✉❧t❛r ♦ ❧✐♥❦ ✯✴
   ❞✐s♣❧❛②✿ ♥♦♥❡❀

    ✴✯ ❱✐s✉❛❧ ❛ ❣♦st♦✦ ✯✴
    ❝♦❧♦r✿ ②❡❧❧♦✇❀
    ♣♦s✐t✐♦♥✿ ❛❜s♦❧✉t❡❀
    ❧❡❢t✿ ✶✽✵♣①❀
    t♦♣✿ ✹✶✵♣①❀
⑥
❁✴st②❧❡❃

      E mande-o aparecer na função gameOver:

❢✉♥❝t✐♦♥ ❣❛♠❡❖✈❡r✭✮ ④
   ✴✴ ✳✳✳

    ✴✴ ▲✐♥❦ ❞❡ ♣♦st❛r ♣♦♥t✉❛çã♦
    ❞♦❝✉♠❡♥t✳❣❡t❊❧❡♠❡♥t❇②■❞✭✬♣♦st❛r❴♣♦♥t✉❛❝❛♦✬✮
       ✳st②❧❡✳❞✐s♣❧❛② ❂ ✬❜❧♦❝❦✬❀
⑥

    A função postarPontuacao chama a API do Facebook para abrir uma
janela que compartilha texto:

❢✉♥❝t✐♦♥ ♣♦st❛rP♦♥t✉❛❝❛♦✭✮ ④
    ✴✴ ❆q✉✐ ♦❜t❡rí❛♠♦s ❛ ♣♦♥t✉❛çã♦ ❞♦ ❥♦❣♦
    ✈❛r ♣♦♥t✉❛❝❛♦ ❂ ✶✵✵✵✵✵❀

      ✴✴ ❆P■ ❞❡ ❢❡❡❞ ❞♦ ❋❛❝❡❜♦♦❦
      ❋❇✳✉✐✭

208


[PAGINA 216]
Casa do Código                        Capítulo 9. Publique seu jogo e torne-o conhecido



       ④
        ♠❡t❤♦❞✿ ✬❢❡❡❞✬✱
        ♥❛♠❡✿ ✬❏♦❣♦ ❞❡ ◆❛✈❡✬✱
        ❝❛♣t✐♦♥✿ ✬❏♦❣✉❡ ❡ ❝♦♠♣❛rt✐❧❤❡ ❝♦♠ s❡✉s ❛♠✐❣♦s✦✬✱
        ❞❡s❝r✐♣t✐♦♥✿ ✭
           ✬▼✐♥❤❛ ♣♦♥t✉❛çã♦ ❢♦✐✿ ✬ ✰ ♣❛✐♥❡❧✳♣♦♥t✉❛❝❛♦
        ✮✱
        ❧✐♥❦✿ ✬❤tt♣✿✴✴s✉❛❴❤♦s♣❡❞❛❣❡♠❴❛q✉✐✬
       ⑥✱
       ❢✉♥❝t✐♦♥✭r❡s♣♦♥s❡✮ ④⑥
     ✮❀
⑥

    Por último, mande o link desaparecer na função iniciarJogo:

❢✉♥❝t✐♦♥ ✐♥✐❝✐❛r❏♦❣♦✭✮ ④
   ❞♦❝✉♠❡♥t✳❣❡t❊❧❡♠❡♥t❇②■❞✭✬♣♦st❛r❴♣♦♥t✉❛❝❛♦✬✮✳st②❧❡✳❞✐s♣❧❛② ❂
      ✬♥♦♥❡✬❀

    ✴✴ ✳✳✳
⑥

    Dê ao link um visual bem agradável e veja-o na tela de Game Over:




                                                                                  209


[PAGINA 217]
9.2. Linkando com as redes sociais                           Casa do Código




Figura 9.18: Tela de Game Over com link para postar a pontuação no Face-
book




              Figura 9.19: Popup de compartilhamento do Facebook




210


[PAGINA 218]
Casa do Código                          Capítulo 9. Publique seu jogo e torne-o conhecido



    Agora seu jogo está pronto para ser divulgado nas redes sociais pelos seus
jogadores!




                                                                                     211


[PAGINA 219]


[PAGINA 220]
Casa do Código                                         Referências Bibliográficas




Referências Bibliográficas

[1] David Geary. Core HTML5 Canvas - Graphics, Animation and Game De-
    velopment. 2012.

[2] David Geary. Html5 2d game development: Introducing snail bait. 2012.

[3] W3Schools. Html5 canvas.




                                                                            213
