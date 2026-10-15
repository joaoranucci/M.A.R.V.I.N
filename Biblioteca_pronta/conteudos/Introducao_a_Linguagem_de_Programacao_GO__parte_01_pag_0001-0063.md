# Introducao_a_Linguagem_de_Programacao_GO

Arquivo original: most_similar_papers_to_this_one/Introducao_a_Linguagem_de_Programacao_GO.pdf
SHA-256 do original: b879bd8dc54beee59cba687778a625babc6beac42d06e16fe472cd413f3986fa

Texto extraido para consulta. As paginas abaixo usam a ordem do arquivo PDF, incluindo capas.
Parte preparada: 1/1


[PAGINA 1]
      Introdução à
Linguagem de Programação




Revisão 1 – Julho/2020 – Quarto mês da quarentena


[PAGINA 2]
                              Apresentação
Este curso de Introdução à Linguagem GO é uma continuação do curso
Algoritmos e & Lógica de programação.
Supõe-se, portanto, que o estudante já possua conhecimento teórico das estruturas
básicas dos algoritmos, bem como noções sobre os tipos e estruturas de dados
elementares como Arrays e Strings.
Para um melhor aproveitamento do curso, acesse os exercícios resolvidos no
GITHUB e veja também nossa apostila do Curso de Programação C .


[PAGINA 3]
  Temporada 1




Conceitos Básicos


[PAGINA 4]
                                  Características da Linguagem
A linguagem GO foi Desenvolvida em 2007 por uma equipe dentro do Google liderada por Robert Griesemer, Rob
Pike e Ken Thompson.




Principais características:                            O que foi deixado de lado:
 Sintaxe C Like. Concisa e simples, porém rígida.      Classes!
 Estaticamente compilada, mas com inferência de        Herança!
  tipos!                                                Overloading!
 Coleta de lixo e concorrência robusta.                Generics!
 Modular, com suporte para orientação a objetos mas    Exceções
  com ênfase em interfaces.
 Ponteiros, sem aritmética.
                                                                                                        4


[PAGINA 5]
                             Instalação e Preparação do Ambiente
O primeiro passo é preparar o seu workspace, ou seja, as pastas de trabalho onde vão ficar seus arquivos de
código-fonte, executáveis e etc.
Precisamos criar pelo menos três pastas que podem ficar dentro de qualquer outro diretório de sua preferência, por
exemplo: uma pasta de nome workspace.

•   pkg: Pasta onde ficam os pacotes e bibliotecas que você baixou ou criou para referência em seus programas.
•   src: Seus arquivos de código-fonte.
•   bin: Aqui estão os arquivos executáveis que você criou e instalou a partir da pasta src.

Agora vamos baixar e instalar o GO na pasta padrão (C:\Go em Windows ou /usr/local/go no Linux).
Site oficial para download: https://golang.org/dl/
Instruções de instalação: https://golang.org/doc/install

Depois, vamos criar quatro variáveis de ambiente :

•   GOPATH: Caminho para o seu workspace.
•   GOROOT: Caminho onde o GO foi instalado.
•   GOBIN: Caminho onde você quer seus executáveis.De preferência a suppasta bin do workspace.
•   PATH: Aponta para os binários do GO, geralmente a subpasta bin do caminho onde o GO foi instalado.           5


[PAGINA 6]
                             Instalação e Preparação do Ambiente
Golang enfatiza o uso de sistemas de controle de versão, como o GIT. Você precisará para instalar pacotes de
biblioteca de terceiros. Se você não tiver um instalado no seu sistema, consulte as instruções de instalação neste
link.

O último passo é baixar uma IDE. Você pode escolher uma aqui nesse link.
Sugiro fortemente duas delas:
• Visual Studio Code com a extensão para a linguagem GO.
• LiteIDE: ambiente de desenvolvimento exclusivo para linguagem GO.
• Geany: Editor de Textos para programadores. Já vem configurado para compilar programas GO

Feita a instalação e a preparação do ambiente, o próximo passo é digitar nosso primeiro programa, o Alô Mundo,
que é o primeiro programa para desenvolvemos quando vamos aprender uma nova linguagem. Esse programa
apenas apresenta uma mensagem de boas vindas na tela, mas através dele podemos aprender conceitos iniciais
muito importantes sobre a linguagem.

Em nossos estudos, sempre vamos fazer comparações com a linguagem C e suas derivadas para facilitar o
aprendizado.

                                                                                                                6


[PAGINA 7]
                                              Alô Mundo!
 1   package main
 2   // Primeira aplicação GO                        As chaves { } são usadas para marcar o início e fim dos
 3   import “fmt”                                    blocos de comandos e devem ser indentadas (*) dessa forma
 4   func main() {
 5       fmt.Println("Hello from GO!")
 6   }                                                (*) Muitos dicionários preferem o termo “endentação”.


(1) Todo programa GO deve começar com a declaração do pacote ao qual ele pertence. A instrução package main
e a função main da linha 4 dizem ao compilador que este é um programa executável. A função main, portanto, é o
ponto de partida das aplicações. Quando executamos o programa, essa função é iniciada, e quando ela finaliza, o
programa termina. Portanto, o identificador main para funções e pacotes possui um significado especial aqui.
(2) Os comentários em GO seguem o mesmo estilo da linguagem C.
(3) Nessa linha estamos importando o pacote fmt que contém funções de formatação de entrada e saída.
(4,5,6) Nessas linhas de código temos a função principal (main), que a funçãp de entrada. Neste caso, a função
imprimirá a mensagem "Hello from GO!" usando o método Println() presente no pacote fmt.
Obs:
1. Ao contrário de C, não usamos o separador ponto e vírgula (;) no final dos comandos.
2. Assim como o C, GO é sensitive case. No entanto, maiúsculas e minúsculas possuem um significado especial
     na linguagem como veremos mais à frente.
3. A posição das chaves e a endentação (*), assim como estão, são padrões que é prudente seguirmos.          7


[PAGINA 8]
                                      Compilando e Executando
Nosso programa “Alô Mundo” que está em um arquivo alo.go foi colocado em uma subpasta alo da pasta src do
workspace.
Se você planeja publicar seu módulo para que outros usem, o caminho do módulo deve ser um local a partir do qual
as ferramentas GO possam baixaá-lo. Para ativar o rastreamento de dependência para seu código, vá para a pasta
onde se encontra o arquivo alo.go, e execute o seguinte comando:
 go mod init alo

Uma vez que GO é uma linguagem compilada, para executar nosso programa Alô Mundo, devemos compilá-lo
para gerar um executável e, para isso, usamos a linha de comando:
 go build hello.go
Ou, melhor ainda, para compilar e executar, digite:
 go run hello.go

Outros utilitários da linha de comando, não abordados nesse curso, são:
• go vet: Verifica o código-fonte e exibe as linhas com comandos suspeitos, com problemas de lógica.
• go get: Instala pacotes de terceiros, comumente armazenados em repositório de códigos como o GitHub.
• gofmt: Formata o código-fonte.
• goimports: Verifica o código-fonte e corrige as linhas com imports perdidos ou necessários.                 8


[PAGINA 9]
                                                  Pacotes e Importação
Para incentivar a modularização e a organização, cada programa GO deve fazer parte de um package. Um
package é uma coleção de arquivos de código-fonte, localizados na mesma pasta, que são compilados em
conjunto. Para declarar um arquivo de código-fonte como parte de um pacote, digitamos a seguinte declaração no
cabeçalho do arquivo:
 package packagename

Esta declaração do pacote deve ser a primeira linha de código. Desta forma, todas as funções, tipos e variáveis
definidas no seu arquivo GO tornam-se parte desse pacote.
GO tem uma poderosa biblioteca nativa (GO Standard Library) que também é organizada em pacotes.

Algumas bibliotecas comuns:                                  Para usar uma dessas bibliotecas, usamos o comando
                                                             de importação.
Package    Funcionalidades
                                                             Assim:              Ou assim:
fmt        Formação de dados de entrada e saída
                                                              import "fmt"         import (
math       Funções matemáticas
                                                              import “math"          "fmt"
strconv    Conversões                                                                m “math"
strings    Manipulação de Strings                                                  )
io         Funções básicas de entrada e saída
                                                             Obs: No segundo exemplo, usamos um apelido (alias)
net/http   Implementação de clientes e servidores http
                                                             para o package math. Isso facilita as referências. 9


[PAGINA 10]
                                       Tipos de Dados Básicos
O tipo de dado de uma variável estabelece uma faixa de valores que ela pode aceitar, bem como as operações
passíveis de serem realizadas com esses valores. Em quase toda linguagem, os tipos são divididos em:

•   Primitivos ou básicos: Não podem ser decompostos em valores mais simples, ou seja, são atômicos e,
    geralmente, possuem relação direta com a arquitetura do computador.
•   Compostos ou estruturados: São tipos de dados formados à partir dos tipos básicos, podendo inclusive serem
    definidos pelo programador.

Os tipos de dados primitivos em GO subdividem-se em Numéricos, Caracteres e Booleanos.

Os tipos numéricos, por sua vez, podem ser inteiros ou de ponto flutuante, de acordo com a tabela exibida na
página seguinte.

Os tipos caracteres em GO são dois: o byte (caracteres ASCII de 8 bits) e o rune (caracteres unicode de 32 bits).
São, na verdade, tipos numéricos, como veremos a seguir.

GO disponibiliza ainda o tipo bool para representar valores lógicos que, diferentemente da linguagem C, não são
tratados como tipos numéricos, aceitando apenas dois valores: true ou false.
                                                                                                              10


[PAGINA 11]
                            Tipos de Dados Numéricos


Tipo de dado   Descrição
uint8          Inteiro de 8 bits sem sinal (0 a 255)
uint16         Inteiro de 16 bits sem sinal (0 a 65535)
uint32         Inteiro de 32 bits sem sinal (0 a 4294967295)
uint64         Inteiro de 64 bits sem sinal (0 a 18446744073709551615)
uint           Inteiro sem sinal dependente da plataforma
int8           Inteiro de 8 bits com sinal (-128 a 127)
int16          Inteiro de 16 bits com sinal (-32768 a 32767)
int32          Inteiro de 32 bits com sinal (-2147483648 a 2147483647)
int64          Inteiro de 64 bits com sinal (-9223372036854775808 a 9223372036854775807)
int            Inteiro com sinal dependente da plataforma
float32        Número de ponto flutuande de 32 bits padrão IEEE-754
float64        Número de ponto flutuande de 64 bits padrão IEEE-754

                                                                                           11


[PAGINA 12]
                                Variáveis - Declaração e Atribuição
Como sabemos, uma variável é o nome dado a um local de memória para armazenar um valor de um tipo de dados
específico.
A operação de declaração de uma variável consiste em definir seu nome e tipo de dados. Já, a operação de
atribuição consiste em armazenar na variável (posição de memória) um valor compatível com seu tipo de dado.

Como a linguagem GO é estática e fortemente tipada, todas as variáveis precisam ser declaradas antes de serem
usadas, seja explicitamente ou de forma que o compilador possa inferir seu tipo.

A operação de inicialização consiste em atribuir um valor inicial para a variável logo depois que ela foi declarada.
Um ponto interessante em GO é que todas as variáveis são automaticamente inicializadas na declaração:
variáveis numéricas e caracteres com 0 (zero) e booleanas com false.

O operador de atribuição padrão é o sinal de igual (=). GO possui ainda um operador de declaração e inicialização
(:=) que veremos a seguir.

A sintaxe geral de declaração/inicialização de variáveis é:
 [var] nome_variável [tipo_dados] [= | := <valor>]

Obs: Se você declarar uma variável e não utilizá-la no código, isso causará um erro de compilação.               12


[PAGINA 13]
                              Variáveis - Declaração e Atribuição
Exemplos de declarações e atribuições:
 // Aqui declaramos uma variável de nome “idade” do tipo int. Seu valor será zero.
 var idade int

 // Neste outro exemplo, declaramos a variável e depois atribuímos o valor 18 para ela.
 var idade int
 idade = 18


 // Agora, declaração e atribuição no mesmo comando
 var idade int = 18

 // Várias variáveis
 var (
     idade int     = 18
     peso float64 = 85.5
 )

Obs: GO desencoraja o uso de underscore ou hífen para nomes de variáveis. Por exemplo, uma variável nomeada
como peso_ideal, deverá ser renomeada para pesoIdeal ou PesoIdeal.                                       13


[PAGINA 14]
                                Variáveis – Inferência de Tipos
Podemos declarar uma variável sem especificar seu tipo de dado. Este será inferido pelo compilador de acordo
com o valor atribuído:
 // Como o valor atribuído NÃO possui parte decimal, a variável será declarada como “int”.
 var idade = 30

 // Como o valor atribuído POSSUI parte decimal, a variável será declarada como “float64”.
 var peso = 73.7


GO possui um operador de declaração (:=) por inferência de tipos conhecida como short hand declaration. Essa
forma de declaração não necessita da palavra reservada var e é a preferida dos Gophers.

 // A variável é declarada como “int” com valor inicial de 30
 idade := 30

 // Várias variáveis
 // Nesse caso, a variável “idade” será do tipo “int” e a variável “peso” do tipo “float64”
 idade, peso := 30, 70.7

                                                                                                         14


[PAGINA 15]
                                                Constantes
Uma constante é um valor armazenado na memória que não pode ser alterado, mantendo-se fixo durante todo o
tempo de execução do programa. Podem ser constantes nomeadas ou literais.

Uma constante nomeada é como uma variável, pois recebe um nome, um tipo e uma posição na memória. A
diferença é que não podem ser alteradas pelos comandos de atribuição, ou seja, não podem estar do lado esquerdo
da atribuição (left-side value).

Para declararmos uma constante, usamos a palavra reservada const:
const masculino byte = ‘F’
O tipo da constante pode ser omitido na declaração, pois pode ser inferido, porém não podemos usar a declaração
curta (:=)
Já, uma constante literal é aquela que é especificada diretamente no código, sem nome.
Por exemplo: No comando abaixo, os valores 30 e 70.7 são constantes literais e seu tipos são inferenciados pelo
compilador.
idade, peso := 30, 70.7


                                                                                                              15


[PAGINA 16]
                              Operações Aritméticas e Conversões
As operações matemáticas em GO não diferem muito das outras linguagens, a não ser em relação à conversão de
tipos nas expressões. Um cuidado especial devem ter os programadores que estão acostumados com outras
linguagens que efetuam o cast automático de tipos nas expressões. Em GO essas conversões devem ser feitas de
forma manual. Vejam um exemplo:

Errado:                                     Correto:
   var a float64 = 1000                        var a float64 = 1000
   var b int = 10                              var b int = 10
   var soma float64 = a + b                    var soma float64 = a + float64(b)
   fmt.Println(soma)                           fmt.Println(soma)



Para fazer as conversões, use as funções apropriada para cada tipo, como uint(), float64(), float32(), etc.




                                                                                                              16


[PAGINA 17]
                           Operadores Aritméticos e de Atribuição
Segue um resumo dos operadores aritméticos e de atribuição mais utilizados em GO:

Operadores de atribuição                              Operadores aritméticos
 Operador       Descrição                              Operador           Descrição
 x = y          Atribuição
 x := y         Declaração e atribuição                 +                 Adição
 x += y         Adiciona e atribui
                                                        -                 Subtração
 x -= y         Subtrai e atribui
 x *= y         Multiplica e atribui                    *                 Multiplicação
 x /= y         Divide e atribui                        /                 Divisão
 x++            Atribui e incrementa                    %                 Resto da divisão
 ++x            Incrementa e atribui
 x--            Atribui e subtrai                       ++                Incremento
 --x            Subtrai e atribui                       --                Decremento



                                                                                             17


[PAGINA 18]
                                                       Ponteiros
Ponteiros são variáveis que armazenam endereços de          var a int = 7 // a é variável int = 7
memória.                                                    var b *int    // b é um ponteiro para int
Assim como qualquer variável, um ponteiro precisa ser       b = &a        // b recebe o endereço de a
declarado e deve apontar para valores do mesmo tipo de
dado para o qual foi criado.                                fmt.Println(a) // Imprime 7
Dessa forma, podemos guardar em uma variável                fmt.Println(&a) // Imprime 0xc0000100a0
ponteiro o endereço de memória de outra variável e,         fmt.Println(b) // Imprime 0xc0000100a0
assim, acessar diretamente o seu valor.                     fmt.Println(*b) // Imprime 7
Golang disponibiliza dois operadores para trabalharmos
                                                            *b++ // Incrementa o valor apontado por b
com ponteiros e endereços de memória:
                                                            fmt.Println(a)   // Imprime 8
Operador Nome          Descrição
&        Referência    Retorna o endereço de memória de
                                               Obs: Os endereços que aparecem acima são na minha
                       uma variável
*                                              máquina, naquele momento. Na sua máquina vão
         Derreferência Retorna o conteúdo de um endereço
                       de memória              aparecer outros endereços.
                                               Ponteiros são elementos importantes da linguagem GO
Para declararmos uma variável ponteiro, usamos e você vai ter que usá-los. Por isso reservamos um curso
também o operador ‘*’.                         à parte sobre eles. Voltaremos a falar sobre endereços de
Vejamos um exemplo:                            memória na temporada sobre funções.                    18


[PAGINA 19]
                                    Funções de Saída de Dados
Vamos abordar agora as funções para impressão de dados na tela. Para imprimir expressões envolvendo variáveis e
constantes, o pacote fmt disponibiliza as seguintes funções:

•   Print() → Usada para imprimir uma sequência de expressões separadas por vírgulas. Para cada expressão será
    usado um formato padrão.
•   Println() → Faz a mesma coisa que print(), no entanto pula de linha após a impressão.
•   Printf() → Imprime uma expressão usando um template com códigos de formatação (verbos).

Os códigos de formatação usados pelo printf() são parecidos com os da linguagem C. Vejamos alguns:

                    Código    Descrição
                    %v        Formatador genérico. Usa inferência de tipos
                    %d        Valor inteiro na base 10
                    %f        Valor em Ponto flutuante
                    %c        Tipos caractere
                    %s        Uma string
                    %t        Valor booleano: true ou false
                    %T        Mostra o tipo de dados da variável
                                                                                                            19


[PAGINA 20]
                         Funções de Saída de Dados - Exemplos
 package main

 import "fmt"

 func main() {
   var (
     peso   float64 = 75.0
     idade int      = 18
     altura float64 = 1.76
   )
   fmt.Println("Olá!")
   fmt.Println("Sua idade é igual a: ", idade)
   fmt.Printf(“Vc apresentou um peso de %f quilos e uma altura de %f metros", peso, altura)
 }

Irá imprimir:
Olá!
Sua idade é igual a: 18
Vc apresentou um peso de 75.000000 quilos e uma altura de 1.760000 metros
                                                                                              20


[PAGINA 21]
                                  Funções de Entrada de Dados
Para finalizar essa parte introdutória do curso, vamos abordar agora as funções para leitura de dados através das
quais o usuário informa, pelo teclado, os dados de entrada requeridos pelas aplicações. Para essa finalidade, o
pacote fmt disponibiliza as seguintes funções:
• Scan() → Usada para ler os dados vindos do dispositivo de entrada padrão (teclado) e armazenar na memória.
   O formato dos dados será inferido pelo tipo da variável.
• Scanf() → Semelhante ao Scan, porém o formato é definido pelo programador através de códigos de
   formatação (verbos).

Os códigos de formatação usados pelo Scanf() são parecidos com os da linguagem C. Vejamos alguns:

                    Código     Descrição
                    %v         Formatador genérico. Usa inferência de tipos
                    %d         Valor inteiro na base 10
                    %f         Valor em Ponto flutuante
                    %c         Tipos caractere
                    %s         Uma string
                    %t         Valor booleano: true ou false
                    %T         Mostra o tipo de dados da variável
                                                                                                              21


[PAGINA 22]
                         Funções de Entrada de Dados - Exemplos
 package main
 import "fmt"
 func main() {
   idade, peso, altura := 0, 0.0, 0.0
   fmt.Print("Informe a idade: ")
   fmt.Scanf("%v", &idade) // Veja que passamos o endereço da variável
   fmt.Print("Informe o peso: ")
   fmt.Scanf("%v", &peso)
   fmt.Print("Informe a altura: ")
   fmt.Scanf("%v", &altura)
   fmt.Printf("Olá!\nSua idade é igual a %v\n: ", idade)
   fmt.Printf("Vc apresentou um peso de %g quilos e uma altura de %g metros", peso, altura)
 }

Irá imprimir: Informe a idade: 30
              Informe o peso: 75
              Informe a altura: 1.77
              Olá!
              Sua idade é igual a: 30
              Vc apresentou um peso de 75 quilos e uma altura de 1.77 metros                  22


[PAGINA 23]
                  Fim da Temporada 1: Consolidando o Conhecimento
Exercício: Ler duas notas e calcular a média aritmética entre elas.
 // media.go:

 package main
 import "fmt“

 func main() {
   // Declaração de variáveis
   var nota1, nota2, media float64

     // Leitura das variáveis informadas pelo usuário
     fmt.Print("Informe a nota 1: ")
     fmt.Scan(&nota1)
     fmt.Print("Informe a nota 2: ")
     fmt.Scan(&nota2)

     // Processamento e exibição do resultado
     media = (nota1 + nota2) / 2.0
     fmt.Printf("A média entre %f e %f é %f", nota1, nota2, media)
 }

                               Baixe este e outros exercícios resolvidos no GITHUB   23


[PAGINA 24]
    Temporada 2




Estruturas de Decisão


[PAGINA 25]
                                       Estruturas de Decisão
As estruturas de decisão permitem dividir o fluxo de    if condição1 {
execução das instruções entre dois ou mais caminhos       // Trecho executado se condição1 é verdadeira
diferentes, permitindo realizar tomadas de decisão de   } else if condição2 {
                                                          // Trecho executado se condição2 é verdadeira
acordo com a análise de uma expressão lógica
                                                        } ... else {
(true/false).                                             // Trecho executado se todas condições
                                                          // anteriores forem falsas}
GOLANG possui três tipos de estruturas condicionais:    }


1) if - else → Estrutura de decisão tradicional que 3) switch → Estrutura de decisão especializada em
permite escolher entre dois fluxos alternativos.    múltiplas alternativas de fluxo, não necessariamente
                                                    através de expressões lógicas.
if condição {
  // trecho executado se a condição é verdadeira        switch [expressão] {
} else {                                                case expressão1: Trecho de comandos
  // trecho executado se a condição é falsa             case expressão2: Trecho de comandos
}                                                       ...
                                                        default: Trecho de comandos
                                                        }
2) if - else if → Estrutura de decisão alternativa quando
temos mais de duas possibilidades de fluxo.               Vamos ver agora exemplos de cada uma →
                            →                                                                             25


[PAGINA 26]
                                 Estruturas de Decisão - Exemplos
1) Testa se número é par usando if - else:                3) Testa positividade do número com if - else if:
 var numero int = 1                                          var numero int = 1
 if numero%2 == 0 {                                          if numero > 0 {
   fmt.Printf("O número %d é par", numero)                     fmt.Printf("O número %d é positivo", numero)
 } else {                                                    } else if numero < 0 {
   fmt.Printf("O número %d é ímpar", numero)                   fmt.Printf("O número %d é negativo", numero)
 }                                                           } else {
                                                               fmt.Printf("O número %d é neutro", numero)
                                                             }
2) Testa positividade do número com if - else aninhado:
                                                          Obs:
 var numero int = 1
 if numero > 0 {
                                                          1. A condição avaliada não precisa ficar entre
   fmt.Printf("O número %d é positivo", numero)              parênteses
 } else {                                                 2. As chaves são obrigatórias.
   if numero < 0 {                                        3. A posição das chaves, “indentação” e posição do
     fmt.Printf("O número %d é negativo", numero)
   } else {
                                                             else como estão são importantes e podem causar
     fmt.Printf("O número %d é neutro", numero)              erros de compilação
   }                                                      4. A cláusula else é opcional .
 }

                                                                                                              26


[PAGINA 27]
                               Estruturas de Decisão - Exemplos
4) Testa positividade do número com switch:             5) Informa o dia da semana com switch:
 numero := -1                                              diaSemana := 6
 switch {                                                  switch diaSemana {
   case numero < 0:                                        case 0:
     fmt.Printf("O número %d é negativo", numero)            fmt.Println("Hoje é domingo")
   case numero > 0:                                        case 6:
     fmt.Printf("O número %d é positivo", numero)            fmt.Println("Hoje é Sábado")
   default:                                                case 1, 2, 3, 4, 5:
     fmt.Printf("O número %d é neutro", numero)              fmt.Println("Hoje é dia de semana")
 }                                                         default:
                                                             fmt.Println("Dia inválido")
                                                           }


Obs:
1. A estrutura switch em GO é mais poderosa e flexível em relação a outras linguagens .
2. Podemos testar expressões lógicas como no exemplo 4.
3. O comando break não é necessário.


                                                                                                   27


[PAGINA 28]
                 Fim da Temporada 2 – Consolidando o Conhecimento
Exercício: Dadas as dimensões dos três lados A,B,C de um triângulo, desenvolva um algoritmo para determinar o
tipo do triângulo de acordo com seus lados: Equilátero, Isósceles ou Escaleno. Obs: Em todo triângulo, cada um
dos lados deve ser menor que a soma dos outros dois.
 // triangulo.go                                         // Teste e exibição dos resultados
                                                         if !(A < (B+C) && B < (A+C) && C < (A+B)) {
 package main                                              fmt.Println(“Lados inválidos")
                                                         } else {
 import "fmt"                                              switch {
                                                           case A == B && B == C:
 func main() {                                               fmt.Println("Triângulo Equilátero")
                                                           case A == B || A == C || B == C:
   // Declaração das variáveis (float64)                     fmt.Println("Triângulo Isósceles")
   A, B, C := 0.0, 0.0, 0.0                                default:
                                                             fmt.Println("Triângulo Escaleno")
   // Leitura dos dados                                    } // Fim switch
   fmt.Print("Informe o lado A: ")                       } // Fim if
   fmt.Scan(&A)                                        } // Fim main
   fmt.Print("Informe o lado B: ")
   fmt.Scan(&B)
   fmt.Print("Informe o lado C: ")                        Baixe este e outros exercícios resolvidos no GITHUB
   fmt.Scan(&C)
                         →
                                                                                                                28


[PAGINA 29]
     Temporada 3




Estruturas de Repetição


[PAGINA 30]
                                      Estruturas de Repetição
As estruturas de repetições são construções que permitem a execução repetitiva de um bloco de códigos de acordo
com a avaliação de uma condição (expressão lógica). A repetição ocorrerá enquanto essa condição for verdadeira
(condição de parada).
Curiosa e acertadamente, a linguagem GO possui apenas uma estrutura de repetição: O laço for que é muito
flexível e poderoso, podendo realizar qualquer tipo de repetição das linguagens tradicionais.
 for [pré; ] [condição;] [pós] {
 ...
 [break]
 [continue]
 ...
 }

Onde:
• pré → Comando executado antes da primeira iteração.
• condição → Expressão lógica que representa a condição de parada, avaliada a cada iteração.
• pós → Comando executado no fim de cada iteração.
• break /continue → Usados para, respectivamente, interromper ou saltar a execução do laço de repetição.

É possível também fazer iterações em coleções de dados como slices e strings, como veremos na temporada sobre
estruturas de dados.                                                                                       30


[PAGINA 31]
                              Estruturas de Repetição - Exemplos
1) Laço for simples, exibindo os número de 1 até 10:     4) Contagem de 6 a 10 com continue:
for i := 1; i <= 10; i++ {                               for i := 1; i <= 10; i++ {
    fmt.Println(i)                                         if i < 6 {
}                                                            continue
                                                           }
                                                           fmt.Println(i)
2) Laço while simples, exibindo os número de 1 até 10:   }
i := 1
for i <= 10 {                                            Obs:
 fmt.Println(i)                                          1. As chaves são obrigatórias e na posição em que
 i++                                                        estão.
}
                                                         2. Parênteses envolvendo os componentes não são
                                                            necessários
3) Contagem de 1 a 5 com break:                          3. Existe uma maneira mais fácil de iterar sobre
for i := 1; i <= 10; i++ {
                                                            coleções de dados, como arrays e slices: o
    fmt.Println(i)                                          operador range que veremos a seguir.
    if i == 5 {
      break
    }
}
                                                                                                       31


[PAGINA 32]
                  Fim da Temporada 3 – Consolidando o Conhecimento
Exercício: Imprima as temperaturas em graus Celsius, Kelvin e Fahrenheit variando na faixa de -100oC até 100oC,
sabendo que:


 package main

 import "fmt"

 func main() {
   // Declaração das variáveis para Celsius, Fahreinheit e Kelvin
   var C, F, K float64

     // Repetição de -100 C até 100 C
     for C = -100; C <= 100; C++ {
       F = C*9.0/5.0 + 32.0 // Cálculo de Fahreinheit
       K = C + 273.15 // Cálculo de Kelvin
       fmt.Printf("%f C = %f F = %f K\n", C, F, K) // Impressão
     }

 }

                               Baixe este e outros exercícios resolvidos no GITHUB
                                                                                                            32


[PAGINA 33]
       Temporada 4




Estruturas de Dados Básicas


[PAGINA 34]
                                Estruturas de Dados Compostas
As estruturas de dados compostas são os tipos de dados formados à partir dos tipos primitivos. Neste curso
introdutório, vamos estudar as seguintes estruturas disponibilizadas nativamente pela linguagem GO:

•   Strings → Uma string em GO possui as mesmas características abstratas de outras linguagens, mas sua
    implementação é bem diferente. Em GO, uma string é uma cadeia imutável de caracteres (bytes) representados
    usando a codificação UTF-8.

•   Arrays → Os arrays em GO possuem as mesmas características abstratas de linguagens como C e Java, ou
    seja, uma coleção com tamanho fixo de variáveis do mesmo tipo e que são acessadas através de índices.

•   Slices → Um slice é uma abstração de um array. Como o nome diz, uma fatia, os seja, uma view para um
    array. Assim como um array, um slice é indexado e possui um tamanho, mas sua vantagem é que podemos
    mudar esse tamanho com facilidade.

•   Maps → Equivalem aos arrays associativos, onde temos uma coleção de pares “chave → valor”

•   Structs → Uma struct é uma estrutura de dados heterogênea. Abstratamente é um registro composto de
    campos de diferentes tipos de dados, mas logicamente relacionados.
                                                                                                           34


[PAGINA 35]
                                                  Arrays
Um array unidimensional (vetor) é uma estrutura homogênea de dados que armazena uma sequência de
variáveis (elementos), todas do mesmo tipo acessados individualmente através de um número sequencial que
denominamos índice do array. Ou seja, cada elemento do vetor é identificado por sua posição dentro do vetor.

•   A quantidade de elementos (tamanho do array) e seu tipo devem ser definidas no momento da declaração e são
    imutáveis;
•   Os elementos possuem ordinalidade, cada um pode ser identificado pela sua posição (índice do vetor);
•   Em GO, os índices dos vetores começam em 0 (zero) e vão até (tamanho-1)
•   Cada elemento do vetor, por meio do seu índice, pode ser acessado como uma variável individual.
•   No array abaixo de nome “idade”, o valor do elemento de índice 4 é 81.


                               0   1     2    3    4     5    6    7     8    9       Índices (de 0 a 9)
                              17 33 21 67 81 10 45 29 79 98                           Valores


                                         Vetor idade com 10 elementos

                                                                                                           35


[PAGINA 36]
                                      Operações com Arrays
Declaração de Arrays                               Representação didática do array de nome nota:
Para declararmos um array, precisamos informar seu    5        6.5         7          Elementos
nome, tamanho e tipo de dado. Exemplo:                0         1          2          Índices
var nota[3] float64
                                                      Podemos também atribuir valores através da leitura pela
Essa declaração vai criar um array de nome nota com 3 função Scan(), sempre através do índice:
elementos do tipo int, indexados de 0 a 2. Todos os
                                                       fmt.Print(“Digite o valor para o vetor: ”)
elementos vão ser preenchidos com o valor 0.0.
                                                       fmt.Scan(nota[1])
Outra forma de declarar um array, é atribuir valores
para seus elementos já na criação:
                                                      Acessando os elementos de um array
 var nota = [35] float64{5,6.5,7}
                                                      Sempre através do índice:
                                                        fmt.Println(nota[1])
Atribuindo valores para os elementos de um array
Devemos especificar o elemento pelo seu índice:        Alternativamente, podemos imprimir todo o vetor, dessa
Nota[0] = 5
                                                       forma:
Nota[1] = 6.5                                           fmt.Println(nota)
Nota[2] = 7
                                                                                                          36


[PAGINA 37]
                         O Operador Range e o Identificador Blank
Para iterarmos sobre os elementos de um array podemos usar a estrutura de repetição for da forma tradicional:
 for i:= 0, i < len(nota); i++ {                              Onde: len é a função que devolve o tamanho do
   fmt.Printf(“indice = %d e Valor = %f”,i,nota[i]) vetor, i é o índice do vetor e nota[i] é o conteúdo
 }                                                            de cada elemento.

No entanto, em GO, existe uma forma mais fácil, usando o operador range que devolve, a cada iteração do for, o
índice e o valor do array (conteúdo):
 for i,v := range nota {
   fmt.Printf(“Indice = %d e Valor = %f”,i,v)
 }

Caso alguns desses valores de retorno não sejam necessários, podemos ignorá-los através do identificador blank, o
underscore. Por exemplo, caso o índice do elemento não seja necessário, podemos refazer a repetição anterior:
for _,v := range nota {
  fmt.Printf(“Valor = %f”,v)
}

Na verdade, o identificador blank é muito utilizado em GO, como veremos na temporada sobre funções.
                                                                                                              37


[PAGINA 38]
                                         Arrays - Exemplo
Exercício: Leia 10 notas de um aluno, armazene em um array e calcule a média Geral. Logo após, relacione as
notas que estão acima da média.
package main                                                   // Parte 3 - Notas maiores que a média
import "fmt"                                                   fmt.Println("Notas Maiores do que a média:")
                                                               for i, v := range nota {
func main() {                                                    if v > media {
  const numNotas int = 10 // Quantidade de notas                   fmt.Printf("Nota %d = %f\n", i, v)
  var (                                                          }
      nota        [numNotas]float64 // Arrqy de notas          }
      soma, media float64 = 0, 0                           }
  )

  // Parte 1 – Leitura
  for i := 0; i < 10; i++ {                               Veja que, nesse exemplo, usamos operador range
    fmt.Printf("Informe a nota %d: ", i)                  para iterar entre os elementos do vetor.
    fmt.Scan(&nota[i]) // Armazena nota no array          Quando iteramos uma coleção usando range, dois
    soma += nota[i] // Calcula a soma das notas
  }
                                                          valores são retornados para cada iteração:
                                                          O primeiro é o índice (i) e o segundo é uma cópia
  // Parte 2 – Cálculo da média                           do valor do elemento desse índice (v).
  media = soma / float64(numNotas) // Cálculo da média
  fmt.Printf("Média = %f\n", media)                 →                                                     38


[PAGINA 39]
                                                     Slices
Um slice é uma estrutura que aponta para um array, permitindo manipular os seus elementos e o seu tamanho. Na
verdade, um slice não armazena nenhum valor: sempre haverá um array associado onde os elementos estarão
armazenados.

As seguintes propriedades estão associadas a um slice:
• ptr → Um ponteiro para o array associado.
• len → Tamanho do slice (número de elementos).
• cap → Capacidade do slice (tamanho máximo).




Depois de criado o slice, podemos manipular seus elementos da mesma forma como fazemos com os arrays
(através dos índices), com a vantagem de que slices possuem funções para adicionar elementos, alterando seus
tamanhos.
                                                                                                          39


[PAGINA 40]
                                       Operações com Slices
Declaração                                       Adicionando elementos ao slice
Podemos usar a função make(), passando o tipo de Podemos usar a função append, passando o slice e os
dado, o tamanho e a capacidade do slice:         elementos a serem adicionados:
 nota := make([]float64,3,10)                            a := make([]int, 0,10)
                                                         a = append(a, 1, 2, 3)
Essa operação vai criar um slice de nome nota, com 3
elementos numerados de 0 a 2, mas com capacidade de Nesse exemplo, criamos um slice vazio e adicionamos
crescimento para 10 elementos.                        três elementos, que podem ser acessados pelos seus
Para obter o tamanho e capacidade de um slice, usamos índices de 0 a 2.
as funções len() e cap(), respectivamente.
                                                      Percorrendo um slice com range
Podemos também criar um slice informando seus Podemos usar uma repetição para iterar sobre os
elementos:                                            elementos do slice:
 nota := []float64(5,6.5,7)                              var s = []int{1, 2, 4, 8, 16, 32, 64, 128}
                                                         for indice, valor := range s {
                                                           fmt.Printf("Índice = %d\n”, indice)
Para atribuição dos valores, impressão e leitura de um     fmt.Printf("Valor = %d\n", valor)
slice, procedemos da mesma forma como fazemos com        }
arrays.                                                                                               40


[PAGINA 41]
                                          Slices - Exemplo
Exercício: Leia um número indeterminado de números inteiros e armazene os pares em um slice de nome par e os
ímpares em um slice de nome impar. A leitura deverá parar quando for digitado um número negativo.
package main                                                   // Parte 2 - Notas maiores que a média
import "fmt"                                                   fmt.Println("Números Pares:")
                                                               for _, valor := range par {
 func main() {                                                   fmt.Println(valor)
   var par, impar []int // Slices                              }
   var numero int                                              fmt.Println("Números Ímpares:")
   // Parte 1 – Leitura e armazenamento nos slices             for _, valor := range impar {
   for {                                                         fmt.Println(valor)
     fmt.Print("Dígite um número: ")                           }
     fmt.Scan(&numero)                                     }
     if numero < 0 { // Fim da leitura
       break                                              Veja no range que ignoramos o índice e usamos só
o    }                                                    o valor (v) do slice. Para isso, usamos o operador _.
     if numero%2 == 0 { // Slice par
       par = append(par, numero)
     } else { // Slice impar
       impar = append(impar, numero)
     }
   }
                                                      →                                                     41


[PAGINA 42]
                                                      Strings
De forma abstrata, uma string é um tipo de dado que representa um texto, uma palavra ou frase qualquer, ou seja,
um conjunto de caracteres.
Em GO, o tipo de dados string é uma sequência de caracteres unicode com a codificação UTF-8.

Uma string possui um tamanho associado e cada caractere pode ser obtido pela sua posição dentro da string.
Dessa forma a palavra “GOLANG” pode ser representada didaticamente, como:
  G     O     L     A     N      G           string
  0     1     2     3     4      5           posição dos caracteres
Onde, por exemplo, a letra ‘L’ está na posição 2.

Internamente as strings são tratadas como slices de bytes e, para sua manipulação, devemos importar o package
‘strings’ da biblioteca padrão.

Para declararmos e inicializarmos uma string, usamos o separador de aspas duplas:
 var s string      ou em um comando só: var s string = “GOLANG”
 s = “GOLANG”

                                                                                                             42


[PAGINA 43]
                                         Operações com Strings
Função len() para obter o tamanho:
                                                       Obter a posição de uma substring:
s := “PYTHON”                                                                                 Vai imprimir: 2
fmt.Prinln(len(s))            Vai imprimir: 6
                                                       s := "GOLANG"
                                                       fmt.Println(strings.Index(s,“L")
Para obter o caractere em uma posição:
                                                                                           Vai imprimir: true
                                                       Verifica se a string contém uma substring:
s := “PYTHON”
fmt.Printf("%c", s[1])               Vai imprimir: Y
                                                       s := "GOLANG"
                                                       fmt.Println(strings.Constains(s,“GO")
Para obter uma substring:
s := “GOLANG”
                                                       Consulte a documentação do package strings para
fmt.Println(s[2:5])            Vai imprimir: LANG      conhecer mais funções.
                                                       Obs: Para leitura de strings com espaços, o pacote
                                 Vai imprimir:         bufio contém métodos mais apropriados, como o
Para concatenar strings:         GOLANG e PYTHON       readString que veremos no exercício seguinte.
s := "GOLANG"
S1 = "PYTHON"
fmt.Println(s + " e " + s1)                                                                                 43


[PAGINA 44]
                                         Strings - Exemplo
Exercício: Leia o nome de uma pessoa e abrevie da seguinte forma: Primeira letra do nome seguida de ponto(.)
mais o último sobrenome. Exemplo: José Luiz de Almeida Soares deve abreviar como: J.Soares
package main                                              // Parte 2 – Calcula o nome abreviado
                                                          if !s.Contains(nome, " ") { // Nome sem sobrenome
import (                                                    nomeAbreviado = string(nome)
  "bufio"                                                 } else {
  f "fmt“ // f é um alias para o package "fmt"              primeiraLetra = string(nome[0])
  "os“                                                      ultimoEspaco = s.LastIndex(nome, " ") + 1
  s "strings“ // s é um alias para “strings"                sobreNome = nome[ultimoEspaco:]
)                                                           nomeAbreviado = primeiraLetra + "." + sobreNome
                                                          }
func main() {                                             f.Println("Nome abreviado = ", nomeAbreviado)
  // Parte 1 – Declaração e leitura das variáveis     }
  var (
    nome, sobreNome string
    nomeAbreviado, primeiraLetra string
    ultimoEspaco int
  )
  f.Println("Digite o nome: ")
  scan := bufio.NewReader(os.Stdin)
  nome, _ = scan.ReadString('\n’)
                                                →
                                                                                                          44


[PAGINA 45]
                                                  Maps
A estrutura map, também conhecida como array associativo ou dicionário, é uma coleção não ordenada de pares
chave → valor (key-value) onde a chave não se repete. Pode-se fazer analogia remota com um array, no qual os
índices podem ser de qualquer tipo.
Vamos supor que desejássemos estabelecer um correspondência entre os estados do Brasil e suas siglas.
Poderíamos usar um map configurado da seguinte forma:

 São Paulo Minas Gerais Rio de Janeiro Espírito Santo              Valor (Value)
    SP         MG             RJ             ES                     Chave (Key)
Esse é um exemplo de um map onde a chave e seu valor são do tipo string.
Dessa forma temos, por exemplo, que à chave “MG” corresponde o valor “Minas Gerais”, ambos valores do tipo
string.

Em GO Podemos definir maps com chaves e valores de qualquer tipo. Além disso, a linguagem disponibiliza,
nativamente, uma série de funções para adicionar, localizar, deletar e manipular elementos de um map.

                                                    →

                                                                                                         45


[PAGINA 46]
                                       Operações com Maps
Declaração                                              estado[“SC”] = “Santa Catarina”
Podemos declarar e inicializar um map assim:
                                                  Neste exemplo adicionamos um novo estado no map.
estado := make(map[string]string)
                                                  Da mesma forma, podemos alterar qualquer valor pela
Aqui declaramos um map vazio com chaves e valores sua chave.
do tipo string
                                                  Acessando um valor de uma chave
estado := map[string]string{                      Basta indicarmos a chave:
    “SP": “São Paulo”,
    “MG”: “Minas Gerais”                                x,f := estado[“SC”]
    “RJ": “Rio de Janeiro”,
                                                       Neste exemplo, a variável x vai receber o valor “Santa
    “ES”: “Espírito Santo”,
}
                                                       Catarina” e a variável f o valor true

Aqui declaramos e atribuímos os pares. Repare a última Para deletar uma chave:
vírgula: isso não causa erro, é um padrão em GO.
                                                        delete(estado,”SC”)
Atribuição de valores para as chaves
Para atribuirmos ou adicionarmos um novo par para o
map, basta especificarmos a chave:                                                                        46


[PAGINA 47]
                                         Maps - Exemplo
Exercício: Leia uma quantidade indefinida de nomes de alunos e notas. Armazene-os em uma map com a chave
nome → nota. A leitura termina quando digitar o nome “fim”. Imprimir os alunos com nota maior que a média.
package main                                               if _, achou := mapNota[nome]; achou {
import (                                                     fmt.Println("Nome repetido! Redigite...")
  "fmt"                                                      continue
  s "strings"                                              }
)
                                                           fmt.Print("Informe a nota: ")
func main() {                                              fmt.Scanln(&nota)
  mapNota := make(map[string]float64)                      mapNota[nome] = nota
  var nota, soma, media float64 = 0, 0, 0                  i++
  var nome string = "nome"                                 soma += nota
  var i int = 0                                          } // Fim for
  for {                                                  media = soma / float64(i)
    fmt.Print("Informe o nome: ")                        fmt.Println("Média = ", media)
    fmt.Scanln(&nome)                                    for i, v := range mapNota {
    if s.ToUpper(nome) == "FIM" {                          if v > media {
      break                                                  fmt.Println(i, v)
    }                                                      }
                                                         }
                                                     }
                                                →
                                                                                                         47


[PAGINA 48]
                                                Structs
Uma struct é um tipo de dado composto heterogêneo definido pelo usuário composto por um conjunto de
variáveis, não necessariamente do mesmo tipo, denominados campos.

Podemos usar uma struct para definir estruturas complexas como, por exemplo, uma ficha de um funcionário ou
um produto de comércio eletrônico.
Representam um papel importante na linguagem, pois são a base para construções orientada a objetos, como
veremos em outro curso.

Além disso, o uso de structs em conjunto com slices, propiciam ferramentas para a construção de algoritmos
modulares, flexíveis e legíveis.




                                                                                                        48


[PAGINA 49]
                                       Operações com Structs
Declaração                                            Acessando os campos
Exemplo de uma struct para representar uma pessoa:    Usamos o separador “.” para acessar os elementos
                                                      individuais:
type struct regPessoa {
  nome string                                         pessoa.nome = “José”
  peso float64                                        pessoa.peso = 73
  altura float64                                      pessoa.altura = 1.76
}

Para declarar uma variável do tipo regPessoa, pode-se Ou para imprimir:
usar a função new():
                                                      fmt.PrintLn(pessoa.nome)
pessoa := new(regPessoa)                              fmt.PrintLn(pessoa.peso)
                                                      fmt.PrintLn(pessoa.altura)

Ou podemos instanciar e inicializar:
pessoa := regPessoa{
nome:   “José”,
peso:   73,
altura: 1.76,
}                                                                                                  49


[PAGINA 50]
                Fim da Temporada 4 – Consolidando o Conhecimento
Exercício: Crie uma struct para armazenar o nome, altura e peso ideal de uma pessoa. Depois crie um slice e
preencha seus elementos com structs do tipo pessoa. Leia os dados com uma repetição até ser digitado um nome
igual a “fim”. Calcule o peso ideal com base na fórmula: Peso ideal = 72.7 x altura - 58.0. Imprima o slice
package main                                  Leitura, cálculo e impressão do slice de pessoas
                                              for {
import (                                        f.Println("Digite o nome da pessoa: ")
  f "fmt"                                       f.Scanln(&nm)
  s "strings"                                   if s.ToUpper(nm) == "FIM" {
)                                                 break
                                                }
type regPessoa struct {                         f.Println("Digite a altura da pessoa: ")
  nome      string                              f.Scanln(&al)
  altura    float64                             pi = 72.7*al - 58.0 // Cálculo do peso ideal
  pesoIdeal float64                             pessoa := regPessoa{nome: nm, altura: al, pesoIdeal: pi}
}                                               pessoas = append(pessoas, pessoa)
                                              }
func main() {                                 for i, v := range pessoas {
  // Slice de regPessoa                         f.Println(i, v)
  pessoas := make([]regPessoa, 0, 10)         }
  var nm string // Nome da pessoa         }
  // Altura e peso
  var al, pi float64                →            Baixe este e outros exercícios resolvidos no GITHUB       50


[PAGINA 51]
Temporada 5




 Funções


[PAGINA 52]
                                                  Funções
Como vimos na apostila de algoritmos, uma função é uma técnica de modularização que consiste em encapsular
um bloco de código que possui uma determinada funcionalidade de tal modo que possa ser reutilizado por outros
módulos do sistema.
Em outras palavras, uma função é um trecho de código identificado por um nome e dedicado a resolver uma tarefa
específica, retornando ou não uma informação com base em alguns valores de entrada.
As funções em GO são first-class citizens, ou seja, elas podem ser atribuídas a variáveis, passadas como
argumento, imediatamente invocadas ou adiadas para execução.

Outras características:
 Pode, opcionalmente, receber parâmetros de entrada de diversos tipos.
 Retorna, opcionalmente, um ou mais valores de diversos tipos.
 Pode ser declarada dentro do próprio módulo que a chamou ou ficar em packages separados.
 Pode ser usada em expressões.
 Suporta valores de retorno nomeados, variadic functions e funções anônimas.



                                                                                                           52


[PAGINA 53]
                                                   Funções
A declaração de uma função pode conter as seguintes partes

<func> nome_função ([lista_declaração_parâmetros]) [(lista_tipos_retorno)] {
  ...
  [return <lista_variáveis_retorno>)]
}

•   A palavra reservado func indica que uma função vai ser declarada e é obrigatória
•   O nome da função (nome_função) pode ser em minúsculas ou Camel Case. Evite underscore.
•   A lista de parâmetros de entrada (lista_declaração_parâmetros) é uma lista de declaração de variáveis que
    serão usadas pela função e cujos valores serão fornecidos na chamada da função. São opcionais: podem haver
    funções que executam suas tarefas sem a necessidade de nenhuma informação externa.
•   A lista de tipos de retorno (lista_tipos_retorno) é uma lista de tipos válidos dos valores que serão retornados
    pela função. É opcional: existem funções que não retornam valores. Não existe o tipo void, como em C.
•   Se a função retornar algum valor, eles serão declarados através do comando return seguido dos valores de
    retorno.


                                                                                                                53


[PAGINA 54]
                                         Funções - Exemplo
Exercício: Crie uma função de nome soma que receba 2 valores e retorne a soma desses valores. No programa
principal leia dois números e calcule sua soma através da função criada.
package main
import f "fmt"

func main() {
  // Declaração e leitura dos números a serem somados
  n1, n2 := 0, 0
  f.Print("Digite o primeiro número: ")      Aqui chamamos a função soma e passamos 2 argumentos que
  f.Scan(&n1)                                são os números lidos. Os argumentos n1 e n2 serão atribuídos
  f.Print("Digite o segundo número: ")       aos parâmetros numero1 e numero2 da função definida
  f.Scan(&n2)                                abaixo e o retorno da função será atribuído à variável s
    // Cálculo da soma através da chamada à função
    s := soma(n1, n2) // Cálculo da soma através da função
    f.Printf("A soma entre %d e %d é %d", n1, n2, s)
}

// Definição da função soma                     Aqui definimos a função soma que recebe 2 parâmetros como
func soma(numero1, numero2 int) int {           entrada e retorna um único valor que é a soma dos valores
  return numero1 + numero2                      recebidos
}
                                                                                                            54


[PAGINA 55]
                          Funções com Múltiplos Valores de Retorno
Uma característica marcante na linguagem GO é que as funções podem retornar mais de uma valor. Em linguagens
como Java ou C isso não é possível, seria necessário retornar um vetor ou classe para essa finalidade.
Vejamos um exemplo: Em matemática, a divisão por zero não é permitida. Vamos fazer uma função que divida dois
números e retorne dois valores: Um valor float64 com o resultado da divisão e outro valor booleano indicando se
houve erro na divisão, caso o divisor seja 0 (zero):
func divisao(numero1, numero2 float64) (bool, float64) {
  erro := false
  result := 0.0                                                   A chamada da função ficaria assim:
  if numero2 == 0 {
    erro = true                                                      e, r := divisao(n1, n2)
  } else {                                                           if !e {
    result = numero1 / numero2                                         f.Println(“Resultado = ",r)
  }                                                                  } else {
  return erro, result                                                  f.Println(“Divisão não permitida")
}                                                                    }

Veja que a função divisao retorna dois valores: erro, valor booleano indicando se a divisão é possível, e result com
o resultado da divisão. Na chamada da função, atribuímos esses retornos para as variáveis e e r, respectivamente.
Assim, testamos o valor do erro para exibirmos a mensagem apropriada.
Caso seja desejável ignorar um dos retornos, usamos o identificador blank (underscore).
Exemplo:      _, r := divisao(n1, n2) // Nesse caso, ignoramos o retorno booleano de erro                          55


[PAGINA 56]
                       Funções Variádicas e Funções como Variáveis
Funções variádicas: Mais conhecidas como variadic functions são funções que aceitam um número
indeterminado de parâmetros. Na chamada da função pode-se passar os valores separados por vírgula ou através de
um slice. Como exemplo, faremos uma função soma que faça uma soma de vários valores passados como
argumentos:
func soma(nums ...int) int {
  result := 0                                           Exemplos de chamada da função:
  for _, n := range nums {
    result += n                                         fmt.Println(Sum()) // Retorna 0
  }                                                     fmt.Println(Sum(5)) // Retorna 5
  return result                                         fmt.Println(Sum(2, 5, 1)) // Retorna 8
}

Veja que, para declararmos, colocamos ... seguidos do tipo dos parâmetros.

Funções como variáveis: É possível atribuir uma função para uma variável e até passá-la como argumento para
uma outra função:
f := func() {
  fmt.Println(“Alô Mundo!")
}
f() // Vai imprimir “Alô Mundo!”
                                                                                                            56


[PAGINA 57]
                             Escopo de Variáveis e Tempo de Vida
                                          Visibilidade dentro do pacote

O escopo ou visibilidade de variáveis tem a ver com o princípio do ocultamento de informações e permite que
as variáveis só possam ser acessadas de dentro da função que as criou. Isso é mais seguro, pois evita que módulos
externos interfiram na lógica das funções.
A linguagem GO possui os seguintes escopos de variáveis:
• Global: São as variáveis declaradas fora de qualquer bloco ou função e são acessíveis em todo o pacote onde
    foram declaradas. O tempo de vida dessas variáveis se encerra quando o programa se encerra.
• Local: São variáveis declaradas dentro de uma função ou bloco de código e são vistas somente na função/bloco
    em que foram declaradas. O tempo de vida dessas variáveis se encerra quando a função/bloco se encerra
Obs: O escopo static não existe em GO.

                                           Visibilidade entre pacotes

Quando importamos um pacote, obtemos tem acesso a todas variáveis e funções desse pacote que possuam a
primeira letra maiúscula. Repetindo: o critério para que uma função seja acessível (visível) entre os pacotes é que
ela se inicie por uma letra maiúscula.
Repare as funções que estudamos até agora. Você não se perguntou porque usamos frm.Printf e não fmt.printf?
As funções que começam com letra minúscula são acessíveis somente no pacote e não são exportadas.                57


[PAGINA 58]
                       Escopo de Variáveis e Tempo de Vida
package main
import "fmt"

var v int = 7         // v é variável global vista em todo pacote
func main() {
  fmt.Println(v)      // Vai imprimir 7 → variável global
  {
    fmt.Println(v)    // Vai imprimir 7 → variável global
    v := 2
    fmt.Println(v)    // Vai imprimir 2 → variável local do bloco
  }
  fmt.Println(v)      // Vai imprimir 7 → Variável global
  f()
  // fmt.Println(x)   // Erro → x não é acessível
}

func f() {
  x := 5
  fmt.Println(x)      // Vai imprimir 5 na chamada da função → variável local
}
                                                                                58


[PAGINA 59]
                   Passagem de Parâmetro por Valor e por Referência
Existem duas formas de passarmos os valores dos argumentos para os parâmetros das funções:

•    Passagem por valor: o valor das variáveis dos argumentos não se alteram, mesmo que os parâmetros sejam
     modificado na função.
•    Passagem por referência: Os valores das variáveis dos parâmetros refletem nos argumentos.

Na linguagem GO, as variáveis passadas como argumentos para as funções são sempre passados por valor.
Para passamos valores por referência, podemos usar o operadores de referência (&) que vimos no estudo dos
ponteiros. Dessa forma passamos o endereço da variável.
    package main                  package main                     No primeiro exemplo, o valor de v foi
    import "fmt"                  import "fmt"                     passado por valor e a função incrementa
    func main() {                 func main() {                    não vai funcionar.
      v := 0                        v := 0                         Já no segundo exemplo, o valor de v foi
      incrementa(v)                 incrementa(&v)                 passado por referência e seu valor foi
      fmt.Println(v) // 0           fmt.Println(v) // 1            incrementado para 1 corretamente.
    }                             }
    func incrementa(x int) {      func incrementa(x *int) {
      x++                           *x++
    }                             }
                                                                                                        59


[PAGINA 60]
                 Fim da Temporada 5 – Consolidando o Conhecimento
Exercício: Crie uma função para calcular as raízes de uma equação do segundo grau pela fórmula de Bhaskara. O
retorno da função será um slice com as raízes. Caso o slice retorne vazio significa que equação não possui raízes
reais.
package main                                  if len(r) == 0 {
                                                f.Println("Equação não possui raízes reais")
import (                                      } else if len(r) == 1 {
  f "fmt"                                       f.Println("x = ", r[0])
  m "math"                                    } else {
)                                               f.Printf("x1 = %f e x2 = %f\n", r[0], r[1])
                                              }
func main() {                               } // Fim main
  var a, b, c float64                       func bhaskara(a, b, c float64) []float64 {
  f.Print("Digite o coeficiente a: ")         raizes := make([]float64, 0, 10)
  f.Scan(&a)                                  delta := b*b - 4.0*a*c
  f.Print("Digite o coeficiente b: ")         if delta == 0 {
  f.Scan(&b)                                    raizes = append(raizes, -b/(2.0*a))
  f.Print("Digite o coeficiente c: ")         } else if delta > 0 {
  f.Scan(&c)                                    raizes = append(raizes, (-b+m.Sqrt(delta))/(2.0*a))
  r := bhaskara(a, b, c)                        raizes = append(raizes, (-b-m.Sqrt(delta))/(2.0*a))
                                       →      }
                                              return raizes
Baixe os exercícios resolvidos no GITHUB    }
                                                                                                              60


[PAGINA 61]
                                           Exercícios Propostos
1) Um sistema de equações lineares como:                   pode ser resolvido segundo:             e


Escreva um algoritmo em GO que lê os coeficientes a,b,c,d,e e f e calcule de x e y.

2) Escreva um algoritmo em GO que leia 3 números inteiros e mostre o maior deles.

3) Leia um número N e escreva os N número maiores que N.
Exemplo: N = 4 → Escrever: 5,6,7,8

4) Leia um número N inteiro e calcule S = 1 – 1/2 + 1/3 – 1/4 + ... +/- 1/N

5) Leia um número inteiro N e um vetor (array ou slice) com números reais e Calcule o produto escalar entre o
número N e o vetor.

6) Escreva uma função em GO para verificar se uma palavra informada pelo usuário é um palíndromo ou não.
                                                                                                                61


[PAGINA 62]
                                         FIM
                                          Obrigado!


Neste curso fizemos uma pequena introdução à linguagem GO com o objetivo de dar
condições ao aluno para se aprofundar nos estudos e nos assuntos não abordados aqui, tais
como:
 GO Routines (Threads) e tratamento de erros
 Orientação a objetos
 Estruturas de dados complexas
 Bancos de dados e WEB
Veja a bibliografia a seguir para mais informações.


[PAGINA 63]
                                      Saiba mais...
Links
 TutorialsPoint
 Geeks for Geeks
 A Tour of GO
 GO by Example



Livros
 The Little Go Book
 Essencial GO



Exercícios resolvidos e outros recursos
 GitHub
 http://www.josecintra.com/blog
                                                      63
