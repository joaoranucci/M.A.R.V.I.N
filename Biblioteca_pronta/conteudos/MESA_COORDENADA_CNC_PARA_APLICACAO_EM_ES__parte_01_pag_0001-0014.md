# MESA_COORDENADA_CNC_PARA_APLICACAO_EM_ES

Arquivo original: most_similar_papers_to_this_one/MESA_COORDENADA_CNC_PARA_APLICACAO_EM_ES.pdf
SHA-256 do original: e5a86fe2fa84291faa961193acdb37ccd6a1912b66e17de06c81cb99570e8250

Texto extraido para consulta. As paginas abaixo usam a ordem do arquivo PDF, incluindo capas.
Parte preparada: 1/1


[PAGINA 1]
                                  PROJETO APLICADO
                    INSTITUTO POLITÉCNICO – Centro Universitário UNA

       MESA COORDENADA CNC PARA APLICAÇÃO EM ESCRITA
     BRAILLE GRAU UM: FOCO PARA A LÍNGUA PORTUGUESA
Curso: Engenharia de Computação      Professor Orientador: Luiz Guilherme Hilel Drumond Silveira
  Ana Caroline de Mendonça, Bernardino F. Machado Neto, Daphne Fernanda F. B. de Carvalho,
 Diego W. Pereira Neto, Fernando Piermatei, Igor Augusto S. de Oliveira, Jonathan R. B. Campos.




      Resumo  O sistema Braille é um recurso para a acessibilidade, porém o
acesso a documentos em Braille nem sempre é fácil. Este artigo apresenta os
resultados do projeto de uma mesa coordenada CNC para escrita Braille grau um:
foco na língua portuguesa; destinado a implementar, avaliar e validar, por meio de
testes de legibilidade do documento impresso, o produto final do equipamento.
      Palavras-chave  Braille, CNC, motor de passo, microcontrolador 8051.

1. INTRODUÇÃO

      No Brasil, os direitos das pessoas portadoras de deficiência vêm sendo
negligenciados; enfrentam-se diversas barreiras físicas, existentes diante da
despreocupação e do despreparo dos técnicos das diversas áreas, como transporte,
comunicação, entre outros (GARCIA, 2008).
      O crescente desenvolvimento tecnológico contribui para a melhor inserção do
portador de deficiência à sociedade. A acessibilidade em espaços públicos e
privados vem sendo aprimorada, porém algumas deficiências não ganham o foco
necessário. Deficientes visuais, por exemplo, necessitam de ambientes adaptados
para melhor locomoção e interação. Para tal, é comumente utilizado o Braille,
sistema de escrita em relevo constituído por 64 sinais formados por pontos a partir
do conjunto matricial (123456) (CERQUEIRA, 2006).
      O Braille é um recurso para acessibilidade, porém as tecnologias de
impressão Braille apresentam difícil aquisição, bem como, o número de pessoas
especializadas na operação e manutenção desses equipamentos são reduzidos,
tornando o custo alto. As impressoras Braille computadorizadas usadas no Brasil
são importadas, devido a isso são configuradas para a impressão em outro idioma,
gerando uma maior dificuldade para a adaptação do equipamento para produzir o



                                                                                               1


[PAGINA 2]
Braille em codificação segundo o padrão brasileiro (BORGES; CHAGAS JÚNIOR,
2010).
         Mesas coordenadas são tecnologias comumente utilizadas, devido à sua
versatilidade e baixo custo; estas apresentam aplicações nas áreas industrial,
comercial e de serviços.
         Diante disso a questão norteadora deste estudo foi elaborada: qual solução
pode ser desenvolvida para a produção em pequeno porte de conteúdo impresso em
Braille?
         Deste modo, objetiva-se projetar uma mesa coordenada CNC (Computer
Numeric Control) para escrita Braille, tendo como foco a língua portuguesa. Objetiva-
se especificamente avaliar a legibilidade do documento produzido pela mesa
coordenada CNC.

2. REVISÃO BIBLIOGRÁFICA

         Nesta seção, apresenta-se uma revisão bibliográfica sobre o sistema Braille,
escrita e geração de conteúdo, CNC, motor de passo e microcontrolador 8051.

    2.1.    Sistema Braille
         O sistema Braille foi inventado por Louis Braille, em 1825, trata-se de um
sistema de escrita em relevo mais adotado em todo o mundo, constituído por 64
sinais; conjunto de 6 pontos (3 linhas e 2 colunas), denominado sinal fundamental. O
espaço ocupado pelo sinal fundamental é denominado de célula Braille. Para
estabelecer a posição relativa, os pontos são numerados de cima para baixo e da
esquerda para a direita (CERQUEIRA, 2006). A figura 01 apresenta a célula Braille.




                                  Figura 01: célula Braille
                              Fonte: CERQUEIRA et. al. (2006)

         O Braille é aplicado à representação dos símbolos literais, matemáticos,
químicos, fonéticos, informáticos, musicais, etc., sendo a escrita Braille baseada em
três graus. O grau 1 é usado para representar cada caractere correspondente no
sistema comum de escrita, aplicado na alfabetização de deficientes visuais, mais
fácil de aprender em relação ao grau 2 e 3, porém, é mais lento para ser transcrito e
lido, tendo o produto impresso final mais volumoso; o grau 2 e o grau 3 apresenta


                                                                                     2


[PAGINA 3]
uma forma de escrita Braille abreviada, onde um caractere pode representar duas ou
mais letras ou mesmo uma palavra inteira (CERQUEIRA, 2006).
      A aplicação à língua portuguesa apresenta quase todos os sinais a sua
significação original, apenas algumas vogais acentuadas e outros símbolos se
representam por sinais exclusivos. Os sinais do código Braille empregam-se
geralmente em conformidade com os preceitos da ortografia oficial e com os textos
que representam (CERQUEIRA, 2006). O Anexo A contém o alfabeto Braille,
elementos textuais, sinais usados com números e sinais exclusivos da escrita Braille.
      A geração de conteúdo Braille pode ser realizada de forma manual, máquina
de escrever e computadorizada. A transcrição manual é realizada por meio do uso
da reglete e do punção; por meio de máquina é feito utilizando a máquina Braille,
equipamento mecânico ou elétrico, no qual seis teclas produzem pontos em relevo;
a impressora Braille computadorizada é um equipamento que produz em papel
textos em Braille, estas são conectadas a um microcomputador através de porta
serial, fazendo uso do protocolo SPI (Serial Peripheral Interface) destinado à
comunicação síncrona com dispositivos; ou porta paralela (CERQUEIRA, 2006); o
processo de transcrição da impressora Braille computadorizada apresenta tempo de
produção menor do que o processo de escrita manual ou máquina de escrever
(BORGES; CHAGAS JÚNIOR, 2010). A figura 02 apresenta uma máquina Braille (a)
e impressora Braille computadorizada de médio (b) e grande (c) porte.




Figura 02: máquina Braille (a) e impressora Braille computadorizada de médio (b) e grande (c) porte
                          Fonte: adaptado de CERQUEIRA et. al. (2006)

      Na transcrição para Braille deve se seguir o mais próximo possível a
disposição de qualquer texto em tinta. Para tal é realizada a adaptação de textos
para transcrição, processo no qual às adequações e ajustes prévios devem ser
feitos no texto, considerando as características do conteúdo e as especificidades da
leitura tátil (CERQUEIRA, 2006).

    2.2.   CNC
      Dentre várias técnicas de automação de sistemas pode-se destacar o CNC
(Computer Numeric Control), muito utilizado para a geração de peças com
geometrias complexas. A máquina CNC é composta da unidade de comando, onde
se encontra o software e processam-se todos os cálculos do sistema, a máquina

                                                                                                  3


[PAGINA 4]
propriamente dita e os acionamentos dos motores, responsáveis pelos movimentos
dos eixos na sequência programada, sem a intervenção do operador. Para realizar
estes procedimentos envolvem-se comandos de movimentação, posicionamento,
velocidade, frequência de rotação, entre outros (QUEIROZ, 2007).
      A máquina pode realizar a movimentação dos eixos utilizando os métodos de
coordenadas cartesianas, em único eixo linear, em um plano na composição de dois
eixos ou pela movimentação no espaço utilizando simultaneamente os três eixos. O
programa para o CNC é estruturado na forma de blocos de dados, onde cada bloco
contém dados para produzir uma ação na máquina. Qualquer mudança na peça do
equipamento acarreta na simples mudança no programa (SOUZA; ULBRICH, 2009).

    2.3.   Motor de passo
      Os motores de passo são dispositivos eletromecânicos que convertem pulsos
elétricos em movimentos mecânicos que geram variações angulares discretas, as
quais geram precisão de movimentos. Deve-se observar, para um controle
adequado, a tensão de alimentação e a corrente elétrica que as bobinas do motor de
passo suportam (BRITOS; SANTOS, 2008).
      O rotor (eixo) de um motor de passo é rotacionado em pequenos incrementos
angulares (passos), quando pulsos elétricos são aplicados em determinada
sequência nos terminais deste. A rotação é diretamente relacionada aos impulsos
elétricos recebidos, bem como a sequência a qual tais pulsos são aplicados reflete
diretamente na direção a qual o motor gira. A velocidade que o rotor gira é dada pela
frequência de pulsos recebidos. O número de passos é dado pelo número de
alinhamentos possíveis entre o rotor e as bobinas. A energização de uma bobina de
cada vez produz um deslocamento no rotor (BRITOS; SANTOS, 2008).
      Quando se deseja que o motor rode tanto para um sentido quanto para outro
utiliza-se a Ponte H, circuito construído por quatro "chaves" (S1-S4), acionadas de
forma alternada (S1 e S4 ou S2 e S3), onde cada configuração das chaves faz o
motor girar em um sentido (BRITOS; SANTOS, 2008).

    2.4.   Microcontrolador 8051
      O microcontrolador é um dispositivo semicondutor em forma de circuito
integrado (CI), que contém as partes básicas de um microcomputador, são elas:
unidade central de processamento (CPU), unidade de memória e unidade de
entrada e saída (E/S) (GIMENEZ, 2002).

                                                                                   4


[PAGINA 5]
      O microcontrolador 8051 pode ser reprogramado por software, sem a
necessidade de retirar o chip do circuito. O programa executável fica alojado na
memória ROM (Read-Only Memory), portanto, este armazena as instruções a serem
executadas e dados fixos cujo programa acessará, sendo usado apenas para fazer
leitura dos dados. A memória RAM (Random-Access Memory) é destinada à
manipulação dos dados, realiza o armazenamento temporário dos dados
(NICOLOSI; BRONZERI, 2005).

3. MATERIAIS E MÉTODOS

      Para a elaboração da hipótese, projetou-se a mesa coordenada controlada
por um CNC com dois eixos (XY), os quais se deslocam em um plano horizontal e
são acionados por dois motores de passo CC (Corrente Contínua). A tabela 01
apresenta os materiais utilizados. O Apêndice A apresenta os valores aproximados
dos materiais usados para construção do protótipo.
          Componente da mesa                                Material
                                      Compensado de madeira MDF de 84x49 cm e 15
      Base da mesa
                                      mm de espessura.
                                      Compensado de madeira MDF de 06 mm de
      Plataforma do papel
                                      espessura. Área útil para impressão 25x22 cm.
                                      Motores de passo CC usados em scanner. Modelo:
      Movimentação dos eixos
                                      M35SP-7
      Cabeça de impressão             Solenóide.
                                      Bipolar Stepper Motor Driver e Ponte H L298.
      Drivers
                                      Adicionais: L297, ULN2003AN.
                                      02 chapas de metal para sustentar o eixo de
      Eixo Y (colunas)
                                      digitalização de um scanner.
      Eixo X (linhas)                 02 corrediças de rolamentos.
       Tabela 01: materiais usados para elaboração do hardware da mesa de coordenadas
                                      Fonte: DO AUTOR.

      Para a elaboração do hardware da mesa de coordenadas foi necessário:
         Eixo X: fixado sobre a base da mesa para suporte da plataforma do papel;
          realiza o movimento do papel para impressão das linhas.
         Eixo Y: fixado acima da plataforma do papel, contém a cabeça de
          impressão; realiza o movimento do solenóide para impressão das colunas.
         Projetou-se uma placa de circuito impresso 10x15 cm para gerenciar o
          fornecimento de energia elétrica para os motores e o solenóide; controle
          do sensor fototransistor. O Apêndice B contém o diagrama do circuito.
         Movimentação dos motores: utilizou-se drivers para controle da rotação,
          sentido e clock (frequência) do motor.

                                                                                        5


[PAGINA 6]
         Fornecimento de tensão contínua: utilizou-se fonte de tensão contínua de
          12v para alimentação dos motores, reguladores de tensão foram utilizados
          para que fossem fornecidos 5v aos motores; utilizou-se fonte de tensão
          contínua de 24v para alimentação do solenóide.
         Sensor fototransistor: utilizado para identificar as coordenadas (0,0), ponto
          de origem da impressão.
         Microcontrolador 8051: utilizou-se para controle lógico da mesa, transmitir
          os comandos de movimentação dos eixos e marcar o papel, gerando a
          célula Braille.
      Após o desenvolvimento do hardware, iniciou-se a programação do software.
Utilizou-se a versão gratuita do compilador “MIKROC PRO for 8051” para
desenvolvimento do código-fonte, em linguagem C; este é compilado e transferido
para a memória ROM do microcontrolador 8051.
      Elaboraram-se questionários de múltipla escolha para verificação da hipótese,
foi realizado pesquisas com instituições que atendem deficientes visuais e com
pessoas que utilizam o sistema Braille; realizaram-se testes de legibilidade do
documento produzido pela mesa coordenada. Para a utilização dos questionários
realizou-se a elaboração das perguntas e respostas, amostragem da população,
avaliação das respostas e análise dos resultados.

4. RESULTADOS EXPERIMENTAIS

      Nesta seção, apresentam-se os resultados dos questionários aplicados a
instituições e pessoas que utilizam o sistema Braille e os resultados do produto
impresso produzido pelo protótipo da mesa coordenada, bem como, o teste de
legibilidade do documento.

   4.1.   Questionários
      Realizaram-se pesquisas com instituições que atendem deficientes visuais e
com pessoas que utilizam o sistema Braille de 18/10/2013 à 15/11/2013; dentre a
população alvo obteve-se uma amostra de 8 instituições e uma amostra de 20
pessoas que utilizam o sistema Braille. Sendo a amostra pequena, os resultados não
podem ser generalizados à população alvo, porém estes podem indicar uma
tendência dentre os participantes da pesquisa.



                                                                                     6


[PAGINA 7]
       Dentre as instituições participantes, quatro (04) declararam receber auxilio do
governo brasileiro para a aquisição de impressora Braille; em média adquiriram três
(03) impressoras Braille; todas as instituições participantes demonstraram interesse
na aquisição de uma impressora Braille de baixo custo compatível com a língua
portuguesa. O gráfico 01 apresenta as respostas fornecidas a outras questões do
questionário; no gráfico 01 (a) as respostas correspondem ao nível de 1 a 5.




Questão 1. Classifique a importância de documentos Braille para alfabetização de deficientes visuais.
Questão 2. Classifique a dificuldade de aquisição de impressora Braille.
Questão 3. Classifique a dificuldade de adaptação de impressora Braille com a língua portuguesa.
        Gráfico 01: respostas a pesquisa com instituições que atendem deficientes visuais.
                                         Fonte: DO AUTOR.

       Dentre as pessoas que utilizam o sistema Braille que responderam ao
questionário, constatou-se que os motivos principais para que não adquiram
impressora Braille são: o custo alto e a manutenção cara e/ou de difícil acesso.
Perguntou-se sobre o aprendizado do sistema Braille, a aquisição de impressora
Braille e o interesse na aquisição do equipamento de baixo custo. O gráfico 02
apresenta as respostas fornecidas as questões do questionário.




Questão 1. Aprendeu a ler o sistema Braille durante a alfabetização?
Questão 2. Possui impressora Braille?
Questão 3. É de interesse uma impressora Braille de baixo custo compatível com o português?
            Gráfico 02: respostas a pesquisa com pessoas que utilizam o sistema Braille.
                                      Fonte: DO AUTOR.

    4.2.    Protótipo
       O desenvolvimento do protótipo foi realizado de forma a evitar trepidações da
plataforma do papel, durante a impressão; com isso, gerando estabilidade durante a
impressão do documento Braille e aumentando a precisão da impressão.


                                                                                                    7


[PAGINA 8]
Inicialmente, para controle do eixo X, havia sido utilizado o motor 23LM-C352-15 de
impressora matricial, porém ocorreram trepidações e ruídos elevados, sendo
substituído por um motor de scanner. Durante a marcação do papel, para gerar a
célula Braille, é produzido ruído devido ao impacto direto com a madeira; para
diminuir o ruído, adicionou-se a área útil de impressão um material de microfibra,
diminuindo o impacto entre o solenóide e a plataforma do papel. A figura 03
apresenta fotos do protótipo desenvolvido.




    (a) Visão do microcontrolador 8051, drivers dos
                                                         (b) Visão da cabeça de impressão.
         motores e placa de circuito impresso.




           (c) Visão do eixo Y, solenóide e                (d) Vista do eixo X e corrediças
                 plataforma do papel.                               de rolamentos.
           Figura 03: fotos do protótipo - mesa coordenada CNC para impressão Braille.
                                         Fonte: DO AUTOR.

       O código-fonte, desenvolvido para controle das ações da mesa coordenada,
constitui-se de funções básicas para movimento do eixo X para cima e para baixo,
movimento do eixo Y para a esquerda e para a direita e marcação do papel.
Realizaram-se diversos testes de impressão, foi verificado que o uso de altas
velocidades de rotação prejudica a precisão da movimentação do motor de passo,
interferindo na qualidade da impressão. Configurou-se a mesa coordenada para, ao
inicializar, se posicionar no ponto de origem da impressão; a versão gratuita do
compilador “MIKROC PRO for 8051” limita a criação do código-fonte para 4096
bytes, com isso, mediante acionamento por botão, realiza-se a impressão das
palavras programadas; foi definida a célula Braille para sete (7) letras do alfabeto,


                                                                                              8


[PAGINA 9]
são elas: a, b, n, o, r, s, u; são impressas quatro (4) palavras, uma em cada linha. A
tabela 02 apresenta a transcrição das palavras no sistema Braille.
             Palavra             Braille
               una
                            
              obras
                           
               urso
                            
             banana
                           
            Tabela 02: exemplo das palavras.        Figura 04: resultado da impressão.
                  Fonte: DO AUTOR.                          Fonte: DO AUTOR.

      Realizaram-se testes de legibilidade do documento Braille impresso pela
mesa coordenada de 12/11/2013 à 15/11/2013; pesquisa realizada com pessoas
que utilizam o sistema Braille, dentre a população alvo obteve-se uma amostra de 17
pessoas. A figura 04 apresenta o resultado a impressão.
      Todos os participantes da pesquisa tiveram dificuldades para ler o
documento, os principais motivos alegados foram o espaçamento entre colunas,
células e linhas; os respondentes acharam que havia letras separadas e em alguns
momentos a existência de pontos a mais na célula Braille. O relevo foi considerado
agradável, não ocasionando a sensação de "arranhar" o dedo. O gráfico 03
apresenta as respostas fornecidas as questões do questionário.




       Gráfico 03: respostas ao teste de legibilidade do documento produzido pelo protótipo.
                                        Fonte: DO AUTOR.

      Observa-se que a palavra "una" foi a que menos se conseguiu identificar e a
palavra "banana" foi a que melhor conseguiu-se ler. Erros de leitura motivados pelo
espaçamento, onde a célula Braille definida para a letra “n” foi confundida com o
“sinal de maiúscula” do sistema Braille, o que dificultou a identificação das letras.
      Com isso, identificou-se a necessidade de ajustes no espaçamento do texto
impresso, para melhoria da legibilidade do documento.


                                                                                               9


[PAGINA 10]
5. CONCLUSÃO

      O objetivo deste estudo foi alcançado, sendo realizado o desenvolvimento do
protótipo de uma mesa coordenada CNC para escrita Braille de grau um, com foco
na língua portuguesa.
      Concluiu-se com as pesquisas realizadas com instituições que atendem
deficientes visuais e com pessoas que utilizam o sistema Braille, que de fato o
sistema Braille é considerado muito importante durante a alfabetização de
deficientes visuais; e que a aquisição de equipamento para produção de
documentos Braille é difícil, assim como a adaptação do equipamento, sendo
verificada uma tendência entre os respondentes. Identificou-se um interesse
expressivo pelo protótipo produzido.
      Verificou-se que a mesa coordenada desenvolvida apresenta estabilidade,
não ocorrendo trepidações que interfiram na precisão do equipamento; apta a
produção em pequeno porte de conteúdo impresso em Braille.
      Durante o teste de legibilidade do documento impresso, observou-se
dificuldade para leitura das palavras impressas, portanto, se faz necessária a
adaptação do código-fonte, modificando a movimentação realizada pelos motores de
passo; diante disto, é possível melhorar a impressão, pois, o equipamento
desenvolvido é capaz de realizar movimentos precisos. Durante o desenvolvimento
do software não foi possível implementar mais do que sete (07) letras para geração
de palavras, devido a limitação de 4096 bytes de memória de código-fonte
disponibilizados pela versão gratuita do compilador, o que impossibilitou a geração
de palavras variadas, necessário para a realização de teste de legibilidade completo.
      Para trabalhos futuros, com relação ao software pode ser aprimorado o
código-fonte, realizando a inserção de todos os símbolos do sistema Braille, sendo
necessária a aquisição da licença do compilador “MIKROC PRO for 8051”. Tem-se,
também, o desenvolvimento da comunicação via porta serial, fazendo uso do
protocolo SPI, onde se realiza a transferência de um documento de texto a ser
transcrito para Braille e impresso. Sugere-se o desenvolvimento de uma adaptação
no hardware para que seja realizado o reconhecimento de caracteres transcritos em
um documento Braille. Propõe-se, também, o desenvolvimento do software para a
impressão de gráficos e figuras geométricas em relevo.



                                                                                  10


[PAGINA 11]
6. REFERÊNCIAS BIBLIOGRÁFICAS

  BORGES, José Antonio dos Santos; CHAGAS JÚNIOR, Geraldo José Ferreira.
  Impressão Braille no Brasil: o papel do Braivox, Braille Fácil e Pintor Braille. Rio
  de Janeiro: Núcleo de Computação Eletrônica, UFRJ, 2010.


  BRITOS, Felipe Gonçalves; SANTOS, Vinicius Puga de Almeida. Motor de
  Passo. Universidade Federal Fluminense. Niterói: Escola de Engenharia, 2008.


  CERQUEIRA, Jonir Bechara et. al. Grafia Braille para a Língua Portuguesa.
  Ministério da Educação. Secretaria de Educação Especial. Brasília: SEESP,
  2006.


  GARCIA, Carla Cristina. Sociologia da Acessibilidade. Curitiba: IESDE Brasil
  S.A., 2008.


  GIMENEZ, Salvador Pinillos. Microcontroladores 8051: Teoria do hardware e
  do software / Aplicações em controle digital / Laboratório e simulação. São Paulo:
  Pearson Prentice Hall, 2002.


  NICOLOSI,     Denys     Emílio    Campion;       BRONZERI,     Rodrigo    Barbosa.
  Microcontrolador 8051 com linguagem C: prático e didático – família
  AT89S8252 Atmel. São Paulo: Érica, 2005.


  QUEIROZ, Marcelo Torres. Automação de mesa coordenada destinada à
  máquina fresadora CNC. Universidade Federal Fluminense. Niterói: Escola de
  Engenharia Mecânica, 2007.


  SOUZA, Adriano Fagali de; ULBRICH, Cristiane Brasil Lima. Engenharia
  integrada por computador e sistemas CAD/CAM/CNC – princípios e
  aplicações. São Paulo: Artliber Editora, 2009.




                                                                                   11


[PAGINA 12]
                                      APÊNDICE A

      A tabela 03 apresenta os valores aproximados dos materiais utilizados na
construção do protótipo. Sendo o custo de material aproximado de R$ 572,40, sem
considerar o valor dos scanners e do compensado de madeira MDF adquiridos por
doação.

                       Material                     Valor aproximado Qnt.        Preço
      Motor de passo                                          R$ 18,40 2         R$ 36,80
      Driver L297                                             R$ 13,00 1         R$ 13,00
      Circuito Integrado 74HC08                                R$ 5,00 1          R$ 5,00
      Driver ULN2003AN                                         R$ 5,00 1          R$ 5,00
      Circuito Integrado LM7805                                R$ 4,50 1          R$ 4,50
      Circuito Integrado LM7812                                R$ 4,50 1          R$ 4,50
      Resistor 1 Ohm                                           R$ 1,30 4          R$ 5,20
      Resistor 220 Ohms                                        R$ 0,10 3          R$ 0,30
      Resistor 10000 Ohms                                      R$ 0,10 4          R$ 0,40
      Resistor 1000 Ohms                                       R$ 0,10 3          R$ 0,30
      Led                                                      R$ 0,40 1          R$ 0,40
      Potenciômetro 22000 Ohms                                 R$ 1,00 1          R$ 1,00
      Driver Ponte H - L298                                   R$ 34,00 1         R$ 34,00
      Bipolar Stepper Motor Driver                            R$ 76,00 1         R$ 76,00
      Placa Circuito Impresso 10x15 cm                        R$ 10,00 1         R$ 10,00
      Conector Molex 5 vias                                    R$ 2,50 2          R$ 5,00
      Relé 12v                                                 R$ 3,00 3          R$ 9,00
      Solenóide 24v                                           R$ 20,00 1         R$ 20,00
      Conector P2 fêmea                                        R$ 1,00 2          R$ 2,00
      Corrediças de rolamentos                                R$ 11,00 2         R$ 22,00
      Compensado de madeira MDF 85x60 cm*                         R$ - 1             R$ -
      Fonte de tensão continua 24v                            R$ 34,00 1         R$ 34,00
      Fonte de tensão continua 12v                            R$ 34,00 1         R$ 34,00
      Scanner *                                                   R$ - 2             R$ -
      Kit Microcontrolador 8051                              R$ 250,00 1        R$ 250,00
                                            Total                               R$ 572,40
      * - doação.
       Tabela 03: valores aproximados dos materiais utilizados na construção do protótipo.
                                     Fonte: DO AUTOR.




                                                                                             12


[PAGINA 13]
                                 APÊNDICE B

      Diagrama do circuito de controle do motor inferior pelo driver L298 e L297,
controle do solenóide, controle dos sensores fototransistores e uso do ULN2003AN
para realizar o controle de pulso, evitando que o microcontrolador 8051 receba
correntes superiores as suportadas, realiza o acoplamento entre o microcontrolador
8051, os reles, e o solenóide.




                                                                               13


[PAGINA 14]
                                               ANEXO A

1. Alfabeto Braille
  a       b               c       d        e        f       g       h       i       j

          
  k           l       m           n        o        p       q       r       s       t

          
  u       v           w            x       y        z       ç

       
  á       é               í       ó        ú        à       è       â       ê       ô

          
  ã       õ               ï       ü

    
2. Elementos textuais
  ,       ;           :           .„       ?        !       -       _           “   *

       
  <       >           &           /        |        (       )       [           ]


3. Sinais usados com números
      €           $           %        §        =       +       -       x       

    
4. Sinais exclusivos da escrita Braille
maiúscula número

       



                                                                                        14
