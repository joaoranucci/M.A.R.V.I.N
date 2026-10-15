# DESBRAVANDO_JAVA_E_ORIENTACAO_A_OBJETOS

Arquivo original: more_papers_by_thyago_louiz/DESBRAVANDO_JAVA_E_ORIENTACAO_A_OBJETOS.pdf
SHA-256 do original: 914d13195a1408b1ce29dbc43b5be277351faee940ea080a4be169fd39ae54c1

Texto extraido para consulta. As paginas abaixo usam a ordem do arquivo PDF, incluindo capas.
Parte preparada: 1/1


[PAGINA 1]


[PAGINA 2]
    © Casa do Código
Todos os direitos reservados e protegidos pela Lei nº9.610, de
10/02/1998.
Nenhuma parte deste livro poderá ser reproduzida, nem transmitida, sem
autorização prévia por escrito da editora, sejam quais forem os meios:
fotográﬁcos, eletrônicos, mecânicos, gravação ou quaisquer outros.

    Casa do Código
Livros para o programador
Rua Vergueiro, 3185 - 8º andar
04101-300 – Vila Mariana – São Paulo – SP – Brasil


[PAGINA 3]
Casa do Código




“À minha esposa Jordana e ao maior presente que um dia sonhei receber, nossa
filha Katherine.”
– Rodrigo Turini




                                                                           i


[PAGINA 4]


[PAGINA 5]
Casa do Código




Agradecimentos

Não há outra maneira de começar este livro que não seja agradecendo a to-
dos que incentivaram e contribuíram direta ou indiretamente em sua edição.
Victor Harada, Maurício Aniche e Guilherme Silveira foram alguns deles.
    Fica um agradecimento especial ao Paulo Silveira, não só pela sua detal-
hada revisão e suas diversas sugestões e melhorias para esse livro, mas tam-
bém pela influência direta que tem em meu dia a dia profissional.
    Gostaria também de estender o agradecimento para toda equipe da
Caelum. São profissionais exemplares que me incentivam a aprender e en-
sinar diariamente.




                                                                         iii


[PAGINA 6]


[PAGINA 7]
Casa do Código                                                                 Sumário




Sumário

1   Java                                                                            1
    1.1    Nosso primeiro código Java . . . . . . . . . . . . . . . . . . .          1
    1.2    Algumas regras e convenções . . . . . . . . . . . . . . . . . .          3
    1.3    Entendendo o método main . . . . . . . . . . . . . . . . . . .           4
    1.4    Trabalhando com uma IDE . . . . . . . . . . . . . . . . . . . .          6
    1.5    Acesse o código desse livro e entre em contato conosco . . .             9

2   Variáveis e tipos primitivos                                                   11
    2.1    Nosso projeto . . . . . . . . . . . . . . . . . . . . . . . . . . . .    11
    2.2    Declaração e atribuição de variáveis . . . . . . . . . . . . . . .       11
    2.3    Tipos primitivos . . . . . . . . . . . . . . . . . . . . . . . . . .    14
    2.4    Casting de valores . . . . . . . . . . . . . . . . . . . . . . . . .    16
    2.5    Adicionando condicionais . . . . . . . . . . . . . . . . . . . .        18
    2.6    Loopings e mais loopings . . . . . . . . . . . . . . . . . . . . .      21

3   Orientação a objetos                                                           29
    3.1    Criando um molde de livros . . . . . . . . . . . . . . . . . . .        30
    3.2    Criando um novo método . . . . . . . . . . . . . . . . . . . .          34
    3.3    Objetos para todos os lados! . . . . . . . . . . . . . . . . . . .      38
    3.4    Entendendo a construção de um objeto . . . . . . . . . . . . .          51
    3.5    Vantagens da orientação a objetos . . . . . . . . . . . . . . . .       53

                                                                                    v


[PAGINA 8]
Sumário                                                           Casa do Código


4 Encapsulamento                                                               55
  4.1 Limitando desconto do Livro . . . . . . . . . . . . . . . . . . .        55
  4.2 Isolando comportamentos . . . . . . . . . . . . . . . . . . . .          59
  4.3 Código encapsulado . . . . . . . . . . . . . . . . . . . . . . . .       61
  4.4 Getters e Setters . . . . . . . . . . . . . . . . . . . . . . . . . .    62
  4.5 Definindo dependências pelo construtor . . . . . . . . . . . .           67

5    Herança e polimorfismo                                                    75
     5.1 Trabalhando com livros digitais . . . . . . . . . . . . . . . . .     75
     5.2 Reescrevendo métodos da superclasse . . . . . . . . . . . . .         80
     5.3 Regras próprias de um LivroFisico . . . . . . . . . . . . . . .       85
     5.4 Vendendo diferentes tipos de Livro . . . . . . . . . . . . . . .      87
     5.5 Acumulando total de compras . . . . . . . . . . . . . . . . . .       91
     5.6 Herança ou composição? . . . . . . . . . . . . . . . . . . . . .      94

6 Classe abstrata                                                              95
  6.1 Qual o tipo de cada Livro? . . . . . . . . . . . . . . . . . . . .       95
  6.2 Minilivro não tem desconto! . . . . . . . . . . . . . . . . . . .        98
  6.3 Método abstrato . . . . . . . . . . . . . . . . . . . . . . . . . .     102
  6.4 Relembrando algumas regras . . . . . . . . . . . . . . . . . . .        104

7    Interface                                                                105
     7.1 O contrato Produto . . . . . . . . . . . . . . . . . . . . . . . .   108
     7.2 Diminuindo acoplamento com Interfaces . . . . . . . . . . .           112
     7.3 Novas regras da interface no Java 8 . . . . . . . . . . . . . . .    114

8    Pacotes                                                                  119
     8.1 Organizando nossas classes . . . . . . . . . . . . . . . . . . . .   119
     8.2 Modificadores de acesso . . . . . . . . . . . . . . . . . . . . .    126

9 Arrays e exception                                                          129
  9.1 Trabalhando com multiplicidade . . . . . . . . . . . . . . . .          129
  9.2 As diferentes exceções e como lidar com elas . . . . . . . . .          136
  9.3 Muitas e muitas Exception . . . . . . . . . . . . . . . . . . . .       142
  9.4 Também podemos lançar exceções! . . . . . . . . . . . . . . .           147

vi


[PAGINA 9]
Casa do Código                                                              Sumário



10 Conhecendo a API                                                             151
   10.1 Todo objeto tem um tipo em comum . . . . . . . . . . . . . .            151
   10.2 Wrappers dos tipos primitivos . . . . . . . . . . . . . . . . . .       161
   10.3 O pacote java.lang . . . . . . . . . . . . . . . . . . . . . . . . .    163

11 Collection Framework                                                       169
   11.1 O trabalho de manipular arrays . . . . . . . . . . . . . . . . . 169
   11.2 Ordenando nossa List de produtos . . . . . . . . . . . . . . . 178
   11.3 Gerenciando cupons de desconto . . . . . . . . . . . . . . . . 182
   11.4 java.util.Map . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188

12 Streams e novidades do Java 8                                                193
   12.1 Ordenando com Java 8 . . . . . . . . . . . . . . . . . . . . . .        193
   12.2 forEach do Java 8 . . . . . . . . . . . . . . . . . . . . . . . . . .   198
   12.3 Filtrando livros pelo autor . . . . . . . . . . . . . . . . . . . .     198

13 Um pouco da história do Java                                            203
   13.1 Origem da linguagem . . . . . . . . . . . . . . . . . . . . . . . 203
   13.2 Escreva uma vez, rode em qualquer lugar! . . . . . . . . . . . 204
   13.3 Linha do tempo . . . . . . . . . . . . . . . . . . . . . . . . . . 205

14 Continuando seus estudos                                                     211
   14.1 Entre em contato conosco . . . . . . . . . . . . . . . . . . . .        212




                                                                                vii


[PAGINA 10]


[PAGINA 11]
Capítulo 1

Java
1.1    Nosso primeiro código Java
No lugar de começar com conceitos e teorias, vamos logo partir para uma boa
dose de prática! Abra seu editor de texto preferido e escreva o seguinte código
Java:

❝❧❛ss ▼❡✉Pr✐♠❡✐r♦Pr♦❣r❛♠❛ ④

      ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④
          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❖ ♣r✐♠❡✐r♦ ❞❡ ♠✉✐t♦s✦✧✮❀
      ⑥
⑥

   Esse programa imprime um texto simples. Confuso? Não se preocupe,
em breve cada uma dessas palavras terá seu sentido bem claro.


[PAGINA 12]
1.1. Nosso primeiro código Java                               Casa do Código


   Salve o arquivo em algum diretório de sua preferência, mas é importante
que ele se chame MeuPrimeiroPrograma.java.
   Nosso próximo passo será compilar esse código fonte. Faremos isso man-
ualmente utilizando o javac, compilador padrão da Oracle.
   Abra seu terminal e digite javac MeuPrimeiroPrograma.java.
Note que para isso você precisa estar na mesma pasta do arquivo, ou passar o
caminho completo para ele.


    Navegando pelas pastas e listando arquivos

       Você pode utilizar o comando cd (change directory) para navegar
    pelas suas pastas via terminal. Um exemplo em Windows seria:

    ❉✿❭❃ ❝❞ ❉❡s❦t♦♣❭❧✐✈r♦
    ❉✿❭❉❡s❦t♦♣❭❧✐✈r♦❃

       O mesmo comando pode ser utilizado em um ambiente Unix (Linux
    ou Mac OS). Para listar, há uma diferença. Em Windows utilizamos o
    comando dir:

    ❉✿❭❉❡s❦t♦♣❭❧✐✈r♦❃ ❞✐r
        ▼❡✉Pr✐♠❡✐r♦Pr♦❣r❛♠❛✳❥❛✈❛
        ▼❡✉Pr✐♠❡✐r♦Pr♦❣r❛♠❛✳❝❧❛ss

      Porém, nos outros sistemas que foram citados o comando será ls.
    Repare:

    t✉r✐♥✐ ⑦ ✩ ❝❞ ❉❡s❦t♦♣✴❧✐✈r♦
    t✉r✐♥✐✴❉❡s❦t♦♣✴❧✐✈r♦ ⑦ ✩ ❧s
        ▼❡✉Pr✐♠❡✐r♦Pr♦❣r❛♠❛✳❥❛✈❛
        ▼❡✉Pr✐♠❡✐r♦Pr♦❣r❛♠❛✳❝❧❛ss



    Note que, se nenhum erro de compilação ocorrer, no mesmo diretório
agora existirá um novo arquivo com o mesmo nome de nossa classe Java
(neste caso, MeuPrimeiroPrograma), porém a sua extensão será .class.
Este novo arquivo é o bytecode gerado pelo compilador.

2


[PAGINA 13]
Casa do Código                                                  Capítulo 1. Java



    Para executá-lo, ainda pelo terminal, digite o comando java
MeuPrimeiroPrograma. O comando java é o responsável por executar
a JVM (máquina virtual, ou Java Virtual Machine) que irá interpretar o byte-
code de seu programa. Repare que neste comando não passamos a extensão
do arquivo:

t✉r✐♥✐✴❉❡s❦t♦♣✴❧✐✈r♦ ⑦ ✩ ❥❛✈❛ ▼❡✉Pr✐♠❡✐r♦Pr♦❣r❛♠❛
    ❖ ♣r✐♠❡✐r♦ ❞❡ ♠✉✐t♦s✦

    E pronto! Você já compilou e executou o seu primeiro programa em Java.
    Não se preocupe, a JVM, bytecode e outros conceitos e siglas importantes
serão melhor detalhados mais à frente.

  Instalação do Java

     Para executar os códigos deste livro, você precisará ter o JDK (Java
  Development Kit) instalado. Se precisar, você pode seguir as instruções
  do link a seguir para instalar de acordo com seu sistema operacional:
     http://www.caelum.com.br/apostila-java-orientacao-objetos/
  apendice-instalacao-do-java/
     Precisa de ajuda? Não deixe de nos mandar um e-mail no grupo:
     https://groups.google.com/d/forum/livro-java-oo


1.2    Algumas regras e convenções
Você pode ter reparado que seguimos algumas regras e convenções até agora.
Vamos entendê-las um pouco melhor.
    Podemos       começar     pelo     nome      de    nosso     arquivo,
MeuPrimeiroPrograma. Em Java, o nome de uma classe sempre se
inicia com letra maiúscula e, quando necessário, as palavras seguintes
também têm seu case alterado. Dessa forma “esse nome de classe
    vira “EsseNomeDeClasse
    . Essa abordagem é bastante conhecida como CamelCase.
    Um arquivo .java possui a definição de uma classe. É uma prática
recomendada nomear a classe e o arquivo da mesma forma, caso contrário

                                                                              3


[PAGINA 14]
1.3. Entendendo o método main                                   Casa do Código


poderá existir alguma confusão no momento de executá-la. Por exemplo,
considere que temos um arquivo meu-primeiro-programa.java con-
tendo a classe que chamamos de MeuPrimeiroPrograma. Para compilá-lo
faremos:

t✉r✐♥✐✴❉❡s❦t♦♣✴❧✐✈r♦ ⑦ ✩ ❥❛✈❛❝ ♠❡✉✲♣r✐♠❡✐r♦✲♣r♦❣r❛♠❛✳❥❛✈❛

    Porém, o arquivo compilado (com o bytecode) terá o nome
MeuPrimeiroPrograma.class.            Como executar esse programa? A
resposta será com o nome da classe, e não do arquivo. Neste caso:

t✉r✐♥✐✴❉❡s❦t♦♣✴❧✐✈r♦ ⑦ ✩ ❥❛✈❛ ▼❡✉Pr✐♠❡✐r♦Pr♦❣r❛♠❛

    Note também que há um par de chaves {} definindo o inicio e final (es-
copo) de sua classe e as instruções sempre terminam com ponto e vírgula.
    Por fim, é fundamental perceber que esta é uma linguagem case sensitive,
ou seja, leva em consideração o case (caixa) em que as instruções são escritas.
Escrever System com letra minúscula, por exemplo, resultaria em um erro
de compilação.
    Você pode ler mais a respeito dessas e de outras convenções da linguagem
no documento oficial Code Conventions for the Java Programming Language,
disponível no site da Oracle:
    http://www.oracle.com/technetwork/java/index-135089.html


1.3     Entendendo o método main
Ao ser executada, a máquina virtual (JVM) procura pelo bloco main
declarado em sua classe. Esse é um bloco especial (ou método, como pas-
saremos a chamar a partir de agora) e se parece com:

♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④
    ✴✴ s❡✉ ❝ó❞✐❣♦ ❛q✉✐
⑥

   Suas aplicações Java, em geral, vão possuir apenas um método main,
um único ponto de partida. Quando rodamos o comando java passando o


4


[PAGINA 15]
Casa do Código                                                Capítulo 1. Java



nome de nossa classe, dissemos para a JVM executar todo o conteúdo que es-
tiver dentro do corpo (das chaves) desse método. Em nosso exemplo, foi uma
simples instrução de impressão, o System.out.println("o primeiro
de muitos!").
    Há ainda como passar argumentos para o método main ao executar um
programa Java. O parâmetro String[] args que o método recebe den-
tro de seus parênteses será o responsável por armazenar esses argumentos
para que possam ser acessados em nosso código. Mas, afinal, o que é esse
String[]? Um array de String em Java, porém, por enquanto não esta-
mos interessados em entender um array e todos os seus detalhes, tudo o que
precisamos saber é que ele vai armazenar uma multiplicidade de Strings.
    Um exemplo dessa passagem de parâmetro seria:

t✉r✐♥✐✴❉❡s❦t♦♣✴❧✐✈r♦ ⑦ ✩ ❥❛✈❛ ▼❡✉Pr✐♠❡✐r♦Pr♦❣r❛♠❛ ❏❛✈❛ ❘♦❞r✐❣♦

   Para isso funcionar, modificamos nosso código para exibir o conteúdo
guardado nas posições 0 e 1 ( args[0], args[1]) desse conjunto de argu-
mentos:

❝❧❛ss ▼❡✉Pr✐♠❡✐r♦Pr♦❣r❛♠❛ ④

     ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④
         ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❖ ♣r✐♠❡✐r♦ ❞❡ ♠✉✐t♦s ❝ó❞✐❣♦s
             ❡s❝r✐t♦s ❡♠ ✧ ✰❛r❣s❬✵❪✰ ✧ ♣❡❧♦ ✧ ✰❛r❣s❬✶❪✰ ✧✦✧✮❀
     ⑥
⑥

   Execute para conferir o resultado! Não se esqueça que, como modifi-
camos nosso código, precisaremos compilar novamente:

t✉r✐♥✐✴❉❡s❦t♦♣✴❧✐✈r♦ ⑦ ✩ ❥❛✈❛❝ ▼❡✉Pr✐♠❡✐r♦Pr♦❣r❛♠❛✳❥❛✈❛
t✉r✐♥✐✴❉❡s❦t♦♣✴❧✐✈r♦ ⑦ ✩ ❥❛✈❛ ▼❡✉Pr✐♠❡✐r♦Pr♦❣r❛♠❛ ❏❛✈❛ ❘♦❞r✐❣♦

    Nesse exemplo, o resultado impresso será:

❖ ♣r✐♠❡✐r♦ ❞❡ ♠✉✐t♦s ❝ó❞✐❣♦s ❡s❝r✐t♦s ❡♠ ❏❛✈❛ ♣❡❧♦ ❘♦❞r✐❣♦✦




                                                                            5


[PAGINA 16]
1.4. Trabalhando com uma IDE                                    Casa do Código




    Erro de compilação?

       Um erro de digitação, a falta de um ponto e vírgula ou uma difer-
    ença de case em seu código são alguns dos muitos motivos que podem
    resultar em um erro de compilação. Conhecer e entender esses erros é
    fundamental, talvez você queira inclusive provocar algum deles para ver
    como seu código se comparta.
       Qual será a mensagem caso eu esqueça de escrever um ponto e vír-
    gula? Escreva um teste simples pra descobrir! Um exemplo:

    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧s❡♠ ♣♦♥t♦✲❡✲✈✐r❣✉❧❛✧✮

       A mensagem de erro será:

    ❙②♥t❛① ❡rr♦r✱ ✐♥s❡rt ✧❀✧ t♦ ❝♦♠♣❧❡t❡ ❇❧♦❝❦❙t❛t❡♠❡♥ts

      Lembre-se que você pode e deve tirar todas as suas dúvidas no GUJ,
    em http://guj.com.br.


1.4 Trabalhando com uma IDE
Escrever, compilar e executar seu código Java em um bloco de notas junto
com terminal é bastante trabalhoso. É fundamental conhecer esse processo,
mas em seu dia a dia você provavelmente vai preferir utilizar alguma das mais
diversas ferramentas de desenvolvimento conhecidas para ajudá-lo nesse tra-
balho.
    Essas ferramentas são chamadas de IDE (Integrated Development Envi-
ronment) e podem tornar seu desenvolvimento muito mais produtivo e in-
teressante, oferecendo-lhe recursos como syntax highlight e auto complete das
instruções de seu código.
    No decorrer deste livro, vamos utilizar o Eclipse, você pode fazer o down-
load de sua versão mais recente em:
    https://www.eclipse.org/downloads/
    Essa é uma IDE gratuita e open source, sem dúvida uma das preferidas do
mercado e instituições de ensino. Seus diversos atalhos e templates prontos

6


[PAGINA 17]
Casa do Código                                                    Capítulo 1. Java



são grandes diferenciais.
    Existem diversas outras boas opções no mercado, como por exemplo o
NetBeans da Oracle, ou o IntelliJ IDEA, sendo este último pago.

Criando seu primeiro projeto no Eclipse
     Depois de fazer o download, você não precisará instalar a IDE. Esta é
uma executável inteiramente escrita em Java, basta executá-la e escolher a
pasta onde será a sua área de trabalho (workspace). Escolha um local de sua
preferência.
     Vamos criar nosso projeto! Para isso, você pode por meio do menu escol-
her as opções File > New > Java Project. Vamos chamar o projeto
que desenvolveremos durante o curso de livraria.
     Repare que, depois de concluir, esse projeto será representando em seu
sistema operacional como uma pasta, dentro do workspace que você escolheu.
Por enquanto, dentro desse diretório você encontrará a pasta src, onde ficará
todo o seu código .java e também a pasta bin, onde ficará o bytecode
compilado.

Produtividade extrema
    Agora que já criamos o projeto, vamos criar nossa primeira classe
pelo Eclipse. Você pode fazer isso pelo menu File > New > Class.
Para conhecer um pouco da IDE, vamos criar novamente a classe
MeuPrimeiroPrograma.
    Depois de preencher o nome, selecione a opção finish e veja o resultado:

♣✉❜❧✐❝ ❝❧❛ss ▼❡✉Pr✐♠❡✐r♦Pr♦❣r❛♠❛ ④

⑥

    A estrutura de sua classe já está pronta, vamos agora escrever seu método
main. Para fazer isso, escreva a palavra main dentro de sua classe e pressione
o atalho Control + Espaço.
    Esse é o atalho de code completion da IDE. Se tudo correu bem, seu código
ficou assim:


                                                                                7


[PAGINA 18]
1.4. Trabalhando com uma IDE                                 Casa do Código


♣✉❜❧✐❝ ❝❧❛ss ▼❡✉Pr✐♠❡✐r♦Pr♦❣r❛♠❛ ④

     ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④


     ⑥
⑥

    Interessante, não acha? Além de termos mais produtividade ao escrever,
evitamos que erros de digitação aconteçam.
    Vamos além, agora dentro do método main, digite syso e pressione
Control + Espaço para fazer code completion novamente.
    Você pode e deve usar e abusar desse recurso!

♣✉❜❧✐❝ ❝❧❛ss ▼❡✉Pr✐♠❡✐r♦Pr♦❣r❛♠❛ ④

     ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④
         ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❖ ♣r✐♠❡✐r♦ ❞❡ ♠✉✐t♦s✦✧✮❀
     ⑥
⑥

    Agora, com o código pronto, as próximas etapas seriam compilar e
executá-lo, mas a compilação já está pronta!
    Isso mesmo, conforme você vai escrevendo seu código, a IDE já cuida de
compilá-lo. Repare que se você apagar o ponto e vírgula, por exemplo, essa
linha ficará sublinhada em vermelho. Essa é uma indicação visual de que seu
código não está compilando.
    Para executar o código, você pode clicar com o botão direito do mouse
em sua classe e selecionar as opções Run As > Java Application . Ou
por atalho, pressionando Control + F11.
    Repare que a saída de seu código vai aparecer na aba Console.

❖ ♣r✐♠❡✐r♦ ❞❡ ♠✉✐t♦s✦




8


[PAGINA 19]
Casa do Código                                                   Capítulo 1. Java




  Atalhos do Eclipse

     Conhecer os atalhos da IDE vai torná-lo um programador muito mais
  produtivo. Você pode ler mais a respeito e conhecer mais atalhos pela
  documentação do Eclipse em:
     https://www.eclipse.org/users/
     E também no post:
     http://blog.caelum.com.br/as-tres-principais-teclas-de-atalho-do-eclipse/



     Se esse for o seu primeiro contato com a linguagem, recomendamos que
você pratique bastante a sintaxe antes de partir para os próximos capítu-
los. Sinta-se confortável com o processo de escrever, compilar e executar seu
código Java. Tenho certeza de que em breve essa será sua rotina.


1.5 Acesse o código desse livro e entre em con-
    tato conosco
Todos os exemplos deste livro podem ser encontrados no repositório:
    https://github.com/Turini/livro-oo
    Mas claro, não deixe de escrever todo o código que vimos para praticar a
sintaxe e se adaptar com os detalhes da linguagem. Além disso, sempre que
possível faça novos testes além dos aqui sugeridos.
    Ficou com alguma dúvida? Não deixe de me mandar um e-mail. A
seguinte lista foi criada exclusivamente para facilitar o seu contato conosco
e com os demais leitores:
    https://groups.google.com/d/forum/livro-java-oo
    Suas sugestões, criticas e melhorias serão muito mais do que bem-vindas!
    Outro recurso que você pode usar para esclarecer suas dúvidas e partic-
ipar ativamente na comunidade Java é o fórum do GUJ, espero encontrá-lo
por lá.
    http://www.guj.com.br/


                                                                               9


[PAGINA 20]


[PAGINA 21]
Capítulo 2

Variáveis e tipos primitivos
2.1    Nosso projeto
Durante o livro, vamos criar e evoluir a aplicação Java de uma livraria como a
Casa do Código. Esse contexto vai nos possibilitar colocar em prática todos os
principais recursos e conceitos da linguagem, desde o mais simples ao mais
avançado, além de conhecer e trabalhar com as APIs e features de sua mais
nova versão.


2.2    Declaração e atribuição de variáveis
Vamos criar uma nova classe Java cujo objetivo será calcular o valor
total de livros do nosso estoque na livraria. Podemos chamá-la de
CalculadoraDeEstoque.


[PAGINA 22]
2.2. Declaração e atribuição de variáveis                     Casa do Código


♣✉❜❧✐❝ ❝❧❛ss ❈❛❧❝✉❧❛❞♦r❛❉❡❊st♦q✉❡ ④

      ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④

      ⑥
⑥

    Precisamos agora armazenar dentro de seu método main o valor de nos-
sos livros. Uma forma simples de fazer isso seria:

♣✉❜❧✐❝ ❝❧❛ss ❈❛❧❝✉❧❛❞♦r❛❉❡❊st♦q✉❡ ④

      ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④

             ❞♦✉❜❧❡ ❧✐✈r♦❏❛✈❛✽❀
             ❞♦✉❜❧❡ ❧✐✈r♦❚❉❉❀
      ⑥
⑥

    Dessa forma, estamos pedindo ao Java que reserve regiões da memória
para futuramente armazenar esses valores. Essa instrução que criamos é con-
hecida como uma variável.
    Repare que essas duas variáveis declaradas possuem um tipo double
(número com ponto flutuante). Logo, conheceremos os outros tipos exis-
tentes, mas é importante reconhecer desde já que toda variável em Java pre-
cisara ter um.
    Utilizamos o sinal = (igual) para atribuir um valor para estas variáveis
que representam alguns de nossos livros:

❞♦✉❜❧❡ ❧✐✈r♦❏❛✈❛✽❀
❞♦✉❜❧❡ ❧✐✈r♦❚❉❉❀

❧✐✈r♦❏❛✈❛✽ ❂ ✺✾✳✾✵❀
❧✐✈r♦❚❉❉ ❂ ✺✾✳✾✵❀

    Mas, neste caso, como já sabemos o valor que será atribuído no momento
de sua declaração, podemos fazer a atribuição de forma direta no momento
em que cada variável é declarada:

12


[PAGINA 23]
Casa do Código                                Capítulo 2. Variáveis e tipos primitivos



❞♦✉❜❧❡ ❧✐✈r♦❏❛✈❛✽ ❂ ✺✾✳✾✵❀
❞♦✉❜❧❡ ❧✐✈r♦❚❉❉ ❂ ✺✾✳✾✵❀

   Agora que já temos alguns valores de livros, vamos calcular a sua soma e
acumular em uma nova variável. Isso pode ser feito da seguinte forma:

❞♦✉❜❧❡ s♦♠❛ ❂ ❧✐✈r♦❏❛✈❛✽ ✰ ❧✐✈r♦❚❉❉❀

    Pronto, isso é tudo que precisamos por enquanto para completar a nossa
CalculadoraDeEstoque. Após somar esses valores, vamos imprimir o
valor do resultado no console:

♣✉❜❧✐❝ ❝❧❛ss ❈❛❧❝✉❧❛❞♦r❛❉❡❊st♦q✉❡ ④

     ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④

          ❞♦✉❜❧❡ ❧✐✈r♦❏❛✈❛✽ ❂ ✺✾✳✾✵❀
          ❞♦✉❜❧❡ ❧✐✈r♦❚❉❉ ❂ ✺✾✳✾✵❀

          ❞♦✉❜❧❡ s♦♠❛ ❂ ❧✐✈r♦❏❛✈❛✽ ✰ ❧✐✈r♦❚❉❉❀

          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❖ t♦t❛❧ ❡♠ ❡st♦q✉❡ é ✧✰ s♦♠❛✮❀
     ⑥
⑥

    Escreva e execute esse código para praticar! Neste exemplo, o resultado
será:

❖ t♦t❛❧ ❡♠ ❡st♦q✉❡ é ✶✶✾✳✽

   Além do operador de soma ( +), você também pode usar os seguintes
operadores em seu código Java:




                                                                                   13


[PAGINA 24]
2.3. Tipos primitivos                                        Casa do Código




2.3 Tipos primitivos
Vimos que é possível representar um número com ponto flutuante utilizando
o tipo double, mas existem diversos outros tipos para representar os difer-
entes valores com que trabalhamos no dia a dia.
    Para representar um número inteiro, por exemplo, podemos utilizar os
tipos byte, short, int ou long. Isso mesmo, o código a seguir compila
com qualquer um desses tipos:

❜②t❡ ✐♥t❡✐r♦✶ ❂ ✶✵❀
s❤♦rt ✐♥t❡✐r♦✷ ❂ ✶✵❀
✐♥t ✐♥t❡✐r♦✸ ❂ ✶✵❀
❧♦♥❣ ✐♥t❡✐r♦✹ ❂ ✶✵❀

    Mas, afinal, quando eu devo utilizar cada um desses? A grande diferença
está no tamanho de cada um desses tipos. Por exemplo, um short suporta
até 2 bytes, enquanto um long suporta 8 bytes.
    Muito diferente de antigamente, hoje não há uma preocupação tão grande
em economizar bytes na declaração de suas variáveis. Você raramente verá
um programador utilizando um short para guardar um número pequeno,

14


[PAGINA 25]
Casa do Código                                 Capítulo 2. Variáveis e tipos primitivos



no lugar de usar logo um int. Mas claro, conhecer os diferentes tipos e a
capacidade de cada um deles é essencial para um bom programador.
    Esses são os possíveis tipos primitivos da linguagem Java:




    Um detalhe simples, porém muito importante, sobre os tipos primitivos
é que, quando você atribui um valor para eles (utilizando o operador =),
este valor será copiado para a sua variável. Por exemplo, repare no seguinte
código:

✐♥t ♥✉♠❡r♦ ❂ ✹❀
✐♥t ♦✉tr♦◆✉♠❡r♦■❣✉❛❧ ❂ ♥✉♠❡r♦❀
♥✉♠❡r♦ ❂ ♥✉♠❡r♦ ✰ ✺❀

❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭♥✉♠❡r♦✮❀
❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭♦✉tr♦◆✉♠❡r♦■❣✉❛❧✮❀


                                                                                    15


[PAGINA 26]
2.4. Casting de valores                                         Casa do Código


     Neste caso, com certeza o valor da variável numero no momento em que
for impressa será 9, mas e quanto ao outroNumeroIgual? Repare que ela
recebe numero e seu valor foi alterado logo em seguida.
     Execute esse código e você perceberá que o outroNumeroIgual con-
tinuará com o valor 4, pois este era o valor da variável numero no momento
da atribuição. Ou seja, a variável outroNumeroIgual guardou uma cópia
do valor, e não uma referência a ela ou algo do tipo.


     Tipos não primitivos

       Logo conheceremos outros tipos (não primitivos) da linguagem Java,
     mas desde já repare que um texto, assim como qualquer outro valor, tam-
     bém tem um tipo! Esse tipo é conhecido por String.
       Você poderia, no lugar de fazer:

     ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❊✉ s♦✉ ✉♠❛ ❙tr✐♥❣✧✮❀

        Declarar da seguinte forma:

     ❙tr✐♥❣ t❡①t♦ ❂ ✧❊✉ s♦✉ ✉♠❛ ❙tr✐♥❣✧❀
     ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭t❡①t♦✮❀




2.4       Casting de valores
Como você já deve ter percebido, nem todos os valores são com-
patíveis. Por exemplo, se eu tentar declarar o valor de nossos livros na
CalculadoraDeEstoque como um int, um erro de compilação aconte-
cerá.
♣✉❜❧✐❝ ❝❧❛ss ❈❛❧❝✉❧❛❞♦r❛❉❡❊st♦q✉❡ ④

       ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④

             ✐♥t ❧✐✈r♦❏❛✈❛✽ ❂ ✺✾✳✾✵❀
             ✐♥t ❧✐✈r♦❚❉❉ ❂ ✺✾✳✾✵❀


16


[PAGINA 27]
Casa do Código                                 Capítulo 2. Variáveis e tipos primitivos



          ✐♥t s♦♠❛ ❂ ❧✐✈r♦❏❛✈❛✽ ✰ ❧✐✈r♦❚❉❉❀

          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❖ t♦t❛❧ ❡♠ ❡st♦q✉❡ é ✧✰ s♦♠❛✮❀
     ⑥
⑥

     Repare no Eclipse (ou qualquer outra IDE ou editor de texto que estiver
utilizando em seus testes) que o seguinte erro será exibido:

❚②♣❡ ♠✐s♠❛t❝❤✿ ❝❛♥♥♦t ❝♦♥✈❡rt ❢r♦♠ ❞♦✉❜❧❡ t♦ ✐♥t

   Ou seja, um int não pode guardar um número com ponto flutuante (
double). Faz sentido.
    Mas, sim, o contrário é totalmente possível. Repare no código:

♣✉❜❧✐❝ ❝❧❛ss ❈❛❧❝✉❧❛❞♦r❛❉❡❊st♦q✉❡ ④

     ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④

          ❞♦✉❜❧❡ ❧✐✈r♦❏❛✈❛✽ ❂ ✻✵❀
          ❞♦✉❜❧❡ ❧✐✈r♦❚❉❉ ❂ ✻✵❀

          ❞♦✉❜❧❡ s♦♠❛ ❂ ❧✐✈r♦❏❛✈❛✽ ✰ ❧✐✈r♦❚❉❉❀

          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❖ t♦t❛❧ ❡♠ ❡st♦q✉❡ é ✧✰ s♦♠❛✮❀
     ⑥
⑥

    Mesmo arredondando o valor dos livros para um número inteiro (neste
caso, 60), um double pode sim guardar esse valor. Portanto, eu posso
atribuir valores menores em variáveis com uma capacidade maior; o que eu
não posso é o contrário. Uma analogia dev que gosto muito e se encaixa bem
aqui é: “Você pode colocar uma formiga na casa de um cavalo, o contrário não
daria certo”.
    Mas repare que nem mesmo o seguinte código compila:

❞♦✉❜❧❡ ❧✐✈r♦❏❛✈❛✽ ❂ ✻✵❀
✐♥t ♥✉♠❡r♦■♥t❡✐r♦ ❂ ❧✐✈r♦❏❛✈❛✽❀


                                                                                    17


[PAGINA 28]
2.5. Adicionando condicionais                                   Casa do Código


    Da mesma forma que antes, estamos tentando atribuir um double (que é
um tipo de tamanho maior) em um int. Não importa se o valor que atribuí-
mos a este double é um valor inteiro válido (um bom candidato para o tipo
int). O compilador vai se preocupar com o tipo de suas variáveis, e não
com seus valores, até porque, como o próprio nome indica, esses valores são
mutáveis, portanto essa atribuição seria perigosa.
    Em algum momento, você pode precisar forçar essa conversão de tipos,
dizendo ao compilador: “tudo bem, eu garanto que o valor deste double pode
ser moldado para um numero inteiro
    . Para isso, utilizamos um recurso conhecido como casting.

✐♥t ♥✉♠❡r♦■♥t❡✐r♦ ❂ ✭✐♥t✮ ❧✐✈r♦❏❛✈❛✽❀

      Neste caso, seu código vai compilar sem nenhum problema e a variável
numeroInteiro terá uma copia do valor 60.
    Se o valor do livroJava8 fosse 59.90, ou seja, um número com ponto
flutuante e você fizesse esse casting haveria uma perda de precisão. A var-
iável numeroInteiro teria apenas o valor 59 copiado.


2.5      Adicionando condicionais
Nossa CalculadoraDeEstoque precisa de uma nova funcionalidade. Se o
valor total de livros for menor que 150 reais, precisamos ser alertados de que
nosso estoque está baixíssimo, caso contrário, devemos mostrar uma men-
sagem indicando de que está tudo sob controle!
    Em Java, podemos fazer essa condicional de uma forma bem comum, uti-
lizando um if e else. Observe:

♣✉❜❧✐❝ ❝❧❛ss ❈❛❧❝✉❧❛❞♦r❛❉❡❊st♦q✉❡ ④

      ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④

            ❞♦✉❜❧❡ ❧✐✈r♦❏❛✈❛✽ ❂ ✺✾✳✾✵❀
            ❞♦✉❜❧❡ ❧✐✈r♦❚❉❉ ❂ ✺✾✳✾✵❀

            ❞♦✉❜❧❡ s♦♠❛ ❂ ❧✐✈r♦❏❛✈❛✽ ✰ ❧✐✈r♦❚❉❉❀


18


[PAGINA 29]
Casa do Código                                 Capítulo 2. Variáveis e tipos primitivos




          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❖ t♦t❛❧ ❡♠ ❡st♦q✉❡ é ✧✰ s♦♠❛✮❀

          ✐❢ ✭s♦♠❛ ❁ ✶✺✵✮ ④
              ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❙❡✉ ❡st♦q✉❡ ❡stá ♠✉✐t♦ ❜❛✐①♦✦✧✮❀
          ⑥ ❡❧s❡ ④
              ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❙❡✉ ❡st♦q✉❡ ❡stá ❜♦♠✧✮❀
          ⑥
     ⑥
⑥

    Como já é esperado, esse código só vai imprimir a mensagem de estoque
baixo se o valor da soma for menor ( <) que 150. Caso contrário, irá executar
o conteúdo de dentro do bloco else.
    Passamos uma condição como argumento fazendo uma comparação en-
tre o valor da variável soma com o valor 150. Essa condição vai resultar em
um valor true quando verdadeira, ou false caso contrário. Esse tipo de
condição é conhecido como expressão booleana. Seu resultado sempre será
do tipo boolean:

❜♦♦❧❡❛♥ r❡s✉❧t❛❞♦ ❂ s♦♠❛ ❁ ✶✺✵❀

    Você pode usar qualquer um dos seguintes operadores relacionais pra
construir uma expressão booleana: > (maior), < (menor), >= (maior ou
igual), <= (menor ou igual), == (igual sim, são dois iguais! Lembre-se que
um único igual significa atribuição) e, por fim, != (diferente).
    Há ainda a alternativa de encadear mais condições em nosso if. Por
exemplo, para receber uma mensagem indicando que o estoque está muito
alto, podemos adicionar a seguinte condição:

♣✉❜❧✐❝ ❝❧❛ss ❈❛❧❝✉❧❛❞♦r❛❉❡❊st♦q✉❡ ④

     ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④

          ❞♦✉❜❧❡ ❧✐✈r♦❏❛✈❛✽ ❂ ✺✾✳✾✵❀
          ❞♦✉❜❧❡ ❧✐✈r♦❚❉❉ ❂ ✺✾✳✾✵❀

          ❞♦✉❜❧❡ s♦♠❛ ❂ ❧✐✈r♦❏❛✈❛✽ ✰ ❧✐✈r♦❚❉❉❀

                                                                                    19


[PAGINA 30]
2.5. Adicionando condicionais                                   Casa do Código




            ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❖ t♦t❛❧ ❡♠ ❡st♦q✉❡ é ✧✰ s♦♠❛✮❀

            ✐❢ ✭s♦♠❛ ❁ ✶✺✵✮ ④
                ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❙❡✉ ❡st♦q✉❡ ❡stá ♠✉✐t♦ ❜❛✐①♦✦✧✮❀
            ⑥ ❡❧s❡ ✐❢ ✭s♦♠❛ ❃❂ ✷✵✵✵✮ ④
                ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❙❡✉ ❡st♦q✉❡ ❡stá ♠✉✐t♦ ❛❧t♦✦✧✮❀
            ⑥ ❡❧s❡ ④
                ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❙❡✉ ❡st♦q✉❡ ❡stá ❜♦♠✧✮❀
            ⑥
      ⑥
⑥


    Operador ternário

       É muito comum escrevermos condicionais como a seguinte, que, de
    acordo com alguma condição booleana, retorna um valor diferente. Re-
    pare:

    ❞♦✉❜❧❡ ✈❛❧♦r ❂ ✵❀
    ✐❢ ✭✈✶ ❃ ✈✷✮ ④
        ✈❛❧♦r ❂ ✶✵✵❀
    ⑥ ❡❧s❡ ④
        ✈❛❧♦r ❂ ✵❀
    ⑥

       Uma alternativa bastante conhecida e utilizada para estes casos é o
    operador ternário ?: . Com ele, você pode fazer o mesmo da seguinte
    forma:

    ❞♦✉❜❧❡ ✈❛❧♦r ❂ ✈✶ ❃ ✈✷ ❄ ✶✵✵ ✿ ✵❀

        Sem dúvida, fica bem mais enxuto, não acha? Performaticamente, não
    há nenhuma vantagem significante em usar uma ou outra estratégia, mas
    é sempre interessante levar em consideração a legibilidade do código. Em
    alguns casos, usar o operador ternário pode custar um pouco da legibil-
    idade e deixar o código mais complexo.


20


[PAGINA 31]
Casa do Código                                   Capítulo 2. Variáveis e tipos primitivos



2.6     Loopings e mais loopings
Considerando que todos os livros têm o preço 59.90, seria muito trabalhoso
criar tantas variáveis para que o valor da soma ultrapasse 2000 reais. Para nos
ajudar na construção desses livros podemos criar uma estrutura de repetição
(um looping). Uma das formas de se fazer isso seria utilizando o while:

❞♦✉❜❧❡ s♦♠❛ ❂ ✵❀
✐♥t ❝♦♥t❛❞♦r ❂ ✵❀

✇❤✐❧❡ ✭❝♦♥t❛❞♦r ❁ ✸✺✮ ④
    ❞♦✉❜❧❡ ✈❛❧♦r❉♦▲✐✈r♦ ❂ ✺✾✳✾✵❀
    s♦♠❛ ❂ s♦♠❛ ✰ ✈❛❧♦r❉♦▲✐✈r♦❀
    ❝♦♥t❛❞♦r ❂ ❝♦♥t❛❞♦r ✰ ✶❀
⑥

    O while é bastante parecido com o if. A grande diferença é que, en-
quanto sua expressão booleana for true, seu código continuará sendo exe-
cutado. Neste exemplo estamos criando uma variável soma para acumular
o valor total dos livros e também uma variável contador para controlar a
quantidade de vezes que queremos iterar.
    Note que estamos adicionando 35 livros, já que a condição é contador
< 35 e que a cada iteração incrementamos 1 ao valor do contador.
    Nosso código completo fica da seguinte forma:

♣✉❜❧✐❝ ❝❧❛ss ❈❛❧❝✉❧❛❞♦r❛❉❡❊st♦q✉❡ ④

      ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④

          ❞♦✉❜❧❡ s♦♠❛ ❂ ✵❀
          ✐♥t ❝♦♥t❛❞♦r ❂ ✵❀

          ✇❤✐❧❡ ✭❝♦♥t❛❞♦r ❁ ✸✺✮ ④
              ❞♦✉❜❧❡ ✈❛❧♦r❉♦▲✐✈r♦ ❂ ✺✾✳✾✵❀
              s♦♠❛ ❂ s♦♠❛ ✰ ✈❛❧♦r❉♦▲✐✈r♦❀
              ❝♦♥t❛❞♦r ❂ ❝♦♥t❛❞♦r ✰ ✶❀
          ⑥



                                                                                      21


[PAGINA 32]
2.6. Loopings e mais loopings                                       Casa do Código


            ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❖ t♦t❛❧ ❡♠ ❡st♦q✉❡ é ✧✰ s♦♠❛✮❀

            ✐❢ ✭s♦♠❛ ❁ ✶✺✵✮ ④
                ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❙❡✉ ❡st♦q✉❡ ❡stá ♠✉✐t♦ ❜❛✐①♦✦✧✮❀
            ⑥ ❡❧s❡ ✐❢ ✭s♦♠❛ ❃❂ ✷✵✵✵✮ ④
                ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❙❡✉ ❡st♦q✉❡ ❡stá ♠✉✐t♦ ❛❧t♦✦✧✮❀
            ⑥ ❡❧s❡ ④
                ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❙❡✉ ❡st♦q✉❡ ❡stá ❜♦♠✧✮❀
            ⑥
       ⑥
⑥

      Ao executá-lo a saída será:

❖ t♦t❛❧ ❡♠ ❡st♦q✉❡ é ✷✵✾✻✳✺✵✵✵✵✵✵✵✵✵✵✶✹
❙❡✉ ❡st♦q✉❡ ❡stá ♠✉✐t♦ ❛❧t♦✦


     Looping infinito

         É muito comum esquecermos de modificar o valor que está sendo
     comparado dentro do while ou nas diferentes formas que veremos para
     se fazer um looping. Isso vai resultar no que chamamos de looping infinito,
     uma vez que a condição de looping sempre será true. Se quiser testar,
     adicione um comentário na linha que incrementa o valor do contador
     e execute o código:

     ✇❤✐❧❡ ✭❝♦♥t❛❞♦r ❁ ✸✺✮ ④
         ❞♦✉❜❧❡ ✈❛❧♦r❉♦▲✐✈r♦ ❂ ✺✾✳✾✵❀
         s♦♠❛ ❂ s♦♠❛ ✰ ✈❛❧♦r❉♦▲✐✈r♦❀
         ✴✴ ❝♦♥t❛❞♦r ❂ ❝♦♥t❛❞♦r ✰ ✶❀
     ⑥



    Podemos deixar nosso código ainda mais enxuto utilizando o operador
de atribuição +=. Basta, no lugar de fazer:

s♦♠❛ ❂ s♦♠❛ ✰ ✈❛❧♦r❉♦▲✐✈r♦❀

22


[PAGINA 33]
Casa do Código                                Capítulo 2. Variáveis e tipos primitivos



    Mudarmos o código para:

s♦♠❛ ✰❂ ✈❛❧♦r❉♦▲✐✈r♦❀

   Essa é uma forma equivalente de se incrementar o valor de uma variável.
O mesmo poderia ser feito com nosso contador, repare:

❝♦♥t❛❞♦r ✰❂ ✶❀

    Podemos utilizar essa técnica com os seguintes operadores:




   Mas para esse caso há uma forma ainda mais enxuta, utilizando o oper-
ador unário ++:

❝♦♥t❛❞♦r ✰✰❀

    O código do while agora fica da seguinte forma:

✇❤✐❧❡ ✭❝♦♥t❛❞♦r ❁ ✸✺✮ ④
    ❞♦✉❜❧❡ ✈❛❧♦r❉♦▲✐✈r♦ ❂ ✺✾✳✾✵❀
    s♦♠❛ ✰❂ ✈❛❧♦r❉♦▲✐✈r♦❀
    ❝♦♥t❛❞♦r ✰✰❀
⑥

                                                                                   23


[PAGINA 34]
2.6. Loopings e mais loopings                                 Casa do Código


    Nosso código pode ficar ainda mais enxuto utilizando uma outra forma
de looping extremamente conhecida e utilizada, o for.
    Observe que a estrutura que utilizamos no while foi parecida com:

✴✴ ✐♥✐❝✐❛❧✐③❛çã♦ ❞♦ ❝♦♥t❛❞♦r

✇❤✐❧❡ ✭❝♦♥❞✐çã♦✮ ④

      ✴✴ ❛t✉❛❧✐③❛çã♦ ❞♦ ❝♦♥t❛❞♦r
⑥

     Com o for, podemos fazer isso de uma forma ainda mais direta:

❢♦r✭✐♥✐❝✐❛❧✐③❛çã♦❀ ❝♦♥❞✐çã♦❀ ❛t✉❛❧✐③❛çã♦✮ ④

⑥

    Isso mesmo, além da condição booleana ele também reserva um local para
inicialização de variáveis e atualização de seus valores. Com o for nosso
código pode ser escrito assim:

❞♦✉❜❧❡ s♦♠❛ ❂ ✵❀
❢♦r ✭✐♥t ❝♦♥t❛❞♦r ❂ ✵❀ ❝♦♥t❛❞♦r ❁ ✸✺❀ ❝♦♥t❛❞♦r ✰✰✮ ④
    s♦♠❛ ✰❂ ✺✾✳✾✵❀
⑥

   Sem dúvida, é uma forma mais direta. Você muitas vezes verá essa variável
contador que criamos ser chamada de i (index, ou índice). Seguindo esse
padrão, nosso código completo fica assim:

♣✉❜❧✐❝ ❝❧❛ss ❈❛❧❝✉❧❛❞♦r❛❉❡❊st♦q✉❡ ④

      ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④

            ❞♦✉❜❧❡ s♦♠❛ ❂ ✵❀

            ❢♦r ✭❞♦✉❜❧❡ ✐ ❂ ✵❀ ✐ ❁ ✸✺❀ ✐ ✰✰✮ ④
                s♦♠❛ ✰❂ ✺✾✳✾✵❀
            ⑥


24


[PAGINA 35]
Casa do Código                           Capítulo 2. Variáveis e tipos primitivos



          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❖ t♦t❛❧ ❡♠ ❡st♦q✉❡ é ✧✰ s♦♠❛✮❀

          ✐❢ ✭s♦♠❛ ❁ ✶✺✵✮ ④
              ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❙❡✉ ❡st♦q✉❡ ❡stá ♠✉✐t♦ ❜❛✐①♦✦✧✮❀
          ⑥ ❡❧s❡ ✐❢ ✭s♦♠❛ ❃❂ ✷✵✵✵✮ ④
              ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❙❡✉ ❡st♦q✉❡ ❡stá ♠✉✐t♦ ❛❧t♦✦✧✮❀
          ⑥ ❡❧s❡ ④
              ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❙❡✉ ❡st♦q✉❡ ❡stá ❜♦♠✧✮❀
          ⑥
     ⑥
⑥




                                                                              25


[PAGINA 36]
2.6. Loopings e mais loopings                                    Casa do Código




   Trabalhando com continue e break

      Você pode utilizar a palavra-chave continue para pular uma iter-
   ação de seu looping e forçar a execução do próximo laço. O código a
   seguir vai imprimir todos os números de 0 a 10, mas vai pular o número
   7:

   ❢♦r✭✐♥t ✐ ❂ ✵❀ ✐ ❁❂ ✶✵❀ ✐✰✰✮ ④
       ✐❢ ✭✐ ❂❂ ✼✮ ④
           ❝♦♥t✐♥✉❡❀
       ⑥
       ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✐✮❀
   ⑥

      Outra possibilidade comum é parar a execução de um looping
   dada uma determinada condição. Para isso, utilizamos a palavra-chave
   break:

   ❢♦r✭✐♥t ✐ ❂ ✵❀ ✐ ❁❂ ✶✵❀ ✐✰✰✮ ④
       ✐❢ ✭✐ ❂❂ ✼✮ ④
           ❜r❡❛❦❀
       ⑥
       ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✐✮❀
   ⑥

       Neste caso, apenas os números de 0 a 6 serão impressos.




26


[PAGINA 37]
Casa do Código                                 Capítulo 2. Variáveis e tipos primitivos




  Operadores lógicos

     Você pode e deve usar operadores lógicos em suas expressões
  booleanas sempre que necessário. Por exemplo, repare no código a
  seguir:

  ✐❢ ✭✈✶ ❃ ✈✷✮ ④
      ✐❢ ✭✈✷ ❁ ✈✸✮ ④
          ✴✴ é ❃ q✉❡ ✈✶ ❡ ❁ q✉❡ ✈✸
      ⑥
  ⑥

     Esse encadeamento de ifs prejudica um pouco a legibilidade, não
  acha? Que tal fazer:

  ✐❢ ✭✈✶ ❃ ✈✷ ✫✫ ✈✷ ❁ ✈✸✮ ④
      ✴✴ é ❃ q✉❡ ✈✶ ❡ ❁ q✉❡ ✈✸
  ⑥

      O código terá o mesmo efeito com um único if, agora usando o
  operador and ( &&). Outras opções são o or ( ||) e a negativa ( !). Para
  negar uma condição booleana tudo o que você precisa fazer é adicionar
  o sinal ! antes de sua declaração, veja:

  ❜♦♦❧❡❛♥ ❝♦♥❞✐❝❛♦ ❂ ✶ ❃ ✵❀
  ✐❢ ✭✦❝♦♥❞✐❝❛♦✮ ④
      ✴✴ ♥ã♦ ✈❛✐ ❡♥tr❛r ❛q✉✐
  ⑥




                                                                                   27


[PAGINA 38]


[PAGINA 39]
Capítulo 3

Orientação a objetos
A linguagem Java tem como forte característica ter como paradigma a orien-
tação a objetos, que estudaremos profundamente no decorrer do livro. Esse
paradigma existe desde a década de 70, mas foi depois do surgimento do Java
que ficou bastante famoso e que passou a ser levado mais a sério.
    Repare que nossa CalculadoraDeEstoque está fazendo todo o tra-
balho dentro de seu método main, ainda de forma muito procedural. A ori-
entação a objetos propõe uma maneira diferente de fazer isso, você passa a
trabalhar de um jeito mais próximo à realidade humana. Para cada necessi-
dade importante teremos objetos que interagem entre si e que são compostos
por estado (atributos) e comportamento (métodos). Quer um exemplo? Ob-
serve como estamos representando o preço de nossos livros:

❞♦✉❜❧❡ s♦♠❛ ❂ ✵❀


[PAGINA 40]
3.1. Criando um molde de livros                                  Casa do Código


❢♦r ✭❞♦✉❜❧❡ ✐ ❂ ✵❀ ✐ ❁ ✸✺❀ ✐ ✰✰✮ ④
    s♦♠❛ ✰❂ ✺✾✳✾✵❀
⑥

    O valor 59.90 está fazendo isso. Ele representa o valor do livro; mas, e
quanto ao seu nome, descrição e demais informações? Todas essas infor-
mações representam o que um livro tem e são extremamente importantes
para nosso sistema. O grande problema do paradigma procedural é que não
existe uma forma simples de conectar todos esses elementos, já na orientação
a objetos podemos fazer isso de um jeito muito simples! Assim como no con-
texto real, podemos criar um objeto para representar tudo o que um livro tem
e o que ele faz.


    Uma nova forma de pensar

       Se você já está acostumado com algum outro paradigma, esse é o
    momento de abrir a sua mente. Repare que esse é um paradigma to-
    talmente diferente, você precisará pensar de maneira diferente e escrever
    seu código de outra forma.


3.1     Criando um molde de livros
Vamos criar uma nova classe Java chamada Livro. Essa classe será um
molde, que representará o que um livro deve ter e como ele deve se comportar
em nosso sistema.

♣✉❜❧✐❝ ❝❧❛ss ▲✐✈r♦ ④

⑥

    Para deixar essa classe mais interessante, vamos adicionar alguns campos
para representar o que um livro tem. Esses são os atributos de nossa classe:

♣✉❜❧✐❝ ❝❧❛ss ▲✐✈r♦ ④

      ❙tr✐♥❣ ♥♦♠❡❀

30


[PAGINA 41]
Casa do Código                                      Capítulo 3. Orientação a objetos



     ❙tr✐♥❣ ❞❡s❝r✐❝❛♦❀
     ❞♦✉❜❧❡ ✈❛❧♦r❀
     ❙tr✐♥❣ ✐s❜♥❀
⑥

     Repare que esses atributos são muito parecidos com variáveis que pode-
mos criar dentro de nosso método main, por exemplo. Mas eles não estão
dentro de um bloco e, sim, dentro do escopo da classe, por isso recebem o
nome diferenciado de atributo.
     Nosso molde já está pronto para uso. Por enquanto, um livro terá um
nome, descrição, valor e ISBN (um número de identificação, International
Standard Book Number).
     Esses campos não serão populados na classe Livro, ela é apenas o molde!
O que precisamos é criar um objeto a partir desse molde. Para fazer isso,
utilizamos a palavra-chave new.

▲✐✈r♦ ❧✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦✭✮❀

    Observe que a variável livro tem um tipo, assim como qualquer variável
em Java, mas diferente de um int, double ou String como já estamos
acostumados, agora seu tipo é a própria classe Livro.
    Ao criar um objeto de Livro e atribuir a uma variável livro, estamos
estabelecendo uma forma de nos referenciar a esse objeto que até então não
tem nenhum valor populado.

Populando os atributos do livro
    Agora que fizemos isso, a partir da variável livro, podemos acessar o
objeto que foi criado em memória e popular os seus atributos. Um exemplo
seria:

▲✐✈r♦ ❧✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦✭✮❀
❧✐✈r♦✳♥♦♠❡ ❂ ✧❏❛✈❛ ✽ Prát✐❝♦✧❀
❧✐✈r♦✳❞❡s❝r✐❝❛♦ ❂ ✧◆♦✈♦s r❡❝✉rs♦s ❞❛ ❧✐♥❣✉❛❣❡♠✧❀
❧✐✈r♦✳✈❛❧♦r ❂ ✺✾✳✾✵❀
❧✐✈r♦✳✐s❜♥ ❂ ✧✾✼✽✲✽✺✲✻✻✷✺✵✲✹✻✲✻✧❀



                                                                                 31


[PAGINA 42]
3.1. Criando um molde de livros                                Casa do Código


    Repare que utilizamos um . (ponto) para acessar os atributos desse objeto
em específico. Você também pode recuperar as informações adicionadas nos
seus objetos acessando seus atributos da seguinte forma:

❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❖ ♥♦♠❡ ❞♦ ❧✐✈r♦ é ✧ ✰ ❧✐✈r♦✳♥♦♠❡✮❀

     Neste caso, a saída será:

❖ ♥♦♠❡ ❞♦ ❧✐✈r♦ é ❏❛✈❛ ✽ Prát✐❝♦

    Vamos criar uma nova classe chamada CadastroDeLivros em nosso
projeto. Ela deve ter um método main que cria um novo livro, preenche
alguns de seus atributos e depois imprime os seus valores. Algo como:

♣✉❜❧✐❝ ❝❧❛ss ❈❛❞❛str♦❉❡▲✐✈r♦s ④

      ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④

            ▲✐✈r♦ ❧✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦✭✮❀
            ❧✐✈r♦✳♥♦♠❡ ❂ ✧❏❛✈❛ ✽ Prát✐❝♦✧❀
            ❧✐✈r♦✳❞❡s❝r✐❝❛♦ ❂ ✧◆♦✈♦s r❡❝✉rs♦s ❞❛ ❧✐♥❣✉❛❣❡♠✧❀
            ❧✐✈r♦✳✈❛❧♦r ❂ ✺✾✳✾✵❀
            ❧✐✈r♦✳✐s❜♥ ❂ ✧✾✼✽✲✽✺✲✻✻✷✺✵✲✹✻✲✻✧❀

            ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❧✐✈r♦✳♥♦♠❡✮❀
            ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❧✐✈r♦✳❞❡s❝r✐❝❛♦✮❀
            ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❧✐✈r♦✳✈❛❧♦r✮❀
            ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❧✐✈r♦✳✐s❜♥✮❀
      ⑥
⑥

     Execute a classe para ver a saída! Deverá ser:

❏❛✈❛ ✽ Prát✐❝♦
◆♦✈♦s r❡❝✉rs♦s ❞❛ ❧✐♥❣✉❛❣❡♠
✺✾✳✾
✾✼✽✲✽✺✲✻✻✷✺✵✲✹✻✲✻




32


[PAGINA 43]
Casa do Código                                       Capítulo 3. Orientação a objetos




  Classe x Objeto

      Uma classe é apenas um molde. Uma especificação que define para a
  máquina virtual o que um objeto desse tipo deverá ter e como ele deve
  se comportar. Nossa livraria poderá ter milhares de livros (objetos), mas
  existirá apenas uma classe Livro (molde). Cada objeto que criarmos
  do tipo Livro terá seus próprios valores, ou seja, cada livro terá o seu
  próprio nome, sua descrição, um valor e um número de ISBN.


   Nosso CadastroDeLivros está muito simples, com um único livro.
Vamos criar mais um, já com seus atributos preenchidos:

♣✉❜❧✐❝ ❝❧❛ss ❈❛❞❛str♦❉❡▲✐✈r♦s ④

     ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④

          ▲✐✈r♦ ❧✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦✭✮❀
          ❧✐✈r♦✳♥♦♠❡ ❂ ✧❏❛✈❛ ✽ Prát✐❝♦✧❀
          ❧✐✈r♦✳❞❡s❝r✐❝❛♦ ❂ ✧◆♦✈♦s r❡❝✉rs♦s ❞❛ ❧✐♥❣✉❛❣❡♠✧❀
          ❧✐✈r♦✳✈❛❧♦r ❂ ✺✾✳✾✵❀
          ❧✐✈r♦✳✐s❜♥ ❂ ✧✾✼✽✲✽✺✲✻✻✷✺✵✲✹✻✲✻✧❀

          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❧✐✈r♦✳♥♦♠❡✮❀
          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❧✐✈r♦✳❞❡s❝r✐❝❛♦✮❀
          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❧✐✈r♦✳✈❛❧♦r✮❀
          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❧✐✈r♦✳✐s❜♥✮❀

          ▲✐✈r♦ ♦✉tr♦▲✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦✭✮❀
          ♦✉tr♦▲✐✈r♦✳♥♦♠❡ ❂ ✧▲ó❣✐❝❛ ❞❡ Pr♦❣r❛♠❛çã♦✧❀
          ♦✉tr♦▲✐✈r♦✳❞❡s❝r✐❝❛♦ ❂ ✧❈r✐❡ s❡✉s ♣r✐♠❡✐r♦s ♣r♦❣r❛♠❛s✧❀
          ♦✉tr♦▲✐✈r♦✳✈❛❧♦r ❂ ✺✾✳✾✵❀
          ♦✉tr♦▲✐✈r♦✳✐s❜♥ ❂ ✧✾✼✽✲✽✺✲✻✻✷✺✵✲✷✷✲✵✧❀

          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭♦✉tr♦▲✐✈r♦✳♥♦♠❡✮❀
          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭♦✉tr♦▲✐✈r♦✳❞❡s❝r✐❝❛♦✮❀
          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭♦✉tr♦▲✐✈r♦✳✈❛❧♦r✮❀
          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭♦✉tr♦▲✐✈r♦✳✐s❜♥✮❀

                                                                                  33


[PAGINA 44]
3.2. Criando um novo método                                     Casa do Código




     ⑥
⑥

    Porém, observe que até agora nossa classe Livro só tem atributos, ou
seja, só guarda valores. Vimos que uma classe vai além, ela também pode ter
comportamentos (métodos).


3.2 Criando um novo método
A todo momento que criamos um novo objeto do tipo Livro, estamos im-
primindo seus valores. Essa é uma necessidade comum entre todos os livros
de nosso sistema, mas da forma como estamos fazendo, toda hora repetimos
as mesmas 4 linhas de código:

❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❧✐✈r♦✳♥♦♠❡✮❀
❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❧✐✈r♦✳❞❡s❝r✐❝❛♦✮❀
❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❧✐✈r♦✳✈❛❧♦r✮❀
❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❧✐✈r♦✳✐s❜♥✮❀

    A única coisa que muda é o nome da variável, de livro para
outroLivro.
    Pense na seguinte situação, em breve nosso cadastro terá cerca de 100
livros. Para cada livro, teremos 4 linhas de código imprimindo os seus 4 atrib-
utos. Ou seja, teremos 400 linhas de código muito parecidas, praticamente
repetidas.
    Essa repetição de código sempre tem um efeito colateral de-
sagradável, que é a dificuldade de manutenção. Quer ver? O que
acontece se adicionarmos um novo atributo no livro, por exemplo a
data de seu lançamento? Para imprimir a data toda vez que criar um
livro, teremos que mudar 100 partes de nosso código, adicionando o
System.out.println(livro.dataDeLancamento).
    No lugar de deixar essa lógica de impressão dos dados do livro toda espal-
hada, podemos isolar esse comportamento comum entre os livros na classe
Livro! Para isso, criamos um método. Uma forma seria:



34


[PAGINA 45]
Casa do Código                                      Capítulo 3. Orientação a objetos



✈♦✐❞ ♠♦str❛r❉❡t❛❧❤❡s✭✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭♥♦♠❡✮❀
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❞❡s❝r✐❝❛♦✮❀
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✈❛❧♦r✮❀
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✐s❜♥✮❀
⑥

    Esse método define um comportamento para classe Livro. Repare que
a sintaxe de um método é um pouco diferente do que estamos acostumados,
sua estrutura é:

t✐♣♦❉❡❘❡t♦r♥♦ ♥♦♠❡❉♦❈♦♠♣♦rt❛♠❡♥t♦✭✮ ④

     ✴✴ ❝ó❞✐❣♦ q✉❡ s❡rá ❡①❡❝✉t❛❞♦
⑥

    Nesse caso, não estamos retornando nada e, sim, apenas executando in-
struções dentro do método, portanto, seu tipo de retorno é void. Essa
palavra reservada indica que um método não tem retorno.
    Um método também pode ter variáveis declaradas, como por exemplo:

✈♦✐❞ ♠♦str❛r❉❡t❛❧❤❡s✭✮ ④
    ❙tr✐♥❣ ♠❡♥s❛❣❡♠ ❂ ✧▼♦str❛♥❞♦ ❞❡t❛❧❤❡s ❞♦ ❧✐✈r♦ ✧❀
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭♠❡♥s❛❣❡♠✮❀
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭♥♦♠❡✮❀
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❞❡s❝r✐❝❛♦✮❀
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✈❛❧♦r✮❀
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✐s❜♥✮❀
⑥

    A variável mensagem foi declarada dentro do método, logo esse será
seu escopo, ou seja, ela só existirá e poderá ser utilizada dentro do método
mostrarDetalhes.
    Nossa classe Livro ficou desta forma:

♣✉❜❧✐❝ ❝❧❛ss ▲✐✈r♦ ④

     ❙tr✐♥❣ ♥♦♠❡❀
     ❙tr✐♥❣ ❞❡s❝r✐❝❛♦❀

                                                                                 35


[PAGINA 46]
3.2. Criando um novo método                                  Casa do Código


     ❞♦✉❜❧❡ ✈❛❧♦r❀
     ❙tr✐♥❣ ✐s❜♥❀

     ✈♦✐❞ ♠♦str❛r❉❡t❛❧❤❡s✭✮ ④
         ❙tr✐♥❣ ♠❡♥s❛❣❡♠ ❂ ✧▼♦str❛♥❞♦ ❞❡t❛❧❤❡s ❞♦ ❧✐✈r♦ ✧❀
         ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭♠❡♥s❛❣❡♠✮❀
         ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭♥♦♠❡✮❀
         ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❞❡s❝r✐❝❛♦✮❀
         ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✈❛❧♦r✮❀
         ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✐s❜♥✮❀
     ⑥
⑥

    Agora que cada livro possui o comportamento de exibir os seus detalhes,
podemos remover as linhas que faziam esse trabalho no método main e pas-
sar a invocar esse novo método. Repare:

♣✉❜❧✐❝ ❝❧❛ss ❈❛❞❛str♦❉❡▲✐✈r♦s ④

     ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④

           ▲✐✈r♦ ❧✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦✭✮❀
           ❧✐✈r♦✳♥♦♠❡ ❂ ✧❏❛✈❛ ✽ Prát✐❝♦✧❀
           ❧✐✈r♦✳❞❡s❝r✐❝❛♦ ❂ ✧◆♦✈♦s r❡❝✉rs♦s ❞❛ ❧✐♥❣✉❛❣❡♠✧❀
           ❧✐✈r♦✳✈❛❧♦r ❂ ✺✾✳✾✵❀
           ❧✐✈r♦✳✐s❜♥ ❂ ✧✾✼✽✲✽✺✲✻✻✷✺✵✲✹✻✲✻✧❀

           ❧✐✈r♦✳♠♦str❛r❉❡t❛❧❤❡s✭✮❀

           ▲✐✈r♦ ♦✉tr♦▲✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦✭✮❀
           ♦✉tr♦▲✐✈r♦✳♥♦♠❡ ❂ ✧▲ó❣✐❝❛ ❞❡ Pr♦❣r❛♠❛çã♦✧❀
           ♦✉tr♦▲✐✈r♦✳❞❡s❝r✐❝❛♦ ❂ ✧❈r✐❡ s❡✉s ♣r✐♠❡✐r♦s ♣r♦❣r❛♠❛s✧❀
           ♦✉tr♦▲✐✈r♦✳✈❛❧♦r ❂ ✺✾✳✾✵❀
           ♦✉tr♦▲✐✈r♦✳✐s❜♥ ❂ ✧✾✼✽✲✽✺✲✻✻✷✺✵✲✷✷✲✵✧❀

           ♦✉tr♦▲✐✈r♦✳♠♦str❛r❉❡t❛❧❤❡s✭✮❀
     ⑥
⑥



36


[PAGINA 47]
Casa do Código                                    Capítulo 3. Orientação a objetos



    Ao isolar esse comportamento dentro da classe Livro já tivemos um
ganho evidente. Tivemos que escrever menos linhas em nosso main, o
código ficou com menos repetições pois teve maior reaproveitamento. Mas
essa não é a única vantagem em isolar um comportamento: mesmo que eu
tenha 100 livros cadastrados e use o método mostrarDetalhes 100 vezes,
em quantas partes do meu código eu terei que mexer para modificar a forma
como os livros são exibidos? A resposta é: uma!
    Agora que o comportamento está isolado, só precisaremos alterar o
método, um único ponto do nosso código, para refletir a mudança em to-
dos os lugares que o usam. Vamos colocar isso em prática, basta mudar o
método mostrarDetalhes para:
✈♦✐❞ ♠♦str❛r❉❡t❛❧❤❡s✭✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧▼♦str❛♥❞♦ ❞❡t❛❧❤❡s ❞♦ ❧✐✈r♦ ✧✮❀
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧◆♦♠❡✿ ✧ ✰ ♥♦♠❡✮❀
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❉❡s❝r✐çã♦✿ ✧ ✰ ❞❡s❝r✐❝❛♦✮❀
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❱❛❧♦r✿ ✧ ✰ ✈❛❧♦r✮❀
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧■❙❇◆✿ ✧ ✰ ✐s❜♥✮❀
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧✲✲✧✮❀
⑥

    Execute agora o main da classe CadastroDeLivros. Sem precisar mu-
dar nenhuma linha de seu código, o resultado será:
▼♦str❛♥❞♦ ❞❡t❛❧❤❡s ❞♦ ❧✐✈r♦
◆♦♠❡✿ ❏❛✈❛ ✽ Prát✐❝♦
❉❡s❝r✐çã♦✿ ◆♦✈♦s r❡❝✉rs♦s ❞❛ ❧✐♥❣✉❛❣❡♠
❱❛❧♦r✿ ✺✾✳✾
■❙❇◆✿ ✾✼✽✲✽✺✲✻✻✷✺✵✲✹✻✲✻
✲✲
▼♦str❛♥❞♦ ❞❡t❛❧❤❡s ❞♦ ❧✐✈r♦
◆♦♠❡✿ ▲ó❣✐❝❛ ❞❡ Pr♦❣r❛♠❛çã♦
❉❡s❝r✐çã♦✿ ❈r✐❡ s❡✉s ♣r✐♠❡✐r♦s ♣r♦❣r❛♠❛s
❱❛❧♦r✿ ✺✾✳✾
■❙❇◆✿ ✾✼✽✲✽✺✲✻✻✷✺✵✲✷✷✲✵
✲✲

   Nosso código agora tem uma manutenabilidade muito maior! Sempre
devemos criar métodos de forma genérica e reaproveitável, assim será muito

                                                                               37


[PAGINA 48]
3.3. Objetos para todos os lados!                             Casa do Código


mais fácil e produtivo evoluir o código no futuro.


3.3      Objetos para todos os lados!
Falando em evoluir código, precisamos saber mais informações sobre nos-
sos livros. Por exemplo, quem escreveu o livro? Qual o e-mail do autor? E
quando foi a sua data de publicação? Todas essas informações são relevantes
para nossa livraria e também para nossos clientes. Podemos adicionar essas e
outras informações na classe Livro:

♣✉❜❧✐❝ ❝❧❛ss ▲✐✈r♦ ④

      ❙tr✐♥❣ ♥♦♠❡❀
      ❙tr✐♥❣ ❞❡s❝r✐❝❛♦❀
      ❞♦✉❜❧❡ ✈❛❧♦r❀
      ❙tr✐♥❣ ✐s❜♥❀
      ❙tr✐♥❣ ♥♦♠❡❉♦❆✉t♦r❀
      ❙tr✐♥❣ ❡♠❛✐❧❉♦❆✉t♦r❀
      ❙tr✐♥❣ ❝♣❢❉♦❆✉t♦r❀

      ✈♦✐❞ ♠♦str❛r❉❡t❛❧❤❡s✭✮ ④
          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧▼♦str❛♥❞♦ ❞❡t❛❧❤❡s ❞♦ ❧✐✈r♦ ✧✮❀
          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧◆♦♠❡✿ ✧ ✰ ♥♦♠❡✮❀
          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❉❡s❝r✐çã♦✿ ✧ ✰ ❞❡s❝r✐❝❛♦✮❀
          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❱❛❧♦r✿ ✧ ✰ ✈❛❧♦r✮❀
          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧■❙❇◆✿ ✧ ✰ ✐s❜♥✮❀
          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧✲✲✧✮❀
      ⑥
⑥

    Mas repare que todas essas novas informações pertencem ao autor do
livro e não necessariamente ao livro. Se autor é um elemento importante
para nosso sistema, ele pode e deve ser representado como um objeto! Vamos
fazer essa alteração, basta criar a classe Autor e declarar seus atributos:

♣✉❜❧✐❝ ❝❧❛ss ❆✉t♦r ④

      ❙tr✐♥❣ ♥♦♠❡❀

38


[PAGINA 49]
Casa do Código                                    Capítulo 3. Orientação a objetos



     ❙tr✐♥❣ ❡♠❛✐❧❀
     ❙tr✐♥❣ ❝♣❢❀
⑥

   Portanto, podemos adicionar na classe Livro um atributo do tipo
Autor, que acabamos de criar. Uma classe pode ter outra classe como atrib-
uto, esse é um processo natural conhecido como composição. Nosso código
fica assim:

♣✉❜❧✐❝ ❝❧❛ss ▲✐✈r♦ ④

     ❙tr✐♥❣ ♥♦♠❡❀
     ❙tr✐♥❣ ❞❡s❝r✐❝❛♦❀
     ❞♦✉❜❧❡ ✈❛❧♦r❀
     ❙tr✐♥❣ ✐s❜♥❀
     ❆✉t♦r ❛✉t♦r❀

     ✈♦✐❞ ♠♦str❛r❉❡t❛❧❤❡s✭✮ ④
         ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧▼♦str❛♥❞♦ ❞❡t❛❧❤❡s ❞♦ ❧✐✈r♦ ✧✮❀
         ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧◆♦♠❡✿ ✧ ✰ ♥♦♠❡✮❀
         ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❉❡s❝r✐çã♦✿ ✧ ✰ ❞❡s❝r✐❝❛♦✮❀
         ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❱❛❧♦r✿ ✧ ✰ ✈❛❧♦r✮❀
         ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧■❙❇◆✿ ✧ ✰ ✐s❜♥✮❀
         ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧✲✲✧✮❀
     ⑥
⑥

    Vamos agora criar alguns autores no CadastroDeLivros e associar ao
seu devido livro. Uma forma de fazer isso seria:

❆✉t♦r ❛✉t♦r ❂ ♥❡✇ ❆✉t♦r✭✮❀
❛✉t♦r✳♥♦♠❡ ❂ ✧❘♦❞r✐❣♦ ❚✉r✐♥✐✧❀
❛✉t♦r✳❡♠❛✐❧ ❂ ✧r♦❞r✐❣♦✳t✉r✐♥✐❅❝❛❡❧✉♠✳❝♦♠✳❜r✧❀
❛✉t♦r✳❝♣❢ ❂ ✧✶✷✸✳✹✺✻✳✼✽✾✳✶✵✧❀

    Nesse código, apenas criamos o autor e populamos os seus atributos.
Agora precisamos associar esse objeto ao seu livro. Podemos simplesmente
fazer:

❧✐✈r♦✳❛✉t♦r ❂ ❛✉t♦r❀

                                                                               39


[PAGINA 50]
3.3. Objetos para todos os lados!                          Casa do Código


    Vamos fazer isso com os dois livros, nosso código completo deve ficar
parecido com:

♣✉❜❧✐❝ ❝❧❛ss ❈❛❞❛str♦❉❡▲✐✈r♦s ④

      ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④

             ❆✉t♦r ❛✉t♦r ❂ ♥❡✇ ❆✉t♦r✭✮❀
             ❛✉t♦r✳♥♦♠❡ ❂ ✧❘♦❞r✐❣♦ ❚✉r✐♥✐✧❀
             ❛✉t♦r✳❡♠❛✐❧ ❂ ✧r♦❞r✐❣♦✳t✉r✐♥✐❅❝❛❡❧✉♠✳❝♦♠✳❜r✧❀
             ❛✉t♦r✳❝♣❢ ❂ ✧✶✷✸✳✹✺✻✳✼✽✾✳✶✵✧❀

             ▲✐✈r♦ ❧✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦✭✮❀
             ❧✐✈r♦✳♥♦♠❡ ❂ ✧❏❛✈❛ ✽ Prát✐❝♦✧❀
             ❧✐✈r♦✳❞❡s❝r✐❝❛♦ ❂ ✧◆♦✈♦s r❡❝✉rs♦s ❞❛ ❧✐♥❣✉❛❣❡♠✧❀
             ❧✐✈r♦✳✈❛❧♦r ❂ ✺✾✳✾✵❀
             ❧✐✈r♦✳✐s❜♥ ❂ ✧✾✼✽✲✽✺✲✻✻✷✺✵✲✹✻✲✻✧❀

             ❧✐✈r♦✳❛✉t♦r ❂ ❛✉t♦r❀

             ❧✐✈r♦✳♠♦str❛r❉❡t❛❧❤❡s✭✮❀

             ❆✉t♦r ♦✉tr♦❆✉t♦r ❂ ♥❡✇ ❆✉t♦r✭✮❀
             ♦✉tr♦❆✉t♦r✳♥♦♠❡ ❂ ✧P❛✉❧♦ ❙✐❧✈❡✐r❛✧❀
             ♦✉tr♦❆✉t♦r✳❡♠❛✐❧ ❂ ✧♣❛✉❧♦✳s✐❧✈❡✐r❛❅❝❛❡❧✉♠✳❝♦♠✳❜r✧❀
             ♦✉tr♦❆✉t♦r✳❝♣❢ ❂ ✧✶✷✸✳✹✺✻✳✼✽✾✳✶✵✧❀

             ▲✐✈r♦ ♦✉tr♦▲✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦✭✮❀
             ♦✉tr♦▲✐✈r♦✳♥♦♠❡ ❂ ✧▲ó❣✐❝❛ ❞❡ Pr♦❣r❛♠❛çã♦✧❀
             ♦✉tr♦▲✐✈r♦✳❞❡s❝r✐❝❛♦ ❂ ✧❈r✐❡ s❡✉s ♣r✐♠❡✐r♦s ♣r♦❣r❛♠❛s✧❀
             ♦✉tr♦▲✐✈r♦✳✈❛❧♦r ❂ ✺✾✳✾✵❀
             ♦✉tr♦▲✐✈r♦✳✐s❜♥ ❂ ✧✾✼✽✲✽✺✲✻✻✷✺✵✲✷✷✲✵✧❀

             ♦✉tr♦▲✐✈r♦✳❛✉t♦r ❂ ♦✉tr♦❆✉t♦r❀

             ♦✉tr♦▲✐✈r♦✳♠♦str❛r❉❡t❛❧❤❡s✭✮❀
      ⑥
⑥



40


[PAGINA 51]
Casa do Código                                       Capítulo 3. Orientação a objetos



Referência a objetos
    É fundamental perceber que, quando instanciamos um novo objeto com a
palavra reservada new, um Autor por exemplo, guardamos em sua variável
uma referência para esse objeto, e não seus valores. Ou seja, a variável autor
não guarda o valor de um nome, email e outros atributos da classe Autor,
mas sim uma forma de acessar esses atributos do autor em memória. Muito
diferente de quando trabalhamos com tipos primitivos que guardam uma
cópia do valor.
    Ainda não ficou claro? Observe o seguinte exemplo:
♣✉❜❧✐❝ ❝❧❛ss ❈♦♠♣❛r❛♥❞♦❘❡❢❡r❡♥❝✐❛s ④

     ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④

          ❆✉t♦r ❛✉t♦r ❂ ♥❡✇ ❆✉t♦r✭✮❀
          ❛✉t♦r✳♥♦♠❡ ❂ ✧❘♦❞r✐❣♦ ❚✉r✐♥✐✧❀
          ❛✉t♦r✳❡♠❛✐❧ ❂ ✧r♦❞r✐❣♦✳t✉r✐♥✐❅❝❛❡❧✉♠✳❝♦♠✳❜r✧❀
          ❛✉t♦r✳❝♣❢ ❂ ✧✶✷✸✳✹✺✻✳✼✽✾✳✶✵✧❀

          ❆✉t♦r ❛✉t♦r✷ ❂ ♥❡✇ ❆✉t♦r✭✮❀
          ❛✉t♦r✷✳♥♦♠❡ ❂ ✧❘♦❞r✐❣♦ ❚✉r✐♥✐✧❀
          ❛✉t♦r✷✳❡♠❛✐❧ ❂ ✧r♦❞r✐❣♦✳t✉r✐♥✐❅❝❛❡❧✉♠✳❝♦♠✳❜r✧❀
          ❛✉t♦r✷✳❝♣❢ ❂ ✧✶✷✸✳✹✺✻✳✼✽✾✳✶✵✧❀

     ⑥
⑥

   Aqui estamos criando dois autores com as mesmas informações, mas o
que acontece se eu compará-los da seguinte forma?
✐❢ ✭❛✉t♦r ❂❂ ❛✉t♦r✷✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧■❣✉❛✐s✱ ♠❡s♠♦ ❛✉t♦r✦✧✮❀
⑥ ❡❧s❡ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❤❡✐♥✦❄ P♦r q✉❡ ❞✐❢❡r❡♥t❡s❄✧✮❀
⑥

    Rode o código para conferir o resultado! A saída será:
❤❡✐♥✦❄ P♦r q✉❡ ❞✐❢❡r❡♥t❡s❄

                                                                                  41


[PAGINA 52]
3.3. Objetos para todos os lados!                           Casa do Código


    A resposta é simples, quando comparamos utilizando o == estamos com-
parando o valor da variável, que sempre será a referência (endereço) para
onde encontrar o objeto na memória. E ,claro, cada objeto que criamos fica
em um endereço diferente na memória.
    A imagem a seguir representa os objetos em memória e cada variável de
referência:




     Que ir além? Observe esse código:
❆✉t♦r ❛✉t♦r ❂ ♥❡✇ ❆✉t♦r✭✮❀
❛✉t♦r✳♥♦♠❡ ❂ ✧❘♦❞r✐❣♦ ❚✉r✐♥✐✧❀

▲✐✈r♦ ❧✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦✭✮❀
❧✐✈r♦✳❛✉t♦r ❂ ❛✉t♦r❀

❧✐✈r♦✳❛✉t♦r✳♥♦♠❡ ❂ ✧●✉✐❧❤❡r♠❡ ❙✐❧✈❡✐r❛✧❀

❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❛✉t♦r✳♥♦♠❡✮❀

    Estamos criando um autor e adicionando o nome Rodrigo Turini.
Depois disso, criamos um livro e o associamos a esse autor. Mas re-
pare que em seguida mudamos livro.autor.nome para Guilherme

42


[PAGINA 53]
Casa do Código                                    Capítulo 3. Orientação a objetos



Silveira. Qual será a saída ao imprimir o nome do autor original (
autor.nome)?
    Execute o código para ver a saída. Se você estava esperando Rodrigo
Turini, não fique desapontado.
    Acontece que, depois de associar a referência de autor ao livro, es-
tamos atribuindo ao atributo livro.autor o mesmo endereço (referência)
de memória que tem o autor. Ou seja, das duas formas a seguir estamos
acessando o mesmo objeto:
❛✉t♦r✳♥♦♠❡ ❂ ✧❘♦❞r✐❣♦ ❚✉r✐♥✐✧❀
❧✐✈r♦✳❛✉t♦r✳♥♦♠❡ ❂ ✧●✉✐❧❤❡r♠❡ ❙✐❧✈❡✐r❛✧❀




    Achou complicado? Não se preocupe, durante a leitura faremos muitas
atribuições e relacionamentos entre objetos. Afinal, com certeza isso fará
parte de seu dia a dia.

Mais e mais métodos
    Nosso código evoluiu, agora todo Livro pode ter um Autor. Podemos
evoluir nosso método mostrarDetalhes para que ele passe a mostrar as
informações do autor de cada livro. Uma forma de fazer isso seria:

                                                                               43


[PAGINA 54]
3.3. Objetos para todos os lados!                            Casa do Código


✈♦✐❞ ♠♦str❛r❉❡t❛❧❤❡s✭✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧▼♦str❛♥❞♦ ❞❡t❛❧❤❡s ❞♦ ❧✐✈r♦ ✧✮❀
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧◆♦♠❡✿ ✧ ✰ ♥♦♠❡✮❀
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❉❡s❝r✐çã♦✿ ✧ ✰ ❞❡s❝r✐❝❛♦✮❀
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❱❛❧♦r✿ ✧ ✰ ✈❛❧♦r✮❀
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧■❙❇◆✿ ✧ ✰ ✐s❜♥✮❀

      ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧▼♦str❛♥❞♦ ❞❡t❛❧❤❡s ❞♦ ❛✉t♦r ✧✮❀
      ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧◆♦♠❡✿ ✧ ✰ ❛✉t♦r✳♥♦♠❡✮❀
      ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❊♠❛✐❧✿ ✧ ✰❛✉t♦r✳❡♠❛✐❧✮❀
      ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❈P❋✿ ✧ ✰ ❛✉t♦r✳❝♣❢✮❀
      ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧✲✲✧✮❀
⑥

    Isso funcionaria bem, mas ainda não é a solução ideal. O problema desse
código é que a classe Livro está fazendo mais do que é sua responsabili-
dade. Mostrar as informações de autor deveria ser um comportamento da
classe Autor! E, além disso, o que aconteceria caso nosso próximo objetivo
fosse mostrar apenas os dados de um autor, sem as informações de seu livro?
Teríamos que repetir todas essas ultimas linhas de código! Veja:

❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧▼♦str❛♥❞♦ ❞❡t❛❧❤❡s ❞♦ ❛✉t♦r ✧✮❀
❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧◆♦♠❡✿ ✧ ✰ ❛✉t♦r✳♥♦♠❡✮❀
❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❊♠❛✐❧✿ ✧ ✰❛✉t♦r✳❡♠❛✐❧✮❀
❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❈P❋✿ ✧ ✰ ❛✉t♦r✳❝♣❢✮❀

   Para evitar isso, podemos isolar esse comportamento na classe Autor!
Basta criar um método mostrarDetalhes em seu modelo também:

♣✉❜❧✐❝ ❝❧❛ss ❆✉t♦r ④

      ❙tr✐♥❣ ♥♦♠❡❀
      ❙tr✐♥❣ ❡♠❛✐❧❀
      ❙tr✐♥❣ ❝♣❢❀

      ✈♦✐❞ ♠♦str❛r❉❡t❛❧❤❡s✭✮ ④
          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧▼♦str❛♥❞♦ ❞❡t❛❧❤❡s ❞♦ ❛✉t♦r ✧✮❀
          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧◆♦♠❡✿ ✧ ✰ ♥♦♠❡✮❀
          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❊♠❛✐❧✿ ✧ ✰ ❡♠❛✐❧✮❀

44


[PAGINA 55]
Casa do Código                                      Capítulo 3. Orientação a objetos



          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❈P❋✿ ✧ ✰ ❝♣❢✮❀
     ⑥
⑥

    Pronto! Mais uma vez evitamos repetição de código usando bem a orien-
tação a objetos. Toda classe pode e deve, além de seus atributos, ter compor-
tamentos bem definidos, isolando suas regras de negócio. Podemos agora
remover essas linhas repetidas do método mostrarDetalhes da classe
Livro e apenas delegar a chamada desse novo método:

✈♦✐❞ ♠♦str❛r❉❡t❛❧❤❡s✭✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧▼♦str❛♥❞♦ ❞❡t❛❧❤❡s ❞♦ ❧✐✈r♦ ✧✮❀
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧◆♦♠❡✿ ✧ ✰ ♥♦♠❡✮❀
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❉❡s❝r✐çã♦✿ ✧ ✰ ❞❡s❝r✐❝❛♦✮❀
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❱❛❧♦r✿ ✧ ✰ ✈❛❧♦r✮❀
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧■❙❇◆✿ ✧ ✰ ✐s❜♥✮❀
    ❛✉t♦r✳♠♦str❛r❉❡t❛❧❤❡s✭✮❀
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧✲✲✧✮❀
⑥

    Depois de fazer essas mudanças, vamos executar mais uma vez a classe
CadastroDeLivros. A saída será:

▼♦str❛♥❞♦ ❞❡t❛❧❤❡s ❞♦ ❧✐✈r♦
◆♦♠❡✿ ❏❛✈❛ ✽ Prát✐❝♦
❉❡s❝r✐çã♦✿ ◆♦✈♦s r❡❝✉rs♦s ❞❛ ❧✐♥❣✉❛❣❡♠
❱❛❧♦r✿ ✺✾✳✾
■❙❇◆✿ ✾✼✽✲✽✺✲✻✻✷✺✵✲✹✻✲✻
▼♦str❛♥❞♦ ❞❡t❛❧❤❡s ❞♦ ❛✉t♦r
◆♦♠❡✿ ❘♦❞r✐❣♦ ❚✉r✐♥✐
❊♠❛✐❧✿ r♦❞r✐❣♦✳t✉r✐♥✐❅❝❛❡❧✉♠✳❝♦♠✳❜r
❈P❋✿ ✶✷✸✳✹✺✻✳✼✽✾✳✶✵
✲✲
▼♦str❛♥❞♦ ❞❡t❛❧❤❡s ❞♦ ❧✐✈r♦
◆♦♠❡✿ ▲ó❣✐❝❛ ❞❡ Pr♦❣r❛♠❛çã♦
❉❡s❝r✐çã♦✿ ❈r✐❡ s❡✉s ♣r✐♠❡✐r♦s ♣r♦❣r❛♠❛s
❱❛❧♦r✿ ✺✾✳✾
■❙❇◆✿ ✾✼✽✲✽✺✲✻✻✷✺✵✲✷✷✲✵
▼♦str❛♥❞♦ ❞❡t❛❧❤❡s ❞♦ ❛✉t♦r

                                                                                 45


[PAGINA 56]
3.3. Objetos para todos os lados!                              Casa do Código


◆♦♠❡✿ P❛✉❧♦ ❙✐❧✈❡✐r❛
❊♠❛✐❧✿ ♣❛✉❧♦✳s✐❧✈❡✐r❛❅❝❛❡❧✉♠✳❝♦♠✳❜r
❈P❋✿ ✶✷✸✳✹✺✻✳✼✽✾✳✶✵
✲✲

Métodos com parâmetro
    Depois de instanciado, um objeto do tipo Livro pode precisar ter seu
valor ajustado. É comum aplicar um desconto no preço de um livro, por ex-
emplo. Podemos escrever o seguinte código para aplicar 10% de desconto no
valor de um livro:

♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④

      ▲✐✈r♦ ❧✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦✭✮❀
      ❧✐✈r♦✳✈❛❧♦r ❂ ✺✾✳✾✵❀

      ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❱❛❧♦r ❛t✉❛❧✿ ✧ ✰ ❧✐✈r♦✳✈❛❧♦r✮❀

      ❧✐✈r♦✳✈❛❧♦r ✲❂ ❧✐✈r♦✳✈❛❧♦r ✯ ✵✳✶❀

      ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❱❛❧♦r ❝♦♠ ❞❡s❝♦♥t♦✿ ✧ ✰ ❧✐✈r♦✳✈❛❧♦r✮❀
⑥

    Note que a linha abaixo está calculando a porcentagem de desconto e já
subtraindo do valor do livro.

❧✐✈r♦✳✈❛❧♦r ✲❂ ❧✐✈r♦✳✈❛❧♦r ✯ ✵✳✶❀

     Executando o código, teremos a saída esperada, que é:

❱❛❧♦r ❛t✉❛❧✿ ✺✾✳✾
❱❛❧♦r ❝♦♠ ❞❡s❝♦♥t♦✿ ✺✸✳✾✶

    Mas esse código não está nem um pouco orientado a objetos, estamos
escrevendo um comportamento do livro direto no método main! Já vimos
qual o problema em fazer isso, imagine que existam 100 livros e eu aplique
desconto em todos eles. A nossa lógica de aplicar desconto vai ficar repetida
e espalhada por todo o código.

46


[PAGINA 57]
Casa do Código                                    Capítulo 3. Orientação a objetos



   Como evitar isso? Se aplicar um desconto em seu valor é um comporta-
mento do livro, podemos isolar esse comportamento em um novo método!
No lugar de fazer:

❧✐✈r♦✳✈❛❧♦r ✲❂ ❧✐✈r♦✳✈❛❧♦r ✯ ✵✳✶❀

   Podemos criar um método aplicaDescontoDe que recebe um valor
como parâmetro. Repare:

❧✐✈r♦✳❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭✵✳✶✮❀

    Sim, um método pode e deve receber parâmetros sempre que for preciso.
Veja como fica a sua implementação:

♣✉❜❧✐❝ ✈♦✐❞ ❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭❞♦✉❜❧❡ ♣♦r❝❡♥t❛❣❡♠✮ ④
    ✈❛❧♦r ✲❂ ✈❛❧♦r ✯ ♣♦r❝❡♥t❛❣❡♠❀
⑥

    Note que todo parâmetro de método também precisa ter um nome e
tipo definido. A porcentagem receberá o valor 0.1 ( double) que foi pas-
sado como argumento no momento em que o método foi invocado em nosso
método main.




                                                                              47


[PAGINA 58]
3.3. Objetos para todos os lados!                                Casa do Código




   Nomes ambíguos e o T H I S

     O que aconteceria se o nome do parâmetro do método fosse igual ao
   nome do atributo da classe? Veja como ficaria o nosso código:

   ♣✉❜❧✐❝ ✈♦✐❞ ❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭❞♦✉❜❧❡ ✈❛❧♦r✮ ④
       ✈❛❧♦r ✲❂ ✈❛❧♦r ✯ ✈❛❧♦r❀
   ⑥

       No lugar de uma porcentagem, chamamos o parâmetro de valor,
   assim como o nome do atributo da classe Livro. Como o Java vai saber
   qual valor queremos atualizar? A resposta é: ele não vai. Nosso código
   vai subtrair e multiplicar o valor do parâmetro por ele mesmo, já que este
   tem um escopo menor que o atributo da classe. Ou seja, mesmo com a
   ambiguidade neste caso o código vai compilar, mas o valor considerado
   será o que possui o menor escopo.
       Para evitar esse problema, podemos utilizar a palavra reservada this
   para mostrar que esse é um atributo da classe. Ainda que seja op-
   cional, é sempre uma boa prática usar o this em atributos para evitar
   futuros problemas de ambiguidade e também para deixar claro que este
   é um atributo da classe, e não uma simples variável.


     Com isso, o código de nosso método aplicaDescontoDe fica assim:

♣✉❜❧✐❝ ✈♦✐❞ ❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭❞♦✉❜❧❡ ♣♦r❝❡♥t❛❣❡♠✮ ④
    t❤✐s✳✈❛❧♦r ✲❂ t❤✐s✳✈❛❧♦r ✯ ♣♦r❝❡♥t❛❣❡♠❀
⑥

     E a classe Livro completa:

♣✉❜❧✐❝ ❝❧❛ss ▲✐✈r♦ ④

      ❙tr✐♥❣ ♥♦♠❡❀
      ❙tr✐♥❣ ❞❡s❝r✐❝❛♦❀
      ❞♦✉❜❧❡ ✈❛❧♦r❀
      ❙tr✐♥❣ ✐s❜♥❀
      ❆✉t♦r ❛✉t♦r❀

48


[PAGINA 59]
Casa do Código                                    Capítulo 3. Orientação a objetos




     ✈♦✐❞ ♠♦str❛r❉❡t❛❧❤❡s✭✮ ④
         ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧▼♦str❛♥❞♦ ❞❡t❛❧❤❡s ❞♦ ❧✐✈r♦ ✧✮❀
         ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧◆♦♠❡✿ ✧ ✰ ♥♦♠❡✮❀
         ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❉❡s❝r✐çã♦✿ ✧ ✰ ❞❡s❝r✐❝❛♦✮❀
         ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❱❛❧♦r✿ ✧ ✰ ✈❛❧♦r✮❀
         ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧■❙❇◆✿ ✧ ✰ ✐s❜♥✮❀
         ❛✉t♦r✳♠♦str❛r❉❡t❛❧❤❡s✭✮❀
         ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧✲✲✧✮❀
     ⑥

     ♣✉❜❧✐❝ ✈♦✐❞ ❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭❞♦✉❜❧❡ ♣♦r❝❡♥t❛❣❡♠✮ ④
         t❤✐s✳✈❛❧♦r ✲❂ t❤✐s✳✈❛❧♦r ✯ ♣♦r❝❡♥t❛❣❡♠❀
     ⑥
⑥

Métodos com retorno
    Nossa classe Livro já possui dois métodos, mas os dois são void. Vimos
que o void representa a ausência de um retorno, mas há situações em que
precisaremos retornar algo. Por exemplo, como saber se um livro tem ou
não um autor? Um alternativa seria criar um método temAutor, tendo um
boolean como retorno. Observe um exemplo de uso:

✐❢✭❧✐✈r♦✳t❡♠❆✉t♦r✭✮✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t✭✧❖ ♥♦♠❡ ❞♦ ❛✉t♦r ❞❡ss❡ ❧✐✈r♦ é ✧✮❀
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❧✐✈r♦✳❛✉t♦r✳♥♦♠❡✮❀
⑥

    A implementação desse método é bem simples, ele não receberá nenhum
parâmetro e terá o tipo de retorno boolean:

❜♦♦❧❡❛♥ t❡♠❆✉t♦r✭✮④
    ✴✴ ♦ q✉❡ ❢❛③❡r ❛q✉✐❄
⑥

    Mas como saber se o autor do livro existe ou não? Na verdade, é bem
simples: quando um objeto não foi instanciado, ele não tem nenhuma refer-
ência, portanto seu valor será null. Sabendo disso, tudo o que precisamos

                                                                              49


[PAGINA 60]
3.3. Objetos para todos os lados!                            Casa do Código


fazer no corpo do método é retornar um boolean, informando se o atrib-
uto autor é diferente de null. Para retornar um valor, utilizamos a palavra
reservada return:

❜♦♦❧❡❛♥ t❡♠❆✉t♦r✭✮④
    ❜♦♦❧❡❛♥ ♥❛♦❊❤◆✉❧❧ ❂ t❤✐s✳❛✉t♦r ✦❂ ♥✉❧❧❀
    r❡t✉r♥ ♥❛♦❊❤◆✉❧❧❀
⑥

   Podemos fazer isso de uma forma ainda mais simples, retornando direta-
mente a expressão booleana sem a criação da variável naoEhNull:

❜♦♦❧❡❛♥ t❡♠❆✉t♦r✭✮④
    r❡t✉r♥ t❤✐s✳❛✉t♦r ✦❂ ♥✉❧❧❀
⑥

    Agora que o Livro ganhou esse novo comportamento, vamos tirar
proveito dele dentro do método mostrarDetalhes da própria classe. Pode-
mos mostrar os detalhes do autor apenas quando ele existir. Uma forma de
fazer isso seria:

✈♦✐❞ ♠♦str❛r❉❡t❛❧❤❡s✭✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧▼♦str❛♥❞♦ ❞❡t❛❧❤❡s ❞♦ ❧✐✈r♦ ✧✮❀
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧◆♦♠❡✿ ✧ ✰ ♥♦♠❡✮❀
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❉❡s❝r✐çã♦✿ ✧ ✰ ❞❡s❝r✐❝❛♦✮❀
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❱❛❧♦r✿ ✧ ✰ ✈❛❧♦r✮❀
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧■❙❇◆✿ ✧ ✰ ✐s❜♥✮❀

      ✐❢ ✭t❤✐s✳t❡♠❆✉t♦r✭✮✮ ④
          ❛✉t♦r✳♠♦str❛r❉❡t❛❧❤❡s✭✮❀
      ⑥

      ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧✲✲✧✮❀
⑥

    Pronto! Ao imprimir os detalhes de um livro que não tem autor, apenas
os dados do livro serão exibidos.




50


[PAGINA 61]
Casa do Código                                      Capítulo 3. Orientação a objetos



3.4 Entendendo a construção de um objeto
Agora que já conhecemos um pouco sobre objetos, podemos entender melhor
como funciona seu processo de construção. Repare na sintaxe utilizada para
criar um novo Livro:

▲✐✈r♦ ❧✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦✭✮❀

   Quando escrevemos a instrução Livro() seguida da palavra reservada
new, estamos pedindo para a JVM procurar a classe Livro e invocar o seu
construtor, que se parece com:

♣✉❜❧✐❝ ▲✐✈r♦✭✮④
⑥

    Um construtor é bastante parecido com um método comum, mas ele
não é um. Diferente dos métodos, um construtor tem o mesmo nome da
classe e não tem um retorno declarado.
    Mas, se nunca escrevemos esse construtor, quem o fez? Sempre que você
não criar um construtor para suas classes, o compilador fará isso para você.
    Quer uma prova? Vamos utilizar o programa javap que já vem no JDK
para ver o código compilado. Acesse pelo terminal do seu sistema operacional
a pasta bin de seu projeto e rode o comando javap Livro. A saída deverá
se parecer com:

❚✉r✐♥✐❅ ⑦✴❉♦❝✉♠❡♥ts✴✇♦r❦s♣❛❝❡✴❧✐✈r♦✲♦♦ ❃ ❥❛✈❛♣ ▲✐✈r♦
❈♦♠♣✐❧❡❞ ❢r♦♠ ✧▲✐✈r♦✳❥❛✈❛✧
♣✉❜❧✐❝ ❝❧❛ss ▲✐✈r♦ ④
  ❥❛✈❛✳❧❛♥❣✳❙tr✐♥❣ ♥♦♠❡❀
  ❥❛✈❛✳❧❛♥❣✳❙tr✐♥❣ ❞❡s❝r✐❝❛♦❀
  ❞♦✉❜❧❡ ✈❛❧♦r❀
  ❥❛✈❛✳❧❛♥❣✳❙tr✐♥❣ ✐s❜♥❀
  ♣✉❜❧✐❝ ▲✐✈r♦✭✮❀
  ✈♦✐❞ ♠♦str❛r❉❡t❛❧❤❡s✭✮❀
  ♣✉❜❧✐❝ ✈♦✐❞ ❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭❞♦✉❜❧❡✮❀
⑥

   Note que, mesmo sem criar o construtor vazio, ele está presente em nosso
código compilado:

                                                                                 51


[PAGINA 62]
3.4. Entendendo a construção de um objeto                     Casa do Código


♣✉❜❧✐❝ ▲✐✈r♦✭✮❀

    E, sim, todo código que estiver declarado dentro do construtor será ex-
ecutado quando um objeto desse tipo for criado. Por exemplo, o código a
seguir imprime uma mensagem sempre que criarmos um novo Livro:

♣✉❜❧✐❝ ❝❧❛ss ▲✐✈r♦ ④

      ❙tr✐♥❣ ♥♦♠❡❀
      ❙tr✐♥❣ ❞❡s❝r✐❝❛♦❀
      ❞♦✉❜❧❡ ✈❛❧♦r❀
      ❙tr✐♥❣ ✐s❜♥❀
      ❆✉t♦r ❛✉t♦r❀

      ♣✉❜❧✐❝ ▲✐✈r♦✭✮ ④
          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧♥♦✈♦ ❧✐✈r♦ ❝r✐❛❞♦✧✮❀
      ⑥

      ✴✴ ❞❡♠❛✐s ♠ét♦❞♦s ❞❛ ❝❧❛ss❡
⑥

    Para testar, podemos criar alguns livros dentro de um método main e
executar esse código:

♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④
    ▲✐✈r♦ ❧✐✈r♦✶ ❂ ♥❡✇ ▲✐✈r♦✭✮❀
    ▲✐✈r♦ ❧✐✈r♦✷ ❂ ♥❡✇ ▲✐✈r♦✭✮❀
    ▲✐✈r♦ ❧✐✈r♦✸ ❂ ♥❡✇ ▲✐✈r♦✭✮❀
    ▲✐✈r♦ ❧✐✈r♦✹ ❂ ♥❡✇ ▲✐✈r♦✭✮❀
⑥

     Como já é esperado, a saída será:

♥♦✈♦ ❧✐✈r♦ ❝r✐❛❞♦
♥♦✈♦ ❧✐✈r♦ ❝r✐❛❞♦
♥♦✈♦ ❧✐✈r♦ ❝r✐❛❞♦
♥♦✈♦ ❧✐✈r♦ ❝r✐❛❞♦

   Agora que já temos um construtor, o compilador não vai criar mais nen-
hum. Ele só faz isso quando a sua classe não tem nenhum construtor definido.

52


[PAGINA 63]
Casa do Código                                       Capítulo 3. Orientação a objetos



Veremos mais adiante que construtores também podem receber parâmetros
e inicializar os atributos de suas classes.


3.5    Vantagens da orientação a objetos
Vimos neste capitulo apenas algumas das muitas vantagens de se trabalhar
com orientação a objetos. Observe com atenção o código que criamos. Você
vai conseguir perceber que uma das grandes diferenças da OO é que temos
uma forma forte de criar conexão entre informações e funcionalidades. Além
disso, nosso código fica muito mais organizado e evitamos muita repetição.
O que ganhamos? Um código mais flexível e, com isso, mais fácil de evoluir
e manter.
    Esse é só o começo, no decorrer do livro veremos vários conceitos e recur-
sos como encapsulamento, herança, polimorfismo e muitos outros que tornam
o paradigma ainda mais interessante.




                                                                                  53


[PAGINA 64]


[PAGINA 65]
Capítulo 4

Encapsulamento
4.1 Limitando desconto do Livro
Quando criamos o método aplicaDescontoDe na classe Livro, não de-
terminamos a porcentagem total de desconto que um livro pode ter, mas isso é
muito importante para nossa regra de negócio. Um livro pode ter no máximo
30% de desconto.
    Uma forma simples de evoluir nosso método seria:

♣✉❜❧✐❝ ❜♦♦❧❡❛♥ ❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭❞♦✉❜❧❡ ♣♦r❝❡♥t❛❣❡♠✮ ④
    ✐❢ ✭♣♦r❝❡♥t❛❣❡♠ ❃ ✵✳✸✮ ④
        r❡t✉r♥ ❢❛❧s❡❀
    ⑥
    t❤✐s✳✈❛❧♦r ✲❂ t❤✐s✳✈❛❧♦r ✯ ♣♦r❝❡♥t❛❣❡♠❀
    r❡t✉r♥ tr✉❡❀
⑥


[PAGINA 66]
4.1. Limitando desconto do Livro                               Casa do Código


    Repare que agora estamos retornando um boolean para indicar ao
usuário se o desconto foi aplicado ou não. No momento de usá-lo podemos
fazer algo como:
✐❢ ✭✦❧✐✈r♦✳❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭✵✳✶✮✮④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❉❡s❝♦♥t♦ ♥ã♦ ♣♦❞❡ s❡r ♠❛✐♦r ❞♦ q✉❡ ✸✵✪✧✮❀
⑥


     Código flexível e reaproveitável

        O método aplicaDescontoDe poderia, sim, no lugar de retornar
     um boolean já imprimir a mensagem de validação do limite de de-
     sconto, como por exemplo:

     ♣✉❜❧✐❝ ✈♦✐❞ ❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭❞♦✉❜❧❡ ♣♦r❝❡♥t❛❣❡♠✮ ④
         ✐❢ ✭♣♦r❝❡♥t❛❣❡♠ ❃ ✵✳✸✮ ④
             ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❉❡s❝♦♥t♦ ♥ã♦ ♣♦❞❡ s❡r
                 ♠❛✐♦r ❞♦ q✉❡ ✸✵✪✧✮❀
         ⑥
         t❤✐s✳✈❛❧♦r ✲❂ t❤✐s✳✈❛❧♦r ✯ ♣♦r❝❡♥t❛❣❡♠❀
     ⑥

        Com isso, não seria necessário escrever o if em nosso método main,
     mas repare que estamos perdendo a flexibilidade de customizar nos-
     sas mensagens. Será que todos que forem utilizar esse método querem
     mostrar a mensagem Desconto não pode ser maior do que 30%? E se eu
     quiser mudar esse texto dependendo do usuário ou simplesmente não
     mostrar a mensagem de validação em algum momento?
        Lembre-se sempre de evitar deixar informações tão específicas em
     seus moldes, além de não sobrecarregá-los com comportamentos que
     não deveriam ser de sua responsabilidade.

    Pronto! Nossa lógica já está bem definida, agora um livro não pode ter
um desconto maior do que 30%. Mas vamos testá-la para ter certeza. Para
isso, basta criar a classe RegrasDeDesconto com o seguinte cenário:
♣✉❜❧✐❝ ❝❧❛ss ❘❡❣r❛s❉❡❉❡s❝♦♥t♦ ④


56


[PAGINA 67]
Casa do Código                                        Capítulo 4. Encapsulamento



     ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④

          ▲✐✈r♦ ❧✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦✭✮❀
          ❧✐✈r♦✳✈❛❧♦r ❂ ✺✾✳✾✵❀

          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❱❛❧♦r ❛t✉❛❧✿ ✧ ✰ ❧✐✈r♦✳✈❛❧♦r✮❀

          ✐❢ ✭✦❧✐✈r♦✳❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭✵✳✶✮✮④
              ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❉❡s❝♦♥t♦ ♥ã♦ ♣♦❞❡ s❡r
                   ♠❛✐♦r ❞♦ q✉❡ ✸✵✪✧✮❀
          ⑥ ❡❧s❡ ④
              ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❱❛❧♦r ❝♦♠ ❞❡s❝♦♥t♦✿ ✧
                   ✰ ❧✐✈r♦✳✈❛❧♦r✮❀
          ⑥
     ⑥
⑥

    Ao executá-la, teremos o resultado:

❱❛❧♦r ❛t✉❛❧✿ ✺✾✳✾
❱❛❧♦r ❝♦♠ ❞❡s❝♦♥t♦✿ ✺✸✳✾✶

    E, mudando o valor do desconto para 0.4, a saída será:

❱❛❧♦r ❛t✉❛❧✿ ✺✾✳✾
❉❡s❝♦♥t♦ ♥ã♦ ♣♦❞❡ s❡r ♠❛✐♦r ❞♦ q✉❡ ✸✵✪

   Excelente! É exatamente o comportamento que estamos esperando. Mas
há um problema grave. Nada obriga o desenvolvedor a utilizar o método
aplicaDescontoDe, ele poderia perfeitamente escrever o código desta
forma:

♣✉❜❧✐❝ ❝❧❛ss ❘❡❣r❛s❉❡❉❡s❝♦♥t♦ ④

     ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④

          ▲✐✈r♦ ❧✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦✭✮❀
          ❧✐✈r♦✳✈❛❧♦r ❂ ✺✾✳✾✵❀

          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❱❛❧♦r ❛t✉❛❧✿ ✧ ✰ ❧✐✈r♦✳✈❛❧♦r✮❀

                                                                             57


[PAGINA 68]
4.1. Limitando desconto do Livro                              Casa do Código




            ❧✐✈r♦✳✈❛❧♦r ✲❂ ❧✐✈r♦✳✈❛❧♦r ✯ ✵✳✹❀
            ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❱❛❧♦r ❝♦♠ ❞❡s❝♦♥t♦✿ ✧ ✰ ❧✐✈r♦✳✈❛❧♦r✮❀
      ⑥
⑥

    Ele consegue aplicar o desconto de 40% ou mais, independente de nossa
regra de negócio.
    O problema é que o atributo valor da classe Livro pode ser acessado
diretamente e modificado pelas outras lógicas do nosso sistema. Isso é muito
ruim! Como vimos, ao expor nossos dados, estamos abrindo caminho para
que os objetos possam ser modificados independente das condições verifi-
cadas em seus métodos.
    Apesar de ser um problema muito sério, a solução é bastante simples.
Basta modificar a visibilidade do atributo valor, que até então é default
(padrão). Podemos restringir o acesso para esse atributo para que fique
acessível apenas pela própria classe Livro. Repare:

♣✉❜❧✐❝ ❝❧❛ss ▲✐✈r♦ ④

      ♣r✐✈❛t❡ ❞♦✉❜❧❡ ✈❛❧♦r❀

      ✴✴ ♦✉tr♦s ❛tr✐❜✉t♦s ❡ ♠ét♦❞♦s
⑥

    Como estamos utilizando o modificador de visibilidade private,
ninguém mais além da própria classe Livro conseguirá acessar e modificar
esse valor. Portanto, a seguinte linha da classe RegrasDeDesconto não irá
compilar.

❧✐✈r♦✳✈❛❧♦r ✲❂ ❧✐✈r♦✳✈❛❧♦r ✯ ✵✳✹❀

    O erro será The field Livro.valor is not visible. Ótimo,
isso fará com que a única forma de se aplicar um desconto em um livro
seja passando pela nossa regra de negócio, que está isolada no método
aplicaDescontoDe.



58


[PAGINA 69]
Casa do Código                                        Capítulo 4. Encapsulamento




  Modificadores de visibilidade

      Além do private e default (padrão), existem outros modifi-
  cadores de visibilidade. São eles: public e protected. No momento
  certo entenderemos a fundo cada um deles, mas tenha em mente desde
  já que todos eles são diferentes e possuem regras bem específicas.


4.2 Isolando comportamentos
Ao alterar a visibilidade do atributo valor para private todos os lugares
que acessavam esse atributo passaram a não compilar, já que apenas a própria
classe Livro pode fazer isso. Por exemplo, observe como estávamos pas-
sando o valor do livro:

❧✐✈r♦✳✈❛❧♦r ❂ ✺✾✳✾✵❀

   Como esse acesso não pode mais ser feito, precisaremos criar um com-
portamento (método) na classe Livro para fazer a atribuição desse valor.
Poderíamos chamá-lo de adicionaValor.

❧✐✈r♦✳❛❞✐❝✐♦♥❛❱❛❧♦r✭✺✾✳✾✵✮❀

    Sua implementação será bem simples, observe:

✈♦✐❞ ❛❞✐❝✐♦♥❛❱❛❧♦r✭❞♦✉❜❧❡ ✈❛❧♦r✮ ④
    t❤✐s✳✈❛❧♦r ❂ ✈❛❧♦r❀
⑥

   Há outro erro de compilação que precisaremos resolver. Repare na forma
como estamos imprimindo o valor do Livro:

❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❱❛❧♦r ❛t✉❛❧✿ ✧ ✰ ❧✐✈r♦✳✈❛❧♦r✮❀

    Bem, você já pode ter imaginado que a solução será parecida. Preciso
criar um método retornaValor que não receberá nenhum argumento e
retornará o atributo double valor. Algo como:


                                                                             59


[PAGINA 70]
4.2. Isolando comportamentos                                 Casa do Código


❞♦✉❜❧❡ r❡t♦r♥❛❱❛❧♦r✭✮ ④
    r❡t✉r♥ t❤✐s✳✈❛❧♦r❀
⑥

     E como esse método não recebe parâmetros, o uso do this será opcional.
     Agora podemos imprimir dessa forma:

❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❱❛❧♦r ❛t✉❛❧✿ ✧ ✰ ❧✐✈r♦✳r❡t♦r♥❛❱❛❧♦r✭✮✮❀

Quando usar o private?
    Isso resolveu o problema do valor do livro, mas e quanto aos demais
atributos? Quando devemos deixar um atributo de classe com visibilidade
private? Você deve estar pensando: “quando não quero que ninguém acesse
esse atributo diretamente
    , e é verdade. Mas a questão é: quando eu quero que alguém acesse algum
atributo de forma direta?
    O nome do livro está com visibilidade default, portanto estamos adi-
cionando da seguinte forma:

❧✐✈r♦✳♥♦♠❡ ❂ ✧❏❛✈❛ ✽ Prát✐❝♦✧❀

   Considere que depois de alguns meses apareça a necessidade de validar
que a String passada possui ao menos duas letras, caso contrário não será
um nome válido. Ou seja, nosso código precisará fazer algo como:

❧✐✈r♦✳♥♦♠❡ ❂ ✧❏❛✈❛ ✽ Prát✐❝♦✧❀
✐❢✭❧✐✈r♦✳♥♦♠❡✳❧❡♥❣❤t✭✮ ❁ ✷✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧◆♦♠❡ ✐♥✈á❧✐❞♦✧✮❀
⑥

    Repare que o método lenght foi usado para retornar o tamanho de uma
String. Além desse há diversos outros métodos úteis definidos na classe
String, que conheceremos melhor adiante. O importante agora é perce-
ber que, se acessamos o atributo nome diretamente em mil partes de nosso
código, precisaremos replicar essa mudança em mil lugares. Nada fácil.
    Já vimos que todo comportamento da classe Livro deveria ser isolado
em um método, assim evitamos repetição de código possibilitando o reúso

60


[PAGINA 71]
Casa do Código                                        Capítulo 4. Encapsulamento



desse método por toda a aplicação. O ideal seria desde o começo ter criado
um método adicionaNome com esse comportamento.
    Mas apenas criar o método adicionaNome não teria resolvido o prob-
lema, percebe? Se a visibilidade do atributo ainda fosse default, haveria
duas formas de se adicionar um nome ao livro e nossa lógica de adicionar
nome ainda poderia estar espalhada pela aplicação.
    Como garantir que isso nunca aconteça? Usando private sempre! Todo
atributo de classe deve ser privado, assim garantimos que ninguém os acesse
diretamente e viole as nossas regras de negócio.


4.3 Código encapsulado
Essa mudança que iniciamos em nossa classe faz parte de um conceito muito
importante da OO conhecido como encapsulamento. A ideia é simplesmente
esconder todos os atributos de suas classes (deixando-os private) e encap-
sular seus comportamentos em métodos. Além disso, encapsular é esconder
como funcionam suas regras de negócio, os seus métodos.
    Um bom termômetro para descobrir se o seu código está bem encapsu-
lado é fazendo as duas perguntas:

    • O que esse código faz?

    • Como esse código faz?

    Veja por exemplo quando aplicamos o desconto acessando o atributo di-
retamente:

❧✐✈r♦✳✈❛❧♦r ✲❂ ❧✐✈r♦✳✈❛❧♦r ✯ ✵✳✹❀

    Olhando para esse código, nós conseguimos responder as duas perguntas:
o que e como é feito, mas em um código bem encapsulado você só deveria
conseguir responder a primeira.
    Observe este segundo exemplo:

❧✐✈r♦✳❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭✵✳✶✮❀



                                                                             61


[PAGINA 72]
4.4. Getters e Setters                                         Casa do Código


    Repare que fica claro o que o método aplicaDescontoDe está fazendo,
mas apenas olhando para ele não conseguimos responder como isto será feito.
Se em algum momento no futuro resolvermos mandar um e-mail sempre que
algum desconto for aplicado, não precisaremos mudar milhares de partes de
nosso código, mas sim esse único método que está bem encapsulado. Por-
tanto, o encapsulamento deixa nosso código muito mais passível de mu-
danças.


   Interface da classe

       Os métodos públicos existentes em sua classe são comumente chama-
   dos de interface da classe, afinal em um código encapsulado eles são a
   única maneira de você interagir com os objetos dessa classe.
       Pensar em algum contexto do mundo real pode ajudar a entender en-
   capsulamento e interface da classe. Por exemplo, quando você vai escr-
   ever um texto em um computador, o que importa é o teclado (a interface
   que você usa para fazer isso). Pouco importa como ele funciona interna-
   mente. Quando você mudar de computador ou simplesmente de tipo de
   teclado, não precisará reaprender a usar um teclado.
       Por mais diferente que eles funcionem internamente, isso não fará
   diferença para um usuário final. Ninguém precisa desmontar a lateral
   de um computador e manualmente mudar os circuitos para que o com-
   putador possa interpretar os sinais enviados e mostrar os dados na tela,
   afinal esse comportamento está muito bem encapsulado na interface do
   teclado.


4.4       Getters e Setters
Se todos os atributos de nossas classes forem private, precisaremos criar
um método sempre que quisermos que alguém consiga adicionar um valor
ao atributo e o mesmo quando quisermos que alguém consiga ler e ex-
ibir este valor. Assim como fizemos com os métodos adicionaValor e
retornaValor.
    A convenção de nome para esses dois métodos é utilizar o prefixo get

62


[PAGINA 73]
Casa do Código                                           Capítulo 4. Encapsulamento



(pegar) e set (atribuir). Por exemplo, no lugar de chamar os métodos de
adicionaValor e retornaValor, podemos chamá-los de setValor e
getValor, respectivamente.
    Nosso código fica assim:

♣✉❜❧✐❝ ❝❧❛ss ▲✐✈r♦ ④

      ♣r✐✈❛t❡ ❞♦✉❜❧❡ ✈❛❧♦r❀

      ✴✴ ❞❡♠❛✐s ❛tr✐❜✉t♦s ❡ ♠ét♦❞♦s


      ♣✉❜❧✐❝ ❞♦✉❜❧❡ ❣❡t❱❛❧♦r✭✮ ④
          r❡t✉r♥ ✈❛❧♦r❀
      ⑥

      ♣✉❜❧✐❝ ✈♦✐❞ s❡t❱❛❧♦r✭❞♦✉❜❧❡ ✈❛❧♦r✮ ④
          t❤✐s✳✈❛❧♦r ❂ ✈❛❧♦r❀
      ⑥
⑥

    Repare que o método get não recebe nenhum parâmetro e apenas re-
torna o atributo, enquanto o set sempre recebe um parâmetro com o mesmo
tipo do que o atributo que será atualizado.


    Eclipse: GGAS e Autocomplete

        Criar getters e setters pode parecer um processo trabalhoso,
    mas, por ser um padrão de código muito comum, as principais IDEs do
    mercado possuem atalhos e templates que nos ajudam a fazer isso.
        No eclipse, você pode fazer isso de forma muito produtiva utilizando
    o atalho Control + 3 e depois digitando ggas. Repare que essas
    são as iniciais do comando Generate Getters and Setters. Se-
    lecionando esta opção você poderá escolher para quais atributos criar os
    métodos e clicar em Finish.
        Tudo pronto, o Eclipse gerou o código todo pra você!


                                                                                63


[PAGINA 74]
4.4. Getters e Setters                                      Casa do Código


    Os getters e setters possibilitam o acesso dos atributos de forma
controlada. Mas é muito importante perceber que nem todo atributo deve ter
um getter e setter, você só deve criar esses métodos quando houver uma
real necessidade. Há um post do Paulo Silveira muito interessante ilustrando
essa situação:
    http://blog.caelum.com.br/2006/09/14/nao-aprender-oo-getters-e-setters/
    Depois de criar os getters e setters necessários, nossa classe Livro
deve ficar assim:

♣✉❜❧✐❝ ❝❧❛ss ▲✐✈r♦ ④

      ♣r✐✈❛t❡ ❙tr✐♥❣ ♥♦♠❡❀
      ♣r✐✈❛t❡ ❙tr✐♥❣ ❞❡s❝r✐❝❛♦❀
      ♣r✐✈❛t❡ ❞♦✉❜❧❡ ✈❛❧♦r❀
      ♣r✐✈❛t❡ ❙tr✐♥❣ ✐s❜♥❀
      ♣r✐✈❛t❡ ❆✉t♦r ❛✉t♦r❀

      ✴✴ ❞❡♠❛✐s ♠ét♦❞♦s ♦♠✐t✐❞♦s

      ♣✉❜❧✐❝ ❞♦✉❜❧❡ ❣❡t❱❛❧♦r✭✮ ④
          r❡t✉r♥ ✈❛❧♦r❀
      ⑥

      ♣✉❜❧✐❝ ✈♦✐❞ s❡t❱❛❧♦r✭❞♦✉❜❧❡ ✈❛❧♦r✮ ④
          t❤✐s✳✈❛❧♦r ❂ ✈❛❧♦r❀
      ⑥

      ♣✉❜❧✐❝ ❙tr✐♥❣ ❣❡t◆♦♠❡✭✮ ④
          r❡t✉r♥ ♥♦♠❡❀
      ⑥

      ♣✉❜❧✐❝ ✈♦✐❞ s❡t◆♦♠❡✭❙tr✐♥❣ ♥♦♠❡✮ ④
          t❤✐s✳♥♦♠❡ ❂ ♥♦♠❡❀
      ⑥

      ♣✉❜❧✐❝ ❙tr✐♥❣ ❣❡t❉❡s❝r✐❝❛♦✭✮ ④
          r❡t✉r♥ ❞❡s❝r✐❝❛♦❀
      ⑥


64


[PAGINA 75]
Casa do Código                                     Capítulo 4. Encapsulamento




     ♣✉❜❧✐❝ ✈♦✐❞ s❡t❉❡s❝r✐❝❛♦✭❙tr✐♥❣ ❞❡s❝r✐❝❛♦✮ ④
         t❤✐s✳❞❡s❝r✐❝❛♦ ❂ ❞❡s❝r✐❝❛♦❀
     ⑥

     ♣✉❜❧✐❝ ❙tr✐♥❣ ❣❡t■s❜♥✭✮ ④
         r❡t✉r♥ ✐s❜♥❀
     ⑥

     ♣✉❜❧✐❝ ✈♦✐❞ s❡t■s❜♥✭❙tr✐♥❣ ✐s❜♥✮ ④
         t❤✐s✳✐s❜♥ ❂ ✐s❜♥❀
     ⑥

     ♣✉❜❧✐❝ ❆✉t♦r ❣❡t❆✉t♦r✭✮ ④
         r❡t✉r♥ ❛✉t♦r❀
     ⑥

     ♣✉❜❧✐❝ ✈♦✐❞ s❡t❆✉t♦r✭❆✉t♦r ❛✉t♦r✮ ④
         t❤✐s✳❛✉t♦r ❂ ❛✉t♦r❀
     ⑥
⑥

    Precisamos fazer o mesmo para nossa classe Autor:
♣✉❜❧✐❝ ❝❧❛ss ❆✉t♦r ④

     ♣r✐✈❛t❡ ❙tr✐♥❣ ♥♦♠❡❀
     ♣r✐✈❛t❡ ❙tr✐♥❣ ❡♠❛✐❧❀
     ♣r✐✈❛t❡ ❙tr✐♥❣ ❝♣❢❀

     ✴✴ ❞❡♠❛✐s ♠ét♦❞♦s ♦♠✐t✐❞♦s

     ♣✉❜❧✐❝ ❙tr✐♥❣ ❣❡t◆♦♠❡✭✮ ④
         r❡t✉r♥ ♥♦♠❡❀
     ⑥

     ♣✉❜❧✐❝ ✈♦✐❞ s❡t◆♦♠❡✭❙tr✐♥❣ ♥♦♠❡✮ ④
         t❤✐s✳♥♦♠❡ ❂ ♥♦♠❡❀
     ⑥


                                                                          65


[PAGINA 76]
4.4. Getters e Setters                                           Casa do Código


      ♣✉❜❧✐❝ ❙tr✐♥❣ ❣❡t❊♠❛✐❧✭✮ ④
          r❡t✉r♥ ❡♠❛✐❧❀
      ⑥

      ♣✉❜❧✐❝ ✈♦✐❞ s❡t❊♠❛✐❧✭❙tr✐♥❣ ❡♠❛✐❧✮ ④
          t❤✐s✳❡♠❛✐❧ ❂ ❡♠❛✐❧❀
      ⑥

      ♣✉❜❧✐❝ ❙tr✐♥❣ ❣❡t❈♣❢✭✮ ④
          r❡t✉r♥ ❝♣❢❀
      ⑥

      ♣✉❜❧✐❝ ✈♦✐❞ s❡t❈♣❢✭❙tr✐♥❣ ❝♣❢✮ ④
          t❤✐s✳❝♣❢ ❂ ❝♣❢❀
      ⑥

⑥

    E, por fim, será necessário modificar a classe CadastroDeLivros para
que deixe de acessar os atributos diretamente. Seu código final deve ficar pare-
cido com:

♣✉❜❧✐❝ ❝❧❛ss ❈❛❞❛str♦❉❡▲✐✈r♦s ④

      ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④

             ❆✉t♦r ❛✉t♦r ❂ ♥❡✇ ❆✉t♦r✭✮❀
             ❛✉t♦r✳s❡t◆♦♠❡✭✧❘♦❞r✐❣♦ ❚✉r✐♥✐✧✮❀
             ❛✉t♦r✳s❡t❊♠❛✐❧✭✧r♦❞r✐❣♦✳t✉r✐♥✐❅❝❛❡❧✉♠✳❝♦♠✳❜r✧✮❀
             ❛✉t♦r✳s❡t❈♣❢✭✧✶✷✸✳✹✺✻✳✼✽✾✳✶✵✧✮❀

             ▲✐✈r♦ ❧✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦✭✮❀
             ❧✐✈r♦✳s❡t◆♦♠❡✭✧❏❛✈❛ ✽ Prát✐❝♦✧✮❀
             ❧✐✈r♦✳s❡t❉❡s❝r✐❝❛♦✭✧◆♦✈♦s r❡❝✉rs♦s ❞❛ ❧✐♥❣✉❛❣❡♠✧✮❀
             ❧✐✈r♦✳s❡t❱❛❧♦r✭✺✾✳✾✵✮❀
             ❧✐✈r♦✳s❡t■s❜♥✭✧✾✼✽✲✽✺✲✻✻✷✺✵✲✹✻✲✻✧✮❀

             ❧✐✈r♦✳s❡t❆✉t♦r✭❛✉t♦r✮❀



66


[PAGINA 77]
Casa do Código                                        Capítulo 4. Encapsulamento



          ❧✐✈r♦✳♠♦str❛r❉❡t❛❧❤❡s✭✮❀

          ❆✉t♦r ♦✉tr♦❆✉t♦r ❂ ♥❡✇ ❆✉t♦r✭✮❀
          ♦✉tr♦❆✉t♦r✳s❡t◆♦♠❡✭✧P❛✉❧♦ ❙✐❧✈❡✐r❛✧✮❀
          ♦✉tr♦❆✉t♦r✳s❡t❊♠❛✐❧✭✧♣❛✉❧♦✳s✐❧✈❡✐r❛❅❝❛❡❧✉♠✳❝♦♠✳❜r✧✮❀
          ♦✉tr♦❆✉t♦r✳s❡t❈♣❢✭✧✶✷✸✳✹✺✻✳✼✽✾✳✶✵✧✮❀

          ▲✐✈r♦ ♦✉tr♦▲✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦✭✮❀
          ♦✉tr♦▲✐✈r♦✳s❡t◆♦♠❡✭✧▲ó❣✐❝❛ ❞❡ Pr♦❣r❛♠❛çã♦✧✮❀
          ♦✉tr♦▲✐✈r♦✳s❡t❉❡s❝r✐❝❛♦✭✧❈r✐❡ s❡✉s ♣r✐♠❡✐r♦s ♣r♦❣r❛♠❛s✧✮❀
          ♦✉tr♦▲✐✈r♦✳s❡t❱❛❧♦r✭✺✾✳✾✵✮❀
          ♦✉tr♦▲✐✈r♦✳s❡t■s❜♥✭✧✾✼✽✲✽✺✲✻✻✷✺✵✲✷✷✲✵✧✮❀

          ♦✉tr♦▲✐✈r♦✳s❡t❆✉t♦r✭♦✉tr♦❆✉t♦r✮❀

          ♦✉tr♦▲✐✈r♦✳♠♦str❛r❉❡t❛❧❤❡s✭✮❀
     ⑥
⑥


4.5 Definindo dependências pelo construtor

Autor é um atributo obrigatório
Agora que nosso código já está bem encapsulado, precisamos atender outra
necessidade de nossa livraria. Todo Livro precisa ter um Autor. Isso é bem
simples: assim como já está sendo feito, logo após criar um livro, podemos
associá-lo ao seu autor pelo método setAutor:
❆✉t♦r ❛✉t♦r ❂ ♥❡✇ ❆✉t♦r✭✮❀
❛✉t♦r✳s❡t◆♦♠❡✭✧❘♦❞r✐❣♦ ❚✉r✐♥✐✧✮❀
✴✴ s❡t ❞♦s ♦✉tr♦s ❛tr✐❜✉t♦s

▲✐✈r♦ ❧✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦✭✮❀
✴✴ s❡t ❞♦s ♦✉tr♦s ❛tr✐❜✉t♦s

❧✐✈r♦✳s❡t❆✉t♦r✭❛✉t♦r✮❀

    Isso já resolve o problema, mas há uma questão. Dessa forma, por alguns
instantes o Livro existe em memória sem ter um Autor relacionado. E

                                                                             67


[PAGINA 78]
4.5. Definindo dependências pelo construtor                   Casa do Código


esse nem é o pior dos problemas, o que acontecerá se esquecermos de chamar
o método setAutor? A resposta é: nada. Ou seja, da forma como nosso
código está escrito, um livro pode existir sem seu autor.
    Como resolver isso? Bem, como já vimos, toda classe tem um
construtor. Ainda que eu não tenha declarado, o compilador fará isso para
mim. O que ainda não vimos é que construtores podem receber parâmetros.
Com isso, podemos obrigar a passagem de alguns valores logo no momento
de criação de nossos objetos.
    Vamos criar um construtor na classe Livro que deve receber um Autor
como parâmetro. Seu código deve ficar assim:

♣✉❜❧✐❝ ▲✐✈r♦✭❆✉t♦r ❛✉t♦r✮ ④
    t❤✐s✳❛✉t♦r ❂ ❛✉t♦r❀
⑥

    Repare que ele ficou com a responsabilidade do método setAutor, que
é atribuir o autor do parâmetro ao atributo da classe.
    A partir do momento em que criamos esse construtor com parâmetro
na classe Livro, o compilador não criará mais o construtor default (vazio).
Portanto, o seguinte código não compila:

▲✐✈r♦ ❧✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦✭✮❀

    Se o único construtor existente na classe recebe um Autor, a única forma
de fazer esse código compilar e criar um Livro será passando um Autor
como argumento. Veja:

❆✉t♦r ❛✉t♦r ❂ ♥❡✇ ❆✉t♦r✭✮❀
❛✉t♦r✳s❡t◆♦♠❡✭✧❘♦❞r✐❣♦ ❚✉r✐♥✐✧✮❀
✴✴ s❡t ❞♦s ♦✉tr♦s ❛tr✐❜✉t♦s

▲✐✈r♦ ❧✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦✭❛✉t♦r✮❀
✴✴ s❡t ❞♦s ♦✉tr♦s ❛tr✐❜✉t♦s

    Claro, há situações em que queremos deixar as duas formas válidas, ou
seja, queremos criar um Livro passando ou não um Autor. Para que isso
funcionasse, precisaríamos adicionar na classe Livro um novo construtor
que não recebe nenhum argumento. Seu código ficaria assim:

68


[PAGINA 79]
Casa do Código                                     Capítulo 4. Encapsulamento



♣✉❜❧✐❝ ❝❧❛ss ▲✐✈r♦ ④

     ♣r✐✈❛t❡ ❙tr✐♥❣ ♥♦♠❡❀
     ♣r✐✈❛t❡ ❙tr✐♥❣ ❞❡s❝r✐❝❛♦❀
     ♣r✐✈❛t❡ ❞♦✉❜❧❡ ✈❛❧♦r❀
     ♣r✐✈❛t❡ ❙tr✐♥❣ ✐s❜♥❀
     ♣r✐✈❛t❡ ❆✉t♦r ❛✉t♦r❀

     ♣✉❜❧✐❝ ▲✐✈r♦✭❆✉t♦r ❛✉t♦r✮ ④
         t❤✐s✳❛✉t♦r ❂ ❛✉t♦r❀
     ⑥

     ♣✉❜❧✐❝ ▲✐✈r♦✭✮ ④
     ⑥

     ✴✴ s❡tt❡rs✱ ❣❡tt❡rs ❡ ♦✉tr♦s ♠ét♦❞♦s
⑥

   Uma classe pode, sim, ter mais de um construtor, isso é conhecido
como uma sobrecarga (overloaded) de construtor. Mas, assim como nos de-
mais métodos, isso funcionará contanto que os construtores não tenham a
mesma quantidade de parâmetro. Por exemplo, se eu tentar fazer:

♣✉❜❧✐❝ ▲✐✈r♦✭✮ ④
⑥

♣✉❜❧✐❝ ▲✐✈r♦✭✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧♥♦✈♦ ❧✐✈r♦ ❝r✐❛❞♦✧✮❀
⑥

    Esse código não compilará, afinal, quando alguém fizer new Livro()
qual dos construtores seria chamado?
    Como nossa regra de negócio exige um Autor para cada Livro, vamos
manter apenas o construtor com parâmetro. Para isso, precisaremos mudar
as nossas classes que criam um novo Livro para atender essa condição. A
classe CadastroDeLivros deve ficar assim:

♣✉❜❧✐❝ ❝❧❛ss ❈❛❞❛str♦❉❡▲✐✈r♦s ④


                                                                         69


[PAGINA 80]
4.5. Definindo dependências pelo construtor             Casa do Código


      ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④

            ❆✉t♦r ❛✉t♦r ❂ ♥❡✇ ❆✉t♦r✭✮❀
            ❛✉t♦r✳s❡t◆♦♠❡✭✧❘♦❞r✐❣♦ ❚✉r✐♥✐✧✮❀
            ❛✉t♦r✳s❡t❊♠❛✐❧✭✧r♦❞r✐❣♦✳t✉r✐♥✐❅❝❛❡❧✉♠✳❝♦♠✳❜r✧✮❀
            ❛✉t♦r✳s❡t❈♣❢✭✧✶✷✸✳✹✺✻✳✼✽✾✳✶✵✧✮❀

            ▲✐✈r♦ ❧✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦✭❛✉t♦r✮❀
            ❧✐✈r♦✳s❡t◆♦♠❡✭✧❏❛✈❛ ✽ Prát✐❝♦✧✮❀
            ❧✐✈r♦✳s❡t❉❡s❝r✐❝❛♦✭✧◆♦✈♦s r❡❝✉rs♦s ❞❛ ❧✐♥❣✉❛❣❡♠✧✮❀
            ❧✐✈r♦✳s❡t❱❛❧♦r✭✺✾✳✾✵✮❀
            ❧✐✈r♦✳s❡t■s❜♥✭✧✾✼✽✲✽✺✲✻✻✷✺✵✲✹✻✲✻✧✮❀

            ❧✐✈r♦✳♠♦str❛r❉❡t❛❧❤❡s✭✮❀

            ❆✉t♦r ♦✉tr♦❆✉t♦r ❂ ♥❡✇ ❆✉t♦r✭✮❀
            ♦✉tr♦❆✉t♦r✳s❡t◆♦♠❡✭✧P❛✉❧♦ ❙✐❧✈❡✐r❛✧✮❀
            ♦✉tr♦❆✉t♦r✳s❡t❊♠❛✐❧✭✧♣❛✉❧♦✳s✐❧✈❡✐r❛❅❝❛❡❧✉♠✳❝♦♠✳❜r✧✮❀
            ♦✉tr♦❆✉t♦r✳s❡t❈♣❢✭✧✶✷✸✳✹✺✻✳✼✽✾✳✶✵✧✮❀

            ▲✐✈r♦ ♦✉tr♦▲✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦✭♦✉tr♦❆✉t♦r✮❀
            ♦✉tr♦▲✐✈r♦✳s❡t◆♦♠❡✭✧▲ó❣✐❝❛ ❞❡ Pr♦❣r❛♠❛çã♦✧✮❀
            ♦✉tr♦▲✐✈r♦✳s❡t❉❡s❝r✐❝❛♦✭✧❈r✐❡ s❡✉s ♣r✐♠❡✐r♦s ♣r♦❣r❛♠❛s✧✮❀
            ♦✉tr♦▲✐✈r♦✳s❡t❱❛❧♦r✭✺✾✳✾✵✮❀
            ♦✉tr♦▲✐✈r♦✳s❡t■s❜♥✭✧✾✼✽✲✽✺✲✻✻✷✺✵✲✷✷✲✵✧✮❀

            ♦✉tr♦▲✐✈r♦✳♠♦str❛r❉❡t❛❧❤❡s✭✮❀
      ⑥
⑥




70


[PAGINA 81]
Casa do Código                                         Capítulo 4. Encapsulamento




  Mantemos ou não o método setAutor?

      Se o construtor já atribuiu o Autor do livro, precisamos manter um
  setter para esse atributo? Isso vai depender de nossa necessidade, claro.
  Pode ser que faça bastante sentido para nossa livraria modificar o autor
  de um livro depois que ele foi criado. Mas fique atento! Você só deve
  manter o setter se ele realmente for necessário, lembre-se da importância
  de manter suas rotinas encapsuladas.


Inicializando atributos da classe
    Por fim, outro ponto que precisamos resolver em nossa livraria
é relacionado ao número de ISBN de nossos livros.         Em nosso
CadastroDeLivros, sempre que criamos um Livro, já atribuímos
seu número de ISBN, mas normalmente esse identificador pode demorar
alguns dias para ficar pronto.
    Repare qual será o resultado do método mostrarDetalhes quando o
ISBN não estiver preenchido:

▼♦str❛♥❞♦ ❞❡t❛❧❤❡s ❞♦ ❧✐✈r♦
◆♦♠❡✿ ❏❛✈❛ ✽ Prát✐❝♦
❉❡s❝r✐çã♦✿ ◆♦✈♦s r❡❝✉rs♦s ❞❛ ❧✐♥❣✉❛❣❡♠
❱❛❧♦r✿ ✺✾✳✾
■❙❇◆✿ ♥✉❧❧
▼♦str❛♥❞♦ ❞❡t❛❧❤❡s ❞♦ ❛✉t♦r
◆♦♠❡✿ ❘♦❞r✐❣♦ ❚✉r✐♥✐
❊♠❛✐❧✿ r♦❞r✐❣♦✳t✉r✐♥✐❅❝❛❡❧✉♠✳❝♦♠✳❜r
❈P❋✿ ✶✷✸✳✹✺✻✳✼✽✾✳✶✵

    O valor null será impresso. Isso acontece pois, diferente dos tipos
primitivos, que sempre possuem um valor padrão (default), objetos como a
String não possuem, portanto, antes de serem inicializadas terão sua refer-
ência igual a null.
    Esse é o valor default de cada tipo primitivo:



                                                                              71


[PAGINA 82]
4.5. Definindo dependências pelo construtor                   Casa do Código




    Outro uso bem comum de um construtor é para inicialização de atrib-
utos, como o caso do ISBN. Para fornecer um valor padrão para este atributo,
poderíamos simplesmente inicializá-lo no construtor da classe:

♣✉❜❧✐❝ ▲✐✈r♦✭❆✉t♦r ❛✉t♦r✮ ④
    t❤✐s✳❛✉t♦r ❂ ❛✉t♦r❀
    t❤✐s✳✐s❜♥ ❂ ✧✵✵✵✲✵✵✲✵✵✵✵✵✲✵✵✲✵✧❀
⑥

    Nesse caso, ao mostrarDetalhes de um Livro sem ISBN, teremos a
saída:

▼♦str❛♥❞♦ ❞❡t❛❧❤❡s ❞♦ ❧✐✈r♦
◆♦♠❡✿ ❏❛✈❛ ✽ Prát✐❝♦
❉❡s❝r✐çã♦✿ ◆♦✈♦s r❡❝✉rs♦s ❞❛ ❧✐♥❣✉❛❣❡♠
❱❛❧♦r✿ ✺✾✳✾

72


[PAGINA 83]
Casa do Código                                      Capítulo 4. Encapsulamento



■❙❇◆✿ ✵✵✵✲✵✵✲✵✵✵✵✵✲✵✵✲✵
▼♦str❛♥❞♦ ❞❡t❛❧❤❡s ❞♦ ❛✉t♦r
◆♦♠❡✿ ❘♦❞r✐❣♦ ❚✉r✐♥✐
❊♠❛✐❧✿ r♦❞r✐❣♦✳t✉r✐♥✐❅❝❛❡❧✉♠✳❝♦♠✳❜r
❈P❋✿ ✶✷✸✳✹✺✻✳✼✽✾✳✶✵


  Delegando para outros construtores

     Repare que, se a classe Livro também tivesse um construtor sem
  argumentos, como a seguir:

  ♣✉❜❧✐❝ ▲✐✈r♦✭❆✉t♦r ❛✉t♦r✮ ④
      t❤✐s✳❛✉t♦r ❂ ❛✉t♦r❀
      t❤✐s✳✐s❜♥ ❂ ✧✵✵✵✲✵✵✲✵✵✵✵✵✲✵✵✲✵✧❀
  ⑥

  ♣✉❜❧✐❝ ▲✐✈r♦✭✮ ④
  ⑥

     O valor de ISBN só seria inicializado quando o construtor com um
  Autor fosse chamado. Para resolver isso, você pode encadear a chamada
  dos construtores utilizando a palavra reservada this, como a seguir:

  ♣✉❜❧✐❝ ▲✐✈r♦✭❆✉t♦r ❛✉t♦r✮ ④
      t❤✐s✭✮❀
      t❤✐s✳❛✉t♦r ❂ ❛✉t♦r❀
  ⑥

  ♣✉❜❧✐❝ ▲✐✈r♦✭✮ ④
      t❤✐s✳✐s❜♥ ❂ ✧✵✵✵✲✵✵✲✵✵✵✵✵✲✵✵✲✵✧❀
  ⑥




                                                                           73


[PAGINA 84]


[PAGINA 85]
Capítulo 5

Herança e polimorfismo
5.1    Trabalhando com livros digitais
Por causa da sua praticidade e fácil portabilidade, muitos leitores preferem
livros digitais (e-books) aos livros físicos. Nossa livraria não pode ficar para
trás, portanto, passaremos a trabalhar com esse novo tipo de livro.
    Mas, afinal, como podemos diferenciar um Livro impresso de um
Ebook? Uma forma simples de fazer isso seria adicionando um atributo que
define o tipo de livro. Poderia simplesmente ser um boolean, marcando se
um livro é impresso ou não. Repare:
♣✉❜❧✐❝ ❝❧❛ss ▲✐✈r♦ ④

      ♣r✐✈❛t❡ ❙tr✐♥❣ ♥♦♠❡❀
      ♣r✐✈❛t❡ ❙tr✐♥❣ ❞❡s❝r✐❝❛♦❀
      ♣r✐✈❛t❡ ❞♦✉❜❧❡ ✈❛❧♦r❀


[PAGINA 86]
5.1. Trabalhando com livros digitais                          Casa do Código


      ♣r✐✈❛t❡ ❙tr✐♥❣ ✐s❜♥❀
      ♣r✐✈❛t❡ ❆✉t♦r ❛✉t♦r❀
      ♣r✐✈❛t❡ ❜♦♦❧❡❛♥ ✐♠♣r❡ss♦❀

      ♣✉❜❧✐❝ ▲✐✈r♦✭❆✉t♦r ❛✉t♦r✮ ④
          t❤✐s✳❛✉t♦r ❂ ❛✉t♦r❀
          t❤✐s✳✐s❜♥ ❂ ✧✵✵✵✲✵✵✲✵✵✵✵✵✲✵✵✲✵✧❀
          t❤✐s✳✐♠♣r❡ss♦ ❂ tr✉❡❀
      ⑥

      ✴✴ ♦✉tr♦s ♠ét♦❞♦s ❞❛ ❝❧❛ss❡
⑥

    Note que em nosso construtor já definimos um valor padrão para o atrib-
uto impresso. Todo Livro que não tenha o valor de impresso definido
será considerado um livro impresso.
    Essa é uma forma simples de resolver o problema e talvez até possa aten-
der bem as nossas necessidades, mas o problema dessa abordagem é que um
Ebook tem alguns comportamentos bastante diferentes do que um livro im-
presso. Por exemplo, o método aplicaDescontoDe da classe Livro at-
ualmente limita a porcentagem de desconto em 30%.

♣✉❜❧✐❝ ❜♦♦❧❡❛♥ ❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭❞♦✉❜❧❡ ♣♦r❝❡♥t❛❣❡♠✮ ④
    ✐❢ ✭♣♦r❝❡♥t❛❣❡♠ ❃ ✵✳✸✮ ④
        r❡t✉r♥ ❢❛❧s❡❀
    ⑥
    t❤✐s✳✈❛❧♦r ✲❂ t❤✐s✳✈❛❧♦r ✯ ♣♦r❝❡♥t❛❣❡♠❀
    r❡t✉r♥ tr✉❡❀
⑥

    Mas quando se trata de um Ebook, a regra é um pouco diferente: pode-
mos aplicar no máximo 15% de desconto. Podemos resolver esse problema
adicionando mais uma condição ao método:

♣✉❜❧✐❝ ❜♦♦❧❡❛♥ ❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭❞♦✉❜❧❡ ♣♦r❝❡♥t❛❣❡♠✮ ④
    ✐❢ ✭♣♦r❝❡♥t❛❣❡♠ ❃ ✵✳✸✮ ④
        r❡t✉r♥ ❢❛❧s❡❀
    ⑥ ❡❧s❡ ✐❢ ✭✦t❤✐s✳✐♠♣r❡ss♦ ✫✫ ♣♦r❝❡♥t❛❣❡♠ ❃ ✵✳✶✺✮ ④
        r❡t✉r♥ ❢❛❧s❡❀

76


[PAGINA 87]
Casa do Código                                   Capítulo 5. Herança e polimorfismo



     ⑥
     t❤✐s✳✈❛❧♦r ✲❂ t❤✐s✳✈❛❧♦r ✯ ♣♦r❝❡♥t❛❣❡♠❀
     r❡t✉r♥ tr✉❡❀
⑥

    Agora nosso código funciona como esperado, mas está um pouco mais
verboso e difícil de entender. O grande problema aqui é que, a cada método
cuja regra seja diferente, teremos que colocar um novo if parecido com esse,
isso sem contar que novos tipos de Livro podem aparecer e tornar nosso
código ainda mais complicado e cheio de condicionais. Devemos sempre es-
crever nosso código pensando em como será sua evolução no futuro.
    Além disso, existem alguns comportamentos e atributos que só servem
para um Ebook. Um deles é o watermark (marca d’água). Essa é a forma
de identificar discretamente o nome e e-mail do dono daquele livro digital,
normalmente no rodapé das páginas.
    Se Ebook é um elemento importante, possui comportamentos e atributos
específicos, ele deveria ser representado como um Objeto! Podemos criar
uma classe Ebook definindo os atributos e comportamentos específicos desse
novo tipo.

♣✉❜❧✐❝ ❝❧❛ss ❊❜♦♦❦ ④

     ♣r✐✈❛t❡ ❙tr✐♥❣ ♥♦♠❡❀
     ♣r✐✈❛t❡ ❙tr✐♥❣ ❞❡s❝r✐❝❛♦❀
     ♣r✐✈❛t❡ ❞♦✉❜❧❡ ✈❛❧♦r❀
     ♣r✐✈❛t❡ ❙tr✐♥❣ ✐s❜♥❀
     ♣r✐✈❛t❡ ❆✉t♦r ❛✉t♦r❀
     ♣r✐✈❛t❡ ❙tr✐♥❣ ✇❛t❡r▼❛r❦❀

     ♣✉❜❧✐❝ ✈♦✐❞ s❡t❲❛t❡r▼❛r❦✭❙tr✐♥❣ ✇❛t❡r▼❛r❦✮ ④
         t❤✐s✳✇❛t❡r▼❛r❦ ❂ ✇❛t❡r▼❛r❦❀
     ⑥

     ♣✉❜❧✐❝ ❙tr✐♥❣ ❣❡t❲❛t❡r▼❛r❦✭✮ ④
         r❡t✉r♥ ✇❛t❡r▼❛r❦❀
     ⑥



                                                                                77


[PAGINA 88]
5.1. Trabalhando com livros digitais                          Casa do Código


      ✴✴ ❣❡tt❡rs✱ s❡tt❡rs ❡ ♦✉tr♦s ♠ét♦❞♦s
⑥

    Nosso código já está um pouco mais interessante, afinal não estamos mais
sobrecarregando a classe Livro com atributos e métodos que serão uti-
lizados apenas quando o tipo do livro for um ebook. Mas há muito código
repetido aqui: além dos comportamentos do Ebook, temos todos os atribu-
tos e métodos já escritos na classe Livro.
    Para evitar toda essa repetição de código, podemos ensinar ao compilador
que o Ebook é um tipo de Livro, ou seja, além de seus próprios atributos e
métodos, essa classe possui tudo o que um Livro tem. Para fazer isto, basta
Ebook dizer na declaração da classe que ela é um Livro, que é uma extensão
dessa classe:

♣✉❜❧✐❝ ❝❧❛ss ❊❜♦♦❦ ❡①t❡♥❞s ▲✐✈r♦ ④

      ♣r✐✈❛t❡ ❙tr✐♥❣ ✇❛t❡r▼❛r❦❀

      ♣✉❜❧✐❝ ❊❜♦♦❦✭❆✉t♦r ❛✉t♦r✮ ④
          s✉♣❡r✭❛✉t♦r✮❀
      ⑥

      ♣✉❜❧✐❝ ✈♦✐❞ s❡t❲❛t❡r▼❛r❦✭❙tr✐♥❣ ✇❛t❡r▼❛r❦✮ ④
          t❤✐s✳✇❛t❡r▼❛r❦ ❂ ✇❛t❡r▼❛r❦❀
      ⑥

      ♣✉❜❧✐❝ ❙tr✐♥❣ ❣❡t❲❛t❡r▼❛r❦✭✮ ④
          r❡t✉r♥ ✇❛t❡r▼❛r❦❀
      ⑥
⑥




78


[PAGINA 89]
Casa do Código                                    Capítulo 5. Herança e polimorfismo




  delegate constructor

     Como a classe Livro tinha um construtor obrigando a passagem de
  um Autor como parâmetro, ao herdar de um Livro, a classe Ebook
  também herdou essa responsabilidade. Repare que utilizamos a palavra
  super para delegar a responsabilidade para a superclasse que já tem esse
  comportamento bem definido.

  ♣✉❜❧✐❝ ❊❜♦♦❦✭❆✉t♦r ❛✉t♦r✮ ④
      s✉♣❡r✭❛✉t♦r✮❀
  ⑥



    Ao utilizar a palavra reservada extends, estamos dizendo que um
Ebook (subclasse) herda tudo o que a classe Livro (superclasse) tem. Por-
tanto, mesmo sem ter nenhum desses métodos declarados diretamente na
classe Ebook, podemos executar o seguinte código sem nenhum problema:

❊❜♦♦❦ ❡❜♦♦❦ ❂ ♥❡✇ ❊❜♦♦❦✭✮❀
❡❜♦❦✳s❡t◆♦♠❡✭✧❏❛✈❛ ✽ Prát✐❝♦✧✮❀

  Como a classe Livro tem os setters para o atributo nome declarados,
um Ebook também terá.


  Herança múltipla

      Uma regra importante da herança em Java é que nossas classes só
  podem herdar diretamente de uma classe pai. Ou seja, não há herança
  múltipla como na linguagem C++. Mas sim, uma classe pode herdar de
  uma classe que herda de outra e assim por diante. Você pode encadear
  a herança de suas classes, no entanto, veremos mais à frente que essa es-
  tratégia não é muito interessante por aumentar de mais o acoplamento
  entre suas classes.



                                                                                 79


[PAGINA 90]
5.2. Reescrevendo métodos da superclasse                  Casa do Código


5.2      Reescrevendo métodos da superclasse
Agora que temos uma forma forte de se representar um Ebook, podemos
criar um método aplicaDescontoDe com o desconto máximo de 15%. As-
sim, evitamos aquele if que verificava se um Livro era impresso ou não.
Na classe Livro o método deve ficar assim:
♣✉❜❧✐❝ ❜♦♦❧❡❛♥ ❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭❞♦✉❜❧❡ ♣♦r❝❡♥t❛❣❡♠✮ ④
    ✐❢ ✭♣♦r❝❡♥t❛❣❡♠ ❃ ✵✳✸✮ ④
        r❡t✉r♥ ❢❛❧s❡❀
    ⑥
    t❤✐s✳✈❛❧♦r ✲❂ t❤✐s✳✈❛❧♦r ✯ ♣♦r❝❡♥t❛❣❡♠❀
    r❡t✉r♥ tr✉❡❀
⑥

    Mas no lugar de a classe Ebook herdar esse comportamento (que deve
ser diferente para ela), podemos reescrevê-lo como a seguir:
♣✉❜❧✐❝ ❝❧❛ss ❊❜♦♦❦ ❡①t❡♥❞s ▲✐✈r♦ ④

      ♣r✐✈❛t❡ ❙tr✐♥❣ ✇❛t❡r▼❛r❦❀

      ♣✉❜❧✐❝ ❊❜♦♦❦✭❆✉t♦r ❛✉t♦r✮ ④
          s✉♣❡r✭❛✉t♦r✮❀
      ⑥

      ♣✉❜❧✐❝ ❜♦♦❧❡❛♥ ❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭❞♦✉❜❧❡ ♣♦r❝❡♥t❛❣❡♠✮ ④
          ✐❢ ✭♣♦r❝❡♥t❛❣❡♠ ❃ ✵✳✶✺✮ ④
              r❡t✉r♥ ❢❛❧s❡❀
          ⑥
          t❤✐s✳✈❛❧♦r ✲❂ t❤✐s✳✈❛❧♦r ✯ ♣♦r❝❡♥t❛❣❡♠❀
          r❡t✉r♥ tr✉❡❀
      ⑥

      ✴✴ ❣❡t ❡ s❡t ❞♦ ✇❛t❡r♠❛r❦
⑥

    Por mais que um Ebook seja um Livro, quando alguém chamar o
método aplicaDescontoDe, o desconto será de 15%, e não de 30% com
o está definido na classe pai.

80


[PAGINA 91]
Casa do Código                                  Capítulo 5. Herança e polimorfismo



    A JVM sempre vai procurar o método primeiro no objeto que foi instanci-
ado e apenas quando não encontrar procurará em sua superclasse. Você pode
ver um exemplo aqui:




                                                                               81


[PAGINA 92]
5.2. Reescrevendo métodos da superclasse                         Casa do Código




     @Override

         Opcionalmente podemos marcar os métodos reescritos com a ano-
     tação @Overrride. Uma anotação é apenas uma marcação, como um
     post-it com uma observação importante sobre o local anotado. As an-
     notations surgiram no Java 1.5, e têm um papel bastante importante na
     maior parte das bibliotecas mais atuais da linguagem. Por questões de
     compatibilidade, o uso do @Override é facultativo, mas é bastante in-
     teressante anotar os seus métodos dessa forma, já que, com isso, o com-
     pilador nos ajudará a validar que esse método é realmente uma reescrita.

     ❅❖✈❡rr✐❞❡
     ♣✉❜❧✐❝ ❜♦♦❧❡❛♥ ❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭❞♦✉❜❧❡ ♣♦r❝❡♥t❛❣❡♠✮ ④
         ✐❢ ✭♣♦r❝❡♥t❛❣❡♠ ❃ ✵✳✶✺✮ ④
             r❡t✉r♥ ❢❛❧s❡❀
         ⑥
         t❤✐s✳✈❛❧♦r ✲❂ t❤✐s✳✈❛❧♦r ✯ ♣♦r❝❡♥t❛❣❡♠❀
         r❡t✉r♥ tr✉❡❀
     ⑥

        Ao anotar nosso método com @Override, o código não compilará
     caso esse método não exista na classe pai (superclasse).


     Antes de testar essa mudança, precisamos fazer uma ultima alteração para
que esse método compile.
     Como a visibilidade do atributo valor da classe Livro é private,
a linha que o acessa diretamente do método aplicaDescontoDe da classe
Ebook não vai funcionar. Afinal, um atributo private só pode ser acessado
pela própria classe, nem mesmo as classes filhas (subclasses) podem violar essa
regra.
     Para que o código funcione, precisamos aumentar essa visibilidade, mas
já conhecemos o problema de deixar os atributos public. Uma alternativa
é modificar a visibilidade dos atributos da classe Livro para protected,
que é um meio termo entre public e private.



82


[PAGINA 93]
Casa do Código                                    Capítulo 5. Herança e polimorfismo



    A visibilidade protected deixará os atributos visíveis também para as
classes filhas, mas normalmente evitamos utilizar esse modificador de visibil-
idade porque ele acaba tendo mais algumas exceções que afrouxam o nosso
encapsulamento. Conheceremos mais sobre o protected adiante, mas
desde já vamos evitar essa alternativa.
    Uma forma bem interessante e simples de resolver o problema é utilizando
a interface da classe pai, seus próprios métodos. Por exemplo, no lugar de
acessar o atributo diretamente, poderíamos utilizar os métodos getValor e
setValor como a seguir:

❅❖✈❡rr✐❞❡
♣✉❜❧✐❝ ❜♦♦❧❡❛♥ ❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭❞♦✉❜❧❡ ♣♦r❝❡♥t❛❣❡♠✮ ④
    ✐❢ ✭♣♦r❝❡♥t❛❣❡♠ ❃ ✵✳✶✺✮ ④
        r❡t✉r♥ ❢❛❧s❡❀
    ⑥
    ❞♦✉❜❧❡ ❞❡s❝♦♥t♦ ❂ t❤✐s✳❣❡t❱❛❧♦r✭✮ ✯ ♣♦r❝❡♥t❛❣❡♠❀
    t❤✐s✳s❡t❱❛❧♦r✭t❤✐s✳❣❡t❱❛❧♦r✭✮ ✲ ❞❡s❝♦♥t♦✮❀
    r❡t✉r♥ tr✉❡❀
⑥

    Dessa forma, não perderemos nem um pouco do encapsulamento da
classe Livro! Quanto mais você estudar e se habituar com a orientação a
objetos, mais você perceberá que garantir o encapsulamento das classes é
fundamental. Ainda que um pouco, quando liberamos acesso dos atributos
da superclasse para suas classes filhas, estamos violando o encapsulamento
dessa classe.




                                                                                 83


[PAGINA 94]
5.2. Reescrevendo métodos da superclasse                       Casa do Código




  this ou super?

    No método aplicaDescontoDe da classe Ebook, chamamos o
  getter e setter do atributo valor utilizando a palavra reservada
  this. Uma outra forma de fazer isso seria utilizando o super. Assim,
  estamos deixando claro que o método invocado é da classe pai. Existem
  situações em que é muito interessante utilizar super, como neste caso:

  ❅❖✈❡rr✐❞❡
  ♣✉❜❧✐❝ ❜♦♦❧❡❛♥ ❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭❞♦✉❜❧❡ ♣♦r❝❡♥t❛❣❡♠✮ ④
      ✐❢ ✭♣♦r❝❡♥t❛❣❡♠ ❃ ✵✳✶✺✮ ④
          r❡t✉r♥ ❢❛❧s❡❀
      ⑥
      r❡t✉r♥ s✉♣❡r✳❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭♣♦r❝❡♥t❛❣❡♠✮❀
  ⑥

      Repare que, logo após fazer a nossa condição, estamos delegando para
  a lógica do método aplicaDescontoDe da classe pai. Com isso, evita-
  mos repetir a lógica que já está definida na superclasse. Mas o que acon-
  teceria se no lugar de super tivéssemos utilizado o this?
      Nesse caso, o método aplicaDescontoDe da classe Ebook estaria
  chamando ele mesmo! Entraríamos em um looping infinito.

   Pronto, chegou a hora de testar esse código para garantir que tudo está
funcionando como esperado. Abra (ou crie, caso já não exista) a classe
RegrasDeDesconto e escreva o seguinte código:

♣✉❜❧✐❝ ❝❧❛ss ❘❡❣r❛s❉❡❉❡s❝♦♥t♦ ④

      ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④

            ❆✉t♦r ❛✉t♦r ❂ ♥❡✇ ❆✉t♦r✭✮❀
            ❛✉t♦r✳s❡t◆♦♠❡✭✧❘♦❞r✐❣♦ ❚✉r✐♥✐✧✮❀

            ▲✐✈r♦ ❧✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦✭❛✉t♦r✮❀
            ❧✐✈r♦✳s❡t❱❛❧♦r✭✺✾✳✾✵✮❀


84


[PAGINA 95]
Casa do Código                                  Capítulo 5. Herança e polimorfismo



           ✐❢ ✭✦❧✐✈r♦✳❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭✵✳✸✮✮④
               ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❉❡s❝♦♥t♦ ♥♦ ❧✐✈r♦ ♥ã♦ ♣♦❞❡ s❡r
                    ♠❛✐♦r ❞♦ q✉❡ ✸✵✪✧✮❀
           ⑥ ❡❧s❡ ④
               ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❱❛❧♦r ❞♦ ❧✐✈r♦ ❝♦♠ ❞❡s❝♦♥t♦✿ ✧
                    ✰ ❧✐✈r♦✳❣❡t❱❛❧♦r✭✮✮❀
           ⑥

           ❊❜♦♦❦ ❡❜♦♦❦ ❂ ♥❡✇ ❊❜♦♦❦✭❛✉t♦r✮❀
           ❡❜♦♦❦✳s❡t❱❛❧♦r✭✷✾✳✾✵✮❀

           ✐❢ ✭✦❡❜♦♦❦✳❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭✵✳✸✮✮④
               ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❉❡s❝♦♥t♦ ♥♦ ❡❜♦♦❦ ♥ã♦ ♣♦❞❡ s❡r
                    ♠❛✐♦r ❞♦ q✉❡ ✶✺✪✧✮❀
           ⑥ ❡❧s❡ ④
               ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❱❛❧♦r ❞♦ ❡❜♦♦❦ ❝♦♠ ❞❡s❝♦♥t♦✿ ✧
                    ✰ ❡❜♦♦❦✳❣❡t❱❛❧♦r✭✮✮❀
           ⑥
      ⑥
⑥

      A saída será:

❱❛❧♦r ❞♦ ❧✐✈r♦ ❝♦♠ ❞❡s❝♦♥t♦✿ ✹✶✳✾✸
❉❡s❝♦♥t♦ ♥♦ ❡❜♦♦❦ ♥ã♦ ♣♦❞❡ s❡r ♠❛✐♦r ❞♦ q✉❡ ✶✺✪

    Mudando o valor de desconto passado para o e-book de 0.3 para 0.15, o
resultado será:

❱❛❧♦r ❞♦ ❧✐✈r♦ ❝♦♠ ❞❡s❝♦♥t♦✿ ✹✶✳✾✸
❱❛❧♦r ❞♦ ❡❜♦♦❦ ❝♦♠ ❞❡s❝♦♥t♦✿ ✷✺✳✹✶✺

   Ótimo, cada tipo de livro teve a sua regra de desconto devidamente apli-
cada.


5.3       Regras próprias de um LivroFisico
Deixamos os comportamentos específicos de um     Ebook bem
encapsulados em sua classe, mas repare que há um problema em

                                                                               85


[PAGINA 96]
5.3. Regras próprias de um LivroFisico                       Casa do Código


nossa herança. Em que lugar devemos colocar os métodos que fazem sentido
apenas para um livro físico? Por exemplo, todo livro físico possui uma taxa
de impressão. Podemos criar um getTaxaImpressao para nos retornar
esse valor, como a seguir:

♣✉❜❧✐❝ ❞♦✉❜❧❡ ❣❡t❚❛①❛■♠♣r❡ss❛♦✭✮ ④
    r❡t✉r♥ t❤✐s✳❣❡t❱❛❧♦r✭✮ ✯ ✵✳✵✺❀
⑥

    Mas onde adicionamos esse método? Se adicionarmos na classe Livro,
o Ebook herdará esse comportamento que não deveria existir em seu tipo.
    Mais uma vez entramos na regra: se um elemento é importante e tem
regras específicas, ele deve ser representado como um objeto. Podemos
criar uma nova classe em nosso projeto, para representar tudo o que um
LivroFisico tem e como ele se comporta. Observe:

♣✉❜❧✐❝ ❝❧❛ss ▲✐✈r♦❋✐s✐❝♦ ❡①t❡♥❞s ▲✐✈r♦ ④

      ♣✉❜❧✐❝ ▲✐✈r♦❋✐s✐❝♦✭❆✉t♦r ❛✉t♦r✮ ④
          s✉♣❡r✭❛✉t♦r✮❀
      ⑥

      ♣✉❜❧✐❝ ❞♦✉❜❧❡ ❣❡t❚❛①❛■♠♣r❡ss❛♦✭✮ ④
          r❡t✉r♥ t❤✐s✳❣❡t❱❛❧♦r✭✮ ✯ ✵✳✵✺❀
      ⑥
⑥

    Dessa maneira, também temos uma forma forte de representar um
LivroFisico, bem encapsulada e que não causa nenhum efeito colateral
nos demais filhos de Livro, como o Ebook.




86


[PAGINA 97]
Casa do Código                                  Capítulo 5. Herança e polimorfismo




  Uma nova classe a cada tipo de livro?

      Uma reação bem comum de quem está aprendendo orientação a ob-
  jetos é perguntar: então eu devo criar uma nova classe pra cada tipo de
  livro?. A resposta é sim. E você logo perceberá que isso não é um prob-
  lema.
      É muito mais interessante trabalhar com classes menores, que rep-
  resentam bem os seus tipos e possuem suas regras específicas bem en-
  capsuladas, do que trabalhar com uma única classe carregando toda essa
  responsabilidade.
      Poderíamos sim ter uma única classe Livro que tivesse todos os
  comportamentos de um LivroFisico, um Ebook e dos demais tipos
  que podem aparecer. Mas imagine o tamanho dessa classe, a quantidade
  de métodos e ifs encadeados para lidar com as diferentes regras de cada
  tipo de Livro. A classe seria enorme e bem difícil de manter.
      Lembre-se sempre que Java é uma linguagem fortemente tipada, você
  pode e deve criar objetos para representar cada tipo de elemento da sua
  aplicação.


5.4    Vendendo diferentes tipos de Livro
Para dar mais um passo em nossa aplicação, criaremos agora uma classe
RegistroDeVendas, por enquanto com um método main e o seguinte con-
teúdo:

♣✉❜❧✐❝ ❝❧❛ss ❘❡❣✐str♦❉❡❱❡♥❞❛s ④

      ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④

          ❆✉t♦r ❛✉t♦r ❂ ♥❡✇ ❆✉t♦r✭✮❀
          ❛✉t♦r✳s❡t◆♦♠❡✭✧▼❛✉r✐❝✐♦ ❆♥✐❝❤❡✧✮❀

          ▲✐✈r♦❋✐s✐❝♦ ❢✐s✐❝♦ ❂ ♥❡✇ ▲✐✈r♦❋✐s✐❝♦✭❛✉t♦r✮❀
          ❢✐s✐❝♦✳s❡t◆♦♠❡✭✧❚❡st✲❉r✐✈❡♥ ❉❡✈❡❧♦♣♠❡♥t✧✮❀



                                                                               87


[PAGINA 98]
5.4. Vendendo diferentes tipos de Livro                       Casa do Código


            ❊❜♦♦❦ ❡❜♦♦❦ ❂ ♥❡✇ ❊❜♦♦❦✭❛✉t♦r✮❀
            ❡❜♦♦❦✳s❡t◆♦♠❡✭✧❚❡st✲❉r✐✈❡♥ ❉❡✈❡❧♦♣♠❡♥t✧✮❀
      ⑥
⑥

   Repare que criamos um LivroFisico e um Ebook com o mesmo
Autor. Nosso próximo passo será adicionar esses dois elementos em um
CarrinhoDeCompras. O código deve ficar parecido com este:

❈❛rr✐♥❤♦❉❡❈♦♠♣r❛s ❝❛rr✐♥❤♦ ❂ ♥❡✇ ❈❛rr✐♥❤♦❉❡❈♦♠♣r❛s✭✮❀
❝❛rr✐♥❤♦✳❛❞✐❝✐♦♥❛✭❢✐s✐❝♦✮❀
❝❛rr✐♥❤♦✳❛❞✐❝✐♦♥❛✭❡❜♦♦❦✮❀

   Vamos agora criar a classe CarrinhoDeCompras e seu método
adiciona. Como vamos adicionar LivroFisicos e também Ebooks, uma
forma de fazer isso seria criando dois métodos adiciona, um para cada tipo
de Livro (uma sobrecarga):

♣✉❜❧✐❝ ❝❧❛ss ❈❛rr✐♥❤♦❉❡❈♦♠♣r❛s ④

      ♣✉❜❧✐❝ ✈♦✐❞ ❛❞✐❝✐♦♥❛✭▲✐✈r♦❋✐s✐❝♦ ❧✐✈r♦✮ ④
          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❆❞✐❝✐♦♥❛♥❞♦✿ ✧ ✰ ❧✐✈r♦✮❀
      ⑥

      ♣✉❜❧✐❝ ✈♦✐❞ ❛❞✐❝✐♦♥❛✭❊❜♦♦❦ ❧✐✈r♦✮ ④
          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❆❞✐❝✐♦♥❛♥❞♦✿ ✧ ✰ ❧✐✈r♦✮❀
      ⑥
⑥

    Esse código funcionaria sem nenhum problema, mas repare que está
muito repetido. Além disso, a cada novo tipo de Livro, precisaremos criar
um novo método adiciona que receba esse tipo como parâmetro, o que
seria um tanto trabalhoso e difícil de manter.
    Para evitar isso, podemos utilizar um recurso da linguagem bastante útil
e poderoso. Como existe uma herança envolvida, podemos dizer que tanto
um LivroFisico como um Ebook são filhos (extensões) da classe Livro.
Poderíamos criar um único método adiciona, que recebe um Livro (su-
perclasse) como parâmetro:

88


[PAGINA 99]


[PAGINA 100]
5.4. Vendendo diferentes tipos de Livro                      Casa do Código




   Não estamos transformando objetos

      Lembre-se que uma variável guarda uma referência para um objeto,
   e não um objeto em si. Até agora, estávamos sempre declarando um
   Ebook com o tipo Ebook. Repare:

   ❊❜♦♦❦ ❡❜♦♦❦ ❂ ♥❡✇ ❊❜♦♦❦✭✮❀

       Mas, como vimos, também podemos dizer que um Ebook é do tipo
   Livro, afinal ele herda (é um) Livro.

   ▲✐✈r♦ ❡❜♦♦❦ ❂ ♥❡✇ ❊❜♦♦❦✭✮❀

       Mas é fundamental perceber que não estamos transformando esse ob-
   jeto. Se criamos um Ebook, ele será um Ebook e ponto. Estamos apenas
   nos referenciando a ele como um Livro, uma abstração.

    Perceba que, como estamos referenciando o parâmetro passado para o
método adiciona da classe CarrinhoDeCompras como um Livro, ape-
nas os métodos presentes na classe Livro poderão ser invocados sem que
um erro de compilação ocorra.
    Para ficar mais claro, ainda que passando um objeto do tipo Ebook para
o adiciona, ao tentar invocar seu método getWaterMark, o seguinte erro
de compilação ocorrerá:

❚❤❡ ♠❡t❤♦❞ ❣❡t❲❛t❡r▼❛r❦✭✮ ✐s ✉♥❞❡❢✐♥❡❞ ❢♦r t❤❡ t②♣❡ ▲✐✈r♦

   Faz sentido. Para que isso funcione, precisaríamos fazer um casting
moldando o parâmetro livro para o tipo Ebook:

♣✉❜❧✐❝ ✈♦✐❞ ❛❞✐❝✐♦♥❛✭▲✐✈r♦ ❧✐✈r♦✮ ④
    ❊❜♦♦❦ ❡❜♦♦❦ ❂ ✭❊❜♦♦❦✮ ❧✐✈r♦❀
    ❡❜♦♦❦✳❣❡t❲❛t❡r▼❛r❦✭✮❀
    ✴✴ r❡st❛♥t❡ ❞♦ ❝ó❞✐❣♦ ♦♠✐t✐❞♦
⑥

    Isso vai funcionar muito bem, contanto que o valor passado de fato seja
do tipo Ebook. Isso é um tanto perigoso, pois podemos muito bem passar

90


[PAGINA 101]
Casa do Código                                  Capítulo 5. Herança e polimorfismo



um LivroFisico como argumento. Neste caso até seria possível fazer um
if para validar que o objeto passado é uma instância de Ebook, mas deixaria
de ser uma vantagem usar polimorfismo aqui.


5.5     Acumulando total de compras
O CarrinhoDeCompras precisa acumular o valor total que está sendo com-
prado. Podemos fazer isso de uma forma bem simples, adicionando um atrib-
uto total e incrementando com o valor do Livro a cada adição.
♣✉❜❧✐❝ ✈♦✐❞ ❛❞✐❝✐♦♥❛✭▲✐✈r♦ ❧✐✈r♦✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❆❞✐❝✐♦♥❛♥❞♦✿ ✧ ✰ ❧✐✈r♦✮❀
    t♦t❛❧ ✰❂ ❧✐✈r♦✳❣❡t❱❛❧♦r✭✮❀
⑥

    Além disso, antes de acumular o total da compra, o método adiciona
aplicará um desconto de 5% para cada livro adicionado:
♣✉❜❧✐❝ ✈♦✐❞ ❛❞✐❝✐♦♥❛✭▲✐✈r♦ ❧✐✈r♦✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❆❞✐❝✐♦♥❛♥❞♦✿ ✧ ✰ ❧✐✈r♦✮❀
    ❧✐✈r♦✳❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭✵✳✵✺✮❀
    t♦t❛❧ ✰❂ ❧✐✈r♦✳❣❡t❱❛❧♦r✭✮❀
⑥

      Ao final, nossa classe CarrinhoDeCompras deve ficar assim:
♣✉❜❧✐❝ ❝❧❛ss ❈❛rr✐♥❤♦❉❡❈♦♠♣r❛s ④

      ♣r✐✈❛t❡ ❞♦✉❜❧❡ t♦t❛❧❀

      ♣✉❜❧✐❝ ✈♦✐❞ ❛❞✐❝✐♦♥❛✭▲✐✈r♦ ❧✐✈r♦✮ ④
          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❆❞✐❝✐♦♥❛♥❞♦✿ ✧ ✰ ❧✐✈r♦✮❀
          ❧✐✈r♦✳❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭✵✳✵✺✮❀
          t♦t❛❧ ✰❂ ❧✐✈r♦✳❣❡t❱❛❧♦r✭✮❀
      ⑥

      ♣✉❜❧✐❝ ❞♦✉❜❧❡ ❣❡t❚♦t❛❧✭✮ ④
          r❡t✉r♥ t♦t❛❧❀
      ⑥
⑥

                                                                               91


[PAGINA 102]


[PAGINA 103]


[PAGINA 104]
5.6. Herança ou composição?                                    Casa do Código


    Como esperado, apenas o desconto do LivroFisico foi aplicado, pois
o método aplicaDescontoDe da classe Ebook limita o desconto a 15%.
    Portanto, não importa a forma como nós nos referenciamos a nossos ob-
jetos, no fim o método executado sempre será o dele.


5.6     Herança ou composição?
Entenderemos melhor o problema mais à frente, mas sempre que possível
procure favorecer o uso da composição entre classes no lugar de utilizar her-
ança. Veremos que o uso da herança aumenta bastante o acoplamento de suas
classes e de alguma forma sempre acaba comprometendo o encapsulamento.
    Tudo isso será melhor aprofundado nos próximos capítulos, mas desde já
você pode se interessar em ler o seguinte artigo no qual James Gosling, con-
siderado pai do Java, fala sobre o assunto:
    http://www.artima.com/intv/gosling3P.html




94


[PAGINA 105]
Capítulo 6

Classe abstrata
6.1 Qual o tipo de cada Livro?
Agora que temos uma forma forte de representar os diferentes tipos de
Livro, podemos nos expressar bem ao fazer uma venda:

❊❜♦♦❦ ❡❜♦♦❦ ❂ ♥❡✇ ❊❜♦♦❦✭❛✉t♦r✮❀
❡❜♦♦❦✳s❡t◆♦♠❡✭✧❈❉■✧✮❀

❝❛rr✐♥❤♦✳❛❞✐❝✐♦♥❛✭❡❜♦♦❦✮❀

   Além de Ebook, também temos um LivroFisico, que já provou ser
um objeto diferente por ter comportamentos diferentes. Mas o que estamos
vendendo quando fazemos new em um Livro?
▲✐✈r♦ ❧✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦✭❛✉t♦r✮❀
❧✐✈r♦✳s❡t◆♦♠❡✭✧❈❉■✧✮❀


[PAGINA 106]
6.1. Qual o tipo de cada Livro?                             Casa do Código




❝❛rr✐♥❤♦✳❛❞✐❝✐♦♥❛✭❧✐✈r♦✮❀

    Afinal, o que é um Livro agora? Um Ebook ou um LivroFisico?
Na verdade, nenhum dos dois. Um Livro é apenas uma abstração de tudo
que os diferentes tipos de livro devem ter (herdar) em nossa livraria.
    Ao fazer uma venda, queremos saber ao certo o tipo de livro que está
sendo vendido, nunca deveríamos permitir a venda de um Livro, mas sim
de suas subclasses.
    Para nossa sorte, há uma forma bem simples de impedir que a classe
Livro seja instanciada e utilizada dessa forma: podemos simplesmente adi-
cionar em sua declaração o modificador abstract. Repare:

♣✉❜❧✐❝ ❛❜str❛❝t ❝❧❛ss ▲✐✈r♦ ④

      ✴✴ ❝♦♥t✐♥✉❛çã♦ ❞♦ ❝ó❞✐❣♦
⑥

    A partir do momento em que tornamos nossa classe abstrata, o compi-
lador vai impedir que qualquer código tente instanciar um Livro. Por ex-
emplo, em nosso CadastroDeLivros:

▲✐✈r♦ ❧✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦✭❛✉t♦r✮❀
❧✐✈r♦✳s❡t◆♦♠❡✭✧❏❛✈❛ ✽ Prát✐❝♦✧✮❀
❧✐✈r♦✳s❡t❉❡s❝r✐❝❛♦✭✧◆♦✈♦s r❡❝✉rs♦s ❞❛ ❧✐♥❣✉❛❣❡♠✧✮❀
❧✐✈r♦✳s❡t❱❛❧♦r✭✺✾✳✾✵✮❀
❧✐✈r♦✳s❡t■s❜♥✭✧✾✼✽✲✽✺✲✻✻✷✺✵✲✹✻✲✻✧✮❀

     O erro de compilação apresentado será:

❈❛♥♥♦t ✐♥st❛♥t✐❛t❡ t❤❡ t②♣❡ ▲✐✈r♦

     Bem claro, não acha? Não se pode mais criar um Livro e ponto final.




96


[PAGINA 107]
Casa do Código                                             Capítulo 6. Classe abstrata




    Por que precisamos da classe L I V R O ?

       Afinal, para que serve a classe Livro, se não podemos mais
    instanciá-la? Lembre-se que essa classe idealiza tudo o que um Livro
    tem, ela ainda está sendo muito útil isolando todos os atributos e compor-
    tamentos que são um padrão entre os diferentes tipos de livro. A classe
    passa a servir exclusivamente para herança e polimorfismo, que são re-
    cursos bastante úteis e poderosos.

    Todo livro criado agora precisa ter seu tipo bem definido, portanto pre-
cisaremos mudar todas as partes de nosso código que criava um Livro para
usar uma de suas classes filhas. A classe CadastroDeLivros, por exemplo,
ficará assim:

♣✉❜❧✐❝ ❝❧❛ss ❈❛❞❛str♦❉❡▲✐✈r♦s ④

      ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④

           ❆✉t♦r ❛✉t♦r ❂ ♥❡✇ ❆✉t♦r✭✮❀
           ❛✉t♦r✳s❡t◆♦♠❡✭✧❘♦❞r✐❣♦ ❚✉r✐♥✐✧✮❀
           ❛✉t♦r✳s❡t❊♠❛✐❧✭✧r♦❞r✐❣♦✳t✉r✐♥✐❅❝❛❡❧✉♠✳❝♦♠✳❜r✧✮❀
           ❛✉t♦r✳s❡t❈♣❢✭✧✶✷✸✳✹✺✻✳✼✽✾✳✶✵✧✮❀

           ▲✐✈r♦ ❧✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦❋✐s✐❝♦✭❛✉t♦r✮❀
           ❧✐✈r♦✳s❡t◆♦♠❡✭✧❏❛✈❛ ✽ Prát✐❝♦✧✮❀
           ❧✐✈r♦✳s❡t❉❡s❝r✐❝❛♦✭✧◆♦✈♦s r❡❝✉rs♦s ❞❛ ❧✐♥❣✉❛❣❡♠✧✮❀
           ❧✐✈r♦✳s❡t❱❛❧♦r✭✺✾✳✾✵✮❀
           ❧✐✈r♦✳s❡t■s❜♥✭✧✾✼✽✲✽✺✲✻✻✷✺✵✲✹✻✲✻✧✮❀

           ❧✐✈r♦✳♠♦str❛r❉❡t❛❧❤❡s✭✮❀

           ✴✴ ♦✉tr♦s ❧✐✈r♦s ❝❛❞❛str❛❞♦s
      ⑥
⑥

   Apesar de não poder instanciar uma classe abstrata, você ainda pode (e
muitas vezes deve) usá-la como referência. Como no método adiciona do

                                                                                  97


[PAGINA 108]
6.2. Minilivro não tem desconto!                                 Casa do Código


CarrinhoDeCompras:

♣✉❜❧✐❝ ✈♦✐❞ ❛❞✐❝✐♦♥❛✭▲✐✈r♦ ❧✐✈r♦✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❆❞✐❝✐♦♥❛♥❞♦✿ ✧ ✰ ❧✐✈r♦✮❀
    ❧✐✈r♦✳❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭✵✳✶✻✮❀
    t♦t❛❧ ✰❂ ❧✐✈r♦✳❣❡t❱❛❧♦r✭✮❀
⑥

    Repare que ainda estamos recebendo um Livro como parâmetro para
continuar usando o polimorfismo. Isso é perfeitamente possível, afinal um
Ebook e um LivroFisico são filhos de Livro, portanto herdam o seu
tipo.


    Quando uma classe deve ser abstrata?

        Quando você for planejar a hierarquia e herança de suas classes, você
    verá que algumas classes são bastante específicas e que jamais deveriam
    ser instanciadas. A classe Animal pode ser vista como um exemplo. O
    que exatamente é um Animal? Poderia ser um Leao, um Pinguim ou
    qualquer outro Animal do planeta. Essa classe pode definir tudo o que
    todos os animais têm em comum, mas cada tipo de Animal tem suas
    particularidades e deve ser representado de uma forma própria.


6.2      Minilivro não tem desconto!
Agora que Livro é abstrato, podemos adicionar um novo tipo de Livro
em nossa livraria. Será um MiniLivro, representando um livro mais enx-
uto e com algumas particularidades que logo conheceremos. Vamos começar
criando essa nova classe:

♣✉❜❧✐❝ ❝❧❛ss ▼✐♥✐▲✐✈r♦ ❡①t❡♥❞s ▲✐✈r♦ ④

      ♣✉❜❧✐❝ ▼✐♥✐▲✐✈r♦✭❆✉t♦r ❛✉t♦r✮ ④
          s✉♣❡r✭❛✉t♦r✮❀
      ⑥
⑥

98


[PAGINA 109]
Casa do Código                                        Capítulo 6. Classe abstrata



    O que acontecerá quando modificarmos o código da classe
RegrasDeDesconto criando um           MiniLivro onde anteriormente
criávamos um Livro? Vamos fazer essa alteração e executá-la para ver o
resultado. A classe deve ficar assim:
♣✉❜❧✐❝ ❝❧❛ss ❘❡❣r❛s❉❡❉❡s❝♦♥t♦ ④

     ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④

          ❆✉t♦r ❛✉t♦r ❂ ♥❡✇ ❆✉t♦r✭✮❀
          ❛✉t♦r✳s❡t◆♦♠❡✭✧❘♦❞r✐❣♦ ❚✉r✐♥✐✧✮❀

          ▲✐✈r♦ ❧✐✈r♦ ❂ ♥❡✇ ▼✐♥✐▲✐✈r♦✭❛✉t♦r✮❀
          ❧✐✈r♦✳s❡t❱❛❧♦r✭✸✾✳✾✵✮❀

          ✐❢ ✭✦❧✐✈r♦✳❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭✵✳✸✮✮④
              ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❉❡s❝♦♥t♦ ♥♦ ❧✐✈r♦ ♥ã♦ ♣♦❞❡
                   s❡r ♠❛✐♦r ❞♦ q✉❡ ✸✵✪✧✮❀
          ⑥ ❡❧s❡ ④
              ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❱❛❧♦r ❞♦ ❧✐✈r♦ ❝♦♠ ❞❡s❝♦♥t♦✿ ✧
                   ✰ ❧✐✈r♦✳❣❡t❱❛❧♦r✭✮✮❀
          ⑥
          ✴✴ ♦✉tr♦s ❞❡s❝♦♥t♦s ♦♠✐t✐❞♦s
     ⑥
⑥

    Ao executar esse código o retorno será:
❛♣❧✐❝❛♥❞♦ ❞❡s❝♦♥t♦ ♥♦ ▲✐✈r♦
❱❛❧♦r ❞♦ ❧✐✈r♦ ❝♦♠ ❞❡s❝♦♥t♦✿ ✷✼✳✾✸

    Observe que foi aplicado um desconto de 30% no valor do livro, mas um
MiniLivro não pode ter desconto! Ele já é um livro com preço promocional,
não podemos permitir que nenhum outro valor de desconto seja aplicado.
   Ao criar um MiniLivro, mesmo sem definirmos isso, ele já poderia ter
um desconto de até 30% pois herdou esse comportamento da classe Livro.
Há uma forma simples de resolver o problema: poderíamos reescrever o
método aplicaDescontoDe da classe MiniLivro para sempre retornar
false. Seu código ficaria assim:

                                                                             99


[PAGINA 110]
6.2. Minilivro não tem desconto!                            Casa do Código


♣✉❜❧✐❝ ❝❧❛ss ▼✐♥✐▲✐✈r♦ ❡①t❡♥❞s ▲✐✈r♦ ④

      ♣✉❜❧✐❝ ▼✐♥✐▲✐✈r♦✭❆✉t♦r ❛✉t♦r✮ ④
          s✉♣❡r✭❛✉t♦r✮❀
      ⑥

      ❅❖✈❡rr✐❞❡
      ♣✉❜❧✐❝ ❜♦♦❧❡❛♥ ❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭❞♦✉❜❧❡ ♣♦r❝❡♥t❛❣❡♠✮ ④
          r❡t✉r♥ ❢❛❧s❡❀
      ⑥
⑥

    Essa solução resolveria o problema, mas é um tanto sensível. Será que
qualquer pessoa que criasse esse novo tipo de Livro se lembraria de modi-
ficar o desconto padrão? Provavelmente não.
    É bastante improvável que um novo desenvolvedor, ou mesmo quem
tenha criado a regra, lembre-se deste detalhe sempre que um novo tipo de
livro for criado. Depender da memória humana nunca é uma boa estratégia.
    No lugar de precisar sobrescrever o método sempre que houver desconto,
poderíamos inverter a situação deixando o comportamento padrão do Livro
abstrato retornar false. Dessa forma, por padrão nenhum livro terá de-
sconto. Sobrescrevemos essa regra apenas quando for necessário.
    Nosso código ficaria assim:

♣✉❜❧✐❝ ❛❜str❛❝t ❝❧❛ss ▲✐✈r♦ ④

      ♣r✐✈❛t❡ ❙tr✐♥❣ ♥♦♠❡❀
      ♣r✐✈❛t❡ ❙tr✐♥❣ ❞❡s❝r✐❝❛♦❀
      ♣r✐✈❛t❡ ❞♦✉❜❧❡ ✈❛❧♦r❀
      ♣r✐✈❛t❡ ❙tr✐♥❣ ✐s❜♥❀
      ♣r✐✈❛t❡ ❆✉t♦r ❛✉t♦r❀

      ♣✉❜❧✐❝ ▲✐✈r♦✭❆✉t♦r ❛✉t♦r✮ ④
          t❤✐s✳❛✉t♦r ❂ ❛✉t♦r❀
          t❤✐s✳✐s❜♥ ❂ ✧✵✵✵✲✵✵✲✵✵✵✵✵✲✵✵✲✵✧❀
      ⑥

      ♣✉❜❧✐❝ ❜♦♦❧❡❛♥ ❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭❞♦✉❜❧❡ ♣♦r❝❡♥t❛❣❡♠✮ ④

100


[PAGINA 111]
Casa do Código                                      Capítulo 6. Classe abstrata



          r❡t✉r♥ ❢❛❧s❡❀
     ⑥

     ✴✴ ♦✉tr♦s ♠ét♦❞♦s✱ ❣❡tt❡rs ❡ s❡tt❡rs
⑥

    Agora que o método aplicaDescontoDe da classe pai sempre retorna
false, precisaremos mudar a classe LivroFisico para permitir até 30%
de desconto:
♣✉❜❧✐❝ ❝❧❛ss ▲✐✈r♦❋✐s✐❝♦ ❡①t❡♥❞s ▲✐✈r♦ ④

     ♣✉❜❧✐❝ ▲✐✈r♦❋✐s✐❝♦✭❆✉t♦r ❛✉t♦r✮ ④
         s✉♣❡r✭❛✉t♦r✮❀
     ⑥

     ♣✉❜❧✐❝ ❞♦✉❜❧❡ ❣❡t❚❛①❛■♠♣r❡ss❛♦✭✮ ④
         r❡t✉r♥ t❤✐s✳❣❡t❱❛❧♦r✭✮ ✯ ✵✳✵✺❀
     ⑥

     ♣✉❜❧✐❝ ❜♦♦❧❡❛♥ ❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭❞♦✉❜❧❡ ♣♦r❝❡♥t❛❣❡♠✮ ④
         ✐❢ ✭♣♦r❝❡♥t❛❣❡♠ ❃ ✵✳✸✮ ④
             r❡t✉r♥ ❢❛❧s❡❀
         ⑥
         ❞♦✉❜❧❡ ❞❡s❝♦♥t♦ ❂ ❣❡t❱❛❧♦r✭✮ ✯ ♣♦r❝❡♥t❛❣❡♠❀
         s❡t❱❛❧♦r✭❣❡t❱❛❧♦r✭✮ ✲ ❞❡s❝♦♥t♦✮❀
         ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❛♣❧✐❝❛♥❞♦ ❞❡s❝♦♥t♦ ♥♦ ▲✐✈r♦❋✐s✐❝♦✧✮❀
         r❡t✉r♥ tr✉❡❀
     ⑥
⑥

   Nossa classe MiniLivro não precisará mais sobrescrever o método. Seu
código pode ficar assim:
♣✉❜❧✐❝ ❝❧❛ss ▼✐♥✐▲✐✈r♦ ❡①t❡♥❞s ▲✐✈r♦ ④

     ♣✉❜❧✐❝ ▼✐♥✐▲✐✈r♦✭❆✉t♦r ❛✉t♦r✮ ④
         s✉♣❡r✭❛✉t♦r✮❀
     ⑥
⑥

                                                                          101


[PAGINA 112]
6.3. Método abstrato                                            Casa do Código


    Essa estratégia é um pouco mais interessante, afinal não permitiremos
mais desconto do que uma classe deveria ter. O problema é que precisaremos
lembrar de reescrever esse comportamento em todo novo tipo de Livro que
tenha desconto. Ainda corremos o risco de esquecer e, desta vez, não permitir
desconto para um Livro que tenha direito.


6.3      Método abstrato
Se cada novo Livro terá uma estratégia de desconto diferente, ou seja, se
não há um desconto padrão entre todos os tipos de livro, poderíamos simples-
mente apagar esse método dessa classe abstrata e escrevê-lo apenas nas classes
que devem ter desconto. O problema disso é que perderíamos o polimorfismo,
afinal, se o método não estiver presente na tipo Livro, o seguinte código não
funcionará:

♣✉❜❧✐❝ ✈♦✐❞ ❛❞✐❝✐♦♥❛✭▲✐✈r♦ ❧✐✈r♦✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❆❞✐❝✐♦♥❛♥❞♦✿ ✧ ✰ ❧✐✈r♦✮❀
    ❧✐✈r♦✳❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭✵✳✶✻✮❀
    t♦t❛❧ ✰❂ ❧✐✈r♦✳❣❡t❱❛❧♦r✭✮❀
⑥

    Nem todo Livro terá o método aplicaDescontoDe, não há nenhuma
garantia disso.
    Podemos resolver o problema de uma forma mais efetiva. Toda classe
abstrata, como é o caso da nossa classe Livro, pode ter métodos abstratos.
Toda classe filha (subclasse) concreta (não abstrata) é obrigada a escrever os
métodos abstratos da classe pai (superclasse), caso contrário seu código não
compilará.
    Para tornar o método aplicaDescontoDe abstrato na classe Livro,
basta adicionar o modificador abstract em sua declaração e remover todo
o corpo, colocando apenas um ponto e vírgula. Repare:

♣✉❜❧✐❝ ❛❜str❛❝t ❝❧❛ss ▲✐✈r♦ ④

      ♣r✐✈❛t❡ ❙tr✐♥❣ ♥♦♠❡❀
      ♣r✐✈❛t❡ ❙tr✐♥❣ ❞❡s❝r✐❝❛♦❀
      ♣r✐✈❛t❡ ❞♦✉❜❧❡ ✈❛❧♦r❀

102


[PAGINA 113]
Casa do Código                                             Capítulo 6. Classe abstrata



     ♣r✐✈❛t❡ ❙tr✐♥❣ ✐s❜♥❀
     ♣r✐✈❛t❡ ❆✉t♦r ❛✉t♦r❀

     ♣✉❜❧✐❝ ▲✐✈r♦✭❆✉t♦r ❛✉t♦r✮ ④
         t❤✐s✳❛✉t♦r ❂ ❛✉t♦r❀
         t❤✐s✳✐s❜♥ ❂ ✧✵✵✵✲✵✵✲✵✵✵✵✵✲✵✵✲✵✧❀
     ⑥

     ♣✉❜❧✐❝ ❛❜str❛❝t ❜♦♦❧❡❛♥ ❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭❞♦✉❜❧❡ ♣♦r❝❡♥t❛❣❡♠✮❀

     ✴✴ ♦✉tr♦s ♠ét♦❞♦s✱ ❣❡tt❡rs ❡ s❡tt❡rs
⑥

    Apenas classes abstratas podem ter métodos abstratos. Afinal, se al-
guém invocasse o método aplicaDescontoDe da classe Livro, qual seria
o resultado? Não há nenhuma implementação nele, portanto ele não poderia
ser executado.
    A partir do momento em que tornamos o método aplicaDescontoDe
abstrato, todas as classes filhas precisam escrevê-lo. Por esse motivo, a classe
MiniLivro vai parar de compilar. O erro será:

❚❤❡ t②♣❡ ▼✐♥✐▲✐✈r♦ ♠✉st ✐♠♣❧❡♠❡♥t t❤❡ ✐♥❤❡r✐t❡❞ ❛❜str❛❝t ♠❡t❤♦❞
▲✐✈r♦✳❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭❞♦✉❜❧❡✮

    Para que tudo funcione a classe precisará ficar assim:
♣✉❜❧✐❝ ❝❧❛ss ▼✐♥✐▲✐✈r♦ ❡①t❡♥❞s ▲✐✈r♦ ④

     ♣✉❜❧✐❝ ▼✐♥✐▲✐✈r♦✭❆✉t♦r ❛✉t♦r✮ ④
         s✉♣❡r✭❛✉t♦r✮❀
     ⑥

     ❅❖✈❡rr✐❞❡
     ♣✉❜❧✐❝ ❜♦♦❧❡❛♥ ❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭❞♦✉❜❧❡ ♣♦r❝❡♥t❛❣❡♠✮ ④
         r❡t✉r♥ ❢❛❧s❡❀
     ⑥
⑥

    Ainda não é uma solução perfeita, estamos sendo obrigados a escrever
esse método na classe MiniLivro mesmo que ela não possua essa regra de

                                                                                 103


[PAGINA 114]
6.4. Relembrando algumas regras                                  Casa do Código


desconto. Mas a grande vantagem é que eliminamos totalmente a possibili-
dade de esquecer de definir esse comportamento em novas implementações
da classe Livro. A partir de agora, todo filho de Livro logo quando criado
já precisará definir qual a sua regra de desconto, caso contrário o código não
compila.


6.4 Relembrando algumas regras
Não é nem um pouco complicado trabalhar com classes abstratas, mas exis-
tem algumas regras que precisam ser respeitadas. Apenas para relembrar, são
elas:

      • Uma classe pode ser abstrata sem ter nenhum método abstrato. A par-
        tir do momento em que ela se tornar abstrata, nenhum código poderá
        mais instanciá-la.

      • Se você declarar um método abstrato, precisará tornar a classe abstrata
        também! Você não pode ter métodos abstratos em uma classe que não
        é abstrata.

      • Uma classe abstrata pode ter métodos abstratos e não abstratos (con-
        cretos).

      • Toda classe filha (subclasse) precisa implementar os métodos abstratos
        da classe pai (superclasse). A não ser que ela também seja abstrata.




104


[PAGINA 115]
Capítulo 7

Interface
Além dos mais diversos tipos de Livros, nossa livraria também trabalhará
com Revistas e futuramente outros produtos. Podemos criar uma nova
classe para representá-la, como a seguir:

♣✉❜❧✐❝ ❝❧❛ss ❘❡✈✐st❛ ④

    ♣r✐✈❛t❡ ❙tr✐♥❣ ♥♦♠❡❀
    ♣r✐✈❛t❡ ❙tr✐♥❣ ❞❡s❝r✐❝❛♦❀
    ♣r✐✈❛t❡ ❞♦✉❜❧❡ ✈❛❧♦r❀
    ♣r✐✈❛t❡ ❊❞✐t♦r❛ ❡❞✐t♦r❛❀

    ✴✴ ❣❡tt❡rs ❡ s❡tt❡rs

    ♣✉❜❧✐❝ ❜♦♦❧❡❛♥ ❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭❞♦✉❜❧❡ ♣♦r❝❡♥t❛❣❡♠✮ ④
        ✐❢ ✭♣♦r❝❡♥t❛❣❡♠ ❃ ✵✳✶✮ ④


[PAGINA 116]
                                                           Casa do Código


              r❡t✉r♥ ❢❛❧s❡❀
          ⑥
          ❞♦✉❜❧❡ ❞❡s❝♦♥t♦ ❂ ❣❡t❱❛❧♦r✭✮ ✯ ♣♦r❝❡♥t❛❣❡♠❀
          s❡t❱❛❧♦r✭❣❡t❱❛❧♦r✭✮ ✲ ❞❡s❝♦♥t♦✮❀
          r❡t✉r♥ tr✉❡❀
      ⑥
⑥

   Repare que, além de um nome, descricao e valor, uma revista tam-
bém possui uma regra de desconto e é composta pela classe Editora. Essa
é uma outra classe bastante simples:

♣✉❜❧✐❝ ❝❧❛ss ❊❞✐t♦r❛ ④

      ♣r✐✈❛t❡ ❙tr✐♥❣ ♥♦♠❡❋❛♥t❛s✐❛❀
      ♣r✐✈❛t❡ ❙tr✐♥❣ r❛③❛♦❙♦❝✐❛❧❀
      ♣r✐✈❛t❡ ❙tr✐♥❣ ❝♥♣❥❀

      ✴✴ ❣❡tt❡rs ❡ s❡tt❡rs
⑥

    Precisamos agora evoluir nosso CarrinhoDeCompras para que seja
possível, além de Livros, adicionar Revistas. Uma solução seria duplicar
seu método adiciona:

♣✉❜❧✐❝ ❝❧❛ss ❈❛rr✐♥❤♦❉❡❈♦♠♣r❛s ④

      ♣r✐✈❛t❡ ❞♦✉❜❧❡ t♦t❛❧❀

      ♣✉❜❧✐❝ ✈♦✐❞ ❛❞✐❝✐♦♥❛✭▲✐✈r♦ ❧✐✈r♦✮ ④
          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❆❞✐❝✐♦♥❛♥❞♦✿ ✧ ✰ ❧✐✈r♦✮❀
          ❧✐✈r♦✳❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭✵✳✵✺✮❀
          t♦t❛❧ ✰❂ ❧✐✈r♦✳❣❡t❱❛❧♦r✭✮❀
      ⑥

      ♣✉❜❧✐❝ ✈♦✐❞ ❛❞✐❝✐♦♥❛✭❘❡✈✐st❛ r❡✈✐st❛✮ ④
          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❆❞✐❝✐♦♥❛♥❞♦✿ ✧ ✰ r❡✈✐st❛✮❀
          r❡✈✐st❛✳❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭✵✳✵✺✮❀
          t♦t❛❧ ✰❂ r❡✈✐st❛✳❣❡t❱❛❧♦r✭✮❀


106


[PAGINA 117]
Casa do Código                                              Capítulo 7. Interface



     ⑥

     ♣✉❜❧✐❝ ❞♦✉❜❧❡ ❣❡t❚♦t❛❧✭✮ ④
         r❡t✉r♥ t♦t❛❧❀
     ⑥
⑥

    Mas note como os dois métodos ficaram bastante parecidos, há muita
repetição de código! Além disso, para cada novo produto precisaríamos criar
um novo método, o que tornaria trabalhosa a evolução dessa classe.
    Poderíamos fazer a classe Revista herdar de Livro, de modo que o
polimorfismo seria aplicável e teríamos um único método adiciona. Mas ao
fazer isso toda Revista teria um Autor, ISBN além dos demais atributos e
comportamentos que só se aplicam para os Livros, uma verdadeira bagunça.
    Sim, podemos criar um nível a mais na hierarquia de nossas classes
adicionando a classe Produto, assim Livro e Revista herdariam de
Produto e poderíamos utilizar esse tipo no polimorfismo. A hierarquia de
nossas classes seria:




                                                                            107


[PAGINA 118]
7.1. O contrato Produto                                         Casa do Código


    O grande problema dessa abordagem é que aumentaria demais o acopla-
mento entre as classes, ou seja, o quanto uma classe depende da outra. A
herança cria uma relação muito forte entre as classes. Ao mudar a classe
Produto, por exemplo, todas as subclasses (e também subclasses das sub-
classes) seriam influenciadas.
    E se eu quiser aplicar a mudança apenas para algumas classes? Teríamos
que sobrescrever esse novo comportamento de uma forma desnecessária em
todas as outras, assim como fizemos com a classe MiniLivro. Mesmo sem
existir desconto para essa classe, ela foi obrigada a sobrescrever o método
aplicaDescontoDe para apenas retornar false.
    Com o passar do tempo, o uso da herança faz com que nossas classes
fiquem cada vez mais acopladas e isso dificulta sua evolução.


7.1 O contrato Produto
Em Java, há uma outra forma para se tirar proveito de todos os benefícios do
polimorfismo sem ter que acoplar tanto as suas classes com vários níveis de
herança. Você pode estabelecer um fator em comum entre as classes, criando
uma espécie de contrato.
    Para esse contrato, não importa a forma como será implementado, a única
coisa que importa é que seus métodos (cláusulas) sejam implementados de
alguma forma. Isso lembra algo? Sim, é bastante parecido com um método
abstrato cujo corpo você só define na superclasse para que todas as subclasses
herdem a obrigação de implementá-lo.
    Esse tipo de contrato Java é conhecido como Interface.

   Não se trata de uma interface gráfica

       É muito comum confundir no inicio, mas não estamos falando de
   uma interface gráfica de usuário (GUI). Também não estamos falando da
   interface da classe, seus métodos públicos. Você perceberá no decorrer
   do capítulo que se trata de um recurso diferente, um contrato Java.

   Podemos criar uma interface Produto, que por enquanto terá um
único método abstrato estabelecendo que todo produto deve ter o método

108


[PAGINA 119]
Casa do Código                                                 Capítulo 7. Interface



getValor. Uma interface se parece bastante com uma classe abstrata que
tenha apenas métodos abstratos, mas no lugar de declará-la como uma classe,
utilizamos a palavra reservada interface:

♣✉❜❧✐❝ ✐♥t❡r❢❛❝❡ Pr♦❞✉t♦ ④

     ♣✉❜❧✐❝ ❛❜str❛❝t ❞♦✉❜❧❡ ❣❡t❱❛❧♦r✭✮❀
⑥

     Como todo método sem corpo de uma interface é abstrato, o uso do mod-
ificador abstract é opcional. Não precisamos também adicionar o modi-
ficador public, pois seus métodos também são públicos por padrão. Pode-
mos simplificar a escrita da interface Produto deixando apenas:

♣✉❜❧✐❝ ✐♥t❡r❢❛❝❡ Pr♦❞✉t♦ ④

     ❞♦✉❜❧❡ ❣❡t❱❛❧♦r✭✮❀
⑥

    Uma interface não pode ter atributos e, até a versão 1.7 da linguagem, tam-
bém não pode ter nenhum método concreto, ou seja, com implementação.
Veremos que, a partir do Java 1.8, isso mudou um pouco.
    Podemos agora fazer com que todas as classes que idealizam produtos de
nossa livraria assinem o contrato Produto. Para fazer isso, basta adicionar
a palavra-chave implements seguida do nome da interface que deve ser
implementada na declaração das classes, veja:

♣✉❜❧✐❝ ❛❜str❛❝t ❝❧❛ss ▲✐✈r♦ ✐♠♣❧❡♠❡♥ts Pr♦❞✉t♦ ④
    ✴✴ ❛tr✐❜✉t♦s ❡ ♠ét♦❞♦s ♦♠✐t✐❞♦s
⑥

♣✉❜❧✐❝ ❝❧❛ss ❘❡✈✐st❛ ✐♠♣❧❡♠❡♥ts Pr♦❞✉t♦ ④
    ✴✴ ❛tr✐❜✉t♦s ❡ ♠ét♦❞♦s ♦♠✐t✐❞♦s
⑥

   Como todas essas classes já possuem o método getValor declarado,
você não perceberá nenhuma diferença. Nosso código passa a funcionar
como esperado. Mas é importante perceber que se apagarmos o método

                                                                               109


[PAGINA 120]
7.1. O contrato Produto                                          Casa do Código


getValor a classe deixará de compilar, afinal toda classe que implementa
a interface Produto é obrigada a implementar seus métodos abstratos.
      Veja que com a interface o diagrama de nossas classes fica assim:




    Como todos que implementam uma interface podem ser referenci-
ados por este tipo, podemos usar polimorfismo com interfaces. Por exem-
plo, no método adiciona do CarrinhoDeCompras podemos receber um
Produto como parâmetro:

♣✉❜❧✐❝ ✈♦✐❞ ❛❞✐❝✐♦♥❛✭Pr♦❞✉t♦ ♣r♦❞✉t♦✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❆❞✐❝✐♦♥❛♥❞♦✿ ✧ ✰ ♣r♦❞✉t♦✮❀
    ♣r♦❞✉t♦✳❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭✵✳✶✻✮❀
    t♦t❛❧ ✰❂ ♣r♦❞✉t♦✳❣❡t❱❛❧♦r✭✮❀
⑥

   O polimorfismo funcionará, mas o problema desse código é que nem todo
Produto tem o método aplicaDescontoDe, mas apenas os filhos da classe

110


[PAGINA 121]
Casa do Código                                           Capítulo 7. Interface



Livro. Sim, poderíamos mover o método abstrato aplicaDescontoDe
para a interface Produto, mas se nem todos os produtos têm um desconto,
devemos evitar isso. Por enquanto, removeremos esse desconto, mas logo
veremos uma forma mais interessante de resolver o problema. Nosso método
deve ficar assim:

♣✉❜❧✐❝ ✈♦✐❞ ❛❞✐❝✐♦♥❛✭Pr♦❞✉t♦ ♣r♦❞✉t♦✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❆❞✐❝✐♦♥❛♥❞♦✿ ✧ ✰ ♣r♦❞✉t♦✮❀
    t♦t❛❧ ✰❂ ♣r♦❞✉t♦✳❣❡t❱❛❧♦r✭✮❀
⑥

   Rode a classe RegistroDeVendas para ver que tudo está funcionando
como esperado. A classe continua assim:

♣✉❜❧✐❝ ❝❧❛ss ❘❡❣✐str♦❉❡❱❡♥❞❛s ④

     ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④

          ❆✉t♦r ❛✉t♦r ❂ ♥❡✇ ❆✉t♦r✭✮❀
          ❛✉t♦r✳s❡t◆♦♠❡✭✧▼❛✉r✐❝✐♦ ❆♥✐❝❤❡✧✮❀

          ▲✐✈r♦❋✐s✐❝♦ ❢✐s✐❝♦ ❂ ♥❡✇ ▲✐✈r♦❋✐s✐❝♦✭❛✉t♦r✮❀
          ❢✐s✐❝♦✳s❡t◆♦♠❡✭✧❚❡st✲❉r✐✈❡♥ ❉❡✈❡❧♦♣♠❡♥t✧✮❀
          ❢✐s✐❝♦✳s❡t❱❛❧♦r✭✺✾✳✾✵✮❀

          ❊❜♦♦❦ ❡❜♦♦❦ ❂ ♥❡✇ ❊❜♦♦❦✭❛✉t♦r✮❀
          ❡❜♦♦❦✳s❡t◆♦♠❡✭✧❚❡st✲❉r✐✈❡♥ ❉❡✈❡❧♦♣♠❡♥t✧✮❀
          ❡❜♦♦❦✳s❡t❱❛❧♦r✭✷✾✳✾✵✮❀

          ❈❛rr✐♥❤♦❉❡❈♦♠♣r❛s ❝❛rr✐♥❤♦ ❂ ♥❡✇ ❈❛rr✐♥❤♦❉❡❈♦♠♣r❛s✭✮❀

          ❝❛rr✐♥❤♦✳❛❞✐❝✐♦♥❛✭❢✐s✐❝♦✮❀
          ❝❛rr✐♥❤♦✳❛❞✐❝✐♦♥❛✭❡❜♦♦❦✮❀

          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❚♦t❛❧ ✧ ✰ ❝❛rr✐♥❤♦✳❣❡t❚♦t❛❧✭✮✮❀
     ⑥
⑥

    Ao executá-la, o resultado será:

                                                                          111


[PAGINA 122]
7.2. Diminuindo acoplamento com Interfaces                      Casa do Código



Adicionado: LivroFisico@4f23c55
Adicionado: Ebook@21a33b44
Total 89.8


7.2 Diminuindo acoplamento com Interfaces
O uso da interface já nos ajudou a resolver o problema de polimorfismo de nos-
sos produtos. Agora há uma forma simples e flexível para representar qual-
quer Produto de nossa livraria. Mas ainda precisamos resolver o problema
do método aplicaDescontoDe.
    Ao adicionar esse método abstrato na classe Livro, obrigamos todas as
suas subclasses a implementá-lo, mas não é bem isso que precisamos. Essa
solução deixa de ser interessante quando nem todos os Livros tenham esse
comportamento, como é o caso do MiniLivro, que não pode ter um de-
sconto.
    Outra questão é que apenas os filhos da classe Livros têm essa
obrigação, sendo que uma Revista também deve possuir o método
aplicaDescontoDe.           Podemos diminuir esse acoplamento de uma
forma bem simples, criando uma nova interface! Vamos chamá-la de
Promocional:

♣✉❜❧✐❝ ✐♥❡ ❢❛❝❡ " ♦♠♦❝✐♦♥❛❧ ④

      ❜♦♦❧❡❛♥ ❛♣❧✐❝❛❉❡ ❝♦♥♦❉❡✭❞♦✉❜❧❡ ♣♦ ❝❡♥❛❣❡♠✮❀
⑥

    Agora podemos remover o método aplicaDescontoDe abstrato da
classe Livro e dizer que apenas as classes promocionais, que possuem de-
sconto, implementam essa nova interface:

♣✉❜❧✐❝ ❝❧❛   ▲✐✈ ♦❋✐ ✐❝♦ ❡①❡♥❞ ▲✐✈ ♦ ✐♠♣❧❡♠❡♥ " ♦♠♦❝✐♦♥❛❧ ④
    ✴✴ ❛ ✐❜✉♦ ❡ ♠-♦❞♦ ♦♠✐✐❞♦
⑥

♣✉❜❧✐❝ ❝❧❛   ❊❜♦♦❦ ❡①❡♥❞ ▲✐✈ ♦ ✐♠♣❧❡♠❡♥            " ♦♠♦❝✐♦♥❛❧ ④
        ✴✴ ❛ ✐❜✉♦ ❡ ♠-♦❞♦ ♦♠✐✐❞♦
⑥

112


[PAGINA 123]
Casa do Código                                              Capítulo 7. Interface




♣✉❜❧✐❝ ❝❧❛ss ❘❡✈✐st❛ ✐♠♣❧❡♠❡♥ts Pr♦❞✉t♦✱ Pr♦♠♦❝✐♦♥❛❧ ④
    ✴✴ ❛tr✐❜✉t♦s ❡ ♠ét♦❞♦s ♦♠✐t✐❞♦s
⑥

    Assim como podemos assinar diversos contratos ao longo de nossas vidas,
uma classe também pode implementar diversas interfaces. Repare que a classe
Revista agora implementa duas interfaces, utilizando uma vírgula em sua
declaração.
    A grande vantagem de trabalhar com interfaces é que apenas as classes
que a implementam são obrigadas a implementar seus métodos, portanto,
se eu não quero que MiniLivro tenha desconto, basta não implementar a
interface Promocional.
    Observe como a estrutura de nossas classes está mais flexível. Qualquer
nova classe pode passar a ser promocional, sem herdar nenhuma outra obri-
gação. O mesmo ocorre com o Produto: tudo que uma classe precisa fazer
para ter o tipo Produto é assinar esse contrato e implementar seu método
getValor, sem nenhum efeito colateral indesejado.




                                                                             113


[PAGINA 124]


[PAGINA 125]
Casa do Código                                                Capítulo 7. Interface



Adicionado: Ebook@21a33b44
Total 83.81
     Mais à frente veremos que diversos default methods foram adicionados
nas interfaces da API do Java. Foi possível evoluir seu comportamento sem
quebrar compatibilidade com suas implementações já existentes e bastante
utilizadas.

Interface funcional
    Uma interface não precisa ter um único método abstrato, mas essa é uma
estrutura bem comum. Normalmente, trabalhar com interfaces menores é
uma estratégia interessante, afinal temos mais flexibilidade. Se alguém imple-
mentar aquela interface é porque realmente precisa do comportamento que
ela estabelece.
    A partir do Java 8, as interfaces que obedecem essa regra de ter um único
método abstrato podem ser chamadas de interface funcional. Mesmo
sem ter esse propósito, nossas interfaces Produto e Promocional possuem
essa estrutura e se enquadram no perfil de uma interface funcional.
    Logo veremos que a interface funcional é a chave para outros novos recur-
sos da linguagem, que são as expressões lambda e method references.

A anotação @FunctionalInterface
    Podemos marcar uma interface como funcional explicitamente, para que
o fato de ela ser uma interface funcional não seja pela simples coincidên-
cia de ter um único método abstrato. Para fazer isso, usamos a anotação
@FuncionalInterface:

❅❋✉♥❝✐♦♥❛❧■♥❡❢❛❝❡
♣✉❜❧✐❝ ✐♥❡❢❛❝❡ ♦♠♦❝✐♦♥❛❧ ④

     ❜♦♦❧❡❛♥ ❛♣❧✐❝❛❉❡"❝♦♥♦❉❡✭❞♦✉❜❧❡ ♣♦❝❡♥❛❣❡♠✮❀

     ❞❡❢❛✉❧ ❜♦♦❧❡❛♥ ❛♣❧✐❝❛❉❡"❝♦♥♦❉❡✶✵♦❝❡♥♦✭✮ ④
         ❡✉♥ ❛♣❧✐❝❛❉❡"❝♦♥♦❉❡✭✵✳✶✮❀
     ⑥
⑥

                                                                               115


[PAGINA 126]
7.3. Novas regras da interface no Java 8                        Casa do Código


    Ao fazer essa alteração, note que nada mudou. Ela continua com-
pilando e, executando nossas classes de teste, o resultado será o mesmo.
Mas diferente do caso de não termos anotado nossa interface com
@FunctionalInterface, tente alterá-la da seguinte forma, adicionando
um novo método abstrato:

❅❋✉♥❝t✐♦♥❛❧■♥t❡r❢❛❝❡
♣✉❜❧✐❝ ✐♥t❡r❢❛❝❡ Pr♦♠♦❝✐♦♥❛❧ ④

      ❜♦♦❧❡❛♥ ❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭❞♦✉❜❧❡ ♣♦r❝❡♥t❛❣❡♠✮❀
      ❜♦♦❧❡❛♥ ♥❛♦❙♦✉▼❛✐s❯♠❛■♥t❡r❢❛❝❡❋✉♥❝✐♦♥❛❧✭✮❀

      ❞❡❢❛✉❧t ❜♦♦❧❡❛♥ ❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✶✵P♦r❝❡♥t♦✭✮ ④
          r❡t✉r♥ ❛♣❧✐❝❛❉❡s❝♦♥t♦❉❡✭✵✳✶✮❀
      ⑥
⑥

      O código deixará de compilar, com a seguinte mensagem:

■♥✈❛❧✐❞ ✬❅❋✉♥❝t✐♦♥❛❧■♥t❡r❢❛❝❡✬ ❛♥♥♦t❛t✐♦♥❀
    Pr♦♠♦❝✐♦♥❛❧ ✐s ♥♦t ❛ ❢✉♥❝t✐♦♥❛❧ ✐♥t❡r❢❛❝❡

   E ao tentar compilar fora do Eclipse, com o javac como fizemos no
primeiro capítulo, a mensagem seria ainda mais explicativa:

❥❛✈❛✿ ❯♥❡①♣❡❝t❡❞ ❅❋✉♥❝t✐♦♥❛❧■♥t❡r❢❛❝❡ ❛♥♥♦t❛t✐♦♥
  Pr♦♠♦❝✐♦♥❛❧ ✐s ♥♦t ❛ ❢✉♥❝t✐♦♥❛❧ ✐♥t❡r❢❛❝❡
    ♠✉❧t✐♣❧❡ ♥♦♥✲♦✈❡rr✐❞✐♥❣ ❛❜str❛❝t ♠❡t❤♦❞s ❢♦✉♥❞
    ✐♥ ✐♥t❡r❢❛❝❡ Pr♦♠♦❝✐♦♥❛❧

    Outro detalhe que você já deve ter percebido é que podemos ter um ou
mais default methods declarados em nossa interface e isso não influencia o fato
de ela ser ou não uma interface funcional, apenas métodos abstratos
são considerados.

Herança múltipla no Java 8?
   Métodos defaults foram adicionados para permitir que interfaces
evoluam sem quebrar código existente. Essa frase foi bastante repetida na

116


[PAGINA 127]
Casa do Código                                              Capítulo 7. Interface



lista de discussão da especificação dessa nova versão da linguagem. Eles não
foram criados para permitir alguma variação de herança múltipla ou de mix-
ins. Vale lembrar que há uma série de restrições para esses métodos. Em
especial, eles não podem acessar atributos de instância, até porque isso não
existe em interfaces! Em outras palavras, não há herança múltipla ou com-
partilhamento de estado.




                                                                             117


[PAGINA 128]


[PAGINA 129]
Capítulo 8

Pacotes
8.1   Organizando nossas classes
Por enquanto nossas classes estão todas em um mesmo arquivo, dentro da
pasta src. Conforme o projeto vai evoluindo, mais e mais classes são cri-
adas e fica cada vez mais difícil manter a organização de nosso projeto. Mas
organização não será o único problema aqui.
    Com o passar do tempo, trabalharemos com classes de terceiros (bibliote-
cas) e classes da própria API da linguagem, o que torna ainda maior o risco
de criarmos uma classe com o nome igual a outra existente em alguma dessas
bibliotecas.
    Quer um exemplo? Poderíamos criar uma classe que se chama Date:

❝❧❛ss ❉❛t❡ ④
    ♣r✐✈❛t❡ ✐♥t ❞✐❛❀


[PAGINA 130]
8.1. Organizando nossas classes                                Casa do Código


      ♣r✐✈❛t❡ ✐♥t ♠❡s❀
      ♣r✐✈❛t❡ ✐♥t ❛♥♦❀

      ✴✴ ❣❡tt❡rs ❡ s❡tt❡rs
⑥

    Em um método main qualquer de nossa aplicação, poderíamos instan-
ciar essa classe fazendo:

♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④
    ❉❛t❡ ❞❛t❡ ❂ ♥❡✇ ❉❛t❡✭✮❀
⑥

    Mas na API do Java, já existe uma classe chamada Date. Como a
JVM sabe diferenciar quando precisamos instanciar a nossa classe Date ou
quando deve ser o Date do Java? A resposta é bem simples: em Java classes
são agrupadas por pacotes (packages).
    O pacote da classe Date da API do Java com certeza será diferente do
pacote de nossa classe, portanto, para tirar a ambiguidade podemos instanciar
a classe pelo seu nome completo, como por exemplo:

♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④
    ❥❛✈❛✳✉t✐❧✳❉❛t❡ ❞❛t❡ ❂ ♥❡✇ ❥❛✈❛✳✉t✐❧✳❉❛t❡✭✮❀
⑥

    Estranho? Não se preocupe, vamos melhorar a legibilidade desse código
logo. Mas repare que o nome completo da classe, ou fully qualified name como
é comumente chamado, é composto por nome do pacote . (ponto) nome
da classe. Neste caso, o nome do pacote onde se encontra a classe Date é
java.util.




120


[PAGINA 131]
Casa do Código                                               Capítulo 8. Pacotes




  Pacotes da API do Java

      Além do java.util, existem diversos pacotes com classes essen-
  ciais para nosso dia a dia trabalhando com Java. Algumas classes como
  a String e System não precisam ser escritas com o nome completo,
  pois fazem parte do pacote java.lang, que é o pacote padrão do Java.
  No próximo capítulo estudaremos a fundo o pacote java.lang e, no
  decorrer do livro, veremos alguns dos demais principais pacotes da API.



     Observando o código a seguir você já deve ter sentido uma perda de leg-
ibilidade:

❥❛✈❛✳✉t✐❧✳❉❛t❡ ❞❛t❡ ❂ ♥❡✇ ❥❛✈❛✳✉t✐❧✳❉❛t❡✭✮❀

   Podemos simplificar esse código adicionando um import com o nome
completo da classe no início de nosso arquivo. Repare:

✐♠♣♦rt ❥❛✈❛✳✉t✐❧✳❉❛t❡❀

❝❧❛ss ❚❡st❡ ④
    ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④
        ❉❛t❡ ❞❛t❡ ❂ ♥❡✇ ❉❛t❡✭✮❀
    ⑥
⑥

    Só será necessário escrever o nome completo da classe sem um import se
por alguma razão você precisar usar duas classes com o mesmo nome dentro
do mesmo arquivo. Nesse caso, você poderá fazer o import de uma delas,
mas utilizar o nome completo quando for se referir à outra.
    A essa altura você já deve ter se perguntado: Qual o nome completo da
nossa classe Date? Como nós criamos a classe diretamente no diretório src,
ela não tem um pacote definido. Dizemos que ela está no default package.
    Isso não é nada bom, toda classe deve ser agrupada em pacotes. Isso,
além de ajudar na organização de nossos projetos, ajudará quando houver
uma ambiguidade de nomes.

                                                                            121


[PAGINA 132]
8.1. Organizando nossas classes                               Casa do Código




   Nomenclatura padrão dos pacotes Java

       Por padrão, um pacote em Java sempre:

        • é escrito em letra minúscula (lowercase);

        • deve ser um nome de domínio, iniciado com com, edu, gov etc.

      É muito natural que o pacote seja o seu domínio (ou da
   empresa), como br.com.casadocodigo,            br.com.alura ou
   br.com.caelum. O link a seguir fala um pouco mais sobre as con-
   venções de nomenclaturas de pacotes do Java:
      http://www.oracle.com/technetwork/java/codeconventions-135099.
   html

    Agora que já sabemos disso, podemos criar alguns pacotes para melhor
organizar o nosso projeto. No Eclipse isso pode ser feito pelo menu File
> New > Package, ou utilizando o atalho Control + N e selecionando a
opção package.
    A princípio, criaremos os pacotes:

      • br.com.casadocodigo.livraria para as classes              Autor e
        Editora;

      • br.com.casadocodigo.livraria.produtos para as interfaces
        Promocional, Produto e suas implementações;

      • br.com.casadocodigo.livraria.teste para nossas classes ex-
        ecutáveis, ou seja, que possuem o método main.

    Antes de mover as classes para seus devidos pacotes, é importante con-
hecer algumas regras. A primeira delas é que nossas classes devem ser públi-
cas para que fiquem visíveis entre os diferentes pacotes. Logo falaremos
mais sobre os modificadores de visibilidade e entenderemos a fundo as suas
regras, mas desde já mantenha a regra em mente.


122


[PAGINA 133]
Casa do Código                                                  Capítulo 8. Pacotes



     Outro detalhe importante é que, para o caso das classes públicas, o ar-
quivo .java obrigatoriamente tem que ter o nome da classe. Por exemplo,
a classe Livro tem que ser salva no arquivo Livro.java. Como vimos no
início deste livro, o ideal é você sempre nomear suas classes dessa forma. Essa
é considerada uma boa prática em Java.
     Agora sim, mãos à massa! Você pode arrastar as classes com o mouse para
mover entre pacotes, mas uma alternativa interessante é o atalho Control
+ Alt + V. Esse atalho é equivalente ao menu Refactor > Move....
     Vamos selecionar as classes Autor e Editora e mover para o pa-
cote br.com.casadocodigo.livraria. Nesse momento, alguns erros
de compilação devem aparecer, mas devemos terminar de mover as classes
antes de corrigir qualquer um deles.
     Promocional, Produto, Livro, LivroFisico, MiniLivro,
Ebook,       Revista e qualquer outra implementação de                Produto
que você tenha criado podem ser movidos para o pacote
br.com.casadocodigo.livraria.produtos.
     Para terminar, vamos mover as demais classes, que têm um método main,
para o pacote br.com.casadocodigo.livraria.testes. Lembre-se,
em um projeto real não criaríamos várias classes com método main, só esta-
mos fazendo isso para testar os nossos exemplos.

package, import e possíveis erros

    Se você moveu as classes utilizando o Eclipse ou alguma IDE equivalente,
repare que foi adicionado um import para toda classe que referencia alguma
presente em outro pacote. Caso você não tenha movido pela IDE ou por al-
gum motivo o import não tenha sido adicionado, você precisará fazer isso
manualmente como no exemplo:

♣❛❝❦❛❣❡ ❜r✳❝♦♠✳❝❛s❛❞♦❝♦❞✐❣♦✳❧✐✈r❛r✐❛✳t❡st❡s❀

✐♠♣♦rt ❜r✳❝♦♠✳❝❛s❛❞♦❝♦❞✐❣♦✳❧✐✈r❛r✐❛✳❆✉t♦r❀
✴✴ ♦✉tr♦s ✐♠♣♦rts

♣✉❜❧✐❝ ❝❧❛ss ❈❛❞❛str♦❉❡▲✐✈r♦s ④


                                                                               123


[PAGINA 134]
8.1. Organizando nossas classes                            Casa do Código


      ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④

            ❆✉t♦r ❛✉t♦r ❂ ♥❡✇ ❆✉t♦r✭✮❀
            ❛✉t♦r✳s❡t◆♦♠❡✭✧❘♦❞r✐❣♦ ❚✉r✐♥✐✧✮❀

            ✴✴ ❝♦♥t✐♥✉❛çã♦ ❞❛ ❝❧❛ss❡
⑥

    Como a classe Autor está em um pacote ( package) diferente da classe
CadastroDeLivros, o import é necessário. Ele sempre é necessário
quando queremos utilizar classes de outros pacotes. E não se esqueça que,
para que uma classe seja visível para outro pacote, ela deve ser pública.
    Um outro detalhe é que agora todas as classes têm o package
a que pertencem declarado. Neste exemplo, o package da classe
CadastroDeLivros é:

♣❛❝❦❛❣❡ ❜r✳❝♦♠✳❝❛s❛❞♦❝♦❞✐❣♦✳❧✐✈r❛r✐❛✳t❡st❡s❀

    A ordem das instruções de seus arquivos .java agora será: primeiro o
package ao qual ela pertence, seguido do(s) import(s) quando necessário
e, por último, a declaração da classe.




124


[PAGINA 135]
Casa do Código                                              Capítulo 8. Pacotes




  Importando todas as classes de um package

     No lugar de fazer os seguintes imports:

  ✐♠♣♦rt ❜r✳❝♦♠✳❝❛s❛❞♦❝♦❞✐❣♦✳❧✐✈r❛r✐❛✳❆✉t♦r❀
  ✐♠♣♦rt ❜r✳❝♦♠✳❝❛s❛❞♦❝♦❞✐❣♦✳❧✐✈r❛r✐❛✳❊❞✐t♦r❛❀

    Você também pode utilizar o * para importar todas as classes de
  um package, neste caso o import seria:

  ✐♠♣♦rt ❜r✳❝♦♠✳❝❛s❛❞♦❝♦❞✐❣♦✳❧✐✈r❛r✐❛✳✯❀

      É comum ouvirmos que isso prejudica a performance, mas na reali-
  dade não afetará o tempo de execução. O problema dessa abordagem é
  que não previne a ambiguidade de nomes. Por isso, é sempre recomen-
  dado que você importe classe a classe, pois, além de evitar problemas
  com classes de mesmo nome, tornará a legibilidade dos imports mais
  clara.

    Ainda existe um erro de compilação em nosso projeto (ou talvez mais,
se o seu código não estiver idêntico ao do livro). Em nosso caso, o prob-
lema é na própria classe CadastroDeLivros, quando ela invoca o método
mostrarDetalhes do LivroFisico. O erro de compilação é o seguinte:

❚❤❡ ♠❡t❤♦❞ ♠♦str❛r❉❡t❛❧❤❡s✭✮ ❢r♦♠ t❤❡ t②♣❡ ▲✐✈r♦ ✐s ♥♦t ✈✐s✐❜❧❡

    Isso acontece porque, assim como as classes, para que um método seja
visível em outro pacote ele precisa ser public. Podemos acessar a classe
Livro e adicionar o modificador de visibilidade public no método ou fazer
isso pelo atalho Control + 1 do Eclipse (quickfix), selecionando a opção
Change visibility of method mostrarDetalhes() to public. No final, o método
deve ficar assim:

♣✉❜❧✐❝ ✈♦✐❞ ♠♦str❛r❉❡t❛❧❤❡s✭✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧▼♦str❛♥❞♦ ❞❡t❛❧❤❡s ❞♦ ❧✐✈r♦ ✧✮❀
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧◆♦♠❡✿ ✧ ✰ ♥♦♠❡✮❀
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❉❡s❝r✐çã♦✿ ✧ ✰ ❞❡s❝r✐❝❛♦✮❀

                                                                           125


[PAGINA 136]
8.2. Modificadores de acesso                                  Casa do Código


      ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❱❛❧♦r✿ ✧ ✰ ✈❛❧♦r✮❀
      ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧■❙❇◆✿ ✧ ✰ ✐s❜♥✮❀

      ✐❢ ✭t❤✐s✳t❡♠❆✉t♦r✭✮✮ ④
          ❛✉t♦r✳♠♦str❛r❉❡t❛❧❤❡s✭✮❀
      ⑥
      ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧✲✲✧✮❀
⑥


    Estrutura de pastas

        Note que um pacote é representado como uma estrutura de pastas no
    seu sistema operacional. Por exemplo, a classe Livro que está local-
    izada no pacote br.com.casadocodigo.livraria está dentro do
    diretório br/com/casadocodigo/livraria, que se encontra den-
    tro da pasta src de seu projeto.


8.2      Modificadores de acesso
Agora que nossas classes estão organizadas em pacotes, podemos entender
um pouco melhor os diferentes modificadores de acesso. Já vimos que, para
uma classe ou método ser acessado de outro pacote, eles precisam ter visi-
bilidade public. A regra é clara: uma classe pública pode ser acessada por
qualquer outra classe presente no mesmo projeto. O mesmo vale para atrib-
utos, métodos e construtores.
    Também já conhecemos o private. Esse modificador de acesso torna
classes, atributos, métodos ou construtores visíveis apenas para a própria
classe. Por esse motivo, uma classe não deve ser anotada com private,
quem poderá acessá-la? Mas vimos que faz bastante sentido, para manter o
encapsulamento, sempre deixar seus atributos private.
    Há ainda a visibilidade default (quando não há modificador algum).
A essa altura, você já pode ter percebido que neste caso apenas classes do
mesmo pacote podem ter acesso aos atributos, construtores, métodos ou
classes com a ausência de um modificador de acesso.


126


[PAGINA 137]
Casa do Código                                              Capítulo 8. Pacotes



    O último modificador é o protected, que tentamos evitar no capítulo
de herança. Todo elemento que for protected ficará visível para a própria
classe, para suas classes filhas e também para quem estiver no mesmo pa-
cote. Classes também não podem utilizar esse modificador de acesso.
    A imagem a seguir representa cada modificador de acesso e sua visibili-
dade:




                                                                          127


[PAGINA 138]


[PAGINA 139]
Capítulo 9

Arrays e exception
9.1 Trabalhando com multiplicidade
Nosso CarrinhoDeCompras só está fazendo uma parte de seu trabalho, que
é acumular o valor total dos produtos adicionados. Também precisaremos ter
um atributo nessa classe para guardar uma referência a todos esses Produtos
adicionados.
    Poderíamos adicionar um número limitado de atributos do tipo
Produto, como:

♣✉❜❧✐❝ ❝❧❛ss ❈❛rr✐♥❤♦❉❡❈♦♠♣r❛s ④

    ♣r✐✈❛t❡ ❞♦✉❜❧❡ t♦t❛❧❀
    ♣r✐✈❛t❡ Pr♦❞✉t♦ ♣r♦❞✉t♦✶❀
    ♣r✐✈❛t❡ Pr♦❞✉t♦ ♣r♦❞✉t♦✷❀
    ♣r✐✈❛t❡ Pr♦❞✉t♦ ♣r♦❞✉t♦✸❀


[PAGINA 140]
9.1. Trabalhando com multiplicidade                               Casa do Código


      ♣r✐✈❛t❡ Pr♦❞✉t♦ ♣r♦❞✉t♦✹❀
      ✴✴ ✳✳✳

      ✴✴ ❞❡♠❛✐s ♠ét♦❞♦s ❞❛ ❝❧❛ss❡
⑥

    Deixando esses atributos com o tipo Produto, no lugar de um Livro
ou Revista por exemplo, o polimorfismo nos daria a flexibilidade de
adicionar qualquer classe que implemente essa interface Produto. Mas,
fora isso, nosso código não está nem um pouco flexível! Além de termos
um número limitado de produtos, no método adiciona precisaríamos
fazer várias condições para verificar qual atributo está disponível antes de adi-
cionar:

♣✉❜❧✐❝ ❝❧❛ss ❈❛rr✐♥❤♦❉❡❈♦♠♣r❛s ④

      ♣r✐✈❛t❡ ❞♦✉❜❧❡ t♦t❛❧❀
      ♣r✐✈❛t❡ Pr♦❞✉t♦ ♣r♦❞✉t♦✶❀
      ♣r✐✈❛t❡ Pr♦❞✉t♦ ♣r♦❞✉t♦✷❀
      ♣r✐✈❛t❡ Pr♦❞✉t♦ ♣r♦❞✉t♦✸❀
      ♣r✐✈❛t❡ Pr♦❞✉t♦ ♣r♦❞✉t♦✹❀
      ✴✴✳✳

      ♣✉❜❧✐❝ ✈♦✐❞ ❛❞✐❝✐♦♥❛✭Pr♦❞✉t♦ ♣r♦❞✉t♦✮ ④
          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❆❞✐❝✐♦♥❛♥❞♦✿ ✧ ✰ ♣r♦❞✉t♦✮❀

            ✐❢ ✭t❤✐s✳♣r♦❞✉t♦✶ ✦❂ ♥✉❧❧✮ ④
                t❤✐s✳♣r♦❞✉t♦✶ ❂ ♣r♦❞✉t♦❀
            ⑥
            ❡❧s❡ ✐❢ ✭t❤✐s✳♣r♦❞✉t♦✷ ✦❂ ♥✉❧❧✮ ④
                t❤✐s✳♣r♦❞✉t♦✷ ❂ ♣r♦❞✉t♦❀
            ⑥
            ❡❧s❡ ✐❢ ✭t❤✐s✳♣r♦❞✉t♦✸ ✦❂ ♥✉❧❧✮ ④
                t❤✐s✳♣r♦❞✉t♦✸ ❂ ♣r♦❞✉t♦❀
            ⑥
            ❡❧s❡ ✐❢ ✭t❤✐s✳♣r♦❞✉t♦✹ ✦❂ ♥✉❧❧✮ ④
                t❤✐s✳♣r♦❞✉t♦✹ ❂ ♣r♦❞✉t♦❀
            ⑥
            ✴✴ ✳✳✳

130


[PAGINA 141]
Casa do Código                                        Capítulo 9. Arrays e exception



          ❡❧s❡ ④
              ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧◆ã♦ t❡♠ ♠❛✐s ❡s♣❛ç♦s✧✮❀
              r❡t✉r♥❀
          ⑥
          t♦t❛❧ ✰❂ ♣r♦❞✉t♦✳❣❡t❱❛❧♦r✭✮❀
     ⑥
⑥

    Imagine como seria para mostrar os detalhes dos produtos adicionados,
novamente precisaríamos repetir esses ifs todos com as condicionais. Esse
código seria bem difícil de manter, quase inviável. Além disso, quantos atrib-
utos do tipo Produto um CarrinhoDeCompras teria? 10? 20? Isso vai
depender muito do cliente, ele pode estar comprando um único livro ou uma
coleção completa e diversos outros produtos.

Criando um array de Produto
    Evitamos até agora trabalhar com esse recurso, mas, como vimos
no primeiro capítulo, podemos resolver esse problema trabalhando com
arrays! Não lembra o que é isso? Dê uma boa olhada novamente na
declaração do método main de qualquer uma de suas classes:

♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④
    ✴✴ s❡✉ ❝ó❞✐❣♦ ❛q✉✐
⑥

    Repare que ele recebe um array de Strings como parâmetro! O
String[] args.
    Podemos      utilizar  essa     mesma      estratégia em   nosso
CarrinhoDeCompras, basta remover todos estes atributos do tipo
Produto e declarar um único array. Como fazer isso? É bem simples,
basta adicionar [] depois do tipo e pronto. Nosso CarrinhoDeCompras
vai ficar assim:

♣✉❜❧✐❝ ❝❧❛ss ❈❛rr✐♥❤♦❉❡❈♦♠♣r❛s ④

     ♣r✐✈❛t❡ ❞♦✉❜❧❡ t♦t❛❧❀
     ♣r✐✈❛t❡ Pr♦❞✉t♦❬❪ ♣r♦❞✉t♦s❀

                                                                                131


[PAGINA 142]
9.1. Trabalhando com multiplicidade                          Casa do Código




      ♣✉❜❧✐❝ ✈♦✐❞ ❛❞✐❝✐♦♥❛✭Pr♦❞✉t♦ ♣r♦❞✉t♦✮ ④
          ✴✴ ♣r❡❝✐s❛♠♦s ❛❞✐❝✐♦♥❛r ♥♦ ❛rr❛②
      ⑥
⑥

    Um array é um tipo, um objeto. Isso significa que, antes de fazer qual-
quer operação com o atributo produtos, precisaremos instanciá-lo. A sin-
taxe é um pouco diferente, mas é bem simples:
♣✉❜❧✐❝ ❝❧❛ss ❈❛rr✐♥❤♦❉❡❈♦♠♣r❛s ④

      ♣r✐✈❛t❡ ❞♦✉❜❧❡ t♦t❛❧❀
      ♣r✐✈❛t❡ Pr♦❞✉t♦❬❪ ♣r♦❞✉t♦s ❂ ♥❡✇ Pr♦❞✉t♦❬✶✵❪❀

      ✴✴✳✳
⑥

    Note que ao criar o array fomos obrigados a informar o seu tamanho!
Neste caso, criamos um array de 10 posições. Poderíamos sim receber
a quantidade de Produtos no construtor da classe ou criar um método
setProdutos, isso a deixaria um pouco mais flexível. Mas a princípio,
deixaremos o CarrinhoDeCompras assim, limitado a 10 produtos.
    Agora que estamos trabalhando com um array, precisamos mudar o
método adiciona. Podemos fazer algo como:
♣✉❜❧✐❝ ✈♦✐❞ ❛❞✐❝✐♦♥❛✭Pr♦❞✉t♦ ♣r♦❞✉t♦✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❆❞✐❝✐♦♥❛♥❞♦✿ ✧ ✰ ♣r♦❞✉t♦✮❀
    t❤✐s✳♣r♦❞✉t♦s❬✶❪ ❂ ♣r♦❞✉t♦❀
    t❤✐s✳t♦t❛❧ ✰❂ ♣r♦❞✉t♦✳❣❡t❱❛❧♦r✭✮❀
⑥

      Note que estamos adicionando todos os produtos na mesma posição do
array, na posição 1. Um detalhe muito importante é que a posição 1 é a
segunda posição do array, e não a primeira. Isso acontece pois seus índices
vão de 0 (zero) até seu tamanho -1, ou seja, como criamos um array de 10
posições, ele vai de 0 a 9.
    Uma alternativa seria mudar a assinatura do método adiciona para
receber um int indice como parâmetro, mas deixar esse controle na mão

132


[PAGINA 143]
Casa do Código                                      Capítulo 9. Arrays e exception



de quem vai chamar o método pode não ser muito interessante, isso abriria
caminho para chamar o método duas vezes com o mesmo indice e um
elemento sobrescrever o outro, por exemplo.
    No lugar disso podemos criar um atributo contador que é incremen-
tado a cada nova adição, veja:

♣✉❜❧✐❝ ❝❧❛ss ❈❛rr✐♥❤♦❉❡❈♦♠♣r❛s ④

     ♣r✐✈❛t❡ ❞♦✉❜❧❡ t♦t❛❧❀
     ♣r✐✈❛t❡ Pr♦❞✉t♦❬❪ ♣r♦❞✉t♦s ❂ ♥❡✇ Pr♦❞✉t♦❬✶✵❪❀
     ♣r✐✈❛t❡ ✐♥t ❝♦♥t❛❞♦r ❂ ✵❀

     ♣✉❜❧✐❝ ✈♦✐❞ ❛❞✐❝✐♦♥❛✭Pr♦❞✉t♦ ♣r♦❞✉t♦✮ ④
         ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❆❞✐❝✐♦♥❛♥❞♦✿ ✧ ✰ ♣r♦❞✉t♦✮❀
         t❤✐s✳♣r♦❞✉t♦s❬❝♦♥t❛❞♦r❪ ❂ ♣r♦❞✉t♦❀
         ❝♦♥t❛❞♦r ✰✰❀
         t❤✐s✳t♦t❛❧ ✰❂ ♣r♦❞✉t♦✳❣❡t❱❛❧♦r✭✮❀
     ⑥

     ♣✉❜❧✐❝ ❞♦✉❜❧❡ ❣❡t❚♦t❛❧✭✮ ④
         r❡t✉r♥ t♦t❛❧❀
     ⑥
⑥

    Problema resolvido! Sim, ainda estamos deixando passar algumas situ-
ações, como por exemplo tentar adicionar mais produtos do que cabe den-
tro de nosso array. E se eu tentar adicionar 11 produtos? Precisamos
tratar isso de alguma forma. Por enquanto, o código ficará assim, mas
em breve voltaremos para refatorar e cuidar desse tipo de detalhe da classe
CarrinhoDeCompras.




                                                                              133


[PAGINA 144]


[PAGINA 145]


[PAGINA 146]
9.2. As diferentes exceções e como lidar com elas           Casa do Código




   O enhanced-for do Java 5

     Desde o Java 1.5, é possível iterar em um array (ou qualquer outro
   Iterable, que veremos nos próximos capítulos) com uma sintaxe um
   pouco diferente. No lugar de:

   ❢♦r ✭✐♥t ✐ ❂ ✵❀ ✐ ❁ ♣r♦❞✉t♦s✳❧❡♥❣t❤❀ ✐✰✰✮ ④
       Pr♦❞✉t♦ ♣r♦❞✉t♦ ❂ ♣r♦❞✉t♦s❬✐❪❀
       ✐❢ ✭♣r♦❞✉t♦ ✦❂ ♥✉❧❧✮ ④
           ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭♣r♦❞✉t♦✳❣❡t❱❛❧♦r✭✮✮❀
       ⑥
   ⑥

       Podemos fazer o mesmo da seguinte forma, com o enhanced-for:

   ❢♦r ✭Pr♦❞✉t♦ ♣r♦❞✉t♦ ✿ ♣r♦❞✉t♦s✮ ④
       ✐❢ ✭♣r♦❞✉t♦ ✦❂ ♥✉❧❧✮ ④
           ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭♣r♦❞✉t♦✳❣❡t❱❛❧♦r✭✮✮❀
       ⑥
   ⑥

       Repare que nesse caso não temos um indice e não pre-
   cisamos conhecer o tamanho ( lenght) do array para con-
   seguir percorrê-lo, isso evitaria a confusão com o <= que causou o
   ArrayIndexOutOfBoundsException.



9.2       As diferentes exceções e como lidar com
          elas

Conhecendo a Stacktrace
Pode parecer um pouco assustador no começo, mas a stacktrace normal-
mente nos passa as informações necessárias e fundamentais para a compreen-
são e resolução dos problemas. Vamos analisá-la com mais atenção:

❊①❝❡♣t✐♦♥ ✐♥ t❤r❡❛❞ ✧♠❛✐♥✧
❥❛✈❛✳❧❛♥❣✳❆rr❛②■♥❞❡①❖✉t❖❢❇♦✉♥❞s❊①❝❡♣t✐♦♥✿ ✶✵

136


[PAGINA 147]
Casa do Código                                        Capítulo 9. Arrays e exception



     ❛t ❜r✳❝♦♠✳❝❛s❛❞♦❝♦❞✐❣♦✳❧✐✈r❛r✐❛✳t❡st❡s
         ✳❘❡❣✐str♦❉❡❱❡♥❞❛s✳♠❛✐♥✭❘❡❣✐str♦❉❡❱❡♥❞❛s✳❥❛✈❛✿✸✽✮

     Essa é uma stacktrace bem pequena, você pode perceber o quanto é
fácil de entender. A primeira linha está nos informando qual o nome do prob-
lema (ou exception, como passaremos a chamá-lo) que ocorreu no código
e nos diz em qual posição do array isso aconteceu ( 10). Na segunda e última
linha temos o fully qualified name da classe em que a exception
aconteceu, que ainda nos diz em qual linha, neste caso 38!


  Investigando problemas

     É muito comum enviarmos a stacktrace quando estamos procu-
  rando por ajuda em fóruns (como o http://guj.com.br) ou listas de dis-
  cussões. Isso facilita bastante na investigação do problema.


Tratando exceptions
     Evitar essa exception seria bem simples, bastaria corrigir a comparação
com <= ou utilizar o enhanced-for. Mas há uma forma bastante conhecida
e já utilizada em diversas linguagens para tentar executar um bloco de código
de risco e capturar caso ocorra uma exception neste bloco, evitando que a
stacktrace seja exibida para o usuário final e que a exceção pare a execução
de nosso código. Esse recurso é conhecido como try/catch.
     Para testá-lo, coloque um sysout logo após o for que está gerando o
problema no RegistroDeVendas, algo como:

❢♦r ✭✐♥t ✐ ❂ ✵❀ ✐ ❁❂ ♣r♦❞✉t♦s✳❧❡♥❣t❤❀ ✐✰✰✮ ④
    Pr♦❞✉t♦ ♣r♦❞✉t♦ ❂ ♣r♦❞✉t♦s❬✐❪❀
    ✐❢ ✭♣r♦❞✉t♦ ✦❂ ♥✉❧❧✮ ④
        ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭♣r♦❞✉t♦✳❣❡t❱❛❧♦r✭✮✮❀
    ⑥
⑥

❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❋✉✐ ❡①❡❝✉t❛❞♦✦✧✮❀


                                                                                137


[PAGINA 148]
9.2. As diferentes exceções e como lidar com elas         Casa do Código


   Rode novamente e repare na saída, a mensagem "Fui executado!"
não foi impressa. Vamos agora adicionar o try/catch e executar o código
novamente:

❢♦r ✭✐♥t ✐ ❂ ✵❀ ✐ ❁❂ ♣r♦❞✉t♦s✳❧❡♥❣t❤❀ ✐✰✰✮ ④
    tr② ④
        Pr♦❞✉t♦ ♣r♦❞✉t♦ ❂ ♣r♦❞✉t♦s❬✐❪❀
        ✐❢ ✭♣r♦❞✉t♦ ✦❂ ♥✉❧❧✮ ④
            ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭♣r♦❞✉t♦✳❣❡t❱❛❧♦r✭✮✮❀
        ⑥
    ⑥ ❝❛t❝❤ ✭❆rr❛②■♥❞❡①❖✉t❖❢❇♦✉♥❞s❊①❝❡♣t✐♦♥ ❡✮ ④
        ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❞❡✉ ❡①❝❡♣t✐♦♥ ♥♦ ✐♥❞✐❝❡✿ ✧✰ ✐✮❀
    ⑥
⑥

❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❋✉✐ ❡①❡❝✉t❛❞♦✦✧✮❀

      Agora a saída será:

❚♦t❛❧ ✽✸✳✽✶
✺✸✳✾✶
✷✾✳✾
❞❡✉ ❡①❝❡♣t✐♦♥ ♥♦ ✐♥❞✐❝❡✿ ✶✵
❋✉✐ ❡①❡❝✉t❛❞♦✦

     Como a exception foi devidamente tratada, a execução do código não
foi interrompida.




138


[PAGINA 149]
Casa do Código                                    Capítulo 9. Arrays e exception




  Entendendo a sintaxe do T R Y / C A T C H

    Pode parece um pouco estranho ou até mesmo assustador no começo,
  mas a sintaxe do try/catch não tem nada de tão complicado. Veja:

  tr② ④
      ✴✴ ❛❧❣✉♠ ❝ó❞✐❣♦ ❞❡ r✐s❝♦
  ⑥ ❝❛t❝❤ ✭❆rr❛②■♥❞❡①❖✉t❖❢❇♦✉♥❞s❊①❝❡♣t✐♦♥ ❡✮ ④
      ✴✴ ♦ q✉❡ ❢❛③❡r ❛q✉✐❄
  ⑥

     Nesse caso, dentro do catch podemos colocar o código que quere-
  mos executar apenas quando uma exception do tipo declarado acon-
  tecer. Ou seja, nele colocamos o código que queremos executar apenas
  caso um ArrayIndexOutOfBoundsException ocorra.


Toda exception é filha de Exception
    Em     nosso  try/catchm estamos capturando apenas o
ArrayIndexOutOfBoundsException,       mas    o    que   aconte-
ceria se o array produtos fosse null?        Mesmo que com o
try/catch declarado, receberíamos um outro tipo de exception, a
java.lang.NullPointerException.
    Isso  acontece     porque   estamos     deixando     claro     no
parâmetro   de     nosso      catch     que     queremos     capturar
um        ArrayIndexOutOfBoundsException,            e    não     um
NullPointerException. Poderíamos fazer algo mais genérico como:

❢♦r ✭✐♥t ✐ ❂ ✵❀ ✐ ❁❂ ♣r♦❞✉t♦s✳❧❡♥❣t❤❀ ✐✰✰✮ ④
    tr② ④
        Pr♦❞✉t♦ ♣r♦❞✉t♦ ❂ ♣r♦❞✉t♦s❬✐❪❀
        ✐❢ ✭♣r♦❞✉t♦ ✦❂ ♥✉❧❧✮ ④
            ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭♣r♦❞✉t♦✳❣❡t❱❛❧♦r✭✮✮❀
        ⑥
    ⑥ ❝❛t❝❤ ✭❊①❝❡♣t✐♦♥ ❡✮ ④
        ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❞❡✉ ❡①❝❡♣t✐♦♥ ♥♦ ✐♥❞✐❝❡✿ ✧✰ ✐✮❀


                                                                           139


[PAGINA 150]


[PAGINA 151]
Casa do Código                                        Capítulo 9. Arrays e exception



    Capturar Exception nem sempre é muito interessante, afinal se trata de
um tipo muito genérico! Muitas vezes queremos dar uma tratativa diferente
para cada tipo de exceção do código. Uma alternativa para isso seria capturar
mais de uma exception em um mesmo bloco try:
tr② ④
    Pr♦❞✉t♦ ♣r♦❞✉t♦ ❂ ♣r♦❞✉t♦s❬✐❪❀
    ✐❢ ✭♣r♦❞✉t♦ ✦❂ ♥✉❧❧✮ ④
        ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭♣r♦❞✉t♦✳❣❡t❱❛❧♦r✭✮✮❀
    ⑥
⑥ ❝❛t❝❤ ✭❆rr❛②■♥❞❡①❖✉t❖❢❇♦✉♥❞s❊①❝❡♣t✐♦♥ ❡✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❞❡✉ ❡①❝❡♣t✐♦♥ ♥♦ ✐♥❞✐❝❡✿ ✧✰ ✐✮❀
⑥ ❝❛t❝❤ ✭◆✉❧❧P♦✐♥t❡r❊①❝❡♣t✐♦♥ ❡✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❆ ❛rr❛② ♥ã♦ ❢♦✐ ✐♥st❛♥❝✐❛❞♦✦✧✮❀
⑥

    Agora estamos mostrando uma mensagem diferente para cada situação.

  M U L T I C A T C H do Java 7


    Caso você queira executar a mesma ação para dois tipos de
  Exception diferentes, desde o Java 7 você pode utilizar uma sintaxe
  um pouco diferente:

  tr② ④
          Pr♦❞✉t♦ ♣r♦❞✉t♦ ❂ ♣r♦❞✉t♦s❬✐❪❀
          ✐❢ ✭♣r♦❞✉t♦ ✦❂ ♥✉❧❧✮ ④
              ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭♣r♦❞✉t♦✳❣❡t❱❛❧♦r✭✮✮❀
          ⑥
      ⑥ ❝❛t❝❤
  ✭❆rr❛②■♥❞❡①❖✉t❖❢❇♦✉♥❞s❊①❝❡♣t✐♦♥ ⑤ ◆✉❧❧P♦✐♥t❡r❊①❝❡♣t✐♦♥ ❡✮ ④
          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❢♦✐ ✉♠❛ ❞❛s ❞✉❛s✧✮❀
      ⑥

     A   mensagem      "foi uma das duas"   será exibida
  caso uma      ArrayIndexOutOfBoundsException ou um
  NullPointerException tenha ocorrido.




                                                                                141


[PAGINA 152]
9.3. Muitas e muitas Exception                                  Casa do Código


Executando uma ação com ou sem exception
      Existem momentos em que precisamos executar alguma ação após um
try ou catch, independente se houve ou não uma exception envolvida.
Nesses casos, podemos utilizar uma terceira cláusula chamada finally.
      Observe sua sintaxe:

tr② ④
    ✴✴ ❝ó❞✐❣♦ ❞❡ r✐s❝♦
⑥ ❝❛t❝❤ ✭◆✉❧❧P♦✐♥t❡r❊①❝❡♣t✐♦♥ ❡✮ ④
    ✴✴ tr❛t❛♥❞♦ ◆P❊
⑥ ❝❛t❝❤ ✭❊①❝❡♣t✐♦♥ ❡✮ ④
    ✴✴ tr❛t❛♥❞♦ ❊①❝❡♣t✐♦♥
⑥ ❢✐♥❛❧❧② ④
    ✴✴ ❛❧❣✉♠❛ ❛çã♦ ✐♠♣♦rt❛♥t❡
⑥

    As instruções do bloco finally serão executadas sempre, independente
de tudo ter ido bem ou de alguma exception ter acontecido.
    Esse recurso é muito comum quando estamos trabalhando com conexão
do banco de dados ou leitura/escrita de arquivos. Independente de qualquer
coisa, depois de usar uma conexão, por exemplo, sempre queremos fechá-la.


9.3      Muitas e muitas Exception

As RuntimeExceptions
Claro, além de um for tentando acessar mais índices do que deveria e a
tentativa de executarmos ações em referências nulas, existem diversas outras
situações de risco em que a JVM lançará uma exception. Cada situação
dessa tem uma forma (um tipo) forte de ser representada; conhecê-las pode
ser muito importante para nosso dia a dia.
    Veremos diversas dessas situações e diferentes tipos de Exception no
decorrer deste capítulo e dos demais do livro, mas desde já é interessante en-
tendermos que todos estes casos que vimos até agora poderiam facilmente ser
evitados de forma simples pelo programador.


142


[PAGINA 153]
Casa do Código                                        Capítulo 9. Arrays e exception



    Conhecemos estes tipos de Exceptions como unchecked, pois o com-
pilador não verifica (checa) se as estamos tratando. Em outras palavras, nosso
código compilará com ou sem os try/catchs declarados.
    As unchecked exceptions não herdam diretamente da classe
Exception, mas sim de sua filha RuntimeException. Os casos mais co-
muns são:




Checked Exceptions

    Diferente disso, quando estamos fazendo a leitura de um arquivo ou qual-
quer outra operação de risco que não pode ser facilmente evitada (o ar-
quivo pode não existir, por exemplo) o compilador nos obriga a tratar esse
código! Esse é um outro tipo de exception da linguagem, conhecida como
checked exception.
    Para testar, vamos escrever o seguinte código que realiza a leitura de um

                                                                               143


[PAGINA 154]
9.3. Muitas e muitas Exception                                  Casa do Código


arquivo que não existe. Não se preocupe com o código em si, entenderemos
a API de IO (leitura e escrita) mais à frente. O ponto aqui é perceber que esse
código não compila:
♥❡✇ ❥❛✈❛✳✐♦✳❋✐❧❡■♥♣✉t❙tr❡❛♠✭✧❛rq✉✐✈♦✳t①t✧✮❀

    O erro será “Unhandled exception type FileNotFoundException
    . Note que o compilador checou que ela não está sendo tratada. Para que
o código compile poderíamos fazer algo como:
tr② ④
    ♥❡✇ ❥❛✈❛✳✐♦✳❋✐❧❡■♥♣✉t❙tr❡❛♠✭✧❛rq✉✐✈♦✳t①t✧✮❀
⑥ ❝❛t❝❤ ✭❋✐❧❡◆♦t❋♦✉♥❞❊①❝❡♣t✐♦♥ ❡✶✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧◆ã♦ ❝♦♥s❡❣✉✐ ❛❜r✐r ♦ ❛rq✉✐✈♦✧✮❀
⑥

Delegando a tratativa com throws
    Uma alternativa para o try/catch nesse caso seria adicionando um
throws FileNotFoundException. Isso significa que estamos delegando
a tratativa para quem chamar este método:
♣✉❜❧✐❝ ✈♦✐❞ ❛❜r❡❆rq✉✐✈♦✭✮ t❤r♦✇s ❋✐❧❡◆♦t❋♦✉♥❞❊①❝❡♣t✐♦♥ ④
    ♥❡✇ ❥❛✈❛✳✐♦✳❋✐❧❡■♥♣✉t❙tr❡❛♠✭✧❛rq✉✐✈♦✳t①t✧✮❀
⑥

    Dessa forma, o throws está indicando ao compilador que quem chamar
o método abreArquivo deverá tratar o FileNotFoundException. Em
outras palavras, isso diz: “Ei, esse é um código de risco, ele pode lançar uma
FileNotFoundException
    .
    Chamando-o a partir de um método main poderíamos tratar o erro:
♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④
    tr② ④
        ❛❜r❡❆rq✉✐✈♦✭✮❀
    ⑥ ❝❛t❝❤ ✭❋✐❧❡◆♦t❋♦✉♥❞❊①❝❡♣t✐♦♥ ❡✶✮ ④
        ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧◆ã♦ ❝♦♥s❡❣✉✐ ❛❜r✐r ♦ ❛rq✉✐✈♦✧✮❀
    ⑥
⑥

144


[PAGINA 155]
Casa do Código                                      Capítulo 9. Arrays e exception



     A saída será:

◆ã♦ ❝♦♥s❡❣✉✐ ❛❜r✐r ♦ ❛rq✉✐✈♦

     Ou ainda, usar o throws novamente, no próprio método main:

♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮
        t❤r♦✇s ❋✐❧❡◆♦t❋♦✉♥❞❊①❝❡♣t✐♦♥ ④

      ❛❜r❡❆rq✉✐✈♦✭✮❀
⑥

    Dessa forma, ninguém tratará a exception, estamos deixando passar
para a JVM. A saída será:

❊①❝❡♣t✐♦♥ ✐♥ t❤r❡❛❞ ✧♠❛✐♥✧ ❥❛✈❛✳✐♦✳❋✐❧❡◆♦t❋♦✉♥❞❊①❝❡♣t✐♦♥✿
❛rq✉✐✈♦✳t①t ✭◆♦ s✉❝❤ ❢✐❧❡ ♦r ❞✐r❡❝t♦r②✮

      ❛t ❥❛✈❛✳✐♦✳❋✐❧❡■♥♣✉t❙tr❡❛♠✳♦♣❡♥✭◆❛t✐✈❡ ▼❡t❤♦❞✮
      ❛t ❥❛✈❛✳✐♦✳❋✐❧❡■♥♣✉t❙tr❡❛♠✳❁✐♥✐t❃✭❋✐❧❡■♥♣✉t❙tr❡❛♠✳❥❛✈❛✿✶✸✶✮
      ❛t ❥❛✈❛✳✐♦✳❋✐❧❡■♥♣✉t❙tr❡❛♠✳❁✐♥✐t❃✭❋✐❧❡■♥♣✉t❙tr❡❛♠✳❥❛✈❛✿✽✼✮
      ❛t ❜r✳❝♦♠✳❝❛s❛❞♦❝♦❞✐❣♦✳❧✐✈r❛r✐❛✳t❡st❡s
          ✳❘❡❣✐str♦❉❡❱❡♥❞❛s✳❛❜r❡❆rq✉✐✈♦✭❘❡❣✐str♦❉❡❱❡♥❞❛s✳❥❛✈❛✿✻✷✮
      ❛t ❜r✳❝♦♠✳❝❛s❛❞♦❝♦❞✐❣♦✳❧✐✈r❛r✐❛✳t❡st❡s
          ✳❘❡❣✐str♦❉❡❱❡♥❞❛s✳♠❛✐♥✭❘❡❣✐str♦❉❡❱❡♥❞❛s✳❥❛✈❛✿✶✼✮


    T H R O W ou T H R O W S ?


       É muito comum confundir no início, mas lembre-se que usamos
    o throw no imperativo quando estamos efetivamente lançando uma
    exeption. Quando escrito no indicativo, o throws apenas informa
    ao compilador e a quem mais interessar que determinado método lança
    uma exception.




                                                                             145


[PAGINA 156]
9.3. Muitas e muitas Exception                                 Casa do Código


A familia Throwable
    Vimos que existem diversas Exceptions, sejam elas checked ou
unchecked, porém, além delas existem os tão temidos Errors. Estes são
como um tipo de exception, mas normalmente representam problemas
na JVM (como o OutOfMemoryError). Apesar de em alguns casos con-
seguirmos capturar/tratar estes erros, muitas vezes o melhor a fazer é deixar
a JVM encerrar sua execução. E apesar de ser possível, não devemos lançar
Error em nosso código. Isso não é considerado uma boa prática.
    O Error e Exception são irmãos, pois ambos herdam de Throwable!
A imagem a seguir mostra um pouco da imensa família Throwable:




146


[PAGINA 157]
Casa do Código                                      Capítulo 9. Arrays e exception



9.4     Também podemos lançar exceções!
Nosso código também pode lançar uma exception caso algo inesperado
aconteça. E não estou falando de lançar uma exception acidentalmente.
Assim como um array dispara o ArrayIndexOutOfBoundsException
quando fazemos algo inesperado (tentar acessar mais valores do que o array
suporta), podemos fazer isso com nossas regras.
    Um exemplo simples é na própria classe Livro, onde desde o início
definimos que seria obrigatório passar um Autor como argumento. A re-
gra é clara: não se pode ter um Livro sem Autor e, para garantir isso,
criamos o construtor que obrigava a passagem desse parâmetro:

♣✉❜❧✐❝ ▲✐✈r♦✭❆✉t♦r ❛✉t♦r✮ ④
    t❤✐s✳❛✉t♦r ❂ ❛✉t♦r❀
    t❤✐s✳✐s❜♥ ❂ ✧✵✵✵✲✵✵✲✵✵✵✵✵✲✵✵✲✵✧❀
⑥

    Isso já é bem interessante, mas o grande problema é que ainda podemos
passar uma referência nula de Autor no momento em que criamos o livro,
como:

▲✐✈r♦ ❧✐✈r♦ ❂ ♥❡✇ ▲✐✈r♦❋✐s✐❝♦✭♥✉❧❧✮❀

    Até poderíamos validar o valor passado para o construtor:

♣✉❜❧✐❝ ▲✐✈r♦✭❆✉t♦r ❛✉t♦r✮ ④

      ✐❢ ✭❛✉t♦r ❂❂ ♥✉❧❧✮ ④
          ✴✴ ♦ q✉❡ ❢❛③❡r ❛q✉✐❄
      ⑥
      t❤✐s✳❛✉t♦r ❂ ❛✉t♦r❀
      t❤✐s✳✐s❜♥ ❂ ✧✵✵✵✲✵✵✲✵✵✵✵✵✲✵✵✲✵✧❀
⑥

    Mas o que poderia ser feito se o autor fosse null? Assim como a API do
Java, podemos lançar exceptions para casos como esse. Essa é uma forma
mais robusta do que validar e retornar um boolean ou uma mensagem que
pode simplesmente ser ignorada.
    Veja como fica nosso código:

                                                                             147


[PAGINA 158]
9.4. Também podemos lançar exceções!                     Casa do Código


♣✉❜❧✐❝ ▲✐✈r♦✭❆✉t♦r ❛✉t♦r✮ ④

      ✐❢ ✭❛✉t♦r ❂❂ ♥✉❧❧✮ ④
          t❤r♦✇ ♥❡✇ ❘✉♥t✐♠❡❊①❝❡♣t✐♦♥✭✮❀
      ⑥
      t❤✐s✳❛✉t♦r ❂ ❛✉t♦r❀
      t❤✐s✳✐s❜♥ ❂ ✧✵✵✵✲✵✵✲✵✵✵✵✵✲✵✵✲✵✧❀
⑥

    Repare que a palavra reservada throw precede a exception que está
sendo disparada, neste caso uma RuntimeException. Há ainda a possibil-
idade de passar uma mensagem via construtor, comportamento presente na
superclasse Exception:

♣✉❜❧✐❝ ▲✐✈r♦✭❆✉t♦r ❛✉t♦r✮ ④

      ✐❢ ✭❛✉t♦r ❂❂ ♥✉❧❧✮ ④
          t❤r♦✇ ♥❡✇ ❘✉♥t✐♠❡❊①❝❡♣t✐♦♥✭
              ✧❖ ❆✉t♦r ❞♦ ▲✐✈r♦ ♥ã♦ ♣♦❞❡ s❡r ♥✉❧♦✧✮❀
      ⑥
      t❤✐s✳❛✉t♦r ❂ ❛✉t♦r❀
      t❤✐s✳✐s❜♥ ❂ ✧✵✵✵✲✵✵✲✵✵✵✵✵✲✵✵✲✵✧❀
⑥

      A saída será:
❊①❝❡♣t✐♦♥ ✐♥ t❤r❡❛❞ ✧♠❛✐♥✧ ❥❛✈❛✳❧❛♥❣✳❘✉♥t✐♠❡❊①❝❡♣t✐♦♥✿
❖ ❆✉t♦r ❞♦ ▲✐✈r♦ ♥ã♦ ♣♦❞❡ s❡r ♥✉❧♦
    ❛t ❜r✳❝♦♠✳❝❛s❛❞♦❝♦❞✐❣♦✳
        ❧✐✈r❛r✐❛✳♣r♦❞✉t♦s✳▲✐✈r♦✳❁✐♥✐t❃✭▲✐✈r♦✳❥❛✈❛✿✶✻✮
    ❛t ❜r✳❝♦♠✳❝❛s❛❞♦❝♦❞✐❣♦✳
        ❧✐✈r❛r✐❛✳♣r♦❞✉t♦s✳▲✐✈r♦❋✐s✐❝♦✳❁✐♥✐t❃✭▲✐✈r♦❋✐s✐❝♦✳❥❛✈❛✿✾✮
    ❛t ❜r✳❝♦♠✳❝❛s❛❞♦❝♦❞✐❣♦✳
❧✐✈r❛r✐❛✳t❡st❡s✳❘❡❣✐str♦❉❡❱❡♥❞❛s✳♠❛✐♥✭❘❡❣✐str♦❉❡❱❡♥❞❛s✳❥❛✈❛✿✶✻✮

Criando sua própria Exception
    No lugar de lançar uma RuntimeException, podemos criar uma
exception bem específica para esse comportamento inesperado. Vamos
criar a AutorNuloException!

148


[PAGINA 159]
Casa do Código                                      Capítulo 9. Arrays e exception



   Como fazer isso? Na verdade, é bem simples: assim como qualquer outra
Exception essa será uma classe normal que herda de Exception ou de
uma de suas filhas. Para que ela seja evitável ( uncheked), vamos herdar de
RuntimeException:

♣❛❝❦❛❣❡ ❜r✳❝♦♠✳❝❛s❛❞♦❝♦❞✐❣♦✳❧✐✈r❛r✐❛✳❡①❝❡♣t✐♦♥❀

♣✉❜❧✐❝ ❝❧❛ss ❆✉t♦r◆✉❧♦❊①❝❡♣t✐♦♥ ❡①t❡♥❞s ❘✉♥t✐♠❡❊①❝❡♣t✐♦♥ ④

     ♣✉❜❧✐❝ ❆✉t♦r◆✉❧♦❊①❝❡♣t✐♦♥✭❙tr✐♥❣ ♠❡♥s❛❣❡♠✮ ④
         s✉♣❡r✭♠❡♥s❛❣❡♠✮❀
     ⑥
⑥

    Note que criamos um construtor que delega a mensagem para o constru-
tor da superclasse, dessa forma nosso código poderá ficar assim:

♣✉❜❧✐❝ ▲✐✈r♦✭❆✉t♦r ❛✉t♦r✮ ④

     ✐❢ ✭❛✉t♦r ❂❂ ♥✉❧❧✮ ④
         t❤r♦✇ ♥❡✇ ❆✉t♦r◆✉❧♦❊①❝❡♣t✐♦♥✭
             ✧❖ ❆✉t♦r ❞♦ ▲✐✈r♦ ♥ã♦ ♣♦❞❡ s❡r ♥✉❧♦✧✮❀
     ⑥
     t❤✐s✳❛✉t♦r ❂ ❛✉t♦r❀
     t❤✐s✳✐s❜♥ ❂ ✧✵✵✵✲✵✵✲✵✵✵✵✵✲✵✵✲✵✧❀
⑥

    Rode novamente o código problemático e veja que a saída será:

❊①❝❡♣t✐♦♥ ✐♥ t❤r❡❛❞ ✧♠❛✐♥✧ ❜r✳❝♦♠✳❝❛s❛❞♦❝♦❞✐❣♦✳❧✐✈r❛r✐❛✳❡①❝❡♣t✐♦♥
        ✳❆✉t♦r◆✉❧♦❊①❝❡♣t✐♦♥✿ ❖ ❆✉t♦r ❞♦ ▲✐✈r♦ ♥ã♦ ♣♦❞❡ s❡r ♥✉❧♦
    ❛t ❜r✳❝♦♠✳❝❛s❛❞♦❝♦❞✐❣♦✳❧✐✈r❛r✐❛✳♣r♦❞✉t♦s
        ✳▲✐✈r♦✳❁✐♥✐t❃✭▲✐✈r♦✳❥❛✈❛✿✶✼✮
    ❛t ❜r✳❝♦♠✳❝❛s❛❞♦❝♦❞✐❣♦✳❧✐✈r❛r✐❛✳♣r♦❞✉t♦s
        ✳▲✐✈r♦❋✐s✐❝♦✳❁✐♥✐t❃✭▲✐✈r♦❋✐s✐❝♦✳❥❛✈❛✿✾✮
    ❛t ❜r✳❝♦♠✳❝❛s❛❞♦❝♦❞✐❣♦✳❧✐✈r❛r✐❛✳t❡st❡s
        ✳❘❡❣✐str♦❉❡❱❡♥❞❛s✳♠❛✐♥✭❘❡❣✐str♦❉❡❱❡♥❞❛s✳❥❛✈❛✿✶✻✮

    Você pode ler mais sobre Exceptions em sua documentação:


                                                                             149


[PAGINA 160]
9.4. Também podemos lançar exceções!                           Casa do Código


     http://docs.oracle.com/javase/8/docs/api/java/lang/Exception.html
     Repare que logo no inicio deste arquivo temos suas subclasses diretas
(Direct Known Subclasses). Achou que são muitas? E essas são apenas as filhas
diretas, ainda temos as filhas de RuntimeException e de suas diversas
outras subclasses.
     Por isso, sempre antes de criar uma Exception própria, tente conferir
se já não há uma implementação existente que represente bem a situação in-
esperada.




150


[PAGINA 161]
Capítulo 10

Conhecendo a API
10.1 Todo objeto tem um tipo em comum
Criamos a interface Produto para o CarrinhoDeCompras suportar a
adição de Revistas e Livros. Essa interface estabelece um tipo em comum
entre essas duas classes, portanto o CarrinhoDeCompras ficou assim:

♣✉❜❧✐❝ ❝❧❛ss ❈❛rr✐♥❤♦❉❡❈♦♠♣r❛s ④

    ♣r✐✈❛t❡ ❞♦✉❜❧❡ t♦t❛❧❀
    ♣r✐✈❛t❡ Pr♦❞✉t♦❬❪ ♣r♦❞✉t♦s ❂ ♥❡✇ Pr♦❞✉t♦❬✶✵❪❀
    ♣r✐✈❛t❡ ✐♥t ❝♦♥t❛❞♦r ❂ ✵❀

    ♣✉❜❧✐❝ ✈♦✐❞ ❛❞✐❝✐♦♥❛✭Pr♦❞✉t♦ ♣r♦❞✉t♦✮ ④
        ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❆❞✐❝✐♦♥❛♥❞♦✿ ✧ ✰ ♣r♦❞✉t♦✮❀
        t❤✐s✳♣r♦❞✉t♦s❬❝♦♥t❛❞♦r❪ ❂ ♣r♦❞✉t♦❀


[PAGINA 162]
10.1. Todo objeto tem um tipo em comum                        Casa do Código


           ❝♦♥t❛❞♦r ✰✰❀
           t❤✐s✳t♦t❛❧ ✰❂ ♣r♦❞✉t♦✳❣❡t❱❛❧♦r✭✮❀
      ⑥

      ✴✴ ❣❡tt❡rs ♣❛r❛ ♦ t♦t❛❧ ❡ ❛rr❛② ❞❡ ♣r♦❞✉t♦s
⑥

    O polimorfismo é a chave para que isso tudo funcione, nosso método
adiciona recebe um Produto como parâmetro e o acumula no array de
Produtos.
    Essa foi uma boa estratégia, mas as duas classes não precisariam im-
plementar nenhuma interface para ter um tipo em comum, pois sem-
pre que criamos uma nova classe em Java ela obrigatoriamente terá uma
superclasse.
    Até a classe Revista tem uma superclasse, mas repare em sua assi-
natura:

♣✉❜❧✐❝ ❝❧❛ss ❘❡✈✐st❛ ✐♠♣❧❡♠❡♥ts Pr♦❞✉t♦✱ Pr♦♠♦❝✐♦♥❛❧ ④

      ✴✴ ❝ó❞✐❣♦ ♦♠✐t✐❞♦
⑥

     Não há nenhum extends declarado nessa classe, como ela pode es-
tar herdando de alguém? Essa é uma situação parecida com a do constru-
tor default, lembra? Na ausência de um construtor, o compilador adi-
cionará um construtor vazio para você. Assim é com a herança, na ausência
de um extends, o Java dirá que sua classe extends um tipo conhecido
como Object.
     Com isso, podemos concluir que toda classe em Java é um Object, sem
exceção. Pode não ser diretamente, mas ainda que indiretamente, ela será,
pois herdará de alguém que herda diretamente ou indiretamente de Object.
     A grande vantagem desse tipo em comum é que toda classe herda alguns
métodos declarados na classe Object e ainda podem ser referenciadas como
tal. Logo veremos alguns desses métodos e como tirar proveito deles em nosso
dia a dia.



152


[PAGINA 163]
Casa do Código                                    Capítulo 10. Conhecendo a API



Castings e mais castings
   Se toda classe já tem esse tipo em comum, por que não mudamos
nosso CarrinhoDeCompras para receber e acumular Object, no lugar
de Produto, como estamos fazendo? Nosso código ficaria assim:

♣✉❜❧✐❝ ❝❧❛ss ❈❛rr✐♥❤♦❉❡❈♦♠♣r❛s ④

     ♣r✐✈❛t❡ ❞♦✉❜❧❡ t♦t❛❧❀
     ♣r✐✈❛t❡ ♦❜❥❡❝t❬❪ ♦❜❥❡❝ts ❂ ♥❡✇ ♦❜❥❡❝t❬✶✵❪❀
     ♣r✐✈❛t❡ ✐♥t ❝♦♥t❛❞♦r ❂ ✵❀

     ♣✉❜❧✐❝ ✈♦✐❞ ❛❞✐❝✐♦♥❛✭♦❜❥❡❝t ♦❜❥❡❝t✮ ④
         ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❆❞✐❝✐♦♥❛♥❞♦✿ ✧ ✰ ♦❜❥❡❝t✮❀
         t❤✐s✳♦❜❥❡❝ts❬❝♦♥t❛❞♦r❪ ❂ ♦❜❥❡❝t❀
         ❝♦♥t❛❞♦r ✰✰❀
         t❤✐s✳t♦t❛❧ ✰❂ ♦❜❥❡❝t✳❣❡t❱❛❧♦r✭✮❀
     ⑥

     ✴✴ ❣❡tt❡rs ♣❛r❛ ♦ t♦t❛❧ ❡ ❛rr❛② ❞❡ ♦❜❥❡❝ts
⑥

    Tente mudar seu código, que logo você perceberá o primeiro problema.
A seguinte linha não compila:

t❤✐s✳t♦t❛❧ ✰❂ ♦❜❥❡❝t✳❣❡t❱❛❧♦r✭✮❀

    Já descobriu por quê? Object não tem o método getValor, não há
garantia para o compilador de que qualquer coisa que passarmos como argu-
mento para esse método terá esse método.
    Como resolver? Bem, poderíamos fazer um casting como a seguir,
moldando a referência do Object para um Produto:

Pr♦❞✉t♦ ♠♦❧❞❛❞♦ ❂ ✭Pr♦❞✉t♦✮ ♦❜❥❡❝t❀
t❤✐s✳t♦t❛❧ ✰❂ ♠♦❧❞❛❞♦✳❣❡t❱❛❧♦r✭✮❀

    Mas, além de muito feio, esse código é muito perigoso, afinal e se o
argumento passado (que agora pode ser qualquer coisa) não implementar
Produto? O resultado seria um ClassCastException.

                                                                           153


[PAGINA 164]
10.1. Todo objeto tem um tipo em comum                       Casa do Código


    E o problema iria além. Por exemplo, para imprimir o valor dos produtos
na classe RegistroDeVendas, estamos fazendo o seguinte código:

Pr♦❞✉t♦❬❪ ♣r♦❞✉t♦s ❂ ❝❛rr✐♥❤♦✳❣❡tPr♦❞✉t♦s✭✮❀

❢♦r ✭✐♥t ✐ ❂ ✵❀ ✐ ❁❂ ♣r♦❞✉t♦s✳❧❡♥❣t❤❀ ✐✰✰✮ ④
    tr② ④
        Pr♦❞✉t♦ ♣r♦❞✉t♦ ❂ ♣r♦❞✉t♦s❬✐❪❀
        ✐❢ ✭♣r♦❞✉t♦ ✦❂ ♥✉❧❧✮ ④
            ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭♣r♦❞✉t♦✳❣❡t❱❛❧♦r✭✮✮❀
        ⑥
    ⑥ ❝❛t❝❤ ✭❆rr❛②■♥❞❡①❖✉t❖❢❇♦✉♥❞s❊①❝❡♣t✐♦♥ ❡✮ ④
        ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❞❡✉ ❡①❝❡♣t✐♦♥ ♥♦ ✐♥❞✐❝❡✿ ✧✰ ✐✮❀
        ❡✳♣r✐♥t❙t❛❝❦❚r❛❝❡✭✮❀
    ⑥
⑥

      Mas agora que já vimos que essa não é a melhor forma de iterar em um
array, podemos utilizar o enhanced-for do Java 7. Nosso código ficaria
assim:

Pr♦❞✉t♦❬❪ ♣r♦❞✉t♦s ❂ ❝❛rr✐♥❤♦✳❣❡tPr♦❞✉t♦s✭✮❀

❢♦r ✭Pr♦❞✉t♦ ♣r♦❞✉t♦ ✿ ♣r♦❞✉t♦s✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭♣r♦❞✉t♦✳❣❡t❱❛❧♦r✭✮✮❀
⑥

   Muito mais simples, não acha? Só que se produtos fosse um array de
Object, esse código não funcionaria como esperamos. Repare:

❖❜❥❡❝t❬❪ ♣r♦❞✉t♦s ❂ ❝❛rr✐♥❤♦✳❣❡tPr♦❞✉t♦s✭✮❀

❢♦r ✭❖❜❥❡❝t ♦❜❥❡❝t ✿ ♣r♦❞✉t♦s✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭♦❜❥❡❝t✳❣❡t❱❛❧♦r✭✮✮❀
⑥

   Novamente: Object não tem o método getValor, portanto, o código
não compila. Poderíamos fazer o casting, claro, mas veja como ficaria
nosso código:

154


[PAGINA 165]
Casa do Código                                     Capítulo 10. Conhecendo a API



❖❜❥❡❝t❬❪ ♣r♦❞✉t♦s ❂ ❝❛rr✐♥❤♦✳❣❡tPr♦❞✉t♦s✭✮❀

❢♦r ✭❖❜❥❡❝t ♦❜❥❡❝t ✿ ♣r♦❞✉t♦s✮ ④
    tr② ④
        Pr♦❞✉t♦ ♠♦❧❞❛❞♦ ❂ ✭Pr♦❞✉t♦✮ ♦❜❥❡❝t❀
        ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭♠♦❧❞❛❞♦✳❣❡t❱❛❧♦r✭✮✮❀
    ⑥ ❝❛t❝❤✭❈❧❛ss❈❛st❊①❝❡♣t✐♦♥ ❡✮ ④
❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❖ ♦❜❥❡t♦ ♣❛ss❛❞♦ ♥ã♦ ✐♠♣❧❡♠❡♥t❛ Pr♦❞✉t♦✧✮❀
    ⑥
⑥

    Difícil de ler, manter e nem um pouco flexível. Você já deve ter perce-
bido que receber um Object como parâmetro nem sempre é uma boa al-
ternativa, pois sempre precisaremos de castings e mais castings, não
há muito como fugir. Manter o tipo do parâmetro e array da classe
RegistroDeVendas como Produto neste caso será uma estratégia bem
mais interessante.


  C A S T I N G em uma só linha


    Também podemos fazer nossos castings em uma única linha,
  como no exemplo:

  ❞♦✉❜❧❡ ✈❛❧♦r ❂ ✭✭Pr♦❞✉t♦✮♦❜❥❡❝t✮✳❣❡t❱❛❧♦r✭✮❀

     O efeito do código seria o mesmo, mas talvez com uma sintaxe um
  pouco mais carregada custando legibilidade.


Alguns dos métodos da classe Object
    Vimos que o custo de fazer polimorfismo com Object pode nem
sempre valer a pena, mas isso não invalida o quanto ela é importante para a
linguagem Java. Nela, estão presentes todos os métodos que toda classe em
Java deve ter!
    Quer um exemplo? Alguma vez você já deve ter escrito o seguinte código:

❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❡❜♦♦❦✮❀

                                                                            155


[PAGINA 166]


[PAGINA 167]
Casa do Código                                      Capítulo 10. Conhecendo a API



contrário, o código não compilaria. Vamos testar, basta imprimir um ebook
novamente:
❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❡❜♦♦❦✮❀

    Agora a saída será:
❊✉ s♦✉ ✉♠ ❊❜♦♦❦

    É sempre interessante sobrescrever esse método, porque assim con-
seguimos estabelecer como representar nossas classes como um texto de uma
forma mais elegante do que o padrão do Object. Já estávamos fazendo isso
com o método mostrarDetalhes, lembra? Podemos modificar sua assi-
natura para que agora seja o toString das classes Livro e Autor, um
exemplo:
♣✉❜❧✐❝ ❛❜str❛❝t ❝❧❛ss ▲✐✈r♦ ✐♠♣❧❡♠❡♥ts Pr♦❞✉t♦ ④

     ✴✴ ❝ó❞✐❣♦ ♦♠✐t✐❞♦

     ❅❖✈❡rr✐❞❡
     ♣✉❜❧✐❝ ✈♦✐❞ t♦❙tr✐♥❣✭✮ ④
         ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧◆♦♠❡✿ ✧ ✰ ♥♦♠❡✮❀
         ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❉❡s❝r✐çã♦✿ ✧ ✰ ❞❡s❝r✐❝❛♦✮❀
         ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❱❛❧♦r✿ ✧ ✰ ✈❛❧♦r✮❀
         ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧■❙❇◆✿ ✧ ✰ ✐s❜♥✮❀

          ✐❢ ✭t❤✐s✳t❡♠❆✉t♦r✭✮✮ ④
              ❛✉t♦r✳t♦❙tr✐♥❣✭✮❀
          ⑥
          ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧✲✲✧✮❀
     ⑥
⑥

Comparando objetos com equals
    Outra situação muito comum em nosso dia a dia é a necessidade de com-
parar objetos. Vimos nos primeiros capítulos do livro que == sempre com-
para o valor dos atributos, que em caso de objetos será sua referência. Isso
significa que o resultado da seguinte comparação será false:

                                                                             157


[PAGINA 168]
10.1. Todo objeto tem um tipo em comum                       Casa do Código


❆✉t♦r ❛✉t♦r ❂ ♥❡✇ ❆✉t♦r✭✮❀
❛✉t♦r✳s❡t◆♦♠❡✭✧❘♦❞r✐❣♦ ❚✉r✐♥✐✧✮❀

❆✉t♦r ❛✉t♦r✷ ❂ ♥❡✇ ❆✉t♦r✭✮❀
❛✉t♦r✷✳s❡t◆♦♠❡✭✧❘♦❞r✐❣♦ ❚✉r✐♥✐✧✮❀

✐❢ ✭❛✉t♦r ❂❂ ❛✉t♦r✷✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧■❣✉❛❧✧✮❀
⑥ ❡❧s❡ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❉✐❢❡r❡♥t❡✧✮❀
⑥

    Execute o código para comprovar: será impressa a palavra Diferente.
Faz sentido, já era de se esperar. Mas e se estivermos interessados em com-
parar os valores dos atributos? Podemos utilizar outro método muitíssimo
interessante da classe Object, o equals. Mas o Java por si só não vai saber
como queremos comparar nossos Autores, se eu apenas mudar o código
para utilizar o equals da forma a seguir, o resultado ainda será false:

✐❢ ✭❛✉t♦r✳❡q✉❛❧s✭❛✉t♦r✷✮✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧■❣✉❛❧✧✮❀
⑥ ❡❧s❡ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❉✐❢❡r❡♥t❡✧✮❀
⑥

    O resultado ainda será false, pois o método equals da classe Object
faz uma comparação com ==, assim como já estávamos fazendo. Mas, afinal,
qual a vantagem de usar o equals? Podemos sobrescrevê-lo ensinando quais
são os critérios de comparação. Um exemplo:

♣✉❜❧✐❝ ❝❧❛ss ❆✉t♦r ④

      ✴✴ ❛tr✐❜✉t♦s ❡ ♠ét♦❞♦s ♦♠✐t✐❞♦s

      ❅❖✈❡rr✐❞❡
      ♣✉❜❧✐❝ ❜♦♦❧❡❛♥ ❡q✉❛❧s✭❖❜❥❡❝t ♦❜❥✮ ④
          ❆✉t♦r ♦✉tr♦ ❂ ✭❆✉t♦r✮ ♦❜❥❀
          r❡t✉r♥ t❤✐s✳♥♦♠❡✳❡q✉❛❧s✭♦✉tr♦✳♥♦♠❡✮❀


158


[PAGINA 169]
Casa do Código                                       Capítulo 10. Conhecendo a API



     ⑥
⑥

    Estamos definindo que, sempre que um Autor tiver um nome igual ao
outro, eles são iguais; em outras palavras, o equals deve retornar true.
Vamos entender melhor essa sobrescrita, a começar pala linha:

❆✉t♦r ♦✉tr♦ ❂ ✭❆✉t♦r✮ ♦❜❥❀

     Note que o equals recebe Object como argumento, portanto a
primeira coisa que fizemos ao implementá-lo foi moldar esse parâmetro para
o tipo Autor. Sim, há um risco bem grande de um ClassCastException
caso o parâmetro passado não seja realmente um Autor, depois veremos
algumas alterativas para lidar com isso.
     Veja que logo em seguida fazemos o seguinte retorno:

r❡t✉r♥ t❤✐s✳♥♦♠❡✳❡q✉❛❧s✭♦✉tr♦✳♥♦♠❡✮❀

    Qual seria o problema de fazer o seguinte?

r❡t✉r♥ t❤✐s✳♥♦♠❡ ❂❂ ♦✉tr♦✳♥♦♠❡❀

    Já percebeu? Claro, String é um objeto, logo estaríamos comparando
sua referência. Adiante falaremos mais sobre o problema da comparação
de Strings, mas o importante agora é perceber que estamos delegando a
comparação do nome ( String) para o método equals da própria classe
String. Ele foi sobrescrito para fazer a comparação pelo texto passado, e não
pela referência de memória.

Lidando com o ClassCastException
    Vimos brevemente que uma ClassCastException pode ser lançada
caso o parâmetro passado para o equals não seja do mesmo tipo moldado,
como no seguinte exemplo:

✐❢✭❛✉t♦r✳❡q✉❛❧s✭✧❘♦❞r✐❣♦✧✮✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧✐❣✉❛✐s✧✮❀
⑥


                                                                              159


[PAGINA 170]
10.1. Todo objeto tem um tipo em comum                         Casa do Código


      Esse
        código             compilará     sem nenhum problema,        afinal
String é um               Object.        Mas ao executá-lo recebemos uma
java.lang.ClassCastException: java.lang.String cannot
be cast to br.com.casadocodigo.livraria.Autor. Como re-
solver? Uma maneira seria tratando com um try/catch, mas veja como o
código fica verboso e difícil de ler:
❅❖✈❡rr✐❞❡
♣✉❜❧✐❝ ❜♦♦❧❡❛♥ ❡q✉❛❧s✭❖❜❥❡❝t ♦❜❥✮ ④

      ❆✉t♦r ♦✉tr♦❀
      tr② ④
          ♦✉tr♦ ❂ ✭❆✉t♦r✮ ♦❜❥❀
      ⑥ ❝❛t❝❤ ✭❈❧❛ss❈❛st❊①❝❡♣t✐♦♥ ❡✮ ④
          r❡t✉r♥ ❢❛❧s❡❀
      ⑥

      r❡t✉r♥ t❤✐s✳♥♦♠❡✳❡q✉❛❧s✭♦✉tr♦✳♥♦♠❡✮❀
⑥

    Uma forma mais interessante seria utilizando o instanceof, como a
seguir:
❅❖✈❡rr✐❞❡
♣✉❜❧✐❝ ❜♦♦❧❡❛♥ ❡q✉❛❧s✭❖❜❥❡❝t ♦❜❥✮ ④
    ✐❢ ✭✦✭♦❜❥ ✐♥st❛♥❝❡♦❢ ❆✉t♦r✮✮ r❡t✉r♥ ❢❛❧s❡❀
    ❆✉t♦r ♦✉tr♦ ❂ ✭❆✉t♦r✮ ♦❜❥❀
    r❡t✉r♥ t❤✐s✳♥♦♠❡✳❡q✉❛❧s✭♦✉tr♦✳♥♦♠❡✮❀
⑥

      Dessa maneira, se o parâmetro passado não foi uma instância do tipo
Autor, retornamos false indicando que não são objetos iguais.
    Existem outros métodos interessantes na classe Object, alguns deles são
o getClass e hashcode. Falaremos deste último no próximo capítulo, mas
saiba desde já que ele sempre acompanha o equals. Um exemplo simples
de uso do getClass seria para mostrar o nome simples da classe, sem seu
pacote ( fully qualified name). Repare:
❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❛✉t♦r✳❣❡t❈❧❛ss✭✮✳❣❡t❙✐♠♣❧❡◆❛♠❡✭✮✮❀

160


[PAGINA 171]
Casa do Código                                       Capítulo 10. Conhecendo a API



10.2 Wrappers dos tipos primitivos
Já não é nenhuma surpresa que o seguinte código compile:

❖❜❥❡❝t ♦❜❥❡t♦ ❂ ♥❡✇ ❆✉t♦r✭✧❘♦❞r✐❣♦✧✮❀

    Nem mesmo se for apenas uma String, pois todo objeto em Java herda
direta ou indiretamente de Object.

❖❜❥❡❝t ♦❜❥❡t♦ ❂ ✧❯♠❛ ❙tr✐♥❣✧❀

    Mas o que você acha do código a seguir?

❖❜❥❡❝t ♦❜❥❡t♦ ❂ ✶✵❀

    Se você estiver utilizando uma versão maior que Java 1.4, ele compilará.
Isso não significa que os tipos primitivos como o int herdam de Object ou
são do mesmo tipo que uma referência, esse é apenas um truque do compi-
lador adicionado no Java 1.5 para simplificar um pouco a sintaxe. Esse recurso
é conhecido como autoboxing.
    Sem isso, para que o código compile precisaríamos fazer:

❖❜❥❡❝t ♦❜❥❡t♦ ❂ ♥❡✇ ■♥t❡❣❡r✭✶✵✮❀

   Note que a classe Integer é usada para embrulhar ( wrapping) o tipo
primitivo int, de forma que podemos tratá-la como uma referência, um
Object. O mesmo se aplica aos demais tipos primitivos. A imagem a seguir
mostra cada um deles e sua classe wrapper (box).




                                                                              161


[PAGINA 172]
10.2. Wrappers dos tipos primitivos                            Casa do Código




   Também podemos desembrulhar os valores primitivos das classes
wrappers:

■♥t❡❣❡r ✐♥t❡❣❡r ❂ ♥❡✇ ■♥t❡❣❡r✭✶✵✮❀
✐♥t ✈❛❧♦r ❂ ✐♥t❡❣❡r✳✐♥t❱❛❧✉❡✭✮❀

   Mas essa não é a única utilidade das classes wrappers, elas estão repletas
de métodos estáticos que podem ser bastante úteis para manipular os tipos
primitivos.

Conversão de valores
    Como transformar um boolean em uma String? E o contrário? Como
transformar um texto em um double válido? Todas essas conversões po-
dem ser feitas de forma bem simples a partir das classes que embrulham esses


162


[PAGINA 173]
Casa do Código                                     Capítulo 10. Conhecendo a API



tipos primitivos. Por exemplo, o método parseBoolean da classe Boolean
transforma uma String em um booleano. Veja:

❜♦♦❧❡❛♥ r❡s✉❧t❛❞♦ ❂ ❇♦♦❧❡❛♥✳♣❛rs❡❇♦♦❧❡❛♥✭✧❢❛❧s❡✧✮❀

    O mesmo pode ser feito para os demais tipos:

❜②t❡ ♣❛rs❡❇②t❡ ❂ ❇②t❡✳♣❛rs❡❇②t❡✭✧✶✧✮❀
s❤♦rt ♣❛rs❡❙❤♦rt ❂ ❙❤♦rt✳♣❛rs❡❙❤♦rt✭✧✶✵✧✮❀
✐♥t ♣❛rs❡■♥t ❂ ■♥t❡❣❡r✳♣❛rs❡■♥t✭✧✶✵✧✮❀
❧♦♥❣ ♣❛rs❡▲♦♥❣ ❂ ▲♦♥❣✳♣❛rs❡▲♦♥❣✭✧✶✵✧✮❀
❢❧♦❛t ♣❛rs❡❋❧♦❛t ❂ ❋❧♦❛t✳♣❛rs❡❋❧♦❛t✭✧✶✵✳✵✧✮❀
❞♦✉❜❧❡ ♣❛rs❡❉♦✉❜❧❡ ❂ ❉♦✉❜❧❡✳♣❛rs❡❉♦✉❜❧❡✭✧✶✵✳✵✧✮❀

     Para transformar qualquer um desses valores em uma String, podemos
utilizar seu método estático valueOf:

❙tr✐♥❣ ♥✉♠❡r♦❊♠❚❡①t♦ ❂ ❙tr✐♥❣✳✈❛❧✉❡❖❢✭✶✵✮❀

    Claro, precisamos tomar bastante cuidado com o valor passado, pois adi-
vinhe qual será o resultado do código a seguir?

✐♥t ♣❛rs❡■♥t ❂ ■♥t❡❣❡r✳♣❛rs❡■♥t✭✧❆❇❈✧✮❀

   Uma Exception! Neste caso: java.lang.NumberFormatException:
For input string: "ABC". Faz bastante sentido, afinal, como transfor-
mar ABC em um número?


  Mais métodos úteis

     Aproveite o momento para explorar os diversos métodos existentes
  em Object e nas classes wrappers, como a Interger. Eles com certeza
  serão bem úteis em seu dia a dia codando em Java!


10.3 O pacote java.lang
Você já deve ter percebido que até agora não precisamos fazer import de
nenhuma das novas classes que vimos neste capítulo. Outro detalhe é que em

                                                                            163


[PAGINA 174]
10.3. O pacote java.lang                                     Casa do Código


nenhum momento anterior precisamos fazer import da classe String ou
mesmo da classe System, não é?
    Isso porque Object, String, System, classes wrappers dos tipos
primitivos entre diversas outras estão todas presentes no pacote padrão do
Java, o java.lang. Este pacote é automaticamente incluído em todas as
suas classes, diferente de todos os demais da linguagem.
    Nele você encontrará classes como a Math, que tem um arsenal completo
de métodos que o auxiliam em operações numéricas como arredondamento
( round), mínimo ( min), máximo ( max), seno ( sin), entre muitos outros.
Alguns exemplos de uso:

❧♦♥❣ r♦✉♥❞ ❂ ▼❛t❤✳r♦✉♥❞✭✸✳✾✾✮❀
❧♦♥❣ ♠❛① ❂ ▼❛t❤✳♠❛①✭✶✵✵✱ ✶✵✮❀
✐♥t ♠✐♥ ❂ ▼❛t❤✳♠✐♥✭✶✵✵✱ ✶✵✮❀
✐♥t ❛❜s ❂ ▼❛t❤✳❛❜s✭✲✺✮❀
❞♦✉❜❧❡ sqrt ❂ ▼❛t❤✳sqrt✭✹✮❀

      Os valores das variáveis, respectivamente, serão:

✹
✶✵✵
✶✵
✺
✷✳✵

   Você pode ver a documentação completa dessa classe em:
   http://docs.oracle.com/javase/8/docs/api/java/lang/Math.html
   Outra classe muito útil em nosso dia a dia é a Random, veja como é fácil
imprimir um número aleatório de 0 a 10:

❘❛♥❞♦♠ r❛♥❞♦♠ ❂ ♥❡✇ ❘❛♥❞♦♠✭✮❀
❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭r❛♥❞♦♠✳♥❡①t■♥t✭✶✵✮✮❀

    Da mesma forma como o nextInt, também existe um método next
para cada tipo primitivo, como o nextBoolean ou nextDouble.




164


[PAGINA 175]
Casa do Código                                     Capítulo 10. Conhecendo a API



java.lang.String

   Para fechar nosso passeio pelo pacote padrão do Java, vamos entender um
pouco melhor a classe String. É muito comum confundi-la com um tipo
primitivo, mas Strings guardam referências a objetos. A prova disso é que
podemos instanciá-la da seguinte forma:

❙tr✐♥❣ ❥❛✈❛ ❂ ♥❡✇ ❙tr✐♥❣✭✧❏❛✈❛✧✮❀

    Assim como qualquer outra variável de referência, não devemos
compará-la utilizando o operador ==, mas sim o equals que foi reescrito na
classe String para comparar cada caractere do texto. Portanto, o resultado
do código a seguir será true:

❙tr✐♥❣ ❥❛✈❛ ❂ ✧❥❛✈❛✧❀
❙tr✐♥❣ ❥❛✈❛✷ ❂ ✧❥❛✈❛✧❀

❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❥❛✈❛✳❡q✉❛❧s✭❥❛✈❛✷✮✮❀

    Mas algo bastante inesperado acontecerá ao compararmos duas Strings
desta forma:

❙tr✐♥❣ ❥❛✈❛ ❂ ✧❥❛✈❛✧❀
❙tr✐♥❣ ❥❛✈❛✷ ❂ ✧❥❛✈❛✧❀

❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❥❛✈❛ ❂❂ ❥❛✈❛✷✮❀

     Aqui, o resultado também será true! Por quê? Isso acontece pois, por
otimização, o Java cria um String pool, um tipo de cache de Strings.
Sempre antes de adicionar em memória, a JVM consulta esse pool para ver-
ificar se não há uma String igual que possa ser reutilizada.
     Para que isso funcione bem, o Java não poderia permitir que a mudança
no valor de uma String afetasse outras Strings que tivessem seu mesmo
valor. Por isso, toda String é imutável.
     Quer uma prova? Tente substituir o valor de uma String com seu
método replace. É bem simples, o primeiro argumento será o valor atual e
o segundo o valor que deverá tomar o seu lugar, por exemplo:


                                                                            165


[PAGINA 176]
10.3. O pacote java.lang                                       Casa do Código


❥❛✈❛✳r❡♣❧❛❝❡✭✧✈✧✱ ✧❝✧✮❀
❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❥❛✈❛✮❀

     É natural esperar que o resultado impresso seja “jaca”, uma vez que sub-
stituímos o caractere “v” por “c”, mas rode o código para ver o resultado:

❥❛✈❛

    É isso mesmo, o valor da variável java continuou o mesmo, já que toda
String é imutável. Para obter o resultado esperado, podemos resgatar o re-
torno do método replace, que será uma nova String. Repare:

❙tr✐♥❣ ♥♦✈❛❙tr✐♥❣ ❂ ❥❛✈❛✳r❡♣❧❛❝❡✭✧✈✧✱ ✧❝✧✮❀
❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭♥♦✈❛❙tr✐♥❣✮❀

    O mesmo vale para todo método que aplica transformações da String,
eles sempre retornam uma referência nova para o valor transformado.
    Agora que já conhecemos essa característica fundamental, podemos usar
os seus mais de 60 métodos. Alguns exemplos são:

❙tr✐♥❣ r❡♣❧❛❝❡ ❂ ❥❛✈❛✳r❡♣❧❛❝❡✭✧✈✧✱ ✧❝✧✮❀
❙tr✐♥❣ ✉♣♣❡r❈❛s❡ ❂ ❥❛✈❛✳t♦❯♣♣❡r❈❛s❡✭✮❀
❙tr✐♥❣ ❧♦✇❡r❈❛s❡ ❂ ✧❏❆❱❆✧✳t♦▲♦✇❡r❈❛s❡✭✮❀
❝❤❛r ❝❤❛r❆t ❂ ❥❛✈❛✳❝❤❛r❆t✭✵✮❀
❜♦♦❧❡❛♥ ❡♥❞s❲✐t❤ ❂ ❥❛✈❛✳❡♥❞s❲✐t❤✭✧❛✧✮❀
❜♦♦❧❡❛♥ st❛rts❲✐t❤ ❂ ❥❛✈❛✳st❛rts❲✐t❤✭✧s✧✮❀
❜♦♦❧❡❛♥ ❡q✉❛❧s ❂ ❥❛✈❛✳❡q✉❛❧s■❣♥♦r❡❈❛s❡✭✧❏❆❱❆✧✮❀

      Os valores das variáveis, respectivamente, serão:

❥❛❝❛
❏❆❱❆
❥❛✈❛
❥
tr✉❡
❢❛❧s❡
tr✉❡

    Dominar o pacote padrão do Java é um grande diferencial. Muitas vezes
já há algo implementado para nos ajudar com situações do dia a dia. Em

166


[PAGINA 177]
Casa do Código                                    Capítulo 10. Conhecendo a API



outras palavras, o pacote java.lang com certeza fará parte de sua rotina.
Aproveite para estudar seus diversos outros métodos e classes. Você pode
encontrar a documentação completa em:
    http://docs.oracle.com/javase/8/docs/api/java/lang/package-summary.
html




                                                                           167


[PAGINA 178]


[PAGINA 179]
Capítulo 11

Collection Framework
11.1 O trabalho de manipular arrays
A princípio, deixamos nosso CarrinhoDeCompras limitando o total de
Produtos em 10 itens. Um número fixo e nem um pouco real. Uma forma
simples de flexibilizar a quantidade de Produtos seria forçando a passagem
do array de Produtos pelo construtor:

♣✉❜❧✐❝ ❝❧❛ss ❈❛rr✐♥❤♦❉❡❈♦♠♣r❛s ④

    ♣r✐✈❛t❡ ❞♦✉❜❧❡ t♦t❛❧❀
    ♣r✐✈❛t❡ Pr♦❞✉t♦❬❪ ♣r♦❞✉t♦s❀
    ♣r✐✈❛t❡ ✐♥t ❝♦♥t❛❞♦r ❂ ✵❀

    ♣✉❜❧✐❝ ❈❛rr✐♥❤♦❉❡❈♦♠♣r❛s✭Pr♦❞✉t♦❬❪ ♣r♦❞✉t♦s✮ ④
        t❤✐s✳♣r♦❞✉t♦s ❂ ♣r♦❞✉t♦s❀


[PAGINA 180]
11.1. O trabalho de manipular arrays                          Casa do Código


      ⑥

      ✴✴ ♦✉tr♦s ♠ét♦❞♦s ❞❛ ❝❧❛ss❡
⑥

    Isso torna seu uso um pouco mais interessante. No momento de criar um
CarrinhoDeCompras, passamos a quantidade de Produtos que poderá ser
adicionada, como:

❈❛rr✐♥❤♦❉❡❈♦♠♣r❛s ❝❛rr✐♥❤♦ ❂
    ♥❡✇ ❈❛rr✐♥❤♦❉❡❈♦♠♣r❛s✭♥❡✇ Pr♦❞✉t♦❬ ✶✵ ❪✮❀

    Mas como saber exatamente se teremos 2, 10, ou 100 Produtos neste
carrinho? Não há um valor fixo, afinal o cliente poderá comprar quantos pro-
dutos ele bem entender. O ponto é que a necessidade de passar um número
fixo no momento de instanciar um array não ajuda muito neste momento.
E o tamanho de um array nunca muda; depois de criado, ele terá aquela
capacidade e ponto, nunca poderá ser redimensionado.
    Poderíamos, sim, no momento de adicionar novos produtos verificar se
há espaço livre no array, e caso não haja, criar um novo com mais espaço
e mover os objetos do antigo para ele. Mas isso seria muito trabalhoso, não
acha? E não é o único trabalho que teríamos ao utilizar um array.
    Outra necessidade seria remover produtos do CarrinhoDeCompras.
Uma implementação simples do método remove seria:

♣✉❜❧✐❝ ✈♦✐❞ r❡♠♦✈❡✭✐♥t ♣♦s✐❝❛♦✮ ④
    t❤✐s✳♣r♦❞✉t♦s❬♣♦s✐❝❛♦❪ ❂ ♥✉❧❧❀
⑥

    Ao atribuir null para determinada posição, ganhamos uma série de
problemas. Repare como ficará nosso array após removermos o elemento
de posição 2:




170


[PAGINA 181]
Casa do Código                                    Capítulo 11. Collection Framework




     E agora, como faremos ao adicionar novos itens? Estávamos inserindo
sequencialmente, mas precisaremos considerar as possíveis posições vazias
no meio do array.
     Uma possibilidade seria criar um outro array, guardando as posições
livres, e consultá-lo antes de inserir um novo Produto. Outra possibilidade
seria sempre reordenar o array depois de remover um item. Mas repare
bem, todas elas tornariam nosso código mais complexo e difícil de manter.
     Manipular um array é bastante trabalhoso. Essas foram apenas algu-
mas das muitas questões que apareceriam em nosso código. Por esse e outros
motivos, o Java2 1.2 introduziu um conjunto de classes e interfaces bastante
conhecido como Collections Framework. Essa robusta API traz estruturas
bem mais interessantes para lidar com os mais diferentes tipos de dados.

ArrayList versus array

    No lugar de trabalhar diretamente com arrays, podemos utilizar uma
ArrayList para representar a multiplicidade de Produtos e nos auxiliar
nas operações necessárias em nosso CarrinhoDeCompras. Essa classe é
uma das introduções da API de Collections, veja a seguir como seu uso
é simples.

❆rr❛②▲✐st ❧✐st❛ ❂ ♥❡✇ ❆rr❛②▲✐st✭✮❀
❙tr✐♥❣ ✈❛❧♦r ❂ ✧❝♦♥❤❡❝❡♥❞♦ ✉♠❛ ❆rr❛②▲✐st✧❀
❧✐st❛✳❛❞❞✭✈❛❧♦r✮❀
❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❧✐st❛✳❝♦♥t❛✐♥s✭✈❛❧♦r✮✮❀
❧✐st❛✳r❡♠♦✈❡✭✈❛❧♦r✮❀

                                                                               171


[PAGINA 182]
11.1. O trabalho de manipular arrays                           Casa do Código


❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❧✐st❛✳❝♦♥t❛✐♥s✭✈❛❧♦r✮✮❀

      A saída será:

tr✉❡
❢❛❧s❡

    O ArrayList tem um conjunto de métodos que, na maior parte do
tempo, representam bem as nossas necessidades. O método remove pode
agora receber o próprio valor a ser removido, mas também tem uma sobre-
carga que recebe a posição que deve ser removida. Você pode escolher qual
opção lhe atender melhor.
    Um ponto muito interessante é que o ArrayList, assim como as de-
mais classes da API de Collection, trabalham de forma genérica. Caso
contrário, haveria uma ArrayList para cada tipo de dado que precisásse-
mos adicionar, como uma String, um int, ou mesmo uma data. Todos os
seus métodos trabalham com Object.
    Portanto, o seguinte código compila:

❆rr❛②▲✐st ❧✐st❛ ❂ ♥❡✇ ❆rr❛②▲✐st✭✮❀
❧✐st❛✳❛❞❞✭✶✵✮❀
❧✐st❛✳❛❞❞✭✧✉♠❛ str✐♥❣✧✮❀
❧✐st❛✳❛❞❞✭♥❡✇ ❘❡✈✐st❛✭✮✮❀

     Mas já vimos o problema de trabalhar com Object dessa forma: será
necessário um casting sempre que precisarmos recuperar um valor dessa
lista. Por exemplo:

✐♥t ✈❛❧♦r ❂ ✭✐♥t✮ ❧✐st❛✳❣❡t✭✵✮❀

     E se o valor do índice zero não fosse um int? Como saber exatamente
o tipo de cada elemento em cada posição da lista? Trabalhar dessa forma não
seria nem um pouco simples, não acha? E na maior parte do tempo, queremos
ter uma lista de um único tipo, e não vários como fizemos agora. Por exemplo,
nosso CarrinhoDeCompras deverá ter uma lista de Produtos.
     Para auxiliar nesse trabalho, desde o Java 5 podemos restringir o tipo
de objetos de uma determinada lista utilizando um recurso conhecido como
Generics. Repare:

172


[PAGINA 183]
Casa do Código                                  Capítulo 11. Collection Framework



❆rr❛②▲✐st❁Pr♦❞✉t♦❃ ♣r♦❞✉t♦s ❂ ♥❡✇ ❆rr❛②▲✐st❁Pr♦❞✉t♦❃✭✮❀

    A sintaxe pode parecer estranha no começo, mas note que a única mu-
dança é que agora estamos indicando ao compilador que essa lista deve tra-
balhar com Produtos. Há dois grandes ganhos aqui, o primeiro será pela
não necessidade de um casting ao recuperar valores desta lista. Veja:

Pr♦❞✉t♦ ❜✉s❝❛❞♦ ❂ ♣r♦❞✉t♦s✳❣❡t✭✵✮❀

    O código fica bem mais limpo sem os castings e evitamos as recorrentes
ClassCastExceptions. O outro ganho será a segurança de que não con-
seguiremos adicionar nada que não seja do tipo Produto nessa lista. O
seguinte código não compila:

♣r♦❞✉t♦s✳❛❞❞✭✧❊✉ ♥ã♦ s♦✉ ✉♠ ♣r♦❞✉t♦✧✮❀




                                                                             173


[PAGINA 184]
11.1. O trabalho de manipular arrays                          Casa do Código




   diamond operator do Java 7

       Desde o Java 7, no lugar de passar o tipo genérico duas vezes como
   fizemos ao instanciar a lista de Produtos, podemos utilizar um re-
   curso conhecido como diamond operator (operador diamante), deixando
   o código assim:

   ❆rr❛②▲✐st❁Pr♦❞✉t♦❃ ♣r♦❞✉t♦s ❂ ♥❡✇ ❆rr❛②▲✐st❁❃✭✮❀

       Esse recurso era bastante limitado, funcionava basicamente se a
   declaração fosse feita na mesma linha. No Java 8, a inferência de tipos
   foi bastante melhorada e, como um efeito colateral, agora podemos fazer
   códigos como este:

   ♣✉❜❧✐❝ ❝❧❛ss ❈❛rr✐♥❤♦❉❡❈♦♠♣r❛s ④

         ♣r✐✈❛t❡ ❆rr❛②▲✐st❁Pr♦❞✉t♦❃ ♣r♦❞✉t♦s❀

         ♣✉❜❧✐❝ ❈❛rr✐♥❤♦❉❡❈♦♠♣r❛s✭✮ ④
             t❤✐s✳♣r♦❞✉t♦s ❂ ♥❡✇ ❆rr❛②▲✐st❁❃✭✮❀
         ⑥
   ⑥

      Note que só estamos instanciando o ArrayList no construtor
   da classe, mas como o compilador sabe inferir bem qual o tipo do
   this.produtos, conseguimos utilizar o diamante sem nenhum prob-
   lema.


       Veja como fica nossa classe CarrinhoDeCompras utilizando uma lista:

♣✉❜❧✐❝ ❝❧❛ss ❈❛rr✐♥❤♦❉❡❈♦♠♣r❛s ④

       ♣r✐✈❛t❡ ❞♦✉❜❧❡ t♦t❛❧❀
       ♣r✐✈❛t❡ ❆rr❛②▲✐st❁Pr♦❞✉t♦❃ ♣r♦❞✉t♦s❀

       ♣✉❜❧✐❝ ❈❛rr✐♥❤♦❉❡❈♦♠♣r❛s✭✮ ④
           t❤✐s✳♣r♦❞✉t♦s ❂ ♥❡✇ ❆rr❛②▲✐st❁❃✭✮❀


174


[PAGINA 185]
Casa do Código                                    Capítulo 11. Collection Framework



     ⑥

     ♣✉❜❧✐❝ ✈♦✐❞ ❛❞✐❝✐♦♥❛✭Pr♦❞✉t♦ ♣r♦❞✉t♦✮ ④
         t❤✐s✳♣r♦❞✉t♦s✳❛❞❞✭♣r♦❞✉t♦✮❀
     ⑥

     ♣✉❜❧✐❝ ✈♦✐❞ r❡♠♦✈❡✭✐♥t ♣♦s✐❝❛♦✮ ④
         t❤✐s✳♣r♦❞✉t♦s✳r❡♠♦✈❡✭♣♦s✐❝❛♦✮❀
     ⑥

     ♣✉❜❧✐❝ ❞♦✉❜❧❡ ❣❡t❚♦t❛❧✭✮ ④
         r❡t✉r♥ t♦t❛❧❀
     ⑥

     ♣✉❜❧✐❝ ❆rr❛②▲✐st❁Pr♦❞✉t♦❃ ❣❡tPr♦❞✉t♦s✭✮ ④
         r❡t✉r♥ ♣r♦❞✉t♦s❀
     ⑥
⑥

     Muito mais simples, não acha? Não precisamos de um atributo
contador, não temos que limitar o tamanho do array, entre outras desvan-
tagens comentadas.
     É interessante reconhecer que um ArrayList não é um array! Essa
confusão é bastante comum, mas na verdade ArrayList usa um array
internamente para armazenar os dados, mas isso está bem encapsulado. Em
nenhum momento precisaremos recuperar seu array interno para fazer op-
erações mais complexas, não temos acesso a ele e nem deveríamos.
     O ArrayList resolve todos os problemas que comentamos do array.
Utilizá-lo, com certeza, será uma melhor opção. Mas existem outros tipos de
lista que não utilizam necessariamente um array internamente. Um exem-
plo é a LinkedList (lista ligada); enquanto a ArrayList é mais rápida
para fazer pesquisas (iterar), a LinkedList é mais rápida para inserir e re-
mover elementos de suas pontas.
     Cada estrutura tem suas vantagens, vale a pena conhecer as diferenças
entre elas para tomar uma boa decisão no momento de utilizar uma lista.
     O que todas elas têm em comum é a interface List, do pacote
java.util. Para não deixar nosso código dependendo de um tipo de lista

                                                                               175


[PAGINA 186]
11.1. O trabalho de manipular arrays                        Casa do Código


específico (acoplamento), já que podemos a qualquer momento mudá-las, é
uma boa prática programar voltado para a interface. Repare como fica nossa
classe CarrinhoDeCompras:

♣✉❜❧✐❝ ❝❧❛ss ❈❛rr✐♥❤♦❉❡❈♦♠♣r❛s ④

      ♣r✐✈❛t❡ ❞♦✉❜❧❡ t♦t❛❧❀
      ♣r✐✈❛t❡ ▲✐st❁Pr♦❞✉t♦❃ ♣r♦❞✉t♦s❀

      ♣✉❜❧✐❝ ❈❛rr✐♥❤♦❉❡❈♦♠♣r❛s✭✮ ④
          t❤✐s✳♣r♦❞✉t♦s ❂ ♥❡✇ ❆rr❛②▲✐st❁Pr♦❞✉t♦❃✭✮❀
      ⑥

      ♣✉❜❧✐❝ ✈♦✐❞ ❛❞✐❝✐♦♥❛✭Pr♦❞✉t♦ ♣r♦❞✉t♦✮ ④
          t❤✐s✳♣r♦❞✉t♦s✳❛❞❞✭♣r♦❞✉t♦✮❀
      ⑥

      ♣✉❜❧✐❝ ✈♦✐❞ r❡♠♦✈❡✭✐♥t ♣♦s✐❝❛♦✮ ④
          t❤✐s✳♣r♦❞✉t♦s✳r❡♠♦✈❡✭♣♦s✐❝❛♦✮❀
      ⑥

      ♣✉❜❧✐❝ ❞♦✉❜❧❡ ❣❡t❚♦t❛❧✭✮ ④
          r❡t✉r♥ t♦t❛❧❀
      ⑥

      ♣✉❜❧✐❝ ▲✐st❁Pr♦❞✉t♦❃ ❣❡tPr♦❞✉t♦s✭✮ ④
          r❡t✉r♥ ♣r♦❞✉t♦s❀
      ⑥
⑥

    Note que, agora que o tipo ArrayList aparece apenas no momento
de instanciar a lista, em todos os demais pontos nos referimos a ela como
uma List<Produto>. Isso torna nosso código muito mais flexível para
mudanças. Para utilizar um LinkedList, bastaria mudar o tipo em que es-
tamos dando new sem causar nenhum efeito colateral indesejado ao restante
do código.
    A imagem a seguir mostra a interface List e algumas de suas implemen-
tações:

176


[PAGINA 187]
Casa do Código                                  Capítulo 11. Collection Framework




    Para finalizar nossa migração de array para List, precisamos corrigir
o erro de compilação da classe RegistroDeVendas, no momento em que
estamos iterando pelos itens do carrinho:

Pr♦❞✉t♦❬❪ ♣r♦❞✉t♦s ❂ ❝❛rr✐♥❤♦✳❣❡tPr♦❞✉t♦s✭✮❀

❢♦r ✭Pr♦❞✉t♦ ♣r♦❞✉t♦ ✿ ♣r♦❞✉t♦s✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭♣r♦❞✉t♦✮❀
⑥



                                                                             177


[PAGINA 188]
11.2. Ordenando nossa List de produtos                          Casa do Código


    A única mudança necessária será no tipo de retorno do método
getProdutos. Basta mudar de Produto[] para List<Produto> e todo
o restante continuará igual.

▲✐st❁Pr♦❞✉t♦❃ ♣r♦❞✉t♦s ❂ ❝❛rr✐♥❤♦✳❣❡tPr♦❞✉t♦s✭✮❀

❢♦r ✭Pr♦❞✉t♦ ♣r♦❞✉t♦ ✿ ♣r♦❞✉t♦s✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭♣r♦❞✉t♦✮❀
⑥

     Isso significa que o enhanced-for também funciona com qualquer
tipo de List (na verdade, com qualquer Iterable, como veremos mais
à frente).


11.2 Ordenando nossa List de produtos
Ao imprimir os valores dessa lista, você perceberá que serão exibidos na
mesma ordem em que foram inseridos. Mas é fato que, sempre que estamos
trabalhando com listas, entre outros tipos de coleções, é natural a necessidade
de exibir seus dados de forma ordenada seguindo algum outro critério.
    Até o Java 7, podíamos utilizar o método estático sort, presente na classe
java.util.Collections:

▲✐st❁❙tr✐♥❣❃ ♥♦♠❡s ❂ ♥❡✇ ❆rr❛②▲✐st❁❃✭✮❀
♥♦♠❡s✳❛❞❞✭✧❘♦❞r✐❣♦ ❚✉r✐♥✐✧✮❀
♥♦♠❡s✳❛❞❞✭✧❆❞r✐❛♥♦ ❆❧♠❡✐❞❛✧✮❀
♥♦♠❡s✳❛❞❞✭✧P❛✉❧♦ ❙✐❧✈❡✐r❛✧✮❀

❈♦❧❧❡❝t✐♦♥s✳s♦rt✭♥♦♠❡s✮❀

❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭♥♦♠❡s✮❀

      Executando esse código, o resultado será:

❬❆❞r✐❛♥♦ ❆❧♠❡✐❞❛✱ P❛✉❧♦ ❙✐❧✈❡✐r❛✱ ❘♦❞r✐❣♦ ❚✉r✐♥✐❪

    É importante perceber que o método sort efetivamente modificou a es-
trutura interna da lista, neste caso deixando-a em ordem alfabética.

178


[PAGINA 189]
Casa do Código                                     Capítulo 11. Collection Framework



    A classe Collections possui diversos outros métodos que podem ser
muito úteis quando você está trabalhando com coleções, principalmente com
Java 7 ou menor. Logo veremos que o Java 8 introduziu diversos recursos para
tornar seu trabalho com coleções ainda mais prático e funcional.
    Alguns outros exemplos de métodos da classe Collections são: o
reverse, para inverter a ordem dos elementos da lista; o copy, para copiar
os elementos de uma lista para outra; e também o emptyList, que retornará
uma lista vazia. Você pode ver os diversos métodos dessa classe em sua de-
talhada documentação:
    http://docs.oracle.com/javase/8/docs/api/java/util/Collections.html
    O sort em nossa List<Strings> utilizou como critério de ordenação
a ordem alfabética. Mas qual seria o resultado do seguinte código?

▲✐st❁Pr♦❞✉t♦❃ ♣r♦❞✉t♦s ❂ ♥❡✇ ❆rr❛②▲✐st❁❃✭✮❀

✴✴ ♣♦♣✉❧❛♥❞♦ ❛ ❧✐st❛ ❝♦♠ ❛❧❣✉♥s ♣r♦❞✉t♦s

❈♦❧❧❡❝t✐♦♥s✳s♦rt✭♣r♦❞✉t♦s✮❀

    Esse código não compila! Observe a saída:

❚❤❡ ♠❡t❤♦❞ s♦rt✭▲✐st❁❚❃✮ ✐♥ t❤❡ t②♣❡ ❈♦❧❧❡❝t✐♦♥s
✐s ♥♦t ❛♣♣❧✐❝❛❜❧❡ ❢♦r t❤❡ ❛r❣✉♠❡♥ts ✭▲✐st❁Pr♦❞✉t♦❃✮

    Faz sentido, afinal qual seria o critério de ordenação? Precisamos ensinar
ao método sort qual elemento deve vir antes de qual, ou seja, como ordenar
elementos do tipo Produto.
    O método sort precisa receber uma lista de elementos comparáveis,
que possuam um método específico ensinando-o como deve comparar tais
elementos. Para garantir que os elementos passados tenham esse método,
mais uma vez a API do Java fez uso de uma interface! Todo elemento or-
denável deve implementar a interface java.lang.Comparable, que pos-
sui o método compareTo.
    Para que nosso código compile, podemos dizer que todo Produto im-
plementa Comparable, mas repare no código a seguir:



                                                                               179


[PAGINA 190]
11.2. Ordenando nossa List de produtos                         Casa do Código


♣✉❜❧✐❝ ✐♥t❡r❢❛❝❡ Pr♦❞✉t♦ ❡①t❡♥❞s ❈♦♠♣❛r❛❜❧❡❁Pr♦❞✉t♦❃ ④

      ❞♦✉❜❧❡ ❣❡t❱❛❧♦r✭✮❀
⑥

    Pode parecer um pouco estranho na primeira vez que você olhar, afinal
estamos utilizando extends, e não o implements. Já percebeu por quê?
Como Produto é uma interface, ela apenas herdará as obrigações da inter-
face Comparable. Já as classes que a implementarem agora além da obri-
gação de escrever seu método getValor terão também que implementar
compareTo, o que logo veremos.
    Apenas um último detalhe antes de partirmos para a implementação do
método: você notou que o Comparable também faz uso do generics do Java
5? Se não tinha notado, dê uma boa olhada na assinatura da interface, que
tem um Comparable<Produto>. Com isso, eliminamos a necessidade de
fazer o casting de Object, que é o tipo do parâmetro de seu método int
compareTo(Object).
    Pronto, finalmente podemos partir para a implementação, que poderá
ser feita na classe abstrata Produto e, portanto, replicada a suas subclasses
LivroFisico, Ebook e MiniLivro. O critério de comparação será seu
valor:

♣✉❜❧✐❝ ❛❜str❛❝t ❝❧❛ss ▲✐✈r♦ ✐♠♣❧❡♠❡♥ts Pr♦❞✉t♦ ④

      ✴✴ ❝ó❞✐❣♦ ♦♠✐t✐❞♦

      ❅❖✈❡rr✐❞❡
      ♣✉❜❧✐❝ ✐♥t ❝♦♠♣❛r❡❚♦✭Pr♦❞✉t♦ ♦✉tr♦✮ ④

            ✐❢ ✭t❤✐s✳❣❡t❱❛❧♦r✭✮ ❁ ♦✉tr♦✳❣❡t❱❛❧♦r✭✮✮④
                r❡t✉r♥ ✲✶❀
            ⑥
            ✐❢ ✭t❤✐s✳❣❡t❱❛❧♦r✭✮ ❃ ♦✉tr♦✳❣❡t❱❛❧♦r✭✮✮④
                r❡t✉r♥ ✶❀
            ⑥
            r❡t✉r♥ ✵❀
      ⑥
⑥

180


[PAGINA 191]
Casa do Código                                  Capítulo 11. Collection Framework



    O mesmo pode ser feito na classe Revista, que não é filha de Livro
mas também é um Produto que deve ser ordenado por valor. O código
pareceu confuso? Não se preocupe, vamos entendê-lo um pouco melhor.
    Note que o método compareTo retorna um int. Devemos retornar
0 (zero) se o objeto comparado (parâmetro outro) for igual a este objeto (
this), um número negativo se este objeto for menor (deva vir antes quando
ordenado) que o objeto passado, ou um número positivo caso seja maior
(deva vir depois).
    Execute o seguinte código para ver o resultado em prática:
♣✉❜❧✐❝ ❝❧❛ss ❖r❞❡♥❛♥❞♦❈♦♠❏❛✈❛ ④

       ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④

           ❆✉t♦r ❛✉t♦r ❂ ♥❡✇ ❆✉t♦r✭✮❀
           ❛✉t♦r✳s❡t◆♦♠❡✭✧❘♦❞r✐❣♦ ❚✉r✐♥✐✧✮❀

           ▲✐✈r♦❋✐s✐❝♦ ❢✐s✐❝♦ ❂ ♥❡✇ ▲✐✈r♦❋✐s✐❝♦✭❛✉t♦r✮❀
           ❢✐s✐❝♦✳s❡t◆♦♠❡✭✧❏❛✈❛ ✽ Prát✐❝♦✧✮❀
           ❢✐s✐❝♦✳s❡t❱❛❧♦r✭✺✾✳✾✵✮❀

           ❊❜♦♦❦ ❡❜♦♦❦ ❂ ♥❡✇ ❊❜♦♦❦✭❛✉t♦r✮❀
           ❡❜♦♦❦✳s❡t◆♦♠❡✭✧❏❛✈❛ ✽ Prát✐❝♦✧✮❀
           ❡❜♦♦❦✳s❡t❱❛❧♦r✭✷✾✳✾✵✮❀

           ▲✐st❁Pr♦❞✉t♦❃ ♣r♦❞✉t♦s ❂ ❆rr❛②s✳❛s▲✐st✭❢✐s✐❝♦✱ ❡❜♦♦❦✮❀

           ❈♦❧❧❡❝t✐♦♥s✳s♦rt✭♣r♦❞✉t♦s✮❀

           ❢♦r ✭Pr♦❞✉t♦ ♣r♦❞✉t♦ ✿ ♣r♦❞✉t♦s✮ ④
               ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭♣r♦❞✉t♦✳❣❡t❱❛❧♦r✭✮✮❀
           ⑥
       ⑥
⑥

    A saída será:
✷✾✳✾
✺✾✳✾

                                                                             181


[PAGINA 192]
11.3. Gerenciando cupons de desconto                        Casa do Código




  Outras implementações

     Como estamos comparando apenas o valor do             Produto,
  poderíamos simplificar nossa implementação retornando apenas a
  subtração de um valor pelo outro. Repare como nosso código fica mais
  simples:

  ♣✉❜❧✐❝ ❛❜str❛❝t ❝❧❛ss ▲✐✈r♦ ✐♠♣❧❡♠❡♥ts Pr♦❞✉t♦ ④

         ✴✴ ❝ó❞✐❣♦ ♦♠✐t✐❞♦

         ❅❖✈❡rr✐❞❡
         ♣✉❜❧✐❝ ✐♥t ❝♦♠♣❛r❡❚♦✭Pr♦❞✉t♦ ♦✉tr♦✮ ④
             r❡t✉r♥ t❤✐s✳❣❡t❱❛❧♦r✭✮ ✲ ♦✉tr♦✳❣❡t❱❛❧♦r✭✮❀
         ⑥
  ⑥

      Mais simples, não acha? Alternativamente, também poderíamos uti-
  lizar o método Integer.compare passando os dois valores como
  parâmetro. Experimente utilizar alguma dessas estratégias para deixar
  seu código mais simples, essa é uma prática bastante comum.


11.3 Gerenciando cupons de desconto
Agora que nossa classe CarrinhoDeCompras já está bem resolvida, pode-
mos seguir para uma outra necessidade de nosso projeto. Precisamos agora
gerenciar cupons de desconto promocionais.
    Como      ponto    de    partida,    podemos      criar    a   classe
GerenciadorDeCupons que possui internamente uma lista com al-
guns cupons já cadastrados. Repare:

♣✉❜❧✐❝ ❝❧❛ss ●❡r❡♥❝✐❛❞♦r❉❡❈✉♣♦♥s ④

      ♣r✐✈❛t❡ ▲✐st❁❙tr✐♥❣❃ ❝✉♣♦♥s❀

      ♣✉❜❧✐❝ ●❡r❡♥❝✐❛❞♦r❉❡❈✉♣♦♥s✭✮ ④


182


[PAGINA 193]
Casa do Código                                  Capítulo 11. Collection Framework



           t❤✐s✳❝✉♣♦♥s ❂ ❆rr❛②s✳❛s▲✐st✭✧❈❯P✼✹✧✱ ✧❈❯P✶✺✽✧✱
               ✧❈❯P✶✹✧✱ ✧❈❯P✺✷✧✱ ✧❈❯P✷✶✧✱ ✧❈❯P✷✷✶✧✱ ✧❈❯P✾✶✧✱
               ✧❈❯P✸✷✼✧✱ ✧❈❯P✹✶✵✧✱ ✧❈❯P✷✼✺✧✱ ✧❈❯P✹✽✹✧✱ ✧❈❯P✷✵✼✧✱
               ✧❈❯P✾✻✧✱ ✧❈❯P✶✶✾✧✱ ✧❈❯P✶✼✹✧✱ ✧❈❯P✷✾✶✧✱ ✧❈❯P✶✧✱
               ✧❈❯P✶✶✺✧✱ ✧❈❯P✷✷✷✧✱ ✧❈❯P✷✼✷✧✮❀
     ⑥
⑥

    Note    que   setamos o método estático         asList da classe
java.util.Arrays para criar nossa lista.          Poderíamos criar um
ArrayList e chamar seu método add para cada elemento, mas é co-
mum utilizar esse novo método para simplificar esse processo. O método
asList é uma fábrica (factory) de List e, com certeza, será muito útil em
seu dia a dia.
    Nosso próximo passo será criar um método para validar os cupons passa-
dos pelo cliente. Ele retornará um boolean indicando se o cupom passado
está ou não presente em nossa List<String> cupons. Vamos chamá-lo
de validaCupom:

♣✉❜❧✐❝ ❜♦♦❧❡❛♥ ✈❛❧✐❞❛❈✉♣♦♠✭❙tr✐♥❣ ❝✉♣♦♠✮ ④
    r❡t✉r♥ t❤✐s✳❝✉♣♦♥s✳❝♦♥t❛✐♥s✭❝✉♣♦♠✮❀
⑥

   Note que utilizamos o já conhecido método contains para fazer essa
consulta. Bem simples, não acha?
   Já estamos prontos para testar esse código. Vamos criar uma nova classe
chamada ConsultaDeDescontos, que deve utilizar esse novo método, o
validaCupom. Repare:

♣✉❜❧✐❝ ❝❧❛ss ❈♦♥s✉❧t❛❉❡❉❡s❝♦♥t♦s ④

     ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④

           ●❡r❡♥❝✐❛❞♦r❉❡❈✉♣♦♥s ❣❡r❡♥❝✐❛❞♦r ❂
               ♥❡✇ ●❡r❡♥❝✐❛❞♦r❉❡❈✉♣♦♥s✭✮❀

           ✐❢✭❣❡r❡♥❝✐❛❞♦r✳✈❛❧✐❞❛❈✉♣♦♠✭✧❈❯P✶✷✸✹✧✮✮④
               ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❈✉♣♦♠ ❞❡ ❞❡s❝♦♥t♦ ✈❛❧✐❞♦✳✧✮❀

                                                                             183


[PAGINA 194]
11.3. Gerenciando cupons de desconto                         Casa do Código


                ✴✴ ❛♣❧✐❝❛ ♦ ❞❡s❝♦♥t♦ ❞❡ss❡ ❝✉♣♦♠
            ⑥ ❡❧s❡ ④
                ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✧❊ss❡ ❝✉♣♦♠ ♥ã♦ ❡①✐st❡✳✧✮❀
            ⑥
      ⑥
⑥

   Rode esse código para ver o resultado. Como o cupom não existe em
nossa lista, a saída será:

❊ss❡ ❝✉♣♦♠ ♥ã♦ ❡①✐st❡✳

     Trabalhar com uma List aqui resolve o problema, mas ela não é a es-
trutura ideal para fazer esse trabalho. Normalmente, trabalhamos com uma
lista quando seus elementos internos podem repetir e sua ordem tem alguma
importância, mas note que não é esse o caso de nossos cupons. Um cupom
é único, não há repetições e, além disso, a ordem deles não importa, afinal
estamos utilizando esses dados apenas para consulta.
     Em casos como este, podemos utilizar uma outra estrutura de dados bas-
tante interessante, um conjunto ( java.util.Set).

java.util.Set

    Um conjunto (ou Set em Java) funciona de forma parecida com os con-
juntos da matemática. Ela é uma coleção, assim como a List, mas em que
não há repetição de seus dados internos. Além disso, sua ordem não é nec-
essariamente a ordem em que os valores foram inseridos, isso pode variar
bastante de cada implementação.
    Assim como a List, o Set é apenas uma interface. Para utilizar um Set,
precisamos instanciar alguma de suas implementações, como a HashSet,
que é uma das implementações mais usadas. Observe como fica nosso código
da classe GerenciadorDeCupons:

♣✉❜❧✐❝ ❝❧❛ss ●❡r❡♥❝✐❛❞♦r❉❡❈✉♣♦♥s ④

      ♣r✐✈❛t❡ ❙❡t❁❙tr✐♥❣❃ ❝✉♣♦♥s❀

      ♣✉❜❧✐❝ ●❡r❡♥❝✐❛❞♦r❉❡❈✉♣♦♥s✭✮ ④

184


[PAGINA 195]
Casa do Código                                    Capítulo 11. Collection Framework



          t❤✐s✳❝✉♣♦♥s ❂ ♥❡✇ ❍❛s❤❙❡t❁❙tr✐♥❣❃✭✮❀

          ❝✉♣♦♥s✳❛❞❞❆❧❧✭❆rr❛②s✳❛s▲✐st✭✧❈❯P✼✹✧✱ ✧❈❯P✶✺✽✧✱
              ✧❈❯P✶✹✧✱ ✧❈❯P✺✷✧✱ ✧❈❯P✷✶✧✱ ✧❈❯P✷✷✶✧✱ ✧❈❯P✾✶✧✱
              ✧❈❯P✸✷✼✧✱ ✧❈❯P✹✶✵✧✱ ✧❈❯P✷✼✺✧✱ ✧❈❯P✹✽✹✧✱ ✧❈❯P✷✵✼✧✱
              ✧❈❯P✾✻✧✱ ✧❈❯P✶✶✾✧✱ ✧❈❯P✶✼✹✧✱ ✧❈❯P✷✾✶✧✱ ✧❈❯P✶✧✱
              ✧❈❯P✶✶✺✧✱ ✧❈❯P✷✷✷✧✱ ✧❈❯P✷✼✷✧✮✮❀
     ⑥

     ♣✉❜❧✐❝ ❜♦♦❧❡❛♥ ✈❛❧✐❞❛❈✉♣♦♠✭❙tr✐♥❣ ❝✉♣♦♠✮ ④
         r❡t✉r♥ t❤✐s✳❝✉♣♦♥s✳❝♦♥t❛✐♥s✭❝✉♣♦♠✮❀
     ⑥
⑥

    Note que utilizamos o método addAll para facilitar essa mudança. Mas
é natural adicionar elementos no Set chamando seu método add, assim
como na List. Outro detalhe importante é que continuamos programando
voltados para a interface, isto é, apesar de dar new em HasSet, o tipo do
atributo cupons é um Set. Essa é e sempre será uma excelente prática, posto
que diminui o acoplamento de nossa classe e facilita evoluções no futuro.
    Nosso código continua funcionando assim como antes. Rode a classe
ConsultaDeDescontos para confirmar! Aparentemente, tudo está igual,
mas na verdade algumas coisas mudaram.
    O primeiro ponto importante a se perceber é que, mesmo que você adi-
cione mais 500 mil cupons iguais nesse conjunto, ao mandar imprimir o seu
tamanho ( size) ele ainda será 20. Você pode rodar o código a seguir para
confirmar isso:

❍❛s❤❙❡t❁❙tr✐♥❣❃ s❡t ❂ ♥❡✇ ❍❛s❤❙❡t❁❙tr✐♥❣❃✭✮❀
s❡t✳❛❞❞✭✧◆ã♦ ❤á r❡♣❡t✐❝ã♦ ❡♠ ❈♦♥❥✉♥t♦s✧✮❀
s❡t✳❛❞❞✭✧◆ã♦ ❤á r❡♣❡t✐❝ã♦ ❡♠ ❈♦♥❥✉♥t♦s✧✮❀
s❡t✳❛❞❞✭✧◆ã♦ ❤á r❡♣❡t✐❝ã♦ ❡♠ ❈♦♥❥✉♥t♦s✧✮❀
s❡t✳❛❞❞✭✧◆ã♦ ❤á r❡♣❡t✐❝ã♦ ❡♠ ❈♦♥❥✉♥t♦s✧✮❀
s❡t✳❛❞❞✭✧◆ã♦ ❤á r❡♣❡t✐❝ã♦ ❡♠ ❈♦♥❥✉♥t♦s✧✮❀
❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭s❡t✳s✐③❡✭✮✮❀

    Qual foi o valor da saída? Exatamente 1, ele ignorou as repetições. Para
ajudar a saber quando você está inserindo uma repetição em um Set, seu

                                                                               185


[PAGINA 196]


[PAGINA 197]


[PAGINA 198]
11.4. java.util.Map                                          Casa do Código




11.4 java.util.Map
Nosso GerenciadorDeCupons já está quase completo. O próximo passo
será aplicar o desconto específico para determinado cupom que foi validado.
Mas como vincular um cupom único com o seu valor de desconto?
    Essa é uma necessidade muito comum: vincular um objeto a uma chave
única, para conseguir buscar esse valor rapidamente. Poderíamos resolver
isso com uma lista, mas já vimos que essa não é a melhor estrutura quando
queremos fazer buscas.

188


[PAGINA 199]


[PAGINA 200]


[PAGINA 201]


[PAGINA 202]


[PAGINA 203]
Capítulo 12

Streams e novidades do Java 8
A API de Collections é bastante robusta, sem dúvidas. Há muito o que explo-
rar em suas diversas estruturas e soluções. Mas o fato é que estamos falando
de uma API gigante e com mais de 15 anos, que com certeza possui algumas
limitações e características que não poderiam ser evoluidas sem que houvesse
uma sobrecarga ou ainda quebra de compatibilidade (veremos no próximo
capítulo o quanto isso é importante para o Java).
    Por esse e diversos outros motivos o Java 8 introduziu diversas novidades
que nos trazem uma forma bem mais interessante e funcional de trabalhar
com nossas coleções. Veremos algumas dessas novidades durante o capítulo.


12.1 Ordenando com Java 8
Vimos que uma maneira de ordenar a List<Produto> era tornando seus el-
ementos comparávis, para isso implementando java.lang.Comparable.


[PAGINA 204]
12.1. Ordenando com Java 8                                  Casa do Código


Mas e se você tiver mais de um critério de ordenação? E se você quiser em
alguns momentos comparar um Livro pelo seu valor e em outros pelo seu
nome?
    Até o Java 7 uma forma de fazer isso seria criando uma nova classe, um
comparador de Livro por nome. Essa classe precisava implementar a inter-
face java.util.Comparator, algo como:

♣✉❜❧✐❝ ❝❧❛ss ❈♦♠♣❛r❛❞♦rP♦r◆♦♠❡ ✐♠♣❧❡♠❡♥ts ❈♦♠♣❛r❛t♦r❁▲✐✈r♦❃④

      ❅❖✈❡rr✐❞❡
      ♣✉❜❧✐❝ ✐♥t ❝♦♠♣❛r❡✭▲✐✈r♦ ❧✶✱ ▲✐✈r♦ ❧✷✮ ④
          r❡t✉r♥ ❧✶✳❣❡t◆♦♠❡✭✮✳❝♦♠♣❛r❡❚♦✭❧✷✳❣❡t◆♦♠❡✭✮✮❀
      ⑥
⑥

   O método sort da Collection tem uma sobrecarga que recebe um
Comparator como parâmetro, portanto agora basta fazer:

❈♦❧❧❡❝t✐♦♥s✳s♦rt✭❧✐✈r♦s✱ ♥❡✇ ❈♦♠♣❛r❛❞♦rP♦r◆♦♠❡✭✮✮❀

    Vamos ver esse código na prática! Crie a classe NovidadesDoJava8 e
adicione o seguinte código para testar:

♣✉❜❧✐❝ ❝❧❛ss ◆♦✈✐❞❛❞❡s❉♦❏❛✈❛✽ ④

      ♣✉❜❧✐❝ st❛t✐❝ ✈♦✐❞ ♠❛✐♥✭❙tr✐♥❣❬❪ ❛r❣s✮ ④

            ❆✉t♦r ❛✉t♦r ❂ ♥❡✇ ❆✉t♦r✭✮❀
            ❛✉t♦r✳s❡t◆♦♠❡✭✧❘♦❞r✐❣♦ ❚✉r✐♥✐✧✮❀

            ▲✐✈r♦ ❥❛✈❛♦♦ ❂ ♥❡✇ ▲✐✈r♦❋✐s✐❝♦✭❛✉t♦r✮❀
            ❥❛✈❛♦♦✳s❡t◆♦♠❡✭✧❏❛✈❛ ❖✳❖✳✧✮❀

            ▲✐✈r♦ ❥❛✈❛✽ ❂ ♥❡✇ ▲✐✈r♦❋✐s✐❝♦✭❛✉t♦r✮❀
            ❥❛✈❛✽✳s❡t◆♦♠❡✭✧❏❛✈❛ ✽ Prát✐❝♦✧✮❀

            ▲✐✈r♦ r✉❜② ❂ ♥❡✇ ▲✐✈r♦❋✐s✐❝♦✭❛✉t♦r✮❀
            r✉❜②✳s❡t◆♦♠❡✭✧▲✐✈r♦ ❞❡ ❘✉❜②✧✮❀


194


[PAGINA 205]
Casa do Código                                Capítulo 12. Streams e novidades do Java 8



          ▲✐st❁▲✐✈r♦❃ ❧✐✈r♦s ❂ ❆rr❛②s✳❛s▲✐st✭❥❛✈❛♦♦✱ ❥❛✈❛✽✮❀

          ❈♦❧❧❡❝t✐♦♥s✳s♦rt✭❧✐✈r♦s✱ ♥❡✇ ❈♦♠♣❛r❛❞♦rP♦r◆♦♠❡✭✮✮❀

          ❢♦r ✭▲✐✈r♦ ❧✐✈r♦ ✿ ❧✐✈r♦s✮ ④
              ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❧✐✈r♦✳❣❡t◆♦♠❡✭✮✮❀
          ⑥
     ⑥
⑥

    Agora execute o código e repare que a saída será:

❏❛✈❛ ✽ Prát✐❝♦
❏❛✈❛ ❖✳❖✳
▲✐✈r♦ ❞❡ ❘✉❜②

Classes anônimas e o lambda
     O que pode incomodar bastante dessa solução é que para cada
novo critério de ordenação, precisaríamos criar uma nova classe como a
ComparadorPorNome. Ainda que seu código seja bem pequeno e não seja
reutilizado em nenhum outro lugar.
     Uma alternativa bastante utilizada até o Java 7 eram as conhecidas classes
anônimas. Você pode sim dar new em uma interface, mas terá que implemen-
tar seus métodos ali mesmo, numa mesma instrução. Podemos fazer isso com
a interface Comparator, no lugar de criar a classe ComparadorPorNome,
podemos fazer:

❈♦❧❧❡❝t✐♦♥s✳s♦rt✭❧✐✈r♦s✱ ♥❡✇ ❈♦♠♣❛r❛t♦r❁▲✐✈r♦❃✭✮ ④
    ❅❖✈❡rr✐❞❡
    ♣✉❜❧✐❝ ✐♥t ❝♦♠♣❛r❡✭▲✐✈r♦ ❧✶✱ ▲✐✈r♦ ❧✷✮ ④
        r❡t✉r♥ ❧✶✳❣❡t◆♦♠❡✭✮✳❝♦♠♣❛r❡❚♦✭❧✷✳❣❡t◆♦♠❡✭✮✮❀
    ⑥
⑥✮❀

    Isso mesmo, é o mesmo código da classe ComparadorPorNome, mas
declarado numa única instrução. Esse recurso é conhecido como classe anôn-
ima, pois afinal essa classe não tem nem mesmo um nome! Achou a sintaxe


                                                                                   195


[PAGINA 206]
12.1. Ordenando com Java 8                                      Casa do Código


estranha? Feia? difícil de ler? Bem... eu concordo! Isso polui bastante o nosso
código.
    Para simplificar esse processo o Java 8 introduziu algumas mudanças, uma
delas foi adicionando o método sort na própria interface List! Pode pare-
cer uma mudança simples, mas agora podemos fazer:

❧✐✈r♦s✳s♦rt✭♥❡✇ ❈♦♠♣❛r❛t♦r❁▲✐✈r♦❃✭✮ ④
    ❅❖✈❡rr✐❞❡
    ♣✉❜❧✐❝ ✐♥t ❝♦♠♣❛r❡✭▲✐✈r♦ ❧✶✱ ▲✐✈r♦ ❧✷✮ ④
        r❡t✉r♥ ❧✶✳❣❡t◆♦♠❡✭✮✳❝♦♠♣❛r❡❚♦✭❧✷✳❣❡t◆♦♠❡✭✮✮❀
    ⑥
⑥✮❀

    Para não quebrar a compatibilidade da interface List, esse método
sort é um método concreto, com código dentro! Lembra do nome desse re-
curso? No capitulo de interface brevemente comentei sobre os tais default
methods, heis um bom exemplo:

❞❡❢❛✉❧t ✈♦✐❞ s♦rt✭❈♦♠♣❛r❛t♦r❁❄ s✉♣❡r ❊❃ ❝✮ ④
    ❈♦❧❧❡❝t✐♦♥s✳s♦rt✭t❤✐s✱ ❝✮❀
⑥

    Isso mesmo, esse método defalt da List apenas delega a chamada
para o método sort de Collections, que já fazia bem este trabalho. Mas
isso ainda não resolve todos os problemas de ordenação, não é? Então vamos
para outra novidade.
    Também no capitulo de interfaces, vimos brevemente que o Java 8 intro-
duziu o conceito de interfaces funcionais. Em poucas palavras, uma inter-
face com um único método abstrato pode ser considerada funcional, como
é o caso da interface Comparator que possui apenas o método compare.
Com isso ganhamos algumas possibilidades, como por exemplo transformar
aquela classe anônima em uma expressão lambda! Uma primeira forma de
fazer isso seria:

❧✐✈r♦s✳s♦rt✭✭▲✐✈r♦ ❧✶✱ ▲✐✈r♦ ❧✷✮ ✲❃ ④
    r❡t✉r♥ ❧✶✳❣❡t◆♦♠❡✭✮✳❝♦♠♣❛r❡❚♦✭❧✷✳❣❡t◆♦♠❡✭✮✮❀
⑥✮❀


196


[PAGINA 207]
Casa do Código                             Capítulo 12. Streams e novidades do Java 8



    Note que a diferença desse código para a classe anônima é que deixamos
apenas os parâmetros do método compare, seguidos do operador -> e sua
implementação. Como o método sort espera receber um Comparator, o
compilador já infere que esse é o tipo da expressão lambda.
    Podemos simplificar ainda mais esse código, retirando o tipo Livro dos
parêmetros, as chaves, o return e até mesmo o ponto-e-virgula. Repare:
❧✐✈r♦s✳s♦rt✭
    ✭❧✶✱ ❧✷✮ ✲❃ ❧✶✳❣❡t◆♦♠❡✭✮✳❝♦♠♣❛r❡❚♦✭❧✷✳❣❡t◆♦♠❡✭✮✮
✮❀

    Esse é um conceito um pouco mais avançado e com certeza
pode parecer bastante estranho ou mesmo assustador no ínicio. O
código (l1, l2) -> l1.getNome().compareTo(l2.getNome())
resulta em uma instância de                  Comparator que devolve
l1.getNome().compareTo(l2.getNome().                 Não há necessidade
de declarar o tipo ( Livro) dos parâmteros, o próprio compilador sabe
inferir isso pra você. Não há necessidade da palavra return e nem mesmo
de chaves, já que temos uma única instrução após o operador ->.
    Para tornar o código ainda mais enxuto e um pouco mais fluente, o
método default comparing foi adicionado na interface Comparator. Ele é
uma fábrica ( factory) de Comparator, tudo que precisamos fazer é passar
uma expressão lambda com o critério de comparação como a seguir:
❧✐✈r♦s✳s♦rt✭❝♦♠♣❛r✐♥❣✭❧ ✲❃ ❧✳❣❡t◆♦♠❡✭✮✮✮❀

    Note que como há apenas um parâmetro nesse lambda, não precisamos
passá-lo dentro de parênteses. Rode o código para ver o resultado! O que
acha?

Simplificando ainda mais com method reference
    A expressão lambda l -> l.getNome() apenas diz ao comparing
qual o método que deverá ser utilizado em sua comparação. Ele está ape-
nas referenciando um método, neste caso o getNome. Em casos como este
podemos ainda fazer:
❧✐✈r♦s✳s♦rt✭❝♦♠♣❛r✐♥❣✭▲✐✈r♦✿✿❣❡t◆♦♠❡✮✮❀

                                                                                197


[PAGINA 208]
12.2. forEach do Java 8                                       Casa do Código


    Esse é um outro recurso do Java 8, conhecido como method
reference. Note que sua sintaxe é o nome da classe seguido de :>: e o
nome do método. Esse recurso pode ser utilizado sempre que temos uma ex-
pressão lambda como a l -> l.getNome(), que apenas delega a chamada
de um método.


12.2       forEach do Java 8
Outro default method que com total certeza fará parte de seu dia a dia é
o forEach, presente na interface Iterable. Note na forma como estamos
iterando pela lista de livros utilizando o enhanced-for:
❢♦r ✭▲✐✈r♦ ❧✐✈r♦ ✿ ❧✐✈r♦s✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❧✐✈r♦✳❣❡t◆♦♠❡✭✮✮❀
⑥

      No Java 8 agora podemos fazer:
❧✐✈r♦s✳❢♦r❊❛❝❤✭❧ ✲❃ ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❧✳❣❡t◆♦♠❡✭✮✮✮❀

    O método forEach, assim como a maior parte dos default methods,
recebe uma interface funcional como parâmetro. Portanto note que foi pos-
sivel utilizar uma expressão lambda para representar nossas intenções.
    O lambda l -> System.out.println(l.getNome()) nada mas
diz do que: “para cada livro, chame o método println imprimindo seu nome”.


12.3       Filtrando livros pelo autor
Além da forma de ordenar e iterar, o Java 8 mudou bastante a forma de fazer
algumas operações rotineiras de quando estamos trabalhando com coleções.
Quer um exemplo prático?

O trabalho de filtrar uma Collection
    Dada uma lista de livros, queremos filtar apenas os que tenham a palavra
Java em seu nome. Até o Java 1.7 uma das formas mais tradicionais de se
fazer isso seria criando uma nova lista para o resultado e condicionando os
elementos que deveriam ser inseridos, como a seguir:

198


[PAGINA 209]
Casa do Código                              Capítulo 12. Streams e novidades do Java 8



▲✐st❁▲✐✈r♦❃ ❢✐❧tr❛❞♦s ❂ ♥❡✇ ❆rr❛②▲✐st❁❃✭✮❀

❢♦r ✭▲✐✈r♦ ❧✐✈r♦ ✿ ❧✐✈r♦s✮ ④
    ✐❢ ✭❧✐✈r♦✳❣❡t◆♦♠❡✭✮✳❝♦♥t❛✐♥s✭✧❏❛✈❛✧✮✮ ④
        ❢✐❧tr❛❞♦s✳❛❞❞✭❧✐✈r♦✮❀
    ⑥
⑥

    Para testar, adicione esse código na classe NovidadesDoJava8 e logo
depois mostre os resultados dessa lista, fazendo um simples for como a
seguir:

❢♦r ✭▲✐✈r♦ ❧✐✈r♦ ✿ ❢✐❧tr❛❞♦s✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❧✐✈r♦✳❣❡t◆♦♠❡✭✮✮❀
⑥

    Note que a saída será:

❏❛✈❛ ✽ Prát✐❝♦
❏❛✈❛ ❖✳❖✳

    Excelente, resolvemos o problema! Mas de uma boa olhada em seu
código... o que achou? Note que além de ser muito verboso, ele exigiu a cri-
ação de uma lista intermediária para o resultado. Esse é sem dúvidas um
código bastante imperativo.
    Operações comuns como essa, filtrar elementos de uma coleção, estão
agora presentes em uma nova API, conhecida como Stream. O Stream traz
para o Java uma forma mais funcional de trabalhar com as nossas coleções,
usando uma interface fluente! Separando as funcionalidades do Stream
da Collection, também ficou mais fácil de deixar claro que métodos são
mutáveis, evitar problema de conflito de nome de métodos, entre outros.

Stream e o filter
    Como criar um Stream? Isso é bem simples, um novo método default
chamado stream foi definido na interface Collection. Com isso, basta
fazer:

❙tr❡❛♠❁▲✐✈r♦❃ str❡❛♠ ❂ ❧✐✈r♦s✳str❡❛♠✭✮❀

                                                                                 199


[PAGINA 210]
12.3. Filtrando livros pelo autor                              Casa do Código


   A partir desse nosso Stream<Livro> conseguimos utilizar por exemplo
o método filter, como a seguir:

❧✐✈r♦s✳str❡❛♠✭✮✳❢✐❧t❡r✭❧ ✲❃ ❧✳❣❡t◆♦♠❡✭✮✳❝♦♥t❛✐♥s✭✧❏❛✈❛✧✮✮❀

    Estamos fazendo a mesma coisa que aquele for com um if dentro do
Java 7, só que agora de uma forma muito mais declarativa!
    Não deixe de testar, mude o código da classe NovidadesDoJava8 e es-
creva o seguinte for para exibir a lista de livros:

❢♦r ✭▲✐✈r♦ ❧✐✈r♦ ✿ ❧✐✈r♦s✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❧✐✈r♦✳❣❡t◆♦♠❡✭✮✮❀
⑥

      Rode o código e o resultado será:

❏❛✈❛ ✽ Prát✐❝♦
❏❛✈❛ ❖✳❖✳
▲✐✈r♦ ❞❡ ❘✉❜②

   Ops, esse Livro de Ruby não deveria estar no resultado! O filtro não
funcionou? Na verdade funcionou, mas a API de Streams é imutável, isso é,
não altera sua coleção inicial. Você pode fazer quantas transformações quiser
sem se preocupar com efeitos colaterais em sua lista.
   Portanto, no lugar de iterar na lista original podemos utilizar o método
forEach também presente na API de Streams da seguinte forma:

❧✐✈r♦s✳str❡❛♠✭✮
    ✳❢✐❧t❡r✭❧ ✲❃ ❧✳❣❡t◆♦♠❡✭✮✳❝♦♥t❛✐♥s✭✧❏❛✈❛✧✮✮
    ✳❢♦r❊❛❝❤✭❧ ✲❃ ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭❧✳❣❡t◆♦♠❡✭✮✮✮❀

      Agora sim, ao executar o código teremos apenas os elementos filtrados:

❏❛✈❛ ✽ Prát✐❝♦
❏❛✈❛ ❖✳❖✳

   Claro, o filter é apenas um dos zilhares métodos presentes nessa nova
API. Você pode ver a lista completa em e alguns exemplos em:
   http://docs.oracle.com/javase/8/docs/api/java/util/stream/Stream.html

200


[PAGINA 211]
Casa do Código                              Capítulo 12. Streams e novidades do Java 8



   Vimos nesse capitulo apenas um pouco do muito que o Java 8 introduziu
com seus novos recursos e APIs. O seguinte post do blog da caelum fala um
pouco mais sobre essas novidades:
   http://blog.caelum.com.br/o-minimo-que-voce-deve-saber-de-java-8/


  O livro Java 8 Prático

      Junto com Paulo Silveira escrevi o livro Java 8 Prático: Lambdas,
  Streams e os novos recursos da linguagem, que entra a fundo em cada de-
  talhe e sumariza os novos recursos do Java. Se você gostou das novidades
  com certeza vai gostar de seu conteúdo:
      http://www.casadocodigo.com.br/products/livro-java8




                                                                                 201


[PAGINA 212]


[PAGINA 213]
Capítulo 13

Um pouco da história do Java
13.1 Origem da linguagem
Já colocamos em prática muitos dos conceitos da orientação a objetos e re-
cursos específicos da linguagem Java, mas para concluir essa primeira parte
do estudo é fundamental conhecermos um pouco de sua história.
    Acredito que quando foi iniciado o Green Team, um projeto da Sun Mi-
crosystems cujo objetivo era criar uma plataforma de computação interativa,
ninguém imaginou que esse seria o início de uma linguagem que mudou o
rumo da história da programação e que atualmente possui mais de 9 milhões
de desenvolvedores. Em 1992 foi feita a primeira demonstração desse projeto,
mas apenas em 1995 que foi anunciado o lançamento oficial da plataforma
Java.
    Na época o uso principal da linguagem era focado em navegadores web


[PAGINA 214]
13.2. Escreva uma vez, rode em qualquer lugar!                  Casa do Código


para rodar pequenas aplicações (os tão conhecidos applets), tanto que foi in-
serida no Netscape Navigator que era o principal navegador do momento.
     Desde então a grande idéia da linguagem é você escrever uma aplicação e
executá-la nos diferentes dispositivos existentes. Ou seja, portabilidade é uma
das características mais fortes e presente desde suas origens. Claro que essa
não é a única característica forte da linguagem, que também é robusta, par-
alelizável, segura e dentre diversas outras que ainda serão melhor detalhadas:
estável.
     Algumas das características que tornam o Java muito bem vindo como
linguagem são sua estabilidade e retrocompatibilidade. Você pode reparar
isso pela numeração de suas versões, repare que apesar da estratégia de mar-
keting de chamá-lo de Java 8, por exemplo, a versão continua sendo 1.8. Ou
seja, o 1 sempre está presente indicando que ainda não houve uma quebra de
compatibilidade desde seu lançamento.
     Podemos então em 2014, com a versão mais recente da linguagem, com-
pilar e executar uma aplicação escrita por volta de 1995 com Java 1.0.2 sem
nenhuma dificuldade. Isso nos dá uma boa segurança de que uma atualiza-
ção de versão não será um problema, por exemplo.
     Há uma comunidade conhecida como JCP (Java Community Process)
cujo objetivo é garantir esse padrão de estabilidade e compatibilidade multi-
plataforma da tecnologia Java. Você pode ler mais sobre a JCP e suas pro-
postas em:
     https://www.jcp.org/en/introduction/overview


13.2       Escreva uma vez, rode em qualquer lugar!
Diferente das demais linguagens, uma aplicação Java pode ser executada em
qualquer um dos diferentes sistemas operacionais existentes, como por exem-
plo Windows, Linux ou Mac OS. Essa possibilidade abre muitos caminhos e
foi um dos principais fatores que tornaram a linguagem tão atraente pro mer-
cado. Exibindo esse benefício, o Java teve como slogan oficial o termo Write
once, run anywhere (escreva uma vez, rode em qualquer lugar).
     A grande chave para essa portabilidade é a máquina virtual, ou JVM (Java
Virtual Machine). No lugar de instruções nativas para um determinado hard-

204


[PAGINA 215]
Casa do Código                               Capítulo 13. Um pouco da história do Java



ware, após compilado um código-fonte em Java é traduzido para um formato
conhecido como bytecode. Esse bytecode independe da arquitetura do sistema
em que foi gerado e portanto poderá ser executado em qualquer plataforma,
contanto que ela tenha uma JVM instalada. A imagem a seguir representa
esse processo:




    Inicialmente o desempenho da linguagem foi um fator preocupante,
tendo como parâmetro de comparação as demais linguagens compiladas em
instruções nativas para uma determinada plataforma. Ao ganhar em porta-
bilidade a linguagem sofreu um grande impacto por adicionar essa camada
intermediária. Em pouco tempo o desempenho deixou de ser um problema,
com introduções e tecnologias que serão melhor detalhadas a seguir nas de-
scrições das diferentes versões da plataforma.


13.3    Linha do tempo
A linguagem foi sem duvida um caso de sucesso. Em sua primeira ver-
são tinha cerca de 250 classes e agora conta com mais de 4.200, ricas APIs,
poderosos recursos e é executada por mais de 3 bilhões de dispositivos. Para
entendermos melhor todo esse sucesso, precisamos conhecer um pouco de
sua história, alguns de seus principais acontecimentos e introduções.

                                                                                 205


[PAGINA 216]
13.3. Linha do tempo                                           Casa do Código


Java 1
    Em 1991 a linguagem foi originalmente chamada de Oak (carvalho, em
inglês) por influência da vista na janela do escritório de seu criador, James
Gosling. Somente a partir de sua primeira versão estável, que foi a 1.0.2 em
1995, passou a ser chamada de Java 1.
    Existiam diversos bugs nesse momento e a performance era bastante
problemática.

Java 1.2
    Com mais de 2 milhões de downloads em sua versão atual, em 1998 foi
lançado o Java 1.2. Nessa versão diversos bugs foram corrigidos e a perfor-
mance foi consideravelmente melhorada. Um dos principais fatores respon-
sáveis por essa melhora foi a introdução do compilador JIT (Just In Time) em
que a compilação é feita durante a excecução do programa (em runtime) ao
invés de antes de sua execução.
    Outra introdução muito importante dessa versão foi a API de Collections,
que será profundamente estudada mais adiante.

  Java 2

     Por uma estratégia de marketing da época a linguagem passou a se
  chamar Java 2 (independente de sua versão, por exemplo a versão 1.3 era
  conhecida como Java(TM) 2 Platform, Standard Edition version 1.3). Ape-
  nas em 2004 na versão 1.5 que o 2 deixou de fazer parte do nome da lin-
  guagem.


Java 1.3
    Em 2000 a mais nova versão do java foi lançada, o Java 1.3. Alavancando
ainda mais sua performace, uma JVM conhecida como HotSpot passou a ser a
máquina virtual padrão da Sun. Essa JVM combinava interpretação de código
e compilação JIT (em tempo de execução).
    O seu código Java ainda era inicialmente interpretado, mas durante a ex-
ecução do programa a JVM passou a identificar os pontos executados com

206


[PAGINA 217]
Casa do Código                                Capítulo 13. Um pouco da história do Java



maior frequência (conhecidos como pontos quentes, ou HotSpots) e quando
necessário transformava esses códigos em instruções nativas da plataforma
que são executadas diretamente no hardware.

Java 1.4
    Chegando a quase 3 mil classes, a API foi enriquecida com introduções
como expressões regulares (Regular Expression), processamento de XML,
Logging e muito mais em sua versão 1.4, lançada em 2002. Essa foi a primeira
versão do Java desenvolvida no âmbito da JCP (Java Community Process).

Java 1.5
     Sem duvida uma das versões mais importantes, o Java 1.5 foi lançado em
setembro de 2004. Dentre diversas outras, Generics, imports estáticos, ano-
tações (metadata) e boxing de tipos primitivos foram algumas de suas novi-
dades.
     Essa versão também ficou bastante conhecida por introduzir uma forma
mais sucinta de iterar em coleções, o enhanced for que será melhor detalhado
adiante.
     Uma nova estratégia de marketing surge. Para melhor refletir o nível de
maturidade, estabilidade, escalabilidade e segurança da plataforma, o Java 1.5
deixou se ser Java 2 e passou a ser conhecido como Java 5. Mas claro, não
estamos falando de uma quebra de compatibilidade, a versão continua sendo
1.5.
     Desde então as versões da linguagem passaram a ser conhecidas pelo seu
ultimo numero.

Java 1.6
    A fim de impulsionar ainda mais a adoção da tecnologia, a Sun tornou
o Java open source. Ou seja, seu código foi aberto para comunidade com a
licença GNU (General Public License), a mesma utilizada pelo sistema opera-
cional Linux. Além disso, diversas otimizações no core da plataforma e na
JVM marcaram a versão 1.6.



                                                                                  207


[PAGINA 218]
13.3. Linha do tempo                                          Casa do Código


Java 1.7
    Quatro anos após sua ultima versão, essa foi a primeira versão após a
aquisição da Sun pela Oracle. O Java 7 foi lançado sob uma nova perspec-
tiva, teve como novidades uma nova API de I/O, recursos como o operador
diamante (diamond operator <>) e o try-with-resources.

Java 8
    A mais atual versão da plataforma sem duvida apresentou mudanças im-
pactantes para a linguagem. Seu lançamento aconteceu em março de 2014,
depois de 3 anos de muita espera. Diversos recursos foram introduzidos nessa
versão, defalt methods, expressões lambdas e method reference, que vimos
brevemente no capitulo anterior, foram algum deles.
    A versão também conta com uma nova API de datas baseada na con-
hecida biblioteca Joda Time, além de uma forma mais funcional de trabalhar
com suas coleções com a API de Stream.
    Vimos que até então seu código que era escrito dessa forma:

▲✐st❁❯s✉❛r✐♦❃ ✉s✉❛r✐♦s❋✐❧tr❛❞♦s ❂ ♥❡✇ ❆rr❛②▲✐st❁❃✭✮❀
❢♦r✭❯s✉❛r✐♦ ✉s✉❛r✐♦ ✿ ✉s✉❛r✐♦s✮ ④
    ✐❢✭✉s✉❛r✐♦✳❣❡tP♦♥t♦s✭✮ ❃ ✶✵✵✮ ④
        ✉s✉❛r✐♦s❋✐❧tr❛❞♦s✳❛❞❞✭✉s✉❛r✐♦✮❀
    ⑥
⑥

❈♦❧❧❡❝t✐♦♥s✳s♦rt✭✉s✉❛r✐♦s❋✐❧tr❛❞♦s✱ ♥❡✇ ❈♦♠♣❛r❛t♦r❁❯s✉❛r✐♦❃✭✮ ④
    ♣✉❜❧✐❝ ✐♥t ❝♦♠♣❛r❡✭❯s✉❛r✐♦ ✉✶✱ ❯s✉❛r✐♦ ✉✷✮ ④
        r❡t✉r♥ ✉✶✳❣❡t◆♦♠❡✭✮✳❝♦♠♣❛r❡❚♦✭✉✷✳❣❡t◆♦♠❡✭✮✮❀
    ⑥
⑥✮❀

❢♦r✭❯s✉❛r✐♦ ✉s✉❛r✐♦ ✿ ✉s✉❛r✐♦s❋✐❧tr❛❞♦s✮ ④
    ❙②st❡♠✳♦✉t✳♣r✐♥t❧♥✭✉s✉❛r✐♦✮❀
⑥

    Agora com Java 8 pode ser escrito de forma muito mais declarativa e fun-
cional:

208


[PAGINA 219]
Casa do Código                                  Capítulo 13. Um pouco da história do Java



✉s✉❛r✐♦s✳str❡❛♠✭✮
    ✳❢✐❧t❡r✭✉ ✲❃ ✉✳❣❡tP♦♥t♦s✭✮ ❃ ✶✵✵✮
    ✳s♦rt❡❞✭❝♦♠♣❛r✐♥❣✭❯s✉❛r✐♦✿✿❣❡t◆♦♠❡✮✮
    ✳❢♦r❊❛❝❤✭❙②st❡♠✳♦✉t✿✿♣r✐♥t❧♥✮❀

      Você pode ler mais sobre a história da plataforma e ver a timeline completa
em:
      http://www.java.com/en/javahistory/
      http://oracle.com.edgesuite.net/timeline/java/




                                                                                    209


[PAGINA 220]


[PAGINA 221]
Capítulo 14

Continuando seus estudos
Não deixe de praticar cada exercício proposto durante o Livro e sempre ir
além com novos testes e cenários mais complexos.
    Há diversas formas de continuar seus estudos, o GUJ é uma delas. Não
apenas para postar suas dúvidas, mas também respondendo aos demais
usuários e sendo um membro ativo da comunidade Java do Brasil. Ensinar
é uma das mais efetivas formas de aprender, espero te ver ensinado e apren-
dendo por lá:
    http://www.guj.com.br
    Outro caminho natural para continuar seus estudos é o livro Java 8
Prático: Lambdas, Streams e os novos recursos da linguagem. Nele explicamos
detalhadamente desde a sintaxe até o uso prático de cada novidade da mais
esperada versão do Java.
    http://www.casadocodigo.com.br/products/livro-java8


[PAGINA 222]
14.1. Entre em contato conosco                                 Casa do Código


14.1 Entre em contato conosco
Encaminhe suas dúvidas ou crie tópicos para discussão na lista que foi criada
especialmente para esse livro:
    https://groups.google.com/d/forum/livro-java-oo
    Além de perguntar, você também pode contribuir com sugestões, críticas
e melhorias para nosso conteúdo. Todas serão muito mais do que bem vindas.




212
