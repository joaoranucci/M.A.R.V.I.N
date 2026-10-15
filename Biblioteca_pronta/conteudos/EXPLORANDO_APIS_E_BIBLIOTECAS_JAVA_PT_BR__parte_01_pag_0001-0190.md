# EXPLORANDO_APIS_E_BIBLIOTECAS_JAVA_PT_BR

Arquivo original: more_papers_by_thyago_louiz/EXPLORANDO_APIS_E_BIBLIOTECAS_JAVA_PT_BR.pdf
SHA-256 do original: b4103eae5ec357e6ea52533b92bb3e0388999b4c305ef873233f4f8d19fd1ea0

Texto extraido para consulta. As paginas abaixo usam a ordem do arquivo PDF, incluindo capas.
Parte preparada: 1/1


[PAGINA 1]


[PAGINA 2]
    © Casa do Código
Todos os direitos reservados e protegidos pela Lei nº9.610, de
10/02/1998.
Nenhuma parte deste livro poderá ser reproduzida, nem transmitida, sem
autorização prévia por escrito da editora, sejam quais forem os meios:
fotográficos, eletrônicos, mecânicos, gravação ou quaisquer outros.

    Casa do Código
Livros para o programador
Rua Vergueiro, 3185 - 8º andar
04101-300 – Vila Mariana – São Paulo – SP – Brasil


[PAGINA 3]
Casa do Código




“Às famílias Bertoldo, Ferreira e Turini.”
– Rodrigo Turini




                                             i


[PAGINA 4]


[PAGINA 5]
Casa do Código




Agradecimentos

Em primeiro lugar, gostaria muito de agradecer a você, o leitor. Foi para você
que cuidadosamente escrevi esse livro, pensando sempre em como o con-
teúdo poderia ser aplicado em seu dia a dia. Espero atender e, quem sabe,
superar as suas expectativas.
    Para evitar consequências imprevisíveis, não posso deixar de agradecer à
minha esposa Jordana. Sem seu valioso incentivo este livro não passaria de
um plano. E também para pequena Katherine, que nesse momento provavel-
mente está chutando a sua barriga.
    Não posso deixar de mencionar a família Silveira, que, pra mim, são os
maiores incentivadores do mundo. Ao Paulo, pela presença, incentivo e men-
toring. Ao Guilherme, pelas ideias, pareamentos e todo conhecimento com-
partilhado. E finalmente ao Sr. Carlos, pela cultura e inspiração diária.
    Por fim, mas nem um pouco menos importante, a toda equipe da Caelum
e Alura. Em especial ao Victor Harada, pois sem suas ideias, críticas e dis-
cussões, boa parte deste livro seria diferente.




                                                                           iii


[PAGINA 6]


[PAGINA 7]
Casa do Código                                                               Sumário




Sumário

1   Introdução                                                                    1
    1.1 O projeto e as tecnologias . . . . . . . . . . . . . . . . . . . . .      1
    1.2 Instalando e configurando o Eclipse . . . . . . . . . . . . . . .         2
    1.3 Download dos arquivos pro projeto . . . . . . . . . . . . . . .           3
    1.4 Acesse o código desse livro . . . . . . . . . . . . . . . . . . . .       4
    1.5 Aproveitando ao máximo o conteúdo . . . . . . . . . . . . . .             5
    1.6 Tirando suas dúvidas . . . . . . . . . . . . . . . . . . . . . . .        5

2   Java FX                                                                       7
    2.1 Nossa primeira App em Java FX . . . . . . . . . . . . . . . . .           7
    2.2 Configurando a livraria-base . . . . . . . . . . . . . . . . . . .       11
    2.3 Preparando nosso cenário . . . . . . . . . . . . . . . . . . . .         13
    2.4 Uma listagem de produtos . . . . . . . . . . . . . . . . . . . .         18

3   Java IO                                                                      29
    3.1 Entrada e saída de dados . . . . . . . . . . . . . . . . . . . . .       29
    3.2 Lendo um arquivo de texto . . . . . . . . . . . . . . . . . . . .        30
    3.3 Lendo texto do teclado com System.in . . . . . . . . . . . . .           34
    3.4 Tornando tudo mais simples com Scanner . . . . . . . . . . .             36
    3.5 Saída de dados e o OutputStream . . . . . . . . . . . . . . . .          38
    3.6 Escrita mais simples com PrintStream . . . . . . . . . . . . .           42
    3.7 Gerando um CSV de produtos . . . . . . . . . . . . . . . . . .           43
    3.8 Botão de exportar produtos . . . . . . . . . . . . . . . . . . .         48
    3.9 Adicionando ações com setOnAction . . . . . . . . . . . . . .            49
    3.10 JavaFx e Java 8 . . . . . . . . . . . . . . . . . . . . . . . . . . .   52

                                                                                  v


[PAGINA 8]
Sumário                                                              Casa do Código


4 Banco de Dados e JDBC                                                          57
  4.1 Iniciando com MySQL . . . . . . . . . . . . . . . . . . . . . .            57
  4.2 Criando a tabela de produtos . . . . . . . . . . . . . . . . . . .         60
  4.3 O pacote java.sql e o JDBC . . . . . . . . . . . . . . . . . . . .         61
  4.4 Abrindo conexão com MySQL em Java . . . . . . . . . . . . .                63
  4.5 Listando todos os produtos do banco . . . . . . . . . . . . . .            66
  4.6 Importando produtos de um dump . . . . . . . . . . . . . . .               69
  4.7 Para saber mais: Adicionando programaticamente . . . . . .                 71
  4.8 Qual a melhor forma de fechar a conexão? . . . . . . . . . . .             75
  4.9 O padrão de projeto DAO . . . . . . . . . . . . . . . . . . . .            78

5    Threads e Paralelismo                                                         85
     5.1 Processamento demorado, e agora? . . . . . . . . . . . . . . .           86
     5.2 Trabalhando com Threads em Java . . . . . . . . . . . . . . .             87
     5.3 O contrato Runnable . . . . . . . . . . . . . . . . . . . . . . .         89
     5.4 Threads com classes anônimas e lambdas . . . . . . . . . . .              91
     5.5 Exportando em uma thread separada . . . . . . . . . . . . . .            94
     5.6 Um pouco mais sobre as Threads . . . . . . . . . . . . . . . .           99
     5.7 Garbage Collector . . . . . . . . . . . . . . . . . . . . . . . . .     101
     5.8 Java FX assíncrono . . . . . . . . . . . . . . . . . . . . . . . . .    103
     5.9 Trabalhando com a classe Task . . . . . . . . . . . . . . . . . .       104
     5.10 Código final com e sem lambdas . . . . . . . . . . . . . . . . .        112

6 CSS no Java FX                                                                 117
  6.1 Seu primeiro CSS no Java FX . . . . . . . . . . . . . . . . . . .           118
  6.2 Extraindo estilos pra um arquivo .css . . . . . . . . . . . . . .          120

7    JAR, bibliotecas e build                                                    135
     7.1 JAR . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    135
     7.2 Gerando JAR executável pela IDE . . . . . . . . . . . . . . . .         136
     7.3 Executando a livraria-fx.jar . . . . . . . . . . . . . . . . . . . .    138
     7.4 Bibliotecas em Java . . . . . . . . . . . . . . . . . . . . . . . .     140
     7.5 Documentando seu projeto com Javadoc . . . . . . . . . . . .            141

vi


[PAGINA 9]
Casa do Código                                                            Sumário



    7.6    Automatizando build com Maven . . . . . . . . . . . . . . . .     146
    7.7    Transformando nossa app em um projeto Maven . . . . . . .         147
    7.8    Adicionando as dependências com Maven . . . . . . . . . . .        151
    7.9    Executando algumas tasks do Maven . . . . . . . . . . . . . .     157
    7.10   Adicionando plugin do Java FX . . . . . . . . . . . . . . . . .   159
    7.11   Maven na linha de comando . . . . . . . . . . . . . . . . . . .   163
    7.12   Como ficou nosso pom.xml . . . . . . . . . . . . . . . . . . .    165

8   Refatorações                                                              169
    8.1 Refatoração . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170
    8.2 Os tão populares Design Patterns . . . . . . . . . . . . . . . . 175

9 Próximos passos com Java                                                   179
  9.1 Entre em contato conosco . . . . . . . . . . . . . . . . . . . .       180




                                                                              vii


[PAGINA 10]


[PAGINA 11]
Capítulo 1

Introdução
1.1   O projeto e as tecnologias
Durante este livro, trabalharemos no projeto de uma livraria. A princípio,
vamos criar uma listagem de produtos com Java FX e ao decorrer dos capítu-
los incrementaremos suas funcionalidades, passando pelas APIs de IO, JDBC,
Threads e muito mais. Além disso, a todo o momento discutiremos sobre boas
práticas da orientação a objetos e design patterns.
     Ao final, o projeto deve ficar parecido com:


[PAGINA 12]
1.2. Instalando e configurando o Eclipse                                Casa do Código




                     Fig. 1.1: Aparência final do projeto deste livro



    Essa listagem de livros é carregada de um banco de dados MySQL, uti-
lizando a API de JDBC. O build e gerenciamento de dependências é total-
mente automatizado, com uso do tão popular Maven. A ação de exportar os
livros é feita em uma Thread diferente, que roda em paralelo com a Thread
principal da aplicação.
    Nosso código já usará a sintaxe e recursos do Java 8, como as famosas ex-
pressões lambdas. Mas não se preocupe, você não precisa conhecer Java 8 ou
nenhuma outra tecnologia além de Java puro para continuar, cada novidade
será muito bem detalhada. Pronto para começar?


1.2 Instalando e configurando o Eclipse
Para começar, você precisará do Eclipse ou qualquer outra IDE de sua prefer-
ência. Utilizarei o Eclipse em meus exemplos, devido ao ganho de produtivi-

2


[PAGINA 13]
Casa do Código                                                Capítulo 1. Introdução



dade (que será mencionado em alguns pontos do livro), além de sua popu-
laridade no mercado e instituições de ensino. Se quiser, você pode fazer o
download do Eclipse em:
    https://www.eclipse.org/downloads/
    Para utilizar o Java FX no Eclipse, você também precisará do e(fx)clipse,
que pode ser baixado pelo seguinte link, no qual você também encontrará um
passo a passo para instalá-lo.
    http://www.eclipse.org/efxclipse/install.html

Algumas outras opções
     Além do Eclipse, existem diversas outras IDEs que podem ser utilizadas
no desenvolvimento desse projeto. Netbeans e Intellij IDEA são algumas delas.
O Netbeans já vem com suporte ao Java FX, sendo assim você não precisará
instalar nada. Você pode ler mais sobre ele e fazer o download em:
     https://netbeans.org/
     Segundo as pesquisas mais recentes, logo depois do Eclipse, o Intellij IDEA
é a IDE mais utilizada pelos desenvolvedores Java. Mas há uma questão: ela
é paga. Você pode baixar uma versão Community Edition (gratuita), mas ela
deixa um pouco a desejar. Se quiser experimentar a versão completa, tem
como opção baixar um trial por 30 dias.
     https://www.jetbrains.com/idea/
     Apesar de utilizamos Eclipse nos exemplos desse livro, você pode usar a
IDE de sua preferência. Fique à vontade em sua escolha.


1.3    Download dos arquivos pro projeto
No link a seguir, você encontrará todos os arquivos necessários para acom-
panhar ativamente os códigos desse livro. Ele inclui a base do projeto, os jars
necessários para você fazer os exercícios, um arquivo de dump com alguns
livros já cadastrados no banco, entre outros.
    http://goo.gl/CfzTLB




                                                                                  3


[PAGINA 14]
1.4. Acesse o código desse livro                                   Casa do Código




    Desbravando a Orientação a Objetos

       Se você já leu meu livro Desbravando a Orientação a Objetos, perce-
    berá que esta é uma evolução do projeto que desenvolvemos por lá. Você
    pode continuar com seu próprio projeto, ou baixar o projeto já pronto se
    preferir.




                    Fig. 1.2: Desbravando Java e Orientação a Objetos


        http://www.casadocodigo.com.br/products/
    livro-orientacao-objetos-java


1.4 Acesse o código desse livro
Todos os exemplos desse livro e também seu código final, em Java 7 e 8, podem
ser encontrados no seguinte repositório:

      • https://github.com/Turini/livro-java

    Não deixe de escrever todos os códigos e exercitá-los durante os capítulos.
Assim você pode tirar um proveito maior do conteúdo. Vá além do que é aqui
sugerido, escreva novos testes, novos layouts e não deixe de compartilhar sua
experiência conosco.

4


[PAGINA 15]
Casa do Código                                                Capítulo 1. Introdução



1.5 Aproveitando ao máximo o conteúdo
Além de colocar todos os exemplos em prática, não deixe de consultar tam-
bém a documentação de cada API e biblioteca que vamos utilizar. Eu sempre
disponibilizo alguns links que podem ser úteis quando um novo assunto é
introduzido.
    Como nosso foco principal é Java, tenha sempre por perto a documen-
tação da linguagem:
    http://docs.oracle.com/javase/8/docs/api/
    Se estiver devidamente configurado, você pode ver a documentação das
classes e métodos pelo próprio Eclipse. Sempre que estou conhecendo uma
nova API, costumo usar o recurso de autocomplete (atalho Control +
space) e navegar pelos seus métodos.
    Veja que, quando paramos em um método específico, um box com sua
documentação é exibido:




                 Fig. 1.3: Explorando a API do Java pelo Eclipse



1.6    Tirando suas dúvidas
Ficou com alguma dúvida durante o livro? Mande um e-mail! Uma lista de
discussões foi criada exclusivamente para facilitar seu contato comigo e com
os demais leitores deste livro. Você pode e deve compartilhar suas dúvidas,
ideias, sugestões e criticas. Todas serão muito bem-vindas.
    https://groups.google.com/group/livro-java


                                                                                  5


[PAGINA 16]
1.6. Tirando suas dúvidas                                      Casa do Código


     Outro recurso que você pode utilizar para esclarecer suas dúvidas e par-
ticipar ativamente na comunidade Java é o fórum do GUJ. Lá você não só
pode perguntar, mas também responder, editar, comentar e assistir a diversas
discussões sobre o universo da programação.
     http://www.guj.com.br/




6


[PAGINA 17]
Capítulo 2

Java FX
2.1 Nossa primeira App em Java FX
Neste capítulo, criaremos uma tela simples usando Java FX, que servirá como
base para integrarmos algumas das outras APIs que veremos no decorrer do
livro. Apesar de nosso foco não ser a interface gráfica em si, escolhemos o
Java FX por ser uma alternativa muito interessante e mais moderna do que o
swing, além de ser bastante elegante. O Java FX já vem incluso no JDK e JRE.

Criando o projeto no Eclipse
    Agora que já configuramos nosso Eclipse para escrever aplicações em Java
FX, podemos criar um novo projeto. Para fazer isso, basta clicar em File >
New > Other... e escolher a opção Java FX Project. Podemos chamar
o projeto de livraria-fx, depois clicar em finish para concluir.


[PAGINA 18]
2.1. Nossa primeira App em Java FX                                     Casa do Código


    Se você estiver utilizando uma versão atual do Eclipse (o que é bastante
recomendado), já deverá aparecer uma estrutura padrão para sua aplicação,
como na seguinte imagem:




                   Fig. 2.1: Estrutura inicial do projeto no Eclipse



    Note que dentro do src, temos uma pacote chamado application
com a classe Main.java e o arquivo application.css. Veremos mais
detalhes sobre esse arquivo .css mais à frente, por enquanto vamos focar
no código Java. A classe Main já deve ter sido criada com o seguinte código:

♣✉❜❧✐❝ ❝❧❛ss ▼❛✐♥ ❡①t❡♥❞s ❆♣♣❧✐❝❛t✐♦♥ ④

      ❅❖✈❡rr✐❞❡
      ♣✉❜❧✐❝ ✈♦✐❞ st❛rt✭❙t❛❣❡ ♣r✐♠❛r②❙t❛❣❡✮ ④
          tr② ④
              ❇♦r❞❡rP❛♥❡ r♦♦t ❂ ♥❡✇ ❇♦r❞❡rP❛♥❡✭✮❀
              ❙❝❡♥❡ s❝❡♥❡ ❂ ♥❡✇ ❙❝❡♥❡✭r♦♦t✱✹✵✵✱✹✵✵✮❀

                  s❝❡♥❡✳❣❡t❙t②❧❡s❤❡❡ts✭✮
                      ✳❛❞❞✭❣❡t❈❧❛ss✭✮✳❣❡t❘❡s♦✉r❝❡✭✧❛♣♣❧✐❝❛t✐♦♥✳❝ss✧✮
                      ✳t♦❊①t❡r♥❛❧❋♦r♠✭✮✮❀

                ♣r✐♠❛r②❙t❛❣❡✳s❡t❙❝❡♥❡✭s❝❡♥❡✮❀
                ♣r✐♠❛r②❙t❛❣❡✳s❤♦✇✭✮❀
            ⑥ ❝❛t❝❤✭❊①❝❡♣t✐♦♥ ❡✮ ④

8


[PAGINA 19]
Casa do Código                                                Capítulo 2. Java FX



                 ❡✳♣r✐♥t❙t❛❝❦❚r❛❝❡✭✮❀
          ⑥
     ⑥

     ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④
         ❧❛✉♥❝❤✭❛r❣s✮❀
     ⑥
⑥

    Não se preocupe caso em seu Eclipse, ou qualquer outra IDE de sua
preferência, essa classe não tenha sido criada. Você pode criá-la facilmente,
mas aproveite e mantenha apenas o código que importa agora nesse começo.
Vamos apagar esse try catch e linhas que criam a classe Scene e aplicam
o estilo css. Por agora só precisamos do seguinte código:

♣✉❜❧✐❝ ❝❧❛ss ▼❛✐♥ ❡①t❡♥❞s ❆♣♣❧✐❝❛t✐♦♥ ④

     ❅❖✈❡rr✐❞❡
     ♣✉❜❧✐❝ ✈♦✐❞ st❛rt✭❙t❛❣❡ ♣r✐♠❛r②❙t❛❣❡✮ ④
         ♣r✐♠❛r②❙t❛❣❡✳s❡t❚✐t❧❡✭✧❙✐st❡♠❛ ❞❛ ❧✐✈r❛r✐❛ ❝♦♠ ❏❛✈❛ ❋❳✧✮❀
         ♣r✐♠❛r②❙t❛❣❡✳s❤♦✇✭✮❀
     ⑥

     ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④
         ❧❛✉♥❝❤✭❛r❣s✮❀
     ⑥

⑥

     Note que já adicionei um titulo que não existia no arquivo Java, faça o
mesmo e execute essa classe para ver o primeiro resultado. Se tudo correu
bem, uma tela cinza com o título Sistema da livraria com Java FX deve apare-
cer:




                                                                               9


[PAGINA 20]
2.1. Nossa primeira App em Java FX                               Casa do Código




                           Fig. 2.2: Primeira tela em Java FX



     Executando código no Eclipse

         Caso não esteja familiarizado com o Eclipse, você pode executar seu
     código de diversas maneiras. Uma delas é clicando com o botão direito na
     classe, selecionando Run As... e depois Java Application. Outra
     alternativa bem prática é utilizando o atalho Control + F11.

    Excelente, já temos algum resultado. Mas antes de seguir precisamos en-
tender um pouco mais sobre a anatomia desse nosso primeiro código.
    Podemos começar pela classe javafx.application.Application.
A regra é simples, a classe principal de nossas aplicações em Java FX pre-
cisa herdar de Application e consequentemente sobrescrever seu único
método abstrato, chamado start. Esse é o ponto de partida de toda apli-
cação que em Java FX.
    Vale lembrar que como esse método é abstrato, somos obrigados a
sobrescrevê-lo. Portanto, caso você não lembre disso, o compilador certa-
mente lhe lembrará com um erro. Além disso, perceba que esse método re-

10


[PAGINA 21]
Casa do Código                                                Capítulo 2. Java FX



cebe um objeto do tipo Stage como parâmetro, que é o container principal
da aplicação.
    Por fim, note também que temos um método main. Nele, invocamos um
outro método chamado launch, também presente na classe Application.
Ele é o responsável por iniciar a aplicação.


2.2 Configurando a livraria-base
Agora que já sabemos um pouco mais sobre esse código inicial, vamos
começar a implementar a nossa listagem de Produtos. Para isso, precisare-
mos da interface Produto e de suas implementações, presentes no arquivo
que você deve ter baixado no capítulo anterior. Não se preocupe se você ainda
não baixou, você pode fazer isso agora pelo seguinte link:
    http://goo.gl/CfzTLB
    Após concluir o download, você precisará importar o projeto no Eclipse.
Primeiro, extraia o conteúdo do ZIP que você baixou para alguma pasta de
sua preferência. Agora, pelo Eclipse, clique no menu File, Import... e
depois em Existing Projects into Workspace.




                 Fig. 2.3: Importando projeto pelo Eclipse.



    Selecione o diretório (em Browse...) onde você colocou o projeto

                                                                              11


[PAGINA 22]
2.2. Configurando a livraria-base                                   Casa do Código


livraria-base, que estava dentro do              ZIP, e logo depois clique em
Finish.




                     Fig. 2.4: Concluindo import do projeto base.



    Queremos agora vincular os dois projetos. Por enquanto, faremos isso
pelo próprio Eclipse, clicando com o botão direito no projeto livraria-fx,
opção Build Path e depois Configure Build Path....




12


[PAGINA 23]
Casa do Código                                                    Capítulo 2. Java FX




                 Fig. 2.5: Build Path > Configure Build Path...



   Vá à aba Projects, clique em Add, escolha o projeto livraria-base,
que acabamos de importar. Depois basta clicar em Ok.




                 Fig. 2.6: Adicionando projeto no build path.



2.3 Preparando nosso cenário
Antes de criar uma tabela, precisamos criar um cenário, onde ficará todo o
conteúdo dessa nossa tela. Uma tela do Java FX sempre é composta por um
container principal ( Stage) e também por um cenário, representado pela
classe Scene. Repare em sua estrutura:

❙❝❡♥❡ s❝❡♥❡ ❂ ♥❡✇ ❙❝❡♥❡✭r♦♦t✱ ❧❛r❣✉r❛✱ ❛❧t✉r❛✮


                                                                                  13


[PAGINA 24]
2.3. Preparando nosso cenário                                  Casa do Código


     Os parâmetros largura e altura representam bem seu significado,
não é? Definimos nele o tamanho do nosso cenário, da tela da nossa aplicação.
Já esse root nada mais é do que um auxiliar, que ajuda no processo de layout,
como ao adicionar ou remover elementos.
     O tipo do parâmetro root é javafx.scene.Parent, que é uma classe
abstrata. De acordo com nossa necessidade, escolhemos uma de suas im-
plementações. Como a tela será composta por 2 elementos (um label e uma
tabela), podemos usar um Group.




14


[PAGINA 25]
Casa do Código                                                 Capítulo 2. Java FX




 Outras implementações

   Além do Group, temos como opções diretamente as classes
 Control, Region e WebView. Além disso, cada uma dessas tem di-
 versas outras subclasses. São várias possibilidades! Uma opção bastante
 usada é a GridPane, do pacote javafx.scene.layout. Ela é filha
 de Pane, que é filha de Region que, finalmente, é filha de Parent.
 Ufa!




           Fig. 2.7: Hierarquia da classe javafx.scene.layout.GridPane


    Você pode conhecer um pouco mais sobre essa e outras implemen-
 tações em:
    https://docs.oracle.com/javafx/2/api/javafx/scene/Parent.html
    Veremos diversas delas durante o livro.

    O código do nosso método start deve ficar parecido com:

♣✉❜❧✐❝ ✈♦✐❞ st❛rt✭❙t❛❣❡ ♣r✐♠❛r②❙t❛❣❡✮ ④
    ●r♦✉♣ ❣r♦✉♣ ❂ ♥❡✇ ●r♦✉♣✭✮❀
    ❙❝❡♥❡ s❝❡♥❡ ❂ ♥❡✇ ❙❝❡♥❡✭❣r♦✉♣✱ ✻✾✵✱ ✺✶✵✮❀
    ♣r✐♠❛r②❙t❛❣❡✳s❡t❙❝❡♥❡✭s❝❡♥❡✮❀

                                                                               15


[PAGINA 26]
2.3. Preparando nosso cenário                                 Casa do Código


      ♣r✐♠❛r②❙t❛❣❡✳s❡t❚✐t❧❡✭✧❙✐st❡♠❛ ❞❛ ❧✐✈r❛r✐❛ ❝♦♠ ❏❛✈❛ ❋❳✧✮❀
      ♣r✐♠❛r②❙t❛❣❡✳s❤♦✇✭✮❀
⑥

    Perceba que estamos chamando o método setScene, vinculando o
cenário com o container principal. Quer ver o resultado? Não deixe de ex-
ecutar o código a cada evolução. Agora a tela estará maior e com um fundo
branco, padrão do cenário.
    O próximo passo será colocar um texto na tela, indicando que essa será a
nossa listagem de produtos. Faremos isso com a auxilio da classe Label, do
pacote javafx.scene.control.

▲❛❜❡❧ ❧❛❜❡❧ ❂ ♥❡✇ ▲❛❜❡❧✭✧▲✐st❛❣❡♠ ❞❡ ▲✐✈r♦s✧✮❀

    Podemos agora utilizar a classe Group, que está vinculada ao nosso
cenário, para adicionar esse novo elemento na página. Para fazer isso,
basta chamar seu método getChildren e adicionar todos os elementos
necessários, que neste caso será apenas o label:

❣r♦✉♣✳❣❡t❈❤✐❧❞r❡♥✭✮✳❛❞❞❆❧❧✭❧❛❜❡❧✮❀

     O código completo do método start deverá ficar assim:

♣✉❜❧✐❝ ✈♦✐❞ st❛rt✭❙t❛❣❡ ♣r✐♠❛r②❙t❛❣❡✮ ④

      ●r♦✉♣ ❣r♦✉♣ ❂ ♥❡✇ ●r♦✉♣✭✮❀
      ❙❝❡♥❡ s❝❡♥❡ ❂ ♥❡✇ ❙❝❡♥❡✭❣r♦✉♣✱ ✻✾✵✱ ✺✶✵✮❀

      ▲❛❜❡❧ ❧❛❜❡❧ ❂ ♥❡✇ ▲❛❜❡❧✭✧▲✐st❛❣❡♠ ❞❡ ▲✐✈r♦s✧✮❀

      ❣r♦✉♣✳❣❡t❈❤✐❧❞r❡♥✭✮✳❛❞❞❆❧❧✭❧❛❜❡❧✮❀
      ♣r✐♠❛r②❙t❛❣❡✳s❡t❙❝❡♥❡✭s❝❡♥❡✮❀
      ♣r✐♠❛r②❙t❛❣❡✳s❡t❚✐t❧❡✭✧❙✐st❡♠❛ ❞❛ ❧✐✈r❛r✐❛ ❝♦♠ ❏❛✈❛ ❋❳✧✮❀
      ♣r✐♠❛r②❙t❛❣❡✳s❤♦✇✭✮❀
⑥

   Ao rodar esse código, teremos a saída esperada, mas o texto está muito
pequeno e grudado nas margens da tela!


16


[PAGINA 27]
Casa do Código                                                 Capítulo 2. Java FX




                 Fig. 2.8: Listagem com o label desalinhado.



    Para melhorar um pouco a aparência desse label, podemos mudar sua
fonte e também adicionar um padding. Para isso, vamos utilizar os métodos
setFont e setPadding, como a seguir:

▲❛❜❡❧ ❧❛❜❡❧ ❂ ♥❡✇ ▲❛❜❡❧✭✧▲✐st❛❣❡♠ ❞❡ ▲✐✈r♦s✧✮❀

❧❛❜❡❧✳s❡t❋♦♥t✭❋♦♥t
    ✳❢♦♥t✭✧▲✉❝✐❞❛ ●r❛♥❞❡✧✱ ❋♦♥tP♦st✉r❡✳❘❊●❯▲❆❘✱ ✸✵✮✮❀

❧❛❜❡❧✳s❡tP❛❞❞✐♥❣✭♥❡✇ ■♥s❡ts✭✷✵✱ ✵✱ ✶✵✱ ✶✵✮✮❀

    O método estático font, da classe javafx.scene.text.Font, nos
possibilita passar a família, tipo e tamanho da fonte que queremos aplicar
em nosso texto. Existem outras sobrecargas desse método para aplicar ape-
nas o tamanho, apenas família e assim por diante. Repare também que no
setPadding estamos utilizando uma classe auxiliar para passar as medidas,
a Insets.
    Execute seu código mais uma vez para perceber o resultado:




                                                                               17


[PAGINA 28]
2.4. Uma listagem de produtos                                    Casa do Código




                        Fig. 2.9: Listagem com label alinhada.



     Um pouco melhor, não acha? Agora podemos partir para a tabela!


2.4      Uma listagem de produtos
Nosso próximo passo será criar uma tabela para exibir nossa lista de pro-
dutos. Antes de focar na tabela, vamos criar uma nova classe no pacote
repositorio, que será responsável por retornar a lista de produtos que de-
verá ser exibida. Podemos chamá-la de RepositorioDeProdutos:

♣❛❝❦❛❣❡ r❡♣♦s✐t♦r✐♦❀

♣✉❜❧✐❝ ❝❧❛ss ❘❡♣♦s✐t♦r✐♦❉❡Pr♦❞✉t♦s ④

      ♣✉❜❧✐❝ ❖❜s❡r✈❛❜❧❡▲✐st❁Pr♦❞✉t♦❃ ❧✐st❛✭✮ ④

            ❆✉t♦r ❛✉t♦r ❂ ♥❡✇ ❆✉t♦r✭✮❀
            ❛✉t♦r✳s❡t◆♦♠❡✭✧❘♦❞r✐❣♦ ❚✉r✐♥✐✧✮❀
            ❛✉t♦r✳s❡t❊♠❛✐❧✭✧r♦❞r✐❣♦✳t✉r✐♥✐❅❝❛❡❧✉♠✳❝♦♠✳❜r✧✮❀
            ❛✉t♦r✳s❡t❈♣❢✭✧✶✷✸✳✹✺✻✳✼✽✾✳✶✵✧✮❀

            ▲✐✈r♦ ❧✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦❋✐s✐❝♦✭❛✉t♦r✮❀
            ❧✐✈r♦✳s❡t◆♦♠❡✭✧❏❛✈❛ ✽ Prát✐❝♦✧✮❀
            ❧✐✈r♦✳s❡t❉❡s❝r✐❝❛♦✭✧◆♦✈♦s r❡❝✉rs♦s ❞❛ ❧✐♥❣✉❛❣❡♠✧✮❀
            ❧✐✈r♦✳s❡t❱❛❧♦r✭✺✾✳✾✵✮❀
            ❧✐✈r♦✳s❡t■s❜♥✭✧✾✼✽✲✽✺✲✻✻✷✺✵✲✹✻✲✻✧✮❀



18


[PAGINA 29]
Casa do Código                                               Capítulo 2. Java FX



          ▲✐✈r♦ ♠❛✐s❯♠❧✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦❋✐s✐❝♦✭❛✉t♦r✮❀
          ♠❛✐s❯♠❧✐✈r♦✳s❡t◆♦♠❡✭✧❉❡s❜r❛✈❛♥❞♦ ❛ ❖✳❖✳✧✮❀
          ♠❛✐s❯♠❧✐✈r♦✳s❡t❉❡s❝r✐❝❛♦✭✧▲✐✈r♦ ❞❡ ❏❛✈❛ ❡ ❖✳❖✧✮❀
          ♠❛✐s❯♠❧✐✈r♦✳s❡t❱❛❧♦r✭✺✾✳✾✵✮❀
          ♠❛✐s❯♠❧✐✈r♦✳s❡t■s❜♥✭✧✸✷✶✲✺✹✲✻✼✽✾✵✲✶✶✲✷✧✮❀

          ❆✉t♦r ♦✉tr♦❆✉t♦r ❂ ♥❡✇ ❆✉t♦r✭✮❀
          ♦✉tr♦❆✉t♦r✳s❡t◆♦♠❡✭✧P❛✉❧♦ ❙✐❧✈❡✐r❛✧✮❀
          ♦✉tr♦❆✉t♦r✳s❡t❊♠❛✐❧✭✧♣❛✉❧♦✳s✐❧✈❡✐r❛❅❝❛❡❧✉♠✳❝♦♠✳❜r✧✮❀
          ♦✉tr♦❆✉t♦r✳s❡t❈♣❢✭✧✶✷✸✳✹✺✻✳✼✽✾✳✶✵✧✮❀

          ▲✐✈r♦ ♦✉tr♦▲✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦❋✐s✐❝♦✭♦✉tr♦❆✉t♦r✮❀
          ♦✉tr♦▲✐✈r♦✳s❡t◆♦♠❡✭✧▲ó❣✐❝❛ ❞❡ Pr♦❣r❛♠❛çã♦✧✮❀
          ♦✉tr♦▲✐✈r♦✳s❡t❉❡s❝r✐❝❛♦✭✧❈r✐❡ s❡✉s ♣r✐♠❡✐r♦s ♣r♦❣r❛♠❛s✧✮❀
          ♦✉tr♦▲✐✈r♦✳s❡t❱❛❧♦r✭✺✾✳✾✵✮❀
          ♦✉tr♦▲✐✈r♦✳s❡t■s❜♥✭✧✾✼✽✲✽✺✲✻✻✷✺✵✲✷✷✲✵✧✮❀

          r❡t✉r♥ ❋❳❈♦❧❧❡❝t✐♦♥s
              ✳♦❜s❡r✈❛❜❧❡❆rr❛②▲✐st✭❧✐✈r♦✱ ♠❛✐s❯♠❧✐✈r♦✱ ♦✉tr♦▲✐✈r♦✮❀
     ⑥

⑥

    Por enquanto, estamos criando os livros e autores manualmente,
mas muito em breve faremos isso de uma forma bem mais interes-
sante. Você já deve ter notado que o tipo de retorno dessa lista é um
tanto diferente daquilo com que estamos acostumados, ela retorna uma
ObservableList<Produto>. Esse é o tipo de lista que a tabela do
Java FX espera receber. Criá-la é bem simples com o apoio da factory
FXCollections, do pacote javafx.collections:
❖❜s❡r✈❛❜❧❡▲✐st ❧✐st❛ ❂
    ❋❳❈♦❧❧❡❝t✐♦♥s✳♦❜s❡r✈❛❜❧❡❆rr❛②▲✐st✭✳✳✳✮❀

     Agora que já temos uma lista, podemos voltar para a classe Main e criar
um novo elemento em nosso cenário ( Scene), uma tabela. Para fazer isso,
utilizaremos a classe TableView, como a seguir:
❖❜s❡r✈❛❜❧❡▲✐st❁Pr♦❞✉t♦❃ ♣r♦❞✉t♦s ❂
    ♥❡✇ ❘❡♣♦s✐t♦r✐♦❉❡Pr♦❞✉t♦s✭✮✳❧✐st❛✭✮❀

                                                                             19


[PAGINA 30]
2.4. Uma listagem de produtos                                  Casa do Código




❚❛❜❧❡❱✐❡✇ t❛❜❧❡❱✐❡✇ ❂ ♥❡✇ ❚❛❜❧❡❱✐❡✇❁❃✭♣r♦❞✉t♦s✮❀

   Já estamos passando a lista de produtos do RepositorioDeProdutos
como argumento em seu construtor. Nesse momento o código de nosso
método start está assim:

♣✉❜❧✐❝ ✈♦✐❞ st❛rt✭❙t❛❣❡ ♣r✐♠❛r②❙t❛❣❡✮ ④
    ●r♦✉♣ ❣r♦✉♣ ❂ ♥❡✇ ●r♦✉♣✭✮❀
    ❙❝❡♥❡ s❝❡♥❡ ❂ ♥❡✇ ❙❝❡♥❡✭❣r♦✉♣✱ ✻✾✵✱ ✺✶✵✮❀

      ❖❜s❡r✈❛❜❧❡▲✐st❁Pr♦❞✉t♦❃ ♣r♦❞✉t♦s ❂
          ♥❡✇ ❘❡♣♦s✐t♦r✐♦❉❡Pr♦❞✉t♦s✭✮✳❧✐st❛✭✮❀

      ❚❛❜❧❡❱✐❡✇ t❛❜❧❡❱✐❡✇ ❂ ♥❡✇ ❚❛❜❧❡❱✐❡✇❁❃✭♣r♦❞✉t♦s✮❀

      ▲❛❜❡❧ ❧❛❜❡❧ ❂ ♥❡✇ ▲❛❜❡❧✭✧▲✐st❛❣❡♠ ❞❡ ▲✐✈r♦s✧✮❀

      ❧❛❜❡❧✳s❡t❋♦♥t✭❋♦♥t
          ✳❢♦♥t✭✧▲✉❝✐❞❛ ●r❛♥❞❡✧✱ ❋♦♥tP♦st✉r❡✳❘❊●❯▲❆❘✱ ✸✵✮✮❀

      ❧❛❜❡❧✳s❡tP❛❞❞✐♥❣✭♥❡✇ ■♥s❡ts✭✷✵✱ ✵✱ ✶✵✱ ✶✵✮✮❀

      ❣r♦✉♣✳❣❡t❈❤✐❧❞r❡♥✭✮✳❛❞❞❆❧❧✭❧❛❜❡❧✮❀

      ♣r✐♠❛r②❙t❛❣❡✳s❡t❙❝❡♥❡✭s❝❡♥❡✮❀
      ♣r✐♠❛r②❙t❛❣❡✳s❡t❚✐t❧❡✭✧❙✐st❡♠❛ ❞❛ ❧✐✈r❛r✐❛ ❝♦♠ ❏❛✈❛ ❋❳✧✮❀
      ♣r✐♠❛r②❙t❛❣❡✳s❤♦✇✭✮❀
⑥

    Podemos agora criar as colunas de nossa tabela. Basta criar uma instância
do tipo TableColumn, recebendo o nome da coluna como parâmetro:

❚❛❜❧❡❈♦❧✉♠♥ ♥♦♠❡❈♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭✧◆♦♠❡✧✮❀

    Além disso, para cada coluna precisamos definir sua fonte de dados, ou
seja, qual propriedade da classe Produto deve ser exibida nessa determi-
nada coluna. Para isso, chamamos seu método setCellValueFactory,
passando um novo PropertyValueFactory como parâmetro:

20


[PAGINA 31]
Casa do Código                                           Capítulo 2. Java FX



❚❛❜❧❡❈♦❧✉♠♥ ♥♦♠❡❈♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭✧◆♦♠❡✧✮❀

♥♦♠❡❈♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
    ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②✭✧♥♦♠❡✧✮✮❀

    Opcionalmente, você pode definir um tamanho mínimo e máximo para
essa coluna, utilizando seus métodos setMinWidth e setMaxWidth. Um
exemplo seria:

❞❡s❝❈♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭✷✸✵✮❀

    Vamos criar uma coluna para cada um dos quatro atributos principais
de nossos Produtos, seu nome, descrição, valor e ISBN (que é seu código
único).
    Ao final, seu código deve ficar assim:

♣✉❜❧✐❝ ✈♦✐❞ st❛rt✭❙t❛❣❡ ♣r✐♠❛r②❙t❛❣❡✮ ④

     ●r♦✉♣ ❣r♦✉♣ ❂ ♥❡✇ ●r♦✉♣✭✮❀
     ❙❝❡♥❡ s❝❡♥❡ ❂ ♥❡✇ ❙❝❡♥❡✭❣r♦✉♣✱ ✻✾✵✱ ✺✶✵✮❀

     ❖❜s❡r✈❛❜❧❡▲✐st❁Pr♦❞✉t♦❃ ♣r♦❞✉t♦s ❂
         ♥❡✇ ❘❡♣♦s✐t♦r✐♦❉❡Pr♦❞✉t♦s✭✮✳❧✐st❛✭✮❀

     ❚❛❜❧❡❱✐❡✇ t❛❜❧❡❱✐❡✇ ❂ ♥❡✇ ❚❛❜❧❡❱✐❡✇✭♣r♦❞✉t♦s✮❀

     ❚❛❜❧❡❈♦❧✉♠♥ ♥♦♠❡❈♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭✧◆♦♠❡✧✮❀
     ♥♦♠❡❈♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭✶✽✵✮❀
     ♥♦♠❡❈♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
         ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②✭✧♥♦♠❡✧✮✮❀

     ❚❛❜❧❡❈♦❧✉♠♥ ❞❡s❝❈♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭✧❉❡s❝r✐çã♦✧✮❀
     ❞❡s❝❈♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭✷✸✵✮❀
     ❞❡s❝❈♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
         ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②✭✧❞❡s❝r✐❝❛♦✧✮✮❀

     ❚❛❜❧❡❈♦❧✉♠♥ ✈❛❧♦r❈♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭✧❱❛❧♦r✧✮❀
     ✈❛❧♦r❈♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭✻✵✮❀
     ✈❛❧♦r❈♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭

                                                                         21


[PAGINA 32]
2.4. Uma listagem de produtos                               Casa do Código


            ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②✭✧✈❛❧♦r✧✮✮❀

      ❚❛❜❧❡❈♦❧✉♠♥ ✐s❜♥❈♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭✧■❙❇◆✧✮❀
      ✐s❜♥❈♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭✶✽✵✮❀
      ✐s❜♥❈♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
          ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②✭✧✐s❜♥✧✮✮❀

      ▲❛❜❡❧ ❧❛❜❡❧ ❂ ♥❡✇ ▲❛❜❡❧✭✧▲✐st❛❣❡♠ ❞❡ ▲✐✈r♦s✧✮❀

      ❧❛❜❡❧✳s❡t❋♦♥t✭❋♦♥t
          ✳❢♦♥t✭✧▲✉❝✐❞❛ ●r❛♥❞❡✧✱ ❋♦♥tP♦st✉r❡✳❘❊●❯▲❆❘✱ ✸✵✮✮❀

      ❧❛❜❡❧✳s❡tP❛❞❞✐♥❣✭♥❡✇ ■♥s❡ts✭✷✵✱ ✵✱ ✶✵✱ ✶✵✮✮❀

      ❣r♦✉♣✳❣❡t❈❤✐❧❞r❡♥✭✮✳❛❞❞❆❧❧✭❧❛❜❡❧✮❀

      ♣r✐♠❛r②❙t❛❣❡✳s❡t❙❝❡♥❡✭s❝❡♥❡✮❀
      ♣r✐♠❛r②❙t❛❣❡✳s❡t❚✐t❧❡✭✧❙✐st❡♠❛ ❞❛ ❧✐✈r❛r✐❛ ❝♦♠ ❏❛✈❛ ❋❳✧✮❀
      ♣r✐♠❛r②❙t❛❣❡✳s❤♦✇✭✮❀
⑥

   Por fim, vamos adicionar as colunas na tabela e depois adicioná-la ao
nosso cenário:

t❛❜❧❡❱✐❡✇✳❣❡t❈♦❧✉♠♥s✭✮✳❛❞❞❆❧❧✭♥♦♠❡❈♦❧✉♠♥✱
    ❞❡s❝❈♦❧✉♠♥✱ ✈❛❧♦r❈♦❧✉♠♥✱ ✐s❜♥❈♦❧✉♠♥✮❀

❣r♦✉♣✳❣❡t❈❤✐❧❞r❡♥✭✮✳❛❞❞❆❧❧✭❧❛❜❡❧✱ t❛❜❧❡❱✐❡✇✮❀

    Ao executar o código, a tabela estará populada como esperamos, mas to-
talmente desalinhada e escondendo a nossa Label:




22


[PAGINA 33]
Casa do Código                                                Capítulo 2. Java FX




             Fig. 2.10: TableView desalinhada, cobrindo o label.



   Para resolver o problema, vamos envolver essa tableView em um
VBox. Esse elemento vai nos ajudar a alinhar a tabela, já que podemos definir
um padding, como a seguir:

❱❇♦① ✈❜♦① ❂ ♥❡✇ ❱❇♦①✭t❛❜❧❡❱✐❡✇✮❀
✈❜♦①✳s❡tP❛❞❞✐♥❣✭♥❡✇ ■♥s❡ts✭✼✵✱ ✵✱ ✵ ✱✶✵✮✮❀

   Basta adicionar esse novo item em nosso cenário, assim como fizemos
com a tabela:

❣r♦✉♣✳❣❡t❈❤✐❧❞r❡♥✭✮✳❛❞❞❆❧❧✭❧❛❜❡❧✱ ✈❜♦①✮❀

    O código final da sua classe Main deve ficar assim:

♣❛❝❦❛❣❡ ❛♣♣❧✐❝❛t✐♦♥❀

✐♠♣♦rt ❥❛✈❛❢①✳❛♣♣❧✐❝❛t✐♦♥✳❆♣♣❧✐❝❛t✐♦♥❀
✐♠♣♦rt ❥❛✈❛❢①✳❝♦❧❧❡❝t✐♦♥s✳❖❜s❡r✈❛❜❧❡▲✐st❀


                                                                              23


[PAGINA 34]
2.4. Uma listagem de produtos                           Casa do Código


✐♠♣♦rt ❥❛✈❛❢①✳❣❡♦♠❡tr②✳■♥s❡ts❀
✐♠♣♦rt ❥❛✈❛❢①✳s❝❡♥❡✳●r♦✉♣❀
✐♠♣♦rt ❥❛✈❛❢①✳s❝❡♥❡✳❙❝❡♥❡❀
✐♠♣♦rt ❥❛✈❛❢①✳s❝❡♥❡✳❝♦♥tr♦❧✳▲❛❜❡❧❀
✐♠♣♦rt ❥❛✈❛❢①✳s❝❡♥❡✳❝♦♥tr♦❧✳❚❛❜❧❡❈♦❧✉♠♥❀
✐♠♣♦rt ❥❛✈❛❢①✳s❝❡♥❡✳❝♦♥tr♦❧✳❚❛❜❧❡❱✐❡✇❀
✐♠♣♦rt ❥❛✈❛❢①✳s❝❡♥❡✳❝♦♥tr♦❧✳❝❡❧❧✳Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②❀
✐♠♣♦rt ❥❛✈❛❢①✳s❝❡♥❡✳❧❛②♦✉t✳❱❇♦①❀
✐♠♣♦rt ❥❛✈❛❢①✳s❝❡♥❡✳t❡①t✳❋♦♥t❀
✐♠♣♦rt ❥❛✈❛❢①✳s❝❡♥❡✳t❡①t✳❋♦♥tP♦st✉r❡❀
✐♠♣♦rt ❥❛✈❛❢①✳st❛❣❡✳❙t❛❣❡❀
✐♠♣♦rt r❡♣♦s✐t♦r✐♦✳❘❡♣♦s✐t♦r✐♦❉❡Pr♦❞✉t♦s❀
✐♠♣♦rt ❜r✳❝♦♠✳❝❛s❛❞♦❝♦❞✐❣♦✳❧✐✈r❛r✐❛✳♣r♦❞✉t♦s✳Pr♦❞✉t♦❀

♣✉❜❧✐❝ ❝❧❛ss ▼❛✐♥ ❡①t❡♥❞s ❆♣♣❧✐❝❛t✐♦♥ ④

      ❅❖✈❡rr✐❞❡
      ♣✉❜❧✐❝ ✈♦✐❞ st❛rt✭❙t❛❣❡ ♣r✐♠❛r②❙t❛❣❡✮ ④

            ●r♦✉♣ ❣r♦✉♣ ❂ ♥❡✇ ●r♦✉♣✭✮❀
            ❙❝❡♥❡ s❝❡♥❡ ❂ ♥❡✇ ❙❝❡♥❡✭❣r♦✉♣✱ ✻✾✵✱ ✺✶✵✮❀

            ❖❜s❡r✈❛❜❧❡▲✐st❁Pr♦❞✉t♦❃ ♣r♦❞✉t♦s ❂
                ♥❡✇ ❘❡♣♦s✐t♦r✐♦❉❡Pr♦❞✉t♦s✭✮✳❧✐st❛✭✮❀

            ❚❛❜❧❡❱✐❡✇❁Pr♦❞✉t♦❃ t❛❜❧❡❱✐❡✇ ❂ ♥❡✇ ❚❛❜❧❡❱✐❡✇❁❃✭♣r♦❞✉t♦s✮❀

            ❚❛❜❧❡❈♦❧✉♠♥ ♥♦♠❡❈♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭✧◆♦♠❡✧✮❀
            ♥♦♠❡❈♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭✶✽✵✮❀
            ♥♦♠❡❈♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
                ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②✭✧♥♦♠❡✧✮✮❀

            ❚❛❜❧❡❈♦❧✉♠♥ ❞❡s❝❈♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭✧❉❡s❝r✐çã♦✧✮❀
            ❞❡s❝❈♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭✷✸✵✮❀
            ❞❡s❝❈♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
                ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②✭✧❞❡s❝r✐❝❛♦✧✮✮❀

            ❚❛❜❧❡❈♦❧✉♠♥ ✈❛❧♦r❈♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭✧❱❛❧♦r✧✮❀
            ✈❛❧♦r❈♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭✻✵✮❀

24


[PAGINA 35]
Casa do Código                                             Capítulo 2. Java FX



          ✈❛❧♦r❈♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
              ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②✭✧✈❛❧♦r✧✮✮❀

          ❚❛❜❧❡❈♦❧✉♠♥ ✐s❜♥❈♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭✧■❙❇◆✧✮❀
          ✐s❜♥❈♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭✶✽✵✮❀
          ✐s❜♥❈♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
              ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②✭✧✐s❜♥✧✮✮❀

          t❛❜❧❡❱✐❡✇✳❣❡t❈♦❧✉♠♥s✭✮✳❛❞❞❆❧❧✭♥♦♠❡❈♦❧✉♠♥✱ ❞❡s❝❈♦❧✉♠♥✱
              ✈❛❧♦r❈♦❧✉♠♥✱ ✐s❜♥❈♦❧✉♠♥✮❀

          ❢✐♥❛❧ ❱❇♦① ✈❜♦① ❂ ♥❡✇ ❱❇♦①✭t❛❜❧❡❱✐❡✇✮❀
          ✈❜♦①✳s❡tP❛❞❞✐♥❣✭♥❡✇ ■♥s❡ts✭✼✵✱ ✵✱ ✵ ✱✶✵✮✮❀

          ▲❛❜❡❧ ❧❛❜❡❧ ❂ ♥❡✇ ▲❛❜❡❧✭✧▲✐st❛❣❡♠ ❞❡ ▲✐✈r♦s✧✮❀

          ❧❛❜❡❧✳s❡t❋♦♥t✭❋♦♥t
              ✳❢♦♥t✭✧▲✉❝✐❞❛ ●r❛♥❞❡✧✱ ❋♦♥tP♦st✉r❡✳❘❊●❯▲❆❘✱ ✸✵✮✮❀

          ❧❛❜❡❧✳s❡tP❛❞❞✐♥❣✭♥❡✇ ■♥s❡ts✭✷✵✱ ✵✱ ✶✵✱ ✶✵✮✮❀

          ❣r♦✉♣✳❣❡t❈❤✐❧❞r❡♥✭✮✳❛❞❞❆❧❧✭❧❛❜❡❧✱ ✈❜♦①✮❀

          ♣r✐♠❛r②❙t❛❣❡✳s❡t❚✐t❧❡✭✧❙✐st❡♠❛ ❞❛ ❧✐✈r❛r✐❛ ❝♦♠ ❏❛✈❛ ❋❳✧✮❀
          ♣r✐♠❛r②❙t❛❣❡✳s❡t❙❝❡♥❡✭s❝❡♥❡✮❀
          ♣r✐♠❛r②❙t❛❣❡✳s❤♦✇✭✮❀
     ⑥

     ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④
         ❧❛✉♥❝❤✭❛r❣s✮❀
     ⑥
⑥

    Ao executá-lo, teremos como resultado uma tela parecida com:




                                                                           25


[PAGINA 36]
2.4. Uma listagem de produtos                                  Casa do Código




          Fig. 2.11: Listagem de produtos com os elementos alinhados.




26


[PAGINA 37]
Casa do Código                                               Capítulo 2. Java FX




  Usando @SuppressWarnings no Eclipse

    Para evitar os diversos alertas (warnings) em amarelo no Eclipse, você
  pode adicionar sob a sua classe a anotação @SuppressWarnings:

  ❅❙✉♣♣r❡ss❲❛r♥✐♥❣s✭④ ✧✉♥❝❤❡❝❦❡❞✧✱ ✧r❛✇t②♣❡s✧ ⑥✮
  ♣✉❜❧✐❝ ❝❧❛ss ▼❛✐♥ ❡①t❡♥❞s ❆♣♣❧✐❝❛t✐♦♥ ④

  ❅❖✈❡rr✐❞❡
  ♣✉❜❧✐❝ ✈♦✐❞ st❛rt✭❙t❛❣❡ ♣r✐♠❛r②❙t❛❣❡✮ ④

       ●r♦✉♣ ❣r♦✉♣ ❂ ♥❡✇ ●r♦✉♣✭✮❀
       ❙❝❡♥❡ s❝❡♥❡ ❂ ♥❡✇ ❙❝❡♥❡✭❣r♦✉♣✱ ✻✾✵✱ ✺✶✵✮❀

       ✴✴ r❡st❛♥t❡ ❞♦ ❝ó❞✐❣♦ ♦♠✐t✐❞♦
  ⑥

      Esses warnings acontecem por causa dos parâmetros genéricos, que
  optamos não passar para simplificar e evitar tanta repetição em nosso
  código. Não se preocupe com isso, voltaremos a falar disso no final do
  livro. Por enquanto, você pode deixar os warnings (o código funcionará
  normalmente), ou adicionar a anotação @SuppressWarnings.


    Excelente, já temos uma interface visual para nosso projeto. Ao decorrer
do livro, trabalharemos com leitura e escrita em arquivos, acesso a banco de
dados e mais. A cada novo capítulo uma ou mais novas funcionalidades serão
adicionadas à nossa aplicação.




                                                                             27


[PAGINA 38]
2.4. Uma listagem de produtos                                Casa do Código




  Mais sobre Java Fx

      Se você gostou do Java FX e quiser estudar um pouco mais a fundo,
  talvez queira dar uma olhada em sua página no site da Oracle:
      http://www.oracle.com/technetwork/java/javase/overview/
  javafx-overview-2158620.html?ssSourceSiteId=otnpt
      Nela você encontra um overview sobre a tecnologia e links para doc-
  umentação, exemplos e muito mais.




28


[PAGINA 39]
Capítulo 3

Java IO
3.1    Entrada e saída de dados
Nossa listagem ainda trabalha com valores fixos, definidos no
RepositorioDeProdutos. Apesar disso, já queremos adicionar uma
função de exportar os dados dessa listagem para um arquivo de texto. Ao
clicar no botão de exportar, um arquivo deverá ser gerado com os dados da
listagem.
     Trabalhar com entrada e saída de dados é uma necessidade completa-
mente natural nos mais diferentes tipos de projetos. Ler valores digitados pelo
teclado, ler ou escrever em um arquivo de diferentes formatos etc., conhecer
a API de controle de entrada e saída, ou IO como é comumente chamada, é
um passo fundamental. Esse será nosso objetivo durante esse capítulo.


[PAGINA 40]
3.2. Lendo um arquivo de texto                                 Casa do Código


3.2 Lendo um arquivo de texto
Já vamos começar de forma prática, queremos ler o conteúdo de um arquivo.
Para começar a testar, crie na raiz do seu projeto (pasta livraria-fx) um
arquivo chamado teste.txt.
    Adicione nesse arquivo o seguinte conteúdo:

❊ss❡ é ✉♠ t❡st❡ ❞❡ ❧❡✐t✉r❛ ❞❡ ❛rq✉✐✈♦
◗✉❡r❡♠♦s ❧❡r ♦ ❝♦♥t❡ú❞♦ ❞❡ t♦❞❛s ❛s ❧✐♥❤❛s
▼❛s ❝♦♠♦ ❧❡r ❛rq✉✐✈♦s ❡♠ ❏❛✈❛❄

    Uma forma de ler o arquivo seria utilizando um FileInputStream,
responsável por fazer a leitura de bytes de um arquivo. O construtor dessa
classe nos obriga passar o nome do arquivo que será lido, que neste caso será
teste.txt:

tr② ④
    ■♥♣✉t❙tr❡❛♠ ✐s ❂ ♥❡✇ ❋✐❧❡■♥♣✉t❙tr❡❛♠✭✧t❡st❡✳t①t✧✮❀
⑥ ❝❛t❝❤ ✭❋✐❧❡◆♦t❋♦✉♥❞❊①❝❡♣t✐♦♥ ❡✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❆rq✉✐✈♦ ♥ã♦ ❡♥❝♦♥tr❛❞♦ ✧✰ ❡✮❀
⑥

    Quando estamos trabalhando com o pacote java.io, grande parte de
seus métodos lançam IOException. Como essa é uma Checked Exception
(não evitável), somos obrigados a tratá-la ou declará-la com um throws. Em
meu exemplo, eu optei por tratar, imprimindo uma mensagem amigável no
console.
    Outro detalhe importante é que declaramos o tipo da classe
FileInputStream como InputStream, que é sua superclasse. Essa
é uma classe abstrata e tem diversas outras implementações, como
AudioInputStream e ByteArrayInputStream.




30


[PAGINA 41]
Casa do Código                                                    Capítulo 3. Java IO




                 Fig. 3.1: InputStream e algumas de suas subclasses



    A grande ideia do InputStream é que ela implementa o comporta-
mento em comum entre os diferentes tipos de entrada. Além de ler um
arquivo de texto, podemos precisar ler de um áudio, uma conexão remota
(com sockets) etc. Cada tipo de leitura terá suas particularidades, mas a classe
InputStream define o comportamento padrão entre elas.
    Qual a vantagem dessa abstração? É bem simples, podemos tirar proveito
do polimorfismo. Imagine um método que recebe um InputStream para
fazer uma leitura de bytes. De onde os dados virão? De um txt? De um
blob do banco de dados? Não importa. Independente de onde os dados vêm,
o processo de leitura será o mesmo. Quando precisarmos ler bytes, não im-
portando de onde, poderemos chamar um método que aceita qualquer im-
plementação de InputStream.




                                                                                  31


[PAGINA 42]
3.2. Lendo um arquivo de texto                                 Casa do Código




         Fig. 3.2: Método recebendo um InputStream como parâmetro.



     O padrão de projeto template method

         Essa abstração utilizada na classe InputStream ilustra um padrão
     de projeto, ou Design Pattern, bastante conhecido e interessante. Estamos
     falando do Template Method.
         Há um post no blog da Caelum que se aprofunda bem nesse exemplo:
         http://blog.caelum.com.br/design-patterns-no-java-se-o-template-method/



    O mesmo acontece com OutputStream, que logo veremos. Assim
como usaremos InputStream para leitura de bytes, podemos usar o
OutputStream para escrita. O pacote de java.io usa e abusa da orien-
tação a objetos, com classes abstratas, interfaces e muito polimorfismo.
    Para concluir a leitura do arquivo, precisamos transformar os bytes desse
arquivo em unicode, guardando um conjunto de chars. Em seguida, con-
catenar esse conjunto de chars para formar as Strings com o conteúdo de
cada uma de suas linhas.
    Parece bem trabalhoso, não é? Mas a API é bem simples, você verá que
esse código é bem padrão. Logo também veremos algumas classes do pacote
java.util que simplificam todo esse processo, mas primeiro, é importante
entendê-lo.

32


[PAGINA 43]
Casa do Código                                                 Capítulo 3. Java IO



    De forma visual, o fluxo padrão de entrada é:




                 Fig. 3.3: Etapas do fluxo padrão de entrada



    E as responsáveis por esse trabalho:




        Fig. 3.4: InputStream, InputStreamReader e BufferedReader



   Já conhecemos a InputStream. As classes InputStreamReader e
BufferedReader são as responsáveis por fazer o restante do trabalho, ler
chars e transformá-las em Strings:

tr② ④
    ■♥♣✉t❙tr❡❛♠ ✐s ❂ ♥❡✇ ❋✐❧❡■♥♣✉t❙tr❡❛♠✭✧t❡st❡✳t①t✧✮❀
    ■♥♣✉t❙tr❡❛♠❘❡❛❞❡r ✐sr ❂ ♥❡✇ ■♥♣✉t❙tr❡❛♠❘❡❛❞❡r✭✐s✮❀
    ❇✉❢❢❡r❡❞❘❡❛❞❡r r❡❛❞❡r ❂ ♥❡✇ ❇✉❢❢❡r❡❞❘❡❛❞❡r✭✐sr✮❀
    ❙tr✐♥❣ ❧✐♥❤❛ ❂ r❡❛❞❡r✳r❡❛❞▲✐♥❡✭✮❀
    ✇❤✐❧❡ ✭❧✐♥❤❛ ✦❂ ♥✉❧❧✮ ④
        ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❧✐♥❤❛✮❀
        ❧✐♥❤❛ ❂ r❡❛❞❡r✳r❡❛❞▲✐♥❡✭✮❀
    ⑥
    r❡❛❞❡r✳❝❧♦s❡✭✮❀
⑥ ❝❛t❝❤ ✭■❖❊①❝❡♣t✐♦♥ ❡✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❊rr♦ ❛♦ t❡♥t❛r ❧❡r ♦ ❛rq✉✐✈♦ ✧ ✰ ❡✮❀
⑥

    A cada chamada, o método readLine lê uma linha e muda o cursor para
a próxima, até que o arquivo acabe. Neste caso, retornará null.


                                                                               33


[PAGINA 44]
3.3. Lendo texto do teclado com System.in                     Casa do Código


    Escreva e execute esse código e você verá que todas as linhas do arquivo
serão impressas no console. Legal, não é?


3.3 Lendo texto do teclado com System.in
Quer uma prova de que a abstração utilizada no InputStream é interes-
sante? Veja como é simples mudar nosso código para que passe a ler do
teclado em vez de um arquivo:

tr② ④
    ■♥♣✉t❙tr❡❛♠ ✐s ❂ ❙②st❡♠✳✐♥❀
    ■♥♣✉t❙tr❡❛♠❘❡❛❞❡r ✐sr ❂ ♥❡✇ ■♥♣✉t❙tr❡❛♠❘❡❛❞❡r✭✐s✮❀
    ❇✉❢❢❡r❡❞❘❡❛❞❡r r❡❛❞❡r ❂ ♥❡✇ ❇✉❢❢❡r❡❞❘❡❛❞❡r✭✐sr✮❀
    ❙tr✐♥❣ ❧✐♥❤❛ ❂ r❡❛❞❡r✳r❡❛❞▲✐♥❡✭✮❀
    ✇❤✐❧❡ ✭❧✐♥❤❛ ✦❂ ♥✉❧❧✮ ④
        ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❧✐♥❤❛✮❀
        ❧✐♥❤❛ ❂ r❡❛❞❡r✳r❡❛❞▲✐♥❡✭✮❀
    ⑥
    r❡❛❞❡r✳❝❧♦s❡✭✮❀
⑥ ❝❛t❝❤ ✭■❖❊①❝❡♣t✐♦♥ ❡✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❊rr♦ ❛♦ t❡♥t❛r ❧❡r ♦ ❛rq✉✐✈♦ ✧ ✰ ❡✮❀
⑥

    Percebeu a diferença? Ela está apenas na primeira linha, quando
declaramos o InputStream. Tudo que precisamos fazer foi utilizar o
System.in, que é a implementação do InputStream responsável por esse
tipo de leitura, do teclado.
    Execute o método para ver o resultado. O console ficará em branco, es-
perando que um texto seja digitado. Digite qualquer coisa e pressione Enter,
o valor será impresso de volta no console. Perceba que, diferente de quando
estamos lendo de um arquivo, neste caso a linha nunca será nula. Portanto,
o código ficará em looping, sempre esperando uma nova entrada.




34


[PAGINA 45]
Casa do Código                                             Capítulo 3. Java IO




                 Fig. 3.5: Exemplo de saída do System.in




                                                                           35


[PAGINA 46]
3.4. Tornando tudo mais simples com Scanner                     Casa do Código




 Encerrando execução manualmente ou com EOF

    Para parar a aplicação que está em looping, aguardando a próxima
 entrada do teclado, você pode pelo Eclipse clicar no ícone de stop.




                 Fig. 3.6: Como interromper a execução pelo Eclipse


    Outra alternativa seria mandar um sinal de fim de stream, o con-
 hecido EOF (end of file). Em sistemas operacionais de base :Unix, como
 Linux e Mac OS, você faz isso com o comando Control + D. Pelo Win-
 dows o comando será Control + Z.


3.4      Tornando tudo mais simples com Scanner
É muito interessante conhecer essa anatomia do InputStream para entrada
de dados, mas a realidade é que dessa forma o processo é muito verboso, com
todas essas etapas. Há uma maneira mais atual e interessante.
    Podemos fazer a mesma leitura do arquivo teste.txt utilizando a
classe Scanner, presente no pacote java.util. Repare como o código
é mais declarativo:

❙❝❛♥♥❡r s❝ ❂ ♥❡✇ ❙❝❛♥♥❡r✭♥❡✇ ❋✐❧❡✭✧t❡st❡✳t①t✧✮✮❀
✇❤✐❧❡ ✭s❝✳❤❛s◆❡①t▲✐♥❡✭✮✮ ④


36


[PAGINA 47]
Casa do Código                                                 Capítulo 3. Java IO



      ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭s❝✳♥❡①t▲✐♥❡✭✮✮❀
⑥

    Execute o código e você perceberá que a saída será a mesma. Muito
mais simples, não acha? O java.util.Scanner surgiu no Java 5 e tem
uma série de métodos úteis para facilitar seu trabalho com leitura de um
InputStream. Métodos como nextDouble, que já lê os bytes e faz a con-
versão, podem ser bastante convenientes no trabalho do dia a dia.


    Conhecendo a API

       Durante a leitura, não deixe de se aprofundar ainda mais pelo
    assunto consultando a documentação das classes mencionadas. O
    java.util.Scanner, por exemplo, está bem documentado em:
       http://docs.oracle.com/javase/8/docs/api/java/util/Scanner.html
       Veja que a própria documentação da classe, logo no início, já mostra
    alguns trechos de código como exemplo.

     Note como fica nosso código de entrada do teclado com essa classe:
❙❝❛♥♥❡r s❝ ❂ ♥❡✇ ❙❝❛♥♥❡r✭❙②st❡♠✳✐♥✮❀
❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❉✐❣✐t❡ s❡✉ ♥♦♠❡✧✮❀
❙tr✐♥❣ ♥♦♠❡❉✐❣✐t❛❞♦ ❂ s❝✳♥❡①t▲✐♥❡✭✮❀
❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❉✐❣✐t❡ s✉❛ ✐❞❛❞❡✧✮❀
✐♥t ✐❞❛❞❡❉✐❣✐t❛❞❛ ❂ s❝✳♥❡①t■♥t✭✮❀
❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧◆♦♠❡✿ ✧ ✰ ♥♦♠❡❉✐❣✐t❛❞♦✮❀
❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧■❞❛❞❡✿ ✧ ✰ ✐❞❛❞❡❉✐❣✐t❛❞❛✮❀

    Bastou mudar o InputStream passado no construtor do Scanner para
o System.in, que já vimos. Note também que estamos utilizando o método
nextInt para recuperar o valor e já converter para um inteiro, caso contrário
seria necessário fazer essa conversão manualmente. Por exemplo:
❙tr✐♥❣ ✐❞❛❞❡❉✐❣✐t❛❞❛ ❂ s❝✳♥❡①t▲✐♥❡✭✮❀
✐♥t ✐❞❛❞❡ ❂ ■♥t❡❣❡r✳♣❛rs❡■♥t✭✐❞❛❞❡❉✐❣✐t❛❞❛✮❀

   Exercite esse código para ir se familiarizando com a API, escreva e execute
em seu projeto. Um exemplo de saída seria:

                                                                               37


[PAGINA 48]
3.5. Saída de dados e o OutputStream                           Casa do Código


❉✐❣✐t❡ s❡✉ ♥♦♠❡
    ❃ ❘♦❞r✐❣♦ ❚✉r✐♥✐
❉✐❣✐t❡ s✉❛ ✐❞❛❞❡
    ❃ ✷✺
◆♦♠❡✿ ❘♦❞r✐❣♦ ❚✉r✐♥✐
■❞❛❞❡✿ ✷✺


3.5      Saída de dados e o OutputStream
O processo de escrita (saída de dados) é muito parecido, mas no lu-
gar de InputStream, InputStreamReader e BufferedReader,
temos respectivamente o OutputStream, OutputStreamWriter e
BufferedWriter.




         Fig. 3.7: OutputStream, OutputStreamWriter e BufferedWriter



      Um exemplo de uso seria:

❖✉t♣✉t❙tr❡❛♠ ♦s ❂ ♥❡✇ ❋✐❧❡❖✉t♣✉t❙tr❡❛♠✭✧s❛✐❞❛✳t①t✧✮❀
❖✉t♣✉t❙tr❡❛♠❲r✐t❡r ♦s✇ ❂ ♥❡✇ ❖✉t♣✉t❙tr❡❛♠❲r✐t❡r✭♦s✮❀
❇✉❢❢❡r❡❞❲r✐t❡r ❜✇ ❂ ♥❡✇ ❇✉❢❢❡r❡❞❲r✐t❡r✭♦s✇✮❀

    Note que, agora, no lugar de ler de um arquivo existente, estamos criando
um novo, neste caso chamado saida.txt. Também somos obrigados a pas-
sar essa informação no construtor da classe FileOutputStream.
    Por sinal, note novamente o polimorfismo em ação. Usamos um
FileOutputStream, mas dissemos que seu tipo é OutputStream. Há
uma implementação para cada tipo de escrita:




38


[PAGINA 49]
Casa do Código                                                Capítulo 3. Java IO




             Fig. 3.8: OutputStream e algumas de suas subclasses



    Podemos utilizar o método write para escrita do arquivo, mas ele não
faz uma quebra de linha. Uma alternativa para isso seria chamar o método
newLine, que carrega essa responsabilidade.

❜✇✳✇r✐t❡✭✧❚❡st❛♥❞♦ ❛ ❡s❝r✐t❛ ❡♠ ❛rq✉✐✈♦✧✮❀
❜✇✳♥❡✇▲✐♥❡✭✮❀
❜✇✳✇r✐t❡✭✧❈♦♥t❡ú❞♦ ♥❛ ♣ró①✐♠❛ ❧✐♥❤❛✧✮❀

    Ou simplesmente concatenar um /n na String:

❜✇✳✇r✐t❡✭✧❚❡st❛♥❞♦ ❛ ❡s❝r✐t❛ ❡♠ ❛rq✉✐✈♦❭♥✧✮❀
❜✇✳✇r✐t❡✭✧❈♦♥t❡ú❞♦ ♥❛ ♣ró①✐♠❛ ❧✐♥❤❛✧✮❀




                                                                              39


[PAGINA 50]
3.5. Saída de dados e o OutputStream                           Casa do Código




  Fechando o arquivo com close

       É fundamental sempre fecharmos o arquivo, chamando seu método
  close. Ao chamar o método close de um BufferedWriter,
  ele já fará o trabalho de fechar o OutputStreamWriter e
  FileOutputStream para você. Em cascata.
     Caso você se esqueça de fechar o arquivo nesse exemplo, que é um
  programa minúsculo, ele provavelmente não vai fazer a escrita no ar-
  quivo (os bytes ficam no buffer do escritor). Se for uma aplicação maior,
  o próprio Java fechará o BufferedWriter para você em algum mo-
  mento (por causa do garbage collector, que veremos mais à frente). Mas
  nunca devemos deixar de fechar um arquivo esperando que isso acon-
  teça, sempre devemos chamar o close quando terminarmos de fazer
  uma escrita ou leitura (um io).
     No próximo capítulo, veremos uma forma bem interessante de
  fechar recursos, como um arquivo ou mesmo uma conexão com
  banco de dados. Vamos aprender que isso pode e deve ser feito
  em um bloco finally, ou ainda com um recurso conhecido como
  try-with-resources.


    Pronto, agora que já sabemos isso podemos criar uma nova classe de teste
para ver esse código em ação. Crie a classe TesteSaida para fazer alguns
testes, ela pode se parecer com:

♣✉❜❧✐❝ ❝❧❛ss ❚❡st❡❙❛✐❞❛ ④

      ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮
              t❤r♦✇s ■❖❊①❝❡♣t✐♦♥ ④

            ❖✉t♣✉t❙tr❡❛♠ ♦s ❂ ♥❡✇ ❋✐❧❡❖✉t♣✉t❙tr❡❛♠✭✧s❛✐❞❛✳t①t✧✮❀
            ❖✉t♣✉t❙tr❡❛♠❲r✐t❡r ♦s✇ ❂ ♥❡✇ ❖✉t♣✉t❙tr❡❛♠❲r✐t❡r✭♦s✮❀
            ❇✉❢❢❡r❡❞❲r✐t❡r ❜✇ ❂ ♥❡✇ ❇✉❢❢❡r❡❞❲r✐t❡r✭♦s✇✮❀

            ❜✇✳✇r✐t❡✭✧❚❡st❛♥❞♦ ❛ ❡s❝r✐t❛ ❡♠ ❛rq✉✐✈♦✧✮❀
            ❜✇✳♥❡✇▲✐♥❡✭✮❀

40


[PAGINA 51]
Casa do Código                                               Capítulo 3. Java IO



          ❜✇✳✇r✐t❡✭✧❈♦♥t❡ú❞♦ ♥❛ ♣ró①✐♠❛ ❧✐♥❤❛✧✮❀
          ❜✇✳❝❧♦s❡✭✮❀
     ⑥
⑥

    Execute o código para ver o resultado. Um ponto importante é que a IDE
normalmente não atualiza o seu projeto automaticamente se você criar um
arquivo por fora dela, portanto, não se esqueça de dar um F5 (refresh) no
projeto após executar a classe para que o arquivo saida.txt fique visível.




                   Fig. 3.9: Arquivo saida.txt no Eclipse



    Só por curiosidade, se quiser você pode testar mudar a implementação de
OutputStream, assim como fizemos no exemplo de escrita. Experimente
usar o System.out:

♣✉❜❧✐❝ ❝❧❛ss ❚❡st❡❙❛✐❞❛ ④

     ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮
             t❤r♦✇s ■❖❊①❝❡♣t✐♦♥ ④

          ❖✉t♣✉t❙tr❡❛♠ ♦s ❂ ❙②st❡♠✳♦✉t❀
          ❖✉t♣✉t❙tr❡❛♠❲r✐t❡r ♦s✇ ❂ ♥❡✇ ❖✉t♣✉t❙tr❡❛♠❲r✐t❡r✭♦s✮❀
          ❇✉❢❢❡r❡❞❲r✐t❡r ❜✇ ❂ ♥❡✇ ❇✉❢❢❡r❡❞❲r✐t❡r✭♦s✇✮❀



                                                                             41


[PAGINA 52]
3.6. Escrita mais simples com PrintStream                       Casa do Código


            ❜✇✳✇r✐t❡✭✧❚❡st❛♥❞♦ ❛ ❡s❝r✐t❛ ❡♠ ❛rq✉✐✈♦✧✮❀
            ❜✇✳♥❡✇▲✐♥❡✭✮❀
            ❜✇✳✇r✐t❡✭✧❈♦♥t❡ú❞♦ ♥❛ ♣ró①✐♠❛ ❧✐♥❤❛✧✮❀
            ❜✇✳❝❧♦s❡✭✮❀
      ⑥
⑥

    Simples, não é? A mudança foi mínima e já temos a capacidade de escr-
ever em outro local, além de um arquivo. A saída será:

❚❡st❛♥❞♦ ❛ ❡s❝r✐t❛ ❡♠ ❛rq✉✐✈♦
❈♦♥t❡ú❞♦ ♥❛ ♣ró①✐♠❛ ❧✐♥❤❛

   Mas, claro, nesse caso específico um System.out.println seria muito
mais simples. Por falar em simplicidade, veremos agora como simplificar esse
processo de escrita.


3.6       Escrita mais simples com PrintStream
Assim como o java.util.Scanner facilita o processo de leitura de bytes,
desde o Java 5 temos uma forma mais interessante de fazer esse processo de es-
crita, com a classe java.io.PrintStream. Repare como fica nosso código
utilizando-a:

Pr✐♥t❙tr❡❛♠ ♦✉t ❂ ♥❡✇ Pr✐♥t❙tr❡❛♠✭✧s❛✐❞❛✳t①t✧✮❀
♦✉t✳♣r✐♥t❧♥✭✧❚❡st❛♥❞♦ ❛ ❡s❝r✐t❛ ❡♠ ❛rq✉✐✈♦✧✮❀
♦✉t✳♣r✐♥t❧♥✭✧❈♦♥t❡ú❞♦ ♥❛ ♣ró①✐♠❛ ❧✐♥❤❛✧✮❀
♦✉t✳❝❧♦s❡✭✮❀

    Muito mais simples, não acha? Achou essa API familiar? Na verdade,
você provavelmente já vem usando indiretamente o PrintStream desde o
seu primeiro hello world em Java, pois este é o tipo do atributo out da classe
System. Repare:

Pr✐♥t❙tr❡❛♠ ♦✉t ❂ ❙②st❡♠✳♦✉t❀
♦✉t✳♣r✐♥t❧♥✭✧❛❣♦r❛ ❛ s❛í❞❛ é ♥♦ ❝♦♥s♦❧❡✧✮❀
♦✉t✳♣r✐♥t❧♥✭✧❈♦♥t❡ú❞♦ ♥❛ ♣ró①✐♠❛ ❧✐♥❤❛✧✮❀



42


[PAGINA 53]
Casa do Código                                                Capítulo 3. Java IO



    Ambas as classes Scanner e PrintStream facilitam bastante o pro-
cesso de entrada e saída de dados. Quer ler mais sobre essas duas classes?
Não deixe de conferir sua documentação:

    • http://docs.oracle.com/javase/8/docs/api/java/io/PrintStream.html

    • http://docs.oracle.com/javase/8/docs/api/java/util/Scanner.html


3.7 Gerando um CSV de produtos
Agora que já conhecemos um pouco da API de io, vamos adicionar um novo
comportamento em nossa listagem de produtos. Queremos exportar os pro-
dutos da listagem para um arquivo CSV. O termo CSV vem de comma sep-
arated value, ou seja, valores separados por vírgula. Esse formato é bastante
comum e utilizado no dia a dia.
    Queremos ao final ter um arquivo parecido com:

◆♦♠❡✱ ❉❡s❝r✐❝❛♦✱ ❱❛❧♦r✱ ■❙❇◆
❏❛✈❛ ✽ Prát✐❝♦✱ ◆♦✈♦s r❡❝✉rs♦s ❞❛ ❧✐♥❣✉❛❣❡♠✱ ✺✾✳✾✱
✾✼✽✲✽✺✲✻✻✷✺✵✲✹✻✲✻

    Vamos começar criando a classe Exportador, que será responsável por
esse trabalho. Ela terá um único método, chamado paraCSV, que receberá
um List de Produto como parâmetro:

♣✉❜❧✐❝ ❝❧❛ss ❊①♣♦rt❛❞♦r ④

     ♣✉❜❧✐❝ ✈♦✐❞ ♣❛r❛❈❙❱✭▲✐st❁Pr♦❞✉t♦❃ ♣r♦❞✉t♦s✮ ④

     ⑥
⑥

    Implementando esse método, nosso primeiro passo será criar um arquivo
produtos.csv e já colocar um cabeçalho com as informações que vamos
escrever. Podemos usar um PrintStream para fazer o trabalho, repare:

♣✉❜❧✐❝ ✈♦✐❞ ♣❛r❛❈❙❱✭▲✐st❁Pr♦❞✉t♦❃ ♣r♦❞✉t♦s✮
        t❤r♦✇s ■❖❊①❝❡♣t✐♦♥ ④

                                                                              43


[PAGINA 54]
3.7. Gerando um CSV de produtos                                 Casa do Código




     Pr✐♥t❙tr❡❛♠ ♣s ❂ ♥❡✇ Pr✐♥t❙tr❡❛♠✭✧♣r♦❞✉t♦s✳❝s✈✧✮❀
     ♣s✳♣r✐♥t❧♥✭✧◆♦♠❡✱ ❉❡s❝r✐❝❛♦✱ ❱❛❧♦r✱ ■❙❇◆✧✮❀

     ♣s✳❝❧♦s❡✭✮❀
⑥

    Já execute o código para ver o resultado. O arquivo deve ser criado na raiz
do seu projeto e por enquanto apenas com o conteúdo:

◆♦♠❡✱ ❉❡s❝r✐❝❛♦✱ ❱❛❧♦r✱ ■❙❇◆

   Excelente. Agora tudo o que precisamos fazer é iterar nessa lista de pro-
dutos adicionando uma linha para cada elemento, como por exemplo:

♣✉❜❧✐❝ ✈♦✐❞ ♣❛r❛❈❙❱✭▲✐st❁Pr♦❞✉t♦❃ ♣r♦❞✉t♦s✮
        t❤r♦✇s ■❖❊①❝❡♣t✐♦♥ ④

     Pr✐♥t❙tr❡❛♠ ♣s ❂ ♥❡✇ Pr✐♥t❙tr❡❛♠✭✧♣r♦❞✉t♦s✳❝s✈✧✮❀
     ♣s✳♣r✐♥t❧♥✭✧◆♦♠❡✱ ❉❡s❝r✐❝❛♦✱ ❱❛❧♦r✱ ■❙❇◆✧✮❀

     ❢♦r ✭Pr♦❞✉t♦ ♣r♦❞✉t♦ ✿ ♣r♦❞✉t♦s✮ ④
         ♣s✳♣r✐♥t❧♥✭♣r♦❞✉t♦✳❣❡t◆♦♠❡✭✮ ✰ ✧✱ ✧
             ✰ ♣r♦❞✉t♦✳❣❡t❉❡s❝r✐❝❛♦✭✮ ✰ ✧✱ ✧
             ✰ ♣r♦❞✉t♦✳❣❡t❱❛❧♦r✭✮ ✰ ✧✱ ✧
             ✰ ♣r♦❞✉t♦✳❣❡t■s❜♥✭✮✮❀
     ⑥
     ♣s✳❝❧♦s❡✭✮❀
⑥

    Isso já trará o resultado que esperamos. Mas o código esté bem feio, não
acha? Essa concatenação de Strings pode prejudicar bastante a legibilidade
e dificultar a manutenção de nosso código.




44


[PAGINA 55]
Casa do Código                                                     Capítulo 3. Java IO




    Usando o projeto do outro livro?

        Se, no lugar de baixar o projeto base, você estiver utilizando o projeto
    do livro Desbravando Java e Orientação a Objetos, você precisará modi-
    ficar sua interface Produto para que esse código compile.
        Ela deve ficar assim:

    ♣✉❜❧✐❝ ✐♥t❡r❢❛❝❡ Pr♦❞✉t♦
            ❡①t❡♥❞s ❈♦♠♣❛r❛❜❧❡❁Pr♦❞✉t♦❃ ④

          ❞♦✉❜❧❡ ❣❡t❱❛❧♦r✭✮❀
          ❙tr✐♥❣ ❣❡t◆♦♠❡✭✮❀
          ❙tr✐♥❣ ❣❡t❉❡s❝r✐❝❛♦✭✮❀
          ❙tr✐♥❣ ❣❡t■s❜♥✭✮❀
    ⑥



    Uma opção talvez mais interessante seria usar o String.format, como
a seguir:
♣✉❜❧✐❝ ✈♦✐❞ ♣❛r❛❈❙❱✭▲✐st❁Pr♦❞✉t♦❃ ♣r♦❞✉t♦s✮
        t❤r♦✇s ■❖❊①❝❡♣t✐♦♥ ④

        Pr✐♥t❙tr❡❛♠ ♣s ❂ ♥❡✇ Pr✐♥t❙tr❡❛♠✭✧♣r♦❞✉t♦s✳❝s✈✧✮❀
        ♣s✳♣r✐♥t❧♥✭✧◆♦♠❡✱ ❉❡s❝r✐❝❛♦✱ ❱❛❧♦r✱ ■❙❇◆✧✮❀

        ❢♦r ✭Pr♦❞✉t♦ ♣r♦❞✉t♦ ✿ ♣r♦❞✉t♦s✮ ④

               ♣s✳♣r✐♥t❧♥✭❙tr✐♥❣✳❢♦r♠❛t✭✧✪s✱ ✪s✱ ✪s✱ ✪s✧✱
                       ♣r♦❞✉t♦✳❣❡t◆♦♠❡✭✮✱
                       ♣r♦❞✉t♦✳❣❡t❉❡s❝r✐❝❛♦✭✮✱
                       ♣r♦❞✉t♦✳❣❡t❱❛❧♦r✭✮✱
                       ♣r♦❞✉t♦✳❣❡t■s❜♥✭✮✮✮❀
        ⑥
        ♣s✳❝❧♦s❡✭✮❀
⑥

        Ufa!     Um pouco melhor.         Claro, poderíamos ter usado um

                                                                                   45


[PAGINA 56]
3.7. Gerando um CSV de produtos                                 Casa do Código


StringBuilder,            StringJoiner etc., mas essa opção é bem sim-
ples e já resolve o problema. Vamos ver se está funcionando? Crie um
método main dentro dessa mesma classe para testar, ele pode ficar assim:

♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮
        t❤r♦✇s ■❖❊①❝❡♣t✐♦♥ ④

     ▲✐✈r♦ ❧✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦❋✐s✐❝♦✭♥❡✇ ❆✉t♦r✭✮✮❀
     ❧✐✈r♦✳s❡t◆♦♠❡✭✧❏❛✈❛ ✽ Prát✐❝♦✧✮❀
     ❧✐✈r♦✳s❡t❉❡s❝r✐❝❛♦✭✧◆♦✈♦s r❡❝✉rs♦s ❞❛ ❧✐♥❣✉❛❣❡♠✧✮❀
     ❧✐✈r♦✳s❡t❱❛❧♦r✭✺✾✳✾✵✮❀
     ❧✐✈r♦✳s❡t■s❜♥✭✧✾✼✽✲✽✺✲✻✻✷✺✵✲✹✻✲✻✧✮❀

     ▲✐✈r♦ ♠❛✐s❯♠❧✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦❋✐s✐❝♦✭♥❡✇ ❆✉t♦r✭✮✮❀
     ♠❛✐s❯♠❧✐✈r♦✳s❡t◆♦♠❡✭✧❉❡s❜r❛✈❛♥❞♦ ❛ ❖✳❖✳✧✮❀
     ♠❛✐s❯♠❧✐✈r♦✳s❡t❉❡s❝r✐❝❛♦✭✧▲✐✈r♦ ❞❡ ❏❛✈❛ ❡ ❖✳❖✧✮❀
     ♠❛✐s❯♠❧✐✈r♦✳s❡t❱❛❧♦r✭✺✾✳✾✵✮❀
     ♠❛✐s❯♠❧✐✈r♦✳s❡t■s❜♥✭✧✸✷✶✲✺✹✲✻✼✽✾✵✲✶✶✲✷✧✮❀

     ♥❡✇ ❊①♣♦rt❛❞♦r✭✮✳♣❛r❛❈❙❱✭❆rr❛②s✳❛s▲✐st✭❧✐✈r♦✱ ♠❛✐s❯♠❧✐✈r♦✮✮❀
⑥

     O resultado será o arquivo produtos.csv, com o seguinte conteúdo:

◆♦♠❡✱ ❉❡s❝r✐❝❛♦✱ ❱❛❧♦r✱ ■❙❇◆
❏❛✈❛ ✽ Prát✐❝♦✱ ◆♦✈♦s r❡❝✉rs♦s ❞❛ ❧✐♥❣✉❛❣❡♠✱ ✺✾✳✾✱
✾✼✽✲✽✺✲✻✻✷✺✵✲✹✻✲✻
❉❡s❜r❛✈❛♥❞♦ ❛ ❖❖✱ ▲✐✈r♦ ❞❡ ❏❛✈❛ ❡ ❖✳❖✱ ✺✾✳✾✱ ✸✷✶✲✺✹✲✻✼✽✾✵✲✶✶✲✷

    Não encontrou o arquivo? Lembre-se de dar um F5 (refresh) em seu
projeto para ele aparecer na IDE. Ou, se preferir, abra a pasta do seu projeto
direto pelo seu sistema operacional.




46


[PAGINA 57]
Casa do Código                                                  Capítulo 3. Java IO




         Fig. 3.10: Arquivo produtos.csv visto pelo sistema operacional



    Nossa classe Exportador ficou assim:

✐♠♣♦rt ❥❛✈❛✳✐♦✳■❖❊①❝❡♣t✐♦♥❀
✐♠♣♦rt ❥❛✈❛✳✐♦✳Pr✐♥t❙tr❡❛♠❀
✐♠♣♦rt ❥❛✈❛✳✉t✐❧✳▲✐st❀

✐♠♣♦rt ❜r✳❝♦♠✳❝❛s❛❞♦❝♦❞✐❣♦✳❧✐✈r❛r✐❛✳♣r♦❞✉t♦s✳Pr♦❞✉t♦❀

♣✉❜❧✐❝ ❝❧❛ss ❊①♣♦rt❛❞♦r ④

     ♣✉❜❧✐❝ ✈♦✐❞ ♣❛r❛❈❙❱✭▲✐st❁Pr♦❞✉t♦❃ ♣r♦❞✉t♦s✮
             t❤r♦✇s ■❖❊①❝❡♣t✐♦♥ ④

           Pr✐♥t❙tr❡❛♠ ♣s ❂ ♥❡✇ Pr✐♥t❙tr❡❛♠✭✧♣r♦❞✉t♦s✳❝s✈✧✮❀
           ♣s✳♣r✐♥t❧♥✭✧◆♦♠❡✱ ❉❡s❝r✐❝❛♦✱ ❱❛❧♦r✱ ■❙❇◆✧✮❀

           ❢♦r ✭Pr♦❞✉t♦ ♣r♦❞✉t♦ ✿ ♣r♦❞✉t♦s✮ ④

                 ♣s✳♣r✐♥t❧♥✭❙tr✐♥❣✳❢♦r♠❛t✭✧✪s✱ ✪s✱ ✪s✱ ✪s✧✱
                         ♣r♦❞✉t♦✳❣❡t◆♦♠❡✭✮✱
                         ♣r♦❞✉t♦✳❣❡t❉❡s❝r✐❝❛♦✭✮✱
                         ♣r♦❞✉t♦✳❣❡t❱❛❧♦r✭✮✱
                         ♣r♦❞✉t♦✳❣❡t■s❜♥✭✮✮✮❀
           ⑥
           ♣s✳❝❧♦s❡✭✮❀
     ⑥

                                                                               47


[PAGINA 58]
3.8. Botão de exportar produtos                                   Casa do Código


⑥


3.8 Botão de exportar produtos
Agora que já temos o código para exportar uma lista de produtos como um
CSV, podemos adicionar um botão em nossa listagem feita em Java FX para
disparar essa lógica. Isso é bem simples.
    O primeiro passo é criar um                    Button,   do pacote
javafx.scene.control. Opcionalmente, em seu construtor você já
pode passar o texto que quer exibir. Podemos fazer:

❇✉tt♦♥ ❜✉tt♦♥ ❂ ♥❡✇ ❇✉tt♦♥✭✧❊①♣♦rt❛r ❈❙❱✧✮❀

    Da mesma forma que fizemos com a label e tableView, precisamos
adicionar esse botão no cenário da página. Basta adicioná-lo como argu-
mento do método addAll:

❣r♦✉♣✳❣❡t❈❤✐❧❞r❡♥✭✮✳❛❞❞❆❧❧✭❧❛❜❡❧✱ ✈❜♦①✱ ❜✉tt♦♥✮❀

    Execute o código e você perceberá que ele já está na página, mas está de-
salinhado, cobrindo o texto da nossa lable:




                          Fig. 3.11: Button desalinhado na tela



    Bem, para alinhá-lo podemos envolver esse button em um VBox com
um padding definido, assim como fizemos com a tabela. Outra opção mais
simples é utilizar seus métodos setLayoutX e setLayoutY para definir
sua posição, algo como:

48


[PAGINA 59]
Casa do Código                                              Capítulo 3. Java IO



❇✉tt♦♥ ❜✉tt♦♥ ❂ ♥❡✇ ❇✉tt♦♥✭✧❊①♣♦rt❛r ❈❙❱✧✮❀
❜✉tt♦♥✳s❡t▲❛②♦✉t❳✭✺✼✺✮❀
❜✉tt♦♥✳s❡t▲❛②♦✉t❨✭✷✺✮❀

    Agora sim, o resultado será:




          Fig. 3.12: Button alinhado com setLayoutX e setLayoutY


    Mas note que ao clicar no botão nenhuma ação será executada. Faz sen-
tido, ainda não implementamos isso.


3.9    Adicionando ações com setOnAction
O método setOnAction é o responsável por definir as ações que serão ex-
ecutadas no momento do click de nosso Button. Podemos fazer:
❜✉tt♦♥✳s❡t❖♥❆❝t✐♦♥✭❄❄❄✮❀ ✴✴ ♦q❄

    Esse método espera receber uma instância do tipo EventHandler (in-
terface) como parâmetro. Sim, poderíamos criar uma classe que implemen-
tasse essa interface e passá-la como parâmetro, mas comumente fazemos isso
com uma classe anônima:
❜✉tt♦♥✳s❡t❖♥❆❝t✐♦♥✭♥❡✇ ❊✈❡♥t❍❛♥❞❧❡r❁❆❝t✐♦♥❊✈❡♥t❃✭✮ ④
    ❅❖✈❡rr✐❞❡
    ♣✉❜❧✐❝ ✈♦✐❞ ❤❛♥❞❧❡✭❆❝t✐♦♥❊✈❡♥t ❡✈❡♥t✮ ④
        ✴✴ ❛çã♦ ❛ s❡r ❡①❡❝✉t❛❞❛
    ⑥
⑥✮❀



                                                                           49


[PAGINA 60]
3.9. Adicionando ações com setOnAction                        Casa do Código


Classe anônima
    Se você não está acostumado ou nunca viu classes anônimas, não se pre-
ocupe. Apesar de um tanto feias, elas são bem simples de entender. No lugar
de usar uma classe anônima, poderíamos ter criado uma classe que imple-
mentasse EventHandler<ActionEvent>:

♣✉❜❧✐❝ ❝❧❛ss ❆❝❛♦❉♦❇♦t❛♦
    ✐♠♣❧❡♠❡♥ts ❊✈❡♥t❍❛♥❞❧❡r❁❆❝t✐♦♥❊✈❡♥t❃ ④

     ❅❖✈❡rr✐❞❡
     ♣✉❜❧✐❝ ✈♦✐❞ ❤❛♥❞❧❡✭❆❝t✐♦♥❊✈❡♥t ❡✈❡♥t✮ ④
         ✴✴ ❛çã♦ ❛ s❡r ❡①❡❝✉t❛❞❛
     ⑥
⑥

     Poderíamos usá-la assim:

❜✉tt♦♥✳s❡t❖♥❆❝t✐♦♥✭♥❡✇ ❆❝❛♦❉♦❇♦t❛♦✭✮✮❀

    O problema desse código é que cada botão pode ter uma ação que não vai
se repetir em nenhum outro momento do código, só será usada aqui. Além
disso, podemos ter vários botões; teríamos que criar uma classe nova para
fazer a ação de cada um deles?
    Aqui que entra a classe anônima! No lugar de criar uma classe, digamos
que convencional, podemos instanciar diretamente a interface e já instanciar
seus métodos ali mesmo. Essa instância criada é fruto de uma classe anônima,
uma classe que nem tem um nome.
    Agora, voltando ao botão. Queremos portanto adicionar a ação do click
dentro do método handle, que estamos implementando na classe anônima.
Vamos começar com um exemplo simples, apenas mostrando uma mensagem
no console:

❜✉tt♦♥✳s❡t❖♥❆❝t✐♦♥✭♥❡✇ ❊✈❡♥t❍❛♥❞❧❡r❁❆❝t✐♦♥❊✈❡♥t❃✭✮ ④
    ❅❖✈❡rr✐❞❡
    ♣✉❜❧✐❝ ✈♦✐❞ ❤❛♥❞❧❡✭❆❝t✐♦♥❊✈❡♥t ❡✈❡♥t✮ ④
        ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❈❧✐❝❦✦✧✮❀
    ⑥
⑥✮❀

50


[PAGINA 61]
Casa do Código                                                    Capítulo 3. Java IO



   Para testar, execute a aplicação e pressione o botão Exportar CSV al-
gumas vezes, você verá que a cada click o texto será impresso.
   O que queremos na verdade é exportar todos os nossos produtos como
um CSV, portanto, fazemos:

❜✉tt♦♥✳s❡t❖♥❆❝t✐♦♥✭♥❡✇ ❊✈❡♥t❍❛♥❞❧❡r❁❆❝t✐♦♥❊✈❡♥t❃✭✮ ④
    ❅❖✈❡rr✐❞❡
    ♣✉❜❧✐❝ ✈♦✐❞ ❤❛♥❞❧❡✭❆❝t✐♦♥❊✈❡♥t ❡✈❡♥t✮ ④
        ♥❡✇ ❊①♣♦rt❛❞♦r✭✮✳♣❛r❛❈❙❱✭♣r♦❞✉t♦s✮❀
    ⑥
⑥✮❀

    Mas, espera! Esse código ainda não compila. Como o método paraCSV
lança uma IOException, precisamos tratá-la ou declará-la. Vamos tratar:

❜✉tt♦♥✳s❡t❖♥❆❝t✐♦♥✭♥❡✇ ❊✈❡♥t❍❛♥❞❧❡r❁❆❝t✐♦♥❊✈❡♥t❃✭✮ ④
    ❅❖✈❡rr✐❞❡
    ♣✉❜❧✐❝ ✈♦✐❞ ❤❛♥❞❧❡✭❆❝t✐♦♥❊✈❡♥t ❡✈❡♥t✮ ④
        tr② ④
            ♥❡✇ ❊①♣♦rt❛❞♦r✭✮✳♣❛r❛❈❙❱✭♣r♦❞✉t♦s✮❀
        ⑥ ❝❛t❝❤ ✭■❖❊①❝❡♣t✐♦♥ ❡✮ ④
            ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❊rr♦ ❛♦ ❡①♣♦rt❛r✿ ✧✰ ❡✮❀
        ⑥
    ⑥
⑥✮❀

   Pronto! Coloque esse código em ação, basta clicar no botão Exportar
CSV que o arquivo produtos.csv será criado na raiz de seu projeto.




                 Fig. 3.13: Projeto com arquivo produtos.csv criado



                                                                                  51


[PAGINA 62]
3.10. JavaFx e Java 8                                         Casa do Código


3.10        JavaFx e Java 8
Que tal dar um toque de Java 8 nesse código? Os novos recursos dessa ver-
são deixam o código do Java FX bem mais enxuto e interessante. Quer um
exemplo? Dê uma boa olhada novamente na classe anônima que criamos no
setOnAction do botão de exportar:

❜✉tt♦♥✳s❡t❖♥❆❝t✐♦♥✭♥❡✇ ❊✈❡♥t❍❛♥❞❧❡r❁❆❝t✐♦♥❊✈❡♥t❃✭✮ ④
    ❅❖✈❡rr✐❞❡
    ♣✉❜❧✐❝ ✈♦✐❞ ❤❛♥❞❧❡✭❆❝t✐♦♥❊✈❡♥t ❡✈❡♥t✮ ④
        tr② ④
            ♥❡✇ ❊①♣♦rt❛❞♦r✭✮✳♣❛r❛❈❙❱✭♣r♦❞✉t♦s✮❀
        ⑥ ❝❛t❝❤ ✭■❖❊①❝❡♣t✐♦♥ ❡✮ ④
            ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❊rr♦ ❛♦ ❡①♣♦rt❛r✿ ✧✰ ❡✮❀
        ⑥
    ⑥
⑥✮❀

     Que tal escrevê-lo como a seguir, utilizando uma expressão lambda?

❜✉tt♦♥✳s❡t❖♥❆❝t✐♦♥✭❡✈❡♥t ✲❃ ④
    tr② ④
        ♥❡✇ ❊①♣♦rt❛❞♦r✭✮✳♣❛r❛❈❙❱✭♣r♦❞✉t♦s✮❀
    ⑥ ❝❛t❝❤ ✭■❖❊①❝❡♣t✐♦♥ ❡✮ ④
        ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❊rr♦ ❛♦ ❡①♣♦rt❛r✿ ✧✰ ❡✮❀
    ⑥
⑥✮❀

    Cortamos o código quase pela metade! Mas nem sempre menos linhas de
código significa melhora, temos que considerar que isso pode diminuir um
pouco a legibilidade. Para deixar esse código um pouco mais limpo, vamos
extrair um método. Podemos chamá-lo de exportaEmCSV:

♣r✐✈❛t❡ ✈♦✐❞ ❡①♣♦rt❛❊♠❈❙❱✭❖❜s❡r✈❛❜❧❡▲✐st❁Pr♦❞✉t♦❃ ♣r♦❞✉t♦s✮ ④
    tr② ④
        ♥❡✇ ❊①♣♦rt❛❞♦r✭✮✳♣❛r❛❈❙❱✭♣r♦❞✉t♦s✮❀
    ⑥ ❝❛t❝❤ ✭■❖❊①❝❡♣t✐♦♥ ❡✮ ④
        ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❊rr♦ ❛♦ ❡①♣♦rt❛r✿ ✧✰ ❡✮❀
    ⑥
⑥

52


[PAGINA 63]
Casa do Código                                                  Capítulo 3. Java IO



    A expressão lambda ficará assim:

❜✉tt♦♥✳s❡t❖♥❆❝t✐♦♥✭❡✈❡♥t ✲❃ ❡①♣♦rt❛❊♠❈❙❱✭♣r♦❞✉t♦s✮✮❀

     Temos agora uma linha de código! E ela é bastante declarativa> temos um
evento como parâmetro e queremos chamar o método exportaEmCSV,
passando a lista de produtos. Muito mais enxuto e legível, não acha?
     Claro, o Java 8 vai muito além disso. Há diversas outras novidades. Está
curioso para conhecer algumas delas? Então com certeza você vai gostar do
livro que escrevi junto com o Paulo Silveira, o Java 8 Prático Lambdas, Streams
e os novos recursos da linguagem.
     http://www.casadocodigo.com.br/products/livro-java8
     Apesar de estarmos usando algumas coisas do Java 8 nos exemplos desse
livro, esse não é nosso foco. Você que não tem o Java 8 instalado pode manter
a sintaxe das classes anônimas. Eu sempre procuro mostrar das duas formas
para que você consiga acompanhar independente da sua versão do Java. Ok?
     Nesse ponto, o código final da classe Main está assim:

❅❙✉♣♣r❡ss❲❛r♥✐♥❣s✭④ ✧✉♥❝❤❡❝❦❡❞✧✱ ✧r❛✇t②♣❡s✧ ⑥✮
♣✉❜❧✐❝ ❝❧❛ss ▼❛✐♥ ❡①t❡♥❞s ❆♣♣❧✐❝❛t✐♦♥ ④

     ❅❖✈❡rr✐❞❡
     ♣✉❜❧✐❝ ✈♦✐❞ st❛rt✭❙t❛❣❡ ♣r✐♠❛r②❙t❛❣❡✮ ④

          ●r♦✉♣ ❣r♦✉♣ ❂ ♥❡✇ ●r♦✉♣✭✮❀
          ❙❝❡♥❡ s❝❡♥❡ ❂ ♥❡✇ ❙❝❡♥❡✭❣r♦✉♣✱ ✻✾✵✱ ✺✶✵✮❀

          ❖❜s❡r✈❛❜❧❡▲✐st❁Pr♦❞✉t♦❃ ♣r♦❞✉t♦s ❂
              ♥❡✇ ❘❡♣♦s✐t♦r✐♦❉❡Pr♦❞✉t♦s✭✮✳❧✐st❛✭✮❀

          ❚❛❜❧❡❱✐❡✇❁Pr♦❞✉t♦❃ t❛❜❧❡❱✐❡✇ ❂ ♥❡✇ ❚❛❜❧❡❱✐❡✇❁❃✭♣r♦❞✉t♦s✮❀

          ❚❛❜❧❡❈♦❧✉♠♥ ♥♦♠❡❈♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭✧◆♦♠❡✧✮❀
          ♥♦♠❡❈♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭✶✽✵✮❀
          ♥♦♠❡❈♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
              ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②✭✧♥♦♠❡✧✮✮❀

          ❚❛❜❧❡❈♦❧✉♠♥ ❞❡s❝❈♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭✧❉❡s❝r✐çã♦✧✮❀

                                                                                53


[PAGINA 64]
3.10. JavaFx e Java 8                                       Casa do Código


             ❞❡s❝❈♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭✷✸✵✮❀
             ❞❡s❝❈♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
                 ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②✭✧❞❡s❝r✐❝❛♦✧✮✮❀

             ❚❛❜❧❡❈♦❧✉♠♥ ✈❛❧♦r❈♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭✧❱❛❧♦r✧✮❀
             ✈❛❧♦r❈♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭✻✵✮❀
             ✈❛❧♦r❈♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
                 ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②✭✧✈❛❧♦r✧✮✮❀

             ❚❛❜❧❡❈♦❧✉♠♥ ✐s❜♥❈♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭✧■❙❇◆✧✮❀
             ✐s❜♥❈♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭✶✽✵✮❀
             ✐s❜♥❈♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
                 ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②✭✧✐s❜♥✧✮✮❀

             t❛❜❧❡❱✐❡✇✳❣❡t❈♦❧✉♠♥s✭✮✳❛❞❞❆❧❧✭♥♦♠❡❈♦❧✉♠♥✱ ❞❡s❝❈♦❧✉♠♥✱
                 ✈❛❧♦r❈♦❧✉♠♥✱ ✐s❜♥❈♦❧✉♠♥✮❀

             ❢✐♥❛❧ ❱❇♦① ✈❜♦① ❂ ♥❡✇ ❱❇♦①✭t❛❜❧❡❱✐❡✇✮❀
             ✈❜♦①✳s❡tP❛❞❞✐♥❣✭♥❡✇ ■♥s❡ts✭✼✵✱ ✵✱ ✵ ✱✶✵✮✮❀

             ▲❛❜❡❧ ❧❛❜❡❧ ❂ ♥❡✇ ▲❛❜❡❧✭✧▲✐st❛❣❡♠ ❞❡ ▲✐✈r♦s✧✮❀

             ❧❛❜❡❧✳s❡t❋♦♥t✭❋♦♥t
                 ✳❢♦♥t✭✧▲✉❝✐❞❛ ●r❛♥❞❡✧✱ ❋♦♥tP♦st✉r❡✳❘❊●❯▲❆❘✱ ✸✵✮✮❀

             ❧❛❜❡❧✳s❡tP❛❞❞✐♥❣✭♥❡✇ ■♥s❡ts✭✷✵✱ ✵✱ ✶✵✱ ✶✵✮✮❀

             ❇✉tt♦♥ ❜✉tt♦♥ ❂ ♥❡✇ ❇✉tt♦♥✭✧❊①♣♦rt❛r ❈❙❱✧✮❀
             ❜✉tt♦♥✳s❡t▲❛②♦✉t❳✭✺✼✺✮❀
             ❜✉tt♦♥✳s❡t▲❛②♦✉t❨✭✷✺✮❀

             ❜✉tt♦♥✳s❡t❖♥❆❝t✐♦♥✭❡✈❡♥t ✲❃ ❡①♣♦rt❛❊♠❈❙❱✭♣r♦❞✉t♦s✮✮❀

             ❣r♦✉♣✳❣❡t❈❤✐❧❞r❡♥✭✮✳❛❞❞❆❧❧✭❧❛❜❡❧✱ ✈❜♦①✱ ❜✉tt♦♥✮❀

             ♣r✐♠❛r②❙t❛❣❡✳s❡t❚✐t❧❡✭✧❙✐st❡♠❛ ❞❛ ❧✐✈r❛r✐❛ ❝♦♠ ❏❛✈❛ ❋❳✧✮❀
             ♣r✐♠❛r②❙t❛❣❡✳s❡t❙❝❡♥❡✭s❝❡♥❡✮❀
             ♣r✐♠❛r②❙t❛❣❡✳s❤♦✇✭✮❀
      ⑥

54


[PAGINA 65]
Casa do Código                                          Capítulo 3. Java IO




     ♣r✐✈❛t❡ ✈♦✐❞ ❡①♣♦rt❛❊♠❈❙❱✭❖❜s❡r✈❛❜❧❡▲✐st❁Pr♦❞✉t♦❃ ♣r♦❞✉t♦s✮ ④
         tr② ④
             ♥❡✇ ❊①♣♦rt❛❞♦r✭✮✳♣❛r❛❈❙❱✭♣r♦❞✉t♦s✮❀
         ⑥ ❝❛t❝❤ ✭■❖❊①❝❡♣t✐♦♥ ❡✮ ④
             ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❊rr♦ ❛♦ ❡①♣♦rt❛r✿ ✧✰ ❡✮❀
         ⑥
     ⑥

     ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④
         ❧❛✉♥❝❤✭❛r❣s✮❀
     ⑥
⑥

   A única diferença para você, que está usando Java 7, será no
setOnAction do button. Agora que extraímos o método, ele ficará assim
com classe anônima:

❜✉tt♦♥✳s❡t❖♥❆❝t✐♦♥✭♥❡✇ ❊✈❡♥t❍❛♥❞❧❡r❁❆❝t✐♦♥❊✈❡♥t❃✭✮ ④
    ❅❖✈❡rr✐❞❡
    ♣✉❜❧✐❝ ✈♦✐❞ ❤❛♥❞❧❡✭❆❝t✐♦♥❊✈❡♥t ❡✈❡♥t✮ ④
        ❡①♣♦rt❛❊♠❈❙❱✭♣r♦❞✉t♦s✮❀
    ⑥
⑥✮❀




                                                                        55


[PAGINA 66]


[PAGINA 67]
Capítulo 4

Banco de Dados e JDBC
A aplicação está ficando mais completa, mas ainda estamos trabalhando com
valores fixos na listagem de produtos que criamos manualmente na classe
RepositorioDeProdutos. Nosso objetivo agora será buscar essas infor-
mações de um banco de dados, como é natural nas aplicações do dia a dia.


4.1 Iniciando com MySQL
Usaremos o banco de dados MySQL no projeto de nossa livraria, já que é
um dos bancos de dados relacionais mais utilizados no mercado, é gratuito e
bastante simples de instalar.
    Se você ainda não tem o MySQL instalado, pode fazer download pelo link:
    http://dev.mysql.com/downloads/mysql/


[PAGINA 68]
4.1. Iniciando com MySQL                                     Casa do Código




   Ao final da página, você encontrará um campo para escolher seu sistema
operacional. Selecione e depois clique em download, na opção que preferir:




     No mesmo site, você encontra um tutorial de instalação de acordo com o

58


[PAGINA 69]
Casa do Código                                   Capítulo 4. Banco de Dados e JDBC



seu sistema operacional. Ou você pode acessar o tutorial diretamente em:
    http://dev.mysql.com/doc/refman/5.7/en/installing.html
    Após baixar e instalar o MySQL, vamos nos logar no MySQL e criar a base
de dados (database) de nosso projeto. O primeiro passo é bem simples, tudo
que você precisa fazer para se logar é abrir seu terminal e digitar:
♠②sq❧ ✲✉ ❙❊❯❴❯❙❯❆❘■❖ ✲♣ ❙❯❆❴❙❊◆❍❆

    Como em meu caso o usuário é root e eu não tenho uma senha, só
preciso fazer:
♠②sq❧ ✲✉ r♦♦t




                 Fig. 4.3: Tela inicial do MySQL Command Line



  MySQL Command Line ou Workbench?

     Há quem prefira utilizar o MySQL Workbench, que é uma ferramenta
  visual. Pela simplicidade, nos exemplos do livro vamos utilizar o MySQL
  Command Line. Nele, nós executamos as instruções diretamente pela
  linha de comando, no terminal.
     Se tiver qualquer dificuldade para instalar ou executar os comandos,
  não pense duas vezes antes de mandar um e-mail para lista desse livro.


                                                                               59


[PAGINA 70]
4.2. Criando a tabela de produtos                           Casa do Código


   Agora que já estamos logados, podemos criar uma nova database
chamada livraria. Isso pode ser feito com o comando:

❝r❡❛t❡ ❞❛t❛❜❛s❡ ❧✐✈r❛r✐❛❀

     Após executá-lo, a saída deve ser parecida com:

◗✉❡r② ❖❑✱ ✶ r♦✇ ❛❢❢❡❝t❡❞ ✭✵✳✵✵ s❡❝✮

    Perfeito, vamos usar agora o comando use livraria para acessar essa
base de dados que criamos.

✉s❡ ❧✐✈r❛r✐❛❀

     A mensagem Database changed deve ser exibida.


4.2      Criando a tabela de produtos
Podemos agora criar uma tabela onde serão persistidas as informações de
nossos produtos. Faremos isso com o comando create table a seguir:

❈❘❊❆❚❊ ❚❆❇▲❊ ♣r♦❞✉t♦s ✭
    ✐❞ ❇■●■◆❚ ◆❖❚ ◆❯▲▲ ❆❯❚❖❴■◆❈❘❊▼❊◆❚✱
    ♥♦♠❡ ❱❆❘❈❍❆❘✭✷✺✺✮✱
    ❞❡s❝r✐❝❛♦ ❱❆❘❈❍❆❘✭✷✺✺✮✱
    ✈❛❧♦r ❱❆❘❈❍❆❘✭✷✺✺✮✱
    ✐s❜♥ ❱❆❘❈❍❆❘✭✷✺✺✮✱
    P❘■▼❆❘❨ ❑❊❨ ✭✐❞✮
✮❀

    Se você não está acostumado com SQL, não se preocupe. Nosso foco aqui
será a integração do código Java com um banco de dados, e não o SQL em si.
Em poucas palavras, o comando criou uma tabela de produtos com as colunas
id, nome, descricao e isbn, que é o que precisamos por agora. Note
também que dissemos que o id do produto não pode ser nulo e deve ser
autoincrementado, assim o próprio banco de dados cuidará de incrementar o
valor do id a cada novo registro.



60


[PAGINA 71]
Casa do Código                                    Capítulo 4. Banco de Dados e JDBC



4.3    O pacote java.sql e o JDBC
A biblioteca padrão do Java para persistência em banco de dados é con-
hecida como JDBC, de Java Data Base Connective. O JDBC é, na verdade, um
conjunto de interfaces bem elaborado que deve ser implementado de forma
diferente para cada banco de dados. Dessa forma, evitamos que cada banco
tenha seu próprio conjunto de classes e métodos. Qual a vantagem disso?
Manutenibilidade é uma das muitas. Migrar de um banco para outro é um
processo fácil, já que todos implementam as mesmas interfaces, portanto pos-
suem métodos com a mesma assinatura.
     Esse conjunto de classes é conhecido como driver; elas fazem a ponte
entre a API de JDBC e o banco de dados. O nome é análogo aos drivers uti-
lizados na instalação de impressoras. Da mesma forma que os drivers possi-
bilitam a comunicação entre uma determinada impressora com os diferentes
sistemas operacionais existentes, os drivers que implementam as interfaces do
JDBC possibilitam a comunicação entre nosso código Java com os diferentes
bancos de dados existentes.




                                                                                61


[PAGINA 72]
4.3. O pacote java.sql e o JDBC                               Casa do Código




           Fig. 4.4: Comunicação entre código Java e Banco de Dados



   Boa prática: pacote java.sql

      No momento de fazer os imports das classes, tome o cuidado de sem-
   pre escolher o pacote java.sql. Nunca escolha opções de classes
   equivalentes do pacote com.mysql, ou qualquer outro banco de dados
   que você estiver utilizando. Dessa forma, você não se acopla com a API
   do banco de dados que está utilizando.




62


[PAGINA 73]
Casa do Código                                  Capítulo 4. Banco de Dados e JDBC



4.4 Abrindo conexão com MySQL em Java
A classe DriverManager é a responsável por gerenciar o processo de comu-
nicação com os drivers dos bancos de dados. Para abrir uma conexão, tudo
que precisamos fazer é invocar seu método getConnection passando como
parâmetro uma String de conexão do JDBC, seu login e senha. Essa String
de conexão, para o MySQL, tem a seguinte estrutura:

❥❞❜❝✿♠②sq❧✿✴✴■P✴❉❆❚❆❇❆❙❊

    O IP deve ser substituído pelo IP do servidor onde se encontra o banco
de dados. Em nosso caso, como será na mesma máquina, podemos deixar
como localhost. A DATABASE deve ser substituída pelo nome da base de
dados que criamos para o projeto, a livraria. Portanto:

❥❞❜❝✿♠②sq❧✿✴✴❧♦❝❛❧❤♦st✴❧✐✈r❛r✐❛

    Para utilizar o DriverManager, precisaremos adicionar o driver do
MySQL em nosso projeto. Esse arquivo também está disponível no zip
que você baixou com os arquivos necessários para este livro. Basta copiar o
arquivo mysql-connector-java-5.1.34-bin.jar para dentro do seu
projeto no Eclipse. Com o botão direito do mouse, clique no driver e depois
em Build Path e Add to Build Path.




           Fig. 4.5: Adicionando driver do MySQL no Build Path.



    Se você ainda não está familiarizado com o termo JAR, não se preocupe.
Temos um capítulo que detalha bem esse tipo de arquivo e seu uso.
    Agora que temos o driver, vamos criar uma nova classe, que chamaremos
de ConnectionFactory para colocar isso tudo em prática. Seu código de-
verá se parecer com:


                                                                              63


[PAGINA 74]
4.4. Abrindo conexão com MySQL em Java                        Casa do Código


♣✉❜❧✐❝ ❝❧❛ss ❈♦♥♥❡❝t✐♦♥❋❛❝t♦r② ④

      ♣✉❜❧✐❝ ❈♦♥♥❡❝t✐♦♥ ❣❡t❈♦♥♥❡❝t✐♦♥✭✮ ④
          ❙tr✐♥❣ ✉r❧ ❂ ✧❥❞❜❝✿♠②sq❧✿✴✴❧♦❝❛❧❤♦st✴❧✐✈r❛r✐❛✧❀
          r❡t✉r♥ ❉r✐✈❡r▼❛♥❛❣❡r✳❣❡t❈♦♥♥❡❝t✐♦♥✭✉r❧✱ ✧r♦♦t✧✱ ✧✧✮❀
      ⑥
⑥


    Design Patterns e o Factory Method

        Não foi por acaso que chamamos a classe ConnectionFactory
    dessa forma. Essa é uma prática de projeto muito comum e bastante re-
    comendada. Muitas vezes queremos controlar o processo de criação de
    um objeto que pode ser repetido diversas vezes em nosso código, como
    o de abrir uma conexão. O que aconteceria se esse código estivesse es-
    palhado por nossa aplicação e alguma informação mudasse? Uma troca
    de login, por exemplo, faria você mudar diversas partes do seu código.
        Note que, agora que temos a classe ConnectionFactory, não es-
    tamos deixando as informações do banco de dados se replicarem em
    toda nossa aplicação. O método getConnection não recebe nenhum
    parâmetro e retorna uma conexão pronta para ser utilizada. Alguma in-
    formação mudou? Não tem problema, só preciso mudar um único ponto
    do meu código (a implementação do método getConnection), que
    isso será replicado pra todos que o usam. Interessante, não acha?
        Essa boa prática de projeto é conhecida como factory method e
    compõe um dos diversos Design Patterns existentes.


   Mas esse código ainda não compila, o método getConnection lança
uma SQLException. Precisamos tratar ou declarar essa exceção de alguma
forma. uma maneira bastante recomendada de tratar seria:

♣✉❜❧✐❝ ❝❧❛ss ❈♦♥♥❡❝t✐♦♥❋❛❝t♦r② ④

      ♣✉❜❧✐❝ ❈♦♥♥❡❝t✐♦♥ ❣❡t❈♦♥♥❡❝t✐♦♥✭✮ ④
          ❙tr✐♥❣ ✉r❧ ❂ ✧❥❞❜❝✿♠②sq❧✿✴✴❧♦❝❛❧❤♦st✴❧✐✈r❛r✐❛✧❀


64


[PAGINA 75]
Casa do Código                                  Capítulo 4. Banco de Dados e JDBC



           tr② ④
               r❡t✉r♥ ❉r✐✈❡r▼❛♥❛❣❡r✳❣❡t❈♦♥♥❡❝t✐♦♥✭✉r❧✱ ✧r♦♦t✧✱ ✧✧✮❀
           ⑥ ❝❛t❝❤ ✭❙◗▲❊①❝❡♣t✐♦♥ ❡✮ ④
               t❤r♦✇ ♥❡✇ ❘✉♥t✐♠❡❊①❝❡♣t✐♦♥✭❡✮❀
           ⑥
     ⑥
⑥

    Qual a vantagem em fazer isso? Afinal só estamos “embrulhando” e re-
lançando a SQLException como uma RuntimeException. A grande
ideia dessa prática é que assim não deixamos essa exception da API de JDBC
se espalhar pelo nosso código, diminuindo acoplamento com essa API.
    Já podemos testar nosso código para garantir que a conexão com o
banco de dados está acontecendo sem nenhum problema. Podemos criar
um método main, na própria classe ConnectionFactory, com o seguinte
código:

♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④
    ❈♦♥♥❡❝t✐♦♥ ❝♦♥♥ ❂ ♥❡✇ ❈♦♥♥❡❝t✐♦♥❋❛❝t♦r②✭✮✳❣❡t❈♦♥♥❡❝t✐♦♥✭✮❀
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❈♦♥❡①❛♦ ❛❜❡rt❛✱ ❡ ❛❣♦r❛❄✧✮❀
    ❝♦♥♥✳❝❧♦s❡✭✮❀
⑥

    Execute para ver se tudo está ok. Alguns dos erros comuns são:

    • Errar a digitação da String de conexões, como por exemplo esquecer
      de uma barra ou algo desse tipo. Neste caso, uma exception parecida
      com a seguinte deve acontecer:

         ❈❛✉s❡❞ ❜②✿ ❥❛✈❛✳sq❧✳❙◗▲❊①❝❡♣t✐♦♥✿ ◆♦ s✉✐t❛❜❧❡
             ❞r✐✈❡r ❢♦✉♥❞ ❢♦r ❥❞❜❝✿♠②sq❧✿✴❧♦❝❛❧❤♦st✴❧✐✈r❛r✐❛

    • Referenciar uma database que não existe. Por exemplo, se eu não criar
      a database livraria no MySQL, o seguinte erro vai acontecer:

         ❈❛✉s❡❞ ❜②✿ ❝♦♠✳♠②sq❧✳❥❞❜❝✳❡①❝❡♣t✐♦♥s✳❥❞❜❝✹
             ✳▼②❙◗▲❙②♥t❛①❊rr♦r❊①❝❡♣t✐♦♥✿ ❯♥❦♥♦✇♥ ❞❛t❛❜❛s❡ ✬❧✐✈r❛r✐❛✬



                                                                              65


[PAGINA 76]
4.5. Listando todos os produtos do banco                     Casa do Código


    Se tudo correu bem, a mensagem Conexao aberta, e agora? deve ser ex-
ibida. Podemos dar mais um passo, adicionar e listar elementos com a API
do JDBC.


4.5 Listando todos os produtos do banco
Vamos começar pelo nosso objetivo, que é listar todos os produtos do banco
de dados. Para fazer isso, limpe o conteúdo do método lista da classe
RepositorioDeProdutos, deixe apenas:

♣✉❜❧✐❝ ❝❧❛ss ❘❡♣♦s✐t♦r✐♦❉❡Pr♦❞✉t♦s ④

      ♣✉❜❧✐❝ ❖❜s❡r✈❛❜❧❡▲✐st❁Pr♦❞✉t♦❃ ❧✐st❛✭✮ ④

            r❡t✉r♥ ❋❳❈♦❧❧❡❝t✐♦♥s✳♦❜s❡r✈❛❜❧❡❆rr❛②▲✐st✭✮❀
      ⑥
⑥

   O primeiro passo será escrever a SQL que queremos executar no banco,
que será algo como:
❙tr✐♥❣ sq❧ ❂ ✧s❡❧❡❝t ✯ ❢r♦♠ ♣r♦❞✉t♦s✧❀

    A cláusula select com * está indicando que queremos todas as colu-
nas de todos os produtos. Para executar esta, ou qualquer outra query, pre-
cisaremos antes abrir uma conexão com o banco e pra isso podemos utilizar
a ConnectionFactory que criamos. O código fica assim:
❈♦♥♥❡❝t✐♦♥ ❝♦♥♥ ❂ ♥❡✇ ❈♦♥♥❡❝t✐♦♥❋❛❝t♦r②✭✮✳❣❡t❈♦♥♥❡❝t✐♦♥✭✮❀
❙tr✐♥❣ sq❧ ❂ ✧s❡❧❡❝t ✯ ❢r♦♠ ♣r♦❞✉t♦s✧❀

    Como enviar e executar essa query em um banco de dados? É bem sim-
ples, há uma interface chamada PreparedStatement para nos ajudar neste
trabalho. Basta chamar o método prepareStatement da Connection
que criamos, passando a SQL como argumento:
❈♦♥♥❡❝t✐♦♥ ❝♦♥♥ ❂ ♥❡✇ ❈♦♥♥❡❝t✐♦♥❋❛❝t♦r②✭✮✳❣❡t❈♦♥♥❡❝t✐♦♥✭✮❀
❙tr✐♥❣ sq❧ ❂ ✧s❡❧❡❝t ✯ ❢r♦♠ ♣r♦❞✉t♦s✧❀
Pr❡♣❛r❡❞❙t❛t❡♠❡♥t ♣s ❂ ❝♦♥♥✳♣r❡♣❛r❡❙t❛t❡♠❡♥t✭sq❧✮❀
♣s✳❡①❡❝✉t❡◗✉❡r②✭✮❀

66


[PAGINA 77]
Casa do Código                                   Capítulo 4. Banco de Dados e JDBC



    Esse código lança uma    SQLException, vamos relançar essa
exceção como uma Runtime, da mesma forma que fizemos na
ConnectionFactory para diminuir o acoplamento com a API de
JDBC. O código ficará assim:
❈♦♥♥❡❝t✐♦♥ ❝♦♥♥ ❂ ♥❡✇ ❈♦♥♥❡❝t✐♦♥❋❛❝t♦r②✭✮✳❣❡t❈♦♥♥❡❝t✐♦♥✭✮❀
Pr❡♣❛r❡❞❙t❛t❡♠❡♥t ♣s❀
tr② ④
    ♣s ❂ ❝♦♥♥✳♣r❡♣❛r❡❙t❛t❡♠❡♥t✭✧s❡❧❡❝t ✯ ❢r♦♠ ♣r♦❞✉t♦s✧✮❀
    ♣s✳❡①❡❝✉t❡◗✉❡r②✭✮❀
⑥ ❝❛t❝❤ ✭❙◗▲❊①❝❡♣t✐♦♥ ❡✮ ④
    t❤r♦✇ ♥❡✇ ❘✉♥t✐♠❡❊①❝❡♣t✐♦♥✭❡✮❀
⑥

     O método executeQuery fará seu trabalho e retornará um objeto
com todos os registros do resultado da consulta. Esse objeto tem o tipo
ResultSet. Cada chamada ao seu método next retornará true en-
quanto houver próximos registros, portanto, é natural iterar nessa estrutura
utilizando um while, como faremos a seguir:
✇❤✐❧❡✭r❡s✉❧t❙❡t✳♥❡①t✭✮✮ ④
    ✴✴ ❝♦♠♦ ♣❡❣❛r ♦ ♥♦♠❡✱ ✈❛❧♦r✱ ❡t❝❄
⑥

    Seus métodos get são os responsáveis por recuperar o valor de uma
determinada coluna da tabela. Se for uma coluna de texto, utilizamos o
getString, getInt para um inteiro e assim por diante. Em nosso caso,
precisaremos apenas dos métodos getString para nome, descricao, isbn e
do getDouble para o valor do produto. O código deve ficar assim:
✇❤✐❧❡✭r❡s✉❧t❙❡t✳♥❡①t✭✮✮ ④
    ❙tr✐♥❣ ♥♦♠❡ ❂ r❡s✉❧t❙❡t✳❣❡t❙tr✐♥❣✭✧♥♦♠❡✧✮❀
    ❙tr✐♥❣ ❞❡s❝r✐❝❛♦ ❂ r❡s✉❧t❙❡t✳❣❡t❙tr✐♥❣✭✧❞❡s❝r✐❝❛♦✧✮❀
    ❞♦✉❜❧❡ ✈❛❧♦r ❂ r❡s✉❧t❙❡t✳❣❡t❉♦✉❜❧❡✭✧✈❛❧♦r✧✮❀
    ❙tr✐♥❣ ✐s❜♥ ❂ r❡s✉❧t❙❡t✳❣❡t❙tr✐♥❣✭✧✐s❜♥✧✮❀
⑥

   Para concluir, nosso método precisa retornar a ObservableList de
Produtos que será consumida pela nossa listagem em Java FX. Por enquanto,
vamos representar os produtos apenas como LivroFisico:

                                                                               67


[PAGINA 78]
4.5. Listando todos os produtos do banco                     Casa do Código


✇❤✐❧❡✭r❡s✉❧t❙❡t✳♥❡①t✭✮✮ ④
    ▲✐✈r♦❋✐s✐❝♦ ❧✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦❋✐s✐❝♦✭♥❡✇ ❆✉t♦r✭✮✮❀
    ❧✐✈r♦✳s❡t◆♦♠❡✭r❡s✉❧t❙❡t✳❣❡t❙tr✐♥❣✭✧♥♦♠❡✧✮✮❀
    ❧✐✈r♦✳s❡t❉❡s❝r✐❝❛♦✭r❡s✉❧t❙❡t✳❣❡t❙tr✐♥❣✭✧❞❡s❝r✐❝❛♦✧✮✮❀
    ❧✐✈r♦✳s❡t❱❛❧♦r✭r❡s✉❧t❙❡t✳❣❡t❉♦✉❜❧❡✭✧✈❛❧♦r✧✮✮❀
    ❧✐✈r♦✳s❡t■s❜♥✭r❡s✉❧t❙❡t✳❣❡t❙tr✐♥❣✭✧✐s❜♥✧✮✮❀
    ♣r♦❞✉t♦s✳❛❞❞✭❧✐✈r♦✮❀
⑥

        Ao final, nossa classe RepositorioDeProdutos deve ficar assim:

♣✉❜❧✐❝ ❝❧❛ss ❘❡♣♦s✐t♦r✐♦❉❡Pr♦❞✉t♦s ④

    ♣✉❜❧✐❝ ❖❜s❡r✈❛❜❧❡▲✐st❁Pr♦❞✉t♦❃ ❧✐st❛✭✮ ④

        ❖❜s❡r✈❛❜❧❡▲✐st❁Pr♦❞✉t♦❃ ♣r♦❞✉t♦s ❂ ♦❜s❡r✈❛❜❧❡❆rr❛②▲✐st✭✮❀
        ❈♦♥♥❡❝t✐♦♥ ❝♦♥♥ ❂ ♥❡✇ ❈♦♥♥❡❝t✐♦♥❋❛❝t♦r②✭✮✳❣❡t❈♦♥♥❡❝t✐♦♥✭✮❀
        Pr❡♣❛r❡❞❙t❛t❡♠❡♥t ♣s❀
        tr② ④
            ♣s ❂ ❝♦♥♥✳♣r❡♣❛r❡❙t❛t❡♠❡♥t✭✧s❡❧❡❝t ✯ ❢r♦♠ ♣r♦❞✉t♦s✧✮❀
            ❘❡s✉❧t❙❡t r❡s✉❧t❙❡t ❂ ♣s✳❡①❡❝✉t❡◗✉❡r②✭✮❀

            ✇❤✐❧❡✭r❡s✉❧t❙❡t✳♥❡①t✭✮✮ ④
               ▲✐✈r♦❋✐s✐❝♦ ❧✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦❋✐s✐❝♦✭♥❡✇ ❆✉t♦r✭✮✮❀
               ❧✐✈r♦✳s❡t◆♦♠❡✭r❡s✉❧t❙❡t✳❣❡t❙tr✐♥❣✭✧♥♦♠❡✧✮✮❀
               ❧✐✈r♦✳s❡t❉❡s❝r✐❝❛♦✭r❡s✉❧t❙❡t✳❣❡t❙tr✐♥❣✭✧❞❡s❝r✐❝❛♦✧✮✮❀
               ❧✐✈r♦✳s❡t❱❛❧♦r✭r❡s✉❧t❙❡t✳❣❡t❉♦✉❜❧❡✭✧✈❛❧♦r✧✮✮❀
               ❧✐✈r♦✳s❡t■s❜♥✭r❡s✉❧t❙❡t✳❣❡t❙tr✐♥❣✭✧✐s❜♥✧✮✮❀
            ♣r♦❞✉t♦s✳❛❞❞✭❧✐✈r♦✮❀
            ⑥
            r❡s✉❧t❙❡t✳❝❧♦s❡✭✮❀
            ♣s✳❝❧♦s❡✭✮❀
            ❝♦♥♥✳❝❧♦s❡✭✮❀
        ⑥ ❝❛t❝❤ ✭❙◗▲❊①❝❡♣t✐♦♥ ❡✮ ④
            t❤r♦✇ ♥❡✇ ❘✉♥t✐♠❡❊①❝❡♣t✐♦♥✭❡✮❀
        ⑥
        r❡t✉r♥ ♣r♦❞✉t♦s❀
    ⑥
⑥


68


[PAGINA 79]
Casa do Código                                   Capítulo 4. Banco de Dados e JDBC



    Mas, espera! Ao executar a classe Main agora, nossa listagem de produtos
está vazia! Faz sentido, não é? Afinal, não adicionamos nenhum produto ao
banco de dados, a tabela produtos está vazia. Esse será nosso próximo
passo.


  Inserindo manualmente no MySQL

     Se você quiser, pode inserir um livro manualmente na tabela de pro-
  dutos para confirmar desde já que seu código está funcionando como
  deveria. Você pode fazer isso executando os seguintes comandos em seu
  terminal:

  ✩ ♠②sq❧ ✲✉ r♦♦t ❧✐✈r❛r✐❛
  ✩ ✐♥s❡rt ✐♥t♦ ♣r♦❞✉t♦s ✭♥♦♠❡✱ ❞❡s❝r✐❝❛♦✱ ✈❛❧♦r✱ ✐s❜♥✮
      ✈❛❧✉❡s ✭✬❏❛✈❛ ✽ Prát✐❝♦✬✱ ✬◆♦✈♦s r❡❝✉rs♦s ❞❛ ❧✐♥❣✉❛❣❡♠✬✱
      ✬✺✾✳✾✵✬✱ ✬✾✼✽✲✽✺✲✻✻✷✺✵✲✹✻✲✻✬✮❀




4.6 Importando produtos de um dump
Para não precisar cadastrar manualmente, vamos importar o arquivo
dump.sql com alguns livros já cadastrados para nossa tabela de produtos.
Um arquivo de dumb é um arquivo de texto com instruções SQL, com os in-
serts de dados ou até mesmo com as instruções de criação de tabelas.


  Criando seu próprio dump

     Se quiser saber mais sobre esse arquivo de dump, ou mesmo criar o
  seu próprio, você pode dar uma olhada no link:
     http://dev.mysql.com/doc/refman/5.0/en/mysqldump-sql-format.
  html
     Isso pode ser bem útil quando queremos fazer backups de segurança
  de nossas bases de dados.



                                                                              69


[PAGINA 80]
4.6. Importando produtos de um dump                          Casa do Código


    Esse arquivo também está presente naquele zip com o conteúdo inicial
do projeto, em arquivos-do-livro/dump.sql. Tudo que precisamos
fazer para importar esse dump em nosso banco de dados é executar a seguinte
instrução no terminal:

♠②sq❧ ✲✉r♦♦t ❁ ❈❆▼■◆❍❖❴❈❖▼P▲❊❚❖❴P❆❘❆❴❖❴❉❯▼P

    Para facilitar o processo, você pode copiar o arquivo dump.sql para a
pasta raiz de seu usuário, e executar apenas:

♠②sq❧ ✲✉r♦♦t ❁ ❞✉♠♣✳sq❧

   Ótimo! Depois que concluir, tente acessar novamente a listagem de pro-
dutos. Se tudo correu bem, diversos livros devem ser listados.




70


[PAGINA 81]
Casa do Código                                    Capítulo 4. Banco de Dados e JDBC




    Frameworks ORM

        Existem diversas ferramentas que facilitam e muito o uso do JDBC,
    que são conhecidas como ferramentas ORM, de Object Relational Map-
    ping. A ideia é que você trabalhe pensando exclusivamente em orientação
    a objetos, enquanto essas bibliotecas (ou frameworks, como são comu-
    mente chamadas) o ajudam a traduzir isso para o mundo relacional dos
    bancos de dados. O Hibernate é um dos frameworks de ORM mais con-
    hecidos e utilizados do mercado. Aconselho bastante que você pesquise
    a respeito desses e outros após conhecer a API de JDBC do Java.
        Se quiser saber mais sobre o hibernate você pode querer dar uma ol-
    hada no site:
        http://hibernate.org/orm/


4.7     Para saber mais: Adicionando programati-
        camente
Para conhecer um pouquinho mais sobre a API do JDBC, vamos criar mais
um método na classe RepositorioDeProdutos, que exemplificará como
é feito um INSERT no banco de dados programaticamente. Vamos chamá-lo
de adiciona, afinal esse será seu propósito.

♣✉❜❧✐❝ ❝❧❛ss ❘❡♣♦s✐t♦r✐♦❉❡Pr♦❞✉t♦s ④

      ♣✉❜❧✐❝ ❖❜s❡r✈❛❜❧❡▲✐st❁Pr♦❞✉t♦❃ ❧✐st❛✭✮ ④
          ✴✴ ❝ó❞✐❣♦ ♦♠✐t✐❞♦
      ⑥

      ♣✉❜❧✐❝ ✈♦✐❞ ❛❞✐❝✐♦♥❛✭Pr♦❞✉t♦ ♣r♦❞✉t♦✮ ④
          ✴✴ ❝ó❞✐❣♦ ❞❡ ❛❞✐❝✐♦♥❛r ❝♦♠ ❏❉❇❈
      ⑥
⑥

    Note que esse método já está recebendo o Produto que deverá ser adi-
cionado no banco.

                                                                                71


[PAGINA 82]
4.7. Para saber mais: Adicionando programaticamente       Casa do Código


    Da mesma forma como fizemos com o método lista, utilizaremos a
interface PreparedStatement para executar as instruções SQL no banco
de dados.

♣✉❜❧✐❝ ✈♦✐❞ ❛❞✐❝✐♦♥❛✭Pr♦❞✉t♦ ♣r♦❞✉t♦✮ ④
    ❈♦♥♥❡❝t✐♦♥ ❝♦♥♥ ❂ ♥❡✇ ❈♦♥♥❡❝t✐♦♥❋❛❝t♦r②✭✮✳❣❡t❈♦♥♥❡❝t✐♦♥✭✮❀
    Pr❡♣❛r❡❞❙t❛t❡♠❡♥t ♣s ❂ ❝♦♥♥✳♣r❡♣❛r❡❙t❛t❡♠❡♥t✭✧❄❄❄✧✮❀

      ✴✴ ❝ó❞✐❣♦ ❞❡ ❡①❡❝✉t❛r ♦ Pr❡♣❛r❡❞❙t❛t❡♠❡♥t

      ♣s✳❝❧♦s❡✭✮❀
      ❝♦♥♥✳❝❧♦s❡✭✮❀
⑥

   Vale lembrar que esse código não compilará se não tratarmos a
SQLException que o método prepareStatement lança.

♣✉❜❧✐❝ ✈♦✐❞ ❛❞✐❝✐♦♥❛✭Pr♦❞✉t♦ ♣r♦❞✉t♦✮ ④
    ❈♦♥♥❡❝t✐♦♥ ❝♦♥♥ ❂ ♥❡✇ ❈♦♥♥❡❝t✐♦♥❋❛❝t♦r②✭✮✳❣❡t❈♦♥♥❡❝t✐♦♥✭✮❀
    Pr❡♣❛r❡❞❙t❛t❡♠❡♥t ♣s❀
    tr② ④
        ♣s ❂ ❝♦♥♥✳♣r❡♣❛r❡❙t❛t❡♠❡♥t✭✧❄❄❄✧✮❀

            ✴✴ ❝ó❞✐❣♦ ❞❡ ❡①❡❝✉t❛r ♦ Pr❡♣❛r❡❞❙t❛t❡♠❡♥t

          ♣s✳❝❧♦s❡✭✮❀
          ❝♦♥♥✳❝❧♦s❡✭✮❀
      ⑥ ❝❛t❝❤ ✭❙◗▲❊①❝❡♣t✐♦♥ ❡✮ ④
          t❤r♦✇ ♥❡✇ ❘✉♥t✐♠❡❊①❝❡♣t✐♦♥✭❡✮❀
      ⑥
⑥

    Por enquanto, o código está muito parecido com o de listagem, mas a
grande diferença começa aqui. Uma forma de escrever a cláusula INSERT
que será executada no banco de dados seria:

♣s ❂ ❝♦♥♥✳♣r❡♣❛r❡❙t❛t❡♠❡♥t✭✧✐♥s❡rt ✐♥t♦ ♣r♦❞✉t♦s ✭♥♦♠❡✱
    ❞❡s❝r✐❝❛♦✱ ✈❛❧♦r✱ ✐s❜♥✮ ✈❛❧✉❡s ✭✬▲✐✈r♦ ❞❡ P❍P✬✱
    ✬❯♠ ❧✐✈r♦ s♦❜r❡ P❍P✬✱ ✬✺✾✳✾✵✬✱ ✬✶✷✸✲✹✺✲✻✼✽✾✵✲✶✷✲✸✬✮✧✮❀


72


[PAGINA 83]
Casa do Código                                   Capítulo 4. Banco de Dados e JDBC



    Mas, claro, não podemos deixar esses valores fixos em nosso código. Uma
alternativa é concatenar os atributos do Produto, como faremos a seguir:

♣s ❂ ❝♦♥♥✳♣r❡♣❛r❡❙t❛t❡♠❡♥t✭✧✐♥s❡rt ✐♥t♦ ♣r♦❞✉t♦s ✭♥♦♠❡✱ ✧
    ✰ ✧❞❡s❝r✐❝❛♦✱ ✈❛❧♦r✱ ✐s❜♥✮ ✈❛❧✉❡s ✭✬✧✰♣r♦❞✉t♦✳❣❡t◆♦♠❡✭✮✰✧✬✱ ✧
    ✰ ✧✬✧✰♣r♦❞✉t♦✳❣❡t❉❡s❝r✐❝❛♦✭✮✰✧✬✱ ✬✧✰♣r♦❞✉t♦✳❣❡t❱❛❧♦r✭✮✰✧✬✱ ✧
    ✰ ✧✬✧✰♣r♦❞✉t♦✳❣❡t■s❜♥✭✮✰✧✮✧✮❀

    Que tal? Nem um pouco legível, não acha? Imagine se no lugar de 4
campos existissem cerca de 20, com o que esse código se pareceria?
    A prova de que é muito difícil manter um código como esse é que ao final
da String eu deixei de fora uma ‘ (aspas simples). Você identificou isso ao
olhar pro código? Sem dúvida poderia passar despercebido.
    Mas esse não é o único problema desse código cheio de concatenações, há
ainda o clássico problema de nomes que contêm aspas simples (como Joana
D’arc). O que aconteceria ao tentar concatenar essa String na SQL anterior?
A instrução SQL vai quebrar toda! Pior ainda, fazer concatenação dessa forma
possibilita ao usuário final modificar seu SQL para executar o que ele bem
entender, o clássico problema de SQL Injection.




                                                                               73


[PAGINA 84]
4.7. Para saber mais: Adicionando programaticamente             Casa do Código




     Para saber mais: SQL Injection

         Para entender melhor o que é uma injeção de SQL, vamos considerar
     a seguinte instrução que faz um SELECT verificando se o usuário existe.
     Ela comumente seria executada por um formulário de login.

     ♣s ❂ ❝♦♥♥✳♣r❡♣❛r❡❙t❛t❡♠❡♥t✭✧s❡❧❡❝t ✯ ❢r♦♠ ✉s✉❛r✐♦s ✇❤❡r❡ ✧
         ✰ ✧❧♦❣✐♥ ❂ ✬✧✰❧♦❣✐♥✰✧✬ ❛♥❞ s❡♥❤❛ ❂✬✧✰s❡♥❤❛✰✧✬✧✮❀

        O que acontece se o valor da variável login for um texto vazio e o
     valor da variável senha for ’ or 1=1? Vamos substituir a String
     com esses valores para verificar. O resultado será:

     s❡❧❡❝t ✯ ❢r♦♠ ✉s✉❛r✐♦s ✇❤❡r❡ ❧♦❣✐♥ ❂✬✬ ❛♥❞ s❡♥❤❛ ❂✬✬ ♦r ✶❂✶

         Esse comando trará todos os usuários de nosso banco de dados! Ou
     seja, o usuário final da aplicação pode enviar qualquer informação, que
     pode ser maliciosa, e resultar em um retorno inesperado como esse.
     Nunca devemos concatenar variáveis em comandos SQL dessa forma.



    Bem, já vimos que essa é uma péssima prática. No lugar de concatenar
dessa forma, a interface PreparedStatement nos oferece uma série de
métodos set para popularmos os valores variáveis da instrução SQL. Nosso
comando SQL ficará como a seguir, deixando pontos de interrogação no lugar
desses valores:

♣s ❂ ❝♦♥♥✳♣r❡♣❛r❡❙t❛t❡♠❡♥t✭✧✐♥s❡rt ✐♥t♦ ♣r♦❞✉t♦s ✭♥♦♠❡✱✧
        ✰ ✧ ❞❡s❝r✐❝❛♦✱ ✈❛❧♦r✱ ✐s❜♥✮ ✈❛❧✉❡s ✭❄✱❄✱❄✱❄✮✧✮❀

     Para popular as variáveis, podemos utilizar os métodos setString para
os valores de texto e setDouble para o campo valor, que é do tipo
double, sempre passando a posição (que curiosamente começa em 1, e não
0), seguida do valor que deve ser preenchido:

♣s ❂ ❝♦♥♥✳♣r❡♣❛r❡❙t❛t❡♠❡♥t✭✧✐♥s❡rt ✐♥t♦ ♣r♦❞✉t♦s ✭♥♦♠❡✱✧
        ✰ ✧ ❞❡s❝r✐❝❛♦✱ ✈❛❧♦r✱ ✐s❜♥✮ ✈❛❧✉❡s ✭❄✱❄✱❄✱❄✮✧✮❀

74


[PAGINA 85]
Casa do Código                                   Capítulo 4. Banco de Dados e JDBC




♣s✳s❡t❙tr✐♥❣✭✶✱ ♣r♦❞✉t♦✳❣❡t◆♦♠❡✭✮✮❀
♣s✳s❡t❙tr✐♥❣✭✷✱ ♣r♦❞✉t♦✳❣❡t❉❡s❝r✐❝❛♦✭✮✮❀
♣s✳s❡t❉♦✉❜❧❡✭✸✱ ♣r♦❞✉t♦✳❣❡t❱❛❧♦r✭✮✮❀
♣s✳s❡t❙tr✐♥❣✭✹✱ ♣r♦❞✉t♦✳❣❡t■s❜♥✭✮✮❀


4.8       Qual a melhor forma de fechar a conexão?
Um ponto fundamental que precisa ser cuidadosamente verificado sempre
que estamos trabalhando com banco de dados é a forma como fechamos nos-
sas conexões. O nosso código parece estar fazendo isso adequadamente, não
acha? Dê uma boa olhada:

♣✉❜❧✐❝ ❝❧❛ss ❘❡♣♦s✐t♦r✐♦❉❡Pr♦❞✉t♦s ④

      ♣✉❜❧✐❝ ❖❜s❡r✈❛❜❧❡▲✐st❁Pr♦❞✉t♦❃ ❧✐st❛✭✮ ④

           ✴✴ ❝ó❞✐❣♦ ♦♠✐t✐❞♦
           tr② ④
               ✴✴ ❝ó❞✐❣♦ ♦♠✐t✐❞♦
               ❝♦♥♥✳❝❧♦s❡✭✮❀
           ⑥ ❝❛t❝❤ ✭❙◗▲❊①❝❡♣t✐♦♥ ❡✮ ④
               t❤r♦✇ ♥❡✇ ❘✉♥t✐♠❡❊①❝❡♣t✐♦♥✭❡✮❀
           ⑥
           r❡t✉r♥ ♣r♦❞✉t♦s❀
      ⑥
⑥

    Tudo parece estar certo, afinal estamos fechando a conexão. Isso é feito
dentro do bloco try, logo após executar o código no banco de dados. Mas
o que acontecerá quando esse código lançar uma Exception? Bem, você já
deve ter percebido o problema. O código do bloco try será interrompido, o
catch será executado e a conexão não será fechada.
    Uma forma de resolver o problema seria adicionando a chamada ao
método close também dentro do catch, como no exemplo:

♣✉❜❧✐❝ ❝❧❛ss ❘❡♣♦s✐t♦r✐♦❉❡Pr♦❞✉t♦s ④


                                                                               75


[PAGINA 86]
4.8. Qual a melhor forma de fechar a conexão?               Casa do Código


      ♣✉❜❧✐❝ ❖❜s❡r✈❛❜❧❡▲✐st❁Pr♦❞✉t♦❃ ❧✐st❛✭✮ ④

            ✴✴ ❝ó❞✐❣♦ ♦♠✐t✐❞♦
            tr② ④
                ✴✴ ❝ó❞✐❣♦ ♦♠✐t✐❞♦
                ❝♦♥♥✳❝❧♦s❡✭✮❀
            ⑥ ❝❛t❝❤ ✭❙◗▲❊①❝❡♣t✐♦♥ ❡✮ ④
                ❝♦♥♥✳❝❧♦s❡✭✮❀
                t❤r♦✇ ♥❡✇ ❘✉♥t✐♠❡❊①❝❡♣t✐♦♥✭❡✮❀
            ⑥
            r❡t✉r♥ ♣r♦❞✉t♦s❀
      ⑥
⑥

    Isso resolve o problema, mas o que você acha da solução? Nunca é muito
interessante replicar código dessa forma; o que aconteceria se esse método
tivesse múltiplos blocos catch? Copiamos e colamos em cada um deles? E
se esquecermos de algum?
    Por nossa sorte não precisamos fazer dessa forma, que não parece ser
ideal. Podemos utilizar o finally:

♣✉❜❧✐❝ ❝❧❛ss ❘❡♣♦s✐t♦r✐♦❉❡Pr♦❞✉t♦s ④

      ♣✉❜❧✐❝ ❖❜s❡r✈❛❜❧❡▲✐st❁Pr♦❞✉t♦❃ ❧✐st❛✭✮ ④

            ✴✴ ❝ó❞✐❣♦ ♦♠✐t✐❞♦
            tr② ④
                ✴✴ ❝ó❞✐❣♦ ♦♠✐t✐❞♦
            ⑥ ❝❛t❝❤ ✭❙◗▲❊①❝❡♣t✐♦♥ ❡✮ ④
                t❤r♦✇ ♥❡✇ ❘✉♥t✐♠❡❊①❝❡♣t✐♦♥✭❡✮❀
            ⑥ ❢✐♥❛❧❧② ④
                ❝♦♥♥✳❝❧♦s❡✭✮❀
            ⑥
            r❡t✉r♥ ♣r♦❞✉t♦s❀
      ⑥
⑥

   As instruções de dentro do bloco finally sempre são executadas,
em caso de exception ou não. É sempre muito interessante fazer oper-

76


[PAGINA 87]
Casa do Código                                  Capítulo 4. Banco de Dados e JDBC



ações como esta, de fechar uma conexão, dentro desse bloco. Colocamos no
finally operações que devem ser executadas a qualquer custo.
    Mas ainda há um problema. Se você fez essa mudança, já deve ter perce-
bido que o código parou de compilar. O problema é que o método close da
classe Connection lança uma checked exception, ou seja, uma exceção que
precisa ser tratada ou declarada. Adicionar um novo try catch dentro do
bloco finally teria um custo bem grande na legibilidade desse código. Re-
pare como ele ficaria:

♣✉❜❧✐❝ ❝❧❛ss ❘❡♣♦s✐t♦r✐♦❉❡Pr♦❞✉t♦s ④

     ♣✉❜❧✐❝ ❖❜s❡r✈❛❜❧❡▲✐st❁Pr♦❞✉t♦❃ ❧✐st❛✭✮ ④

          ✴✴ ❝ó❞✐❣♦ ♦♠✐t✐❞♦
          tr② ④
              ✴✴ ❝ó❞✐❣♦ ♦♠✐t✐❞♦
          ⑥ ❝❛t❝❤ ✭❙◗▲❊①❝❡♣t✐♦♥ ❡✮ ④
              t❤r♦✇ ♥❡✇ ❘✉♥t✐♠❡❊①❝❡♣t✐♦♥✭❡✮❀
          ⑥ ❢✐♥❛❧❧② ④
              tr② ④
                  ❝♦♥♥✳❝❧♦s❡✭✮❀
              ⑥ ❝❛t❝❤ ✭❙◗▲❊①❝❡♣t✐♦♥ ❡✮ ④
                  t❤r♦✇ ♥❡✇ ❘✉♥t✐♠❡❊①❝❡♣t✐♦♥✭❡✮❀
              ⑥
          ⑥
          r❡t✉r♥ ♣r♦❞✉t♦s❀
     ⑥
⑥

   O código ficou bem ruim, não acha? Por nossa sorte, o Java 7 trouxe
uma novidade muito interessante, conhecida como try-with-resources.
Você pode declarar e também inicializar a Connection dentro do try,
como a seguir:

♣✉❜❧✐❝ ❝❧❛ss ❘❡♣♦s✐t♦r✐♦❉❡Pr♦❞✉t♦s ④

     ♣✉❜❧✐❝ ❖❜s❡r✈❛❜❧❡▲✐st❁Pr♦❞✉t♦❃ ❧✐st❛✭✮ ④



                                                                              77


[PAGINA 88]
4.9. O padrão de projeto DAO                                      Casa do Código


           ✴✴ ❝ó❞✐❣♦ ♦♠✐t✐❞♦
           tr② ✭❈♦♥♥❡❝t✐♦♥ ❝♦♥♥ ❂ ♥❡✇ ❈♦♥♥❡❝t✐♦♥❋❛❝t♦r②✭✮
               ✳❣❡t❈♦♥♥❡❝t✐♦♥✭✮✮ ④
               ✴✴ ❝ó❞✐❣♦ ♦♠✐t✐❞♦
           ⑥ ❝❛t❝❤ ✭❙◗▲❊①❝❡♣t✐♦♥ ❡✮ ④
               t❤r♦✇ ♥❡✇ ❘✉♥t✐♠❡❊①❝❡♣t✐♦♥✭❡✮❀
           ⑥
           r❡t✉r♥ ♣r♦❞✉t♦s❀
     ⑥
⑥

    Pronto, a conexão será fechada para você, independente de se o código
funcionou ou lançou uma exception. Mas em que momento chamamos
o método close? A resposta é: em nenhum. O segredo desse recurso
está na interface AutoCloseable, que interfaces como a Connection
herdam. Você só pode usar o try-with-resources em objetos do tipo
AutoCloseable, assim o Java sabe exatamente qual o método que deve
ser chamado após a execução do seu try catch. Ele funciona como um
finally implícito.


4.9 O padrão de projeto DAO
Uma      última      alteração que podemos fazer nessa classe, a
RepositorioDeProdutos, é em seu nome. O que estamos fazendo
é uma prática bem comum: isolar a lógica de acesso ao banco de dados em
uma classe especialista neste trabalho. O fluxo atual está assim:




                       Fig. 4.7: Fluxo atual de acesso a dados.



    O benefício de encapsular essa regra de negócios (acesso ao banco)
em uma classe já é facilmente notado quando pensamos em evoluções
futuras. Por exemplo, se no lugar de persistirmos as informações em

78


[PAGINA 89]
Casa do Código                                     Capítulo 4. Banco de Dados e JDBC



um banco de dados resolvermos utilizar uma planilha de Excel, quantas
classes precisarão ser alteradas em nosso projeto? Apenas uma, nosso
RepositorioDeProdutos.




                 Fig. 4.8: Acesso a dados do banco ou planilha.



    Como o comportamento está isolado, encapsulado, fica fácil evoluir sem
causar efeitos colaterais indesejados. Para a classe Main, pouco importa
se quando ela chama repositorio.lista() a listagem é carregada de
uma planilha ou base de dados do MySQL, PostgreSQL, Oracle ou qualquer
outro. Pouco importa se estamos usando JDBC ou alguma ferramenta que
simplifique o trabalho, como o hibernate. O que importa para quem chama o
método lista é que ele retorne a listagem de produtos, e ponto.
    Essa boa pratica é tão conhecida e utilizada no dia a dia que acabou vi-
rando um dos mais importantes Design Patterns; ele é usado em todos os pro-
jetos que conheço! Talvez você já tenha ouvido falar do termo DAO, eis seu
significado: é um acrônimo para Data Access Object.
    Mesmo sem saber, já estamos usando o design pattern DAO, mas é muito
comum e recomendado seguirmos o padrão de nome desse tipo de classe.
Como ela encapsula acesso a dados da classe Produto, por padrão normal-
mente a chamamos de ProdutoDAO.
    Note que é muito similar ao que fizemos com a ConnectionFactory,
que é outro design pattern que conhecemos. Como ela é uma fábrica de
Connection, recebe como prefixo o nome da classe e como sufixo a palavra
Factory.
    Agora que sabemos a convenção, vamos fazer a alteração em nosso
código. Para renomear uma classe pelo Eclipse, basta selecionar essa classe

                                                                                 79


[PAGINA 90]
4.9. O padrão de projeto DAO                            Casa do Código


pelo package explorer (view lateral) e pressionar F2.




   Uma janela chamada Rename Compilation Unit deve ser exibida. Para
concluir, mudamos o nome para ProdutoDAO e clicamos em Finish.




80


[PAGINA 91]
Casa do Código                                Capítulo 4. Banco de Dados e JDBC




    Nosso DAO completo deve ficar assim:

♣✉❜❧✐❝ ❝❧❛ss Pr♦❞✉t♦❉❆❖ ④

     ♣✉❜❧✐❝ ❖❜s❡r✈❛❜❧❡▲✐st❁Pr♦❞✉t♦❃ ❧✐st❛✭✮ ④

          ❖❜s❡r✈❛❜❧❡▲✐st❁Pr♦❞✉t♦❃ ♣r♦❞✉t♦s ❂
              ♦❜s❡r✈❛❜❧❡❆rr❛②▲✐st✭✮❀
          Pr❡♣❛r❡❞❙t❛t❡♠❡♥t ♣s❀
          tr② ✭❈♦♥♥❡❝t✐♦♥ ❝♦♥♥ ❂
                  ♥❡✇ ❈♦♥♥❡❝t✐♦♥❋❛❝t♦r②✭✮✳❣❡t❈♦♥♥❡❝t✐♦♥✭✮✮ ④
              ♣s ❂ ❝♦♥♥✳♣r❡♣❛r❡❙t❛t❡♠❡♥t✭
                      ✧s❡❧❡❝t ✯ ❢r♦♠ ♣r♦❞✉t♦s✧✮❀
              ❘❡s✉❧t❙❡t r❡s✉❧t❙❡t ❂ ♣s✳❡①❡❝✉t❡◗✉❡r②✭✮❀

                 ✇❤✐❧❡✭r❡s✉❧t❙❡t✳♥❡①t✭✮✮ ④
                     ▲✐✈r♦❋✐s✐❝♦ ❧✐✈r♦ ❂
                         ♥❡✇ ▲✐✈r♦❋✐s✐❝♦✭♥❡✇ ❆✉t♦r✭✮✮❀
                     ❧✐✈r♦✳s❡t◆♦♠❡✭r❡s✉❧t❙❡t✳❣❡t❙tr✐♥❣✭✧♥♦♠❡✧✮✮❀


                                                                            81


[PAGINA 92]
4.9. O padrão de projeto DAO                                Casa do Código


                       ❧✐✈r♦✳s❡t❉❡s❝r✐❝❛♦✭r❡s✉❧t❙❡t✳❣❡t❙tr✐♥❣✭
                                           ✧❞❡s❝r✐❝❛♦✧✮✮❀
                       ❧✐✈r♦✳s❡t❱❛❧♦r✭r❡s✉❧t❙❡t✳❣❡t❉♦✉❜❧❡✭✧✈❛❧♦r✧✮✮❀
                       ❧✐✈r♦✳s❡t■s❜♥✭r❡s✉❧t❙❡t✳❣❡t❙tr✐♥❣✭✧✐s❜♥✧✮✮❀
                       ♣r♦❞✉t♦s✳❛❞❞✭❧✐✈r♦✮❀
               ⑥
               r❡s✉❧t❙❡t✳❝❧♦s❡✭✮❀
               ♣s✳❝❧♦s❡✭✮❀
           ⑥ ❝❛t❝❤ ✭❙◗▲❊①❝❡♣t✐♦♥ ❡✮ ④
               t❤r♦✇ ♥❡✇ ❘✉♥t✐♠❡❊①❝❡♣t✐♦♥✭❡✮❀
           ⑥
           r❡t✉r♥ ♣r♦❞✉t♦s❀
     ⑥

     ♣✉❜❧✐❝ ✈♦✐❞ ❛❞✐❝✐♦♥❛✭Pr♦❞✉t♦ ♣r♦❞✉t♦✮ ④
         Pr❡♣❛r❡❞❙t❛t❡♠❡♥t ♣s❀

           tr② ✭❈♦♥♥❡❝t✐♦♥ ❝♦♥♥ ❂
               ♥❡✇ ❈♦♥♥❡❝t✐♦♥❋❛❝t♦r②✭✮✳❣❡t❈♦♥♥❡❝t✐♦♥✭✮✮ ④
               ♣s ❂ ❝♦♥♥✳♣r❡♣❛r❡❙t❛t❡♠❡♥t✭✧✐♥s❡rt ✐♥t♦ ♣r♦❞✉t♦s
                       ✭♥♦♠❡✱✧ ✰ ✧ ❞❡s❝r✐❝❛♦✱ ✈❛❧♦r✱ ✐s❜♥✮
                       ✈❛❧✉❡s ✭❄✱❄✱❄✱❄✮✧✮❀

                 ♣s✳s❡t❙tr✐♥❣✭✶✱ ♣r♦❞✉t♦✳❣❡t◆♦♠❡✭✮✮❀
                 ♣s✳s❡t❙tr✐♥❣✭✷✱ ♣r♦❞✉t♦✳❣❡t❉❡s❝r✐❝❛♦✭✮✮❀
                 ♣s✳s❡t❉♦✉❜❧❡✭✸✱ ♣r♦❞✉t♦✳❣❡t❱❛❧♦r✭✮✮❀
                 ♣s✳s❡t❙tr✐♥❣✭✹✱ ♣r♦❞✉t♦✳❣❡t■s❜♥✭✮✮❀

               ♣s✳❡①❡❝✉t❡✭✮❀
               ♣s✳❝❧♦s❡✭✮❀
           ⑥ ❝❛t❝❤ ✭❙◗▲❊①❝❡♣t✐♦♥ ❡✮ ④
               t❤r♦✇ ♥❡✇ ❘✉♥t✐♠❡❊①❝❡♣t✐♦♥✭❡✮❀
           ⑥
     ⑥
⑥

   O único impacto em nossa classe Main será na linha em que usávamos
o RepositorioDeProdutos:
❖❜s❡r✈❛❜❧❡▲✐st❁Pr♦❞✉t♦❃ ♣r♦❞✉t♦s ❂

82


[PAGINA 93]
Casa do Código                                 Capítulo 4. Banco de Dados e JDBC



          ♥❡✇ ❘❡♣♦s✐t♦r✐♦❉❡Pr♦❞✉t♦s✭✮✳❧✐st❛✭✮❀

    Agora que ele chama ProdutoDAO, a linha ficará assim:
❖❜s❡r✈❛❜❧❡▲✐st❁Pr♦❞✉t♦❃ ♣r♦❞✉t♦s ❂ ♥❡✇ Pr♦❞✉t♦❉❆❖✭✮✳❧✐st❛✭✮❀

   Mas não se preocupe em alterar manualmente, o Eclipse já fez isso para
você.
   O fluxo agora é:




             Fig. 4.11: Acesso a dados encapsulado em um DAO.




 Outras alternativas para renomear classes

    A forma que vimos é uma das muitas de se renomear uma classe pela
 IDE. Outra opção bastante comum pelo Eclipse é utilizando o atalho
 Control + Shift + R (rename). A diferença é que o utilizamos di-
 retamente na classe, com o cursor sob seu nome:




     Basta mudar seu nome e depois pressionar Enter. Todos que fazem
 referência para essa classe também serão atualizados automaticamente.


                                                                             83


[PAGINA 94]
4.9. O padrão de projeto DAO                                    Casa do Código


   Também podemos renomear o pacote do nosso ProdutoDAO, que atual-
mente se chama repositorio. Vamos alterar para dao. O processo será o
mesmo, clicamos no pacote, pressionamos F2, escolhemos um novo nome e
depois Finish. Ele ficará assim:




    A vantagem de utilizar essas convenções de nomes é que é muito mais
fácil para quem cair de paraquedas no projeto saiba se contextualizar. Se você
entrar hoje em um projeto e precisar alterar a forma que um Usuario é
persistido, qual classe você vai abrir? O UsuarioDAO. Não tem erro, você
não precisa saber nada sobre o projeto para saber disso.




84


[PAGINA 95]
Capítulo 5

Threads e Paralelismo
A consulta ao banco de dados que alimenta nossa listagem de produtos é su-
ficientemente rápida, afinal estamos trabalhando com poucos valores. Mas já
parou para pensar o que aconteceria se ela demorasse para responder? Outro
ponto que poderia causar um problema é a exportação dessa lista para o ar-
quivo CSV. Quanto mais produtos, mais ela deve demorar. Como nossa apli-
cação reage enquanto uma tarefa está demorando para ser executada?
     Neste capítulo, veremos esse problema em prática, assim como uma al-
ternativa para resolvê-lo. Vamos conhecer um pouco da forma como o Java
faz para executar ações em paralelo, com uso de Threads, classes anônimas
e muitos lambdas do Java 8. Se você ainda não está acostumado com esse
recurso, com certeza vai aproveitar bastante os exemplos deste capítulo para
praticar.


[PAGINA 96]
5.1. Processamento demorado, e agora?                           Casa do Código


5.1 Processamento demorado, e agora?
Uma forma simples de experienciar isso em prática seria forçando nossa apli-
cação a dormir por alguns instantes, no momento em que geramos o arquivo
CSV. Assim conseguimos simular que a função demora cerca de 20 segundos
para ser executada.

❜✉tt♦♥✳s❡t❖♥❆❝t✐♦♥✭❡✈❡♥t ✲❃ ④
    ❚❤r❡❛❞✳s❧❡❡♣✭✷✵✵✵✵✮❀
    ❡①♣♦rt❛❊♠❈❙❱✭♣r♦❞✉t♦s✮❀
⑥✮❀

    Veja que quem cuidou desse trabalho foi o método estático sleep, pre-
sente na classe Thread (que muito em breve será desmistificada). Essa classe
está presente no pacote java.lang, portanto não precisa ser importada. Ele
recebe como parâmetro o tempo em milissegundos em que deve dormir (tem-
porariamente pausar) a linha de execução atual, e o força a tratar ou declarar
uma InterruptedException.

❜✉tt♦♥✳s❡t❖♥❆❝t✐♦♥✭❡✈❡♥t ✲❃ ④
    tr② ④
        ❚❤r❡❛❞✳s❧❡❡♣✭✷✵✵✵✵✮❀
    ⑥ ❝❛t❝❤ ✭■♥t❡rr✉♣t❡❞❊①❝❡♣t✐♦♥ ❡✮ ④
        ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❖♣s✱ ♦❝♦rr❡✉ ✉♠ ❡rr♦✿ ✧✰ ❡✮❀
    ⑥
    ❡①♣♦rt❛❊♠❈❙❱✭♣r♦❞✉t♦s✮❀
⑥✮❀

    Depois dessa alteração, a ação de exportar o arquivo produtos.csv vai
levar pelo menos 20 segundos para ser executada. Execute a aplicação para
ver isso acontecendo.
    O que acontece se você tentar redimencionar a janela, clicar nas linhas da
tabela, ou fazer qualquer coisa similar enquanto a ação do button está sendo
executada?




86


[PAGINA 97]
Casa do Código                                       Capítulo 5. Threads e Paralelismo




            Fig. 5.1: Aplicação não respondendo, totalmente travada.


      A aplicação fica totalmente travada!

A necessidade de executar ações em paralelo
    Podem ser muitas as situações em que precisamos executar ações em par-
alelo. Em um sistema operacional, por exemplo, fazemos isso o tempo todo!
Podemos fazer um download e ao mesmo tempo navegar na internet. Já pen-
sou como seria ter que esperar o download terminar para só depois fazer qual-
quer outra coisa? O próprio sistema operacional já gerencia todos os progra-
mas executados em vários processos paralelos, não precisamos nos preocupar
com isso.
    Em nossa aplicação Java também podemos executar ações em paralelo,
como exportar os dados da listagem sem ter que travar as demais funções e,
enquanto isso, mostrar o avanço da função de exportar para dar um retorno
(feedback) ao usuário.


5.2      Trabalhando com Threads em Java
Em Java podemos criar linhas de execuções paralelas utilizando a classe
Thread, do pacote java.lang, a mesma que utilizamos para fazer a apli-

                                                                                  87


[PAGINA 98]
5.2. Trabalhando com Threads em Java                           Casa do Código


cação dormir por 20 segundos.
    Para criar e iniciar a execução de uma thread, só precisamos instanciar
um objeto desse tipo e chamar seu método start:
❚❤r❡❛❞ t❤r❡❛❞ ❂ ♥❡✇ ❚❤r❡❛❞✭✮❀
t❤r❡❛❞✳st❛rt✭✮❀

    Mas há uma questão, o que essa thread faz? Criamos uma nova linha
de execução, mas em nenhum momento dissemos o que ela deve fazer. Ela
morrerá assim que for criada.
    A classe Thread tem um construtor que recebe como argumento um ob-
jeto com o código que queremos executar, tudo que precisamos fazer é criar
essa classe. Vamos chamá-la de ExportadorDeCSV, já que é isso o que quer-
emos fazer em paralelo.
♣❛❝❦❛❣❡ t❤r❡❛❞s❀

♣✉❜❧✐❝ ❝❧❛ss ❊①♣♦rt❛❞♦r❉❡❈❙❱ ④

      ♣✉❜❧✐❝ ✈♦✐❞ ❡①♣♦rt❛✭✮ ④
          ✴✴ ❝ó❞✐❣♦ q✉❡ ❞❡✈❡ s❡r ❡①❡❝✉t❛❞♦ ❡♠ ♣❛r❛❧❡❧♦
      ⑥
⑥

   Vamos, agora, no momento de criar uma Thread, passar o exportador
como argumento:
❊①♣♦rt❛❞♦r❉❡❈❙❱ ❡①♣♦rt❛❞♦r ❂ ♥❡✇ ❊①♣♦rt❛❞♦r❉❡❈❙❱✭✮❀
❚❤r❡❛❞ t❤r❡❛❞ ❂ ♥❡✇ ❚❤r❡❛❞✭❡①♣♦rt❛❞♦r✮❀
t❤r❡❛❞✳st❛rt✭✮❀

     Tudo parece certo, mas esse código não vai compilar. O erro será:
❝♦♥str✉❝t♦r ❥❛✈❛✳❧❛♥❣✳❚❤r❡❛❞✳❚❤r❡❛❞✭❥❛✈❛✳❧❛♥❣✳❘✉♥♥❛❜❧❡✮ ✐s
♥♦t ❛♣♣❧✐❝❛❜❧❡✳ ✭❛r❣✉♠❡♥t ♠✐s♠❛t❝❤❀ t❤r❡❛❞s✳❊①♣♦rt❛❞♦r❉❡❈❙❱
❝❛♥♥♦t ❜❡ ❝♦♥✈❡rt❡❞ t♦ ❥❛✈❛✳❧❛♥❣✳❘✉♥♥❛❜❧❡✮

    Faz sentido, afinal, como a Thread saberá qual o método que deve ser
executado? E se a classe ExportadorDeCSV tivesse dez métodos, como ela
escolheria um?

88


[PAGINA 99]
Casa do Código                                       Capítulo 5. Threads e Paralelismo



5.3    O contrato Runnable
Para ensinar à classe Thread qual método deve ser executado e dar uma
garantia ao compilador de que esse método está declarado em nossa classe,
usamos um contrato, uma interface Java. Não precisamos criar uma nova in-
terface; se você olhar com atenção na mensagem gerada pelo erro de compi-
lação, você perceberá que esse contrato já existe e é esperado. Estamos falando
da interface java.lang.Runnable.
    Uma classe que assina o contrato Runnable assume a responsabilidade
de ser um executável. Essa interface tem um único método, chamado run.
Por esse motivo, a Thread sabe exatamente como executá-la.
    Vamos modificar nosso ExportadorDeCSV para implementar essa in-
terface. Agora que sabemos como o método deve se chamar, trocaremos o
nome do método de exporta para run:

♣❛❝❦❛❣❡ t❤r❡❛❞s❀

♣✉❜❧✐❝ ❝❧❛ss ❊①♣♦rt❛❞♦r❉❡❈❙❱ ✐♠♣❧❡♠❡♥ts ❘✉♥♥❛❜❧❡ ④

      ❅❖✈❡rr✐❞❡
      ♣✉❜❧✐❝ ✈♦✐❞ r✉♥✭✮ ④
          ✴✴ ❝ó❞✐❣♦ q✉❡ ❞❡✈❡ s❡r ❡①❡❝✉t❛❞♦ ❡♠ ♣❛r❛❧❡❧♦
      ⑥
⑥

   Ótimo, nosso código passou a compilar.
   Para testar, coloque um System.out.println no método run. Algo
simples, como:

♣❛❝❦❛❣❡ t❤r❡❛❞s❀

♣✉❜❧✐❝ ❝❧❛ss ❊①♣♦rt❛❞♦r❉❡❈❙❱ ✐♠♣❧❡♠❡♥ts ❘✉♥♥❛❜❧❡ ④

      ❅❖✈❡rr✐❞❡
      ♣✉❜❧✐❝ ✈♦✐❞ r✉♥✭✮ ④
          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❘♦❞❛♥❞♦ ❡♠ ♣❛r❛❧❡❧♦✦✧✮❀
      ⑥
⑥

                                                                                  89


[PAGINA 100]
5.3. O contrato Runnable                                      Casa do Código


     Agora, crie a classe TestandoThread, com o seguinte método main:

♣❛❝❦❛❣❡ t❤r❡❛❞s❀

♣✉❜❧✐❝ ❝❧❛ss ❚❡st❛♥❞♦❚❤r❡❛❞ ④

      ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥ ✭❙tr✐♥❣✳✳✳ ❛r❣s✮ ④

            ❊①♣♦rt❛❞♦r❉❡❈❙❱ ❡①♣♦rt❛❞♦r ❂ ♥❡✇ ❊①♣♦rt❛❞♦r❉❡❈❙❱✭✮❀
            ❚❤r❡❛❞ t❤r❡❛❞ ❂ ♥❡✇ ❚❤r❡❛❞✭❡①♣♦rt❛❞♦r✮❀
            t❤r❡❛❞✳st❛rt✭✮❀
            ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❚❡r♠✐♥❡✐ ❞❡ r♦❞❛r ♦ ♠❛✐♥✧✮❀
      ⑥
⑥

     Execute o código para ver o resultado. Deverá ser algo como:

❘♦❞❛♥❞♦ ❡♠ ♣❛r❛❧❡❧♦✦
❚❡r♠✐♥❡✐ ❞❡ r♦❞❛r ♦ ♠❛✐♥

    A ordem pode variar, já que são duas linhas de execuções em paralelo.
Mas não se preocupe com isso agora. O importante é as duas mensagens
terem sido impressas no console. Note que em nenhum momento chamamos
o método run do nosso ExportadorDeCSV, mas ao chamar o método
start da classe Thread ela fez isso por nós.




90


[PAGINA 101]
Casa do Código                                       Capítulo 5. Threads e Paralelismo




  Para saber mais: escalonador de Threads

      Como executamos ações em paralelo quando existe um único pro-
  cessador na máquina? O segredo está no scheduler de threads. Ele é
  um escalonador que pega todas as threads que precisam ser executadas
  e faz seu processador alternar entre elas. Isso acontece tão rápido que
  parece que as duas (ou mais) threads estão rodando ao mesmo tempo.
  Essa alternação que ele faz é conhecida como context switch, ou troca
  de contexto.
      Quando existem dois ou mais processadores, a máquina virtual do
  Java e grande parte (se não todos) os sistemas operacionais conseguem
  tirar proveito disso. Nesse caso, verdadeiramente teremos execuções par-
  alelas, ainda escalonadas pelo scheduler do Java. Isso porque podemos
  ter 20 threads sendo executadas em dois processadores, por exemplo. A
  diferença é que a troca de contexto acontecerá entre eles e não em um
  único processador.


5.4 Threads com classes anônimas e lambdas
No lugar de criarmos a classe ExportadorDeCSV implementando um
Runnable, poderíamos fazer isso diretamente utilizando uma classe anôn-
ima. Isso é extremamente comum quando estamos trabalhando com
Threads. O código ficaria assim:
❘✉♥♥❛❜❧❡ ❡①♣♦rt❛❞♦r ❂ ♥❡✇ ❘✉♥♥❛❜❧❡✭✮ ④
    ❅❖✈❡rr✐❞❡
    ♣✉❜❧✐❝ ✈♦✐❞ r✉♥✭✮ ④
        ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❘♦❞❛♥❞♦ ❡♠ ♣❛r❛❧❡❧♦✦✧✮❀
    ⑥
⑥❀

❚❤r❡❛❞ t❤r❡❛❞ ❂ ♥❡✇ ❚❤r❡❛❞✭❡①♣♦rt❛❞♦r✮❀
t❤r❡❛❞✳st❛rt✭✮❀

   No lugar de extrair as variáveis intermediárias, é natural fazer isso direta-
mente:

                                                                                   91


[PAGINA 102]
5.4. Threads com classes anônimas e lambdas                   Casa do Código


♥❡✇ ❚❤r❡❛❞✭♥❡✇ ❘✉♥♥❛❜❧❡✭✮ ④
    ❅❖✈❡rr✐❞❡
    ♣✉❜❧✐❝ ✈♦✐❞ r✉♥✭✮ ④
        ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❘♦❞❛♥❞♦ ❡♠ ♣❛r❛❧❡❧♦✦✧✮❀
    ⑥
⑥✮✳st❛rt✭✮❀

     O código completo da classe TestandoThread fica:

♣❛❝❦❛❣❡ t❤r❡❛❞s❀

♣✉❜❧✐❝ ❝❧❛ss ❚❡st❛♥❞♦❚❤r❡❛❞ ④

      ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥ ✭❙tr✐♥❣✳✳✳ ❛r❣s✮ ④

            ♥❡✇ ❚❤r❡❛❞✭♥❡✇ ❘✉♥♥❛❜❧❡✭✮ ④
                ❅❖✈❡rr✐❞❡
                ♣✉❜❧✐❝ ✈♦✐❞ r✉♥✭✮ ④
                    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❘♦❞❛♥❞♦ ❡♠ ♣❛r❛❧❡❧♦✦✧✮❀
                ⑥
            ⑥✮✳st❛rt✭✮❀
            ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❚❡r♠✐♥❡✐ ❞❡ r♦❞❛r ♦ ♠❛✐♥✧✮❀
      ⑥
⑥

    Vamos executar o código para ver o resultado? A mesma coisa. As duas
mensagens serão impressas, podendo variar um pouco a ordem, já que são
executadas em paralelo.
    O problema desse código está tanto na verbosidade quanto na sintaxe, que
é bem poluída. Chegam a chamar esse tipo de código de “problema vertical
    , por causa da quantidade de linhas.
    Essa foi uma das motivações para introdução das expressões lambdas, do
Java 8. Assim como já estamos usando esse recurso com a ação do button,
podemos usar com o Runnable. O segredo está no conceito de interface
funcional, que é como uma interface de um único método abstrato é chamada
no Java 8.
    Em outras palavras, como um Runnable só tem um método abstrato,
podemos usar a sintaxe do lambda, já que o Java saberá exatamente qual

92


[PAGINA 103]
Casa do Código                                    Capítulo 5. Threads e Paralelismo



método está sendo implementado. O código ficará assim:

♣❛❝❦❛❣❡ t❤r❡❛❞s❀

♣✉❜❧✐❝ ❝❧❛ss ❚❡st❛♥❞♦❚❤r❡❛❞ ④

     ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥ ✭❙tr✐♥❣✳✳✳ ❛r❣s✮ ④

          ♥❡✇ ❚❤r❡❛❞✭✭✮ ✲❃ ④
              ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❘♦❞❛♥❞♦ ❡♠ ♣❛r❛❧❡❧♦✦✧✮❀
          ⑥✮✳st❛rt✭✮❀
          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❚❡r♠✐♥❡✐ ❞❡ r♦❞❛r ♦ ♠❛✐♥✧✮❀
     ⑥
⑥

    O que acha, mais simples? A sintaxe pode parecer estranha no começo,
mas sem dúvida o código está mais enxuto. Como existe apenas uma única
instrução dentro da expressão lambda, podemos tirar as chaves, ponto e vír-
gula e colocar tudo em um único statement:

♣❛❝❦❛❣❡ t❤r❡❛❞s❀

♣✉❜❧✐❝ ❝❧❛ss ❚❡st❛♥❞♦❚❤r❡❛❞ ④

     ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥ ✭❙tr✐♥❣✳✳✳ ❛r❣s✮ ④

          ♥❡✇ ❚❤r❡❛❞✭✭✮ ✲❃ ❙②st❡♠✳♦✉t
              ✳♣r✐♥t❧♥✭✧❘♦❞❛♥❞♦ ❡♠ ♣❛r❛❧❡❧♦✦✧✮✮✳st❛rt✭✮❀

          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❚❡r♠✐♥❡✐ ❞❡ r♦❞❛r ♦ ♠❛✐♥✧✮❀
     ⑥
⑥

    O foco do livro não é Java 8, mas se você ainda não está acostumado com
as expressões lambdas e outros recursos, não deixe de praticar. Ficou com
alguma dúvida? Lembre-se de mandar um e-mail na lista do grupo.




                                                                                93


[PAGINA 104]
5.5. Exportando em uma thread separada                       Casa do Código


5.5     Exportando em uma thread separada
Pronto, agora que conhecemos um pouco mais sobre Threads em Java,
podemos atacar o problema da lógica de exportar em CSV. Para não travar
a aplicação, podemos rodar toda a lógica de exportar a lista de produtos em
paralelo!
    Vamos aplicar essa mudança à classe Main. A action do button ficará
assim:

❇✉tt♦♥ ❜✉tt♦♥ ❂ ♥❡✇ ❇✉tt♦♥✭✧❊①♣♦rt❛r ❈❙❱✧✮❀

❜✉tt♦♥✳s❡t❖♥❆❝t✐♦♥✭❡✈❡♥t ✲❃ ④

      ♥❡✇ ❚❤r❡❛❞✭✭✮ ✲❃ ④
          tr② ④
              ❚❤r❡❛❞✳s❧❡❡♣✭✷✵✵✵✵✮❀
          ⑥ ❝❛t❝❤ ✭■♥t❡rr✉♣t❡❞❊①❝❡♣t✐♦♥ ❡✮ ④
              ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❖♣s✱ ♦❝♦rr❡✉ ✉♠ ❡rr♦✿ ✧✰ ❡✮❀
          ⑥
          ❡①♣♦rt❛❊♠❈❙❱✭♣r♦❞✉t♦s✮❀
      ⑥✮✳st❛rt✭✮❀
⑥✮❀




94


[PAGINA 105]
Casa do Código                                     Capítulo 5. Threads e Paralelismo




  Se você está com Java 7...

     Em Java 7, com uso das classes anônimas, esse código ficaria assim:

  ❇✉tt♦♥ ❜✉tt♦♥ ❂ ♥❡✇ ❇✉tt♦♥✭✧❊①♣♦rt❛r ❈❙❱✧✮❀

  ❜✉tt♦♥✳s❡t❖♥❆❝t✐♦♥✭♥❡✇ ❊✈❡♥t❍❛♥❞❧❡r❁❆❝t✐♦♥❊✈❡♥t❃✭✮ ④
      ❅❖✈❡rr✐❞❡
      ♣✉❜❧✐❝ ✈♦✐❞ ❤❛♥❞❧❡✭❆❝t✐♦♥❊✈❡♥t ❡✈❡♥t✮ ④

            ♥❡✇ ❚❤r❡❛❞✭♥❡✇ ❘✉♥♥❛❜❧❡✭✮ ④
                ❅❖✈❡rr✐❞❡
                ♣✉❜❧✐❝ ✈♦✐❞ r✉♥✭✮ ④
                    tr② ④
                        ❚❤r❡❛❞✳s❧❡❡♣✭✷✵✵✵✵✮❀
                    ⑥ ❝❛t❝❤ ✭■♥t❡rr✉♣t❡❞❊①❝❡♣t✐♦♥ ❡✮ ④
                        ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❖♣s✱
                            ♦❝♦rr❡✉ ✉♠ ❡rr♦✿ ✧✰ ❡✮❀
                    ⑥
                    ❡①♣♦rt❛❊♠❈❙❱✭♣r♦❞✉t♦s✮❀
                ⑥
            ⑥✮✳st❛rt✭✮❀
        ⑥
  ⑥✮❀

     Vale lembrar que você não precisa ter o Java 8 instalado para rodar
  esses exemplos, no final do capítulo vou mostrar o código completo com
  Java 7 também. Aproveite para fazer uma comparação entre as duas sin-
  taxes.


    Para melhorar um pouco a legibilidade, vamos extrair o código do
Thread.sleep, que faz a aplicação dormir por 20 segundos, para dentro
de um método:

♣r✐✈❛t❡ ✈♦✐❞ ❞♦r♠❡P♦r❱✐♥t❡❙❡❣✉♥❞♦s✭✮ ④
    tr② ④
        ❚❤r❡❛❞✳s❧❡❡♣✭✷✵✵✵✵✮❀


                                                                                 95


[PAGINA 106]
5.5. Exportando em uma thread separada                         Casa do Código


      ⑥ ❝❛t❝❤ ✭■♥t❡rr✉♣t❡❞❊①❝❡♣t✐♦♥ ❡✮ ④
          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❖♣s✱ ♦❝♦rr❡✉ ✉♠ ❡rr♦✿ ✧✰ ❡✮❀
      ⑥
⑥

     Agora o código da action de exportar em CSV fica assim:

❜✉tt♦♥✳s❡t❖♥❆❝t✐♦♥✭❡✈❡♥t ✲❃ ④
    ♥❡✇ ❚❤r❡❛❞✭✭✮ ✲❃ ④
        ❞♦r♠❡P♦r❱✐♥t❡❙❡❣✉♥❞♦s✭✮❀
        ❡①♣♦rt❛❊♠❈❙❱✭♣r♦❞✉t♦s✮❀
    ⑥✮✳st❛rt✭✮❀
⑥✮❀

    Com essas alterações, o código completo da classe Main deve ficar da
seguinte forma:

♣❛❝❦❛❣❡ ❛♣♣❧✐❝❛t✐♦♥❀

✴✴ ✐♠♣♦rts ♦♠✐t✐❞♦s

❅❙✉♣♣r❡ss❲❛r♥✐♥❣s✭④ ✧✉♥❝❤❡❝❦❡❞✧✱ ✧r❛✇t②♣❡s✧ ⑥✮
♣✉❜❧✐❝ ❝❧❛ss ▼❛✐♥ ❡①t❡♥❞s ❆♣♣❧✐❝❛t✐♦♥ ④

      ❅❖✈❡rr✐❞❡
      ♣✉❜❧✐❝ ✈♦✐❞ st❛rt✭❙t❛❣❡ ♣r✐♠❛r②❙t❛❣❡✮ ④

            ●r♦✉♣ ❣r♦✉♣ ❂ ♥❡✇ ●r♦✉♣✭✮❀
            ❙❝❡♥❡ s❝❡♥❡ ❂ ♥❡✇ ❙❝❡♥❡✭❣r♦✉♣✱ ✻✾✵✱ ✺✶✵✮❀

            ❖❜s❡r✈❛❜❧❡▲✐st❁Pr♦❞✉t♦❃ ♣r♦❞✉t♦s ❂
                ♥❡✇ Pr♦❞✉t♦❉❆❖✭✮✳❧✐st❛✭✮❀

            ❚❛❜❧❡❱✐❡✇❁Pr♦❞✉t♦❃ t❛❜❧❡❱✐❡✇ ❂
                ♥❡✇ ❚❛❜❧❡❱✐❡✇❁❃✭♣r♦❞✉t♦s✮❀

            ❚❛❜❧❡❈♦❧✉♠♥ ♥♦♠❡❈♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭✧◆♦♠❡✧✮❀
            ♥♦♠❡❈♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭✶✽✵✮❀
            ♥♦♠❡❈♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
                ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②✭✧♥♦♠❡✧✮✮❀

96


[PAGINA 107]
Casa do Código                               Capítulo 5. Threads e Paralelismo




          ❚❛❜❧❡❈♦❧✉♠♥ ❞❡s❝❈♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭✧❉❡s❝r✐çã♦✧✮❀
          ❞❡s❝❈♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭✷✸✵✮❀
          ❞❡s❝❈♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
              ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②✭✧❞❡s❝r✐❝❛♦✧✮✮❀

          ❚❛❜❧❡❈♦❧✉♠♥ ✈❛❧♦r❈♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭✧❱❛❧♦r✧✮❀
          ✈❛❧♦r❈♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭✻✵✮❀
          ✈❛❧♦r❈♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
              ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②✭✧✈❛❧♦r✧✮✮❀

          ❚❛❜❧❡❈♦❧✉♠♥ ✐s❜♥❈♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭✧■❙❇◆✧✮❀
          ✐s❜♥❈♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭✶✽✵✮❀
          ✐s❜♥❈♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
              ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②✭✧✐s❜♥✧✮✮❀

          t❛❜❧❡❱✐❡✇✳❣❡t❈♦❧✉♠♥s✭✮✳❛❞❞❆❧❧✭♥♦♠❡❈♦❧✉♠♥✱ ❞❡s❝❈♦❧✉♠♥✱
              ✈❛❧♦r❈♦❧✉♠♥✱ ✐s❜♥❈♦❧✉♠♥✮❀

          ❢✐♥❛❧ ❱❇♦① ✈❜♦① ❂ ♥❡✇ ❱❇♦①✭t❛❜❧❡❱✐❡✇✮❀
          ✈❜♦①✳s❡tP❛❞❞✐♥❣✭♥❡✇ ■♥s❡ts✭✼✵✱ ✵✱ ✵ ✱✶✵✮✮❀

          ▲❛❜❡❧ ❧❛❜❡❧ ❂ ♥❡✇ ▲❛❜❡❧✭✧▲✐st❛❣❡♠ ❞❡ ▲✐✈r♦s✧✮❀

          ❧❛❜❡❧✳s❡t❋♦♥t✭❋♦♥t
              ✳❢♦♥t✭✧▲✉❝✐❞❛ ●r❛♥❞❡✧✱ ❋♦♥tP♦st✉r❡✳❘❊●❯▲❆❘✱ ✸✵✮✮❀

          ❧❛❜❡❧✳s❡tP❛❞❞✐♥❣✭♥❡✇ ■♥s❡ts✭✷✵✱ ✵✱ ✶✵✱ ✶✵✮✮❀

          ❇✉tt♦♥ ❜✉tt♦♥ ❂ ♥❡✇ ❇✉tt♦♥✭✧❊①♣♦rt❛r ❈❙❱✧✮❀
          ❜✉tt♦♥✳s❡t▲❛②♦✉t❳✭✺✼✺✮❀
          ❜✉tt♦♥✳s❡t▲❛②♦✉t❨✭✷✺✮❀

          ❜✉tt♦♥✳s❡t❖♥❆❝t✐♦♥✭❡✈❡♥t ✲❃ ④
              ♥❡✇ ❚❤r❡❛❞✭✭✮ ✲❃ ④
                  ❞♦r♠❡P♦r❱✐♥t❡❙❡❣✉♥❞♦s✭✮❀
                  ❡①♣♦rt❛❊♠❈❙❱✭♣r♦❞✉t♦s✮❀
              ⑥✮✳st❛rt✭✮❀
          ⑥✮❀

                                                                          97


[PAGINA 108]
5.5. Exportando em uma thread separada                        Casa do Código




            ❣r♦✉♣✳❣❡t❈❤✐❧❞r❡♥✭✮✳❛❞❞❆❧❧✭❧❛❜❡❧✱ ✈❜♦①✱ ❜✉tt♦♥✮❀

            ♣r✐♠❛r②❙t❛❣❡✳s❡t❚✐t❧❡✭
                ✧❙✐st❡♠❛ ❞❛ ❧✐✈r❛r✐❛ ❝♦♠ ❏❛✈❛ ❋❳✧✮❀
            ♣r✐♠❛r②❙t❛❣❡✳s❡t❙❝❡♥❡✭s❝❡♥❡✮❀
            ♣r✐♠❛r②❙t❛❣❡✳s❤♦✇✭✮❀
      ⑥

      ♣r✐✈❛t❡ ✈♦✐❞ ❡①♣♦rt❛❊♠❈❙❱✭❖❜s❡r✈❛❜❧❡▲✐st❁Pr♦❞✉t♦❃ ♣r♦❞✉t♦s✮④
          tr② ④
              ♥❡✇ ❊①♣♦rt❛❞♦r✭✮✳♣❛r❛❈❙❱✭♣r♦❞✉t♦s✮❀
          ⑥ ❝❛t❝❤ ✭■❖❊①❝❡♣t✐♦♥ ❡✮ ④
              ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❊rr♦ ❛♦ ❡①♣♦rt❛r✿ ✧✰ ❡✮❀
          ⑥
      ⑥

      ♣r✐✈❛t❡ ✈♦✐❞ ❞♦r♠❡P♦r❱✐♥t❡❙❡❣✉♥❞♦s✭✮ ④
          tr② ④
              ❚❤r❡❛❞✳s❧❡❡♣✭✷✵✵✵✵✮❀
          ⑥ ❝❛t❝❤ ✭■♥t❡rr✉♣t❡❞❊①❝❡♣t✐♦♥ ❡✮ ④
              ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❖♣s✱ ♦❝♦rr❡✉ ✉♠ ❡rr♦✿ ✧✰ ❡✮❀
          ⑥
      ⑥

      ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④
          ❧❛✉♥❝❤✭❛r❣s✮❀
      ⑥
⑥

     Pronto para testar mais uma vez? Execute a aplicação e mande exportar a
lista de produtos como CSV. Você vai perceber que, mesmo que esse código
demore 20 segundos para ser executado, o restante da aplicação continua fun-
cionando sem travar. Experimente redimencionar a janela, clicar nas linhas
da tabela etc. Tudo continua funcionando.




98


[PAGINA 109]
Casa do Código                                      Capítulo 5. Threads e Paralelismo



5.6 Um pouco mais sobre as Threads
Trabalhar com Threads nem sempre é um sonho. Quando estamos trabal-
hando com linhas de execuções diferentes, a complexidade de nosso código
aumenta. Há ainda uma preocupação constante, que são os temíveis proble-
mas de concorrência. O que poderia dar errado?
   Dê uma boa olhada no seguinte código:
♣✉❜❧✐❝ ❝❧❛ss ▲✐✈r♦❋✐s✐❝♦ ❡①t❡♥❞s ▲✐✈r♦
        ✐♠♣❧❡♠❡♥ts Pr♦♠♦❝✐♦♥❛❧ ④

     ♣r✐✈❛t❡ ❜♦♦❧❡❛♥ ❥❛❚❡✈❡❉❡s❝♦♥t♦ ❂ ❢❛❧s❡❀
     ✴✴ ♣❛rt❡ ❞♦ ❝ó❞✐❣♦ ♦♠✐t✐❞♦

     ♣✉❜❧✐❝ ❜♦♦❧❡❛♥ ❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭❞♦✉❜❧❡ ♣♦r❝❡♥t❛❣❡♠✮ ④
         ✐❢ ✭❥❛❚❡✈❡❉❡s❝♦♥t♦✮ ④
             r❡t✉r♥ ❢❛❧s❡❀
         ⑥
         ❥❛❚❡✈❡❉❡s❝♦♥t♦ ❂ tr✉❡❀
         ✴✴ r❡st❛♥t❡ ❞♦ ❝ó❞✐❣♦ ❞♦ ♠ét♦❞♦
     ⑥
⑥

    Grande parte do código está omitido, mas só precisamos focar nessa
parte. Essa classe possui um método chamado aplicaDescontoDe, que
da forma que está só aplica o desconto uma única vez por instância. Temos
um atributo boolean para nos ajudar, o jaTeveDesconto. O código é bem
simples e tudo parece certo. De certa maneira está, o problema só vai aparecer
quando duas ou mais Thread concorrerem pelo acesso desse método.
    Imagine que queremos fazer um processamento em massa, em todos os
nossos livros, chamando o método aplicaDescontoDe. Esse processa-
mento será executado em paralelo, com diversas Threads. O que acontece
se duas Threads passarem “ao mesmo tempo” pelo if que valida se ele já
teve desconto?
    Isso pode resultar em um desastre. Como a primeira Thread pode
ainda não ter chegado à linha que atribui true ao valor do atributo
jaTeveDesconto, as duas vão passar pelo if. Em outras palavras, vamos
aplicar o desconto duas vezes para o mesmo objeto.

                                                                                 99


[PAGINA 110]
5.6. Um pouco mais sobre as Threads                           Casa do Código


    Claro, esse é um exemplo bem simples e o problema não aconteceria sem-
pre. Esse código poderia ser executado por um mês sem nunca acontecer uma
acesso concorrente, até que um belo dia o scheduler de threads passasse duas
para o mesmo objeto.
    Como impedir isso? O Java nos oferece um recurso interessante, um meio
de garantir que apenas uma Thread acessará determinado bloco ou método.
Se outra Thread chegar, ela vai precisar esperar a primeira terminar todo o
trabalho para depois começar o seu. O acesso é sincronizado.

♣✉❜❧✐❝ ❝❧❛ss ▲✐✈r♦❋✐s✐❝♦ ❡①t❡♥❞s ▲✐✈r♦
        ✐♠♣❧❡♠❡♥ts Pr♦♠♦❝✐♦♥❛❧ ④

      ♣r✐✈❛t❡ ❜♦♦❧❡❛♥ ❥❛❚❡✈❡❉❡s❝♦♥t♦ ❂ ❢❛❧s❡❀
      ✴✴ ♣❛rt❡ ❞♦ ❝ó❞✐❣♦ ♦♠✐t✐❞♦

      ♣✉❜❧✐❝ s②♥❝❤r♦♥✐③❡❞ ❜♦♦❧❡❛♥
      ❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭❞♦✉❜❧❡ ♣♦r❝❡♥t❛❣❡♠✮ ④
          ✐❢ ✭❥❛❚❡✈❡❉❡s❝♦♥t♦✮ ④
              r❡t✉r♥ ❢❛❧s❡❀
          ⑥
          ❥❛❚❡✈❡❉❡s❝♦♥t♦ ❂ tr✉❡❀
          ✴✴ r❡st❛♥t❡ ❞♦ ❝ó❞✐❣♦ ❞♦ ♠ét♦❞♦
      ⑥
⑥

     Note no uso da palavra chave synchronized. É ela quem dá essa carac-
terística ao método aplicaDescontoDe. Com isso, já estamos prevenindo
acesso concorrente a essa lógica, garantimos que não existirá concorrência
nela. Normalmente chamamos de thread safe uma classe que está protegida
contra acesso concorrente.




100


[PAGINA 111]
Casa do Código                                    Capítulo 5. Threads e Paralelismo




  Bloco sincronizado

     Utilizando o modificador synchronized em um método, estamos
  dizendo que todo o código daquele método é sincronizado. Faz sentido.
  Mas como dizer que apenas um bloco de código deve ser sincronizado?
     Há uma outra forma de utilizar o synchronized, definindo um
  bloco de código que recebe qual é o objeto que será bloqueado:

  ♣✉❜❧✐❝ ❜♦♦❧❡❛♥ ❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭❞♦✉❜❧❡ ♣♦r❝❡♥t❛❣❡♠✮ ④
      s②♥❝❤r♦♥✐③❡❞ ✭t❤✐s✮ ④
          ✐❢ ✭❥❛❚❡✈❡❉❡s❝♦♥t♦✮ ④
              r❡t✉r♥ ❢❛❧s❡❀
          ⑥
      ⑥
      ❥❛❚❡✈❡❉❡s❝♦♥t♦ ❂ tr✉❡❀
      ✴✴ r❡st❛♥t❡ ❞♦ ❝ó❞✐❣♦ ❞♦ ♠ét♦❞♦
  ⑥

     Agora apenas o if está no bloco do synchronized, no lugar de
  todo o método.


5.7 Garbage Collector
Não podemos falar de threads sem comentar sobre uma Thread bastante
conhecida em Java, responsável por jogar fora os objetos que não estão mais
sendo referenciados em nosso código. Estamos falando do famoso Garbage
Collector (coletor de lixo).
    Já não é uma novidade que quando criamos um novo objeto, suas infor-
mações serão mantidas em memória. Atribuímos esse objeto do tipo Autor,
por exemplo, a uma variável para futuramente termos uma forma de nos ref-
erenciarmos a ele:

❆✉t♦r ❛✉t♦r ❂ ♥❡✇ ❆✉t♦r✭✮❀




                                                                              101


[PAGINA 112]
5.7. Garbage Collector                                           Casa do Código




           Fig. 5.2: Variável autor referenciando o objeto em memória.



    Mas o que acontece com o objeto em memória quando deixamos de nos
referenciar a ele? Por exemplo, ao atribuir um novo autor para essa variável:

❆✉t♦r ❛✉t♦r ❂ ♥❡✇ ❆✉t♦r✭✮❀
❆✉t♦r ♦✉tr♦ ❂ ♥❡✇ ❆✉t♦r✭✮❀
❛✉t♦r ❂ ♦✉tr♦❀




              Fig. 5.3: Duas variáveis referenciando o mesmo objeto.



    A partir desse momento, ninguém mais está referenciando esse objeto, di-
reta ou indiretamente. Isso significa que ele não existe mais em memória? Não
necessariamente. Significa com toda a certeza que ele não está mais acessível,
mas não que ele foi removido da memória.
    Vale lembrar que quem cuida desse trabalho é o Garbage Collector
(GC), que é uma Thread. Mas quando ela é executada? A todo mo-
mento? Provavelmente não, isso teria um custo bem grande e totalmente


102


[PAGINA 113]
Casa do Código                                       Capítulo 5. Threads e Paralelismo



desnecessário. Ela é executada de forma estratégica, quando for preciso e con-
veniente para a JVM, podendo depender de uma implementação para outra.
    Não há uma forma de obrigar a thread do Garbage Collector a ser execu-
tada. A classe System até possui um método estático chamado gc, mas não
se engane, chamá-lo não significa que o GC será executado. Isso apenas sug-
ere para a JVM que rode o GC, ela pode ou não aceitar. O uso desse método
normalmente é desencorajado, são pouquíssimas as situações em que usá-lo
fará alguma diferença em sua aplicação, o ideal é não depender disso.


5.8 Java FX assíncrono
Agora que já conhecemos um pouco mais sobre a API de Threads do Java,
podemos voltar ao nosso código. Resolvemos o problema de a ação demorada
travar a aplicação, mas não estamos dando uma resposta muito adequada para
o cliente que pediu a lista como um CSV. Ele clica não botão, olha no diretório
e o arquivo produtos.csv ainda não está lá. Só depois de alguns segundos
o arquivo é gerado.
     Para melhorar isso, podemos mostrar uma mensagem indicando que o
arquivo está sendo exportado e logo em seguida atualizá-la para indicar que
o trabalho foi concluído.
     Vamos começar criando uma Label chamada progresso, para
mostrar este texto.

▲❛❜❡❧ ♣r♦❣r❡ss♦ ❂ ♥❡✇ ▲❛❜❡❧✭✮❀

    Note que não atribuímos um texto inicial para ela, seu texto será adi-
cionado e atualizado dinamicamente pela ação de exportar produtos.
    Lembre-se de que, para deixá-la visível, precisamos adicioná-la ao group
de elementos dessa tela:

❣r♦✉♣✳❣❡t❈❤✐❧❞r❡♥✭✮✳❛❞❞❆❧❧✭
    ❧❛❜❡❧✱ ✈❜♦①✱ ❜✉tt♦♥✱ ♣r♦❣r❡ss♦✮❀

    Ótimo, agora podemos tentar adicionar e atualizar seu texto dentro da
Thread que acontece no setOnAction do botão de exportar. Uma possi-
bilidade seria:

                                                                                 103


[PAGINA 114]
5.9. Trabalhando com a classe Task                          Casa do Código


❜✉tt♦♥✳s❡t❖♥❆❝t✐♦♥✭❡✈❡♥t ✲❃ ④
    ♥❡✇ ❚❤r❡❛❞✭✭✮ ✲❃ ④
        ♣r♦❣r❡ss♦✳s❡t❚❡①t✭✧❊①♣♦rt❛♥❞♦✳✳✳✧✮❀
        ❞♦r♠❡P♦r❱✐♥t❡❙❡❣✉♥❞♦s✭✮❀
        ❡①♣♦rt❛❊♠❈❙❱✭♣r♦❞✉t♦s✮❀
        ♣r♦❣r❡ss♦✳s❡t❚❡①t✭✧❈♦♥❝❧✉í❞♦✦✧✮❀
    ⑥✮✳st❛rt✭✮❀
⑥✮❀

    Com isso, queremos que, ao iniciar, nossa Thread adicione o texto
Exportando... no Label, que chamamos de progresso. Quando con-
cluir, mude seu texto para Concluído!. Parece fazer sentido, não acha? Mas
ao executar:

❊①❝❡♣t✐♦♥ ✐♥ t❤r❡❛❞ ✧❚❤r❡❛❞✲✺✧
    ❥❛✈❛✳❧❛♥❣✳■❧❧❡❣❛❧❙t❛t❡❊①❝❡♣t✐♦♥✿
    ◆♦t ♦♥ ❋❳ ❛♣♣❧✐❝❛t✐♦♥ t❤r❡❛❞❀

    Isso aconteceu porque não podemos adicionar ou atualizar o texto de um
elemento do Java FX em uma Thread que não seja do Java FX, ou sua própria
Thread principal.


5.9 Trabalhando com a classe Task
Para nos ajudar nesse trabalho, o Java FX oferece uma classe chamada Task.
Essa classe é bem útil quando estamos trabalhando de forma assíncrona,
como já veremos em prática. Ela tem um único método abstrato, chamado
call.
    Comumente instanciamos uma Task utilizando classes anônimas:

❚❛s❦❁❱♦✐❞❃ t❛s❦ ❂ ♥❡✇ ❚❛s❦❁❱♦✐❞❃✭✮ ④
    ❅❖✈❡rr✐❞❡
    ♣r♦t❡❝t❡❞ ❱♦✐❞ ❝❛❧❧✭✮ t❤r♦✇s ❊①❝❡♣t✐♦♥ ④
        ✴✴ ❛❧❣✉♠ tr❛❜❛❧❤♦
        r❡t✉r♥ ♥✉❧❧❀
    ⑥
⑥❀


104


[PAGINA 115]
Casa do Código                                   Capítulo 5. Threads e Paralelismo




  Pergunta: por que não um lambda?

     Talvez você se pergunte por que criamos a Task usando uma classe
  anônima e não com uma expressão lambda? Porque funciona com o
  Runnable, mas não com a Task. Não vou falar a resposta agora, tente
  descobrir. Ok? Não se preocupe, em breve eu lhe conto.


    A Task pode ter um retorno, mas note que, como não queremos retornar
nada, utilizamos o tipo Void (classe wrapper do já tão conhecido void).
    Vamos modificar nosso código para que, no lugar de executar o método
de dormir por 20 segundos e exportar dentro de um Runnable, ela faça isso
dentro da Task.
    No lugar de fazer:

❜✉tt♦♥✳s❡t❖♥❆❝t✐♦♥✭❡✈❡♥t ✲❃ ④
    ♥❡✇ ❚❤r❡❛❞✭✭✮ ✲❃ ④
        ❞♦r♠❡P♦r❱✐♥t❡❙❡❣✉♥❞♦s✭✮❀
        ❡①♣♦rt❛❊♠❈❙❱✭♣r♦❞✉t♦s✮❀
    ⑥✮✳st❛rt✭✮❀
⑥✮❀

    Vamos quebrar esse trabalho em duas partes, primeiro criando uma in-
stância de Task cujo método call fará esse trabalho. Ela deve ficar dentro
do setOnAction, no botão de exportar:

❜✉tt♦♥✳s❡t❖♥❆❝t✐♦♥✭❡✈❡♥t ✲❃ ④

      ❚❛s❦❁❱♦✐❞❃ t❛s❦ ❂ ♥❡✇ ❚❛s❦❁❱♦✐❞❃✭✮ ④
          ❅❖✈❡rr✐❞❡
          ♣r♦t❡❝t❡❞ ❱♦✐❞ ❝❛❧❧✭✮ t❤r♦✇s ❊①❝❡♣t✐♦♥ ④
              ❞♦r♠❡P♦r❱✐♥t❡❙❡❣✉♥❞♦s✭✮❀
              ❡①♣♦rt❛❊♠❈❙❱✭♣r♦❞✉t♦s✮❀
              r❡t✉r♥ ♥✉❧❧❀
          ⑥
      ⑥❀

⑥✮❀

                                                                             105


[PAGINA 116]
5.9. Trabalhando com a classe Task                            Casa do Código


   Agora, ainda dentro do setOnAction, vamos criar e iniciar uma nova
Thread passando essa Task como argumento.

❜✉tt♦♥✳s❡t❖♥❆❝t✐♦♥✭❡✈❡♥t ✲❃ ④

      ❚❛s❦❁❱♦✐❞❃ t❛s❦ ❂ ♥❡✇ ❚❛s❦❁❱♦✐❞❃✭✮ ④
          ❅❖✈❡rr✐❞❡
          ♣r♦t❡❝t❡❞ ❱♦✐❞ ❝❛❧❧✭✮ t❤r♦✇s ❊①❝❡♣t✐♦♥ ④
              ❞♦r♠❡P♦r❱✐♥t❡❙❡❣✉♥❞♦s✭✮❀
              ❡①♣♦rt❛❊♠❈❙❱✭♣r♦❞✉t♦s✮❀
              r❡t✉r♥ ♥✉❧❧❀
          ⑥
      ⑥❀

      ♥❡✇ ❚❤r❡❛❞✭t❛s❦✮✳st❛rt✭✮❀
⑥✮❀

      O trecho de código do botão de exportar ficará assim:

❇✉tt♦♥ ❜✉tt♦♥ ❂ ♥❡✇ ❇✉tt♦♥✭✧❊①♣♦rt❛r ❈❙❱✧✮❀

▲❛❜❡❧ ♣r♦❣r❡ss♦ ❂ ♥❡✇ ▲❛❜❡❧✭✮❀

❜✉tt♦♥✳s❡t❖♥❆❝t✐♦♥✭❡✈❡♥t ✲❃ ④

      ❚❛s❦❁❱♦✐❞❃ t❛s❦ ❂ ♥❡✇ ❚❛s❦❁❱♦✐❞❃✭✮ ④
          ❅❖✈❡rr✐❞❡
          ♣r♦t❡❝t❡❞ ❱♦✐❞ ❝❛❧❧✭✮ t❤r♦✇s ❊①❝❡♣t✐♦♥ ④
              ❞♦r♠❡P♦r❱✐♥t❡❙❡❣✉♥❞♦s✭✮❀
              ❡①♣♦rt❛❊♠❈❙❱✭♣r♦❞✉t♦s✮❀
              r❡t✉r♥ ♥✉❧❧❀
          ⑥
      ⑥❀

      ♥❡✇ ❚❤r❡❛❞✭t❛s❦✮✳st❛rt✭✮❀
⑥✮❀

   Podemos executar nossa aplicação para confirmar que tudo está funcio-
nando.


106


[PAGINA 117]
Casa do Código                                   Capítulo 5. Threads e Paralelismo




  Resposta: por que não um lambda?

     Você provavelmente já descobriu o motivo, mas não podemos imple-
  mentar a Task como um lambda porque ela não é uma interface fun-
  cional. Ela não é nem mesmo uma interface: se você olhar seu código
  perceberá que se trata de uma classe anônima. Nós só podemos usar a
  sintaxe do lambda com interfaces funcionais, sem exceções.


Mas e quanto ao texto da Label?
    Mudamos para Task e tudo continua funcionando, mas e quanto ao texto
da Label de progresso? O problema ainda não foi resolvido.
    Agora que estamos usando a API do Java FX para executar código assín-
crono, podemos tirar bastante proveito de alguns recursos. Por exemplo, há
um método chamado setOnRunning em Task que nos permite executar
um evento quando a task está prestes a ser executada.

t❛s❦✳s❡t❖♥❘✉♥♥✐♥❣✭♥❡✇ ❊✈❡♥t❍❛♥❞❧❡r❁❲♦r❦❡r❙t❛t❡❊✈❡♥t❃✭✮ ④
    ❅❖✈❡rr✐❞❡
    ♣✉❜❧✐❝ ✈♦✐❞ ❤❛♥❞❧❡✭❲♦r❦❡r❙t❛t❡❊✈❡♥t ❡✮ ④
        ✴✴ ❛❧❣✉♠❛ ❛çã♦ ❛q✉✐
    ⑥
⑥✮❀

    O EventHandler sim é uma interface funcional, portanto, podemos
tirar proveito do lambda. O código fica assim:

t❛s❦✳s❡t❖♥❘✉♥♥✐♥❣✭ ❡ ✲❃ ④
    ✴✴ ❛❧❣✉♠❛ ❛çã♦ ❛q✉✐
⑥✮❀

   Nesse momento, podemos atualizar o texto da Label, dizendo que o
produto está sendo exportado:

t❛s❦✳s❡t❖♥❘✉♥♥✐♥❣✭❡ ✲❃ ④
    ♣r♦❣r❡ss♦✳s❡t❚❡①t✭✧❡①♣♦rt❛♥❞♦✳✳✳✧✮❀
⑥✮❀

                                                                             107


[PAGINA 118]
5.9. Trabalhando com a classe Task                         Casa do Código


    Como é uma única expressão, não precisamos das chaves nem do ponto
e vírgula:

t❛s❦✳s❡t❖♥❘✉♥♥✐♥❣✭❡ ✲❃ ♣r♦❣r❡ss♦✳s❡t❚❡①t✭✧❡①♣♦rt❛♥❞♦✳✳✳✧✮✮❀

      O código do evento de setOnAction ficará assim:

❜✉tt♦♥✳s❡t❖♥❆❝t✐♦♥✭❡✈❡♥t ✲❃ ④

      ❚❛s❦❁❱♦✐❞❃ t❛s❦ ❂ ♥❡✇ ❚❛s❦❁❱♦✐❞❃✭✮ ④
          ❅❖✈❡rr✐❞❡
          ♣r♦t❡❝t❡❞ ❱♦✐❞ ❝❛❧❧✭✮ t❤r♦✇s ❊①❝❡♣t✐♦♥ ④
              ❞♦r♠❡P♦r❱✐♥t❡❙❡❣✉♥❞♦s✭✮❀
              ❡①♣♦rt❛❊♠❈❙❱✭♣r♦❞✉t♦s✮❀
              r❡t✉r♥ ♥✉❧❧❀
          ⑥
      ⑥❀

      t❛s❦✳s❡t❖♥❘✉♥♥✐♥❣✭❡ ✲❃ ♣r♦❣r❡ss♦✳s❡t❚❡①t✭✧❡①♣♦rt❛♥❞♦✳✳✳✧✮✮❀

      ♥❡✇ ❚❤r❡❛❞✭t❛s❦✮✳st❛rt✭✮❀
⑥✮❀

   Vamos testar. Após modificar o código, podemos executá-lo e ao clicar
em exportar o resultado será o esperado:




108


[PAGINA 119]
Casa do Código                                        Capítulo 5. Threads e Paralelismo




             Fig. 5.4: Texto ‘exportando...’ sendo exibido na tela.



    O texto está desalinhado, claro. Mas logo cuidaremos disso. Ainda pre-
cisamos fazer com que esse texto seja atualizado no momento em que a Task
seja concluída. Podemos fazer isso utilizando um outro método de callback,
o setOnSucceeded.
    Ele também recebe um EventHandler como parâmetro, portanto, va-
mos de lambda:

t❛s❦✳s❡t❖♥❙✉❝❝❡❡❞❡❞✭❡ ✲❃ ④
    ♣r♦❣r❡ss♦✳s❡t❚❡①t✭✧❝♦♥❝❧✉í❞♦✦✧✮❀
⑥✮❀

    Agora nosso código está assim:

❜✉tt♦♥✳s❡t❖♥❆❝t✐♦♥✭❡✈❡♥t ✲❃ ④

     ❚❛s❦❁❱♦✐❞❃ t❛s❦ ❂ ♥❡✇ ❚❛s❦❁❱♦✐❞❃✭✮ ④
         ❅❖✈❡rr✐❞❡
         ♣r♦t❡❝t❡❞ ❱♦✐❞ ❝❛❧❧✭✮ t❤r♦✇s ❊①❝❡♣t✐♦♥ ④
             ❞♦r♠❡P♦r❱✐♥t❡❙❡❣✉♥❞♦s✭✮❀
             ❡①♣♦rt❛❊♠❈❙❱✭♣r♦❞✉t♦s✮❀
             r❡t✉r♥ ♥✉❧❧❀
         ⑥
     ⑥❀

                                                                                  109


[PAGINA 120]
5.9. Trabalhando com a classe Task                           Casa do Código




      t❛s❦✳s❡t❖♥❘✉♥♥✐♥❣✭❡ ✲❃ ♣r♦❣r❡ss♦✳s❡t❚❡①t✭✧❡①♣♦rt❛♥❞♦✳✳✳✧✮✮❀

      t❛s❦✳s❡t❖♥❙✉❝❝❡❡❞❡❞✭❡ ✲❃ ♣r♦❣r❡ss♦✳s❡t❚❡①t✭✧❝♦♥❝❧✉í❞♦✦✧✮✮❀

      ♥❡✇ ❚❤r❡❛❞✭t❛s❦✮✳st❛rt✭✮❀
⑥✮❀


  Outros métodos interessantes

     Além do setOnRunning e setOnSucceeded, que acabamos de
  conhecer, a classe Task tem outros métodos de callback que podem ser
  muito úteis em seu dia a dia. São eles:

        • setOnCancelled

        • setOnFailed

        • setOnScheduled

      Não deixe de conferir a documentação da classe Task para saber
   mais detalhes desses e outros métodos. Além de pesquisar, tente testar
   alguns deles em seu projeto.
      https://docs.oracle.com/javafx/2/api/javafx/concurrent/Task.html


    Pronto, vamos ver o resultado. Ao clicar em Exportar CSV a men-
sagem exportando... é exibida. Alguns segundos depois, o texto é atual-
izado para concluído!. Sucesso.




110


[PAGINA 121]
Casa do Código                                        Capítulo 5. Threads e Paralelismo




                 Fig. 5.5: Texto concluído sendo exibido na tela.



   Por fim, podemos alinhar essas mensagens. Faremos isso da mesma
forma como foi feito no button:

▲❛❜❡❧ ♣r♦❣r❡ss♦ ❂ ♥❡✇ ▲❛❜❡❧✭✮❀
♣r♦❣r❡ss♦✳s❡t▲❛②♦✉t❳✭✹✽✺✮❀
♣r♦❣r❡ss♦✳s❡t▲❛②♦✉t❨✭✸✵✮❀

    Ao executar a aplicação, clincando em Exportar CSV teremos:




                                                                                   111


[PAGINA 122]
5.10. Código final com e sem lambdas                        Casa do Código


      Após alguns segundos...




   Perfeito. Vimos que trabalhar com Threads não é fácil, mas também não
é um bicho de sete cabeças. Temos que tomar alguns cuidados extras, claro.
Em Java FX, a classe Task ajuda bastante nesse trabalho. Ela oferece uma
forma flexível e desacoplada de encapsular e executar código paralelo.


5.10      Código final com e sem lambdas
Nosso código final, com Java 8, ficou assim:

❅❙✉♣♣r❡ss❲❛r♥✐♥❣s✭④ ✧✉♥❝❤❡❝❦❡❞✧✱ ✧r❛✇t②♣❡s✧ ⑥✮
♣✉❜❧✐❝ ❝❧❛ss ▼❛✐♥ ❡①t❡♥❞s ❆♣♣❧✐❝❛t✐♦♥ ④

      ❅❖✈❡rr✐❞❡
      ♣✉❜❧✐❝ ✈♦✐❞ st❛rt✭❙t❛❣❡ ♣r✐♠❛r②❙t❛❣❡✮ ④

            ●r♦✉♣ ❣r♦✉♣ ❂ ♥❡✇ ●r♦✉♣✭✮❀
            ❙❝❡♥❡ s❝❡♥❡ ❂ ♥❡✇ ❙❝❡♥❡✭❣r♦✉♣✱ ✻✾✵✱ ✺✶✵✮❀

            ❖❜s❡r✈❛❜❧❡▲✐st❁Pr♦❞✉t♦❃ ♣r♦❞✉t♦s ❂
                ♥❡✇ Pr♦❞✉t♦❉❆❖✭✮✳❧✐st❛✭✮❀

            ❚❛❜❧❡❱✐❡✇❁Pr♦❞✉t♦❃ t❛❜❧❡❱✐❡✇ ❂

112


[PAGINA 123]
Casa do Código                                Capítulo 5. Threads e Paralelismo



                 ♥❡✇ ❚❛❜❧❡❱✐❡✇❁❃✭♣r♦❞✉t♦s✮❀

          ❚❛❜❧❡❈♦❧✉♠♥ ♥♦♠❡❈♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭✧◆♦♠❡✧✮❀
          ♥♦♠❡❈♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭✶✽✵✮❀
          ♥♦♠❡❈♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
              ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②✭✧♥♦♠❡✧✮✮❀

          ❚❛❜❧❡❈♦❧✉♠♥ ❞❡s❝❈♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭✧❉❡s❝r✐çã♦✧✮❀
          ❞❡s❝❈♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭✷✸✵✮❀
          ❞❡s❝❈♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
              ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②✭✧❞❡s❝r✐❝❛♦✧✮✮❀

          ❚❛❜❧❡❈♦❧✉♠♥ ✈❛❧♦r❈♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭✧❱❛❧♦r✧✮❀
          ✈❛❧♦r❈♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭✻✵✮❀
          ✈❛❧♦r❈♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
              ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②✭✧✈❛❧♦r✧✮✮❀

          ❚❛❜❧❡❈♦❧✉♠♥ ✐s❜♥❈♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭✧■❙❇◆✧✮❀
          ✐s❜♥❈♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭✶✽✵✮❀
          ✐s❜♥❈♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
              ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②✭✧✐s❜♥✧✮✮❀

          t❛❜❧❡❱✐❡✇✳❣❡t❈♦❧✉♠♥s✭✮✳❛❞❞❆❧❧✭♥♦♠❡❈♦❧✉♠♥✱ ❞❡s❝❈♦❧✉♠♥✱
              ✈❛❧♦r❈♦❧✉♠♥✱ ✐s❜♥❈♦❧✉♠♥✮❀

          ❢✐♥❛❧ ❱❇♦① ✈❜♦① ❂ ♥❡✇ ❱❇♦①✭t❛❜❧❡❱✐❡✇✮❀
          ✈❜♦①✳s❡tP❛❞❞✐♥❣✭♥❡✇ ■♥s❡ts✭✼✵✱ ✵✱ ✵ ✱✶✵✮✮❀

          ▲❛❜❡❧ ❧❛❜❡❧ ❂ ♥❡✇ ▲❛❜❡❧✭✧▲✐st❛❣❡♠ ❞❡ ▲✐✈r♦s✧✮❀

          ❧❛❜❡❧✳s❡t❋♦♥t✭❋♦♥t
              ✳❢♦♥t✭✧▲✉❝✐❞❛ ●r❛♥❞❡✧✱ ❋♦♥tP♦st✉r❡✳❘❊●❯▲❆❘✱ ✸✵✮✮❀

          ❧❛❜❡❧✳s❡tP❛❞❞✐♥❣✭♥❡✇ ■♥s❡ts✭✷✵✱ ✵✱ ✶✵✱ ✶✵✮✮❀

          ▲❛❜❡❧ ♣r♦❣r❡ss♦ ❂ ♥❡✇ ▲❛❜❡❧✭✮❀
          ♣r♦❣r❡ss♦✳s❡t▲❛②♦✉t❳✭✹✽✺✮❀
          ♣r♦❣r❡ss♦✳s❡t▲❛②♦✉t❨✭✸✵✮❀



                                                                           113


[PAGINA 124]
5.10. Código final com e sem lambdas                      Casa do Código


            ❇✉tt♦♥ ❜✉tt♦♥ ❂ ♥❡✇ ❇✉tt♦♥✭✧❊①♣♦rt❛r ❈❙❱✧✮❀
            ❜✉tt♦♥✳s❡t▲❛②♦✉t❳✭✺✼✺✮❀
            ❜✉tt♦♥✳s❡t▲❛②♦✉t❨✭✷✺✮❀

            ❜✉tt♦♥✳s❡t❖♥❆❝t✐♦♥✭❡✈❡♥t ✲❃ ④

                  ❚❛s❦❁❱♦✐❞❃ t❛s❦ ❂ ♥❡✇ ❚❛s❦❁❱♦✐❞❃✭✮ ④
                      ❅❖✈❡rr✐❞❡
                      ♣r♦t❡❝t❡❞ ❱♦✐❞ ❝❛❧❧✭✮ t❤r♦✇s ❊①❝❡♣t✐♦♥ ④
                          ❞♦r♠❡P♦r❱✐♥t❡❙❡❣✉♥❞♦s✭✮❀
                          ❡①♣♦rt❛❊♠❈❙❱✭♣r♦❞✉t♦s✮❀
                          r❡t✉r♥ ♥✉❧❧❀
                      ⑥
                  ⑥❀

                  t❛s❦✳s❡t❖♥❘✉♥♥✐♥❣✭
                      ❡ ✲❃ ♣r♦❣r❡ss♦✳s❡t❚❡①t✭✧❡①♣♦rt❛♥❞♦✳✳✳✧✮✮❀

                  t❛s❦✳s❡t❖♥❙✉❝❝❡❡❞❡❞✭
                      ❡ ✲❃ ♣r♦❣r❡ss♦✳s❡t❚❡①t✭✧❝♦♥❝❧✉í❞♦✦✧✮✮❀

                  ♥❡✇ ❚❤r❡❛❞✭t❛s❦✮✳st❛rt✭✮❀
            ⑥✮❀

            ❣r♦✉♣✳❣❡t❈❤✐❧❞r❡♥✭✮✳❛❞❞❆❧❧✭❧❛❜❡❧✱ ✈❜♦①✱ ❜✉tt♦♥✱
                                       ♣r♦❣r❡ss♦✮❀

            ♣r✐♠❛r②❙t❛❣❡✳s❡t❚✐t❧❡✭
                ✧❙✐st❡♠❛ ❞❛ ❧✐✈r❛r✐❛ ❝♦♠ ❏❛✈❛ ❋❳✧✮❀
            ♣r✐♠❛r②❙t❛❣❡✳s❡t❙❝❡♥❡✭s❝❡♥❡✮❀
            ♣r✐♠❛r②❙t❛❣❡✳s❤♦✇✭✮❀
      ⑥

      ♣r✐✈❛t❡ ✈♦✐❞ ❡①♣♦rt❛❊♠❈❙❱✭❖❜s❡r✈❛❜❧❡▲✐st❁Pr♦❞✉t♦❃ ♣r♦❞✉t♦s✮④
          tr② ④
              ♥❡✇ ❊①♣♦rt❛❞♦r✭✮✳♣❛r❛❈❙❱✭♣r♦❞✉t♦s✮❀
          ⑥ ❝❛t❝❤ ✭■❖❊①❝❡♣t✐♦♥ ❡✮ ④
              ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❊rr♦ ❛♦ ❡①♣♦rt❛r✿ ✧✰ ❡✮❀
          ⑥

114


[PAGINA 125]
Casa do Código                                Capítulo 5. Threads e Paralelismo



     ⑥

     ♣r✐✈❛t❡ ✈♦✐❞ ❞♦r♠❡P♦r❱✐♥t❡❙❡❣✉♥❞♦s✭✮ ④
         tr② ④
             ❚❤r❡❛❞✳s❧❡❡♣✭✷✵✵✵✵✮❀
         ⑥ ❝❛t❝❤ ✭■♥t❡rr✉♣t❡❞❊①❝❡♣t✐♦♥ ❡✮ ④
             ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❖♣s✱ ♦❝♦rr❡✉ ✉♠ ❡rr♦✿ ✧✰ ❡✮❀
         ⑥
     ⑥

     ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④
         ❧❛✉♥❝❤✭❛r❣s✮❀
     ⑥
⑥

    Conforme prometido, a parte que muda do setOnAction em Java 7:
❜✉tt♦♥✳s❡t❖♥❆❝t✐♦♥✭♥❡✇ ❊✈❡♥t❍❛♥❞❧❡r❁❆❝t✐♦♥❊✈❡♥t❃✭✮ ④
    ❅❖✈❡rr✐❞❡
    ♣✉❜❧✐❝ ✈♦✐❞ ❤❛♥❞❧❡✭❆❝t✐♦♥❊✈❡♥t ❡✈❡♥t✮ ④

          ❚❛s❦❁❱♦✐❞❃ t❛s❦ ❂ ♥❡✇ ❚❛s❦❁❱♦✐❞❃✭✮ ④
              ❅❖✈❡rr✐❞❡
              ♣r♦t❡❝t❡❞ ❱♦✐❞ ❝❛❧❧✭✮ t❤r♦✇s ❊①❝❡♣t✐♦♥ ④
                  ❞♦r♠❡P♦r❱✐♥t❡❙❡❣✉♥❞♦s✭✮❀
                  ❡①♣♦rt❛❊♠❈❙❱✭♣r♦❞✉t♦s✮❀
                  r❡t✉r♥ ♥✉❧❧❀
              ⑥
          ⑥❀

          t❛s❦✳s❡t❖♥❘✉♥♥✐♥❣✭♥❡✇ ❊✈❡♥t❍❛♥❞❧❡r❁❲♦r❦❡r❙t❛t❡❊✈❡♥t❃✭✮ ④
              ❅❖✈❡rr✐❞❡
              ♣✉❜❧✐❝ ✈♦✐❞ ❤❛♥❞❧❡✭❲♦r❦❡r❙t❛t❡❊✈❡♥t ❡✮ ④
                  ♣r♦❣r❡ss♦✳s❡t❚❡①t✭✧❡①♣♦rt❛♥❞♦✳✳✳✧✮❀
              ⑥
          ⑥✮❀

          t❛s❦✳s❡t❖♥❙✉❝❝❡❡❞❡❞✭
          ♥❡✇ ❊✈❡♥t❍❛♥❞❧❡r❁❲♦r❦❡r❙t❛t❡❊✈❡♥t❃✭✮ ④
              ❅❖✈❡rr✐❞❡

                                                                           115


[PAGINA 126]
5.10. Código final com e sem lambdas                           Casa do Código


                  ♣✉❜❧✐❝ ✈♦✐❞ ❤❛♥❞❧❡✭❲♦r❦❡r❙t❛t❡❊✈❡♥t ❡✮ ④
                      ♣r♦❣r❡ss♦✳s❡t❚❡①t✭✧❝♦♥❝❧✉í❞♦✦✧✮❀
                  ⑥
            ⑥✮❀

            ♥❡✇ ❚❤r❡❛❞✭t❛s❦✮✳st❛rt✭✮❀
      ⑥
⑥✮❀

    Curiosamente, o Eclipse nos oferece uma forma bem simples de converter
classes anônimas para expressões lambda e vice-versa. Basta você selecionar
o código e utilizar o atalho Control + 1. Quando temos um lambda, a
opção Convert to anonymous classe creation estará disponível.




          Fig. 5.8: Convertendo lambda para classe anônima no Eclipse.



   O mesmo vale para o caminho contrário, quando temos uma classe anôn-
ima e queremos transformar em uma expressão lambda, mas nesse caso a
opção será Convert to lambda expression. Esses recursos da IDE nos ajudam
muito, migrar classes anônimas para lambdas nunca foi tão divertido!




116


[PAGINA 127]
Capítulo 6

CSS no Java FX
Nossa aplicação está cada vez mais completa, mas antes de continuar veremos
como melhorar ainda mais não só a aparência de nossa listagem de produtos,
mas também a qualidade e manutenibilidade de nosso código.
    Se você perceber, o estilo padrão do Java FX já é bastante atraente. Sem
adicionar cores ou configurar nada, nossa aplicação já está com uma aparên-
cia bem aceitável. Repare em detalhes como a borda e a linha selecionada na
tabela de produtos. Ao passar o mouse sob o botão Exportar CSV, você
também pode perceber que sua cor ficará mais suave.
    Mas ao utilizar estilos personalizados do Java FX vamos além da aparên-
cia. Você perceberá ao longo do capítulo que isso possibilita deixar nosso
código ainda mais limpo, enxuto e fácil de manter. Vamos começar?


[PAGINA 128]
6.1. Seu primeiro CSS no Java FX                                Casa do Código


6.1      Seu primeiro CSS no Java FX
Antes de sair aplicando novos estilos em nosso código, vamos olhar mais de
perto a forma como fizemos até agora. Repare como fizemos para person-
alizar a fonte e adicionar um padding em nossa Label, por exemplo.

▲❛❜❡❧ ❧❛❜❡❧ ❂ ♥❡✇ ▲❛❜❡❧✭✧▲✐st❛❣❡♠ ❞❡ ▲✐✈r♦s✧✮❀
❧❛❜❡❧✳s❡t❋♦♥t✭❋♦♥t✳❢♦♥t✭
    ✧▲✉❝✐❞❛ ●r❛♥❞❡✧✱ ❋♦♥tP♦st✉r❡✳❘❊●❯▲❆❘✱ ✸✵✮✮❀
❧❛❜❡❧✳s❡tP❛❞❞✐♥❣✭♥❡✇ ■♥s❡ts✭✷✵✱ ✵✱ ✶✵✱ ✶✵✮✮❀

    Isso funciona muito bem, mas adiciona uma certa verbosidade a nosso
código. O que realmente importa aqui é a primeira linha, onde criamos a
Label. Queremos um código limpo e simples de entender, pois, quanto mais
próximo disso nosso código for, melhor será sua manutenibilidade. Repare
no que acontece se tirarmos o estilo desse código:

▲❛❜❡❧ ❧❛❜❡❧ ❂ ♥❡✇ ▲❛❜❡❧✭✧▲✐st❛❣❡♠ ❞❡ ▲✐✈r♦s✧✮❀

      Ficou ótimo! Bem simples de entender. Mas o resultado visual...




    O ponto é: precisamos atacar os dois pontos. O código precisa ser limpo,
mas ao mesmo tempo nossas views precisam ser estilizadas para que a apli-
cação fique mais atraente e tenha uma boa usabilidade.
    Nossa solução inicial será extrair estes estilos e aplicá-los utilizando o
método setStyle, como a seguir:


118


[PAGINA 129]
Casa do Código                                         Capítulo 6. CSS no Java FX



▲❛❜❡❧ ❧❛❜❡❧ ❂ ♥❡✇ ▲❛❜❡❧✭✧▲✐st❛❣❡♠ ❞❡ ▲✐✈r♦s✧✮❀
❧❛❜❡❧✳s❡t❙t②❧❡✭❄❄❄✮❀

   Esse método espera receber como parâmetro as propriedades CSS que
devem ser aplicadas no elemento. Um exemplo seria:

▲❛❜❡❧ ❧❛❜❡❧ ❂ ♥❡✇ ▲❛❜❡❧✭✧▲✐st❛❣❡♠ ❞❡ ▲✐✈r♦s✧✮❀

❧❛❜❡❧✳s❡t❙t②❧❡✭✧✲❢①✲❢♦♥t✲s✐③❡✿
        ✸✵♣①❀ ✲❢①✲♣❛❞❞✐♥❣✿ ✷✵ ✵ ✶✵ ✶✵❀✧✮❀

   Se você já está habituado com CSS, deve ter percebido que as propriedades
aqui são muito parecidas com CSS que utilizamos na web, tendo o prefixo
-fx sempre presente como uma diferença. Neste caso, o código está fazendo
o mesmo que o anterior, onde declarávamos o tamanho da fonte e padding
programaticamente. Podemos executá-lo para verificar o resultado:




   Excelente! Ele está com a aparência esperada, mas agora utilizando as
propriedades do CSS.




                                                                             119


[PAGINA 130]
6.2. Extraindo estilos pra um arquivo .css                       Casa do Código




  Java FX CSS Reference Guide

     Na documentação do método setStyle, você encontrará um link
  direto para a página CSS Reference Guide, onde os possíveis estilos são
  explicados detalhadamente. Essa página pode ajudar bastante no dia a
  dia; consulte-a sempre que quiser conhecer mais detalhes sobre as pro-
  priedades e possibilidades dos parâmetros CSS.




                Fig. 6.3: Documentação do método setStyle pelo Eclipse




6.2       Extraindo estilos pra um arquivo .css
A mudança que fizemos já pode ser interessante, mas ainda não resolve
nosso problema. Ainda estamos misturando nosso código de estilos com
o restante do código! No lugar de utilizar o setStyle dessa forma,
podemos (e devemos, sempre que possível) isolar nossos estilos no arquivo
application.css.
    Se você criou o projeto utilizando uma versão mais atual do Eclipse, ou
qualquer outra IDE moderna, o arquivo application.css deve ter sido
criado junto com ele. Não se preocupe se isso não aconteceu, esse é um ar-
quivo normal. Se necessário, você pode criá-lo clicando em New..., sub-
menu File e digitando o nome application.css ou qualquer outro
nome que preferir.

120


[PAGINA 131]
Casa do Código                                          Capítulo 6. CSS no Java FX



    Dentro dele colocaremos o seguinte conteúdo:
✳❧❛❜❡❧ ④
    ✲❢①✲❢♦♥t✲s✐③❡✿ ✸✵♣①❀
    ✲❢①✲♣❛❞❞✐♥❣✿ ✷✵ ✵ ✶✵ ✶✵❀
⑥

     Note que se parece muito com a estrutura do CSS padrão. Aplicamos o
efeito em .label, pois é a classe padrão (default) do elemento Label. A
maior parte dos elementos visuais do Java FX já tem uma classe default, que
normalmente é seu próprio nome.
     Agora tudo que precisamos fazer é adicionar o arquivo
application.css como um estilo de nosso cenário. Em nossa classe
Main, faremos algo como:

s❝❡♥❡✳❣❡t❙t②❧❡s❤❡❡ts✭✮✳❛❞❞✭❣❡t❈❧❛ss✭✮
    ✳❣❡t❘❡s♦✉r❝❡✭✧❛♣♣❧✐❝❛t✐♦♥✳❝ss✧✮✳t♦❊①t❡r♥❛❧❋♦r♠✭✮✮❀

    Pronto! Ao rodar esse código, vemos que o resultado não foi bem o que
estávamos esperando:




    O efeito foi aplicado, mas para todos os labels da view. Para nossa sorte
(ou o oposto disso) o componente TableView também utiliza labels em suas
colunas.


                                                                              121


[PAGINA 132]
6.2. Extraindo estilos pra um arquivo .css                   Casa do Código


Identificando elementos únicos
    Precisamos de uma forma única de identificar o Label que contém nosso
texto da listagem, sem que os efeitos dele interfiram nos demais Labels que
existem, ou possam existir em algum momento futuro, na view. Podemos
fazer isso adicionando um identificador único ao elemento, como a seguir:

▲❛❜❡❧ ❧❛❜❡❧ ❂ ♥❡✇ ▲❛❜❡❧✭✧▲✐st❛❣❡♠ ❞❡ ▲✐✈r♦s✧✮❀
❧❛❜❡❧✳s❡t■❞✭✧❧❛❜❡❧✲❧✐st❛❣❡♠✧✮❀

     Como você pode ver, o método setId nos ajuda com esse trabalho.
Agora que temos uma maneira única de nos referir ao Label, basta mod-
ificar o arquivo application.css para ficar assim:

★❧❛❜❡❧✲❧✐st❛❣❡♠ ④
    ✲❢①✲❢♦♥t✲s✐③❡✿ ✸✵♣①❀
    ✲❢①✲♣❛❞❞✐♥❣✿ ✷✵ ✵ ✶✵ ✶✵❀
⑥

    O seletor de id tem a estrutura idêntica, mas recebe um # como prefixo,
no lugar do . utilizado para as classes dos elementos. Execute o código e
dessa vez o resultado será o esperado:




Extraindo mais estilos pro application.css
    Da mesma forma como fizemos para tirar o padding na Label princi-
pal da nossa listagem, podemos tirar do VBox que utilizamos para alinhar a
tabela. Veja como ele está agora:

122


[PAGINA 133]
Casa do Código                                       Capítulo 6. CSS no Java FX



❱❇♦① ✈❜♦① ❂ ♥❡✇ ❱❇♦①✭t❛❜❧❡❱✐❡✇✮❀
✈❜♦①✳s❡tP❛❞❞✐♥❣✭♥❡✇ ■♥s❡ts✭✼✵✱ ✵✱ ✵ ✱✶✵✮✮❀

    Poderíamos simplesmente remover a chamada ao método setPadding
e no arquivo application.css adicionar o estilo:

✳✈❜♦① ④
    ✲❢①✲♣❛❞❞✐♥❣✿ ✼✵ ✵ ✵ ✶✵❀
⑥

    Mas há um detalhe importante, nem todo elemento em Java FX tem uma
classe seletora já definida.
    Em outras palavras, para aplicar um estilo no Label, fizemos:

✳❧❛❜❡❧ ④
    ★ ❡st✐❧♦s ❛q✉✐
⑥

    Ou seja, por padrão o Label já tem uma classe seletora, chamada
.label. Já o VBox não tem uma classe padrão, ou seja, o CSS que escreve-
mos com o seletor .vbox não vai funcionar. Ao executar a app dessa forma,
percebemos que o padding não foi aplicado:




   Já sabemos como resolver esse problema, certo? Da mesma forma como
demos um identificador único para o Label (label-listagem), podemos dar
um ID para o VBox, aplicando um estilo para ele:

                                                                           123


[PAGINA 134]
6.2. Extraindo estilos pra um arquivo .css                  Casa do Código


❱❇♦① ✈❜♦① ❂ ♥❡✇ ❱❇♦①✭t❛❜❧❡❱✐❡✇✮❀
✈❜♦①✳s❡t■❞✭✧✈❜♦①✧✮❀

      Em nosso arquivo application.css, podemos fazer:

★✈❜♦① ④
    ✲❢①✲♣❛❞❞✐♥❣✿ ✼✵ ✵ ✵ ✶✵❀
⑥

    Ótimo, ao executar o código vemos que o padding foi aplicado. Note o #
do seletor, para identificá-lo como um ID.
    Podemos agora modificar um pouco o estilo do Button de expor-
tar produtos como CSV. A primeira mudança pode ser extrair os métodos
setLayouts para um estilo CSS. O código agora está assim:

❇✉tt♦♥ ❜✉tt♦♥ ❂ ♥❡✇ ❇✉tt♦♥✭✧❊①♣♦rt❛r ❈❙❱✧✮❀
❜✉tt♦♥✳s❡t▲❛②♦✉t❳✭✺✼✺✮❀
❜✉tt♦♥✳s❡t▲❛②♦✉t❨✭✷✺✮❀

    No lugar disso, removemos as chamadas aos dois métodos e adi-
cionamos o mesmo efeito no application.css, utilizando as pro-
priedades -fx-translate-x e -fx-translate-y:

✳❜✉tt♦♥ ④
    ✲❢①✲tr❛♥s❧❛t❡✲①✿ ✺✼✺❀
    ✲❢①✲tr❛♥s❧❛t❡✲②✿ ✷✺❀
⑥

   Também podemos aplicar uma cor nesse botão, utilizando o
-fx-background-color. Uma forma de fazer isso seria:

✳❜✉tt♦♥ ④
    ✲❢①✲tr❛♥s❧❛t❡✲①✿ ✺✼✺❀
    ✲❢①✲tr❛♥s❧❛t❡✲②✿ ✷✺❀
    ✲❢①✲❜❛❝❦❣r♦✉♥❞✲❝♦❧♦r✿ r❣❜✭✸✶✱ ✶✹✾✱ ✷✵✻✮❀
    ✲❢①✲t❡①t✲❢✐❧❧✿ ✇❤✐t❡❀
⑥

   Assim, o button ficará com o azul padrão do Java FX. Se preferir,
você pode aplicar qualquer outra cor. O mesmo para os outros elementos,

124


[PAGINA 135]
Casa do Código                                          Capítulo 6. CSS no Java FX



claro. Note que também utilizamos a propriedade -fx-text-fill para
deixar o texto branco. Além desses, existem diversas outras propriedades.
Aproveite para explorar o Java FX CSS Reference Guide durante seus testes
para conhecer mais algumas delas.
    Outro detalhe bem interessante é que, da mesma forma que no CSS con-
vencional de navegadores, também podemos adicionar um :hover em nos-
sos seletores para definir o estilo para o momento em que o mouse estiver
sob o elemento. Para ver isso em prática, vamos dizer que queremos uma
transparência maior no button, quando estiver em hover:

✳❜✉tt♦♥✿❤♦✈❡r ④
    ✲❢①✲❜❛❝❦❣r♦✉♥❞✲❝♦❧♦r✿ r❣❜❛✭✸✶✱ ✶✹✾✱ ✷✵✻✱ ✵✳✼✶✮❀
⑥

    Atualize e execute seu código. Você perceberá a transparência ao passar
o cursor do mouse sob o botão.




                 Fig. 6.7: Button com e sem efeito de hover


    O mesmo pode ser feito com o Label de progresso, que está assim:

▲❛❜❡❧ ♣r♦❣r❡ss♦ ❂ ♥❡✇ ▲❛❜❡❧✭✮❀
♣r♦❣r❡ss♦✳s❡t▲❛②♦✉t❳✭✹✽✺✮❀
♣r♦❣r❡ss♦✳s❡t▲❛②♦✉t❨✭✸✵✮❀

    Removemos essas duas linhas e damos um ID para esse campo:

▲❛❜❡❧ ♣r♦❣r❡ss♦ ❂ ♥❡✇ ▲❛❜❡❧✭✮❀
♣r♦❣r❡ss♦✳s❡t■❞✭✧❧❛❜❡❧✲♣r♦❣r❡ss♦✧✮❀

    Agora basta adicionar o estilo no arquivo de CSS:

                                                                              125


[PAGINA 136]
6.2. Extraindo estilos pra um arquivo .css                     Casa do Código


★❧❛❜❡❧✲♣r♦❣r❡ss♦ ④
    ✲❢①✲tr❛♥s❧❛t❡✲①✿ ✹✽✺❀
    ✲❢①✲tr❛♥s❧❛t❡✲②✿ ✸✵❀
⑥


   Explorando mais seletores e efeitos

       Você pode utilizar diversas outras funções e efeitos, como um
   linear-gradient na cor de seu button ou fundo do scene. E que
   tal um efeito de sombra?

   ✳❜✉tt♦♥ ④
       ✲❢①✲❜❛❝❦❣r♦✉♥❞✲❝♦❧♦r✿
           ❧✐♥❡❛r✲❣r❛❞✐❡♥t✭★✻✶❛✷❜✶✱ ★✷❆✺✵✺✽✮❀
       ✲❢①✲❡❢❢❡❝t✿ ❞r♦♣s❤❛❞♦✇✭t❤r❡❡✲♣❛ss✲❜♦①✱
           r❣❜❛✭✵✱✵✱✵✱✵✳✻✮✱ ✺✱ ✵✳✵✱ ✵✱ ✶✮❀
   ⑥

      Não deixe de testar. Você pode ver esses e diversos outros efeitos no
   tutorial de Java FX da Oracle:
      https://docs.oracle.com/javase/8/javafx/get-started-tutorial


Quantidade de produtos e valor em estoque
    Para deixar nossa listagem um pouco mais completa, vamos adicionar um
novo Label com o valor total que temos em estoque e também a quantidade
de produtos. Criar a label já sabemos. Podemos também adicionar um
identificador único, com o método setID, para aplicar um estilo no novo
elemento. O código ficará assim:
▲❛❜❡❧ ❧❛❜❡❧❋♦♦t❡r ❂ ♥❡✇ ▲❛❜❡❧✭✧❚❡①t♦ ✈❛✐ ❛q✉✐✧✮❀
❧❛❜❡❧❋♦♦t❡r✳s❡t■❞✭✧❧❛❜❡❧✲❢♦♦t❡r✧✮❀

   No CSS, podemos alinhar a label-footer e também modificar o
tamanho de sua fonte, para que tenha um destaque maior.
★❧❛❜❡❧✲❢♦♦t❡r ④
    ✲❢①✲❢♦♥t✲s✐③❡✿ ✶✺♣①❀

126


[PAGINA 137]
Casa do Código                                            Capítulo 6. CSS no Java FX



      ✲❢①✲tr❛♥s❧❛t❡✲①✿ ✷✶✵❀
      ✲❢①✲tr❛♥s❧❛t❡✲②✿ ✹✽✵❀
⑥

     Precisamos agora adicionar o texto e valores que devem aparecer nesse
Label. Vamos utilizar o método format da classe String mais uma vez,
para deixar o resultado formatado como a seguir:
▲❛❜❡❧ ❧❛❜❡❧❋♦♦t❡r ❂ ♥❡✇ ▲❛❜❡❧✭
    ❙tr✐♥❣✳❢♦r♠❛t✭✧❱♦❝ê t❡♠ ❘✩✪✳✷❢ ❡♠ ❡st♦q✉❡✱ ✧ ✰
        ✧❝♦♠ ✉♠ t♦t❛❧ ❞❡ ✪❞ ♣r♦❞✉t♦s✳✧✱ ✶✵✵✳✵✵✱ ✶✵✮✮❀

❧❛❜❡❧❋♦♦t❡r✳s❡t■❞✭✧❧❛❜❡❧✲❢♦♦t❡r✧✮❀

     Dessa forma, o resultado será parecido com:
❱♦❝ê t❡♠ ❘✩✶✵✵✳✵✵ ❡♠ ❡st♦q✉❡✱ ❝♦♠ ✉♠ t♦t❛❧ ❞❡ ✶✵ ♣r♦❞✉t♦s✳


    Para saber mais: String#format

        Note que utilizamos %.2f para formatar um número de ponto flu-
    tuante em duas casas decimais, além do %d para exibir o número in-
    teiro. Existem diversas outras opções, como %s para Strings, %c
    para chars e %t para datas. Se você não está familiarizado com as
    convenções do Formatter e quiser conhecer um pouco mais, pode dar
    uma olhada em:
        https://docs.oracle.com/javase/7/docs/api/java/util/Formatter.html

     Não queremos trabalhar com um valor fixo, como acabamos de fazer. No
lugar disso, nos interessa recuperar o valor total de todos os produtos de nossa
lista. Podemos iterar na lista acumulando todos os valores em uma variável
temporária:
❞♦✉❜❧❡ ✈❛❧♦r❚♦t❛❧ ❂ ✵✳✵❀

❢♦r ✭Pr♦❞✉t♦ ♣r♦❞✉t♦✿ ♣r♦❞✉t♦s✮ ④
    ✈❛❧♦r❚♦t❛❧ ✰❂ ♣r♦❞✉t♦✳❣❡t❱❛❧♦r✭✮❀
⑥

                                                                                127


[PAGINA 138]
6.2. Extraindo estilos pra um arquivo .css                        Casa do Código


    Não tem muito segredo nesse código, usamos o += para incrementar o
valor de cada produto.


   Código mais declarativo com Java 8

      No lugar de escrever esse código imperativo, onde declaramos uma
   variável intermediária ( valorTotal) e incrementamos seu valor em
   um enhanced-for, que tal fazer esse mesmo trabalho de uma forma
   mais declarativa, com um toque de programação funcional do Java 8?
      Utilizando a nova API de Stream, o código ficaria assim:

   ❞♦✉❜❧❡ ✈❛❧♦r❚♦t❛❧ ❂ ♣r♦❞✉t♦s✳str❡❛♠✭✮
       ✳♠❛♣❚♦❉♦✉❜❧❡✭Pr♦❞✉t♦✿✿❣❡t❱❛❧♦r✮✳s✉♠✭✮❀

      Se você está utilizando Java 8, atualize seu código para testar. O resul-
   tado será o mesmo.

     Para concluir, podemos recuperar a quantidade de produtos em estoque
utilizando o método size da lista de produtos:

▲❛❜❡❧ ❧❛❜❡❧❋♦♦t❡r ❂ ♥❡✇ ▲❛❜❡❧✭
    ❙tr✐♥❣✳❢♦r♠❛t✭✧❱♦❝ê t❡♠ ❘✩✪✳✷❢ ❡♠ ❡st♦q✉❡✱ ✧ ✰
        ✧❝♦♠ ✉♠ t♦t❛❧ ❞❡ ✪❞ ♣r♦❞✉t♦s✳✧✱
        ✈❛❧♦r❚♦t❛❧✱ ♣r♦❞✉t♦s✳s✐③❡✭✮✮✮❀

❧❛❜❡❧❋♦♦t❡r✳s❡t■❞✭✧❧❛❜❡❧✲❢♦♦t❡r✧✮❀

      Só precisamos adicionar o labelFooter na view, e pronto:

❣r♦✉♣✳❣❡t❈❤✐❧❞r❡♥✭✮✳❛❞❞❆❧❧✭❧❛❜❡❧✱
    ✈❜♦①✱ ❜✉tt♦♥✱ ♣r♦❣r❡ss♦✱ ❧❛❜❡❧❋♦♦t❡r✮❀

      Perfeito, execute o código para ver o resultado!




128


[PAGINA 139]
Casa do Código                                      Capítulo 6. CSS no Java FX




    O código completo da classe Main ficou assim:

♣❛❝❦❛❣❡ ❛♣♣❧✐❝❛t✐♦♥❀

✐♠♣♦rt ✐♦✳❊①♣♦rt❛❞♦r❀

✐♠♣♦rt ❥❛✈❛✳✐♦✳■❖❊①❝❡♣t✐♦♥❀

✐♠♣♦rt ❥❛✈❛❢①✳❛♣♣❧✐❝❛t✐♦♥✳❆♣♣❧✐❝❛t✐♦♥❀
✐♠♣♦rt ❥❛✈❛❢①✳❝♦❧❧❡❝t✐♦♥s✳❖❜s❡r✈❛❜❧❡▲✐st❀
✐♠♣♦rt ❥❛✈❛❢①✳❝♦♥❝✉rr❡♥t✳❚❛s❦❀
✐♠♣♦rt ❥❛✈❛❢①✳❣❡♦♠❡tr②✳■♥s❡ts❀
✐♠♣♦rt ❥❛✈❛❢①✳s❝❡♥❡✳✯❀
✐♠♣♦rt ❥❛✈❛❢①✳s❝❡♥❡✳❝♦♥tr♦❧✳✯❀
✐♠♣♦rt ❥❛✈❛❢①✳s❝❡♥❡✳❝♦♥tr♦❧✳❝❡❧❧✳Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②❀
✐♠♣♦rt ❥❛✈❛❢①✳s❝❡♥❡✳❧❛②♦✉t✳❱❇♦①❀

                                                                         129


[PAGINA 140]
6.2. Extraindo estilos pra um arquivo .css               Casa do Código


✐♠♣♦rt ❥❛✈❛❢①✳s❝❡♥❡✳t❡①t✳✯❀
✐♠♣♦rt ❥❛✈❛❢①✳st❛❣❡✳❙t❛❣❡❀
✐♠♣♦rt ❜r✳❝♦♠✳❝❛s❛❞♦❝♦❞✐❣♦✳❧✐✈r❛r✐❛✳♣r♦❞✉t♦s✳Pr♦❞✉t♦❀
✐♠♣♦rt ❞❛♦✳Pr♦❞✉t♦❉❆❖❀

❅❙✉♣♣r❡ss❲❛r♥✐♥❣s✭④ ✧✉♥❝❤❡❝❦❡❞✧✱ ✧r❛✇t②♣❡s✧ ⑥✮
♣✉❜❧✐❝ ❝❧❛ss ▼❛✐♥ ❡①t❡♥❞s ❆♣♣❧✐❝❛t✐♦♥ ④

      ❅❖✈❡rr✐❞❡
      ♣✉❜❧✐❝ ✈♦✐❞ st❛rt✭❙t❛❣❡ ♣r✐♠❛r②❙t❛❣❡✮ ④

             ●r♦✉♣ ❣r♦✉♣ ❂ ♥❡✇ ●r♦✉♣✭✮❀
             ❙❝❡♥❡ s❝❡♥❡ ❂ ♥❡✇ ❙❝❡♥❡✭❣r♦✉♣✱ ✻✾✵✱ ✺✶✵✮❀

             s❝❡♥❡✳❣❡t❙t②❧❡s❤❡❡ts✭✮✳❛❞❞✭❣❡t❈❧❛ss✭✮
                 ✳❣❡t❘❡s♦✉r❝❡✭✧❛♣♣❧✐❝❛t✐♦♥✳❝ss✧✮✳t♦❊①t❡r♥❛❧❋♦r♠✭✮✮❀

             ❖❜s❡r✈❛❜❧❡▲✐st❁Pr♦❞✉t♦❃ ♣r♦❞✉t♦s ❂
                 ♥❡✇ Pr♦❞✉t♦❉❆❖✭✮✳❧✐st❛✭✮❀

             ❚❛❜❧❡❱✐❡✇❁Pr♦❞✉t♦❃ t❛❜❧❡❱✐❡✇ ❂
                 ♥❡✇ ❚❛❜❧❡❱✐❡✇❁❃✭♣r♦❞✉t♦s✮❀

             ❚❛❜❧❡❈♦❧✉♠♥ ♥♦♠❡❈♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭✧◆♦♠❡✧✮❀
             ♥♦♠❡❈♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭✶✽✵✮❀
             ♥♦♠❡❈♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
                 ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②✭✧♥♦♠❡✧✮✮❀

             ❚❛❜❧❡❈♦❧✉♠♥ ❞❡s❝❈♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭✧❉❡s❝r✐çã♦✧✮❀
             ❞❡s❝❈♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭✷✸✵✮❀
             ❞❡s❝❈♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
                 ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②✭✧❞❡s❝r✐❝❛♦✧✮✮❀

             ❚❛❜❧❡❈♦❧✉♠♥ ✈❛❧♦r❈♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭✧❱❛❧♦r✧✮❀
             ✈❛❧♦r❈♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭✻✵✮❀
             ✈❛❧♦r❈♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
                 ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②✭✧✈❛❧♦r✧✮✮❀

             ❚❛❜❧❡❈♦❧✉♠♥ ✐s❜♥❈♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭✧■❙❇◆✧✮❀

130


[PAGINA 141]
Casa do Código                                     Capítulo 6. CSS no Java FX



          ✐s❜♥❈♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭✶✽✵✮❀
          ✐s❜♥❈♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
              ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②✭✧✐s❜♥✧✮✮❀

          t❛❜❧❡❱✐❡✇✳❣❡t❈♦❧✉♠♥s✭✮✳❛❞❞❆❧❧✭♥♦♠❡❈♦❧✉♠♥✱ ❞❡s❝❈♦❧✉♠♥✱
              ✈❛❧♦r❈♦❧✉♠♥✱ ✐s❜♥❈♦❧✉♠♥✮❀

          ❢✐♥❛❧ ❱❇♦① ✈❜♦① ❂ ♥❡✇ ❱❇♦①✭t❛❜❧❡❱✐❡✇✮❀
          ✈❜♦①✳s❡t■❞✭✧✈❜♦①✧✮❀

          ▲❛❜❡❧ ❧❛❜❡❧ ❂ ♥❡✇ ▲❛❜❡❧✭✧▲✐st❛❣❡♠ ❞❡ ▲✐✈r♦s✧✮❀
          ❧❛❜❡❧✳s❡t■❞✭✧❧❛❜❡❧✲❧✐st❛❣❡♠✧✮❀

          ▲❛❜❡❧ ♣r♦❣r❡ss♦ ❂ ♥❡✇ ▲❛❜❡❧✭✮❀
          ♣r♦❣r❡ss♦✳s❡t■❞✭✧❧❛❜❡❧✲♣r♦❣r❡ss♦✧✮❀

          ❇✉tt♦♥ ❜✉tt♦♥ ❂ ♥❡✇ ❇✉tt♦♥✭✧❊①♣♦rt❛r ❈❙❱✧✮❀

          ❜✉tt♦♥✳s❡t❖♥❆❝t✐♦♥✭❡✈❡♥t ✲❃ ④

                 ❚❛s❦❁❱♦✐❞❃ t❛s❦ ❂ ♥❡✇ ❚❛s❦❁❱♦✐❞❃✭✮ ④
                     ❅❖✈❡rr✐❞❡
                     ♣r♦t❡❝t❡❞ ❱♦✐❞ ❝❛❧❧✭✮ t❤r♦✇s ❊①❝❡♣t✐♦♥ ④
                         ❞♦r♠❡P♦r❱✐♥t❡❙❡❣✉♥❞♦s✭✮❀
                         ❡①♣♦rt❛❊♠❈❙❱✭♣r♦❞✉t♦s✮❀
                         r❡t✉r♥ ♥✉❧❧❀
                     ⑥
                 ⑥❀

                 t❛s❦✳s❡t❖♥❘✉♥♥✐♥❣✭❡ ✲❃ ♣r♦❣r❡ss♦✳s❡t❚❡①t✭
                                         ✧❡①♣♦rt❛♥❞♦✳✳✳✧✮✮❀

                 t❛s❦✳s❡t❖♥❙✉❝❝❡❡❞❡❞✭❡ ✲❃ ♣r♦❣r❡ss♦✳s❡t❚❡①t✭
                                         ✧❝♦♥❝❧✉í❞♦✦✧✮✮❀

                 ♥❡✇ ❚❤r❡❛❞✭t❛s❦✮✳st❛rt✭✮❀
          ⑥✮❀

          ❞♦✉❜❧❡ ✈❛❧♦r❚♦t❛❧ ❂ ♣r♦❞✉t♦s✳str❡❛♠✭✮

                                                                         131


[PAGINA 142]
6.2. Extraindo estilos pra um arquivo .css                    Casa do Código


                          ✳♠❛♣❚♦❉♦✉❜❧❡✭Pr♦❞✉t♦✿✿❣❡t❱❛❧♦r✮✳s✉♠✭✮❀

             ▲❛❜❡❧ ❧❛❜❡❧❋♦♦t❡r ❂ ♥❡✇ ▲❛❜❡❧✭
                     ❙tr✐♥❣✳❢♦r♠❛t✭✧❱♦❝ê t❡♠ ❘✩✪✳✷❢ ❡♠ ❡st♦q✉❡✱ ✧ ✰
                         ✧❝♦♠ ✉♠ t♦t❛❧ ❞❡ ✪❞ ♣r♦❞✉t♦s✳✧✱
                         ✈❛❧♦r❚♦t❛❧✱ ♣r♦❞✉t♦s✳s✐③❡✭✮✮✮❀

             ❧❛❜❡❧❋♦♦t❡r✳s❡t■❞✭✧❧❛❜❡❧✲❢♦♦t❡r✧✮❀

             ❣r♦✉♣✳❣❡t❈❤✐❧❞r❡♥✭✮✳❛❞❞❆❧❧✭❧❛❜❡❧✱
                 ✈❜♦①✱ ❜✉tt♦♥✱ ♣r♦❣r❡ss♦✱ ❧❛❜❡❧❋♦♦t❡r✮❀

             ♣r✐♠❛r②❙t❛❣❡✳s❡t❚✐t❧❡✭
                 ✧❙✐st❡♠❛ ❞❛ ❧✐✈r❛r✐❛ ❝♦♠ ❏❛✈❛ ❋❳✧✮❀
             ♣r✐♠❛r②❙t❛❣❡✳s❡t❙❝❡♥❡✭s❝❡♥❡✮❀
             ♣r✐♠❛r②❙t❛❣❡✳s❤♦✇✭✮❀
      ⑥

      ♣r✐✈❛t❡ ✈♦✐❞ ❡①♣♦rt❛❊♠❈❙❱✭❖❜s❡r✈❛❜❧❡▲✐st❁Pr♦❞✉t♦❃ ♣r♦❞✉t♦s✮④
          tr② ④
              ♥❡✇ ❊①♣♦rt❛❞♦r✭✮✳♣❛r❛❈❙❱✭♣r♦❞✉t♦s✮❀
          ⑥ ❝❛t❝❤ ✭■❖❊①❝❡♣t✐♦♥ ❡✮ ④
              ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❊rr♦ ❛♦ ❡①♣♦rt❛r✿ ✧✰ ❡✮❀
          ⑥
      ⑥

      ♣r✐✈❛t❡ ✈♦✐❞ ❞♦r♠❡P♦r❱✐♥t❡❙❡❣✉♥❞♦s✭✮ ④
          tr② ④
              ❚❤r❡❛❞✳s❧❡❡♣✭✷✵✵✵✵✮❀
          ⑥ ❝❛t❝❤ ✭■♥t❡rr✉♣t❡❞❊①❝❡♣t✐♦♥ ❡✮ ④
              ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❖♣s✱ ♦❝♦rr❡✉ ✉♠ ❡rr♦✿ ✧✰ ❡✮❀
          ⑥
      ⑥

      ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④
          ❧❛✉♥❝❤✭❛r❣s✮❀
      ⑥
⑥



132


[PAGINA 143]
Casa do Código                                 Capítulo 6. CSS no Java FX



    E nosso arquivo application.css:

★❧❛❜❡❧✲❧✐st❛❣❡♠ ④
    ✲❢①✲❢♦♥t✲s✐③❡✿ ✸✵♣①❀
    ✲❢①✲♣❛❞❞✐♥❣✿ ✷✵ ✵ ✶✵ ✶✵❀
⑥

★❧❛❜❡❧✲♣r♦❣r❡ss♦ ④
    ✲❢①✲tr❛♥s❧❛t❡✲①✿ ✹✽✺❀
    ✲❢①✲tr❛♥s❧❛t❡✲②✿ ✸✵❀
⑥

✳t❛❜❧❡✲✈✐❡✇ ④
    ✲❢①✲♠✐♥✲✇✐❞t❤✿ ✻✻✺❀
    ✲❢①✲♠❛①✲✇✐❞t❤✿ ✻✻✺❀
⑥

✳t❛❜❧❡✲❝♦❧✉♠♥ ④
    ✲❢①✲♣❛❞❞✐♥❣✿ ✵ ✵ ✵ ✶✵❀
⑥

★✈❜♦① ④
    ✲❢①✲♣❛❞❞✐♥❣✿ ✼✵ ✵ ✵ ✶✵❀
⑥

✳❜✉tt♦♥ ④
    ✲❢①✲tr❛♥s❧❛t❡✲①✿ ✺✼✺❀
    ✲❢①✲tr❛♥s❧❛t❡✲②✿ ✷✺❀
    ✲❢①✲❜❛❝❦❣r♦✉♥❞✲❝♦❧♦r✿ r❣❜✭✸✶✱ ✶✹✾✱ ✷✵✻✮❀
    ✲❢①✲t❡①t✲❢✐❧❧✿ ✇❤✐t❡❀
⑥

✳❜✉tt♦♥✿❤♦✈❡r ④
    ✲❢①✲❜❛❝❦❣r♦✉♥❞✲❝♦❧♦r✿ r❣❜❛✭✸✶✱ ✶✹✾✱ ✷✵✻✱ ✵✳✼✶✮❀
⑥

★❧❛❜❡❧✲❢♦♦t❡r ④
    ✲❢①✲❢♦♥t✲s✐③❡✿ ✶✺♣①❀
    ✲❢①✲tr❛♥s❧❛t❡✲①✿ ✷✶✵❀


                                                                     133


[PAGINA 144]
6.2. Extraindo estilos pra um arquivo .css                      Casa do Código


      ✲❢①✲tr❛♥s❧❛t❡✲②✿ ✹✽✵❀
⑥

    Antes de seguir para os próximos capítulos, você pode personalizar ainda
mais a sua listagem. Aplique novos estilos, cores, fontes, efeitos. Use e abuse
da documentação para absorver esse conteúdo de forma prática. Se quiser,
você pode compartilhar comigo e com os demais leitores o resultado final do
projeto com as suas melhorias.




134


[PAGINA 145]
Capítulo 7

JAR, bibliotecas e build
Queremos o quanto antes lançar nossa aplicação, distribuir nas diversas
livrarias e stands de venda. Por onde podemos começar?
    Neste capítulo, veremos não só como compactar e distribuir nossa apli-
cação final, mas também como gerar e utilizar bibliotecas para linguagem
Java. Além disso, veremos uma forma interessante de fazer o build e gerenci-
amento de dependências de nosso projeto, utilizando Maven, que é uma das
ferramentas mais essenciais do mercado de hoje em dia.


7.1 JAR
Não queremos mandar todas as nossas classes e arquivos de configurações
soltos para o cliente final, isso seria uma bagunça. Perder um dos arquivos
implicaria no não funcionamento da aplicação, por exemplo. Uma forma bem


[PAGINA 146]
7.2. Gerando JAR executável pela IDE                            Casa do Código


mais interessante seria compactar tudo em um único arquivo, um ZIP com
tudo que o usuário precisa para executar nosso código.
    Esse tipo de ZIP recebe na verdade a extensão JAR, de Java ARchive
(arquivo Java). Nele estarão presentes nosso código-fonte compilado (
bytecode), arquivos de configurações e dependências.
    Como criar um JAR executável? Isso é bem simples, você inclusive pode
fazer com qualquer compactador ZIP atual que conheça. Veremos uma
forma bem prática de fazer pela própria IDE, em nosso caso o Eclipse.


  JAR na linha de comando

     Você também pode gerar um JAR diretamente pala linha de co-
  mando, utilizando o programa jar presente no JDK. Apesar de ser um
  pouco mais trabalhoso, você consegue gerar o seu executável com o co-
  mando:

  ❥❛r ✲❝✈❢ ❧✐✈r❛r✐❛✳❥❛r
      sr❝✴❛♣♣❧✐❝❛t✐♦♥✴✯✳❥❛✈❛
      sr❝✴❞❜✴✯✳❥❛✈❛
      sr❝✴✐♦✴✯✳❥❛✈❛
      sr❝✴r❡♣♦s✐t♦r✐♦✴✯✳❥❛✈❛❀




7.2 Gerando JAR executável pela IDE
Fazer o processo pelo Eclipse, ou qualquer outra IDE moderna, é verdadeira-
mente mais simples. Para gerar o JAR executável de nossa aplicação Java FX,
tudo o que precisamos fazer é clicar com o botão direito no projeto, selecionar
Export e em seguida a opção Runnable JAR File.




136


[PAGINA 147]
Casa do Código                                  Capítulo 7. JAR, bibliotecas e build




    Após selecioná-la, podemos escolher em Launch configuration qual a
classe que deverá ser executada ao rodar esse JAR. Vamos escolher a
classe Main. Além disso, no campo Export destination, precisamos
preencher o local em que o arquivo executável Java deve ser criado, assim
como seu nome e extensão (que será .jar):




                                                                               137


[PAGINA 148]
7.3. Executando a livraria-fx.jar                             Casa do Código




    Em meu caso, o caminho ficou /Users/turini/Desktop/livraria-fx.jar,
em outras palavras, o arquivo se chamará livraria-fx.jar e será criado
em minha área de trabalho.
    Tudo pronto, basta clicar em Finish. Simples, não acha? Aproveite para
gerar o JAR executável em sua casa, siga esses passos e confira se o arquivo
livraria-fx.jar foi criado no caminho que você definiu.


7.3 Executando a livraria-fx.jar
Agora que temos o arquivo criado, podemos tentar executá-lo para conferir se
tudo correu bem. Vamos fazer isso pela linha de comando, utilizando java

138


[PAGINA 149]
Casa do Código                                    Capítulo 7. JAR, bibliotecas e build



-jar SEU_EXECUTAVEL. Um exemplo seria:

❥❛✈❛ ✲❥❛r ❉❡s❦t♦♣✴❧✐✈r❛r✐❛✲❢①✳❥❛r

    Excelente, a app está funcionando conforme esperado!




    Note que, ao clicar em Export CSV, o arquivo produtos.csv com a
relação de todos os livros será criado na área de trabalho, mesmo local onde
se encontra o JAR.




                                                                                 139


[PAGINA 150]
7.4. Bibliotecas em Java                                       Casa do Código




   Para saber mais: JAR Launcher e outros

       Você pode utilizar programas como o JAR Launcher para rodar os
   seus executáveis Java com apenas um click, sem a necessidade de digi-
   tar o comando java -jar no terminal. No Mac OS, por exemplo, esse
   programa já vem instalado. Há diversas outras opções para os mais difer-
   entes sistemas operacionais.


7.4      Bibliotecas em Java
Um JAR não precisa necessariamente ser um executável. É muito comum
criarmos um JAR com um conjunto de classes que podem ser reutilizados
em outros projetos. Em outras palavras, criar uma biblioteca Java.
    Por sinal, o grande número de bibliotecas gratuitas em Java é um dos fa-
tores que fazem a linguagem ser tão bem aceita no mercado. Precisa gerar

140


[PAGINA 151]
Casa do Código                                     Capítulo 7. JAR, bibliotecas e build



relatórios, manipular XMLs, conectar ao banco de dados, gerar códigos de
barras etc.? Você já tem tudo isso pronto! O ecossistema do Java é enorme.
E, o melhor, grande parte (talvez a maior parte) dos projetos (bibliotecas) em
Java é gratuita e tem seu código aberto, os conhecidos open sources.
    A Caelum, empresa onde trabalho, possui diversos projetos open source.
VRaptor, Mamute e Stella são alguns deles. Contribuir com projetos de
código aberto tem diversos benefícios, desde o conhecimento, que você com
certeza vai adquirir e compartilhar, até o reconhecimento e divulgação de seu
trabalho. Se você quiser, pode conhecer alguns deles no repositório público
da Caelum:
    http://github.com/caelum/


7.5    Documentando seu projeto com Javadoc
É sempre muito interessante documentar as suas classes quando você cria
um novo JAR. Afinal, como a pessoa que vai usá-lo saberá quais classes e
métodos estão disponíveis? Outras informações como exceções que o código
pode lançar e detalhes importantes de seu uso também são diferenciais sig-
nificantes.
    O próprio código do Java é todo documentado, você pode ver a docu-
mentação completa de sua API pelo site da Oracle:
    http://download.java.net/jdk8/docs/api/index.html




                                                                                  141


[PAGINA 152]
7.5. Documentando seu projeto com Javadoc                       Casa do Código




    Você pode (e deve) usar o javadoc para criar uma documentação equiv-
alente para os seus projetos. Esse programa também já vem na JDK e pode
ser usado diretamente pela linha de comando, ou com ajuda da IDE. Se ainda
não conhece o javadoc, pode gostar de ler mais a respeito em:
    http://www.oracle.com/technetwork/articles/java/index-137868.html

Um exemplo prático de documentação em Java
    É muito simples documentar seus projetos em Java, o javadoc cuida de
boa parte do trabalho pesado. Mas, claro, é sempre interessante oferecer algu-
mas informações para enriquecer a documentação de nosso projeto. Fazemos
isso no próprio código:

142


[PAGINA 153]
Casa do Código                                      Capítulo 7. JAR, bibliotecas e build



✴✯✯
 ✯ ❈✉✐❞❛ ❞♦ ❛❝❡ss♦ ❛♦s ❞❛❞♦s ❞❛ ❝❧❛ss❡ ④❅❧✐♥❦ Pr♦❞✉t♦⑥✳
 ✯
 ✯ ❅❛✉t❤♦r ❘♦❞r✐❣♦ ❚✉r✐♥✐ ❁r♦❞r✐❣♦✳t✉r✐♥✐❅❝❛❡❧✉♠✳❝♦♠✳❜r❃
 ✯ ❅s✐♥❝❡ ✶✳✵
 ✯✴
♣✉❜❧✐❝ ❝❧❛ss Pr♦❞✉t♦❉❆❖ ④

     ✴✯✯
      ✯ ▲✐st❛ t♦❞♦s ♦s ♣r♦❞✉t♦s ❞♦ ❜❛♥❝♦ ❞❡ ❞❛❞♦s
      ✯
      ✯ ❅r❡t✉r♥ ④❅❧✐♥❦ ❖❜s❡r✈❛❜❧❡▲✐st⑥ ❝♦♠ t♦❞♦s ♦s ♣r♦❞✉t♦s
      ✯ ❅t❤r♦✇s ❘✉♥t✐♠❡❊①❝❡♣t✐♦♥ ❡♠ ❝❛s♦ ❞❡ ❡rr♦s
      ✯✴
     ♣✉❜❧✐❝ ❖❜s❡r✈❛❜❧❡▲✐st❁Pr♦❞✉t♦❃ ❧✐st❛✭✮ ④
         ✴✴ ❝ó❞✐❣♦ ♦♠✐t✐❞♦
     ⑥

     ✴✯✯
      ✯ ❅♣❛r❛♠ ♣r♦❞✉t♦ q✉❡ ❞❡✈❡rá s❡r ❛❞✐❝✐♦♥❛❞♦ ♥♦ ❜❛♥❝♦✳
      ✯ ❅t❤r♦✇s ❘✉♥t✐♠❡❊①❝❡♣t✐♦♥ ❡♠ ❝❛s♦ ❞❡ ❡rr♦s
      ✯✴
     ♣✉❜❧✐❝ ✈♦✐❞ ❛❞✐❝✐♦♥❛✭Pr♦❞✉t♦ ♣r♦❞✉t♦✮ ④
         ✴✴ ❝ó❞✐❣♦ ♦♠✐t✐❞♦
     ⑥
⑥

    Observe que isso é feito com um tipo de bloco de comentário com signifi-
cado especial. Ele sempre começa com /** e termina com */, nas outras
linhas, colocamos apenas um *.
    Você pode adicionar uma descrição para as classes e métodos, mas prefira
nada muito extenso e que conte detalhes de implementação. Por exemplo,
imagine que no javadoc eu diga que estamos persistindo em um banco de
dados MySQL. O que acontecerá se eu migrar de banco? A documentação
ficará desatualizada ou eu precisarei lembrar (o que provavelmente não vai
acontecer).
    Também podemos definir outras informações na documentação, como
fizemos com o autor, desde quando a classe existe (since), parâmetros, retorno,

                                                                                   143


[PAGINA 154]
7.5. Documentando seu projeto com Javadoc                         Casa do Código


exceptions etc. Tudo isso é feito de forma simples com as próprias anotações
de marcação do javadoc.
    Depois de devidamente documentado, pelo Eclipse, podemos ir em
Project e depois escolher a opção Generate Javadoc.




               Fig. 7.6: Gerando javadoc pela interface do Eclipse.



    Uma nova janela aparecerá. Tudo o que precisamos fazer é selecionar o
projeto que queremos documentar e o diretório onde a documentação deverá
ser gerada. Vamos colocar dentro de uma pasta chamada doc dentro do
próprio projeto.




144


[PAGINA 155]
Casa do Código                                     Capítulo 7. JAR, bibliotecas e build




            Fig. 7.7: Configurando o projeto e destino do javadoc.


     Agora só precisamos clicar em Finish e pronto, confira que a pasta doc
foi criada:




            Fig. 7.8: Arquivos criados pelo javadoc na pasta doc.



                                                                                  145


[PAGINA 156]
7.6. Automatizando build com Maven                            Casa do Código


   Abra o arquivo index.html em seu navegador para ver o resultado,
você vai gostar.


7.6     Automatizando build com Maven
O Eclipse facilitou bastante o processo de gerar o JAR executável, mas con-
forme a aplicação vai evoluindo o processo de build pode se tornar mais com-
plexo. É necessário compilar o projeto, copiar suas dependências, configu-
rações etc. Esse processo tem que ser repetido sempre.
    Fazer isso manualmente, ainda que com ajuda da IDE, pode ser tanto tra-
balhoso quanto problemático. A cada execução, o humano que está fazendo
a tarefa pode se esquecer de algum dos passos, cometer algum erro etc.
    Qual a solução? Automatizar todo esse processo. Existem diversas ferra-
mentas de build que nos auxiliam nesse trabalho, o Maven é uma das mais
populares. Com ele e seus diversos plugins, o processo de build e gerencia-
mento de dependências de nossas aplicações ficam bem simples e sofisticados.




146


[PAGINA 157]
Casa do Código                                    Capítulo 7. JAR, bibliotecas e build




  Download e instalação do Maven

     Para saber se você tem o Maven instalado em seu sistema operacional,
  basta abrir o terminal e digitar o comando mvn -version. A saída
  deverá ser parecida com:

  ❘♦❞r✐❣♦s✲▼❛❝❇♦♦❦✲Pr♦✿⑦ t✉r✐♥✐✩ ♠✈♥ ✲✈❡rs✐♦♥
  ❆♣❛❝❤❡ ▼❛✈❡♥ ✸✳✷✳✸ ✭✳✳✳❀ ✷✵✶✹✲✵✽✲✶✶❚✶✼✿✺✽✿✶✵✲✵✸✿✵✵✮
  ▼❛✈❡♥ ❤♦♠❡✿ ✴❆♣♣❧✐❝❛t✐♦♥s✴❛♣❛❝❤❡✲♠❛✈❡♥✲✸✳✷✳✸
  ❏❛✈❛ ✈❡rs✐♦♥✿ ✶✳✽✳✵❴✷✺✱ ✈❡♥❞♦r✿ ❖r❛❝❧❡ ❈♦r♣♦r❛t✐♦♥
  ❏❛✈❛ ❤♦♠❡✿ ✴▲✐❜r❛r②✴❏❛✈❛✴✳✳✳✴❥❞❦✶✳✽✳✵❴✷✺✳❥❞❦✴❈♦♥t❡♥ts✴❍♦♠❡✴❥r❡
  ❉❡❢❛✉❧t ❧♦❝❛❧❡✿ ❡♥❴❯❙✱ ♣❧❛t❢♦r♠ ❡♥❝♦❞✐♥❣✿ ❯❚❋✲✽
  ❖❙ ♥❛♠❡✿ ✧♠❛❝ ♦s ①✧✱ ✈❡rs✐♦♥✿ ✧✶✵✳✾✳✹✧✱ ❛r❝❤✿ ✧①✽✻❴✻✹✧

     Se você ainda não tem o Maven instalado, pode fazer seu download
  direto pelo seu site:
     http://maven.apache.org/download.cgi
     Lá você também encontra instruções de instalação para cada SO. Se
  encontrar qualquer dificuldade para fazer isso, não deixe de postar no
  GUJ ou nos mandar um e-mail.


7.7 Transformando nossa app em um projeto
    Maven
Agora que já temos tudo baixado e configurado, podemos converter nossa
app para um projeto Maven. O Eclipse também simplifica muito esse tra-
balho, tudo o que precisamos fazer é clicar com o botão direito no projeto e
selecionar:

    • Configure

    • Convert to Maven Project




                                                                                 147


[PAGINA 158]
7.7. Transformando nossa app em um projeto Maven             Casa do Código




      A janela Create new POM deve aparecer. Nela, vamos preencher o campo
Group Id com br.com.casadocodigo, que é o pacote padrão do projeto,
o Artifact Id com o nome livraria-fx e manter as outras opções com
o valor padrão.




148


[PAGINA 159]
Casa do Código                              Capítulo 7. JAR, bibliotecas e build




   Clicamos em Finish e pronto, um arquivo chamado pom.xml foi cri-
ado em nosso projeto.




                                                                           149


[PAGINA 160]
7.7. Transformando nossa app em um projeto Maven    Casa do Código




      Esse arquivo possui o seguinte conteúdo:

❁♣r♦❥❡❝t ①♠❧♥s❂✧❤tt♣✿✴✴♠❛✈❡♥✳❛♣❛❝❤❡✳♦r❣✴P❖▼✴✹✳✵✳✵✧
    ①♠❧♥s✿①s✐❂✧❤tt♣✿✴✴✇✇✇✳✇✸✳♦r❣✴✷✵✵✶✴❳▼▲❙❝❤❡♠❛✲✐♥st❛♥❝❡✧
    ①s✐✿s❝❤❡♠❛▲♦❝❛t✐♦♥❂✧❤tt♣✿✴✴♠❛✈❡♥✳❛♣❛❝❤❡✳♦r❣✴P❖▼✴✹✳✵✳✵
        ❤tt♣✿✴✴♠❛✈❡♥✳❛♣❛❝❤❡✳♦r❣✴①s❞✴♠❛✈❡♥✲✹✳✵✳✵✳①s❞✧❃

  ❁♠♦❞❡❧❱❡rs✐♦♥❃✹✳✵✳✵❁✴♠♦❞❡❧❱❡rs✐♦♥❃
  ❁❣r♦✉♣■❞❃❜r✳❝♦♠✳❝❛s❛❞♦❝♦❞✐❣♦❁✴❣r♦✉♣■❞❃
  ❁❛rt✐❢❛❝t■❞❃❧✐✈r❛r✐❛✲❢①❁✴❛rt✐❢❛❝t■❞❃
  ❁✈❡rs✐♦♥❃✵✳✵✳✶✲❙◆❆P❙❍❖❚❁✴✈❡rs✐♦♥❃

  ❁❜✉✐❧❞❃
    ❁s♦✉r❝❡❉✐r❡❝t♦r②❃sr❝❁✴s♦✉r❝❡❉✐r❡❝t♦r②❃

      ❁r❡s♦✉r❝❡s❃
        ❁r❡s♦✉r❝❡❃
          ❁❞✐r❡❝t♦r②❃sr❝❁✴❞✐r❡❝t♦r②❃
          ❁❡①❝❧✉❞❡s❃
            ❁❡①❝❧✉❞❡❃✯✯✴✯✳❥❛✈❛❁✴❡①❝❧✉❞❡❃

150


[PAGINA 161]
Casa do Código                                     Capítulo 7. JAR, bibliotecas e build



         ❁✴❡①❝❧✉❞❡s❃
       ❁✴r❡s♦✉r❝❡❃
     ❁✴r❡s♦✉r❝❡s❃

     ❁♣❧✉❣✐♥s❃
       ❁♣❧✉❣✐♥❃
         ❁❛rt✐❢❛❝t■❞❃♠❛✈❡♥✲❝♦♠♣✐❧❡r✲♣❧✉❣✐♥❁✴❛rt✐❢❛❝t■❞❃
         ❁✈❡rs✐♦♥❃✸✳✶❁✴✈❡rs✐♦♥❃
         ❁❝♦♥❢✐❣✉r❛t✐♦♥❃
           ❁s♦✉r❝❡❃✶✳✽❁✴s♦✉r❝❡❃
           ❁t❛r❣❡t❃✶✳✽❁✴t❛r❣❡t❃
         ❁✴❝♦♥❢✐❣✉r❛t✐♦♥❃
       ❁✴♣❧✉❣✐♥❃
     ❁✴♣❧✉❣✐♥s❃

  ❁✴❜✉✐❧❞❃
❁✴♣r♦❥❡❝t❃

    Ao abrir o arquivo pela primeira vez, o Eclipse provavelmente mostrará
apenas a página de Overview. Para ver o conteúdo deste XML, você pode clicar
na aba pom.xml que fica visível no rodapé do editor:




   Não se preocupe em entender cada detalhe deste XML de configuração
agora, mas note que ele já tem algumas informações essenciais de nosso build.
Nossa app agora já é um projeto Maven. Bem simples, não acha?


7.8 Adicionando as dependências com Maven
Agora que já estamos trabalhando com Maven, podemos deixar o controle
das bibliotecas que temos em nosso projeto com ele. Ele será o responsável
pelo gerenciamento de nossas dependências.


                                                                                   151


[PAGINA 162]
7.8. Adicionando as dependências com Maven                   Casa do Código


    Atualmente nosso projeto tem apenas duas: o driver de conexão com
MySQL e a base do projeto da livraria, onde se encontra a interface Produto
e suas implementações.
    Para começar, vamos remover esses dois elementos de nosso classpath.
Faremos isso clicando com o botão direito no projeto, opção Build Path e
Configure Build Path.
    Na aba Library, clicamos no mysql-connector-java.jar e em
Remove.




   Em seguida, faremos o mesmo com o projeto livraria-base, na aba
Project:




152


[PAGINA 163]
Casa do Código                                       Capítulo 7. JAR, bibliotecas e build




    Ao clicar em Ok, o projeto já deve parar de compilar, afinal essas bibliote-
cas são necessárias. Vamos agora abrir o arquivo pom.xml e declarar essas
duas dependências lá:

❁✦✲✲ ✐♥✐❝✐♦ ❞♦ ❛rq✉✐✈♦ ♦♠✐t✐❞♦ ✲✲❃
❁❞❡♣❡♥❞❡♥❝✐❡s❃
    ❁❞❡♣❡♥❞❡♥❝②❃
        ❁❣r♦✉♣■❞❃❜r✳❝♦♠✳❝❛❡❧✉♠✳❧✐✈r❛r✐❛❁✴❣r♦✉♣■❞❃
        ❁❛rt✐❢❛❝t■❞❃❧✐✈r❛r✐❛✲❜❛s❡❁✴❛rt✐❢❛❝t■❞❃
        ❁✈❡rs✐♦♥❃✶✳✵✳✵✲❙◆❆P❙❍❖❚❁✴✈❡rs✐♦♥❃
    ❁✴❞❡♣❡♥❞❡♥❝②❃
    ❁❞❡♣❡♥❞❡♥❝②❃
        ❁❣r♦✉♣■❞❃♠②sq❧❁✴❣r♦✉♣■❞❃
        ❁❛rt✐❢❛❝t■❞❃♠②sq❧✲❝♦♥♥❡❝t♦r✲❥❛✈❛❁✴❛rt✐❢❛❝t■❞❃
        ❁✈❡rs✐♦♥❃✺✳✶✳✸✹❁✴✈❡rs✐♦♥❃
    ❁✴❞❡♣❡♥❞❡♥❝②❃
❁✴❞❡♣❡♥❞❡♥❝✐❡s❃

                                                                                     153


[PAGINA 164]
7.8. Adicionando as dependências com Maven                  Casa do Código


❁✴♣r♦❥❡❝t❃

      Note que para fazer isso só precisamos adicionar uma tag chamada
dependencies, e para cada dependência uma nova tag dependency com
a seguinte estrutura:

❁❞❡♣❡♥❞❡♥❝②❃
    ❁❣r♦✉♣■❞❃ ❱❆▲❖❘❴❆◗❯■ ❁✴❣r♦✉♣■❞❃
    ❁❛rt✐❢❛❝t■❞❃ ❱❆▲❖❘❴❆◗❯■ ❁✴❛rt✐❢❛❝t■❞❃
    ❁✈❡rs✐♦♥❃ ❱❆▲❖❘❴❆◗❯■ ❁✴✈❡rs✐♦♥❃
❁✴❞❡♣❡♥❞❡♥❝②❃



 Adicionando pela interface do Eclipse

    Se preferir, você também pode adicionar novas dependências em seu
 projeto diretamente pela interface do Eclipse. Basta clicar em Maven e
 Add Dependency.




    Dessa forma, você não precisa escrever nenhuma linha de XML, ele
 fará esse trabalho para você.


154


[PAGINA 165]
Casa do Código                                     Capítulo 7. JAR, bibliotecas e build



   Vamos ver se tudo funcionou? Basta clicar com o botão direto no projeto,
Maven e escolher Update Project... (ou pressionar o atalho Alt + F5).




    Feito isso, a ferramenta fará seu trabalho e o projeto deve voltar a com-
pilar. Note que as dependências ficam visíveis em Maven Dependencies,
direto pelo package explorer:




                                                                                   155


[PAGINA 166]
7.8. Adicionando as dependências com Maven         Casa do Código




Buscando por dependências no Maven
   Assim como o mysql-connector-java, você pode encontrar qual-
quer outra dependência necessária pra seus projetos no site:
   http://search.maven.org/




156


[PAGINA 167]
Casa do Código                                     Capítulo 7. JAR, bibliotecas e build




   Basta clicar na versão que quer utilizar e copiar a tag da dependência para
dentro do arquivo pom.xml de seu projeto.




7.9    Executando algumas tasks do Maven
Vamos agora ver o build do Maven em prática? Na opção Run As..., cli-
cando com o botão direito no projeto, escolha Maven Build.


                                                                                  157


[PAGINA 168]
7.9. Executando algumas tasks do Maven                     Casa do Código




      Adicione no campo Goals as opções:
      • compile package




    Essas são algumas das tasks padrões do Maven. Como o próprio nome já
diz, estamos dizendo que queremos compilar e empacotar, gerar um JAR do
projeto. Se você quiser, pode ler mais sobre esses Goals em:

158


[PAGINA 169]
Casa do Código                                     Capítulo 7. JAR, bibliotecas e build



    http://maven.apache.org/guides/introduction/
introduction-to-the-lifecycle.html
    Ao executar, a saída será parecida com:

❬■◆❋❖❪ ❙❝❛♥♥✐♥❣ ❢♦r ♣r♦❥❡❝ts✳✳✳
❬■◆❋❖❪
✳✳✳
❬■◆❋❖❪ ✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲
❬■◆❋❖❪ ❇✉✐❧❞✐♥❣ ❧✐✈r❛r✐❛✲❢① ✵✳✵✳✶✲❙◆❆P❙❍❖❚
❬■◆❋❖❪ ✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲
❬■◆❋❖❪
✳✳✳
❬■◆❋❖❪ ❇✉✐❧❞✐♥❣ ❥❛r✿ ✴❯s❡rs✴t✉r✐♥✐✴❉♦❝✉♠❡♥ts✴✇♦r❦s♣❛❝❡
    ✴❧✐✈r❛r✐❛✲❢①✴t❛r❣❡t✴❧✐✈r❛r✐❛✲❢①✲✵✳✵✳✶✲❙◆❆P❙❍❖❚✳❥❛r
❬■◆❋❖❪ ✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲
❬■◆❋❖❪ ❇❯■▲❉ ❙❯❈❈❊❙❙
❬■◆❋❖❪ ✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲
❬■◆❋❖❪ ❚♦t❛❧ t✐♠❡✿ ✼✳✶✷✾ s
❬■◆❋❖❪ ❋✐♥✐s❤❡❞ ❛t✿ ✷✵✶✹✲✶✶✲✷✷❚✷✵✿✶✹✿✹✼✲✵✸✿✵✵
❬■◆❋❖❪ ❋✐♥❛❧ ▼❡♠♦r②✿ ✽▼✴✾✹▼
❬■◆❋❖❪ ✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲

    Sucesso! O build foi concluído sem nenhuma falha. Note que o JAR foi
criado dentro de uma pasta chamada target, esse é o destino padrão da
ferramenta.
    Mas esse JAR não é um executável! Precisamos deixar claro ao Maven
que esse é um projeto Java FX. Como fazer isso?


7.10    Adicionando plugin do Java FX
Como um extra, ensinaremos ao Maven como gerar um JAR executável do
Java FX. Só de pensar parece trabalhoso, não é? Mas na verdade isso tudo já
está pronto, existem diversos plugins que nos auxiliam nesse trabalho. Uma
opção bastante utilizada é o javafx-maven-plugin.
    Da mesma forma como fizemos para adicionar uma dependência, pode-
mos abrir o arquivo pom.xml e adicionar as seguintes linhas do plugin, logo
após o maven-compiler-plugin que já está declarado:

                                                                                  159


[PAGINA 170]
7.10. Adicionando plugin do Java FX                          Casa do Código


❁♣❧✉❣✐♥s❃
    ❁✦✲✲ ♠❛✈❡♥✲❝♦♠♣✐❧❡r✲♣❧✉❣✐♥ ♦♠✐t✐❞♦ ✲✲❃
    ❁♣❧✉❣✐♥❃
        ❁❣r♦✉♣■❞❃❝♦♠✳③❡♥❥❛✈❛❁✴❣r♦✉♣■❞❃
        ❁❛rt✐❢❛❝t■❞❃❥❛✈❛❢①✲♠❛✈❡♥✲♣❧✉❣✐♥❁✴❛rt✐❢❛❝t■❞❃
        ❁✈❡rs✐♦♥❃✽✳✶✳✷❁✴✈❡rs✐♦♥❃
        ❁❝♦♥❢✐❣✉r❛t✐♦♥❃
            ❁♠❛✐♥❈❧❛ss❃❛♣♣❧✐❝❛t✐♦♥✳▼❛✐♥❁✴♠❛✐♥❈❧❛ss❃
        ❁✴❝♦♥❢✐❣✉r❛t✐♦♥❃
    ❁✴♣❧✉❣✐♥❃
❁✴♣❧✉❣✐♥s❃

    Observe que estamos definindo que a classe application.Main é a
classe principal de nossa aplicação. Além disso, precisamos adicionar a tag
organization como a seguir:

❁♦r❣❛♥✐③❛t✐♦♥❃
    ❁♥❛♠❡❃❈❛s❛ ❞♦ ❈ó❞✐❣♦❁✴♥❛♠❡❃
❁✴♦r❣❛♥✐③❛t✐♦♥❃

    Tudo pronto! Já podemos usar uma de suas tasks. Para gerar um JAR
executável, por exemplo, você pode clicar em Run As..., Maven Build
e em Goals adicionar o valor jfx:jar.




160


[PAGINA 171]
Casa do Código                                   Capítulo 7. JAR, bibliotecas e build




    Ao clicar em Run, o resultado será parecido com:

❬■◆❋❖❪ ❙❝❛♥♥✐♥❣ ❢♦r ♣r♦❥❡❝ts✳✳✳
✳✳✳
❬■◆❋❖❪ ❇✉✐❧❞✐♥❣ ❏❛✈❛ ❋❳ ❏❆❘ ❢♦r ❛♣♣❧✐❝❛t✐♦♥
❬■◆❋❖❪ ❆❞❞✐♥❣ ✬❞❡♣❧♦②✬ ❞✐r❡❝t♦r② t♦ ▼♦❥♦
   ❝❧❛ss♣❛t❤✿ ✴❯s❡rs✴t✉r✐♥✐✴❉♦❝✉♠❡♥ts
   ✴✇♦r❦s♣❛❝❡✴❧✐✈r❛r✐❛✲❢①✴sr❝✴♠❛✐♥✴❞❡♣❧♦②
❬■◆❋❖❪ ✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲
❬■◆❋❖❪ ❇❯■▲❉ ❙❯❈❈❊❙❙
❬■◆❋❖❪ ✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲
❬■◆❋❖❪ ❚♦t❛❧ t✐♠❡✿ ✻✳✼✾✸ s
❬■◆❋❖❪ ❋✐♥✐s❤❡❞ ❛t✿ ✷✵✶✹✲✶✶✲✷✷❚✷✵✿✸✻✿✶✵✲✵✸✿✵✵
❬■◆❋❖❪ ❋✐♥❛❧ ▼❡♠♦r②✿ ✾▼✴✾✸▼
❬■◆❋❖❪ ✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲✲

    Note que o arquivo JAR foi gerado dentro da pasta target, no subdi-
retório jfx/app:



                                                                                161


[PAGINA 172]
7.10. Adicionando plugin do Java FX                             Casa do Código




    Se quiser, teste para verificar que ele foi criado corretamente. Para isso,
basta digitar o comando:

❥❛✈❛ ✲❥❛r t❛r❣❡t✴❥❢①✴❛♣♣✴❧✐✈r❛r✐❛✲❢①✲✵✳✵✳✶✲❙◆❆P❙❍❖❚✲❥❢①✳❥❛r

   Perfeito, tudo está funcionando. Mas isso foi um pouco trabalhoso, não
acha? Para nossa sorte, o plugin de Java FX já tem uma task que cria e executa
o JAR de nossa aplicação automaticamente! Para utilizá-la, clique novamente
em Run As..., Maven Build.... No campo Goals adicione jfx:run:




162


[PAGINA 173]
Casa do Código                                      Capítulo 7. JAR, bibliotecas e build




    Agora basta clicar em Run e a app será executada a partir do JAR criado
pelo plugin.


  Conhecendo mais alguns plugins

     Além do plugin de Java FX que utilizamos, existem mais centenas de
  plugins que facilitam bastante o nosso trabalho. Você pode ver uma lista
  com alguns dos plugins existentes em:
     http://maven.apache.org/plugins/index.html


7.11    Maven na linha de comando
Vimos que é possível executar as metas do Maven diretamente pelo Eclipse,
mas comumente esse trabalho é feito diretamente pela linha de comando. Se
você quiser testar, basta abrir a pasta do seu projeto pelo terminal e executar
a instrução mvn com as metas que você quiser. Por exemplo:
♠✈♥ ❥❢①✿r✉♥

                                                                                   163


[PAGINA 174]
7.11. Maven na linha de comando                                Casa do Código


    Note que o resultado será o mesmo, um JAR executável de nossa app será
criado e executado. Você pode executar uma série de comandos de uma só
vez, basta separá-los por um espaço, como a seguir:

♠✈♥ ❝❧❡❛♥ ❥❢①✿r✉♥

    A primeira meta executada, o clean, é utilizada para limpar os arquivos
e diretórios gerados pelo Maven na pasta target. Esse comando, portanto,
limpa a pasta target e logo em seguida executa o jfx:run responsável
por gerar e executar o JAR do projeto.
    Algumas das metas mais comuns do Maven são:

      • compile compila o código-fonte do projeto

      • test compila e executa seus testes de unidade existentes no projeto

      • package empacota (gera o JAR, por exemplo) do código compilado
        de seu projeto

      • validate valida se o projeto tem todas as informações necessárias
        para seu funcionamento

      • install instala localmente seu projeto

     Se você estiver interessado, pode conhecer um pouco mais sobre as pos-
sibilidades do Maven em:
     http://maven.apache.org/general.html




164


[PAGINA 175]
Casa do Código                                    Capítulo 7. JAR, bibliotecas e build




  Outra opção: ANT e Ivy

     Outra opção bastante conhecida e utilizada no mercado é o Ant, tam-
  bém da Apache. Ele cuida apenas do processo de build. Para o gerencia-
  mento de dependências você pode contar com outro framework bastante
  conhecido, o Ivy. Esses dois trabalham bem juntos e têm suas vantagens
  e desvantagens, assim como qualquer outra ferramenta. Há quem prefira
  usá-los no lugar do Maven. Interessado em saber mais sobre Ant e Ivy?
  A documentação deles pode ajudar bastante, elas estão disponíveis nos
  links:

      • http://ant.apache.org/manual/index.html

      • http://ant.apache.org/ivy/




7.12 Como ficou nosso pom.xml
Após as alterações, nosso arquivo pom.xml ficou assim:

❁♣r♦❥❡❝t ①♠❧♥s❂✧❤tt♣✿✴✴♠❛✈❡♥✳❛♣❛❝❤❡✳♦r❣✴P❖▼✴✹✳✵✳✵✧
    ①♠❧♥s✿①s✐❂✧❤tt♣✿✴✴✇✇✇✳✇✸✳♦r❣✴✷✵✵✶✴❳▼▲❙❝❤❡♠❛✲✐♥st❛♥❝❡✧
    ①s✐✿s❝❤❡♠❛▲♦❝❛t✐♦♥❂✧❤tt♣✿✴✴♠❛✈❡♥✳❛♣❛❝❤❡✳♦r❣✴P❖▼✴✹✳✵✳✵
        ❤tt♣✿✴✴♠❛✈❡♥✳❛♣❛❝❤❡✳♦r❣✴①s❞✴♠❛✈❡♥✲✹✳✵✳✵✳①s❞✧❃

     ❁♠♦❞❡❧❱❡rs✐♦♥❃✹✳✵✳✵❁✴♠♦❞❡❧❱❡rs✐♦♥❃
     ❁❣r♦✉♣■❞❃❧✐✈r❛r✐❛✲❢①❁✴❣r♦✉♣■❞❃
     ❁❛rt✐❢❛❝t■❞❃❧✐✈r❛r✐❛✲❢①❁✴❛rt✐❢❛❝t■❞❃
     ❁✈❡rs✐♦♥❃✵✳✵✳✶✲❙◆❆P❙❍❖❚❁✴✈❡rs✐♦♥❃

     ❁♦r❣❛♥✐③❛t✐♦♥❃
         ❁♥❛♠❡❃❈❛s❛ ❞♦ ❈ó❞✐❣♦❁✴♥❛♠❡❃
     ❁✴♦r❣❛♥✐③❛t✐♦♥❃

     ❁❜✉✐❧❞❃
         ❁s♦✉r❝❡❉✐r❡❝t♦r②❃sr❝❁✴s♦✉r❝❡❉✐r❡❝t♦r②❃

                                                                                 165


[PAGINA 176]
7.12. Como ficou nosso pom.xml                        Casa do Código


          ❁r❡s♦✉r❝❡s❃
              ❁r❡s♦✉r❝❡❃
                  ❁❞✐r❡❝t♦r②❃sr❝❁✴❞✐r❡❝t♦r②❃
                  ❁❡①❝❧✉❞❡s❃
                      ❁❡①❝❧✉❞❡❃✯✯✴✯✳❥❛✈❛❁✴❡①❝❧✉❞❡❃
                  ❁✴❡①❝❧✉❞❡s❃
              ❁✴r❡s♦✉r❝❡❃
          ❁✴r❡s♦✉r❝❡s❃
          ❁♣❧✉❣✐♥s❃
              ❁♣❧✉❣✐♥❃
                  ❁❛rt✐❢❛❝t■❞❃♠❛✈❡♥✲❝♦♠♣✐❧❡r✲♣❧✉❣✐♥❁✴❛rt✐❢❛❝t■❞❃
                  ❁✈❡rs✐♦♥❃✸✳✶❁✴✈❡rs✐♦♥❃
                  ❁❝♦♥❢✐❣✉r❛t✐♦♥❃
                      ❁s♦✉r❝❡❃✶✳✽❁✴s♦✉r❝❡❃
                      ❁t❛r❣❡t❃✶✳✽❁✴t❛r❣❡t❃
                  ❁✴❝♦♥❢✐❣✉r❛t✐♦♥❃
              ❁✴♣❧✉❣✐♥❃
              ❁♣❧✉❣✐♥❃
                  ❁❣r♦✉♣■❞❃❝♦♠✳③❡♥❥❛✈❛❁✴❣r♦✉♣■❞❃
                  ❁❛rt✐❢❛❝t■❞❃❥❛✈❛❢①✲♠❛✈❡♥✲♣❧✉❣✐♥❁✴❛rt✐❢❛❝t■❞❃
                  ❁✈❡rs✐♦♥❃✽✳✶✳✷❁✴✈❡rs✐♦♥❃
                  ❁❝♦♥❢✐❣✉r❛t✐♦♥❃
                      ❁♠❛✐♥❈❧❛ss❃❛♣♣❧✐❝❛t✐♦♥✳▼❛✐♥❁✴♠❛✐♥❈❧❛ss❃
                  ❁✴❝♦♥❢✐❣✉r❛t✐♦♥❃
              ❁✴♣❧✉❣✐♥❃
          ❁✴♣❧✉❣✐♥s❃
      ❁✴❜✉✐❧❞❃
      ❁r❡♣♦rt✐♥❣❃
          ❁♣❧✉❣✐♥s❃
              ❁♣❧✉❣✐♥❃
                  ❁❣r♦✉♣■❞❃♦r❣✳❛♣❛❝❤❡✳♠❛✈❡♥✳♣❧✉❣✐♥s❁✴❣r♦✉♣■❞❃
                  ❁❛rt✐❢❛❝t■❞❃♠❛✈❡♥✲♣❧✉❣✐♥✲♣❧✉❣✐♥❁✴❛rt✐❢❛❝t■❞❃
                  ❁✈❡rs✐♦♥❃✸✳✷❁✴✈❡rs✐♦♥❃
              ❁✴♣❧✉❣✐♥❃
          ❁✴♣❧✉❣✐♥s❃
      ❁✴r❡♣♦rt✐♥❣❃
      ❁❞❡♣❡♥❞❡♥❝✐❡s❃
          ❁❞❡♣❡♥❞❡♥❝②❃
              ❁❣r♦✉♣■❞❃❜r✳❝♦♠✳❝❛❡❧✉♠✳❧✐✈r❛r✐❛❁✴❣r♦✉♣■❞❃

166


[PAGINA 177]
Casa do Código                                  Capítulo 7. JAR, bibliotecas e build



            ❁❛rt✐❢❛❝t■❞❃❧✐✈r❛r✐❛✲❜❛s❡❁✴❛rt✐❢❛❝t■❞❃
            ❁✈❡rs✐♦♥❃✶✳✵✳✵✲❙◆❆P❙❍❖❚❁✴✈❡rs✐♦♥❃
        ❁✴❞❡♣❡♥❞❡♥❝②❃
        ❁❞❡♣❡♥❞❡♥❝②❃
            ❁❣r♦✉♣■❞❃♠②sq❧❁✴❣r♦✉♣■❞❃
            ❁❛rt✐❢❛❝t■❞❃♠②sq❧✲❝♦♥♥❡❝t♦r✲❥❛✈❛❁✴❛rt✐❢❛❝t■❞❃
            ❁✈❡rs✐♦♥❃✺✳✶✳✸✹❁✴✈❡rs✐♦♥❃
        ❁✴❞❡♣❡♥❞❡♥❝②❃
    ❁✴❞❡♣❡♥❞❡♥❝✐❡s❃
❁✴♣r♦❥❡❝t❃

    É natural não reagir tão bem ao ver um arquivo xml com tantas in-
formações, mas após usar a ferramenta por alguns instantes você logo deve
perceber que não é nada de tão complicado. Atualizar suas dependências
nunca foi tão fácil, além de que podemos fazer o build completo de nossa
aplicação com apenas um comando.




                                                                               167


[PAGINA 178]


[PAGINA 179]
Capítulo 8

Refatorações
“Refatoração é uma técnica controlada para reestruturar um trecho de código
existente, alterando sua estrutura interna sem modificar seu comportamento
externo. Consiste em uma série de pequenas transformações que preservam o
comportamento inicial. Cada transformação (chamada de refatoração) reflete
em uma pequena mudança, mas uma sequência de transformações pode
produzir uma significante reestruturação. Como cada refatoração é pequena, é
menos provável que se introduza um erro. Além disso, o sistema continua em
pleno funcionamento depois de cada pequena refatoração, reduzindo as
chances de o sistema ser seriamente danificado durante a reestruturação.
– Martin Fowler

    Essa ideia de utilizar pequenas transformações para melhorar a qualidade
do nosso código recebe o nome de baby steps (passos de bebê). Essa é uma
prática fundamental, utilizada para melhorar a legibilidade, clareza e design


[PAGINA 180]
8.1. Refatoração                                                Casa do Código


de nosso código. Sempre que for fazer uma refatoração, evite mudar tudo
de uma só vez. Caso algum erro apareça, será muito mais difícil identificar
qual das mudanças foi a responsável pelo erro (ou bug, como normalmente
chamamos).
    Neste capítulo, vamos fazer pequenas refatorações em nosso código, bus-
cando melhorar a legibilidade, evitar repetições e, com isso, aumentar a qual-
idade e manutenibilidade de nosso projeto. Além disso, relembraremos algu-
mas das boas práticas e design patterns que vimos ao decorrer do livro. Pronto
para começar?


8.1      Refatoração
Logo que começamos a trabalhar com a tabela de Produtos, você deve ter
percebido que o Eclipse mostrou vários warnings. Inclusive, usamos a ano-
tação @SuppressWarnings para silenciar esses alertas, mas por que eles
estão acontecendo?




      Olhando com cuidado para a mensagem, temos a informação:
❚❛❜❧❡❈♦❧✉♠♥ ✐s ❛ r❛✇ t②♣❡✳ ❘❡❢❡r❡♥❝❡s t♦ ❣❡♥❡r✐❝
    t②♣❡ ❚❛❜❧❡❈♦❧✉♠♥❁❙✱❚❃ s❤♦✉❧❞ ❜❡ ♣❛r❛♠❡t❡r✐③❡❞

    Em outras palavras, não estamos informando os parâmetros genéricos da
classe TableColumn. Idealmente, no lugar de fazer:
❚❛❜❧❡❈♦❧✉♠♥ ♥♦♠❡❈♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭✧◆♦♠❡✧✮❀

♥♦♠❡❈♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭✶✽✵✮❀

♥♦♠❡❈♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
        ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②✭✧♥♦♠❡✧✮✮❀

170


[PAGINA 181]
Casa do Código                                          Capítulo 8. Refatorações



    Seria necessário fazer assim:

❚❛❜❧❡❈♦❧✉♠♥❁Pr♦❞✉t♦✱ ❙tr✐♥❣❃ ♥♦♠❡❈♦❧✉♠♥ ❂
        ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥❁Pr♦❞✉t♦✱ ❙tr✐♥❣❃✭✧◆♦♠❡✧✮❀

♥♦♠❡❈♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭✶✽✵✮❀

♥♦♠❡❈♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
    ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②❁Pr♦❞✉t♦✱ ❙tr✐♥❣❃✭✧♥♦♠❡✧✮✮❀

    Veja que agora estamos definindo a classe TableColumn passando o
Produto, que é o tipo do objeto que está sendo manipulado, mais a String,
que é o tipo do conteúdo no campo da tabela. Mas o código ficou muito
mais verboso, não acha? Por isso, desde o início optamos por não passar o
parâmetro genérico, apesar das centenas de warnings.
    Outro problema nessa parte do código está na quantidade de repetições.
Observe que grande parte do código está idêntico, para cada coluna:

❚❛❜❧❡❱✐❡✇❁Pr♦❞✉t♦❃ t❛❜❧❡❱✐❡✇ ❂ ♥❡✇ ❚❛❜❧❡❱✐❡✇❁❃✭♣r♦❞✉t♦s✮❀

❚❛❜❧❡❈♦❧✉♠♥ ♥♦♠❡❈♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭✧◆♦♠❡✧✮❀
♥♦♠❡❈♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭✶✽✵✮❀
♥♦♠❡❈♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
    ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②✭✧♥♦♠❡✧✮✮❀

❚❛❜❧❡❈♦❧✉♠♥ ❞❡s❝❈♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭✧❉❡s❝r✐çã♦✧✮❀
❞❡s❝❈♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭✷✸✵✮❀
❞❡s❝❈♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
    ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②✭✧❞❡s❝r✐❝❛♦✧✮✮❀

❚❛❜❧❡❈♦❧✉♠♥ ✈❛❧♦r❈♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭✧❱❛❧♦r✧✮❀
✈❛❧♦r❈♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭✻✵✮❀
✈❛❧♦r❈♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
    ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②✭✧✈❛❧♦r✧✮✮❀

❚❛❜❧❡❈♦❧✉♠♥ ✐s❜♥❈♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭✧■❙❇◆✧✮❀
✐s❜♥❈♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭✶✽✵✮❀
✐s❜♥❈♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
    ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②✭✧✐s❜♥✧✮✮❀

                                                                            171


[PAGINA 182]
8.1. Refatoração                                              Casa do Código




t❛❜❧❡❱✐❡✇✳❣❡t❈♦❧✉♠♥s✭✮✳❛❞❞❆❧❧✭♥♦♠❡❈♦❧✉♠♥✱ ❞❡s❝❈♦❧✉♠♥✱
    ✈❛❧♦r❈♦❧✉♠♥✱ ✐s❜♥❈♦❧✉♠♥✮❀

    Seguindo as boas práticas da orientação a objetos, devemos isolar com-
portamentos repetidos em métodos. O ganho vai desde a reutilização, já que
ele poderá ser chamado várias vezes em nosso código, até em legibilidade, já
que podemos lhe dar um nome bastante significativo.
    Vamos fazer essa pequena refatoração em nosso código. O método
poderá ficar assim:

♣r✐✈❛t❡ ❚❛❜❧❡❈♦❧✉♠♥ ❝r✐❛❈♦❧✉♥❛✭❙tr✐♥❣ t✐t✉❧♦✱
        ✐♥t ❧❛r❣✉r❛✱ ❙tr✐♥❣ ❛tr✐❜✉t♦✮ ④

      ❚❛❜❧❡❈♦❧✉♠♥ ❝♦❧✉♠♥ ❂ ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥✭t✐t✉❧♦✮❀
      ❝♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭❧❛r❣✉r❛✮❀
      ❝♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
              ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②✭❛tr✐❜✉t♦✮✮❀

      r❡t✉r♥ ❝♦❧✉♠♥❀
⑥




172


[PAGINA 183]
Casa do Código                                          Capítulo 8. Refatorações




 Usando Extract Method do Eclipse

    Experimente selecionar o trecho de código que você quer extrair e
 pressionar as teclas de atalho Control + Shift + M.




     Basta digitar o nome do método que você quer criar e pronto!


    Apesar de simples, essa pequena mudança já dá uma cara bem melhor
para nosso código. Ele ficou assim:

❚❛❜❧❡❱✐❡✇❁Pr♦❞✉t♦❃ t❛❜❧❡❱✐❡✇ ❂ ♥❡✇ ❚❛❜❧❡❱✐❡✇❁❃✭♣r♦❞✉t♦s✮❀

❚❛❜❧❡❈♦❧✉♠♥ ♥♦♠❡❈♦❧✉♠♥ ❂ ❝r✐❛❈♦❧✉♥❛✭✧◆♦♠❡✧✱ ✶✽✵✱ ✧♥♦♠❡✧✮❀
❚❛❜❧❡❈♦❧✉♠♥ ❞❡s❝❈♦❧✉♠♥ ❂
    ❝r✐❛❈♦❧✉♥❛✭✧❉❡s❝r✐çã♦✧✱ ✷✸✵✱ ✧❞❡s❝r✐❝❛♦✧✮❀
❚❛❜❧❡❈♦❧✉♠♥ ✈❛❧♦r❈♦❧✉♠♥ ❂ ❝r✐❛❈♦❧✉♥❛✭✧❱❛❧♦r✧✱ ✻✵✱ ✧✈❛❧♦r✧✮❀
❚❛❜❧❡❈♦❧✉♠♥ ✐s❜♥❈♦❧✉♠♥ ❂ ❝r✐❛❈♦❧✉♥❛✭✧■❙❇◆✧✱ ✶✽✵✱ ✧✐s❜♥✧✮❀

                                                                            173


[PAGINA 184]
8.1. Refatoração                                                Casa do Código




t❛❜❧❡❱✐❡✇✳❣❡t❈♦❧✉♠♥s✭✮✳❛❞❞❆❧❧✭♥♦♠❡❈♦❧✉♠♥✱ ❞❡s❝❈♦❧✉♠♥✱
    ✈❛❧♦r❈♦❧✉♠♥✱ ✐s❜♥❈♦❧✉♠♥✮❀

    Além disso, agora que ele está isolado, podemos até adicionar os parâmet-
ros genéricos sem sentir tanto o custo de legibilidade. O método ficará assim:

♣r✐✈❛t❡ ❚❛❜❧❡❈♦❧✉♠♥❁Pr♦❞✉t♦✱ ❙tr✐♥❣❃ ❝r✐❛❈♦❧✉♥❛✭❙tr✐♥❣ t✐t✉❧♦✱
        ✐♥t ❧❛r❣✉r❛✱ ❙tr✐♥❣ ❛tr✐❜✉t♦✮ ④

      ❚❛❜❧❡❈♦❧✉♠♥❁Pr♦❞✉t♦✱ ❙tr✐♥❣❃ ❝♦❧✉♠♥ ❂
              ♥❡✇ ❚❛❜❧❡❈♦❧✉♠♥❁Pr♦❞✉t♦✱ ❙tr✐♥❣❃✭t✐t✉❧♦✮❀
      ❝♦❧✉♠♥✳s❡t▼✐♥❲✐❞t❤✭❧❛r❣✉r❛✮❀

      ❝♦❧✉♠♥✳s❡t❈❡❧❧❱❛❧✉❡❋❛❝t♦r②✭
          ♥❡✇ Pr♦♣❡rt②❱❛❧✉❡❋❛❝t♦r②❁Pr♦❞✉t♦✱ ❙tr✐♥❣❃✭❛tr✐❜✉t♦✮✮❀

      r❡t✉r♥ ❝♦❧✉♠♥❀
⑥

Outras formas de refatoração
    A extração de métodos é apenas um dos muitos tipos de refatorações.
Renomear variáveis, classes e métodos também faz bastante diferença em
nosso código, quanto mais claro for o nome, mais fácil será entender o al-
goritmo. Extrair variáveis é um outro tipo bastante comum e recomendado.
    O Eclipse ajuda bastante nesse trabalho, há uma diversidade bem grande
de atalhos para refatoração. A princípio, você não precisa decorar cada um
desses atalhos, basta se lembrar do Alt + Shift + T. Ele mostra as possíveis
refatorações para um determinado trecho de código. Por exemplo, ao usá-lo
em uma classe:




174


[PAGINA 185]
Casa do Código                                             Capítulo 8. Refatorações




    Observe que algumas das sugestões são: renomear a classe, mover para
outro pacote, extrair uma interface, entre diversas outras.

Desafio: mais e mais refatorações
    As mudanças que fizemos aqui são bastante simples, meu objetivo foi
mostrar o quanto isso pode significar em nosso código. Daqui para frente é
com você. Que outras transformações poderiam melhorar esse projeto? Passe
um tempo pesquisando a respeito, com toda certeza vai valer a pena. Vale
lembrar que existem refatorações bem mais complexas, que afetam diversas
partes de nossa aplicação e até mesmo a sua arquitetura.


8.2 Os tão populares Design Patterns
Não é à toa que eles são populares, vale muito a pena entender e aplicar esses
conceitos sempre que for possível em nossos projetos. E isso não muda de-
pendendo da linguagem ou tecnologia que você estiver utilizando, o que
torna a ideia ainda mais interessante.
    Design Patterns é um assunto muito extenso, precisaríamos de pelo menos

                                                                               175


[PAGINA 186]
8.2. Os tão populares Design Patterns                             Casa do Código


mais umas 200 páginas pra nos aprofundar nisso. Mas mesmo assim eu tentei
mostrar aqui alguns dos mais fundamentais para nosso dia a dia desenvol-
vendo em Java. Relembrando alguns deles:

      • Factory Method: você não quer deixar o código de criação de um
        objeto complicado espalhado por aí. Podemos estar falando de uma
        Connection do JDBC, como vimos no exemplo passado, ou qualquer
        outro. Ele não se limita a uma tecnologia específica. Nosso código ficou
        assim:

        ♣✉❜❧✐❝ ❝❧❛ss ❈♦♥♥❡❝t✐♦♥❋❛❝t♦r② ④

            ♣✉❜❧✐❝ ❈♦♥♥❡❝t✐♦♥ ❣❡t❈♦♥♥❡❝t✐♦♥✭✮ ④
              ❙tr✐♥❣ ✉r❧ ❂ ✧❥❞❜❝✿♠②sq❧✿✴✴❧♦❝❛❧❤♦st✴❧✐✈r❛r✐❛✧❀
              tr② ④
                  r❡t✉r♥ ❉r✐✈❡r▼❛♥❛❣❡r✳❣❡t❈♦♥♥❡❝t✐♦♥✭✉r❧✱ ✧r♦♦t✧✱ ✧✧✮❀
              ⑥ ❝❛t❝❤ ✭❙◗▲❊①❝❡♣t✐♦♥ ❡✮ ④
                  t❤r♦✇ ♥❡✇ ❘✉♥t✐♠❡❊①❝❡♣t✐♦♥✭❡✮❀
              ⑥
            ⑥
        ⑥

        Quais as vantagens? Estamos encapsulando esse processo compli-
        cado que é criar uma conexão. Além disso, concentramos nossas in-
        formações de login, senha e nome do banco de dados em um único
        objeto. Se alguma dessas informações mudar, eu só preciso atualizar
        essa classe, um único ponto da minha aplicação e não os zilhares de
        lugares que acessam nosso banco.

      • DAO: a ideia desse pattern é criar uma camada especialista em acessar
        dados de nossos objetos. Não importa se ele está usando JDBC, Hi-
        bernate ou qualquer outra tecnologia. As regras do MySQL, Oracle ou
        qualquer outro banco de dados ficam encapsuladas. Note que encapsu-
        lamento é um dos pilares de quase todos os design patterns. No lugar
        de sair acessando o banco de dados diretamente pelas nossas classes,
        passamos sempre pela camada do DAO:


176


[PAGINA 187]
Casa do Código                                         Capítulo 8. Refatorações




             Fig. 8.4: Acesso a dados encapsulado em um DAO.



    • Template Method: apesar de não implementarmos esse pattern dire-
      tamente em nosso código, vimos ele em prática na API de IO do Java.
      InputStream ilustra esse exemplo, no fluxo de entrada. O fluxo é o
      mesmo, independente de onde vamos ler os bytes:




       Fig. 8.5: Método recebendo um InputStream como parâmetro.



    Esses são apenas alguns dos muitos que você provavelmente vai usar em
seu dia a dia. Mesmo que não saiba, muitas vezes isso acontece.




                                                                          177


[PAGINA 188]


[PAGINA 189]
Capítulo 9

Próximos passos com Java
É isso, espero que tenha aproveitado bastante o conteúdo. Foi uma longa jor-
nada, que para você talvez tenha começado no livro Desbravando Java e Ori-
entação a Objetos. Nos dois livros tentei apresentar todos os conceitos com
exemplos mão na massa e com um foco mais prático.
    Não pare por aqui, continue praticando! Tente sempre ir além com novos
testes e cenários além dos aqui propostos. Para mim, a prática é a forma mais
efetiva de aprender e fixar qualquer coisa.
    A partir daqui, você pode descobrir as muitas outras funcionalidades da
linguagem, assim como suas milhares de bibliotecas, explorar novas APIs etc.
Há muito mais o que explorar no ecossistema da plataforma Java.


[PAGINA 190]
9.1. Entre em contato conosco                                  Casa do Código


9.1      Entre em contato conosco
Não se esqueça de que você pode encaminhar suas dúvidas na lista que foi
criada especialmente para este livro. Não só dúvidas! As sugestões, críticas,
ideias e melhorias também são essenciais para nós:
    https://groups.google.com/group/livro-java




180
