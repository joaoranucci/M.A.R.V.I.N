# O_GUIA_PRATICO_DO_VISUAL_BASIC_2010

Arquivo original: most_similar_papers_to_this_one/O_GUIA_PRATICO_DO_VISUAL_BASIC_2010.pdf
SHA-256 do original: 57bfe24e0ebe38e2fdf71c13987e060041aa29f6c4a6f9a53d2e51b6083eb08b

Texto extraido para consulta. As paginas abaixo usam a ordem do arquivo PDF, incluindo capas.
Parte preparada: 1/1


[PAGINA 1]


[PAGINA 2]


[PAGINA 3]
VÍ TOR PEREI RA




   Portugal/ 2010


[PAGINA 4]
’Microsoft’ is a registered trademark of Microsoft Corporation in the United States
and/or other countries and is used by Centro Atlântico under license from owner. ‘O
Guia Prático do Visual Basic 2010’ is an independent publication not affiliated with
Microsoft Corporation.


Reservados todos os direitos por Centro Atlântico, Lda.
Qualquer reprodução, incluindo fotocópia, só pode ser feita com autorização expressa dos editores da obra.




O GUIA PRÁTICO DO VISUAL BASIC 2010
Colecção: Tecnologias
Autor:           Vítor Emanuel Pereira


Direcção gráfica: Centro Atlântico
Revisão técnica: Centro Atlântico
Capa: Paulo Buchinho


© Centro Atlântico, Lda., 2010
   Ap. 413
   4764-901 V. N. Famalicão
Portugal
Tel. 808 20 22 21


geral@centroatlantico.pt
www.centroatlantico.pt


Impressão e acabamento: Papelmunde
1ª edição: Junho de 2010
ISBN: 978-989-615-092-1
Depósito legal:        /10




Marcas registadas: Todos os termos mencionados neste livro conhecidos como sendo marcas
registadas de produtos e serviços foram apropriadamente capitalizados. A utilização de um ter-
mo neste livro não deve ser encarada como afectando a validade de alguma marca registada
de produto ou serviço.
O Editor e os Autores não se responsabilizam por possíveis danos morais ou físicos causados
pelas instruções contidas no livro nem por endereços Internet que não correspondam às Home-
-Pages pretendidas.


[PAGINA 5]
                                                                                                    Índice
PREFÁCIO                                                                                                            13
Introdução .......................................................................................................... 13
Público-alvo e Pré-requisitos ................................................................................. 14
Características Principais ...................................................................................... 14
Convenções Usadas ............................................................................................. 15
Visão Geral e Organização ................................................................................... 16

SOBRE O AUTOR                                                                                                       19



PARTE I: Introdução e Visão Geral

1      O MICROSOFT VISUAL BASIC 2010                                                                                23
1.1               Introdução ......................................................................................... 23
1.2               Novidades do Visual Studio 2010 ..................................................... 24
1.3               Outras Características do Visual Studio ........................................... 29
1.4               Instalação e Configuração ................................................................ 37
1.5               A Plataforma .NET ............................................................................ 39
1.6               Resumo ............................................................................................ 41
1.7               Exercícios Propostos ........................................................................ 42

2      O AMBIENTE DE DESENVOLVIMENTO INTEGRADO                                                                      43
2.1               Visão Geral do IDE ........................................................................... 43
2.2               Menus ............................................................................................... 46
2.3               Barras de Ferramentas ..................................................................... 54
2.4               As Janelas do IDE ............................................................................ 55
2.5               Resumo ............................................................................................ 59
2.6               Exercícios Propostos ........................................................................ 60

3      VISÃO GERAL DO VISUAL BASIC                                                                                  61
3.1               O Primeiro Programa ........................................................................ 61
3.2               Visão Geral do Visual Basic.............................................................. 65
3.3               Estruturas Básicas da Programação: Decisões e Repetições .......... 68
3.4               Interacção com o Utilizador em Modo de Consola............................ 72
3.5               Resumo ............................................................................................ 73
3.6               Exercícios Propostos ........................................................................ 73


[PAGINA 6]
6                         CENTRO ATLÂNTICO – COLECÇÃO TECNOLOGIAS – O GUIA PRÁTICO DO VISUAL BASIC 2010



PARTE II: O Visual Basic

4      TIPOS DE DADOS                                                                                                        77
4.1            Aplicações do Computador e Tipos de Dados .................................. 77
4.2            Introdução às Variáveis..................................................................... 79
4.3            Tipos de Dados ................................................................................. 80
       4.3.1   Numéricos Inteiros e Não inteiros ................................................................ 81
       4.3.3   Caracteres ................................................................................................... 84
       4.3.4   Booleanos .................................................................................................... 85
       4.3.5   Datas............................................................................................................ 86
       4.3.6   O tipo Object ................................................................................................ 86
       4.3.7   Estruturas..................................................................................................... 88
       4.3.8   Enumerações ............................................................................................... 90
4.4            Operações Básicas ........................................................................... 92
4.5            Conversões entre tipos de dados...................................................... 93
       4.5.1   Conversões Por Promoção e Despromoção................................................ 94
       4.5.2   Quando usar conversões com despromoção .............................................. 95
       4.5.3   Funções de Conversão de Tipos de Dados ................................................. 95
4.6            Resumo............................................................................................. 97
4.7            Exercícios Propostos ........................................................................ 98

5      VARIÁVEIS E LITERAIS                                                                                                  99
5.1            Elementos da Programação .............................................................. 99
5.2            Declaração de Variáveis ................................................................. 100
5.3            Nomes dos Elementos da Programação......................................... 103
5.4            Âmbito das Variáveis ...................................................................... 104
5.5            Literais ............................................................................................ 107
5.6            Operador Atribuição e Expressões ................................................. 109
5.7            Precedência de Operadores e Avaliação de Expressões ............... 111
5.8            Opções do Compilador ................................................................... 112
       5.8.1   Option Explicit ............................................................................................ 113
       5.8.2   Option Strict ............................................................................................... 114
       5.8.3   Option Compare......................................................................................... 115
       5.8.4   Option Infer ................................................................................................ 116
5.9            Resumo........................................................................................... 117
5.10           Exercícios Propostos ...................................................................... 117

6      OPERADORES                                                                                                         119
6.1            Introdução ....................................................................................... 119
6.2            Aritméticos ...................................................................................... 120
6.3            Relacionais ..................................................................................... 126
6.4            Lógicos e Bit a Bit ........................................................................... 129


[PAGINA 7]
ÍNDICE                                                                                                                   7


6.5              Atribuição ........................................................................................ 133
6.6              Deslocamento ................................................................................. 136
6.7              Concatenação................................................................................. 138
6.8              Introdução às Funções Predefinidas............................................... 139
6.9              Precedência e Associatividade ....................................................... 140
6.10             Resumo .......................................................................................... 144
6.11             Exercícios Propostos ...................................................................... 144

7        DECISÕES                                                                                                147
7.1              Introdução às Estruturas de Decisão .............................................. 147
7.2              A Declaração If...Then...Else .......................................................... 148
         7.2.1   Alternativas Múltiplas: ElseIf ...................................................................... 151
         7.2.2   Declarações If...Then...Else Encadeadas .................................................. 153
7.3              A Declaração Select Case .............................................................. 156
7.4              Resumo .......................................................................................... 161
7.5              Exercícios Propostos ...................................................................... 161

8        REPETIÇÕES                                                                                              163
8.1              Introdução às Estruturas de Repetição ........................................... 163
8.2              Ciclo For...Next ............................................................................... 164
8.3              Ciclos Do Loop ............................................................................... 171
8.4              Ciclo For Each...Next ...................................................................... 176
8.5              Conceito de Iteração, Contador e Acumulador ............................... 178
8.6              Ciclos Encadeados ......................................................................... 180
8.7              Ciclos Infinitos................................................................................. 181
8.8              Resumo .......................................................................................... 182
8.9              Exercícios Propostos ...................................................................... 182

9        SUBROTINAS E FUNÇÕES                                                                                    185
9.1              Dividir, Reutilizar e Abstrair ............................................................. 186
9.2              Dois Tipos de Métodos: Subrotinas e Funções .............................. 186
9.3              Subrotinas....................................................................................... 188
9.4              Funções .......................................................................................... 191
9.5              Escolha de Nomes de Métodos ...................................................... 198
9.6              Correspondência Argumentos-Parâmetros..................................... 199
9.7              Passagem por Valor e por Referência ............................................ 200
9.8              Parâmetros Opcionais .................................................................... 203
9.9              Vector de Elementos Opcionais ...................................................... 205
9.10             Sobrecarga de Métodos.................................................................. 208
9.11             Funções Recursivas ....................................................................... 209
9.12             Resumo .......................................................................................... 212
9.13             Exercícios Propostos ...................................................................... 212


[PAGINA 8]
8                             CENTRO ATLÂNTICO – COLECÇÃO TECNOLOGIAS – O GUIA PRÁTICO DO VISUAL BASIC 2010


10 VECTORES                                                                                                                215
10.1               Vectores .......................................................................................... 215
       10.1.1 Introdução .................................................................................................. 216
       10.1.2 Vectores e Ciclos ....................................................................................... 217
10.2               A classe Array ................................................................................. 224
10.3               Redimensionar Vectores ................................................................. 230
10.4               Matrizes .......................................................................................... 234
10.5               Jagged Arrays ................................................................................. 238
10.6               Resumo........................................................................................... 241
10.7               Exercícios Propostos ...................................................................... 242

11 STRINGS                                                                                                                 243
11.1               Informação sobre Caracteres .......................................................... 243
11.2               Operações Básicas ......................................................................... 246
11.3               A Classe String ............................................................................... 252
11.4               Acesso aos Caracteres ................................................................... 256
11.5               Criar Strings .................................................................................... 259
11.6               Remover Caracteres ....................................................................... 260
11.7               Comparar Strings ............................................................................ 262
11.8               Outras Operações Comuns............................................................. 266
11.9               O Operador Like.............................................................................. 267
11.10              A Classe StringBuilder .................................................................... 269
11.11              Resumo........................................................................................... 276
11.12              Exercícios Propostos ...................................................................... 276

12 TRATAMENTO DE ERROS E DEBUGGING                                                                                         279
12.1               Tipos de Erros ................................................................................. 279
       12.1.1 Erros de Sintaxe ........................................................................................ 280
       12.1.2 Erros de Lógica .......................................................................................... 282
       12.1.3 Erros de Execução..................................................................................... 282
12.2               Exercício Prático de Tratamento de Erros....................................... 284
12.3               Resumo........................................................................................... 294
12.4               Exercícios Propostos ...................................................................... 295

13 PROGRAMAÇÃO ORIENTADA AOS OBJECTOS                                                                                      297
13.1               Introdução ....................................................................................... 297
13.2               Conceitos Básicos........................................................................... 302
       13.2.1      Classes e Objectos .................................................................................... 302
       13.2.2      Níveis de Acesso ....................................................................................... 304
       13.2.3      Propriedades.............................................................................................. 305
       13.2.4      Métodos ..................................................................................................... 307
       13.2.5      Membros Partilhados ................................................................................. 309


[PAGINA 9]
ÍNDICE                                                                                                                        9


         13.2.6 Construtores .............................................................................................. 310
         13.2.7 Sobrecarga de Métodos ............................................................................ 313
         13.2.8 Redefinição de Operadores ....................................................................... 314
13.3                Desenvolvimento de uma Classe.................................................... 316
13.4                Membros Genéricos........................................................................ 320
13.5                Resumo .......................................................................................... 325
13.6                Exercícios Propostos ...................................................................... 325




PARTE III: A Plataforma .NET

14 O ESPAÇO DE NOMES SYSTEM                                                                                           329
14.1                Estruturas dos Tipos de Dados Básicos ......................................... 329
         14.1.1 As Estruturas de Inteiros ........................................................................... 330
         14.1.2 As Estruturas de Vírgula Flutuante ............................................................ 332
         14.1.3 A Estrutura Decimal ................................................................................... 334
14.2                A classe Object ............................................................................... 334
14.3                A estrutura Char ............................................................................. 336
14.4                A estrutura DateTime ...................................................................... 339
14.5                A classe Math ................................................................................. 343
14.6                A classe Random ............................................................................ 347
14.7                Resumo .......................................................................................... 352
14.8                Exercícios Propostos ...................................................................... 352

15 LANGUAGE-INTEGRATED QUERY (LINQ)                                                                                   355
15.1                O espaço de nomes System.Linq ................................................... 355
15.2                A sintaxe de uma consulta LINQ..................................................... 356
15.3                A cláusula Select ............................................................................ 357
         15.3.1 A cláusula Select com transformação........................................................ 359
15.4                A cláusula Where ............................................................................ 360
15.5                Agregação de dados ....................................................................... 362
         15.5.1 Agregação com condições ........................................................................ 363
         15.5.2 Agregação com strings .............................................................................. 365
15.6                Eliminar valores repetidos............................................................... 367
15.7                Operadores de Conversão.............................................................. 368
15.8                Operadores de Elementos .............................................................. 369
15.9                Ordenação ...................................................................................... 372
15.10               Agrupamento de dados................................................................... 374
15.11               Resumo .......................................................................................... 378
15.12               Exercícios Propostos ...................................................................... 379


[PAGINA 10]
10                          CENTRO ATLÂNTICO – COLECÇÃO TECNOLOGIAS – O GUIA PRÁTICO DO VISUAL BASIC 2010


16 COLECÇÕES                                                                                                         381
16.1             Espaços de nomes sobre Colecções .............................................. 381
16.2             A classe List .................................................................................... 384
16.3             A classe BitArray ............................................................................. 387
16.4             A classe Queue ............................................................................... 393
16.5             A classe Stack................................................................................. 396
16.6             As classes Dictionary e SortedDictionary ........................................ 401
16.7             A classe SortedList ......................................................................... 410
16.8             A classe LinkedList ......................................................................... 412
16.9             A classe HashSet ............................................................................ 415
16.10            Resumo........................................................................................... 421
16.11            Exercícios Propostos ...................................................................... 422

17 STREAMS                                                                                                           423
17.1             O espaço de nome System.IO ........................................................ 423
17.2             A classe System.IO.Stream ............................................................ 427
17.3             Redireccionar os “Standard Streams” ............................................. 429
17.4             As classes StreamReader e StreamWriter ...................................... 431
17.5             As classes StringReader e StringWriter .......................................... 435
17.6             As classes BinaryReader e BinaryWriter......................................... 437
17.7             Acesso Directo a Ficheiros.............................................................. 440
17.8             Resumo........................................................................................... 444
17.9             Exercícios Propostos ...................................................................... 445




PARTE IV: Aplicações Windows

18 DESENHO DA INTERFACE GRÁFICA                                                                                      449
18.1             A Caixa de Ferramentas (Toolbox) ................................................. 449
18.2             Visão Geral dos Controlos .............................................................. 451
       18.2.1    Aba Common Controls ............................................................................... 452
       18.2.2    Aba Containers .......................................................................................... 454
       18.2.3    Aba Menus & Toolbars .............................................................................. 455
       18.2.4    Restantes Abas.......................................................................................... 456
18.3             Aplicações Windows: Primeiro Exemplo ......................................... 456
18.4             Interacção com o Utilizador em Windows ....................................... 463
18.5             Desenho da GUI: Apresentação de boas práticas .......................... 463
18.6             Propriedades dos Controlos............................................................ 464
18.7             Projecto em Visual Basic: Gestão de Filmes................................... 467
       18.7.1 Desenho da Interface Gráfica .................................................................... 469


[PAGINA 11]
ÍNDICE                                                                                                                         11


18.8                Especificar a Ordem dos Tabs........................................................ 476
18.9                Posicionamento dos Controlos no Form ......................................... 477
18.10               Resumo .......................................................................................... 479
18.11               Exercícios Propostos ...................................................................... 479

19 CONSTRUÇÃO DE UM JOGO                                                                                                 481
19.1                Antevisão do Projecto ..................................................................... 481
19.2                Controlos Utilizados ........................................................................ 484
19.3                Controlos RadioButton, CheckBox e GroupBox.............................. 484
19.4                Controlos ListBox e ComboBox ...................................................... 486
19.5                Controlos NumericUpDown e ToolTip............................................. 488
19.6                Projecto em Visual Basic: Jogo ‘Adivinha o Número’...................... 489
         19.6.1 Desenho da Interface Gráfica .................................................................... 489
         19.6.2 Adicionar Código aos Eventos ................................................................... 492
19.7                Resumo .......................................................................................... 496
19.8                Exercícios Propostos ...................................................................... 496

20 CRIAÇÃO DE UM EDITOR DE TEXTO                                                                                         497
20.1                Antevisão do Projecto ..................................................................... 497
20.2                Caixas de Diálogo Predefinidas ...................................................... 499
20.3                Caixa de Diálogo MessageBox ....................................................... 500
         20.3.1     Botões disponíveis..................................................................................... 501
         20.3.2     Ícones disponíveis ..................................................................................... 502
         20.3.3     Botão por omissão ..................................................................................... 503
         20.3.4     Valor retornado .......................................................................................... 503
         20.3.5     Exemplos de Utilização ............................................................................. 503
20.4                Caixa de Diálogo ColorDialog ......................................................... 504
20.5                Caixa de Diálogo FontDialog .......................................................... 505
20.6                Caixas de Diálogo OpenFileDialog e SaveFileDialog ..................... 505
20.7                Projecto em Visual Basic: Bloco de Notas ...................................... 507
         20.7.1 Desenho da Interface Gráfica .................................................................... 507
         20.7.2 Adicionar Código aos Eventos ................................................................... 507
         20.7.3 Explicação do Código ................................................................................ 511
20.8                Resumo .......................................................................................... 514
20.9                Exercícios Propostos ...................................................................... 515

21 CONSTRUÇÃO DE UM WEB BROWSER                                                                                          517
21.1                Antevisão do Projecto ..................................................................... 517
21.2                Controlos utilizados......................................................................... 518
21.3                Projecto em Visual Basic: Web Browser ......................................... 519
         21.3.1 Criar um Splash Screen............................................................................. 520
         21.3.2 Adicionar uma Barra de Menus ................................................................. 522


[PAGINA 12]
12                           CENTRO ATLÂNTICO – COLECÇÃO TECNOLOGIAS – O GUIA PRÁTICO DO VISUAL BASIC 2010


       21.3.3 Adicionar e Chamar uma Janela Ajuda > Sobre ........................................ 523
       21.3.4 Adicionar outros Controlos ......................................................................... 525
       21.3.5 Configurar o Controlo ToolStrip ................................................................. 526
       21.3.6 Configurar o Controlo StatusStrip .............................................................. 527
       21.3.7 Inserir o código para navegar em múltiplas abas ...................................... 528
       21.3.8 Navegar pela primeira vez ......................................................................... 530
       21.3.9 Adicionar mais Opções de Menu ............................................................... 531
       21.3.10 Adicionar um Menu de Contexto ................................................................ 536
21.4              Resumo........................................................................................... 538
21.5              Exercícios Propostos ...................................................................... 538

22 INTRODUÇÃO ÀS BASES DE DADOS                                                                                       539
22.1              Antevisão do Projecto ..................................................................... 540
22.2              Conceitos, Regras e Terminologia básica ....................................... 540
22.3              Componentes de acesso a Bases de Dados .................................. 543
22.4              Projecto em Visual Basic: Gestão de Contactos ............................. 544
       22.4.1     Criar uma Base de Dados .......................................................................... 545
       22.4.2     Ligar uma Aplicação a uma Base de Dados .............................................. 548
       22.4.3     Visualizar Dados ........................................................................................ 550
       22.4.4     Actualizar Dados ........................................................................................ 552
22.5              Resumo........................................................................................... 554
22.6              Exercícios Propostos ...................................................................... 554

23 PROGRAMAÇÃO DE BASES DE DADOS COM ADO.NET 557
23.1              Base de Dados................................................................................ 557
       23.1.1 Base de Dados Microsoft Access .............................................................. 558
       23.1.2 Base de Dados em SQL Server ................................................................. 559
23.2              Ler dados com a classe DataReader .............................................. 561
23.3              Ler dados com a classe DataSet .................................................... 565
23.4              Actualizar dados.............................................................................. 567
23.5              Inserir novas Linhas ........................................................................ 569
23.6              Procurar Linhas ............................................................................... 571
23.7              Eliminar Linhas................................................................................ 573
23.8              Resumo........................................................................................... 575
23.9              Exercícios Propostos ...................................................................... 575


[PAGINA 13]
                                                               Prefácio




Introdução
O Visual Studio 2010 é o sucessor do Visual Studio 2008 e também o principal
ambiente de desenvolvimento integrado da Microsoft. Lançado em simultâneo
com a versão 4.0 da plataforma .NET, está disponível em diversas edições,
incluindo a versão Express, que é grátis (confira as condições de utilização em
http://www.microsoft.com/express/).
Esta nova versão do Visual Studio é, sem qualquer margem para dúvida, uma
evolução inteligente na disponibilização de ferramentas poderosas e de classe
indiscutível para que cada vez mais programadores conheçam o fascinante
mundo da programação.
Assim, é seguro afirmar que nunca houve melhor altura para aprender a pro-
gramar um computador, tanto a nível de simplicidade como de funcionalidades
disponibilizadas. Por outro lado, nunca a necessidade de programação de
computadores foi tão necessária e apreciada: desde as mais pequenas rotinas
diárias que facilitam a nossa vida quotidiana, passando pelos aspectos profis-
sionais em todas as áreas da sociedade, até aos momentos de descanso e
lazer.
O Visual Basic é a linguagem de programação mais popular a nível mundial.
Contudo, não se deixe enganar pelo nome: o Visual Basic (‘basic’ significa
‘básico’) não é uma ferramenta de demonstração ou uma versão para desen-
volver aplicações de qualidade ou funcionalidade limitada. É uma poderosa
ferramenta que permite, entre outros, a criação de aplicações para o Win-
dows e de bibliotecas de código reutilizável (ficheiros .DLL). É perfeitamente
adequada para aquelas pessoas que desejam aprender a programar mas
também para programadores experientes, com o objectivo de desenvolver
software com utilidade prática e de forma simples e rápida.


[PAGINA 14]
14                   CENTRO ATLÂNTICO – COLECÇÃO TECNOLOGIAS – O GUIA PRÁTICO DO VISUAL BASIC 2010



Público-alvo e Pré-requisitos
Este livro é para todos aqueles que se interessam pela programação de com-
putadores.
Por um lado, estudantes que necessitam de uma obra de qualidade que cubra,
de forma didáctica, e desde os aspectos mais básicos, o Visual Basic.
Por outro lado, actuais programadores de Visual Basic e/ou de outras lingua-
gens de programação que pretendam consolidar conhecimentos e aprofundar
aspectos mais avançados como, por exemplo, as consultas LINQ.
Por último, aprendizes de programadores ou mesmo aquelas pessoas que
sempre pensaram que a programação era algo demasiado difícil e exclusivo
dos profissionais.
Para a leitura deste livro não são necessários quaisquer requisitos prévios ao
nível de linguagens de programação de computadores. O único conhecimento
necessário é o da utilização de aplicações de computadores, mais concreta-
mente de programas em ambiente Windows como, por exemplo, as aplicações
do Microsoft Office.
No entanto, caso o leitor pertença ao grupo de pessoas que já possui alguns
conhecimentos sobre linguagens de programação, por exemplo, tendo já pro-
gramado em versões anteriores do Visual Basic, então a transição para o
Visual Basic 2008 deverá ser consideravelmente mais simples, podendo, mais
rapidamente, começar a utilizar funcionalidades mais avançadas.



Características Principais
Estruturado de forma pedagógica, este livro inclui diversas características
pensadas para que a programação de computadores seja simultaneamente
divertida e prática. Algumas das principais características deste livro incluem:
     Praticamente todos os capítulos apresentam inúmeros exercícios práti-
        cos, com diversas variantes, que o leitor pode reproduzir e que o aju-
        dam a compreender o alcance dos tópicos abordados;
     A Parte I lista as principais características do Visual Basic/Visual Stu-
        dio e faz uma breve apresentação dos menus e janelas principais. É
        também dada uma visão geral do Visual Basic em diversos exercícios
        práticos;
     A Parte II, composta por dez capítulos, apresenta um enquadramento
        sobre os conceitos básicos da programação de computadores, desde
        tipos de dados até conceitos mais avançados, como a programação
        orientada aos objectos;
     Na Parte III são abordadas funcionalidades avançadas da plataforma
        .NET, designadamente o espaço de nomes System, as consultas


[PAGINA 15]
PREFÁCIO                                                                        15


           LINQ, as estruturas de dados do tipo colecções e ainda o conceito de
           streams;
          Na Parte IV, os capítulos de desenvolvimento de aplicações completas
           apresentam, como primeira secção, uma «Antevisão do Projecto», que
           resume o funcionamento básico pretendido;
          Os ficheiros dos exemplos práticos encontram-se disponíveis para os
           leitores. Veja na página 20 como pode ter acesso a esses ficheiros.
          Todos os capítulos terminam com um Resumo que sumaria os princi-
           pais pontos abordados, bem assim como diversos Exercícios Propos-
           tos, para que o leitor possa passar da teoria à prática e testar os seus
           conhecimentos.



Convenções Usadas
Este livro utiliza diversas convenções com vista a facilitar a assimilação da
informação:
     Palavras-chave, importantes para a compreensão do assunto a tratar,
        ou então valores a introduzir pelo leitor, são identificados a negrito:
        «Esta prática designa-se por abstracção.»
        «Atribua o texto Operadores Atribuição e o nome btnAtribuir.»
     Termos em inglês ou nomes específicos ao Visual Basic são
        apresentados, de uma forma geral, em itálico (com excepção de con-
        ceitos que deverão ser familiares):
        «De forma idêntica ao Splash Screen, seleccione...»
        «Seleccione o form e aceda à janela de Propriedades.»
     O acesso a opções de menus é formatado em letras maiúsculas
        pequenas. O carácter ">" é utilizado para separar o menu da opção:
        «...seleccione PROJECT > ADD W INDOWS FORM…»
     O código em Visual Basic encontra-se formatado com o tipo de dados
        Consolas:

               Dim extenso() As String = {"zero", "um", "dois", "três",
                     "quatro", "cinco", "seis", "sete", "oito", "nove"}


          Combinações de teclas são identificadas através do carácter "+". Por
           exemplo, Ctrl+Espaço significa manter pressionada a tecla "Control"
           e, de seguida, premir a barra de espaços, soltando de seguida as duas
           teclas.


[PAGINA 16]
16                   CENTRO ATLÂNTICO – COLECÇÃO TECNOLOGIAS – O GUIA PRÁTICO DO VISUAL BASIC 2010



Visão Geral e Organização
Este livro está dividido em vinte e três capítulos, organizados em quatro par-
tes.

A Parte I: Introdução e Visão Geral consiste nos primeiros três capítulos.
    Capítulo 1 – O Microsoft Visual Basic 2010. Este capítulo faz uma
       apresentação do binómio constituído pelo Visual Basic 2010 Express e
       pela plataforma .NET.
    Capítulo 2 – O Ambiente de Desenvolvimento Integrado. Apresenta
       a «bancada laboratorial» onde iremos desenvolver os nossos progra-
       mas, experimentando-os antes de os distribuir ao grande público.
    Capítulo 3 – Visão Geral do Visual Basic. Apresenta uma visão geral
       do Visual Basic através de diversos programas simples.


A Parte II: O Visual Basic apresenta os conceitos básicos da programação
em Visual Basic em dez capítulos.
    Capítulo 4 – Tipos de Dados. Aborda os tipos de dados do Visual
       Basic, o conceito de variável e os diversos tipos de conversões exis-
       tentes.
    Capítulo 5 – Variáveis e Literais. Apresenta a sintaxe usada na
       declaração de variáveis, bem como os diversos âmbitos existentes, e
       ainda o tipo de dados associado aos literais. Descreve quatro impor-
       tantes opções do compilador do Visual Basic.
    Capítulo 6 – Operadores. Os diferentes tipos de operadores –
       aritméticos, relacionais, lógicos e de atribuição –, para além dos con-
       ceitos de funções predefinidas e de precedência de operadores são
       apresentados neste capítulo.
    Capítulo 7 – Decisões. Descreve as duas estruturas de controlo bási-
       cas de decisão, que permitem que o computador possa executar
       código de forma condicional.
    Capítulo 8 – Repetições. Descreve as estruturas de controlo básicas
       de repetição (ciclos), usadas para se repetir um conjunto de linhas de
       código.
    Capítulo 9 – Subrotinas e Funções. De forma a realçar a importância
       e as vantagens da programação modular, este capítulo aborda os dois
       tipos de métodos existentes: subrotinas e funções, descrevendo os
       seus detalhes de funcionamento.
    Capítulo 10 – Vectores. O tema deste capítulo são os vectores
       (arrays) uni e multidimensionais, para além do conceito de vector
       irregular.


[PAGINA 17]
PREFÁCIO                                                                     17


          Capítulo 11 – Strings. Aborda a manipulação de caracteres e texto
           tanto a nível das suas operações básicas como das existentes na pla-
           taforma .NET. Apresenta as classes String e StringBuilder.
          Capítulo 12 – Tratamento de Erros e Debugging. Apresenta os três
           tipos de erros da programação de computadores: sintaxe, lógica e
           execução. Aborda o debugging, que permite encontrar erros de lógica
           e ‘afinar’ o programa.
          Capítulo 13 – Programação Orientada aos Objectos. Descreve o
           paradigma da programação orientada aos objectos, nomeadamente
           através de exemplos e à luz de conceitos apresentados em capítulos
           anteriores.


A Parte III: A Plataforma .NET aborda diversas classes da plataforma .NET.
Esta parte é composta por quatro capítulos.
    Capítulo 14 – O Espaço de Nomes System. Explora o espaço de
       nomes de nível hierárquico mais alto da plataforma .NET, designada-
       mente as estruturas relativas aos tipos de dados básicos e as classes
       Math e Random.
    Capítulo 15 – Language-Integrated Query (LINQ). Apresenta a
       poderosa característica que adiciona capacidades nativas de consulta
       ao Visual Basic, com sintaxe semelhante à linguagem SQL.
    Capítulo 16 – Colecções. As estruturas de dados do tipo vectores
       dinâmicos, vectores de bits, filas, pilhas, dicionários, listas ligadas e
       conjuntos são descritas neste capítulo.
    Capítulo 17 – Streams. Este capítulo aborda os três tipos de streams
       existentes: bytes, caracteres e binários, para além de distinguir entre
       streams sequenciais e de acesso directo.


A Parte IV: Aplicações Windows aborda a criação de aplicações para o Win-
dows. Esta parte é composta por seis capítulos.
    Capítulo 18 – Desenho da Interface Gráfica. Fornece uma visão
       geral do desenho da interface gráfica, designadamente através da
       criação de uma aplicação com os controlos mais comuns.
    Capítulo 19 – Construção de um Jogo. Ilustra a criação de um jogo
       para adivinhar um número ‘pensado’ pelo computador. Os controlos do
       Windows que permitem ao utilizador seleccionar opções são descritos
       neste capítulo.
    Capítulo 20 – Criação de um Editor de Texto. Ilustra as funcionalida-
       des associadas à utilização de caixas de diálogo predefinidas, um
       conjunto de componentes típicos das aplicações Windows.


[PAGINA 18]
18                    CENTRO ATLÂNTICO – COLECÇÃO TECNOLOGIAS – O GUIA PRÁTICO DO VISUAL BASIC 2010


        Capítulo 21 – Construção de um Web Browser. Cria um Web Brow-
         ser que usa as seguintes características: barras de menu, ferramentas
         e de estado, um splash screen inicial e o controlo que permite navegar
         na Internet.
        Capítulo 22 – Introdução às Bases de Dados. Apresenta os concei-
         tos e a terminologia básica, identifica os componentes de acesso a
         dados e cria uma base de dados, permitindo visualizar e actualizar os
         dados.
        Capítulo 23 – Programação de Bases de Dados com ADO.NET.
         Apresenta as principais classes da plataforma .NET que permitem a
         gestão de uma base de dados relacional. Ilustra a leitura e a actualiza-
         ção de dados, e a inserção e eliminação de linhas.


[PAGINA 19]
