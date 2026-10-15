# UNIVERSIDADE_TECNOLOGICA_FEDERAL_DO_PARA

Arquivo original: most_similar_papers_to_this_one/UNIVERSIDADE_TECNOLOGICA_FEDERAL_DO_PARA.pdf
SHA-256 do original: 7c4b9455726d7129ea3b6b9edaf7b441de58a7cf6d5c902d7bfb17f3853b0b49

Texto extraido para consulta. As paginas abaixo usam a ordem do arquivo PDF, incluindo capas.
Parte preparada: 1/1


[PAGINA 1]
                           PR
UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ




                              REVISÃO
                           PROGRAMAÇÃO
                        ORIENTADA A OBJETOS
                          UTILIZANDO JAVA




                                             Prof. Cesar Augusto Tacla
                                                  Departamento Acadêmico de Informática
                                                  ht t p : / / w w w . d ai nf . c ef et pr . br / ~ t ac l a


[PAGINA 2]
O uso e reprodução desta apostila
requerem autorização expressa do
autor.




                                    2


[PAGINA 3]
            !" #
             $%&' (&)*$
        +     $      *
            !*)     #* (& * * #* $ ,$% &
              % ' #* -& ./*                                                                                                                                         0

            1       !    2 !
            3.1.1   Sobrecarga ...................................................................................................................................... 9
            3.1.2   Sobreposição/Reescrita (override) ................................................................................................ 10
            3.1.3   Princípio da substituição ............................................................................................................... 11


    +                    3       4         2

            1&% *
            -   ( #&#*

                (& * $ * $&
                (& * &$ $5&#&    . %&
                (& * &$ $5&#& ( %& * &$6$ )&
                                  !
    0           & &% * 7       %& #* *8./* '& & ) ' 8*                                       #*        9 :& *                                                       0
                        "                      #
    ;        <%*=>                                                                                                                                                  ;
    ;         ' #* *<%*=>                                                                                                                                           ;
    ;         & & <%*=?*
    ;+       &$=& <%*=?*
$       "    %




                                                                                                                                                                    3


[PAGINA 4]
Um objeto representa uma entidade concreta (ex. produto em estoque) ou abstrata (transação
bancária, histórico, taxa de juros) do mundo real. Também pode ser algo necessário ao funcionamento
do sistema sem uma ligação forte com uma entidade do mundo real.
Um objeto num sistema possui três propriedades:
   Estado: definido pelo conjunto de propriedades do objeto (os atributos) e de suas relações com os
  outros objetos, muda com o tempo. Ex. objeto turma pode estar aberta ou fechada – passa ao estado
  fechada quando 10 alunos fizerem a inscrição.
   Comportamento: como um objeto responde às solicitações dos outros e tudo mais o que um objeto
  é capaz de fazer. É implementado por um conjunto de operações. Ex. objeto turma pode ter
  operações acrescentar aluno ou suprimir aluno.
   Identidade: significa que cada objeto é único no sistema. Por exemplo, o objeto turma Tecno-OO
  manhã é diferente do objeto Tecno-OO tarde.




                                                                                          .
Figura 1. Notação de objeto em UML




Uma classe é uma descrição de um conjunto de objetos com propriedades, comportamento,
relacionamentos e semântica comuns. Uma classe pode ser vista como um esqueleto/modelo para criar
objetos.

Exemplo: classe turma
Atributos: sala, horário
Operações: obter local, adicionar estudante, obter horário

Dicas
    Classes devem encerrar uma só abstração do mundo real. Por exemplo, uma classe estudante
   contendo também o histórico do estudante não é boa. Melhor é dividi-las em duas: estudante e
   histórico estudante.
    Utilize substantivos para nomear as classes
    Podem-se suprimir os atributos e os métodos deixando somente os compartimentos.
    Em UML, classes abstratas são grafadas em itálico




Figura 2. Notação UML para classe.




                                                                                                  4


[PAGINA 5]
       &'()*&+,
Sintaxe para declaração de um atributo em UML:


                    [<visibilidade>]<nome>[<multiplicidade>]:[<tipo>][=<valor inicial>]


    <visibilidade>:
         + = público
         - = privada, somente métodos da classe podem acessá-lo
         # = protegido, métodos da classe e das classes derivadas podem acessá-lo
         ~ = pacote, métodos das classes presentes no mesmo pacote podem acessá-lo
    <nome>: nome do atributo
    <multiplicidade>: por exemplo, valores[5] ou matriz[4, 6]
    <tipo>: Pode-se utilizar os tipos da linguagem de implementação. Por exemplo, char, float ou int.
    <valor inicial>: valor inicial para o atributo que respeite o tipo de dado.

Exemplos
- nome[30]: char
- sexo: char=’f’
+ código: int=20


        -&+.+,
Sintaxe para declaração de um atributo em UML:


                           [<visibilidade>]<nome>(<lista argumentos>):[<tipo>]


    <visibilidade>:
         + público
         - privada, somente métodos da classe podem acessá-lo
         # protegido, métodos da classe e das classes derivadas podem acessá-lo
         ~ pacote, métodos de classes presentes no mesmo pacote podem acessá-lo
    <nome>: nome do método
    <lista de argumentos>: (<nome_argumento>:<tipo>, ..., <nome_argumento><tipo>). Por exemplo,
    (nome:String, idade: int)
    <tipo>: Tipo do dado retornado. Pode-se utilizar os tipos da linguagem de implementação. Por
    exemplo, char, float ou int.

Exemplos
- calcularIdadeEmMeses(Data data_nasc): int
+moverPara(x:int, y:int):void


       /012,*3145/&+
Encapsular num só objeto atributos (dados) e operações permite esconder os detalhes internos de
funcionamento do objeto. Podemos definir, por exemplo, que os atributos não são visíveis (privados) e
que certos métodos os modificam. Também, podemos definir que somente alguns dos métodos dos
objetos de uma classe são visíveis (métodos públicos), os demais seriam para o funcionamento interno
do objeto.




                                                                                                        5


[PAGINA 6]
         +/,&'*&+'5,
São métodos especiais que servem para criar uma instância de uma classe. Pode haver vários métodos
construtores variando-se os argumentos (polimorfismo por sobrecarga). Por exemplo, uma classe
círculo pode oferecer três modos de instanciação: um, pelo centro e raio, por circunscrição e inscrição
num quadrado cuja diagonal é uma reta de x1, y1 a x2, y2 como ilustra a figura 3.
1    import java.lang.Math.*;
2    class Circulo {
3       public float xCentro;
4       public float yCentro;
5       public float raio;
6
7        // Construtora centro + raio
8        Circulo (float x, float y, float r) {
9           xCentro = x;
10          yCentro = y;
11          raio = r;
12       }
13       // Construtora para círculo inscrito num quadrado
14       // assume que abs de x2 é maior que abs de x1
15       Circulo (float x1, float y1, float x2, float y2) {
16          xCentro = (x1 + x2)/2;
17          yCentro = (y1 + y2)/2;
18          raio = Math.abs(x2 - x1)/2;
19       }
20
21       // Construtora para círculo circunscrito num quadrado
22       // assume que abs de x2 é maior que abs de x1
23       Circulo (float x11, float y11, float x22, float y22) {
24          xCentro = (x11 + x22)/2;
25          yCentro = (y11 + y22)/2;
26          raio = Math.abs(x22 - x11)/2;
27       }
28       // outros métodos aqui ...
29   }

Figura 3: exemplo de utilização de várias construtoras.


         54)'+, .5 31,,5 5 .5 /,&6/0(1
Atributos membros de classe são comuns a todos os objetos instâncias de uma mesma classe, ou seja,
um atributo estático é único para todos os objetos instâncias de uma classe. Um método estático
também é um membro de classe e pode ser executado sem que haja um objeto instanciado. Por
exemplo, os métodos da classe Math da API Java são todos statics (java.lang.Math,
http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Math.html). Na Figura 13, observe que nas chamadas
aos métodos Math.pow e Math.sqrt não há objeto instanciado.
Um método estático não pode chamar um método não-estático da mesma classe. De outra forma, um
método de classe não pode chamar um método de instância, pois não há objeto instanciado. Um
método de classe também não pode fazer referências a atributos de instância pelo mesmo motivo. Por
exemplo, na Figura 4, o compilador acusa o seguinte erro na linha 9: non-static method imprimir() cannot
be referenced from static context.
30   public class ImprimirStrings {
31      String str = “atributo-nao-estatico”;
32      public void imprimir() {
33         String a = new String(“abcdef”);
34         String b = new String(“xyz”);
35         System.out.println(a.concat(b));
36      }
37      public static void main(String[] args) {
38         imprimir();
39      }
40   }

Figura 4. Métodos e atributos não-estáticos não podem ser referenciados em contextos estáticos.




                                                                                                       6


[PAGINA 7]
Se fizermos referência ao atributo não-estático str no método main ou no imprimir obtermos o seguinte
erro de compilação: non-static variable str cannot be referenced from static context. Podemos fazer
referência a métodos e atributos não estáticos de outros objetos.
Não devemos abusar de métodos estáticos porque um programa que utiliza somente métodos de
classe não é orientado a objetos (não há objetos). A Figura 5 mostra um exemplo adicional de método
estático e a Tabela 1 resume o vocabulário do assunto.
1    public class Circle {
2      static final double PI = 3.14159;
3      public static double calculaArea(double raio) {
4        return PI * ( raio * raio );
5      }
6    }
7
8    // um método qualquer
9           ...
10    double circleArea = Circle.calculaArea(5); // utilizamos o nome da classe

Figura 5: exemplo de método estático.
TABELA 1:VOCABULÁRIO DE MÉTODOS E ATRIBUTOS ESTÁTICOS
                   De classe                                       De instância
Método             É um método static, não necessita de objeto     É um método não static, necessita de
                   para ser chamado.                               objeto para ser chamado.
Atributo           É um atributo static, existe um só para         É um atributo static, há uma cópia
                   todos os objetos da classe.                     para cada objeto instanciado.


         ,0+2+ .5 1'(785(,
As variáveis existem somente dentro do bloco em que foram definidas, sendo que um bloco é
delimitado por chaves. Na figura 6, temos os seguintes escopos:
     num: atributo de instância existe em todos os métodos da classe (chaves pretas);
     res: atributo de instância existe em todos os métodos da classe (chaves pretas);
     n: argumento do método calcular; existe da linha 5 a 17 (chaves vermelhas);
     res: variável auxiliar declarada na linha 8; existe da linha 8 a 17 (chaves azuis);
     i: variável auxiliar do for; existe nas linhas 9 e 10
1        public class Fatorial {
2           private int num = 0;        // último número calculado
3           private int res = 1;        // último resultado obtido
4
5            public int calcular(int n) {
6               if (n == num) return res;
7               else {
8                     int res = 1;
9                     for (int i=n; i>0; i--)
10                         res = i * res;
11
12               // guarda resultado
13               this.res = res;
14               num = n;
15               return res;
16           }
17       }
18   }
Figura 6: escopo de variáveis (JexemploEscopoVariaveis).

 +4)'5145/&+. Quando um argumento ou uma variável de um método possui nome idêntico a um
atributo (variável res na figura 6) então é preciso utilizar a palavra reservada this para fazer referência
ao atributo. Isto é chamado de sombreamento ou ocultação do atributo pela variável de método.




                                                                                                          7


[PAGINA 8]
É um mecanismo típico de OO para definir classes que compartilham definições de métodos e de
atributos. Isto é feito quando classes apresentam parte do comportamento e da descrição de estado
similares e parte específica.
Por exemplo, num editor gráfico trabalhamos com duas formas geométricas: polígonos regulares e
círculos. Polígonos e círculos têm parte do comportamento similar, podemos movê-los, redesenhá-los,
calcular área e perímetro, e parte específica, polígonos podem ser rotacionados enquanto que círculos
não necessitam deste comportamento. Polígonos podem ser descritos da mesma forma: número de
lados, tamanho do lado, raio da circunferência inscrita (apótema) e centro do polígono. Embora os
círculos tenham centro e raio, não possuem número de lados nem tamanho do lado.
No exemplo em questão, temos uma classe base denominada forma geométrica. Uma classe derivada
herda métodos e atributos da classe base. Portanto, as classes polígono e círculo herdam os métodos e
atributos definidos na classe base. Uma classe derivada pode ser a classe base de outra, constituindo
assim uma relação de hierarquia entre as classes. Por exemplo, a classe polígono pode ser base de uma
classe retângulo, triângulo e outras. Esta técnica diminui os esforços de codificação assim como a
quantidade de código, pois operações comuns às classes são definidas uma só vez.
1    class Ponto {
2       public double x;
3       public double y;
4
5        Ponto(double x, double y) {
6           this.x = x;
7           this.y = y;
8        }
9        public double calcularDist(Ponto p) {
10          return (Math.sqrt(Math.pow(p.x - x, 2.0) + Math.pow(p.y - y, 2.0)));
11       }
12   }
13
14   class Circulo extends FormaGeometrica {
15      Circulo(Ponto c, double r) {
16         centro = c;
17         raio = r;
18      }
19      public double CalcularArea() {
20         return (Math.PI * Math.pow(raio, 2));
21      }
22      public double CalcularPerimetro(){
23         return (2 * Math.PI * raio);
24      }
25      public void Redesenhar() {
26         // não implementada
27         System.out.println("figura redesenhada");
28      }
29   }
30   class Poligono extends FormaGeometrica {
31      public int numLados;
32      public double tamLado;
33      public double angRotacao=0;
34      Poligono(int n, double tam, Ponto c, double r) {
35         numLados = n;
36         tamLado = tam;
37         centro = c;
38         raio = r;
39      }
40      public double CalcularPerimetro() {
41         return (numLados * tamLado);
42      }
43      public double CalcularArea() {
44         return (raio * CalcularPerimetro() / 2);
45      }
46      public double Rotacionar(double incremento) {
47         angRotacao = Math.IEEEremainder(angRotacao+incremento, 360.0);
48         return angRotacao;
49
50       }



                                                                                                    8


[PAGINA 9]
51      public void Redesenhar() {
52         // não implementada
53         System.out.println("figura redesenhada");
54      }
55   }
56   public abstract class FormaGeometrica {
57      public Ponto centro;
58      public Double raio; // para polígonos, é o raio inscrito (apótema)
59      public abstract double CalcularArea();
60      public abstract double CalcularPerimetro();
61      public abstract void Redesenhar();
62      public void moverPara(Ponto novoCentro) {
63         centro = novoCentro;
64         Redesenhar();
65      }
66   }

Figura 7: Exemplo de herança.

A representação em UML do exemplo acima fica:




Figura 8: representação de herança em UML – polígono e círculo são classes derivadas de
   FormaGeométrica.

 5'1/91 4:3&(231. Não há herança múltipla em Java (uma classe deriva de duas ou mais classes base
que não sejam de interface), mas podemos simulá-la utilizando classes com o modificador interface.
 +/,&'*&+'5,. Métodos construtores não são herdados pelas classes derivadas, mas um construtor de
uma classe base é chamado implicitamente antes da primeira linha do construtor da classe derivada.
 *25'. É possível chamar um método tal qual foi definido na classe base utilizando a sintaxe:
super.<método>(<lista argumentos>) . Se utilizar somente super(<lista argumentos>) então chama-se a
construtura da classe base (esta última opção só pode ser utilizada na primeira linha de um método
construtor).


                 ;
Métodos podem ser redefinidos de duas maneiras: pela mudança de seus argumentos (sobrecarga) ou
por sobreposição/reescrita do corpo presevando a mesma assinatura.

         +)'501'<1
São métodos com mesmo nome, mas com assinaturas diferentes (lista de argumentos diferentes). A
sobrecarga pode ocorrer numa mesma classe ou entre classe derivada e classe base. Em Java, se dois
métodos tiverem mesmo nome e mesmos argumentos diferindo apenas no valor de retorno ocorre um
erro de compilação. A figura 9 mostra um exemplo correto de sobrecarga (Somador) e outro incorreto



                                                                                                      9


[PAGINA 10]
(AoQuadrado). Na classe AoQuadrado o compilador aponta que o método elevarQuadrado(float) já foi
definido na classe.
1    public class Somador {
2          public int somar(int a, int b) {
3             return a+b;
4          }
5          public int somar(float a, float b) {
6             return a+b;
7       }
8    }


1        public class AoQuadrado {
2             public float elevarQuadrado(float a) {
3                return a*a;
4          }
5             public double elevarQuadrado(float a) {
6                return (double)a*a;
7             }
8    }
Figura 9: Exemplos de sobrecarga de métodos (correto e incorreto) – JExemploPolimorfismoSobrecarga.

              +)'52+,(9=+> 55,0'(&1 ?+85''(.5@
A sobreposição ocorre quando um método de uma classe base é reescrito na classe derivada. O
método reescrito tem a mesma assinatura que o método da classe base. Assinatura significa mesmo
nome, mesma lista de argumentos e mesmo valor retornado.
1        class ClienteEspecial extends Cliente {
2             ClienteEspecial(double desc) {
3                desconto = desc;
4             }
5             // Sobreposição do método calcularDesconto da classe base Cliente
6             public double calcularDesconto(double valor) {
7                return valor * desconto;
8             }
9          }
10
11   public class Cliente {
12      protected double desconto=0.1; // 10%
13      public double calcularDesconto(double valor) {
14         if (valor > 500)
15            return valor * desconto;
16         else
17            return 0.0;
18      }
19
20        public static void main(String args[]) {
21           Cliente cli[] = {new Cliente(),                     // cli[0]
22                            new ClienteEspecial(0.15)};        // cli[1]
23
24             for (int i=0; i < 2; i++)
25                System.out.println(cli[i].calcularDesconto(100));
26        }
27   }
Figura 10: Exemplo de sobreposição de método (JExemploPolimorfismoSobreposicao).
 5,&'(9A5, B ,+)'52+,(9=+. Alguns métodos não podem ser sobrepostos em função dos modificadores
que recebem:
     final: um método final nunca muda, todas as classes derivadas utilizam a mesma implementação.
     As chamadas aos métodos finais são resolvidas em tempo de compilação (vinculação estática).
     Static: é implicitamente um método final.
     private: são implicitamente finais, porque não podem ser sobrescritos nas classes derivadas
     (embora seja possível escrever um método com mesma assinatura numa classe derivada).




                                                                                                      10


[PAGINA 11]
         '(/0C2(+ .1 ,*),&(&*(9=+


                Um objeto de uma classe derivada é tratado como se fosse objeto da classe base.


Observe que no método main (figura 10) são criadas duas instâncias de cliente, um normal outro
especial. As duas instâncias são colocadas num vetor da classe Cliente, i.e., o cliente especial é tratado
como se fosse um objeto da classe Cliente todas as vezes em que for referenciado por meio da variável
cli[1].
Late Binding (vinculação ou associação dinâmica). A pergunta que se faz é: qual o método
calcularDesconto será chamado para a instância armazenada em cli[1]? O método da classe Cliente ou
da classe ClienteEspecial? A resposta é: o método da classe ClienteEspecial. Em tempo de execução, o
tipo real do objeto armazenado na variável (cli[1]) determina o método a ser chamado. Isto é chamado
de late binding, ou seja, associação dinâmica.




 31,,5 1),&'1&1 Não admite instâncias, não pode ser instanciada. Normalmente são classes bases que
contêm atributos e comportamentos comuns às classes derivadas.
  -&+.+ 1),&'1&+ Um método abstrato é apenas uma declaração significando que ele deverá ser
implementado numa classe derivada concreta (figura 11). Se isto não for feito, a classe derivada deve
ser declarada como abstrata.
Não podem ser declarados como métodos abstratos:
   Métodos construtores: os construtores não são herdados, logo um método construtor abstrato
   nunca seria implementado.
   Métodos static: métodos static não podem ser sobrepostos pelas classes derivadas, logo um
   método static abstrato nunca seria implementado.

1      abstract class Veiculo {
2       public int cavalos;
3       public abstract double calcularIPVA();
4       public abstract static void incrementarVeiculos(); // erro: combinação ilegal
5        public abstract Veiculo(); // erro: modificador abstract não permitido
6      }
7      class Carro extends Veiculo {
8           public double calcularIPVA() {
9              return (cavalos * 100);
10      }
11    }

Figura 11: Exemplo de método abstrato.


                             ;
Uma classe de interface define um contrato que deve ser seguido pelas classes que a implementam.
Uma classe interface é uma classe abstrata onde todos os métodos são implicitamente abstratos e
públicos e todos os atributos são implicitamente públicos, estáticos e finais.



A palavra-chave final pode ser associada a um método ou atributo. Se for associada a um método,
indica que ele não pode ser redefinido. Se for associada a um atributo, indica que seu valor não pode
ser modificado depois de ser inicializado. A inicialização de um atributo final pode ser feita na sua
declaração ou num método construtor. A Figura 12 ilustra um exemplo de utilização de uma classe
interface.



                                                                                                       11


[PAGINA 12]
1    interface IPVA {
2    // definimos algumas constantes (implicitamente são static final e declaramos
3    // um método abstrado calcular IPVA
4       Boolean CARRO_PASSEIO = true,
5             CARRO_UTILITARIO = false;
6       double CTE_UTILITARIO = 0.75,
7             CTE_PASSEIO = 1.0;
8       double VALOR_BASE = 500.00;
9       public double calcularIPVA();
10   }
11
12   class Carro implements IPVA {
13      Boolean tipoCarro=CARRO_PASSEIO;
14      String placa = new String("ABC1010");
15      public double calcularIPVA() {
16         if (tipoCarro==CARRO_PASSEIO)
17            return VALOR_BASE * CTE_PASSEIO;
18         else
19            return VALOR_BASE * CTE_UTILITARIO;
20      }
21   }
22   class Caminhao implements IPVA {
23      String placa = new String("CCC1010");
24      public double calcularIPVA() {
25         return 2 * VALOR_BASE * CTE_UTILITARIO;
26      }
27   }
28
29   public class ExemplificarInterface {
30      // A classe IPVA homogeiniza a execução do método calcularIPVA. Aqui não
31      // sabemos se o objeto é um carro ou um caminhao, mas como ambas as classes
32      // são obrigadas a implementar o método em questão podemos chamá-lo sem
33      // conhecer a classe do objeto.
34      public static void main(String args[]) {
35         IPVA veiculos[] = {new Carro(), new Caminhao()};
36         for (int i=0; i < veiculos.length; i++)
37            System.out.println(veiculos[i].calcularIPVA());
38      }
39   }

Figura 12 : exemplo de classe interface para definir métodos abstratos.
Observe que classes do tipo interface podem ser utilizadas para definir constantes (linhas 4-9, Figura 12).
Note também a aplicação do princípio da substituição na linha 35, uma instância da classe carro (classe
derivada) é referenciada como sendo um objeto de IPVA (classe base). O mesmo vale para o caminhão.

Runnable e Serializable são classes de interface bem conhecidas da API JAVA




Pode-se aplicar os seguintes modificadores de visibilidade a classes, métodos e atributos: público,
protegido, privado e default (de pacote ou friendly). Os três primeiros devem ser definidos
explicitamente e default é implícito. Nem todos podem ser aplicados indistintamente às classes,
métodos e atributos. Por exemplo, o modificador protegido (protected) não é aplicável a classes. Antes
de estudá-los em maior profundidade, é necessário conhecermos o conceito de pacotes.


        10+&5,
Servem para organizar o código, por exemplo, agrupar classes correlatas.
Vamos supor uma classe ponto pertencente ao pacote formas. A classe ponto é internamente nomeada
por formas.ponto. Assim se você estiver utilizando numa aplicação pacotes desenvolvidos por pessoas
(empresas) diferentes, há menos risco de haver coincidência de nomes de classes.
 5031'19=+ D181: package formas;
Se você não declarar o pacote, a classe pertence automaticamente ao pacote default que é o diretório
corrente.



                                                                                                              12


[PAGINA 13]
Para incluir um pacote num código faz-se:
import formas.*; //inclui todas as classes definidas no pacote formas
import formas.ponto; // inclui uma classe específica


         (,()(3(.1.5
Pode ser aplicada às classes, atributos e métodos. Se nada for definido pelo programador (default), as
visibilidades destes elementos são restritas aos membros que fazem parte do mesmo pacote (os
pacotes podem ser vistos como diretórios).
A visibilidade pública modifica a visibilidade default, permitindo que todos os membros do mesmo
pacote ou de outros pacotes enxerguem o que for público.
      'E*(8+ D181: pode conter somente uma classe pública que deve ter o mesmo nome que o
     arquivo. As demais classes (friends) de um arquivo .java possuem a visibilidade padrão (pacote).
      *)3(0: todos os objetos do mesmo ou de outros pacotes podem enxergar classes, atributos ou
     métodos públicos.
      '+&50&5.: atributos protected têm visibilidade restrita à própria classe e às classes derivadas.
     Objetos de classes do mesmo pacote também enxergam atributos protegidos.

       '(81&5: atributos e métodos private são visíveis pelas instâncias de uma mesma classe. Instâncias de uma
     classe derivada não conseguem acessar os atributos e métodos definidos como private na classe base. Exemplo:
1        // Testar visibilidade privada de métodos e atributos
2
3        class Ponto { // esta classe só é visível neste pacote
4           private double x;
5           private double y;
6
7            Ponto(double x, double y) {
8               this.x = x;
9               this.y = y;
10       }
11       private double obterX() {
12          return x;
13       }
14       public double calcularDist(Ponto p) {
15          // O objeto que executa este método pode acessar os atributos privados x e y
16          // do objeto passado como argumento, pois são instâncias da mesma classe.
17          return (Math.sqrt(Math.pow(p.x - x, 2.0) + Math.pow(p.y - y, 2.0)));
18       }
19    }
20    public class FormasGraficas {
21       public static void criarPontos() {
22          Ponto ptoA = new Ponto(2, -6);
23          Ponto ptoB = new Ponto(5, -2);
24          System.out.println("distancia=" + ptoA.calcularDist(ptoB));
25          // Se a linha abaixo for incluída, o erro de compilação seguinte ocorre:
26          // x has private access in Ponto
27          // System.out.println("Coordenada x:"+ptoA.x);
28       }
29       public static void main(String[] args) {
30          criarPontos();
31       }
32    }

Figura 13: Exemplo de atributo privado.


 (,()(3(.1.5 5 5'1/91
Os membros de uma classe base quando herdados por uma classe derivada, levam consigo a
visibilidade. Assim, se um atributo ou método é público na classe base também o será na derivada. O
compilador acusa erro de sintaxe se tentarmos sobrescrever um método com um modificador de acesso mais
restrito que o original.



                                                                                                              13


[PAGINA 14]
    (,()(3(.1.5 5 +/,&'*&+'1,
Construtoras podem receber modificadores de visibilidade. Se uma construtora for definida como
private então a classe deve ter um método estático público que permita criar instâncias. Exemplo:
1         // Testar visibilidade privada de métodos construtores
2
3         public class Semaforo {
4            private int estado;
5            private String[]={“vermelho”, “verde”, “amarelo”};
6
7             private Semaforo() {
8                estado = 0;
9             }
10            public static Semaforo instanciar() {
11               return (new Semaforo());
12            }
13        }




Em Java, é possível codificar classes dentro de outras classes. Estas classes podem ser static ou não
static. Classes não estáticas aninhadas são denominadas classes internas como ilustra a figura 14.
1     class Externa {
2        ...
3        class Interna {
4            ...
5        }
6        class static AninhadaEstatica {
7            ...
8        }
9     }
Figura 14: classes aninhadas
Restrições:
      Classes externas somente podem ter visibilidade de pacote (default) ou pública
      Classes internas são membros de classe e como tal podem ser públicas, protegidas, privadas ou
      de pacote.
      Classes aninhadas estáticas, assim como os métodos estáticos, não podem referenciar diretamente
      variáveis ou métodos de instância da classe externa. Uma classe estática aninhada funciona
      exatamente como outra qualquer não aninhada. Só é colocada dentro de outra por razões de
      encapsulamento.
TABELA 2: COMPARAÇÃO ENTRE CLASSE ANINHADA E ANINHADA STATIC.
                                 Interna (não static)      Aninhada Static
Necessário instanciar objeto
                                 SIM                       NÃO
da classe externa?
Classe interna tem acesso a
atributos e métodos de           SIM                       NÃO
instância da classe externa?
Um objeto da classe interna
tem implicitamente uma
                                 SIM                       NÃO (não há objeto)
referência ao objeto da sua
classe externa?




                                                                                                        14


[PAGINA 15]
         31,,5 (/&5'/1
A figura 15 mostra um exemplo de uma classe aninhada interna. A classe Ponto é interna à classe
JLinha. Observar que dentro da classe Ponto é possível acessar o atributo idLinha (privado em JLinha)
sem referência a um objeto JLinha.
1    public class JLinha {
2       private static int totLinha=0;
3       private int idLinha;
4       protected Ponto pt1;
5       protected Ponto pt2;
6
7        public JLinha(int x1, int y1, int x2, int y2) {
8           idLinha = ++totLinha;
9           pt1 = new Ponto(x1, y1);
10          pt2 = new Ponto(x2, y2);
11       }
12       public JLinha() {
13          idLinha = ++totLinha;
14       }
15
16       public class Ponto {
17          protected int x;
18          protected int y;
19
20           protected Ponto(int x, int y) {
21              this.x = x;
22              this.y = y;
23           }
24           protected String pontoStr() {
25              return "(" + x + ", " + y + ")";
26           }
27
28           protected String pontoStrComId(){
29              return "Linha " + idLinha + " " + pontoStr();
30           }
31       }
32   }
Figura 15: Exemplo de classe aninhada interna: Ponto.

A figura 16 mostra duas formas de se instanciar uma classe interna. Na primeira, a construtora da
classe externa realiza a instanciação da classe interna. Na segunda forma, a instanciação é feita fora da
classe externa. Observar que a chamada de new está atrelada a existência de um objeto da classe Linha
armazenado em l2 já que um objeto de uma classe interna existe somente associado a uma instância da
classe externa.
1    public class JMain {
2       public static void main(String args[]) {
3          // duas formas de instanciar pontos
4
5            // Forma 1: a construtora de linha instancia dois pontos
6            JLinha l1 = new JLinha(5, 15, 7, 17);
7
8            System.out.println(l1.pt1.pontoStr() + " " + l1.pt2.pontoStr());
9
10           // Forma 2: instancia-se linha e depois os pontos
11           JLinha l2 = new JLinha();
12           JLinha.Ponto p1 = l2.new Ponto(10, 10);
13           JLinha.Ponto p2 = l2.new Ponto(20, 20);
14           l2.pt1 = p1;
15           l2.pt2 = p2;
16           System.out.println(l2.pt1.pontoStrComId() + " " + l2.pt2.pontoStrComId());
17       }
18   }
Figura 16: Exemplo de utilização de classe aninhada interna.


Uma aplicação típica de classes internas é a navegação por iterator (classe interna) em um conjunto de
objetos ou de tipos primitivos armazenados em um array na classe externa. Um exemplo disso pode
ser visto em http://java.sun.com/docs/books/tutorial/java/javaOO/innerclasses.html.



                                                                                                      15


[PAGINA 16]
         31,,5, 1/(/F1.1, ,&7&(01,
Classes aninhadas estáticas podem ser bastante úteis para testes. O exemplo seguinte ilustra esta
aplicação para testes de limites de uma classe que simula o funcionamento de um radar de velocidade.
O radar aplica multas para velocidades superiores a 10% da velocidade máxima para a qual foi
configurado. Após compilar o código da figura 17, são geradas os arquivos JRadar.classe e
JRadar$TesteJRadar.
1    // JAVARepositorio\JRevisaoOO\JExemClasseAninhadaEstaticaRadar
2    // Este programa demonstra como utilizar uma classe aninhada
3    // estatica para testar uma classe. Depois da fase de testes
4    // a classe aninhada pode ser desprezada.
5    // Para executar fazer: java -cp . JRadar$TesteJRadar
6
7    public class JRadar {
8       private int velocidadeMaxima;
9
10       public JRadar(int v) {
11          velocidadeMaxima = v;
12       }
13       public Boolean multar(int v) {
14          // multar return true qdo a velocidade detectada pelo
15          // radar excede em 10% a velocidade maxima;
16          if (v > (velocidadeMaxima * 1.1))
17             return true;
18          else
19             return false;
20       }
21
22       public static class TesteJRadar{
23          public static void main(String args[]) {
24             JRadar r[] = {new JRadar(40), new JRadar(60), new JRadar(110)};
25             int v[] = {44, 67, 110};
26             Boolean res[]={false, true, false};
27
28               for (int i=0; i < r.length; i++) {
29                  if (r[i].multar(v[i]) == res[i])
30                     System.out.println("OK");
31                  else
32                     System.out.println("ERRO: radar " + i);
33               }
34           }
35       }
36   }

Figura 17: Exemplo de classe aninhada estática.


         31,,5, 1/(/F1.1, 3+01(, 5 1/G/(41,

Há outros dois tipos de classes aninhadas:
     Local: criada no corpo de um método
     Anônima: criada no corpo de um método sem nome de classe, bastante utilizada em tratamento
     de eventos de interface gráfica. A forma de instanciação é ligeiramente diferente. Observar na
     figura 18, linha 3, a instanciação de uma classe anônima que implementa a classe interface
     ActionListener. Uma classe anônima deve estender ou (exclusivo) implementar uma e somente
     uma classe.
1    Button b = new Button("Ok");
2    b.addActionListener(
3        new ActionListener() {
4            public void actionPerformed(ActionEvent e) {
5                tratarOK();
6            }
7        }
8    );

Figura 18: Exemplo de classe interna anônima.




                                                                                                  16


[PAGINA 17]
0    3       3 1             !
 31/5D1' Antes de começar a programar fazer um pseudo-código ou fluxograma.
Vantagens:
    Ajuda a detectar defeitos antes da codificação (economiza tempo)
    Aumenta a confiabilidade do software
Desvantagens
    Cria mais documentação que deverá ser mantida
    Podem exigir ferramentas adicionais, por exemplo, para desenhar fluxogramas
    Erros podem ser introduzidos no momento da tradução do pseudo-código/fluxograma para o
    programa

 '1&1' 5H059A5,. Verificar se os parâmetros de entrada condizem ao esperado.

 ,1' /+45, 5H2'5,,(8+, /1, 81'(785(, 5 4-&+.+,.
Exemplo:
    manipular (int num) //não diz nada
    obterNumeroAlunosDaTurma (int num) //é melhor
Dê nome aos números
Ex: for (int i=0; i < 54; i++) melhor fazer for (int i=0; i < TAM_TURMA; i++)

Evitar variáveis globais: preferir métodos com parâmetros sempre que possível.
Inicializar as variáveis
Declarar as variáveis perto de sua primeira utilização
Notação
     Classes: iniciam com letras maiúsculas: Aluno, VeiculoMotor
     Métodos: iniciam com letras minúsculas: obterNumeroAlunos()
     Atributos: numChassis
     Variáveis de métodos: em minúsculas ou idem aos atributos

 (01, .5 2'+<'1419=+
Evitar utilizar parâmetros dos métodos como variáveis do método
Limitar o número de parâmetros dos métodos (até 6, máximo 7)

Evitar aninhamentos (loops) com mais de 3 níveis
Verificar contadores de laço (principalmente os limites)
Assegurar que os loops terminam



         1'10&5'C,&(01, .5,5D785(, 21'1 *4 2'+D5&+ .5 ,+I&J1'5
    Correção: o software satisfaz aos requisitos da aplicação?
    Levar em conta que os requisitos variam ao longo do projeto impondo a necessidade de um
    projeto flexível.
    Robustez: o projeto ou a implementação são robustos quando capazes de tratarem situações
    incomuns ou de erro.
    Flexibilidade: tirar mais ou menos do que já foi implementado (por exemplo, uma calculadora
    que só faz uma operação por vez, é possível fazer várias operações). Adicionar novas
    funcionalidades e alterar funcionalidades
    Eficiência: tempo de execução e utilização de recursos (processador, memória, armazenamento).



                                                                                                  17


[PAGINA 18]
       Confiabilidade: tempo médio entre falhas (sistema já está em produção)
       Usabilidade: facilidade de uso


                                       "       #
Este capítulo é um resumo do tutorial da Sun1 que apresenta dois tipos de exceção: não verificadas e
verificadas.


           H059=+
É um evento anormal que ocorre durante a execução do programa interrompendo o fluxo normal de
execução. Quando uma exceção ocorre, um objeto denominado exception object, contendo informações
sobre o erro é criado.
Throwing an exception: significa que um método “lança” uma exceção criando um exception object que
deverá ser processado pelo JRE (Java Runtime Environment). Processado significa passar a exceção a
alguém que saiba o que fazer com ela, ou seja, passá-la a um exception handler. Um exception handler só
saberá tratar o exception object se tiver uma cláusula catch (“pegar a exceção que foi lançada”) que trata
o tipo da exceção em questão.


           (2+, .5 5H059=+
Há dois tipos de exceção: não verificadas e verificadas.
 H059A5, /=+ 85'(I(01.1, ?/+/0F50K5. 5H052&(+/,@ São exceções que não necessitam serem
“capturadas” (catch) pelos métodos. Este tipo de exceção ocorre internamente ao JRE, tais como:
exceções aritméticas (divisão por zero), ponteiros nulos e estouro de índice de vetores/matrizes.
1      public class JExcecoes {
2           public static void gravarArqTexto(String nomeArquivo) {
3                PrintWriter saida = new PrintWriter(new FileWriter(nomeArquivo));
4                saida.println("Eu sou o arquivo " + nomeArquivo);
5                saida.close();
6           }
7         public static double dividir(double x, double y) {
8             // Exemplifica exceção não verificada, não precisa ser "caught"
9             // São exceções internas ao java runtime.
10            // Em caso de divisão por zero, retorna Infinity
11            return x/y;
12        }
13
14         public static double extrairRaizQuadrada(double x) {
15             // Se x for negativo, retorna NaN (not a number)
16             return Math.sqrt(x);
17         }
18           public static void main(String[] args) {
19                System.out.println(dividir(5, 0));
20                System.out.println(extrairRaizQuadrada(-1))
21           }
22     }

Figura 19. Os métodos dividir e extrairRaizQuadrada podem gerar exceções não verificadas em tempo de
compilação.

 H059A5, 85'(I(01.1, ?0F50K5. 5H052&(+/,@ São exceções que devem ser tratadas e o tratamento é
exigido pelo compilador. São exceções que ocorrem externamente ao JRE, por exemplo, aquelas que
ocorrem durante operações de E/S. Na Figura 19, em gravarArqTexto, o método construtor FileWriter
“lança” (pode lançar) uma exceção que deve ser obrigatoriamente tratada. Assim, o compilador acusa
o seguinte erro: .


1
    http://java.sun.com/docs/books/tutorial/essential/exceptions/


                                                                                                        18


[PAGINA 19]
         '1&1' H059A5,
Antes de qualquer coisa é preciso saber qual o tipo de exceção gerada para poder tratá-la. Por
exemplo, o método construtor FileWriter lança uma exceção IOException. Para saber, basta consultar a
documentação do método em http://java.sun.com/j2se/1.5.0/docs/api/index.html. A figura seguinte
reproduz a documentação Java:

Constructor Detail
FileWriter
public FileWriter(String fileName) throws IOException
Constructs a FileWriter object given a file name.
Parameters:
fileName - String The system-dependent filename.
Throws:
IOException - if the named file exists but is a directory rather than a regular file, does not exist but
cannot be created, or cannot be opened for any other reason

Figura 20 : Exceção lançada pelo construtor de FileWriter.

Para tratar uma exceção é preciso cercá-la utilizando o try e pegá-la utilizando o comando catch. Cada
bloco catch é denominado exception handler. Podemos associar mais de um catch a um try. O código
mostrado na Figura 19 não passa na compilação. Para corrigi-lo é preciso substituir o método
gravarArqTexto pelo código mostrado na Figura 20.
public static void gravarArqTexto(String nomeArquivo) {
  PrintWriter saida = null;
  try {
  saida = new PrintWriter(new FileWriter(nomeArquivo));
        saida.println("Eu sou o arquivo " + nomeArquivo);
  } catch (IOException e) {
        System.out.println("Erro na criação do objeto FileWriter: "+
        nomeArquivo+e.getMessage());
  } finally {
        if (saida != null) {
           System.out.println(nomeArquivo + " sera´ fechado");
           saida.close();
        } else
           System.out.println(nomeArquivo + " nao foi aberto");
  }
}

Figura 21 : Blocos try, catch e finally.

Observe que o bloco finally sempre é executado independentemente do bloco try ser executado até o
final ou abortar no meio.


         1/91' H059A5,
Códigos que lançam exceções podem criar objetos descendentes da classe Throwable através do
comando throws. No código abaixo, o método pop lança a exceção pilha vazia.




                                                                                                           19


[PAGINA 20]
23 public Object pop() throws EmptyStackException {
1      Object obj;
2
3      if (size == 0) {
4          throw new EmptyStackException();
5      }
6
7      obj = objectAt(SIZE - 1);
8      setObjectAt(SIZE - 1, null);
9      size--;
10     return obj;
11 }

Figura 22. Exemplo de lançamento de exceção.
java.lang.Object
    java.lang.Throwable
        java.lang.Exception
            java.lang.RuntimeException
                java.util.EmptyStackException

Figura 23. Classe de um objeto de erro deve ser descendente da Throwable.

Um método pode lançar suas próprias exceções, como no exemplo da figura 22, ou lançar exceções
que foram lançadas por outros métodos que não foram tratadas no método em questão. Até o método
main pode lançar exceções geradas por outros métodos para o JRE.




                                                                                             20


[PAGINA 21]
$      "       %
1.   (conceito) Implemente uma classe que represente o comportamento de um semáforo (máquina de
     estados cíclica) e instancie um objeto desta classe demonstrando que funciona por meio de uma
     interface textual.

                                         !"!#          #     $$ %&


2.   (classe de Interface) Baixe o projeto Netbeans Ratos de Interface e faça o seguinte:
     ( ) a. Crie um novo rato de canto que implemente as classes de interface LimitesDoTabuleiro e
      RatoDeTabuleiro nos moldes da RatoDeCanto e modifique a aparência para “X-X”.
     ( ) b. Crie um novo tipo de rato (RatoAleatorio) que anda aleatoriamente no tabuleiro
     ( ) c. Pegue o código do rato de um colega e plugue no simulador
     ( ) d. Faça o diagrama de classes para o sistema só com as classes do problema (UML).
                                         !"!#          #     $$ %&     #       '


3.   (herança) Vamos supor um simulador de futebol simplificado onde jogadores se deslocam num
     tabuleiro de tamanho N X M e a bola ocupa uma das posições (x, y). Todos os jogadores
     apresentam comportamentos básicos similares, são eles: void desenhar(), void apagar(), void
     reposicionar(), void reposicionar(Point p), void inicializar(Ponto p) e Chute chutar(). Desenhar()
     desenha o jogador na posição x, y atual; apagar() apaga o jogador da posição x, y atual,
     reposicionar() faz o jogador retornar ao seu campo na posição inicial e reposicionar(Ponto p)
     define a próxima posição do jogador no tabuleiro sendo que o jogador somente se movimenta de
     casa em casa (não salta!). Suponha que há vários tipos de jogadores que se comportam
     diferentemente (se movimentam e chutam diferentemente) em função da posição, zagueiro,
     atacante, meio-campo e goleiro, e tem aparências diferentes também em função da posição. Um
     jogador somente pode chutar a bola se estiver na mesma posição que esta última. O chute pode ser
     dado para frente, trás, esquerda ou direita, e com uma certa força (fraco, médio, forte). Logo, um
     chute é a combinação de uma direção com uma força. O simulador faz o seguinte a cada ciclo:
     chama a operação Chute jogar() para o time1; calcula a posição da bola em função das informações
     do chute dado ou não, consulta as posições dos goleiros do time1 e time2 executando a operação
     Ponto GetPosGoleiro() para saber se o goleiro agarrou a bola ou se foi gol e redesenha a bola. Em
     seguida, repete os passos para o time2. Em caso de gol, os times recebem um reposicionar() do
     simulador. Neste caso, todos os jogadores devem voltar ao seu campo nas posições originais e o
     ciclo continua. Na operação jogar(), o “time” escolhe quais jogadores vão se movimentar em
     função da posição da bola (aí está a inteligência e coordenação do time). Os jogadores escolhidos
     para se movimentar devem ser apagados (apagar()) da posição onde se encontram, reposicionados
     (reposicionar(Point p)) e redesenhados (desenhar()). Faça um diagrama de classes que represente
     as classes necessárias e implemente um jogo com dois times. IMPORTANTE: o código deve
     permitir que um jogador e, até mesmo, um time com seus jogadores desenvolvido por outro
     programador seja “plugado” no simulador.

                                         !"!#          #     $$ "(%&       #

4.   (herança) Uma locadora de veículos aluga diversos tipos de veículos: caminhões, carros de passeio
     categoria A, B e C, utilitários (furgões e camionetes) e motos. O preço da diária dos veículos varia
     em função do imposto de locação e do valor de locação (ambos diários). A fórmula de cálculo do
     aluguel é diferente para caminhões, carros de passeio, utilitários e motos. Caminhões levam em
     conta o número de eixos e motos, a cilindrada (caso não seja informado, assume-se 125cc).
     Organize as classes hierarquicamente em um diagrama de classes com seus atributos e o método
     calcular valor locação diária.


[PAGINA 22]
                                      !"!#          #     $$ "(%&       ) *+    "     ,


5.   (Herança, polimorfismo) Fazer o diagrama de classes para o código abaixo. Qual o tipo de
     polimorfismo existente no método calcularIPVA()?
1    interface IPVA {
2    // definimos algumas constantes (implicitamente são static final e declaramos
3    // um método abstrado calcular IPVA
4       Boolean CARRO_PASSEIO = true,
5             CARRO_UTILITARIO = false;
6       double CTE_UTILITARIO = 0.75,
7             CTE_PASSEIO = 1.0;
8       double VALOR_BASE = 500.00;
9       public double calcularIPVA();
10   }
11
12   class Carro implements IPVA {
13      Boolean tipoCarro=CARRO_PASSEIO;
14      String placa = new String("ABC1010");
15      public double calcularIPVA() {
16         if (tipoCarro==CARRO_PASSEIO)
17            return VALOR_BASE * CTE_PASSEIO;
18         else
19            return VALOR_BASE * CTE_UTILITARIO;
20      }
21   }
22   class Caminhao implements IPVA {
23      String placa = new String("CCC1010");
24      public double calcularIPVA() {
25         return 2 * VALOR_BASE * CTE_UTILITARIO;
26      }
27   }
28
29   public class ExemplificarInterface {
30      // A classe IPVA homogeiniza a execução do método calcularIPVA. Aqui não
31      // sabemos se o objeto é um carro ou um caminhao, mas como ambas as classes
32      // são obrigadas a implementar o método em questão podemos chamá-lo sem
33      // conhecer a classe do objeto.
34      public static void main(String args[]) {
35         IPVA veiculos[] = {new Carro(), new Caminhao()};
36         for (int i=0; i < veiculos.length; i++)
37            System.out.println(veiculos[i].calcularIPVA());
38
39       }
40   }
              ) *
                                      !"!#          #     $$ "(%&       (      '("!


6.   (Herança, Construtora) Utilizando os operadores super e this, faça o corpo dos métodos
     ObterNomeCientífico presentes código abaixo para que a linha marcada em amarelo imprima o
     nome científico da classe, ordem e a família de Totó na seguinte forma:
     “Mammalia.Carnivora.Canidae”.
     -
                                      !"!#          #     $$ %&     .


                                      !"!#          #     $$ %&     .

Arquivo Mamifero.java
41 public abstract class Mamifero {
42      private static final String nivel = "Classe";
43      private static final String nomeCientifico = "Mammalia";
44      private static final String nomePopular = "Mamifero";
45
46      public String obterNomeCientifico() {
47          // corpo do método
48          return (“um string”);
49      }
50 }
51
52 abstract class Carnivoro extends Mamifero {
53      private static final String nivel = "Ordem";
54      private static final String nomeCientifico = "Carnivora";


[PAGINA 23]
55          private static final String nomePopular = "Carnivoro";
56
57          public String obterNomeCientifico() {
58              // corpo do método
59              return “um string “;
60          }
61   }
62
63       class Canidio extends Carnivoro {
64          private static final String nivel = "Familia";
65          private static final String nomeCientifico = "Canidae";
66          private static final String nomePopular = "Canidios";
67          String nome;
68          Canidio(String nome) {
69              this.nome = nome;
70          }
71          public String obterNomeCientifico() {
72              // corpo do método
73              return “um string“;
74          }
75   }

Arquivo Main.java
76 public class Main {
77      public static void main(String args[]) {
78          Canidios toto = new Canidios(“toto”);
79          System.out.println("Nome cientifico " toto.nome + “ = “);
80          System.out.println(toto.obterNomeCientifico());
81      }
82 }


7.   Ao executar o código abaixo, com o valor impresso para x? Que mensagens serão impressas e em
     qual ordem? Fonte:
Arquivo Main.java
83 public class Main {
84      public static void main(String args[]) {
85          C c = new C();
86          System.out.println(“valor de x = “ + c.x);
87      }
88 }

Arquivo A.java
1   public class A {
2       int x;
3       public A() {
4           x = 1;
5           System.out.println("=== A ===");
6       }
7   }
8
9   class B extends A {
10      public B() {
11          x = 2;
12          System.out.println("\t=== B");
13      }
14 }
15
16 class C extends B {
17      public C() {
18          x = 3;
19          System.out.println("\t\t=== C");
20      }
21 }
8.   (classe abstrata, polimorfismo) Um usuário deseja ter vários tipos de assinaturas para colocar nos
     seus e-mails de acordo com o destinatário (há também uma assinatura default para outros não
     especificados). Como você utilizaria uma classe abstrata, herança e polimorfismo para resolver
     este problema? A assinatura é composta por três atributos: mensagem, nome, ramal. Deve haver
     um método imprimirAssinatura. Implemente e faça o diagrama e classes em UML.
         Destinatário        Assinatura
         Amigo               []s
                             João de Almeida


[PAGINA 24]
          Colega de trabalho   Atenciosamente,
                               João de Almeida
                               Ramal 3455
          Parente              Até mais,
                               João de Almeida



                                         !"!#       #      $$ %&   /      !        %

9.    (membros classe & instância) Interprete o código abaixo e responda, considerando que a e b são
     instâncias de Automóvel:
     a) Qual o valor Automovel.numAutosFeitos após a criação de 5 instâncias de Automóvel?
     b) Qual o valor de a.numAutosFeitos (considerando o item a)?
     c)     Automovel.numAutosFeitos, a.numAutosFeitos e b.numAutosFeitos sempre têm o mesmo
            valor?
1    public class Automovel {
2    public int quilometragem;
3    public static int numAutosFeitos=0;
4
5    public Automovel() {
6        incrementarNumAutosFeitos();
7     }
8   public static void incrementarNumAutosFeitos() {
9       numAutosFeitos++;
10 }
11
12 public void incrementarQuilometragem(int km) {
13      quilometragem += km;
14 }



10. (membros classe & instância) Modificar o código do semáforo (exercício 1) para que toda instância
    de semáforo saiba quantos foram instanciados a qualquer momento.

                                         !"!#       #      $$ %&          '

11. (membros classe & instância, visibilidade) Reutilize o código do semáforo e inclua (ou modifique a)
    uma construtora tornando-a PRIVATE (não pode haver construtora pública). Pergunta-se: como
    uma outra classe poderia instanciar semáforos dado que a construtora é private? Implemente.

                                         !"!#       #      $$ %&          +    (


12. (Visibilidade) O código abaixo contém vários problemas com as definições de visibilidade dos
    métodos, atributos e classes. Corrija-os mantendo os dois arquivos .java.

                                         !"!#       #      $$ %&   (


Arquivo JExemploPacotes.java
// Objetivo: utilizar pacotes e visibilidade.
1   // A classe ponto não é visível deste pacote "default"
2   // pois foi definida como friendly no pacote quadrado
3   import quadrado.*;
4
5   public class JExemploPacotes {
6
7       public static void main(String[] args) {
8         Ponto p = new Ponto(10, 20);
9         Quadrado q = new Quadrado(p, 5);
10        System.out.println(q.calcularArea());
11      }
12 }

Arquivo Quadrado.java


[PAGINA 25]
package quadrado;
1
2   class Ponto {
3      private float x;
4      private float y;
5      Ponto(float x1, float y1) {
6         x = x1;
7         y = y1;
8      }
9   }
10
11 public class Quadrado {
12     private Ponto verticeXY;
13     private float lado;
14
15     Quadrado(Ponto v, float l) {
16        verticeXY = v;
17        lado = l;
18     }
19     public float calcularArea() {
20        return (lado*lado);
21     }
22 }

13. (vis, her, poli) Analise o código abaixo e responda:
Arquivo Pessoa.java

1    package pessoa;
2    import java.io.*;
3    public interface Pessoa {
4       abstract public void imprimir();
5    }
6    abstract class Usuario implements Pessoa {
7       protected String nome;
8       protected int cpf;
9       protected int maxEmprestimo=2;
10      public Usuario(String nome, int cpf) {
11            this.nome = nome;
12            this.cpf = cpf;
13      }
14      public void imprimir() {
15            System.out.println("nome: " + this.nome +
16            " cpf: " + this.cpf + " emprestimos: " +
17            this.maxEmprestimo);
18      }
19   }
20   class UsuarioPadrao extends Usuario {
21      public UsuarioPadrao(String nome, int cpf) {
22           super(nome, cpf);
23      }
24   }
25   class UsuarioEspecial extends Usuario {
26      public UsuarioEspecial(String nome, int cpf) {
27           super(nome, cpf);
28           this.maxEmprestimo = 6;
29      }
30   }

Arquivo CadastroUsuario.java

31   package principal;
32   import pessoa.*;
33
34   public class CadastroUsuario {
35      public static void main(String args[]) {
36           Usuario usuario[] =
37              {new UsuarioPadrao("Joao", 123456),
38               new UsuarioEspecial("Maria", 676767),
39               new UsuarioPadrao("Carlos", 888999)};
40
41              for (int i=0; i < usuario.length; i++)
42                  usuario[i].imprimir();
43       }
44   }
         !"!#         0 #      $$0 %&   +    1     %


[PAGINA 26]
    ( ) a. Quais são os problemas de visibilidade e como corrigi-los mantendo os pacotes e as classes
        nos respectivos pacotes e sem mudar/adicionar métodos?
    ( ) b. O que o programa (depois das correções) imprime na tela quando executado?
    ( ) c. Cite um exemplo de polimorfismo de sobreposição.
    ( ) d. Crie um novo método construtor que faça polimorfismo de sobrecarga sobre o construtor
        Usuario(String nome, int cpf) da classe Usuário.
    ( ) e. Onde foram aplicados o princípio da substituição de classes e vinculação dinâmica (late
        binding)?
    ( ) f. Como você faria para reduzir o acomplamento entre o pacote principal e o pessoa. De outra
        forma, faça com que o código da classe CadastroUsuario só utilize uma classe do pacote
        pessoa. Comparar a solução obtida com o padrão Factory por meio de um diagrama de classes
        (casar com o diagrama de classes do padrão Factory)

                                      !"!#          #      $$ +        1           -       2
                                      !"!#          #      $$ +        1           -       2   3

14. (classes interna, interface). Utilize uma classe interna que implemente a interface Iterator e permita
    navegar num vetor de 10 inteiros (valores aleatórios) armazenados em um atributo de instância da
    classe externa. O método next() do Iterator deve retornar somente os valores ímpares armazenados
    no vetor. Por exemplo, se no vetor existirem os seguintes números: {100, 3987, 123, 4}, a sequência
    de invocações abaixo produz:
     next() -> 3987
     next() -> 123
     next() -> throw NoSuchElementExecption
     O métod hasNext() verifica se há um número ímpar em alguma posição além das já pesquisadas.
     A implementação do método remove() é opcional. Caso não seja feita, deve retornar uma
     instância de UnsupportedOperationException.

                                       !"!#          #     $$ !            '

15. (classe aninhada estática) Utilize uma classe aninhada estática para testar uma classe
    externa que calcula o dígito verificador de um código composto por três dígitos da
    seguinte forma:
    829 => 8*4 + 2*3 + 9*2 = 56 => 56 % 10 = 6 (dígito verificador). O teste deve ser feito para
    dois códigos cujos dígitos verificadores são conhecidos (calculados manualmente).

                                       !"!#          #     $$ %&   +           !       %           )"

16. (boas práticas) Um usuário necessita de um “sistema” para somar dois números reais.
    Codifique o dito sistema preocupando-se com as dicas de programação e procurando
    atender às seguintes propriedades de qualidade de software: correção, robustez e
    flexibilidade.
17. (boas práticas e exceções) Completar o exercício da calculadora levando em conta o
    seguinte:
    Correção: O sistema permite somar quaisquer tipos de números (inteiros, decimais, negativos)?
   Flexibilidade: Somar vários números ao invés de dois somente. O usuário pode fazer várias
   somas sem precisar executar o programa a cada vez? Introduzir novas operações: multiplicação,
   divisão e subtração.
   Robustez: Verifica se os operandos lidos do teclado são numéricos? Verifica se o usuário solicitou
   uma operação válida (adição, subtração, divisão ou multiplicação)?


[PAGINA 27]
   Usabilidade: É fácil de ser usado? As opções para o usuário são claras (ex. como sair do
   programa)?

18. (exceções) Pesquisar o método scanner e ver quais são as exceptions lançadas pelo mesmo.
    Abaixo as exceções lançadas pelo Scanner.nextDouble():
Throws:
       InputMismatchException - if the next token does not match the Float regular expression, or is out of range
       NoSuchElementException - if the input is exhausted
       IllegalStateException - if this scanner is closed
