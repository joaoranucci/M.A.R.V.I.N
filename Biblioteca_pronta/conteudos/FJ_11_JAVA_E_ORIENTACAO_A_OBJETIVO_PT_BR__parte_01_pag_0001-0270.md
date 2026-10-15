# FJ_11_JAVA_E_ORIENTACAO_A_OBJETIVO_PT_BR

Arquivo original: more_papers_by_thyago_louiz/FJ_11_JAVA_E_ORIENTACAO_A_OBJETIVO_PT_BR.pdf
SHA-256 do original: 0de6d84266179412cd498f5311e4d439bc35298648180b7b5ae59d43113e30fe

Texto extraido para consulta. As paginas abaixo usam a ordem do arquivo PDF, incluindo capas.
Parte preparada: 1/1


[PAGINA 1]
FJ-11
Java e Orientação a Objetos


[PAGINA 2]
    A Caelum atua no mercado com consultoria, desenvolvimento e ensino em computação. Sua equipe
participou do desenvolvimento de projetos em vários clientes e, após apresentar os cursos de verão de Java
na Universidade de São Paulo, passou a oferecer treinamentos para o mercado. Toda a equipe tem uma
forte presença na comunidade através de eventos, artigos em diversas revistas, participação em muitos
projetos open source como o VRaptor e o Stella e atuação nos fóruns e listas de discussão como o GUJ.

    Com uma equipe de mais de 60 proﬁssionais altamente qualiﬁcados e de destaque do mercado, oferece
treinamentos em Java, Ruby on Rails e Scrum em suas três unidades - São Paulo, Rio de Janeiro e
Brasília. Mais de 8 mil alunos já buscaram qualiﬁcação nos treinamentos da Caelum tanto em nas unidades
como nas próprias empresas com os cursos incompany.

   O compromisso da Caelum é oferecer um treinamento de qualidade, com material constantemente
atualizado, uma metodologia de ensino cuidadosamente desenvolvida e instrutores capacitados
tecnicamente e didaticamente. E oferecer ainda serviços de consultoria ágil, mentoring e desenvolvimento
de projetos sob medida para empresas.




                                          Comunidade

                 Nossa equipe escreve constantemente artigos no Blog da Caelum que já conta
                 com 150 artigos sobre vários assuntos de Java, Rails e computação em geral.
                 Visite-nos e assine nosso RSS:
                 ➡ blog.caelum.com.br



                 Acompanhe também a equipe Caelum no Twitter:
                 ➡ twitter.com/caelumdev/equipe



                 O GUJ é maior fórum de Java em língua portuguesa, com 700 mil posts e 70 mil
                 usuários. As pessoas da Caelum participam ativamente, participe também:
                 ➡ www.guj.com.br



                 Assine também nossa Newsletter para receber as novidades e destaques dos
                 eventos, artigos e promoções da Caelum:
                 ➡ www.caelum.com.br/newsletter


                 No site da Caelum há algumas de nossas Apostilas disponíveis gratuitamente
                 para download e alguns dos artigos de destaque que escrevemos:
                 ➡ www.caelum.com.br/apostilas
                 ➡ www.caelum.com.br/artigos


[PAGINA 3]
      Conheça alguns de nossos cursos

             FJ-11:                             FJ-26:
             Java e Orientação a objetos        Laboratório de MVC com
                                                Hibernate e JSF para a Web



             FJ-16:                             FJ-31:
             Laboratório Java com Testes,       Java EE avançado e
             XML e Design Patterns              Web Services



             FJ-19:                             FJ-91:
             Preparatório para Certificação     Arquitetura e Design de
             de Programador Java                Projetos Java



             FJ-21:                             FJ-27:
             Java para Desenvolvimento          Spring Framework
             Web



             RR-71:                             RR-75:
             Desenvolvimento Ágil para Web      Ruby e Rails avançados: lidando
             2.0 com Ruby on Rails              com problemas do dia a dia



Para mais informações e outros cursos, visite: caelum.com.br/cursos


  ✓   Mais de 8000 alunos treinados;
  ✓   Reconhecida nacionalmente;
  ✓   Conteúdos atualizados para o mercado e para sua carreira;
  ✓   Aulas com metodologia e didática cuidadosamente preparadas;
  ✓   Ativa participação nas comunidades Java, Rails e Scrum;
  ✓   Salas de aula bem equipadas;
  ✓   Instrutores qualiﬁcados e experientes;
  ✓   Apostilas disponíveis no site.


[PAGINA 4]
                               Sobre esta apostila
   Esta apostila da Caelum visa ensinar de uma maneira elegante, mostrando apenas o que é necessário e
quando é necessário, no momento certo, poupando o leitor de assuntos que não costumam ser de seu interesse
em determinadas fases do aprendizado.

   A Caelum espera que você aproveite esse material. Todos os comentários, críticas e sugestões serão muito
bem-vindos.

    Essa apostila é constantemente atualizada e disponibilizada no site da Caelum. Sempre consulte o site para
novas versões e, ao invés de anexar o PDF para enviar a um amigo, indique o site para que ele possa sempre
baixar as últimas versões. Você pode conferir o código de versão da apostila logo no final do índice.

   Baixe sempre a versão mais nova em: www.caelum.com.br/apostilas

    Esse material é parte integrante do treinamento Java e Orientação a Objetos e distribuído gratuitamente
exclusivamente pelo site da Caelum. Todos os direitos são reservados à Caelum. A distribuição, cópia, revenda
e utilização para ministrar treinamentos são absolutamente vedadas. Para uso comercial deste material, por
favor, consulte a Caelum previamente.


                                                                                          www.caelum.com.br




                                                      1


[PAGINA 5]
Índice


1 Como Aprender Java                                                                                                  1

  1.1 O que é realmente importante? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         1

  1.2 Sobre os exercícios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       1

  1.3 Tirando dúvidas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       1

  1.4 Bibliografia . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    2


2 O que é Java                                                                                                        3

  2.1 Java . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      3

  2.2 Máquina Virtual . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       4

  2.3 Java lento? Hotspot e JIT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       6

  2.4 Versões do Java e a confusão do Java2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .           6

  2.5 JVM? JRE? JDK? O que devo baixar? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .             7

  2.6 Onde usar e os objetivos do Java        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   7

  2.7 Especificação versus implementação . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .            8

  2.8 Como o FJ-11 está organizado . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          8

  2.9 Compilando o primeiro programa . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          9

  2.10 Executando seu primeiro programa . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10

  2.11 O que aconteceu? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10

  2.12 Para saber mais: como é o bytecode? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11

  2.13 Exercícios: Modificando o Hello World . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11

  2.14 O que pode dar errado? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12

  2.15 Um pouco mais... . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13

  2.16 Exercícios adicionais . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13

                                                          i


[PAGINA 6]
3 Variáveis primitivas e Controle de fluxo                                                                         14

   3.1 Declarando e usando variáveis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14

   3.2 Tipos primitivos e valores . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

   3.3 Exercícios: Variáveis e tipos primitivos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

   3.4 Discussão em aula: convenções de código e código legível . . . . . . . . . . . . . . . . . . . . . 18

   3.5 Casting e promoção . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

   3.6 O If-Else . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20

   3.7 O While . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22

   3.8 O For . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22

   3.9 Controlando loops . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23

   3.10 Escopo das variáveis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24

   3.11 Um bloco dentro do outro . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25

   3.12 Para saber mais . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25

   3.13 Exercícios: Fixação de sintaxe . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26

   3.14 Desafios: Fibonacci . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27


4 Orientação a objetos básica                                                                                      28

   4.1 Motivação: problemas do paradigma procedural           . . . . . . . . . . . . . . . . . . . . . . . . . . . 28

   4.2 Criando um tipo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29

   4.3 Uma classe em Java . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31

   4.4 Criando e usando um objeto . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31

   4.5 Métodos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32

   4.6 Métodos com retorno . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34

   4.7 Objetos são acessados por referências . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35

   4.8 O método transfere() . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38

   4.9 Continuando com atributos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39

   4.10 Para saber mais: Uma Fábrica de Carros . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42

   4.11 Um pouco mais... . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43

   4.12 Exercícios: Orientação a Objetos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44

   4.13 Desafios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48

   4.14 Fixando o conhecimento . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48




                                                         ii


[PAGINA 7]
5 Um pouco de arrays                                                                                              49

   5.1 O problema . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49

   5.2 Arrays de referências . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50

   5.3 Percorrendo uma array . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51

   5.4 Percorrendo uma array no Java 5.0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52

   5.5 Exercícios: Arrays . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52

   5.6 Um pouco mais... . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55

   5.7 Desafios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56

   5.8 Testando o conhecimento . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56


6 Modificadores de acesso e atributos de classe                                                                   57

   6.1 Controlando o acesso . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57

   6.2 Encapsulamento . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60

   6.3 Getters e Setters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62

   6.4 Construtores . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64

   6.5 A necessidade de um construtor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65

   6.6 Atributos de classe . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67

   6.7 Um pouco mais... . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68

   6.8 Exercícios: Encapsulamento, construtores e static . . . . . . . . . . . . . . . . . . . . . . . . . . 69

   6.9 Desafios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70


7 Orientação a Objetos – herança, reescrita e polimorfismo                                                        72

   7.1 Repetindo código? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72

   7.2 Reescrita de método . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75

   7.3 Invocando o método reescrito      . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76

   7.4 Polimorfismo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77

   7.5 Um outro exemplo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79

   7.6 Um pouco mais... . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80

   7.7 Exercícios: Herança e Polimorfismo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81

   7.8 Dicussões em aula: Alternativas ao atributo protected . . . . . . . . . . . . . . . . . . . . . . . . 85




                                                        iii


[PAGINA 8]
8 Eclipse IDE                                                                                                       86

   8.1 O Eclipse     . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86

   8.2 Apresentando o Eclipse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86

   8.3 Views e Perspective . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87

   8.4 Criando um projeto novo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89

   8.5 Criando o main . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93

   8.6 Rodando o main . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95

   8.7 Pequenos truques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96

   8.8 Exercícios: Eclipse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96

   8.9 Discussão em aula: Refactoring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98


9 Orientação a Objetos – Classes Abstratas                                                                          99

   9.1 Repetindo mais código?       . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99

   9.2 Classe abstrata . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100

   9.3 Métodos abstratos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102

   9.4 Aumentando o exemplo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103

   9.5 Para saber mais... . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104

   9.6 Exercícios: Classes Abstratas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104

   9.7 Desafios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105


10 Orientação a Objetos - Interfaces                                                                              106

   10.1 Aumentando nosso exemplo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106

   10.2 Interfaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110

   10.3 Dificuldade no aprendizado de interfaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113

   10.4 Exemplo interessante: conexões com o banco de dados . . . . . . . . . . . . . . . . . . . . . . . 113

   10.5 Um pouco mais... . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114

   10.6 Exercícios: Interfaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114

   10.7 Exercícios avançados opcionais . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118

   10.8 Discussão em aula: Favorecer composição em relação à herança . . . . . . . . . . . . . . . . . . 119




                                                         iv


[PAGINA 9]
11 Controlando os erros com Exceções                                                                               120

   11.1 Motivação . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120

   11.2 Exercício para começar com os conceitos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122

   11.3 Exceções de Runtime mais comuns . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126

   11.4 Outro tipo de exceção: Checked Exceptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127

   11.5 Um pouco da grande famíla Throwable . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130

   11.6 Mais de um erro . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130

   11.7 Lançando exceções . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131

   11.8 O que colocar dentro do try? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132

   11.9 Criando seu próprio tipo de exceção . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134

   11.10Para saber mais: finally . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135

   11.11Exercícios: Exceções . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135

   11.12Desafios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137

   11.13Discussão em aula: catch e throws em Exception . . . . . . . . . . . . . . . . . . . . . . . . . . . 138


12 Pacotes - Organizando suas classes e bibliotecas                                                                139

   12.1 Organização . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139

   12.2 Diretórios   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140

   12.3 Import . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140

   12.4 Acesso aos atributos, construtores e métodos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142

   12.5 Usando o Eclipse com pacotes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143

   12.6 Exercícios: Pacotes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144


13 Ferramentas: jar e javadoc                                                                                      146

   13.1 Arquivos, bibliotecas e versões . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146

   13.2 Gerando o jar pelo Eclipse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147

   13.3 Javadoc . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151

   13.4 Gerando o Javadoc . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 152

   13.5 Exercícios: Jar e Javadoc . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156




                                                          v


[PAGINA 10]
14 O pacote java.lang                                                                                              157

   14.1 Pacote java.lang . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157

   14.2 Um pouco sobre a classe System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157

   14.3 java.lang.Object . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158

   14.4 Casting de referências . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159

   14.5 Métodos do java.lang.Object: equals e toString . . . . . . . . . . . . . . . . . . . . . . . . . . . . 160

   14.6 Integer e classes wrappers (box) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 162

   14.7 Autoboxing no Java 5.0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163

   14.8 java.lang.String . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164

   14.9 java.lang.Math . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 166

   14.10Exercícios: java.lang . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167

   14.11Desafio . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170

   14.12Discussão em aula: O que você precisa fazer em Java? . . . . . . . . . . . . . . . . . . . . . . . 170


15 Pacote java.io                                                                                                  171

   15.1 Conhecendo uma API . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 171

   15.2 Orientação a objetos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 171

   15.3 InputStream, InputStreamReader e BufferedReader . . . . . . . . . . . . . . . . . . . . . . . . . 172

   15.4 Lendo Strings do teclado . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 174

   15.5 A analogia para a escrita: OutputStream . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 174

   15.6 Uma maneira mais fácil: Scanner e PrintStream          . . . . . . . . . . . . . . . . . . . . . . . . . . . 175

   15.7 Um pouco mais... . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176

   15.8 Exercícios: Java I/O . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176

   15.9 Discussão em aula: Design Patterns e o Template Method . . . . . . . . . . . . . . . . . . . . . . 180


16 Collections framework                                                                                           182

   16.1 Arrays são trabalhosos, utilizar estrutura de dados . . . . . . . . . . . . . . . . . . . . . . . . . . 182

   16.2 Listas: java.util.List . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 183

   16.3 Listas no Java 5.0 com Generics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186

   16.4 A importância das interfaces nas coleções        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186

   16.5 Ordenação: Collections.sort . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187

   16.6 Exercícios: Ordenação . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 190

   16.7 Conjunto: java.util.Set . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 193

                                                          vi


[PAGINA 11]
  16.8 Principais interfaces: java.util.Collection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 194

  16.9 Percorrendo coleções no Java 5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 195

  16.10Para saber mais: Iterando sobre coleções com java.util.Iterator . . . . . . . . . . . . . . . . . . . 196

  16.11Mapas - java.util.Map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 198

  16.12Para saber mais: Properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 200

  16.13Para saber mais: Equals e HashCode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 200

  16.14Para saber mais: Boas práticas      . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201

  16.15Exercícios: Collections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201

  16.16Desafios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 204


17 Programação Concorrente e Threads                                                                             205

  17.1 Threads . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 205

  17.2 Escalonador e trocas de contexto . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 207

  17.3 Garbage Collector . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 209

  17.4 Para saber mais: problemas com concorrência . . . . . . . . . . . . . . . . . . . . . . . . . . . . 210

  17.5 Para saber mais: Vector e Hashtable . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 212

  17.6 Um pouco mais... . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 213

  17.7 Exercícios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 213

  17.8 Exercícios avançados de programação concorrente e locks . . . . . . . . . . . . . . . . . . . . . 214


18 E agora?                                                                                                      216

  18.1 Exercício prático . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216

  18.2 Certificação . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216

  18.3 Web . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216

  18.4 Revistas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216

  18.5 Grupos de Usuários . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 217

  18.6 Falando em Java - Próximos módulos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 217


19 Apêndice - Sockets                                                                                            218

  19.1 Motivação: uma API que usa os conceitos aprendidos . . . . . . . . . . . . . . . . . . . . . . . . 218

  19.2 Protocolo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 218

  19.3 Porta . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 219

  19.4 Socket . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 219


                                                        vii


[PAGINA 12]
   19.5 Servidor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220

   19.6 Cliente . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 221

   19.7 Imagem geral . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 223

   19.8 Exercícios: Sockets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 223

   19.9 Desafio: Múltiplos Clientes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 225

   19.10Desafio: broadcast das mensagens . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 225

   19.11Solução do sistema de chat . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 226


20 Apêndice - Instalação do Java                                                                                   230

   20.1 Escolhendo a VM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 230

   20.2 Instalando no Ubuntu e outros Linux . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 230

   20.3 No Mac OS X e Solaris . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 230

   20.4 Instalação do JDK em ambiente Windows . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 231


21 Apêndice - Debugging                                                                                            236

   21.1 O que é debugar      . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 236

   21.2 Debugando no Eclipse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 236

   21.3 Perspectiva de debug . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 238

   21.4 Degub avançado       . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 243

   21.5 Profiling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 253

   21.6 Profiling no Eclipse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 253
                                                 Versão: 12.3.19




                                                         viii


[PAGINA 13]
                                                                                              C APÍTULO     1

Como Aprender Java
                                                      “Busco um instante feliz que justifique minha existência”
                                                                                             – Fiodór Dostoievski


 1.1 - O que é realmente importante?
    Muitos livros, ao passar dos capítulos, mencionam todos os detalhes da linguagem juntamente com seus
princípios básicos. Isso acaba criando muita confusão, em especial porque o estudante não consegue distinguir
exatamente o que é primordial aprenderno início daquilo que pode ser estudado mais a frente.

    Se uma classe abstrata deve ou não ter ao menos um método abstrato, se o if só aceita argumentos boole-
anos e todos os detalhes de classes internas realmente não devem ser preocupações para aquele que possui
como objetivo primário aprender Java. Esse tipo de informação será adquirida com o tempo, e não é necessário
no início.

   Neste curso, separamos essas informações em quadros especiais, já que são informações extras. Ou então,
apenas citamos num exercício e deixamos para o leitor procurar informações se for de seu interesse.

    Por fim falta mencionar sobre a prática, que deve ser tratada seriamente: todos os exercícios são muito
importantes e os desafios podem ser feitos quando o curso acabar. De qualquer maneira recomendamos aos
alunos estudar em casa, e praticar bastante código e variações.

             O curso
            Para aqueles que estão fazendo o curso Java e Orientação a Objetos, é recomendado estudar em
            casa aquilo que foi visto durante a aula, tentando resolver os exercícios opcionais e os desafios
            apresentados.


 1.2 - Sobre os exercícios
   Os exercícios do curso variam de práticos até pesquisas na Internet, ou mesmo consultas sobre assuntos
avançados em determinados tópicos para incitar a curiosidade do aprendiz na tecnologia.

    Existem também, em determinados capítulos, uma série de desafios. Eles focam mais no problema compu-
tacional que na linguagem, porém são uma excelente forma de treinar a sintaxe e, principalmente, familiarizar o
aluno com a biblioteca padrão Java, além de proporcionar um ganho na velocidade de desenvolvimento.


 1.3 - Tirando dúvidas
   Para tirar dúvidas dos exercícios, ou de Java em geral, recomendamos o fórum do GUJ (http://www.guj.
com.br/), onde sua dúvida será respondida prontamente. O GUJ foi fundado por desenvolvedores da Caelum,
e hoje conta com mais de um milhão de mensagens.

                                                      1


[PAGINA 14]
                                                     Material do Treinamento Java e Orientação a Objetos




   Fora isso, sinta-se a vontade de entrar em contato com seu instrutor para tirar todas as suas dúvidas que
aparecerem durante o curso.


 1.4 - Bibliografia
   Bibliografia recomendada para iniciantes na plataforma Java

   • Java - Como programar, de Harvey M. Deitel

   • Use a cabeça! - Java, de Bert Bates e Kathy Sierra

   • (Avançado) Effective Java Programming Language Guide - 2nd edition, de Joshua Bloch




                                                             Capítulo 1 - Como Aprender Java - Bibliografia - Página 2


[PAGINA 15]
                                                                                             C APÍTULO     2

O que é Java
                                                       “Computadores são inúteis, eles apenas dão respostas”
                                                                                                    – Picasso

   Chegou a hora de responder as perguntas mais básicas sobre Java. Ao término desse capítulo, você será
capaz de:

   • responder o que é Java;
   • mostrar as vantagens e desvantagens do Java;
   • entender bem o conceito de máquina virtual;
   • compilar e executar um programa simples.


 2.1 - Java
   Entender um pouco da história da plataforma Java é essencial para enxergar os motivos que a levaram ao
sucesso.

   Quais eram os seus maiores problemas quando programava na década de 1990?

   • ponteiros?
   • gerenciamento de memória?
   • organização?
   • falta de bibliotecas?
   • ter de reescrever parte do código ao mudar de sistema operacional?
   • custo financeiro de usar a tecnologia?

    A linguagem Java resolve bem esses problemas, que até então apareciam com frequência nas outras lin-
guagens. Alguns desses problemas foram particularmente atacados porque uma das grandes motivações para
a criação da plataforma Java era de que essa linguagem fosse usada em pequenos dispositivos, como tvs,
video-cassetes, aspiradores, liquidificadores e outros. Apesar disso a linguagem teve seu lançamento focado
no uso em clientes web (browsers) para rodar pequenas aplicações (applets). Hoje em dia esse não é o grande
mercado do Java: apesar de ter sido idealizado com um propósito e lançado com outro, o Java ganhou destaque
no lado do servidor.

   O Java é desenvolvido e mantido pela Sun (http://www.sun.com) através de um comitê (http://www.jcp.
org) e seu site principal é o http://java.sun.com. (java.com é um site mais institucional, voltado ao consumidor
de produtos e usuários leigos, não desenvolvedores). Com a compra da Sun pela Oracle em 2009, muitas URLs
e nomes tem sido trocados para refletir a marca da Oracle.

                                                       3


[PAGINA 16]
                                                       Material do Treinamento Java e Orientação a Objetos




             Breve história do Java
            A Sun criou um time (conhecido como Green Team) para desenvolver inovações tecnológicas em
            1992. Esse time foi liderado por James Gosling, considerado o pai do Java. O time voltou com a
            idéia de criar um interpretador (já era uma máquina virtual, veremos o que é isso mais a frente) para
            pequenos dispositivos, facilitando a reescrita de software para aparelhos eletrônicos, como vídeo
            cassete, televisão e aparelhos de TV a cabo.
            A idéia não deu certo. Tentaram fechar diversos contratos com grandes fabricantes de eletrônicos,
            como Panasonic, mas não houve êxito devido ao conflito de interesses e custos. Hoje, sabemos
            que o Java domina o mercado de aplicações para celulares com mais de 2.5 bilhões de dispositivos
            compatíveis, porém em 1994 ainda era muito cedo para isso.
            Com o advento da web, a Sun percebeu que poderia utilizar a idéia criada em 1992 para rodar
            pequenas aplicações dentro do browser. A semelhança era que na internet havia uma grande
            quantidade de sistemas operacionais e browsers, e com isso seria grande vantagem poder pro-
            gramar numa única linguagem, independente da plataforma. Foi aí que o Java 1.0 foi lançado:
            focado em transformar o browser de apenas um cliente fino (thin client ou terminal burro) para uma
            aplicação que possa também realizar operações, não apenas renderizar html.
            Atualmente os applets realmente não são o foco da Sun. É curioso notar que a tecnologia Java
            nasceu com um objetivo em mente, foi lançado com outro, mas, no final, decolou mesmo no desen-
            volvimento de aplicações do lado do servidor. Sorte?
            Você pode ler a história da linguagem Java em: http://java.sun.com/java2/whatis/1996/
            storyofjava.html
            E um vídeo interessante: http://tinyurl.com/histjava
            Em 2009 a Oracle comprou a Sun, fortalecendo a marca. A Oracle sempre foi, junto com a IBM,
            uma das empresas que mais investiram e fizeram negócios através do uso da plataforma Java.


   No Brasil, diversos grupos de usuários se formaram para tentar disseminar o conhecimento da linguagem.
Um deles é o GUJ (http://www.guj.com.br), uma comunidade virtual com artigos, tutoriais e fórum para tirar
dúvidas, o maior em língua portuguesa com mais de cem mil usuários e 1 milhão de mensagens.

   Encorajamos todos os alunos a usar muito os fóruns do mesmo, pois é uma das melhores maneiras para
achar soluções para pequenos problemas que acontecem com grande freqüência.


 2.2 - Máquina Virtual
   Em uma linguagem de programação como C e Pascal, temos a seguinte situação quando vamos compilar
um programa:




   O código fonte é compilado para código de máquina específico de uma plataforma e sistema operacional.
Muitas vezes o próprio código fonte é desenvolvido visando uma única plataforma!

   Esse código executável (binário) resultante será executado pelo sistema operacional e, por esse motivo, ele
deve saber conversar com o sistema operacional em questão.




                                                                  Capítulo 2 - O que é Java - Máquina Virtual - Página 4


[PAGINA 17]
                                                        Material do Treinamento Java e Orientação a Objetos




     Isto é, temos um código executável para cada sistema operacional. É necessário compilar uma vez para
Windows, outra para o Linux, e assim por diante, caso a gente queira que esse nosso software possa ser
utilizado em várias plataformas. Esse é o caso de aplicativos como o OpenOffice, Firefox e outros.

    Como foi dito anteriormente, na maioria das vezes, a sua aplicação se utiliza das bibliotecas do sistema
operacional, como, por exemplo, a de interface gráfica para desenhar as “telas”. A biblioteca de interface gráfica
do Windows é bem diferente das do Linux: como criar então uma aplicação que rode de forma parecida nos
dois sistemas operacionais?

   Precisamos reescrever um mesmo pedaço da aplicação para diferentes sistemas operacionais, já que eles
não são compatíveis.

   Já o Java utiliza do conceito de máquina virtual, onde existe, entre o sistema operacional e a aplicação,
uma camada extra responsável por “traduzir” - mas não apenas isso - o que sua aplicação deseja fazer para as
respectivas chamadas do sistema operacional onde ela está rodando no momento:




   Dessa forma, a maneira com a qual você abre uma janela no Linux ou no Windows é a mesma: você
ganha independência de sistema operacional. Ou, melhor ainda, independência de plataforma em geral: não é
preciso se preocupar em qual sistema operacional sua aplicação está rodando, nem em que tipo de máquina,
configurações, etc.

    Repare que uma máquina virtual é um conceito bem mais amplo que o de um interpretador. Como o próprio
nome diz, uma máquina virtual é como um “computador de mentira": tem tudo que um computador tem. Em
outras palavras, ela é responsável por gerenciar memória, threads, a pilha de execução, etc.

   Sua aplicação roda sem nenhum envolvimento com o sistema operacional! Sempre conversando apenas
com a Java Virtual Machine (JVM).

                                                                   Capítulo 2 - O que é Java - Máquina Virtual - Página 5


[PAGINA 18]
                                                       Material do Treinamento Java e Orientação a Objetos




    Essa característica é interessante: como tudo passa pela JVM, ela pode tirar métricas, decidir onde é melhor
alocar a memória, entre outros. Uma JVM isola totalmente a aplicação do sistema operacional. Se uma JVM
termina abruptamente, só as aplicações que estavam rodando nela irão terminar: isso não afetará outras JVMs
que estejam rodando no mesmo computador, nem afetará o sistema operacional.

    Essa camada de isolamento também é interessante quando pensamos em um servidor que não pode se
sujeitar a rodar código que possa interferir na boa execução de outras aplicações.

    Essa camada, a máquina virtual, não entende código java, ela entende um código de máquina específico.
Esse código de máquina é gerado por um compilador java, como o javac, e é conhecido por “bytecode”, pois
existem menos de 256 códigos de operação dessa linguagem, e cada “opcode” gasta um byte. O compilador
Java gera esse bytecode que, diferente das linguagens sem máquina virtual, vai servir para diferentes sistemas
operacionais, já que ele vai ser “traduzido” pela JVM.


             Write once, run anywhere
            Esse é um slogan que a Sun usa para o Java, já que você não precisa reescrever partes da sua
            aplicação toda vez que quiser mudar de sistema operacional.


 2.3 - Java lento? Hotspot e JIT
    Hotspot é a tecnologia que a JVM utiliza para detectar pontos quentes da sua aplicação: código que é
executado muito, provavelmente dentro de um ou mais loops. Quando a JVM julgar necessário, ela vai compilar
estes códigos para instruções realmente nativas da plataforma, tendo em vista que isso vai provavelmente
melhorar a performance da sua aplicação. Esse compilador é o JIT: Just inTime Compiler, o compilador que
aparece “bem na hora” que você precisa.

   Você pode pensar então: porque a JVM não compila tudo antes de executar a aplicação? É que teoricamente
compilar dinamicamente, a medida do necessário, pode gerar uma performance melhor. O motivo é simples:
imagine um .exe gerado pelo VisualBasic, pelo gcc ou pelo Delphi; ele é estático. Ele já foi otimizado baseado
em heurísticas, o compilador pode ter tomado uma decisão não tão boa.

    Já a JVM, por estar compilando dinamicamente durante a execução, pode perceber que um determinado
código não está com performance adequada e otimizar mais um pouco aquele trecho, ou ainda mudar a estra-
tégia de otimização. É por esse motivo que as JVMs mais recentes (como a do Mustang, Java 6), em alguns
casos, chega a ganhar, em muitos casos, de códigos C compilados com o GCC 3.x, se rodados durante um
certo tempo.


 2.4 - Versões do Java e a confusão do Java2
    Java 1.0 e 1.1 são as versões muito antigas do Java, mas já traziam bibliotecas importantes como o JDBC
e o java.io.

   Com o Java 1.2 houve um aumento grande no tamanho da API, e foi nesse momento em que trocaram a
nomenclatura de Java para Java2, com o objetivo de diminuir a confusão que havia entre Java e Javascript. Mas
lembre-se, não há versão “Java 2.0”, o 2 foi incorporado ao nome, tornando-se Java2 1.2.

   Depois vieram o Java2 1.3 e 1.4, e o Java 1.5 passou a se chamar Java 5, tanto por uma questão de
marketing e porque mudanças significativas na linguagem foram incluídas. É nesse momento que o “2” do
nome Java desaparece. Repare que para fins de desenvolvimento, o Java 5 ainda é referido como Java 1.5.



                                                          Capítulo 2 - O que é Java - Java lento? Hotspot e JIT - Página 6


[PAGINA 19]
                                                       Material do Treinamento Java e Orientação a Objetos




    Até a versão 1.4, existia um terceiro número (1.3.1, 1.4.1, 1.4.2, etc), indicando bug fixes e melhorias. A
partir do Java 5 existem apenas updates: Java 5 update 7, por exemplo.

    Hoje a última versão disponível do Java é a 6.0, lançada em 2006. Da versão 1.4 para a 5.0, a linguagem
sofreu muitas modificações, o que de certa forma fomentou a mudança no versionamento do Java. Já o Java
6.0 não trouxe nenhuma mudança na linguagem, mas trouxe mais recursos na API e muitas melhorias de
performance na VM.

   Existe compatibilidade para trás em todas as versões do Java. Um class gerado pelo javac da versão 1.2
precisa necessariamente rodar na JVM 6.0. Por isso, recomendamos sempre usar a última versão do Java para
usufruir das tecnologias mais modernas mas sem correr o risco de quebrar aplicações antigas.


 2.5 - JVM? JRE? JDK? O que devo baixar?
   O que você vai baixar no site do java?

   • JVM = apenas a virtual machine, esse download não existe, ela sempre vem acompanhada.

   • JRE = Java Runtime Environment, ambiente de execução Java, formado pela JVM e bibliotecas, tudo
     que você precisa para executar uma aplicação Java. Mas nós precisamos de mais.

   • JDK = Java Development Kit: Nós, desenvolvedores, faremos o download do JDK do Java SE (Standard
     Edition). Ele é formado pela JRE somado a ferramentas, como o compilador.


 2.6 - Onde usar e os objetivos do Java
    No decorrer do curso, você pode achar que o Java tem menro produtividade quando comparada com a
linguagem que você está acostumado.

   É preciso ficar claro que a premissa do Java não é a de criar sistemas pequenos, onde temos um ou dois
desenvolvedores, mais rapidamente que linguagens como php, perl, e outras.

    O foco da plataforma é outro: aplicações de médio a grande porte, onde o time de desenvolvedores tem
várias pessoas e sempre pode vir a mudar e crescer. Não tenha dúvidas que criar a primeira versão uma
aplicação usando Java, mesmo utilizando IDEs e ferramentas poderosas, será mais trabalhoso que muitas
linguagens script ou de alta produtividade. Porém, com uma linguagem orientada a objetos e madura como o
Java, será extremamente mais fácil e rápido fazer alterações no sistema, desde que você siga as boas práticas
e recomendações sobre design orientado a objetos.

    Além disso, a quantidade enorme de bibliotecas gratuitas para realizar os mais diversos trabalhos (tais como
relatórios, gráficos, sistemas de busca, geração de código de barra, manipulação de XML, tocadores de vídeo,
manipuladores de texto, persistência transparente, impressão, etc) é um ponto fortíssimo para adoção do Java:
você pode criar uma aplicação sofisticada, usando diversos recursos, sem precisar comprar um componente
específico, que costuma caro. O ecossistema do Java é enorme.

   Cada linguagem tem seu espaço e seu melhor uso. O uso do Java é interessante em aplicações que virão a
crescer, em que a legibilidade do código é importante, onde temos muita conectividade e se temos plataformas
(ambientes e sistemas operacionais) heterogêneos (Linux, Unix, OSX e Windows misturados).

    Você pode ver isso pela quantidade enorme de ofertas de emprego procurando desenvolvedores Java para
trabalhar com sistemas web e aplicações de integração no servidor.



                                               Capítulo 2 - O que é Java - JVM? JRE? JDK? O que devo baixar? - Página 7


[PAGINA 20]
                                                        Material do Treinamento Java e Orientação a Objetos




    Apesar disto, a Sun empenha-se em tentar popularizar o uso do Java em aplicações desktop, mesmo com o
fraco marketshare do Swing/AWT/SWT em relação às tecnologias concorrentes (em especial Microsoft .NET).


 2.7 - Especificação versus implementação
    Outro ponto importante: quando falamos de Java Virtual Machine, estamos falando de uma especificação.
Ela diz como o bytecode deve ser interpretado pela JVM. Quando fazemos o download no site da Sun, o que
vem junto é a Sun JVM. Em outras palavras, existem outras JVMs disponíveis, como a JRockit da BEA, a J9 da
IBM, entre outras.

   Isso é outro ponto interessante para as empresas. Caso não estejam gostando de algum detalhe da JVM da
Sun ou prefiram trabalhar com outra empresa, pagando por suporte, elas podem trocar de JVM com a garantia
absoluta de que todo o sistema continuará funcionando, tendo em vista que toda JVM deve ser certificada pela
Sun, provando a sua compatibilidade. Você nem precisa recompilar nenhuma de suas classes.

    Além de independência de hardware e sistema operacional, você tem a independência de vendor: graças
a idéia da JVM ser uma especificação e não um software.


 2.8 - Como o FJ-11 está organizado
   Java é uma linguagem simples: existem poucas regras, muito bem definidas.

    Já quebrar o paradigma procedural para mergulhar na orientação a objetos não é simples. Esse, e ganhar
fluência com a linguagem e API, são os objetivos do FJ-11.

    O começo pode ser um pouco frustrante: exemplos banais, controle de fluxo simples com o if, for, while
e criação de pequenos programas que nem ao menos captam dados do teclado. Apesar de isto tudo ser
necessário, é só nos 20% finais do curso que estaremos utilizando bibliotecas para, no final, criarmos um chat
entre duas máquinas que transferem Strings por TCP/IP. Neste ponto, teremos tudo que é necessário para
entender completamente como a API funciona, quem estende quem, e o porquê.

   Depois desse capítulo onde o Java, a JVM e primeiros conceitos são passados, veremos os comandos
básicos do java para controle de fluxo e utilização de variáveis do tipo primitivo. Criaremos classes para testar
esse pequeno aprendizado, sem saber exatamente o que é uma classe. Isso dificulta ainda mais a curva de
aprendizado, porém cada conceito será introduzido no momento considerado mais apropriado pelos instrutores.

   Passamos para o capítulo de orientação a objetos básico, mostrando os problemas do paradigma procedural
e a necessidade de algo diferente para resolvê-los. Atributos, métodos, variáveis do tipo referência e outros.
Passamos então para um pouco de arrays.

    Os capítulos de modificadores de acesso, herança, classes abstratas e interfaces demonstram o conceito
fundamental que o curso quer passar: encapsule, exponha o mínimo de suas classes, foque no que elas fazem,
no relacionamento entre elas. Com uma bom design, a codificação fica fácil e a modificação e expansão do
sistema também.

    No decorrer desses capítulos, o Eclipse é introduzido de forma natural, evitando-se ao máximo wizards e
menus, priorizando mostrar os chamaados code assists e quick fixes. Isso faz com que o Eclipse trabalhe de
forma simbiótica com o desenvolvedor, sem se intrometer, sem fazer mágica.

   Pacotes, javadoc, jars e java.lang apresentam os últimos conceitos fundamentais do Java, dando toda a
fundação para, então, passarmos a estudar as principais e mais utilizadas APIs do Java SE.



                                                 Capítulo 2 - O que é Java - Especificação versus implementação - Página 8


[PAGINA 21]
                                                     Material do Treinamento Java e Orientação a Objetos




   As APIs estudadas serão java.util, java.io e java.net. Todas elas usam e abusam dos conceitos vistos no
decorrer do curso, ajudando a sedimentá-los. Juntamente, temos os conceitos básicos do uso de Threads, e os
problemas e perigos da programação concorrente quando dados são compartilhados.

    Resumindo: o objetivo do curso é apresentar o Java ao mesmo tempo que os fundamentos da orientação a
objetos são introduzidos. Bateremos muito no ponto de dizer que o importante é como as classes se relacionam
e qual é o papel de cada uma, e não em como elas realizam as suas obrigações. Programe voltado à interface,
e não à implementação.


 2.9 - Compilando o primeiro programa
   Vamos para o nosso primeiro código! O programa que imprime uma linha simples.

   Para mostrar uma linha, podemos fazer:

System.out.println("Minha primeira aplicação Java!");


   Mas esse código não será aceito pelo compilador java. O Java é uma linguagem bastante burocrática, e
precisa de mais do que isso para iniciar uma execução. Veremos os detalhes e os porquês durante os próximos
capítulos. O mínimo que precisaríamos escrever é algo como:

1 class MeuPrograma {
2     public static void main(String[] args) {
3         System.out.println("Minha primeira aplicação Java!");
4     }
5 }



             Notação
           Todos os códigos apresentados na apostila estão formatados com recursos visuais para auxiliar a
           leitura e compreensão dos mesmos. Quando for digitar os códigos no computador, trate os códigos
           como texto simples.
           A numeração das linhas não faz parte do código e não deve ser digitada; é apenas um recurso
           didático. O Java é case sensitive: tome cuidado com maiúsculas e minúsculas.


   Após digitar o código acima, grave-o como MeuPrograma.java em algum diretório. Para compilar, você
deve pedir para que o compilador de Java da Sun, chamado javac, gere o bytecode correspondente ao seu
código Java.




    Depois de compilar, o bytecode foi gerado. Quando o sistema operacional listar os arquivos contidos no
diretório atual, você poderá ver que um arquivo .class foi gerado, com o mesmo nome da sua classe Java.

                                                  Capítulo 2 - O que é Java - Compilando o primeiro programa - Página 9


[PAGINA 22]
                                                    Material do Treinamento Java e Orientação a Objetos




             Assustado com o código?
           Para quem já tem uma experiência com Java, esse primeiro código é muito simples. Mas, se é
           seu primeiro código em Java, pode ser um pouco traumatizante. Não deixe de ler o prefácio do
           curso, que deixará você mais tranqüilo em relação a curva de aprendizado da linguagem, e a como
           o curso está organizado.


             Preciso sempre programar usando o Notepad ou similar?
           Não é necessário digitar sempre seu programa em um simples aplicativo como o Notepad. Você
           pode usar um editor que tenha syntax highlighting e outros benefícios.
           Mas, no começo, é interessante você usar algo que não possua ferramentas, para que você possa
           se acostumar com os erros de compilação, sintaxe e outros. Depois do capítulo de polimorfismo
           e herança sugerimos a utilização do Eclipse (http://www.eclipse.org), a IDE líder no mercado, e
           gratuita. Existe um capítulo a parte para o uso do Eclipse nesta apostila.
           No Linux, recomendamos o uso do gedit ou do kate. No Windows, você pode usar o Notepad++ ou
           o TextPad. No Mac, TextWrangler ou TextMate.


 2.10 - Executando seu primeiro programa
    Os procedimentos para executar seu programa são muito simples. O javac é o compilador Java, e o java é
o responsável por invocar a máquina virtual para interpretar o seu programa.




  Ao executar, pode ser que a acentuação resultante saia errada devido a algumas configurações que deixa-
mos de fazer. Sem problemas.


 2.11 - O que aconteceu?

1 class MeuPrograma {
2     public static void main(String[] args) {
3
4         // miolo do programa começa aqui!
5         System.out.println("Minha primeira aplicação Java!!");
6         // fim do miolo do programa
7
8     }
9 }


    O miolo do programa é o que será executado quando chamamos a máquina virtual. Por enquanto, todas
as linhas anteriores, onde há a declaração de uma classe e a de um método, não importam para nós nesse
momento. Mas devemos saber que toda aplicação Java começa por um ponto de entrada, e este ponto de
entrada é o método main.

   Ainda não sabemos o que é método, mas veremos no capítulo 4. Até lá, não se preocupe com essas
declarações. Sempre que um exercício for feito, o código que nos importa sempre estará nesse miolo.

                                              Capítulo 2 - O que é Java - Executando seu primeiro programa - Página 10


[PAGINA 23]
                                                       Material do Treinamento Java e Orientação a Objetos




    No caso do nosso código, a linha do System.out.println faz com que o conteúdo entre aspas seja colocado
na tela.


    2.12 - Para saber mais: como é o bytecode?
    O MeuPrograma.class gerado não é legível por seres humanos (não que seja impossível). Ele está escrito
no formato que a virtual machine sabe entender e que foi especificado que ela entendesse.

    É como um assembly, escrito para esta máquina em específico. Podemos ler os mnemônicos utilizando a
ferramenta javap que acompanha o JDK:


javap -c MeuPrograma


     E a saída:


MeuPrograma();
  Code:
   0:   aload_0
   1:   invokespecial       #1; //Method java/lang/Object."<init>":()V
   4:   return

public static void main(java.lang.String[]);
  Code:
   0:   getstatic       #2; //Field java/lang/System.out:Ljava/io/PrintStream;
   3:   ldc     #3; //String Minha primeira aplicaão Java!!
   5:   invokevirtual   #4; //Method java/io/PrintStream.println:(Ljava/lang/String;)V
   8:   return

}


     É o código acima, que a JVM sabe ler. É o “código de máquina”, da máquina virtual.

    Um bytecode pode ser revertido para o .java original (com perda de comentários e nomes de variáveis
locais). Caso seu software vá virar um produto de prateleira, é fundamental usar um ofuscador no seu código,
que vai embaralhar classes, métodos e um monte de outros recursos (indicamos o http://proguard.sf.net).


    2.13 - Exercícios: Modificando o Hello World

1) Altere seu programa para imprimir uma mensagem diferente.

2) Altere seu programa para imprimir duas linhas de texto usando duas linhas de código System.out.

3) Sabendo que os caracteres \n representam uma quebra de linhas, imprima duas linhas de texto usando uma
   única linha de código System.out.




                                              Capítulo 2 - O que é Java - Para saber mais: como é o bytecode? - Página 11


[PAGINA 24]
                                                      Material do Treinamento Java e Orientação a Objetos




 2.14 - O que pode dar errado?
   Muitos erros podem ocorrer no momento que você rodar seu primeiro código. Vamos ver alguns deles:

   Código:

1 class X {
2     public static void main (String[] args) {
3         System.out.println("Falta ponto e vírgula")
4     }
5 }


   Erro:


X.java:4: ’;’ expected
        }
        ^
1 error


   Esse é o erro de compilação mais comum: aquele onde um ponto e vírgula fora esquecido. Outros erros de
compilação podem ocorrer se você escreveu palavras chaves (as que colocamos em negrito) em maiúsculas,
esqueceu de abrir e fechar as {}, etc.

   Durante a execução, outros erros podem aparecer:

    - Se você declarar a classe como X, compilá-la e depois tentar usá-la como x minúsculo (java x), o Java te
avisa:


Exception in thread "main" java.lang.NoClassDefFoundError: X (wrong name: x)


   - Se tentar acessar uma classe no diretório ou classpath errado, ou se o nome estiver errado, ocorrerá o
seguinte erro:


Exception in thread "main" java.lang.NoClassDefFoundError: X


   - Se esquecer de colocar static ou o argumento String[] args no método main:


Exception in thread "main" java.lang.NoSuchMethodError: main


   Por exemplo:

1 class X {
2     public void main (String[] args) {
3         System.out.println("Faltou o static");
4     }
5 }



                                                         Capítulo 2 - O que é Java - O que pode dar errado? - Página 12


[PAGINA 25]
                                                    Material do Treinamento Java e Orientação a Objetos




   - Se não colocar o método main como public:


Main method not public.


   Por exemplo:

1 class X {
2     static void main (String[] args) {
3         System.out.println("Faltou o public");
4     }
5 }



 2.15 - Um pouco mais...

1) Procure um colega, ou algum conhecido, que esteja em um projeto Java. Descubra porque Java foi escolhido
   como tecnologia. O que é importante para esse projeto e o que acabou fazendo do Java a melhor escolha?


 2.16 - Exercícios adicionais

1) Um arquivo fonte Java deve sempre ter a extensão .java, ou o compilador o rejeitará. Além disso, existem
   algumas outras regras na hora de dar o nome de um arquivo Java. Experimente gravar o código deste
   capítulo com OutroNome.java ou algo similar. Compile e verifique o nome do arquivo gerado. Como executar
   a sua aplicação agora?




                                                             Capítulo 2 - O que é Java - Um pouco mais... - Página 13


[PAGINA 26]
                                                                                             C APÍTULO    3

Variáveis primitivas e Controle de fluxo
                                                                 “Péssima idéia, a de que não se pode mudar”
                                                                                                  – Montaigne

   Aprenderemos a trabalhar com os seguintes recursos da linguagem Java:

   • declaração, atribuição de valores, casting e comparação de variáveis;
   • controle de fluxo através de if e else;
   • instruções de laço for e while, controle de fluxo com break e continue.


 3.1 - Declarando e usando variáveis
   Dentro de um bloco, podemos declarar variáveis e usá-las. Em Java, toda variável tem um tipo que não
pode ser mudado, uma vez que declarado:


tipoDaVariavel nomeDaVariavel;


   Por exemplo, é possível ter uma idade que guarda um número inteiro:

int idade;


   Com isso, você declara a variável idade, que passa a existir a partir daquela linha. Ela é do tipo int, que
guarda um número inteiro. A partir de agora, você pode usá-la, primeiramente atribuindo valores.

   A linha a seguir é a tradução de: “idade deve valer agora quinze”.

idade = 15;


              Comentários em Java
             Para fazer um comentário em java, você pode usar o // para comentar até o final da linha, ou então
             usar o /* */ para comentar o que estiver entre eles.

              /* comentário daqui,

             ate aqui */

             // uma linha de comentário sobre a idade
             int idade;



                                                      14


[PAGINA 27]
                                                          Material do Treinamento Java e Orientação a Objetos




    Além de atribuir, você pode utilizar esse valor. O código a seguir declara novamente a variável idade com
valor 15 e imprime seu valor na saída padrão através da chamada a System.out.println.

// declara a idade
int idade;
idade = 15;

// imprime a idade
System.out.println(idade);


   Por fim, podemos utilizar o valor de uma variável para algum outro propósito, como alterar ou definir uma
segunda variável. O código a seguir cria uma variável chamada idadeNoAnoQueVem com valor de idade mais
um.

// calcula a idade no ano seguinte
int idadeNoAnoQueVem;
idadeNoAnoQueVem = idade + 1;


   No mesmo momento que você declara uma variável, também é possível inicializá-la por praticidade:

int idade = 15;


   Você pode usar os operadores +, -, / e * para operar com números, sendo eles responsáveis pela adi-
ção, subtração, divisão e multiplicação, respectivamente. Além desses operadores básicos, há o operador %
(módulo) que nada mais mais é que o resto de uma divisão inteira. Veja alguns exemplos:

int quatro = 2 + 2;
int tres = 5 – 2;

int oito = 4 * 2;
int dezesseis = 64 / 4;

int um = 5 % 2; // 5 dividido por 2 dá 2 e tem resto 1;
                // o operador % pega o resto da divisão inteira




                              Capítulo 3 - Variáveis primitivas e Controle de fluxo - Declarando e usando variáveis - Página 15


[PAGINA 28]
                                                           Material do Treinamento Java e Orientação a Objetos




                Como rodar esses códigos?
            Você deve colocar esses trechos de código dentro do método main, que vimos no capítulo anterior.
            Isto é, isso deve ficar no miolo do programa. Use bastante System.out.println, dessa forma você
            pode ver algum resultado, caso contrário, ao executar a aplicação, nada aparecerá.
            Por exemplo, para imprimir a idade e a idadeNoAnoQueVem podemos escrever o seguinte programa
            de exemplo:

            class TestaIdade {


                  public static void main(String[] args) {
                      // imprime a idade
                      System.out.println(idade);

                      // gera uma idade no ano seguinte
                      int idadeNoAnoQueVem;
                      idadeNoAnoQueVem = idade + 1;

                      // imprime a idade
                      System.out.println(idadeNoAnoQueVem);
                  }
            }




   Representar números inteiros é fácil, mas como guardar valores reais, tais como frações de números inteiros
e outros? Outro tipo de variável muito utilizado é o double, que armazena um número com ponto flutuante (e
que também pode armazenar um número inteiro).

double pi = 3.14;
double x = 5 * 10;


   O tipo boolean armazena um valor verdadeiro ou falso, e só: nada de números, palavras ou endereços,
como em algumas outras linguagens.

boolean verdade = true;


   true e false são palavras reservadas do Java. É comum que um boolean seja determinado através de uma
expressão booleana, isto é, um trecho de código que retorna um booleano, como o exemplo:

int idade = 30;
boolean menorDeIdade = idade < 18;


   O tipo char guarda um, e apenas um, caractere. Esse caractere deve estar entre aspas simples. Não se
esqueça dessas duas características de uma variável do tipo char! Por exemplo, ela não pode guardar um
código como ” pois o vazio não é um caractere!

char letra = ’a’;
System.out.println(letra);



                               Capítulo 3 - Variáveis primitivas e Controle de fluxo - Declarando e usando variáveis - Página 16


[PAGINA 29]
                                                              Material do Treinamento Java e Orientação a Objetos




   Variáveis do tipo char são pouco usadas no dia a dia. Veremos mais a frente o uso das Strings, que usamos
constantemente, porém estas não são definidas por um tipo primitivo.


 3.2 - Tipos primitivos e valores
    Esses tipos de variáveis são tipos primitivos do Java: o valor que elas guardam são o real conteúdo da
variável. Quando você utilizar o operador de atribuição = o valor será copiado.

int i = 5; // i recebe uma cópia do valor 5
int j = i; // j recebe uma cópia do valor de i
i = i + 1; // i vira 6, j continua 5


   Aqui, i fica com o valor de 6. Mas e j? Na segunda linha, j está valendo 5. Quando i passa a valer 6, será
que j também muda de valor? Não, pois o valor de um tipo primitivo sempre é copiado.

   Apesar da linha 2 fazer j = i, a partir desse momento essas variáveis não tem relação nenhuma: o que
acontece com uma, não reflete em nada com a outra.

             Outros tipos primitivos
            Vimos aqui os tipos primitivos que mais aparecem. O Java tem outros, que são o byte, short, long
            e float.
            Cada tipo possui características especiais que, para um programador avançado, podem fazer muita
            diferença.


 3.3 - Exercícios: Variáveis e tipos primitivos

1) Na empresa onde trabalhamos, há tabelas com o quanto foi gasto em cada mês. Para fechar o balanço do
   primeiro trimestre, precisamos somar o gasto total. Sabendo que, em Janeiro, foram gastos 15000 reais, em
   Fevereiro, 23000 reais e em Março, 17000 reais, faça um programa que calcule e imprima o gasto total no
   trimestre. Siga esses passos:

   a) Crie uma classe chamada BalancoTrimestral com um bloco main, como nos exemplos anteriores;
   b) Dentro do main (o miolo do programa), declare uma variável inteira chamada gastosJaneiro e inicialize-a
      com 15000;
   c) Crie também as variáveis gastosFevereiro e gastosMarco, inicializando-as com 23000 e 17000, respec-
      tivamente, utilize uma linha para cada declaração;
   d) Crie uma variável chamada gastosTrimestre e inicialize-a com a soma das outras 3 variáveis:

       int gastosTrimestre = gastosJaneiro + gastosFevereiro + gastosMarco;


   e) Imprima a variável gastosTrimestre.

2) (opcional) Adicione código (sem alterar as linhas que já existem) no programa a seguir para imprimir o
   resultado:
   Resultado: 15, 15.1, y, true

   class ExercicioSimples {

                                       Capítulo 3 - Variáveis primitivas e Controle de fluxo - Tipos primitivos e valores - Página 17


[PAGINA 30]
                                                                  Material do Treinamento Java e Orientação a Objetos




       public static void main(String[] args) {

               int i = 10;
               double d = 5;
               char c = ’t’;
               boolean b = true;

               // imprime concatenando diversas variáveis
               System.out.println("Resultado: " + i + ", " + d + ", " + c + ", " + b);
       }
   }



 3.4 - Discussão em aula: convenções de código e código legível
   Discuta com o instrutor e seus colegas sobre convenções de código Java. Por que existem? Por que são
importantes?

   Discuta também as vantagens de se escrever código fácil de ler e se evitar comentários em excesso.

   (Dica: procure por code conventions no campo de busca do site http://java.sun.com.)


 3.5 - Casting e promoção
   Alguns valores são incompatíveis se você tentar fazer uma atribuição direta. Enquanto um número real
costuma ser representado em uma variável do tipo double, tentar atribuir ele a uma variável int não funciona
porque é um código que diz: “i deve valer d”, mas não se sabe se d realmente é um número inteiro ou não.

double d = 3.1415;
int i = d; // não compila


   O mesmo ocorre no seguinte trecho:

int i = 3.14;


   O mais interessante, é que nem mesmo o seguinte código compila:

double d = 5; // ok, o double pode conter um número inteiro
int i = d; // não compila


   Apesar de 5 ser um bom valor para um int, o compilador não tem como saber que valor estará dentro desse
double no momento da execução. Esse valor pode ter sido digitado pelo usuário, e ninguém vai garantir que
essa conversão ocorra sem perda de valores.

   Já no caso a seguir, é o contrário:

int i = 5;
double d2 = i;


           Capítulo 3 - Variáveis primitivas e Controle de fluxo - Discussão em aula: convenções de código e código legível - Página 18


[PAGINA 31]
                                                        Material do Treinamento Java e Orientação a Objetos




     O código acima compila sem problemas, já que um double pode guardar um número com ou sem ponto
flutuante. Todos os inteiros representados por uma variável do tipo int podem ser guardados em uma variável
double, então não existem problemas no código acima.

    Às vezes, precisamos que um número quebrado seja arredondado e armazenado num número inteiro. Para
fazer isso sem que haja o erro de compilação, é preciso ordenar que o número quebrado seja moldado (casted)
como um número inteiro. Esse processo recebe o nome de casting.

double d3 = 3.14;
int i = (int) d3;


   O casting foi feito para moldar a variável d3 como um int. O valor de i agora é 3.

   O mesmo ocorre entre valores int e long.

long x = 10000;
int i = x; // não compila, pois pode estar perdendo informação


   E, se quisermos realmente fazer isso, fazemos o casting:

long x = 10000;
int i = (int) x;



            Casos não tão comuns de casting e atribuição
           Alguns castings aparecem também:

            float x = 0.0;


           O código acima não compila pois todos os literais com ponto flutuante são considerados double
           pelo Java. E float não pode receber um double sem perda de informação, para fazer isso
           funcionar podemos escrever o seguinte:

            float x = 0.0f;


           A letra f, que pode ser máiscula ou minúscula, indica que aquele literal deve ser tratado como float.
           Outro caso, que é mais comum:

            double d = 5;

           float f = 3;

           float x = f + (float) d;

           Você precisa do casting porque o Java faz as contas e vai armazenando sempre no maior tipo que
           apareceu durante as operações, no caso o double.
           E, uma observação: no mínimo, o Java armazena o resultado em um int, na hora de fazer as
           contas.
           Até casting com variáveis do tipo char podem ocorrer. O único tipo primitivo que não pode ser
           atribuído a nenhum outro tipo é o boolean.

                                       Capítulo 3 - Variáveis primitivas e Controle de fluxo - Casting e promoção - Página 19


[PAGINA 32]
                                                      Material do Treinamento Java e Orientação a Objetos




 Castings possíveis
Abaixo estão relacionados todos os casts possíveis na linguagem Java, mostrando a conversão de
um valor para outro. A indicação Impl. quer dizer que aquele cast é implícito e automático, ou
seja, você não precisa indicar o cast explicitamente (lembrando que o tipo boolean não pode ser
convertido para nenhum outro tipo).




 Tamanho dos tipos
Na tabela abaixo, estão os tamanhos de cada tipo primitivo do Java.




 3.6 - O If-Else
   A sintaxe do if no Java é a seguinte:

if (condicaoBooleana) {
    codigo;
}


   Uma condição booleana é qualquer expressão que retorne true ou false. Para isso, você pode usar os
operadores <, >, <=, >= e outros. Um exemplo:

int idade = 15;

                                                Capítulo 3 - Variáveis primitivas e Controle de fluxo - O If-Else - Página 20


[PAGINA 33]
                                                      Material do Treinamento Java e Orientação a Objetos




if (idade < 18) {
    System.out.println("Não pode entrar");
}


   Além disso, você pode usar a cláusula else para indicar o comportamento que deve ser executado no caso
da expressão booleana ser falsa:

int idade = 15;
if (idade < 18) {
    System.out.println("Não pode entrar");
} else {
    System.out.println("Pode entrar");
}


   Você pode concatenar expressões booleanas através dos operadores lógicos “E” e “OU”. O “E” é repre-
sentado pelo && e o “OU” é representado pelo ||.

   Um exemplo seria verificar se ele tem menos de 18 anos e se ele não é amigo do dono:

int idade = 15;
boolean amigoDoDono = true;
if (idade < 18 && amigoDoDono == false) {
    System.out.println("Não pode entrar");
}
else {
    System.out.println("Pode entrar");
}


    Esse código poderia ficar ainda mais legível, utilizando-se o operador de negação, o !. Esse operador
transforma o resultado de uma expressão booleana de false para true e vice versa.

1 int idade = 15;
2 boolean amigoDoDono = true;
3 if (idade < 18 && !amigoDoDono) {
4     System.out.println("Não pode entrar");
5 }
6 else {
7     System.out.println("Pode entrar");
8 }


   Repare na linha 3 que o trecho amigoDoDono == false virou !amigoDoDono. Eles têm o mesmo valor.

   Para comparar se uma variável tem o mesmo valor que outra variável ou valor, utilizamos o operador ==.
Repare que utilizar o operador = dentro de um if vai retornar um erro de compilação, já que o operador = é o
de atribuição.

int mes = 1;
if (mes == 1) {
    System.out.println("Você deveria estar de férias");
}


                                                Capítulo 3 - Variáveis primitivas e Controle de fluxo - O If-Else - Página 21


[PAGINA 34]
                                                       Material do Treinamento Java e Orientação a Objetos




 3.7 - O While
    O while é um comando usado para fazer um laço (loop), isto é, repetir um trecho de código algumas vezes.
A idéia é que esse trecho de código seja repetido enquanto uma determinada condição permanecer verdadeira.

int idade = 15;
while (idade < 18) {
    System.out.println(idade);
    idade = idade + 1;
}


    O trecho dentro do bloco do while será executado até o momento em que a condição idade < 18 passe a
ser falsa. E isso ocorrerá exatamente no momento em que idade == 18, o que não o fará imprimir 18.

int i = 0;
while (i < 10) {
    System.out.println(i);
    i = i + 1;
}


   Já o while acima imprime de 0 a 9.


 3.8 - O For
    Outro comando de loop extremamente utilizado é o for. A idéia é a mesma do while: fazer um trecho
de código ser repetido enquanto uma condição continuar verdadeira. Mas além disso, o for isola também um
espaço para inicialização de variáveis e o modificador dessas variáveis. Isso faz com que fiquem mais legíveis,
as variáveis que são relacionadas ao loop:

for (inicializacao; condicao; incremento) {
    codigo;
}


   Um exemplo é o a seguir:

for (int i = 0; i < 10; i = i + 1) {
    System.out.println("olá!");
}


   Repare que esse for poderia ser trocado por:

int i = 0;
while (i < 10) {
    System.out.println("olá!");
    i = i + 1;
}




                                                  Capítulo 3 - Variáveis primitivas e Controle de fluxo - O While - Página 22


[PAGINA 35]
                                                        Material do Treinamento Java e Orientação a Objetos




    Porém, o código do for indica claramente que a variável i serve, em especial, para controlar a quantidade
de laços executados. Quando usar o for? Quando usar o while? Depende do gosto e da ocasião.


             Pós incremento ++
            i = i + 1 pode realmente ser substituído por i++ quando isolado, porém, em alguns casos, temos
            essa instrução envolvida em, por exemplo, uma atribuição:

            int i = 5;

            int x = i++;

            Qual é o valor de x? O de i, após essa linha, é 6.
            O operador ++, quando vem após a variável, retorna o valor antigo, e incrementa (pós incremento),
            fazendo x valer 5.
            Se você tivesse usado o ++ antes da variável (pré incremento), o resultado seria 6:

            int i = 5;

            int x = ++i; // aqui x valera 6




 3.9 - Controlando loops
    Apesar de termos condições booleanas nos nossos laços, em algum momento, podemos decidir parar o
loop por algum motivo especial sem que o resto do laço seja executado.

for (int i = x; i < y; i++) {
    if (i % 19 == 0) {
        System.out.println("Achei um número divisível por 19 entre x e y");
        break;
    }
}


  O código acima vai percorrer os números de x a y e parar quando encontrar um número divisível por 19,
uma vez que foi utilizada a palavra chave break.

   Da mesma maneira, é possível obrigar o loop a executar o próximo laço. Para isso usamos a palavra chave
continue.


for (int i = 0; i < 100; i++) {
    if (i > 50 && i < 60) {
        continue;
    }
    System.out.println(i);
}


   O código acima não vai imprimir alguns números. (Quais exatamente?)




                                         Capítulo 3 - Variáveis primitivas e Controle de fluxo - Controlando loops - Página 23


[PAGINA 36]
                                                         Material do Treinamento Java e Orientação a Objetos




 3.10 - Escopo das variáveis
    No Java, podemos declarar variáveis a qualquer momento. Porém, dependendo de onde você as declarou,
ela vai valer de um determinado ponto a outro.

// aqui a variável i não existe
int i = 5;
// a partir daqui ela existe


   O escopo da variável é o nome dado ao trecho de código em que aquela variável existe e onde é possível
acessá-la.

   Quando abrimos um novo bloco com as chaves, as variáveis declaradas ali dentro só valem até o fim
daquele bloco.

// aqui a variável i não existe
int i = 5;
// a partir daqui ela existe
while (condicao) {
    // o i ainda vale aqui
    int j = 7;
    // o j passa a existir
}
// aqui o j não existe mais, mas o i continua dentro do escopo


   No bloco acima, a variável j pára de existir quando termina o bloco onde ela foi declarada. Se você tentar
acessar uma variável fora de seu escopo, ocorrerá um erro de compilação.




   O mesmo vale para um if:

if (algumBooleano) {
    int i = 5;
}
else {
    int i = 10;
}
System.out.println(i); // cuidado!


    Aqui a variável i não existe fora do if e do else! Se você declarar a variável antes do if, vai haver outro
erro de compilação: dentro do if e do else a variável está sendo redeclarada! Então o código para compilar e
fazer sentido fica:




                                       Capítulo 3 - Variáveis primitivas e Controle de fluxo - Escopo das variáveis - Página 24


[PAGINA 37]
                                                         Material do Treinamento Java e Orientação a Objetos




int i;
if (algumBooleano) {
    i = 5;
}
else {
    i = 10;
}
System.out.println(i);


   Uma situação parecida pode ocorrer com o for:

for (int i = 0; i < 10; i++) {
    System.out.println("olá!");
}
System.out.println(i); // cuidado!


   Neste for, a variável i morre ao seu término, não podendo ser acessada de fora do for, gerando um erro
de compilação. Se você realmente quer acessar o contador depois do loop terminar, precisa de algo como:

int i;
for (i = 0; i < 10; i++) {
    System.out.println("olá!");
}
System.out.println(i);



 3.11 - Um bloco dentro do outro
   Um bloco também pode ser declarado dentro de outro. Isto é, um if dentro de um for, ou um for dentro de
um for, algo como:

while (condicao) {
    for (int i = 0; i < 10; i++) {
        // código
    }
}



 3.12 - Para saber mais

1) Vimos apenas os comandos mais usados para controle de fluxo. O Java ainda possui o do..while e o
   switch. Pesquise sobre eles e diga quando é interessante usar cada um deles.

2) Algumas vezes, temos vários laços encadeados. Podemos utilizar o break para quebrar o laço mais interno.
   Mas, se quisermos quebrar um laço mais externo, teremos de encadear diversos ifs e seu código ficará uma
   bagunça. O Java possui um artifício chamado labeled loops; pesquise sobre eles.

3) O que acontece se você tentar dividir um número inteiro por 0? E por 0.0?




                                   Capítulo 3 - Variáveis primitivas e Controle de fluxo - Um bloco dentro do outro - Página 25


[PAGINA 38]
                                                              Material do Treinamento Java e Orientação a Objetos




4) Existe um caminho entre os tipos primitivos que indicam se há a necessidade ou não de casting entre os
   tipos. Por exemplo, int -> long -> double (um int pode ser tratado como um double, mas não o contrário).
   Pesquise (ou teste), e posicione os outros tipos primitivos nesse fluxo.

5) Além dos operadores de incremento, existem os de decremento, como --i e i--. Além desses, você pode
   usar instruções do tipo i += x e i -= x, o que essas instruções fazem? Teste.


 3.13 - Exercícios: Fixação de sintaxe
    Mais exercícios de fixação de sintaxe. Para quem já conhece um pouco de Java, pode ser muito simples; mas
recomendamos fortemente que você faça os exercícios para se acostumar com erros de compilação, mensagens
do javac, convenção de código, etc...

    Apesar de extremamente simples, precisamos praticar a sintaxe que estamos aprendendo. Para cada exer-
cício, crie um novo arquivo com extensão .java, e declare aquele estranho cabeçalho, dando nome a uma classe
e com um método main dentro dele:

class ExercicioX {
    public static void main(String[] args) {
        // seu exercicio vai aqui
    }
}


   Não copie e cole de um exercício já existente! Aproveite para praticar.

1) Imprima todos os números de 150 a 300.

2) Imprima a soma de 1 até 1000.

3) Imprima todos os múltiplos de 3, entre 1 e 100.

4) Imprima os fatoriais de 1 a 10.
   O fatorial de um número n é n * n-1 * n-2 ... até n = 1. Lembre-se de utilizar os parênteses. O fatorial de 0 é
   1 O fatorial de 1 é (0!) * 1 = 1 O fatorial de 2 é (1!) * 2 = 2 O fatorial de 3 é (2!) * 3 = 6 O fatorial de 4 é (3!) *
   4 = 24
   Faça um for que inicie uma variável n (número) como 1 e fatorial (resultado) como 1 e varia n de 1 até 10:

   for (int n=1, fatorial=1; n <= 10; n++) {



5) Aumente a quantidade de números que terão os fatoriais impressos, até 20, 30, 40. Em um determinado
   momento, além desse cálculo demorar, vai começar a mostrar respostas completamente erradas. Porque?
   Mude de int para long, e você poderá ver alguma mudança.

6) (opcional) Imprima os primeiros números da série de Fibonacci até passar de 100. A série de Fibonacci é a
   seguinte: 0, 1, 1, 2, 3, 5, 8, 13, 21, etc... Para calculá-la, o primeiro e segundo elementos valem 1, daí por
   diante, o n-ésimo elemento vale o (n-1)-ésimo elemento somado ao (n-2)-ésimo elemento (ex: 8 = 5 + 3).

7) (opcional) Escreva um programa que, dada uma variável x (com valor 180, por exemplo), temos y de acordo
   com a seguinte regra:


                                  Capítulo 3 - Variáveis primitivas e Controle de fluxo - Exercícios: Fixação de sintaxe - Página 26


[PAGINA 39]
                                                           Material do Treinamento Java e Orientação a Objetos




       • se x é par, y = x / 2
       • se x é impar, y = 3 * x + 1
       • imprime y
       • O programa deve então jogar o valor de y em x e continuar até que y tenha o valor final de 1. Por
         exemplo, para x = 13, a saída será:
         40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

               Imprimindo sem pular linha
             Um detalhe importante do método que estamos usando até agora é que uma quebra de linha é
             impressa toda vez que o chamamos. Para não pular uma linha, usamos o método a seguir:

              System.out.print(variavel);




8) (opcional) Imprima a seguinte tabela, usando fors encadeados:

   1

   2 4
   3 6 9
   4 8 12 16
   n n*2 n*3 .... n*n



 3.14 - Desafios: Fibonacci

1) Faça o exercício da série de Fibonacci usando apenas duas variáveis.




                                          Capítulo 3 - Variáveis primitivas e Controle de fluxo - Desafios: Fibonacci - Página 27


[PAGINA 40]
                                                                                            C APÍTULO     4

Orientação a objetos básica
             “Programação orientada à objetos é uma péssima idéia, que só poderia ter nascido na Califórnia.”
                                                                                            – Edsger Dijkstra


   Ao término deste capítulo, você será capaz de:

   • dizer o que é e para que serve orientação a objetos;

   • conceituar classes, atributos e comportamentos;

   • entender o significado de variáveis e objetos na memória.


 4.1 - Motivação: problemas do paradigma procedural
    Orientação a objetos é uma maneira de programar que ajuda na organização e resolve muitos problemas
enfrentados pela programação procedural.

   Consideremos o clássico problema da validação de um CPF. Normalmente, temos um formulário, no qual
recebemos essa informação, e depois temos que enviar esses caracteres para uma função que irá validá-lo,
como no pseudo-código abaixo:


cpf = formulario->campo_cpf
valida(cpf)


    Alguém te obriga a sempre validar esse CPF? Você pode, inúmeras vezes, esquecer de chamar esse vali-
dador. Mais: considere que você tem 50 formulários e precise validar em todos eles o CPF. Se sua equipe tem
3 programadores trabalhando nesses formulários, quem fica responsável por essa validação? Todos!

   A situação pode piorar: na entrada de um novo desenvolvedor, precisaríamos avisá-lo que sempre deve-
mos validar o cpf de um formulário. É nesse momento que nascem aqueles guias de programação para o
desenvolvedor que for entrar nesse projeto - às vezes, é um documento enorme. Em outras palavras, todo
desenvolvedor precisa ficar sabendo de uma quantidade enorme de informações, que, na maioria das vezes,
não está realmente relacionado à sua parte no sistema, mas ele precisa ler tudo isso, resultando um entrave
muito grande!

   Outra situação onde ficam claros os problemas da programação procedural, é quando nos encontramos na
necessidade de ler o código que foi escrito por outro desenvolvedor e descobrir como ele funciona internamente.
Um sistema bem encapsulado não deveria gerar essa necessidade. Em um sistema grande, simplesmente não
temos tempo de ler todo o código existente.




                                                      28


[PAGINA 41]
                                                       Material do Treinamento Java e Orientação a Objetos




    Considerando que você não erre nesse ponto e que sua equipe tenha uma comunicação muito boa (perceba
que comunicação excessiva pode ser prejudicial e atrapalhar o andamento), ainda temos outro problema: ima-
gine que, agora, em todo formulário, você também quer que a idade do cliente seja validada - o cliente precisa
ter mais de 18 anos. Vamos ter de colocar um if... mas onde? Espalhado por todo seu código... Mesmo que
se crie outra função para validar, precisaremos incluir isso nos nossos 50 formulários já existentes. Qual é a
chance de esquecermos em um deles? É muito grande.

    A responsabilidade de verificar se o cliente tem ou não tem 18 anos ficou espalhada por todo o seu código.
Seria interessante poder concentrar essa responsabilidade em um lugar só, para não ter chances de esquecer
isso.

    Melhor ainda seria se conseguissemos mudar essa validação e os outros programadores nem precisassem
ficar sabendo disso. Em outras palavras, eles criariam formulários e um único programador seria responsável
pela validação: os outros nem sabem da existência desse trecho de código. Impossível? Não, o paradigma da
orientação a objetos facilita tudo isso.

    O problema do paradigma procedural é que não existe uma forma simples de criar conexão forte entre dados
e funcionalidades. No paradigma orientado a objetos é muito fácil ter essa conexão através dos recursos da
própria linguagem.


               Quais as vantagens?
              Orientação a objetos vai te ajudar em muito em se organizar e escrever menos, além de concentrar
              as responsabilidades nos pontos certos, flexibilizando sua aplicação, encapsulando a lógica de
              negócios.
              Outra enorme vantagem, onde você realmente vai economizar montanhas de código, é o polimor-
              fismo das referências, que veremos em um posterior capítulo.


   Nos próximo capítulos conseguiremos enxergar toda essa vantagem, mas primeiramente é necessário co-
nhecer um pouco mais da sintaxe e da criação de tipos e referências em Java.


 4.2 - Criando um tipo
   Considere um programa para um banco, é bem fácil perceber que uma entidade extremamente importante
para o nosso sistema é a conta. Nossa idéia aqui é generalizarmos alguma informação, juntamente com funci-
onalidades que toda conta deve ter.

   O que toda conta tem e é importante para nós?

   • número da conta

   • nome do dono da conta

   • saldo

   • limite

   O que toda conta faz e é importante para nós? Isto é, o que gostaríamos de “pedir à conta"?

   • saca uma quantidade x

   • deposita uma quantidade x

                                                     Capítulo 4 - Orientação a objetos básica - Criando um tipo - Página 29


[PAGINA 42]
                                                      Material do Treinamento Java e Orientação a Objetos




   • imprime o nome do dono da conta

   • devolve o saldo atual

   • transfere uma quantidade x para uma outra conta y

   • devolve o tipo de conta

   Com isso, temos o projeto de uma conta bancária. Podemos pegar esse projeto e acessar seu saldo? Não.
O que temos ainda é o projeto. Antes, precisamos construir uma conta, para poder acessar o que ela tem, e
pedir a ela que faça alguma coisa.




   Repare na figura: apesar do papel do lado esquerdo especificar uma Conta, essa especificação é uma
Conta? Nós depositamos e sacamos dinheiro desse papel? Não. Utilizamos a especificação da Conta para
poder criar instâncias que realmente são contas, onde podemos realizar as operações que criamos.

    Apesar de declararmos que toda conta tem um saldo, um número e uma agência no pedaço de papel (como
à esquerda na figura), são nas instâncias desse projeto que realmente há espaço para armazenar esses valores.

    Ao projeto da conta, isto é, a definição da conta, damos o nome de classe. Ao que podemos construir a
partir desse projeto, as contas de verdade, damos o nome de objetos.

    A palavra classe vem da taxonomia da biologia. Todos os seres vivos de uma mesma classe biológica têm
uma série de atributos e comportamentos em comum, mas não são iguais, podem variar nos valores desses
atributos e como realizam esses comportamentos.

    Homo Sapiens define um grupo de seres que possuem características em comum, porém a definição (a
idéia, o conceito) de um Homo Sapiens é um ser humano? Não. Tudo está especificado na classe Homo
Sapiens, mas se quisermos mandar algúem correr, comer, pular, precisaremos de uma instância de Homo
Sapiens, ou então de um objeto do tipo Homo Sapiens.

    Um outro exemplo: uma receita de bolo. A pergunta é certeira: você come uma receita de bolo? Não.
Precisamos instaciá-la, criar um objeto bolo a partir dessa especificação (a classe) para utilizá-la. Podemos
criar centenas de bolos a partir dessa classe (a receita, no caso), eles podem ser bem semelhantes, alguns até
idênticos, mas são objetos diferentes.

   Podemos fazer milhares de analogias semelhantes. A planta de uma casa é uma casa? Definitivamente
não. Não podemos morar dentro da planta de uma casa, nem podemos abrir sua porta ou pintar suas paredes.

                                                    Capítulo 4 - Orientação a objetos básica - Criando um tipo - Página 30


[PAGINA 43]
                                                      Material do Treinamento Java e Orientação a Objetos




Precisamos, antes, construir instâncias a partir dessa planta. Essas instâncias, sim, podemos pintar, decorar
ou morar dentro.

   Pode parecer óbvio, mas a dificuldade inicial do paradigma da orientação a objetos é justo saber distinguir
o que é classe e o que é objeto. É comum o iniciante utilizar, obviamente de forma errada, essas duas palavras
como sinônimos.


    4.3 - Uma classe em Java
     Vamos começar apenas com o que uma Conta tem, e não com o que ela faz (veremos logo em seguida).

     Um tipo desses, como o especificado de Conta acima, pode ser facilmente traduzido para Java:

class Conta {
    int numero;
    String dono;
    double saldo;
    double limite;

      // ..

}



               String
              String é uma classe em Java. Ela guarda uma palavra, isso é um punhado de caracteres. Como
              estamos aprendendo o que é uma classe, entenderemos com detalhes a classe String apenas em
              capítulos posteriores.


    Por enquanto, declaramos o que toda conta deve ter. Estes são os atributos que toda conta, quando criada,
vai ter. Repare que essas variáveis foram declaradas fora de um bloco, diferente do que fazíamos quando tinha
aquele main. Quando uma variável é declarada diretamente dentro do escopo da classe, é chamada de variável
de objeto, ou atributo.


    4.4 - Criando e usando um objeto
   Agora, temos uma classe em Java que especifica o que todo objeto dessa classe deve ter. Mas como
usá-la? Além dessa classe, ainda teremos o Programa.java e a partir dele é que iremos utilizar a classe Conta.

   Para criar (construir, instanciar) uma Conta, basta usar a palavra chave new, utilizamos também os parênte-
ses, que descobriremos o que são, exatamente, em um capítulo posterior:

class Programa {
    public static void main(String[] args) {
        new Conta();
    }
}


  Bem, o código acima cria um objeto do tipo Conta, mas como acessar esse objeto que foi criado? Precisa-
mos ter alguma forma de nos referenciarmos a esse objeto. Precisamos de uma variável:

                                                Capítulo 4 - Orientação a objetos básica - Uma classe em Java - Página 31


[PAGINA 44]
                                                     Material do Treinamento Java e Orientação a Objetos




class Programa {
    public static void main(String[] args) {
        Conta minhaConta;
        minhaConta = new Conta();
    }
}


   Pode parecer estranho escrevermos duas vezes Conta: uma vez na declaração da variável e outra vez no
uso do new. Mas há um motivo, que entenderemos também posteriormente.

   Através da variável minhaConta, agora, podemos acessar o objeto recém criado para alterar seu dono, seu
saldo etc:


 1 class Programa {
 2     public static void main(String[] args) {
 3         Conta minhaConta;
 4         minhaConta = new Conta();
 5
 6         minhaConta.dono = "Duke";
 7         minhaConta.saldo = 1000.0;
 8
 9         System.out.println("Saldo atual: " + minhaConta.saldo);
10     }
11 }


   É importante fixar que o ponto foi utilizado para acessar algo em minhaConta. Agora, minhaConta pertence
ao Duke, e tem saldo de mil reais.


 4.5 - Métodos
   Dentro da classe, também declararemos o que cada conta faz e como isto é feito - os comportamentos
que cada classe tem, isto é, o que ela faz. Por exemplo, de que maneira que uma Conta saca dinheiro?
Especificaremos isso dentro da própria classe Conta, e não em um local desatrelado das informações da própria
Conta. É por isso que essas “funções” são chamadas de métodos. Pois é a maneira de fazer uma operação
com um objeto.

   Queremos criar um método que saca uma determinada quantidade e não devolve nenhuma informação
para quem acionar esse método:

1 class Conta {
2     double salario;
3     // ... outros atributos ...
4
5     void saca(double quantidade) {
6         double novoSaldo = this.saldo - quantidade;
7         this.saldo = novoSaldo;
8     }
9 }


   A palavra chave void diz que, quando você pedir para a conta sacar uma quantia, nenhuma informação será
enviada de volta a quem pediu.

                                                         Capítulo 4 - Orientação a objetos básica - Métodos - Página 32


[PAGINA 45]
                                                     Material do Treinamento Java e Orientação a Objetos




   Quando alguém pedir para sacar, ele também vai dizer quanto quer sacar. Por isso precisamos declarar
o método com algo dentro dos parênteses - o que vai aí dentro é chamado de argumento do método (ou
parâmetro). Essa variável é uma variável comum, chamada também de temporária ou local, pois, ao final da
execução desse método, ela deixa de existir.

    Dentro do método, estamos declarando uma nova variável. Essa variável, assim como o argumento, vai
morrer no fim do método, pois este é seu escopo. No momento que vamos acessar nosso atributo, usamos a
palavra chave this para mostrar que esse é um atributo, e não uma simples variável. (veremos depois que é
opcional)

   Repare que, nesse caso, a conta pode estourar o limite fixado pelo banco. Mais para frente, evitaremos
essa situação, e de uma maneira muito elegante.

   Da mesma forma, temos o método para depositar alguma quantia:

1 class {
2     // ... outros atributos e métodos ...
3
4     void deposita(double quantidade) {
5         this.saldo += quantidade;
6     }
7 }


   Observe que, agora, não usamos uma variável auxiliar e, além disso, usamos a abreviação += para deixar
o método bem simples. O += soma quantidade ao valor antigo do saldo e guarda no próprio saldo, o valor
resultante.

    Para mandar uma mensagem ao objeto e pedir que ele execute um método, também usamos o ponto. O
termo usado para isso é invocação de método.

   O código a seguir saca dinheiro e depois deposita outra quantia na nossa conta:

 1 class TestaAlgunsMetodos {
 2     public static void main(String[] args) {
 3         // criando a conta
 4         Conta minhaConta;
 5         minhaConta = new Conta();
 6
 7         // alterando os valores de minhaConta
 8         minhaConta.dono = "Duke";
 9         minhaConta.saldo = 1000;
10
11         // saca 200 reais
12         minhaConta.saca(200);
13
14         // deposita 500 reais
15         minhaConta.deposita(500);
16         System.out.println(minhaConta.saldo);
17     }
18 }


    Uma vez que seu saldo inicial é 1000 reais, se sacarmos 200 reais, depositarmos 500 reais e imprimirmos
o valor do saldo, o que será impresso?


                                                         Capítulo 4 - Orientação a objetos básica - Métodos - Página 33


[PAGINA 46]
                                                      Material do Treinamento Java e Orientação a Objetos




 4.6 - Métodos com retorno
   Um método sempre tem que retornar alguma coisa, nem que essa coisa seja nada, como nos exemplos
anteriores onde estávamos usando o void.

   Um método pode retornar um valor para o código que o chamou. No caso do nosso método saca , podemos
devolver um valor booleano indicando se a operação foi bem sucedida.

 1 class Conta {
 2     // ... outros metodos e atributos ...
 3
 4     boolean saca(double valor) {
 5         if (this.saldo < valor) {
 6             return false;
 7         }
 8         else {
 9             this.saldo = this.saldo - valor;
10             return true;
11         }
12     }
13 }


   Agora, a declaração do método mudou! O método saca não tem void na frente. Isto quer dizer que, quando
é acessado, ele devolve algum tipo de informação. No caso, um boolean. A palavra chave return indica que o
método vai terminar ali, retornando tal informação.




   Exemplo de uso:

minhaConta.saldo = 1000;
boolean consegui = minhaConta.saca(2000);
if (consegui){
    System.out.println("Consegui sacar");
} else {
    System.out.println("Não consegui sacar");
}


   Ou então, posso eliminar a variável temporária, se desejado:

minhaConta.saldo = 1000;
if (minhaConta.saca(2000)){
    System.out.println("Consegui sacar");
} else {

                                               Capítulo 4 - Orientação a objetos básica - Métodos com retorno - Página 34


[PAGINA 47]
                                                         Material do Treinamento Java e Orientação a Objetos




      System.out.println("Não consegui sacar");
}


   Mais adiante, veremos que algumas vezes é mais interessante lançar uma exceção (exception) nesses
casos.

     Meu programa pode manter na memória não apenas uma conta, como mais de uma:

 1 class TestaDuasContas {
 2     public static void main(String[] args) {
 3
 4         Conta minhaConta;
 5         minhaConta = new Conta();
 6         minhaConta.saldo = 1000;
 7
 8         Conta meuSonho;
 9         meuSonho = new Conta();
10         meuSonho.saldo = 1500000;
11     }
12 }



    4.7 - Objetos são acessados por referências
    Quando declaramos uma variável para associar a um objeto, na verdade, essa variável não guarda o objeto,
e sim uma maneira de acessá-lo, chamada de referência.

   É por esse motivo que, diferente dos tipos primitivos como int e long, precisamos dar new depois de decla-
rada a variável:

1 public static void main(String args[]) {
2     Conta c1;
3     c1 = new Conta();
4
5     Conta c2;
6     c2 = new Conta();
7 }


    O correto aqui, é dizer que c1 se refere a um objeto. Não é correto dizer que c1 é um objeto, pois c1 é uma
variável referência, apesar de, depois de um tempo, os programadores Java falarem “Tenho um objeto c do tipo
Conta”, mas apenas para encurtar a frase “Tenho uma referência c a um objeto do tipo Conta”.

    Basta lembrar que, em Java, uma variável nunca é um objeto. Não há, no Java, uma maneira de criarmos
o que é conhecido como “objeto pilha” ou “objeto local”, pois todo objeto em Java, sem exceção, é acessado
por uma variável referência.

     Esse código nos deixa na seguinte situação:

Conta c1;
c1 = new Conta();

Conta c2;


                                 Capítulo 4 - Orientação a objetos básica - Objetos são acessados por referências - Página 35


[PAGINA 48]
                                                         Material do Treinamento Java e Orientação a Objetos




c2 = new Conta();




   Internamente, c1 e c2 vão guardar um número que identifica em que posição da memória aquela Conta se
encontra. Dessa maneira, ao utilizarmos o “.” para navegar, o Java vai acessar a Conta que se encontra naquela
posição de memória, e não uma outra.

    Para quem conhece, é parecido com um ponteiro, porém você não pode manipulá-lo e utilizá-lo para guardar
outras coisas.

   Agora vamos a um outro exemplo:

 1 class TestaReferencias {
 2     public static void main(String args[]) {
 3         Conta c1 = new Conta();
 4         c1.deposita(100);
 5
 6         Conta c2 = c1; // linha importante!
 7         c2.deposita(200);
 8
 9         System.out.println(c1.saldo);
10          System.out.println(c2.saldo);
11     }
12 }


   Qual é o resultado do código acima? O que aparece ao rodar?

    O que acontece aqui? O operador = copia o valor de uma variável. Mas qual é o valor da variável c1? É o
objeto? Não. Na verdade, o valor guardado é a referência (endereço) de onde o objeto se encontra na memória
principal.

   Na memória, o que acontece nesse caso:

Conta c1 = new Conta();
Conta c2 = c1;




                                 Capítulo 4 - Orientação a objetos básica - Objetos são acessados por referências - Página 36


[PAGINA 49]
                                                         Material do Treinamento Java e Orientação a Objetos




   Quando fizemos c2 = c1, c2 passa a fazer referência para o mesmo objeto que c1 referencia nesse instante.

    Então, nesse código em específico, quando utilizamos c1 ou c2 estamos nos referindo exatamente ao
mesmo objeto! Elas são duas referências distintas, porém apontam para o mesmo objeto! Compará-las com
“==” irá nos retornar true, pois o valor que elas carregam é o mesmo!

   Outra forma de perceber, é que demos apenas um new, então só pode haver um objeto Conta na memória.

    Atenção: não estamos discutindo aqui a utilidade de fazer uma referência apontar pro mesmo objeto que
outra. Essa utilidade ficará mais clara quando passarmos variáveis do tipo referência como argumento para
métodos.

             new
            O que exatamente faz o new?
            O new executa uma série de tarefas, que veremos mais adiante.
            Mas, para melhor entender as referências no Java, saiba que o new, depois de alocar a memória
            para esse objeto, devolve uma “flecha”, isto é, um valor de referência. Quando você atribui isso a
            uma variável, essa variável passa a se referir para esse mesmo objeto.


   Podemos então ver outra situação:

 1 public static void main(String args[]) {
 2     Conta c1 = new Conta();
 3     c1.dono = "Duke";
 4     c1.saldo = 227;
 5
 6     Conta c2 = new Conta();
 7     c2.dono = "Duke";
 8     c2.saldo = 227;
 9
10     if (c1 == c2) {
11         System.out.println("Contas iguais");
12     }
13 }


    O operador == compara o conteúdo das variáveis, mas essas variáveis não guardam o objeto, e sim o
endereço em que ele se encontra. Como em cada uma dessas variáveis guardamos duas contas criadas
diferentemente, eles estão em espaços diferentes da memória, o que faz o teste no if valer false. As contas
podem ser equivalentes no nosso critério de igualdade, porém elas não são o mesmo objeto. Quando se trata
de objetos, pode ficar mais fácil pensar que o == compara se os objetos (referências, na verdade) são o mesmo,
e não se são iguais.

                                 Capítulo 4 - Orientação a objetos básica - Objetos são acessados por referências - Página 37


[PAGINA 50]
                                                      Material do Treinamento Java e Orientação a Objetos




  Para saber se dois objetos têm o mesmo conteúdo, você precisa comparar atributo por atributo. Veremos
uma solução mais elegante para isso também.


    4.8 - O método transfere()
   E se quisermos ter um método que transfere dinheiro entre duas contas? Podemos ficar tentados a criar um
método que recebe dois parâmetros: conta1 e conta2 do tipo Conta. Mas cuidado: assim estamos pensando
de maneira procedural.

   A idéia é que, quando chamarmos o método transfere, já teremos um objeto do tipo Conta (o this), portanto
o método recebe apenas um parâmetro do tipo Conta, a Conta destino (além do valor):

class Conta {

      // atributos e metodos...

      void transfere(Conta destino, double valor) {
          this.saldo = this.saldo - valor;
          destino.saldo = destino.saldo + valor;
      }
}




    Para deixar o código mais robusto, poderíamos verificar se a conta possui a quantidade a ser transferida
disponível. Para ficar ainda mais interessante, você pode chamar os métodos deposita e saca já existentes
para fazer essa tarefa:

class Conta {

      // atributos e metodos...

                                               Capítulo 4 - Orientação a objetos básica - O método transfere() - Página 38


[PAGINA 51]
                                                          Material do Treinamento Java e Orientação a Objetos




      boolean transfere(Conta destino, double valor) {
          boolean retirou = this.saca(valor);
          if (retirou == false) {
              // não deu pra sacar!
              return false;
          }
          else {
              destino.deposita(valor);
              return true;
          }
      }
}




    Quando passamos uma Conta como argumento, o que será que acontece na memória? Será que o objeto
é clonado?

    No Java, a passagem de parâmetro funciona como uma simples atribuição como no uso do “=”. Então, esse
parâmetro vai copiar o valor da variável do tipo Conta que for passado como argumento. E qual é o valor de uma
variável dessas? Seu valor é um endereço, uma referência, nunca um objeto. Por isso não há cópia de objetos
aqui.

     Esse útltimo código poderia ser escrito com uma sintaxe muito mais sucinta. Como?

              Transfere Para
             Perceba que o nome deste método poderia ser transferePara ao invés de só transfere. A
             chamada do método fica muito mais natural, é possível ler a frase em português que ela tem um
             sentido:

              conta1.transferePara(conta2, 50);


             A leitura deste código seria “Conta1 transfere para conta2 50 reais”.


    4.9 - Continuando com atributos
   As variáveis do tipo atributo, diferentemente das variáveis temporárias (declaradas dentro de um método),
recebem um valor padrão. No caso numérico, valem 0, no caso de boolean, valem false.

     Você também pode dar valores default, como segue:

1 class Conta {
2     int numero = 1234;

                                             Capítulo 4 - Orientação a objetos básica - Continuando com atributos - Página 39


[PAGINA 52]
                                                          Material do Treinamento Java e Orientação a Objetos




3        String dono = "Duke";
4        String cpf = "123.456.789-10";
5        double saldo = 1000;
6        double limite = 1000;
7 }


      Nesse caso, quando você criar uma conta, seus atributos já estão “populados” com esses valores colocados.

    Imagine que, agora, começamos a aumentar nossa classe Conta e adicionar nome, sobrenome e cpf do
cliente dono da conta. Começaríamos a ter muitos atributos... e, se você pensar direito, uma Conta não tem
nome, nem sobrenome nem cpf, quem tem esses atributos é um Cliente. Então podemos criar uma nova classe
e fazer uma composição

      Seus atributos também podem ser referências para outras classes. Suponha a seguinte classe Cliente:

1 class Cliente {
2     String nome;
3     String sobrenome;
4     String cpf;
5 }



1 class Conta {
2     int numero;
3     double saldo;
4     double limite;
5     Cliente titular;
6     // ..
7 }


      E dentro do main da classe de teste:

1 class Teste {
2     public static void main(String[] args) {
3         Conta minhaConta = new Conta();
4         Cliente c = new Cliente();
5         minhaConta.titular = c;
6         // ...
7     }
8 }


    Aqui, simplesmente houve uma atribuição. O valor da variável c é copiado para o atributo titular do objeto ao
qual minhaConta se refere. Em outras palavras, minhaConta agora tem uma referência ao mesmo Cliente que c
se refere, e pode ser acessado através de minhaConta.titular.

      Você pode realmente navegar sobre toda essa estrutura de informação, sempre usando o ponto:

Cliente clienteDaMinhaConta = minhaConta.titular;
clienteDaMinhaConta.nome = "Duke";


      Ou ainda, pode fazer isso de uma forma mais direta e até mais elegante:

                                             Capítulo 4 - Orientação a objetos básica - Continuando com atributos - Página 40


[PAGINA 53]
                                                        Material do Treinamento Java e Orientação a Objetos




minhaConta.titular.nome = "Duke";


    Um sistema orientado a objetos é um grande conjunto de classes que vai se comunicar, delegando respon-
sabilidades para quem for mais apto a realizar determinada tarefa. A classe Banco usa a classe Conta que usa a
classe Cliente, que usa a classe Endereco. Dizemos que esses objetos colaboram, trocando mensagens entre
si. Por isso acabamos tendo muitas classes em nosso sistema, e elas costumam ter um tamanho relativamente
curto.

    Mas, e se dentro do meu código eu não desse new em Cliente e tentasse acessá-lo diretamente?

class Teste {
    public static void main(String[] args) {
        Conta minhaConta = new Conta();

         minhaConta.titular.nome = "paulo";
         // ...
    }
}


    Quando damos new em um objeto, ele o inicializa com seus valores default, 0 para números, false para
boolean e null para referências. null é uma palavra chave em java, que indica uma referência para nenhum
objeto.




   Se, em algum caso, você tentar acessar um atributo ou método de alguém que está se referenciando para
null, você receberá um erro durante a execução (NullPointerException, que veremos mais à frente). Da
para perceber, então, que o new não traz um efeito cascata, a menos que você dê um valor default (ou use
construtores, que também veremos mais a frente):

1 class Conta {
2     int numero;
3     double saldo;
4     double limite;
5     Cliente titular = new Cliente();         // quando chamarem new Conta,
6                                              //havera um new Cliente para ele.
7 }




                                           Capítulo 4 - Orientação a objetos básica - Continuando com atributos - Página 41


[PAGINA 54]
                                                         Material do Treinamento Java e Orientação a Objetos




    Com esse código, toda nova Conta criada criado já terá um novo Cliente associado, sem necessidade de
instanciá-lo logo em seguida da instanciação de uma Conta. Qual alternativa você deve usar? Depende do
caso: para toda nova Conta você precisa de um novo Cliente? É essa pergunta que deve ser respondida.
Nesse nosso caso a resposta é não, mas depende do nosso problema.

    Atenção: para quem não está acostumado com referências, pode ser bastante confuso pensar sempre em
como os objetos estão na memória para poder tirar as conclusões de o que ocorrerá ao executar determinado
código, por mais simples que ele seja. Com tempo, você adquire a habilidade de rapidamente saber o efeito de
atrelar as referências, sem ter de gastar muito tempo para isso. É importante, nesse começo, você estar sempre
pensando no estado da memória. E realmente lembrar que, no Java “uma variável nunca carrega um objeto, e
sim uma referência para ele” facilita muito.


 4.10 - Para saber mais: Uma Fábrica de Carros
    Além do Banco que estamos criando, vamos ver como ficariam certas classes relacionadas a uma fábrica de
carros. Vamos criar uma classe Carro, com certos atributos, que descrevem suas características, e com certos
métodos, que descrevem seu comportamento.

 1 class Carro {
 2     String cor;
 3     String modelo;
 4     double velocidadeAtual;
 5     double velocidadeMaxima;
 6
 7     //liga o carro
 8     void liga() {
 9         System.out.println("O carro está ligado");
10     }
11
12     //acelera uma certa quantidade
13     void acelera(double quantidade) {
14         double velocidadeNova = this.velocidadeAtual + quantidade;
15         this.velocidadeAtual = velocidadeNova;
16     }
17
18     //devolve a marcha do carro
19     int pegaMarcha() {
20         if (this.velocidadeAtual < 0) {
21             return -1;
22         }
23         if (this.velocidadeAtual >= 0 && this.velocidadeAtual < 40) {
24             return 1;
25         }
26         if (this.velocidadeAtual >= 40 && this.velocidadeAtual < 80 {
27             return 2;
28         }
29         return 3;
30     }
31 }


   Agora, vamos testar nosso Carro em um programa de testes:



                               Capítulo 4 - Orientação a objetos básica - Para saber mais: Uma Fábrica de Carros - Página 42


[PAGINA 55]
                                                      Material do Treinamento Java e Orientação a Objetos




 1 class TestaCarro {
 2     public static void main(String[] args) {
 3         Carro meuCarro;
 4         meuCarro = new Carro();
 5         meuCarro.cor = "Verde";
 6         meuCarro.modelo = "Fusca";
 7         meuCarro.velocidadeAtual = 0;
 8         meuCarro.velocidadeMaxima = 80;
 9
10         // liga o carro
11         meuCarro.liga();
12
13         // acelera o carro
14         meuCarro.acelera(20);
15         System.out.println(meuCarro.velocidadeAtual);
16     }
17 }


   Nosso carro pode conter também um Motor:

1 class Motor {
2     int potencia;
3     String tipo;
4 }



1 class Carro {
2     String cor;
3     String modelo;
4     double velocidadeAtual;
5     double velocidadeMaxima;
6     Motor motor;
7
8     // ..
9 }


   Podemos, agora, criar diversos Carros e mexer com seus atributos e métodos, assim como fizemos no
exemplo do Banco.


 4.11 - Um pouco mais...

1) Quando declaramos uma classe, um método ou um atributo, podemos dar o nome que quisermos, seguindo
   uma regra. Por exemplo, o nome de um método não pode começar com um número. Pesquise sobre essas
   regras.

2) Como você pode ter reparado, sempre damos nomes às variáveis com letras minúsculas. É que existem
   convenções de código, dadas pela Sun, para facilitar a legibilidade do código entre programadores. Essa
   convenção é muito seguida. Pesquise sobre ela no http://java.sun.com, procure por “code conventions”.

3) É necessário usar a palavra chave this quando for acessar um atributo? Para que, então, utilizá-la?



                                                  Capítulo 4 - Orientação a objetos básica - Um pouco mais... - Página 43


[PAGINA 56]
                                                         Material do Treinamento Java e Orientação a Objetos




4) O exercício a seguir pedirá para modelar um “funcionário”. Existe um padrão para representar suas classes
   em diagramas, que é amplamente utilizado, chamado UML. Pesquise sobre ele.


 4.12 - Exercícios: Orientação a Objetos
   O modelo de funcionários a seguir será utilizado para os exercícios de alguns dos posteriores capítulos.

   O objetivo aqui é criar um sistema para                           gerenciar      os     funcionários       do     Banco.
Os exercícios desse capítulo são extremamente importantes.

1) Modele um funcionário. Ele deve ter o nome do funcionário, o departamento onde trabalha, seu salário
   (double), a data de entrada no banco (String), seu RG (String) e um valor booleano que indique se o
   funcionário está na empresa no momento ou se já foi embora.
   Você deve criar alguns métodos de acordo com sua necessidade. Além deles, crie um método bonifica que
   aumenta o salario do funcionário de acordo com o parâmetro passado como argumento. Crie, também, um
   método demite, que não recebe parâmetro algum, só modifica o valor booleano indicando que o funcionário
   não trabalha mais aqui.
   A idéia aqui é apenas modelar, isto é, só identifique que informações são importantes e o que um funcionário
   faz. Desenhe no papel tudo o que um Funcionario tem e tudo que ele faz.

2) Transforme o modelo acima em uma classe Java. Teste-a, usando uma outra classe que tenha o main. Você
   deve criar a classe do funcionário chamada Funcionario, e a classe de teste você pode nomear como quiser.
   A de teste deve possuir o método main.
   Um esboço da classe:

   class Funcionario {


       double salario;
       // seus outros atributos e métodos

       void bonifica(double aumento) {
           // o que fazer aqui dentro?
       }

       void demite() {
           // o que fazer aqui dentro?
       }
   }


   Você pode (e deve) compilar seu arquivo java sem que você ainda tenha terminado sua classe Funcionario.
   Isso evitará que você receba dezenas de erros de compilação de uma vez só. Crie a classe Funcionario,
   coloque seus atributos e, antes de colocar qualquer método, compile o arquivo java. Funcionario.class
   será gerado, não podemos “executá-la” pois não há um main, mas assim verificamos que nossa classe
   Funcionario já está tomando forma.




                                      Capítulo 4 - Orientação a objetos básica - Exercícios: Orientação a Objetos - Página 44


[PAGINA 57]
                                                          Material do Treinamento Java e Orientação a Objetos




  Esse é um processo incremental. Procure desenvolver assim seus exercícios, para não descobrir só no fim
  do caminho que algo estava muito errado.
  Um esboço da classe que possui o main:

    1 class TestaFuncionario {

   2
   3      public static void main(String[] args) {
   4          Funcionario f1 = new Funcionario();
   5
   6             f1.nome = "Fiodor";
   7             f1.salario = 100;
   8             f1.bonifica(50);
   9
  10             System.out.println("salario atual:" + f1.salario);
  11
  12      }
  13 }


  Incremente essa classe. Faça outros testes, imprima outros atributos e invoque os métodos que você criou
  a mais.
  Lembre-se de seguir a convenção java, isso é importantíssimo. Isto é, nomeDeAtributo, nomeDeMetodo,
  nomeDeVariavel, NomeDeClasse, etc...



               Todas as classes no mesmo arquivo?
              Por enquanto, você pode colocar todas as classes no mesmo arquivo e apenas compilar esse
              arquivo. Ele vai gerar os dois .class.
              Porém, é boa prática criar um arquivo .java para cada classe e, em determinados casos, você será
              obrigado a declarar uma classe em um arquivo separado, como veremos no capítulo 10. Isto não é
              importante para o aprendizado no momento.

3) Crie um método mostra(), que não recebe nem devolve parâmetro algum e simplesmente imprime todos
   os atributos do nosso funcionário. Dessa maneira, você não precisa ficar copiando e colando um monte
   de System.out.println() para cada mudança e teste que fizer com cada um de seus funcionários, você
   simplesmente vai fazer:

   Funcionario f1 = new Funcionario();

  //brincadeiras com f1....


                                       Capítulo 4 - Orientação a objetos básica - Exercícios: Orientação a Objetos - Página 45


[PAGINA 58]
                                                        Material do Treinamento Java e Orientação a Objetos




   f1.mostra();

   Veremos mais a frente o método toString, que é uma solução muito mais elegante para mostrar a repre-
   sentação de um objeto como String, além de não jogar tudo pro System.out (só se você desejar).
   O esqueleto do método ficaria assim:

   class Funcionario {


       // seus outros atributos e métodos

       void mostra() {
           System.out.println("Nome: " + this.nome);
           // imprimir aqui os outros atributos...
       }
   }


4) Construa dois funcionários com o new e compare-os com o ==. E se eles tiverem os mesmos atributos? Para
   isso você vai precisar criar outra referência:

   Funcionario f1 = new Funcionario();

   f1.nome = "Fiodor";
   f1.salario = 100;

   Funcionario f2 = new Funcionario();
   f2.nome = "Fiodor";
   f2.salario = 100;

   if (f1 == f2) {
       System.out.println("iguais");
   } else {
       System.out.println("diferentes");
   }


5) Crie duas referências para o mesmo funcionário, compare-os com o ==. Tire suas conclusões. Para criar
   duas referências pro mesmo funcionário:

   Funcionario f1 = new Funcionario():

   f1.nome = "Fiodor";
   f1.salario = 100;

   Funcionario f2 = f1;

   O que acontece com o if do exercício anterior?
6) (opcional) Em vez de utilizar uma String para representar a data, crie uma outra classe, chamada Data. Ela
   possui 3 campos int, para dia, mês e ano. Faça com que seu funcionário passe a usá-la. (é parecido com
   o último exemplo, em que a Conta passou a ter referência para um Cliente).

   class Funcionario {


       Data dataDeEntrada; // qual é o valor default aqui?

                                     Capítulo 4 - Orientação a objetos básica - Exercícios: Orientação a Objetos - Página 46


[PAGINA 59]
                                                         Material do Treinamento Java e Orientação a Objetos




       // seus outros atributos e métodos

   }

   class Data {

       int dia;
       int mes;
       int ano;
   }

   Modifique sua classe TestaFuncionario para que você crie uma Data e atribua ela ao Funcionario:

   Funcionario f1 = new Funcionario();

   //...
   Data data = new Data(); // ligação!
   f1.dataDeEntrada = data;


   Faça o desenho do estado da memória quando criarmos um Funcionario.

7) (opcional) Modifique seu método mostra para que ele imprima o valor da dataDeEntrada daquele
   Funcionario:

   class Funcionario {


       // seus outros atributos e métodos
       Data dataDeEntrada;

       void mostra() {
           System.out.println("Nome: " + this.nome);
           // imprimir aqui os outros atributos...

              System.out.println("Dia: " + this.dataDeEntrada.dia);
              System.out.println("Mês: " + this.dataDeEntrada.mes);
              System.out.println("Ano: " + this.dataDeEntrada.ano);
       }
   }


   Teste-o.
   Agora, o que acontece se chamarmos o método mostra antes de atribuirmos uma data para este
   Funcionario?

8) (opcional) O que acontece se você tentar acessar um atributo diretamente na classe? Como, por exemplo:

   Funcionario.salario = 1234;


   Esse código faz sentido? E este:

   Funcionario.demite();



   Faz sentido pedir para o esquema do Funcionario demitir?

                                      Capítulo 4 - Orientação a objetos básica - Exercícios: Orientação a Objetos - Página 47


[PAGINA 60]
                                                      Material do Treinamento Java e Orientação a Objetos




 4.13 - Desafios

1) Um método pode chamar ele mesmo. Chamamos isso de recursão. Você pode resolver a série de fibonacci
   usando um método que chama ele mesmo. O objetivo é você criar uma classe, que possa ser usada da
   seguinte maneira:

   Fibonacci fibo = new Fibonacci();

   int i = fibo.calculaFibonacci(6);
   System.out.println(i);


   Aqui imprimirá 8, já que este é o sexto número da série.
   Este método calculaFibonacci não pode ter nenhum laço, só pode chamar ele mesmo como método. Pense
   nele como uma função, que usa a própria função para calcular o resultado.

2) Por que o modo acima é extremamente mais lento para calcular a série do que o modo iterativo (que se usa
   um laço)?

3) Escreva o método recursivo novamente, usando apenas uma linha. Para isso, pesquise sobre o operador
   condicional ternário. (ternary operator)


 4.14 - Fixando o conhecimento
    O objetivo dos exercícios a seguir é fixar o conceito de classes e objetos, métodos e atributos. Dada a
estrutura de uma classe, basta traduzí-la para a linguagem Java e fazer uso de um objeto da mesma em um
programa simples.

   Se você está com dificuldade em alguma parte desse capítulo, aproveite e treine tudo o que vimos até agora
nos pequenos programas abaixo:

1) Programa 1
   Classe: Pessoa Atributos: nome, idade. Método: void fazAniversario()
   Crie uma pessoa, coloque seu nome e idade iniciais, faça alguns aniversários (aumentando a idade) e
   imprima seu nome e sua idade.

2) Programa 2
   Classe: Porta Atributos: aberta, cor, dimensaoX, dimensaoY, dimensaoZ Métodos: void abre(), void fecha(),
   void pinta(String s), boolean estaAberta()
   Crie uma porta, abra e feche a mesma, pinte-a de diversas cores, altere suas dimensões e use o método
   estaAberta para verificar se ela está aberta.

3) Programa 3
   Classe: Casa Atributos: cor, porta1, porta2, porta3 Método: void pinta(String s), int quantasPortasEstaoA-
   bertas()
   Crie uma casa e pinte-a. Crie três portas e coloque-as na casa; abra e feche as mesmas como desejar.
   Utilize o método quantasPortasEstaoAbertas para imprimir o número de portas abertas.




                                                          Capítulo 4 - Orientação a objetos básica - Desafios - Página 48


[PAGINA 61]
                                                                                            C APÍTULO     5

Um pouco de arrays
                                      “O homem esquecerá antes a morte do pai que a perda da propriedade”
                                                                                               – Maquiavel


   Ao término desse capítulo, você será capaz de:

   • declarar e instanciar arrays;

   • popular e percorrer arrays.


 5.1 - O problema
   Dentro de um bloco, podemos declarar variáveis e usá-las.

int idade1;
int idade2;
int idade3;
int idade4;


   Mas também podemos declarar um vetor (array) de inteiros:

int[] idades;


   O int[] é um tipo. Uma array é sempre um objeto, portanto, a variável idades é uma referência. Vamos
precisar criar um objeto para poder usar a array. Como criamos o objeto-array?

idades = new int[10];


   Aqui, o que fizemos foi criar uma array de int de 10 posições, e atribuir o endereço no qual ela foi criada.
Agora, podemos acessar as posições do array.

idades[5] = 10;




                                                      49


[PAGINA 62]
                                                     Material do Treinamento Java e Orientação a Objetos




   O código acima altera a sexta posição do array. No Java, os índices do array vão de 0 a n-1, onde n é o
tamanho dado no momento em que você criou o array. Se você tentar acessar uma posição fora desse alcance,
um erro ocorrerá durante a execução.




             Arrays – um problema no aprendizado de muitas linguagens
            Aprender a usar arrays pode ser um problema em qualquer linguagem. Isso porque envolve uma
            série de conceitos, sintaxe e outros. No Java, muitas vezes utilizamos outros recursos em vez de
            arrays, em especial os pacotes de coleções do Java, que veremos no capítulo 11. Portanto, fique
            tranqüilo caso não consiga digerir toda sintaxe das arrays num primeiro momento.


 5.2 - Arrays de referências

   É comum ouvirmos “array de objetos”. Porém quando criamos uma array de alguma classe, ela possui refe-
rências. O objeto, como sempre, está na memória principal e, na sua array, só ficam guardadas as referências
(endereços).

Conta[] minhasContas;
minhasContas = new Conta[10];


     Quantas contas foram criadas aqui? Na verdade, nenhuma. Foram criados 10 espaços que você pode
utilizar para guardar uma referência a uma Conta. Por enquanto, eles se referenciam para lugar nenhum (null).
Se você tentar:

System.out.println(minhasContas[0].saldo);


   Um erro durante a execução ocorrerá! Pois, na primeira posição da array, não há uma referência para uma
conta, nem para lugar nenhum. Você deve popular sua array antes.

Conta contaNova = new Conta();
contaNova.saldo = 1000.0;
minhasContas[0] = contaNova;


   Ou você pode fazer isso diretamente:

minhasContas[1] = new Conta();
minhasContas[1].saldo = 3200.0;




                                                     Capítulo 5 - Um pouco de arrays - Arrays de referências - Página 50


[PAGINA 63]
                                                     Material do Treinamento Java e Orientação a Objetos




   Uma array de tipos primitivos guarda valores, uma array de objetos guarda referências.


 5.3 - Percorrendo uma array
   Percorrer uma array é muito simples quando fomos nós que a criamos:

public static void main(String args[]) {
    int[] idades = new int[10];
    for (int i = 0; i < 10; i++) {
        idades[i] = i * 10;
    }
    for (int i = 0; i < 10; i++) {
        System.out.println(idades[i]);
    }
}


   Porém, em muitos casos, recebemos uma array como argumento em um método:

void imprimeArray(int[] array) {
    // não compila!!
    for (int i = 0; i < ????; i++) {
        System.out.println(array[i]);
    }
}


   Até onde o for deve ir? Toda array em Java tem um atributo que se chama length, e você pode acessá-lo
para saber o tamanho do array ao qual você está se referenciando naquele momento:

void imprimeArray(int[] array) {
    for (int i = 0; i < array.length; i++) {
        System.out.println(array[i]);
    }

                                                    Capítulo 5 - Um pouco de arrays - Percorrendo uma array - Página 51


[PAGINA 64]
                                                        Material do Treinamento Java e Orientação a Objetos




}



              Arrays não podem mudar de tamanho
             A partir do momento que uma array foi criada, ela não pode mudar de tamanho.
             Se você precisar de mais espaço, será necessário criar uma nova array e, antes de se referir ela,
             copie os elementos da array velha.


    5.4 - Percorrendo uma array no Java 5.0
     O Java 5.0 traz uma nova sintaxe para percorremos arrays (e coleções, que veremos mais a frente).

    No caso de você não ter necessidade de manter uma variável com o índice que indica a posição do elemento
no vetor (que é uma grande parte dos casos), podemos usar o enhanced-for.

class AlgumaClasse{
    public static void main(String args[]) {
        int[] idades = new int[10];
        for (int i = 0; i < 10; i++) {
            idades[i] = i * 10;
        }

          // imprimindo toda a array
          for (int x : idades) {
              System.out.println(x);
          }
      }
}


     E agora nem precisamos mais do length para percorrer matrizes cujo tamanho não conhecemos:

class AlgumaClasse {
    void imprimeArray(int[] array) {
        for (int x : array) {
            System.out.println(x);
        }
    }
}


    O mesmo é válido para arrays de referências. Esse for nada mais é que um truque de compilação para
facilitar essa tarefa de percorrer arrays e torná-la mais legível.


    5.5 - Exercícios: Arrays

1) Volte ao nosso sistema de Funcionario e crie uma classe Empresa dentro do mesmo arquivo .java. A
   Empresa tem um nome, cnpj e uma referência a uma array de Funcionario, além de outros atributos que
   você julgar necessário.

     class Empresa {

                                           Capítulo 5 - Um pouco de arrays - Percorrendo uma array no Java 5.0 - Página 52


[PAGINA 65]
                                                     Material do Treinamento Java e Orientação a Objetos




         // outros atributos
         Funcionario[] empregados;
         String cnpj;
  }


2) A Empresa deve ter um método adiciona, que recebe uma referência a Funcionario como argumento, e
   guarda esse funcionário. Algo como:

   ...

         void adiciona(Funcionario f) {
             // algo tipo:
             //   this.empregados[ ??? ] = f;
             // mas que posição colocar?
         }
  ...


  Você deve inserir o Funcionario em uma posição da array que esteja livre. Existem várias maneiras para
  você fazer isso: guardar um contador para indicar qual a próxima posição vazia ou procurar por uma posição
  vazia toda vez. O que seria mais interessante?
  É importante reparar que o método adiciona não recebe nome, rg, salário, etc. Essa seria uma maneira nem
  um pouco estruturada, muito menos orientada a objetos de se trabalhar. Você antes cria um Funcionario e
  já passa a referência dele, que dentro do objeto possui rg, salário, etc.

3) Crie uma classe TestaEmpresa que possuirá um método main. Dentro dele crie algumas instâncias de
   Funcionario e passe para a empresa pelo método adiciona. Repare que antes você vai precisar criar a
   array, pois inicialmente o atributo empregados da classe Empresa não referencia lugar nenhum (null):

   Empresa empresa = new Empresa();

  empresa.empregados = new Funcionario[10];
  //     ....


  Ou você pode construir a array dentro da própria declaração da classe Empresa, fazendo com que toda vez
  que uma Empresa é instanciada, a array de Funcionario que ela necessita também é criada.
  Crie alguns funcionários e passe como argumento para o adiciona da empresa:

   Funcionario f1 = new Funcionario();

  f1.salario = 1000;
  empresa.adiciona(f1);

  Funcionario f2 = new Funcionario();
  f2.salario = 1700;
  empresa.adiciona(f2);

  Você pode criar esses funcionários dentro de um loop, e dar valores diferentes de salários:

   for (int i = 0; i < 5; i++) {

         Funcionario f = new Funcionario();
         f.salario = 1000 + i * 100;
         empresa.adiciona(f);



                                                        Capítulo 5 - Um pouco de arrays - Exercícios: Arrays - Página 53


[PAGINA 66]
                                                       Material do Treinamento Java e Orientação a Objetos




   }


   Repare que temos de instanciar Funcionario dentro do laço. Se a instanciação de Funcionario ficasse acima
   do laço, estaríamos adicionado cinco vezes a mesma instância de Funcionario nesta Empresa, e mudando
   seu salário a cada iteração, que nesse caso não é o efeito desejado.
   Opcional: o método adiciona pode gerar uma mensagem de erro indicando quando o array já está cheio.

4) Percorra o atributo empregados da sua instância da Empresa e imprima o salários de todos seus funcionários.
   Para fazer isso, você pode criar um método chamado mostraEmpregados dentro da classe Empresa:

   ...

         void mostraEmpregados() {
             for (int i = 0; i < this.empregados.length; i++) {
                 System.out.println("Funcionário na posição: " + i);

                   // preencher para mostrar o salário!!
             }
         }
   ...


   Cuidado ao preencher esse método: alguns índices do seu array podem não conter referência para um
   Funcionario construído, isto é, ainda se referirem para null. Se preferir, use o for novo do java 5.0.
   Aí, através do seu main, depois de adicionar alguns funcionários, basta fazer:

   empresa.mostraEmpregados();



   (opcional) Em vez de mostrar apenas o salário de cada funcionário, você pode chamar o método mostra()
   de cada Funcionario da sua array.

5) (Opcional) Crie um método para verificar se um determinado Funcionario se encontra ou não como
   funcionário desta empresa:

   boolean contem(Funcionario f) {

         // ...
   }


   Você vai precisar fazer um for na sua array e verificar se a referência passada como argumento se encontra
   dentro da array. Evite ao máximo usar números hard-coded, isto é, use o .length.

6) (Opcional) Caso a array já esteja cheia no momento de adicionar um outro funcionário, criar uma nova maior
   e copiar os valores. Isto é, fazer a realocação já que java não tem isso: uma array nasce e morre com o
   mesmo length.



                 Usando o this para passar argumento
             Dentro de um método, você pode usar a palavra this para referenciar a si mesmo e pode passar
             essa referência como argumento.




                                                         Capítulo 5 - Um pouco de arrays - Exercícios: Arrays - Página 54


[PAGINA 67]
                                                  Material do Treinamento Java e Orientação a Objetos




5.6 - Um pouco mais...

 • Arrays podem ter mais de uma dimensão. Isto é, em vez de termos uma array de 10 contas, podemos ter
   uma array de 10 por 10 contas e você pode acessar a conta na posição da coluna x e linha y. Na verdade,
   uma array bidimensional em Java é uma array de arrays. Pesquise sobre isso.




 • Uma array bidimensional não precisa ser retangular, isto é, cada linha pode ter um número diferente de
   colunas. Como? Porque?




 • O que acontece se criarmos uma array de 0 elementos? e -1?

 • O método main recebe uma array de Strings como argumento. Essa array é passada pelo usuário
   quando ele invoca o programa:

    $ java Teste argumento1 outro maisoutro


                                                     Capítulo 5 - Um pouco de arrays - Um pouco mais... - Página 55


[PAGINA 68]
                                                       Material do Treinamento Java e Orientação a Objetos




     E nossa classe:

      class Teste {

           public static void main (String[] args) {
               for(String argumento: args) {
                   System.out.println(argumento);
               }
           }
     }


     Isso imprimirá:

      argumento1

     outro
     maisoutro



 5.7 - Desafios

1) No capítulo anterior, você deve ter reparado que a versão recursiva para o problema de Fibonacci é lenta
   porque toda hora estamos recalculando valores. Faça com que a versão recursiva seja tão boa quanto a
   versão iterativa. (Dica: use arrays para isso)


 5.8 - Testando o conhecimento

1) O objetivo dos exercícios a seguir é fixar os conceitos vistos até agora. Se você está com dificuldade em
   alguma parte desse capítulo, aproveite e treine tudo o que vimos até agora no pequeno programa abaixo:

     • Programa:
         Classe: Casa Atributos: cor, totalDePortas, portas[] Métodos: void pinta(String s), int quantasPortasEs-
         taoAbertas(), void adicionaPorta(Porta p), int totalDePortas()

   Crie uma casa, pinte-a. Crie três portas e coloque-as na casa através do método adicionaPorta, abra
   e feche-as como desejar. Utilize o método quantasPortasEstaoAbertas para imprimir o número de portas
   abertas e o método totalDePortas para imprimir o total de portas em sua casa.




                                                                  Capítulo 5 - Um pouco de arrays - Desafios - Página 56


[PAGINA 69]
                                                                                               C APÍTULO    6

Modificadores de acesso e atributos de
classe
    “A marca do homem imaturo é que ele quer morrer nobremente por uma causa, enquanto a marca do homem
                                                            maduro é querer viver modestamente por uma.”
                                                                                            – J. D. Salinger


      Ao término desse capítulo, você será capaz de:

      • controlar o acesso aos seus métodos, atributos e construtores através dos modificadores private e public;

      • escrever métodos de acesso a atributos do tipo getters e setters;

      • escrever construtores para suas classes;

      • utilizar variáveis e métodos estáticos.

    6.1 - Controlando o acesso
  Um dos problemas mais simples que temos no nosso sistema de contas é que a função saca permite sacar
mesmo que o limite tenha sido atingido. A seguir você pode lembrar como está a classe Conta:

class Conta {
    int numero;
    Cliente titular;
    double saldo;
    double limite;

       // ..

       void saca(double quantidade) {
           this.saldo = this.saldo - quantidade;
       }
}


      A classe a seguir mostra como é possível ultrapassar o limite usando o método saca:

class TestaContaEstouro1 {
    public static void main(String args[]) {
        Conta minhaConta = new Conta();
        minhaConta.saldo = 1000.0;
        minhaConta.limite = 1000.0;

                                                        57


[PAGINA 70]
                                                           Material do Treinamento Java e Orientação a Objetos




         minhaConta.saca(50000); // saldo + limite é só 2000!!
    }
}


   Podemos incluir um if dentro do nosso método saca() para evitar a situação que resultaria em uma conta
em estado inconsistente, com seu saldo abaixo do limite. Fizemos isso no capítulo de orientação a objetos
básica.

    Apesar de melhorar bastante, ainda temos um problema mais grave: ninguém garante que o usuário da
classe vai sempre utilizar o método para alterar o saldo da conta. O código a seguir ultrapassa o limite direta-
mente:

class TestaContaEstouro2 {
    public static void main(String args[]) {
        Conta minhaConta = new Conta();
        minhaConta.limite = 100;
        minhaConta.saldo = -200; //saldo está abaixo dos 100 de limite
    }
}


    Como evitar isso? Uma idéia simples seria testar se não estamos ultrapassando o limite toda vez que formos
alterar o saldo:

class TestaContaEstouro3 {

    public static void main(String args[]) {
        // a Conta
        Conta minhaConta = new Conta();
        minhaConta.limite = 100;
        minhaConta.saldo = 100;

         // quero mudar o saldo para -200
         double novoSaldo = -200;

         // testa se o novoSaldo ultrapassa o limite da conta
         if (novoSaldo < -minhaConta.limite) { //
             System.out.println("Não posso mudar para esse saldo");
         } else {
             minhaConta.saldo = novoSaldo;
         }
    }
}


    Esse código iria se repetir ao longo de toda nossa aplicação e, pior, alguém pode esquecer de fazer essa
comparação em algum momento, deixando a conta na situação inconsistente. A melhor forma de resolver isso
seria forçar quem usa a classe Conta a invocar o método saca e não permitir o acesso direto ao atributo. É o
mesmo caso da validação de CPF.

   Para fazer isso no Java, basta declarar que os atributos não podem ser acessados de fora da classe através
da palavra chave private:

class Conta {

                                 Capítulo 6 - Modificadores de acesso e atributos de classe - Controlando o acesso - Página 58


[PAGINA 71]
                                                           Material do Treinamento Java e Orientação a Objetos




    private double saldo;
    private double limite;
    // ...
}


    private é um modificador de acesso (também chamado de modificador de visibilidade).

    Marcando um atributo como privado, fechamos o acesso ao mesmo em relação a todas as outras classes,
fazendo com que o seguinte código não compile:

class TestaAcessoDireto {
   public static void main(String args[]) {
    Conta minhaConta = new Conta();
    //não compila! você não pode acessar o atributo privado de outra classe
    minhaConta.saldo = 1000;
   }
}




    Na orientação a objetos, é prática quase que obrigatória proteger seus atributos com private. (discutiremos
outros modificadores de acesso em outros capítulos).

    Cada classe é responsável por controlar seus atributos, portanto ela deve julgar se aquele novo valor é válido
ou não! Esta validação não deve ser controlada por quem está usando a classe e sim por ela mesma, centra-
lizando essa responsabilidade e facilitando futuras mudanças no sistema. Muitas outras vezes nem mesmo
queremos que outras classes saibam da existência de determinado atributo, escondendo-o por completo, já que
ele diz respeito ao funcionamento interno do objeto.

    Repare que, agora, quem invoca o método saca não faz a menor idéia de que existe um limite que está
sendo checado. Para quem for usar essa classe, basta saber o que o método faz e não como exatamente ele
o faz (o que um método faz é sempre mais importante do que como ele faz: mudar a implementação é fácil, já
mudar a assinatura de um método vai gerar problemas).

   A palavra chave private também pode ser usada para modificar o acesso a um método. Tal funcionalidade
é normalmente usada quando existe um método apenas auxiliar a própria classe e não queremos que outras
pessoas o usem (ou apenas para seguir a boa prática de expôr-se ao mínimo). Sempre devemos expôr o
mínimo possível de funcionalidades, para criar um baixo acoplamento entre as nossas classes.

   Da mesma maneira que temos o private, temos o modificador public, que permite a todos acessarem um
determinado atributo ou método :

class Conta {
  //...
  public void saca(double quantidade) {
    if (quantidade > this.saldo + this.limite){ //posso sacar até saldo+limite
       System.out.println("Não posso sacar fora do limite!");
     } else {
       this.saldo = this.saldo - quantidade;
    }


                                 Capítulo 6 - Modificadores de acesso e atributos de classe - Controlando o acesso - Página 59


[PAGINA 72]
                                                       Material do Treinamento Java e Orientação a Objetos




    }
}



             E quando não há modificador de acesso?
           Até agora, tínhamos declarado variáveis e métodos sem nenhum modificador como private e
           public. Quando isto acontece, o seu método ou atributo fica num estado de visibilidade inter-
           mediário entre o private e o public, que veremos mais pra frente, no capítulo de pacotes.


    É muito comum, e faz todo sentido, que seus atributos sejam private e quase todos seus métodos sejam
public (não é uma regra!). Desta forma, toda conversa de um objeto com outro é feita por troca de mensagens,
isto é, acessando seus métodos. Algo muito mais educado que mexer diretamente em um atributo que não é
seu!

    Melhor ainda! O dia em que precisarmos mudar como é realizado um saque na nossa classe Conta, adivinhe
onde precisaríamos modificar? Apenas no método saca, o que faz pleno sentido. Como exemplo, imagine
cobrar CPMF de cada saque: basta você modificar ali, e nenhum outro código, fora a classe Conta, precisará
ser recompilado. Mais: as classes que usam esse método nem precisam ficar sabendo de tal modificação! Você
precisa apenas recompilar aquela classe e substituir aquele arquivo .class. Ganhamos muito em esconder o
funcionamento do nosso método na hora de dar manutenção e fazer modificações.


    6.2 - Encapsulamento
    O que começamos a ver nesse capítulo é a idéia de encapsular, isto é, esconder todos os membros de
uma classe (como vimos acima), além de esconder como funcionam as rotinas (no caso métodos) do nosso
sistema.

    Encapsular é fundamental para que seu sistema seja sucetível a mudanças: não precisaremos mudar uma
regra de negócio em vários lugares, mas sim em apenas um único lugar, já que essa regra está encapsulada.
(veja o caso do método saca)




    O conjunto de métodos públicos de uma classe é também chamado de interface da classe, pois esta é a
única maneira a qual você se comunica com objetos dessa classe.

                                   Capítulo 6 - Modificadores de acesso e atributos de classe - Encapsulamento - Página 60


[PAGINA 73]
                                                         Material do Treinamento Java e Orientação a Objetos




              Programando voltado para a interface e não para a implementação
            É sempre bom programar pensando na interface da sua classe, como seus usuários a estarão
            utilizando, e não somente em como ela irá funcionar.
            A implementação em si, o conteúdo dos métodos, não tem tanta importância para o usuário dessa
            classe, uma vez que ele só precisa saber o que cada método pretende fazer, e não como ele faz,
            pois isto pode mudar com o tempo.
            Essa frase vem do livro Design Patterns, de Eric Gamma et al. Um livro cultuado no meio da
            orientação a objetos.


    Sempre que vamos acessar um objeto, utilizamos sua interface. Existem diversas analogias fáceis no mundo
real:

    • Quando você dirige um carro, o que te importa são os pedais e o volante (interface) e não o motor que você
      está usando (implementação). É claro que um motor diferente pode te dar melhores resultados, mas o
      que ele faz é a mesma coisa que um motor menos potente, a diferença está em como ele faz. Para trocar
      um carro a álcool para um a gasolina você não precisa reapreender a dirigir! (trocar a implementação dos
      métodos não precisa mudar a interface, fazendo com que as outras classes continuem usando eles da
      mesma maneira).

    • Todos os celulares fazem a mesma coisa (interface), eles possuem maneiras (métodos) de discar, ligar,
      desligar, atender, etc. O que muda é como eles fazem (implementação), mas repare que para o usuário
      comum pouco importa se o celular é GSM ou CDMA, isso fica encapsulado na implementação (que aqui
      são os circuitos).

    Agora temos conhecimentos suficientes para resolver aquele problema da validação de CPF:

class Cliente {
    private String nome;
    private String endereco;
    private String cpf;
    private int idade;

    public void mudaCPF(String cpf) {
        validaCPF(cpf);
        this.cpf = cpf;
    }

    private void validaCPF(String cpf) {
        // série de regras aqui, falha caso nao seja válido
    }

    // ..
}


   Agora, se alguém tentar criar um Cliente e não usar o mudaCPF para alterar um cpf diretamente, vai receber
um erro de compilação, já que o atributo CPF é privado. E o dia que você não precisar verificar o CPF de quem
tem mais de 60 anos? Seu método fica o seguinte:

public void mudaCPF(String cpf) {
    if (this.idade <= 60) {

                                     Capítulo 6 - Modificadores de acesso e atributos de classe - Encapsulamento - Página 61


[PAGINA 74]
                                                          Material do Treinamento Java e Orientação a Objetos




          validaCPF(cpf);
      }
      this.cpf = cpf;
}


    O controle sobre o CPF está centralizado: ninguém consegue acessá-lo sem passar por aí, a classe Cliente
é a única responsável pelos seus próprios atributos!


    6.3 - Getters e Setters
    O modificador private faz com que ninguém consiga modificar, nem mesmo ler, o atributo em questão. Com
isso temos um problema: como fazer para mostrar o saldo de uma Conta, agora que nem mesmo podemos
acessa-lo para leitura?

    Precisamos então arranjar uma maneira de fazer esse acesso. Sempre que precisamos arrumar uma
maneira de fazer alguma coisa com um objeto, utilizamos de métodos! Vamos então criar um método,
digamos pegaSaldo, para realizar essa simples tarefa:

public class Conta {

      private double saldo;

      // outros atributos omitidos

      private double pegaSaldo() {
          return this.saldo;
      }

      // deposita() saca() e transfere() omitios
}


     Agora, para acessarmos o saldo de uma conta, podemos fazer:

class TestaAcessoComPegaSaldo {
   public static void main(String args[]) {
    Conta minhaConta = new Conta();
    minhaConta.deposita(1000);
    System.out.println("Saldo: " + minhaConta.pegaSaldo());
   }
}


   Para permitir o acesso aos atributos (já que eles são private) de uma maneira controlada, a prática mais
comum é criar dois métodos, um que retorna o valor e outro que muda o valor.

    A convenção para esses métodos é de colocar a palavra get ou set antes do nome do atributo. Por exemplo,
a nossa conta com saldo, limite e titular fica assim, no caso da gente desejar dar acesso a leitura e escrita
a todos os atributos:

public class Conta {

      private double saldo;

                                     Capítulo 6 - Modificadores de acesso e atributos de classe - Getters e Setters - Página 62


[PAGINA 75]
                                                        Material do Treinamento Java e Orientação a Objetos




    private double limite;
    private Cliente titular;

    public double getSaldo() {
        return this.saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public double getLimite() {
        return this.limite;
    }

    public void setLimite(double limite) {
        this.limite = limite;
    }

    public Cliente getTitular() {
        return this.titular;
    }

    public void setTitular(Cliente titular) {
        this.titular = titular;
    }
}


   É uma má prática criar uma classe e, logo em seguida, criar getters e setters para todos seus atributos.
Você só deve criar um getter ou setter se tiver a real necessidade. Repare que nesse exemplo setSaldo não
deveria ter sido criado, já que queremos que todos usem deposita() e saca().

    Outro detalhe importante, um método getX não necessariamente retorna o valor de um atributo que chama X
do objeto em questão. Isso é interessante para o encapsulamento. Imagine a situação: queremos que o banco
sempre mostre como saldo o valor do limite somado ao saldo (uma prática comum dos bancos que costuma
iludir seus clientes). Poderíamos sempre chamar c.getLimite() + c.getSaldo(), mas isso poderia gerar uma
situação de “replace all” quando precisássemos mudar como o saldo é mostrado. Podemos encapsular isso em
um método e, porque não, dentro do próprio getSaldo? Repare:

public class Conta {

    private double saldo;
    private double limite;
    private Cliente titular;

    public double getSaldo() {
        return this.saldo + this.limite;
    }

    // deposita() saca() e transfere() omitidos

    public Cliente getTitular() {
        return this.titular;
    }


                                   Capítulo 6 - Modificadores de acesso e atributos de classe - Getters e Setters - Página 63


[PAGINA 76]
                                                         Material do Treinamento Java e Orientação a Objetos




      public void setTitular(Cliente titular) {
          this.titular = titular;
      }
}


    O código acima nem possibilita a chamada do método getLimite(), ele não existe. E nem deve existir
enquanto não houver essa necessidade. O método getSaldo() não devolve simplesmente o saldo... e sim o que
queremos que seja mostrado como se fosse o saldo. Utilizar getters e setters não só ajuda você a proteger seus
atributos, como também possibilita ter de mudar algo em um só lugar... chamamos isso de encapsulamento,
pois esconde a maneira como os objetos guardam seus dados. É uma prática muito importante.

    Nossa classe está agora totalmente pronta? Isto é, existe a chance dela ficar com menos dinheiro do que
o limite? Pode parecer que não, mas, e se depositarmos um valor negativo na conta? Ficaríamos com menos
dinheiro que o permitido, já que não esperávamos por isso. Para nos proteger disso basta mudarmos o método
deposita() para que ele verifique se o valor é necessariamente positivo.

   Depois disso precisaríamos mudar mais algum outro código? A resposta é não, graças ao encapsulamento
dos nossos dados.

               Cuidado com os getters e setters!
              Como já dito, não devemos criar getters e setters sem um motivo explicito. No blog da Caelum há
              um artigo que ilustra bem esses casos:
              http://blog.caelum.com.br/2006/09/14/nao-aprender-oo-getters-e-setters/


    6.4 - Construtores
    Quando usamos a palavra chave new, estamos construindo um objeto. Sempre quando o new é chamado,
ele executa o construtor da classe. O construtor da classe é um bloco declarado com o mesmo nome que a
classe:

class Conta {
    int numero;
    Cliente titular;
    double saldo;
    double limite;

      // construtor
      Conta() {
          System.out.println("Construindo uma conta.");
      }

      // ..
}


     Então, quando fizermos:

Conta c = new Conta();




                                        Capítulo 6 - Modificadores de acesso e atributos de classe - Construtores - Página 64


[PAGINA 77]
                                                             Material do Treinamento Java e Orientação a Objetos




   A mensagem “construindo uma conta” aparecerá. É como uma rotina de inicialização que é chamada
sempre que um novo objeto é criado. Um construtor pode parecer, mas não é um método.


               O construtor default
              Até agora, as nossas classes não possuíam nenhum construtor. Então como é que era possível
              dar new, se todo new chama um construtor obrigatoriamente?
              Quando você não declara nenhum construtor na sua classe, o Java cria um para você. Esse
              construtor é o construtor default, ele não recebe nenhum argumento e o corpo dele é vazio.
              A partir do momento que você declara um construtor, o construtor default não é mais fornecido.


    O interessante é que um construtor pode receber um argumento, podendo assim inicializar algum tipo de
informação:

class Conta {
    int numero;
    Cliente titular;
    double saldo;
    double limite;

      // construtor
      Conta(Cliente titular) {
          this.titular = titular;
      }

      // ..
}


     Esse construtor recebe o titular da conta. Assim, quando criarmos uma conta, ela já terá um determinado
titular.

Cliente carlos = new Cliente();
carlos.nome = "Carlos";

Conta c = new Conta(carlos);
System.out.println(c.titular.nome);



    6.5 - A necessidade de um construtor
     Tudo estava funcionando até agora. Para que utilizamos um construtor?

    A idéia é bem simples. Se toda conta precisa de um titular, como obrigar todos os objetos que forem criados
a ter um valor desse tipo? Basta criar um único construtor que recebe essa String!

   O construtor se resume a isso! Dar possibilidades ou obrigar o usuário de uma classe a passar argumentos
para o objeto durante o processo de criação do mesmo.

     Por exemplo, não podemos abrir um arquivo para leitura sem dizer qual é o nome do arquivo que desejamos
ler! Portanto, nada mais natural que passar uma String representando o nome de um arquivo na hora de criar
um objeto do tipo de leitura de arquivo, e que isso seja obrigatório.


                         Capítulo 6 - Modificadores de acesso e atributos de classe - A necessidade de um construtor - Página 65


[PAGINA 78]
                                                               Material do Treinamento Java e Orientação a Objetos




   Você pode ter mais de um construtor na sua classe e, no momento do new, o construtor apropriado será
escolhido.

               Construtor: um método especial?
           Um construtor não é um método. Algumas pessoas o chamam de um método especial, mas defini-
           tivamente não é, já que não possui retorno e só é chamado durante a construção do objeto.


             Chamando outro construtor
           Um construtor só pode rodar durante a construção do objeto, isto é, você nunca conseguirá chamar
           o construtor em um objeto já construído. Porém, durante a construção de um objeto, você pode
           fazer com que um construtor chame outro, para não ter de ficar copiando e colando:

            class Conta {

                  int numero;
                  Cliente titular;
                  double saldo;
                  double limite;

                  // construtor
                  Conta(Cliente titular) {
                      //     faz mais uma série de inicializações e configurações
                      this.titular = titular;
                  }

                  public Conta (int numero, Cliente titular) {
                      this(titular); // chama o construtor que foi declarado acima
                      this.numero = numero;
                  }

                  //..
           }




   Existe um outro motivo, o outro lado dos construtores: facilidade. Às vezes, criamos um construtor que
recebe diversos argumentos para não obrigar o usuário de uma classe a chamar diversos métodos do tipo
’set’.

   No nosso exemplo do CPF, podemos forçar que a classe Cliente receba no mínimo o CPF, dessa maneira
um Cliente já será construído e com um CPF válido.


               Java Bean
           Quando criamos uma classe com todos os atributos privados, seus getters e setters e um construtor
           vazio (padrão), na verdade estamos criando um Java Bean (mas não confunda com EJB, que é
           Enterprise Java Beans).
           Para saber mais acesse: http://java.sun.com/products/javabeans/




                           Capítulo 6 - Modificadores de acesso e atributos de classe - A necessidade de um construtor - Página 66


[PAGINA 79]
                                                          Material do Treinamento Java e Orientação a Objetos




    6.6 - Atributos de classe
    Nosso banco também quer controlar a quantidade de contas existentes no sistema. Como poderíamos fazer
isto? A idéia mais simples:

Conta c = new Conta();
totalDeContas = totalDeContas + 1;


   Aqui, voltamos em um problema parecido com o da validação de CPF. Estamos espalhando um código por
toda aplicação, e quem garante que vamos conseguir lembrar de incrementar a variável totalDeContas toda
vez?

     Tentamos então, passar para a seguinte proposta:

class Conta {
    private int totalDeContas;
    //...

      Conta() {
          this.totalDeContas = this.totalDeContas + 1;
      }
}


  Quando criarmos duas contas, qual será o valor do totalDeContas de cada uma delas? Vai ser 1. Pois cada
uma tem essa variável. O atributo é de cada objeto.

    Seria interessante então, que essa variável fosse única, compartilhada por todos os objetos dessa classe.
Dessa maneira, quando mudasse através de um objeto, o outro enxergaria o mesmo valor. Para fazer isso em
java, declaramos a variável como static.

private static int totalDeContas;


   Quando declaramos um atributo como static, ele passa a não ser mais um atributo de cada objeto, e sim
um atributo da classe, a informação fica guardada pela classe, não é mais individual para cada objeto.

     Para acessarmos um atributo estático, não usamos a palavra chave this, mas sim o nome da classe:

class Conta {
    private static int totalDeContas;
    //...

      Conta() {
          Conta.totalDeContas = Conta.totalDeContas + 1;
      }
}


   Já que o atributo é privado, como podemos acessar essa informação a partir de outra classe? Precisamos
de um getter para ele!




                                   Capítulo 6 - Modificadores de acesso e atributos de classe - Atributos de classe - Página 67


[PAGINA 80]
                                                         Material do Treinamento Java e Orientação a Objetos




class Conta {
    private static int totalDeContas;
    //...

      Conta() {
          Conta.totalDeContas = Conta.totalDeContas + 1;
      }

      public int getTotalDeContas() [
          return Conta.totalDeContas;
      }
}


     Como fazemos então para saber quantas contas foram criadas?

Conta c = new Conta();
int total = c.getTotalDeContas();


   Precisamos criar uma conta antes de chamar o método! Isso não é legal, pois gostaríamos de saber quantas
contas existem sem precisar ter acesso a um objeto conta. A idéia aqui é a mesma, transformar esse método
que todo objeto conta tem em um método de toda a classe. Usamos a palavra static de novo, mudando o
método anterior.

public static int getTotalDeContas() {
    return Conta.totalDeContas;
}


     Para acessar esse novo método:

int total = Conta.getTotalDeContas();


   Repare que estamos chamando um método não com uma referência para uma Conta, e sim usando o nome
da classe.

              Métodos e atributos estáticos
            Métodos e atributos estáticos só podem acessar outros métodos e atributos estáticos da mesma
            classe, o que faz todo sentido já que dentro de um método estático não temos acesso a referência
            “this”, pois um método estático é chamado através da classe, e não de um objeto.
            O static realmente traz um “cheiro” procedural, porém em muitas vezes é necessário.


    6.7 - Um pouco mais...

1) Em algumas empresas, o UML é amplamente utilizado. Às vezes, o programador recebe o UML já pronto,
   completo, e só deve preencher a implementação, devendo seguir à risca o UML. O que você acha dessa
   prática? Vantagens e desvantagens.

2) Se uma classe só tem atributos e métodos estáticos, que conclusões podemos tirar? O que lhe parece um
   método estático?

                                    Capítulo 6 - Modificadores de acesso e atributos de classe - Um pouco mais... - Página 68


[PAGINA 81]
                                                               Material do Treinamento Java e Orientação a Objetos




3) O padrão dos métodos get e set não vale para as variáveis de tipo boolean. Esses atributos são acessados
   via is e set. Por exemplo, para verificar se um carro está ligado seriam criados os métodos isLigado e
   setLigado.


 6.8 - Exercícios: Encapsulamento, construtores e static

1) Adicione o modificador de visibilidade (private, se necessário) para cada atributo e método da classe
   Funcionario. Tente criar um Funcionario no main e modificar ou ler um de seus atributos privados. O
   que acontece?

2) Crie os getters e setters necessários da sua classe Funcionario . Por exemplo:

   class Funcionario {

       private double salario;

       // ...

       public double getSalario() {
           return this.salario;
       }

       public void setSalario(double salario) {
           this.salario = salario;
       }
   }


   Não copie e cole! Aproveite para praticar sintaxe. Logo passaremos a usar o Eclipse e aí sim teremos
   procedimentos mais simples para este tipo de tarefa.

3) Modifique suas classes que acessam e modificam atributos de um Funcionario para utilizar os getters e
   setters recém criados.
   Por exemplo, onde você encontra:

   f.salario = 100;

   System.out.println(f.salario);

   passa para:

   f.setSalario(100);

   System.out.println(f.getSalario());


4) Faça com que sua classe Funcionario possa receber, opcionalmente, o nome do Funcionario durante a
   criação do objeto. Utilize construtores para obter esse resultado.
   Dica: utilize um construtor sem argumentos também, para o caso de a pessoa não querer passar o nome do
   Funcionario.
   Seria algo como:

   class Funcionario {


         Capítulo 6 - Modificadores de acesso e atributos de classe - Exercícios: Encapsulamento, construtores e static - Página 69


[PAGINA 82]
                                                        Material do Treinamento Java e Orientação a Objetos




       public Funcionario() {
           // construtor sem argumentos
       }

       public Funcionario(String nome) {
           // construtor que recebe o nome
       }
   }

   Por que você precisa do construtor sem argumentos para que a passagem do nome seja opcional?

5) (opcional) Adicione um atributo na classe Funcionario de tipo int que se chama identificador. Esse identifi-
   cador deve ter um valor único para cada instância do tipo Funcionario. O primeiro Funcionario instanciado
   tem identificador 1, o segundo 2, e assim por diante. Você deve utilizar os recursos aprendidos aqui para
   resolver esse problema.
   Crie um getter para o identificador. Devemos ter um setter?

6) (opcional) Crie os getters e setters da sua classe Empresa e coloque seus atributos como private. Lembre-se
   de que não necessariamente todos os atributos devem ter getters e setters.
   Por exemplo, na classe Empresa, seria interessante ter um setter e getter para a sua array de funcionários?
   Não seria mais interessante ter um método como este?

   class Empresa {

       // ...

       public Funcionario getFuncionario(int posicao) {
           return this.empregados[posicao];
       }
   }


7) (opcional) Na classe Empresa, em vez de criar um array de tamanho fixo, receba como parâmetro no cons-
   trutor o tamanho do array de Funcionario.
   Agora, com esse construtor, o que acontece se tentarmos dar new Empresa() sem passar argumento algum?
   Por quê?

8) (opcional) Como garantir que datas como 31/2/2005 não sejam aceitas pela sua classe Data?

9) (opcional) Crie a classe PessoaFisica. Queremos ter a garantia de que pessoa física alguma tenha CPF
   invalido, nem seja criada PessoaFisica sem cpf inicial. (você não precisa escrever o algoritmo de validação
   de cpf, basta passar o cpf por um método valida(String x)....)


 6.9 - Desafios

1) Porque esse código não compila?

   class Teste {

       int x = 37;
       public static void main(String [] args) {
           System.out.println(x);
       }

                                           Capítulo 6 - Modificadores de acesso e atributos de classe - Desafios - Página 70


[PAGINA 83]
                                                      Material do Treinamento Java e Orientação a Objetos




   }


2) Imagine que tenha uma classe FabricaDeCarro e quero garantir que só existe um objeto desse tipo em toda
   a memória. Não existe uma palavra chave especial para isto em java, então teremos de fazer nossa classe
   de tal maneira que ela respeite essa nossa necessidade. Como fazer isso? (pesquise: singleton design
   pattern)




                                         Capítulo 6 - Modificadores de acesso e atributos de classe - Desafios - Página 71


[PAGINA 84]
                                                                                     C APÍTULO   7

Orientação a Objetos – herança, reescrita e
polimorfismo
                                                          “O homem absurdo é aquele que nunca muda.”
                                                                                – Georges Clemenceau


   Ao término desse capítulo, você será capaz de:

   • dizer o que é herança e quando utilizá-la;

   • reutilizar código escrito anteriormente;

   • criar classes filhas e reescrever métodos;

   • usar todo o poder que o polimorfismo da.


 7.1 - Repetindo código?
   Como toda empresa, nosso Banco possui funcionários. Vamos modelar a classe Funcionario:

class Funcionario {
    String nome;
    String cpf;
    double salario;
     // métodos devem vir aqui
}


   s Além de um funcionário comum, há também outros cargos, como os gerentes. Os gerentes guardam a
mesma informação que um funcionário comum, mas possuem outras informações, além de ter funcionalidades
um pouco diferentes. Um gerente no nosso banco possui também uma senha numérica que permite o acesso
ao sistema interno do banco, além do número de funcionários que ele gerencia:

class Gerente {
    String nome;
    String cpf;
    double salario;
    int senha;
    int numeroDeFuncionariosGerenciados;

    public boolean autentica(int senha) {
        if (this.senha == senha) {
            System.out.println("Acesso Permitido!");

                                                    72


[PAGINA 85]
                                                           Material do Treinamento Java e Orientação a Objetos




             return true;
         } else {
             System.out.println("Acesso Negado!");
             return false;
         }
    }

    // outros métodos
}



             Precisamos mesmo de outra classe?
            Poderíamos ter deixado a classe Funcionario mais genérica, mantendo nela senha de acesso, e o
            número de funcionários gerenciados. Caso o funcionário não fosse um gerente, deixaríamos estes
            atributos vazios.
            Essa é uma possibilidade, porém podemos começar a ter muito atributos opcionais, e a classe
            ficaria estranha. E em relação aos métodos? A classe Gerente tem o método autentica, que não
            faz sentido existir em um funcionário que não é gerente.


    Se tivéssemos um outro tipo de funcionário que tem características diferentes do funcionário comum, preci-
saríamos criar uma outra classe e copiar o código novamente!

   Além disso, se um dia precisarmos adicionar uma nova informação para todos os funcionários, precisaremos
passar por todas as classes de funcionário e adicionar esse atributo. O problema acontece novamente por não
centralizar as informações principais do funcionário em um único lugar!

    Existe um jeito, em Java, de relacionarmos uma classe de tal maneira que uma delas herda tudo que a outra
tem. Isto é uma relação de classe mãe e classe filha. No nosso caso, gostaríamos de fazer com que o Gerente
tivesse tudo que um Funcionario tem, gostaríamos que ela fosse uma extensão de Funcionario. Fazemos isto
através da palavra chave extends.

class Gerente extends Funcionario {
    int senha;
    int numeroDeFuncionariosGerenciados;

    public boolean autentica(int senha) {
        if (this.senha == senha) {
            System.out.println("Acesso Permitido!");
            return true;
        } else {
            System.out.println("Acesso Negado!");
            return false;
        }
    }

    // setter da senha omitido
}


    Em todo momento que criarmos um objeto do tipo Gerente, este objeto possuirá também os atributos defi-
nidos na classe Funcionario, pois agora um Gerente é um Funcionario:



                          Capítulo 7 - Orientação a Objetos – herança, reescrita e polimorfismo - Repetindo código? - Página 73


[PAGINA 86]
                                                           Material do Treinamento Java e Orientação a Objetos




class TestaGerente {
    public static void main(String[] args) {
        Gerente gerente = new Gerente();

         // podemos chamar metodos do Funcionario:
         gerente.setNome("João da Silva");

         // e tambem metodos do Gerente!
         gerente.setSenha(4231);
    }
}


   Dizemos que a classe Gerente herda todos os atributos e métodos da classe mãe, no nosso caso, a
Funcionario. Para ser mais preciso, ela também herda os atributos e métodos privados, porém não conse-
gue acessá-los diretamente.


             Super e Sub classe
            A nomenclatura mais encontrada é que Funcionario é a superclasse de Gerente, e Gerente é a
            subclasse de Funcionario. Dizemos também que todo Gerente é um Funcionário. Outra forma é
            dizer que Funcionario é classe mãe de Gerente e Gerente é classe filha de Funcionario.


   E se precisamos acessar os atributos que herdamos? Não gostaríamos de deixar os atributos de
Funcionario, public, pois dessa maneira qualquer um poderia alterar os atributos dos objetos deste tipo. Existe
um outro modificador de acesso, o protected, que fica entre o private e o public. Um atributo protected só
pode ser acessado (visível) pela própria classe e por suas subclasses (e mais algumas outras classes, mas
veremos isso em outro capítulo).

class Funcionario {
    protected String nome;
    protected String cpf;
    protected double salario;
    // métodos devem vir aqui
}




                          Capítulo 7 - Orientação a Objetos – herança, reescrita e polimorfismo - Repetindo código? - Página 74


[PAGINA 87]
                                                          Material do Treinamento Java e Orientação a Objetos




             Sempre usar protected?
           Então porque usar private? Depois de um tempo programando orientado a objetos, você vai
           começar a sentir que nem sempre é uma boa idéia deixar que a classe filha acesse os atributos
           da classe mãe, pois isso quebra um pouco a idéia de que só aquela classe deveria manipular seus
           atributos. Essa é uma discussão um pouco mais avançada.
           Além disso, não só as subclasses, mas também as outras classes, podem acessar os atributos
           protected, que veremos mais a frente (mesmo pacote). Veja outras alternativas ao protected no
           exercício de discussão em sala de aula juntamente com o instrutor.


    Da mesma maneira podemos ter uma classe Diretor que estenda Gerente, e a classe Presidente pode
estender diretamente de Funcionario.

    Fique claro que essa é uma decisão de negócio. Se Diretor vai estender de Gerente ou não, vai depender
se, para você, Diretor “é um” Gerente.

   Uma classe pode ter várias filhas, mas pode ter apenas uma mãe, é a chamada herança simples do java.




 7.2 - Reescrita de método
   Todo fim de ano, os funcionários do nosso banco recebem uma bonificação. Os funcionários comuns rece-
bem 10% do valor do salário e os gerentes, 15%.

   Vamos ver como fica a classe Funcionario:

class Funcionario {
    protected String nome;
    protected String cpf;
    protected double salario;

    public double getBonificacao() {
        return this.salario * 0.10;
    }
    // métodos


                       Capítulo 7 - Orientação a Objetos – herança, reescrita e polimorfismo - Reescrita de método - Página 75


[PAGINA 88]
                                                              Material do Treinamento Java e Orientação a Objetos




}


     Se deixarmos a classe Gerente como ela está, ela vai herdar o método getBonificacao.

Gerente gerente = new Gerente();
gerente.setSalario(5000.0);
System.out.println(gerente.getBonificacao());


   O resultado aqui será 500. Não queremos essa resposta, pois o gerente deveria ter 750 de bônus nesse
caso. Para consertar isso, uma das opções seria criar um novo método na classe Gerente, chamado, por
exemplo, getBonificacaoDoGerente. O problema é que agora teríamos dois métodos em Gerente, confundindo
bastante quem for usar essa classe, além de que cada um da uma resposta diferente.

    No Java, quando herdamos um método, podemos alterar seu comportamento. Podemos reescrever (rees-
crever, sobrescrever, override) este método:

class Gerente extends Funcionario {
    int senha;
    int numeroDeFuncionariosGerenciados;

      public double getBonificacao() {
          return this.salario * 0.15;
      }
      // ...
}


    Agora sim, o método está correto para o Gerente. Refaça o teste e veja que agora o valor impresso é o
correto (750):

Gerente gerente = new Gerente();
gerente.setSalario(5000.0);
System.out.println(gerente.getBonificacao());



    7.3 - Invocando o método reescrito
    Depois de reescrito, não podemos mais chamar o método antigo que fora herdado da classe mãe: realmente
alteramos o seu comportamento. Mas podemos invocá-lo no caso de estarmos dentro da classe.

   Imagine que para calcular a bonificação de um Gerente devemos fazer igual ao cálculo de um Funcionario
porem adicionando R$ 1000. Poderíamos fazer assim:

class Gerente extends Funcionario {
    int senha;
    int numeroDeFuncionariosGerenciados;

      public double getBonificacao() {
          return this.salario * 0.10 + 1000;
      }
       // ...


                  Capítulo 7 - Orientação a Objetos – herança, reescrita e polimorfismo - Invocando o método reescrito - Página 76


[PAGINA 89]
                                                           Material do Treinamento Java e Orientação a Objetos




}


   Aqui teríamos um problema: o dia que o getBonificacao do Funcionario mudar, precisaremos mudar o
método do Gerente para acompanhar a nova bonificação. Para evitar isso, o getBonificacao do Gerente pode
chamar o do Funcionario utilizando-se da palavra chave super.

class Gerente extends Funcionario {
    int senha;
    int numeroDeFuncionariosGerenciados;

      public double getBonificacao() {
          return super.getBonificacao() + 1000;
      }
       // ...
}


   Essa invocação vai procurar o método com o nome getBonificacao de uma super classe de Gerente. No
caso ele logo vai encontrar esse método em Funcionario.

   Essa é uma prática comum, pois muitos casos o método reescrito geralmente faz “algo a mais” que o método
da classe mãe. Chamar ou não o método de cima é uma decisão sua e depende do seu problema. Algumas
vezes não faz sentido invocar o método que reescrevemos.


    7.4 - Polimorfismo
      O que guarda uma variável do tipo Funcionario? Uma referência para um Funcionario, nunca o objeto em
si.

   Na herança, vimos que todo Gerente é um Funcionario, pois é uma extensão deste. Podemos nos referir a
um Gerente como sendo um Funcionario. Se alguém precisa falar com um Funcionario do banco, pode falar
com um Gerente! Porque? Pois Gerente é um Funcionario. Essa é a semântica da herança.

Gerente gerente = new Gerente();
Funcionario funcionario = gerente;
funcionario.setSalario(5000.0);




   Polimorfismo é a capacidade de um objeto poder ser referenciado de várias formas. (cuidado, polimorfismo
não quer dizer que o objeto fica se transformando, muito pelo contrário, um objeto nasce de um tipo e morre
daquele tipo, o que pode mudar é a maneira como nos referimos a ele).

                               Capítulo 7 - Orientação a Objetos – herança, reescrita e polimorfismo - Polimorfismo - Página 77


[PAGINA 90]
                                                          Material do Treinamento Java e Orientação a Objetos




    Até aqui tudo bem, mas e se eu tentar:

funcionario.getBonificacao();


    Qual é o retorno desse método? 500 ou 750? No Java, a invocação de método sempre vai ser decidida
em tempo de execução. O Java vai procurar o objeto na memória e, aí sim, decidir qual método deve ser
chamado, sempre relacionando com sua classe de verdade, e não com a que estamos usando para referenciá-
lo. Apesar de estarmos nos referenciando a esse Gerente como sendo um Funcionario, o método executado é
o do Gerente. O retorno é 750.

   Parece estranho criar um gerente e referenciá-lo como apenas um funcionário. Por que fariamos isso?
Na verdade, a situação que costuma aparecer é a que temos um método que recebe um argumento do tipo
Funcionario:


class ControleDeBonificacoes {
    private double totalDeBonificacoes = 0;

    public void registra(Funcionario funcionario) {
        this.totalDeBonificacoes += funcionario.getBonificacao();
    }

    public double getTotalDeBonificacoes() {
        return this.totalDeBonificacoes;
    }
}


    E, em algum lugar da minha aplicação (ou no main, se for apenas para testes):

ControleDeBonificacoes controle = new ControleDeBonificacoes();

Gerente funcionario1 = new Gerente();
funcionario1.setSalario(5000.0);
controle.registra(funcionario1);

Funcionario funcionario2 = new Funcionario();
funcionario2.setSalario(1000.0);
controle.registra(funcionario2);

System.out.println(controle.getTotalDeBonificacoes());


   Repare que conseguimos passar um Gerente para um método que recebe um Funcionario como argu-
mento. Pense como numa porta na agência bancária com o seguinte aviso: “Permitida a entrada apenas de
Funcionários”. Um gerente pode passar nessa porta? Sim, pois Gerente é um Funcionario.

   Qual será o valor resultante? Não importa que dentro do método registra do ControleDeBonificacoes receba
Funcionario. Quando ele receber um objeto que realmente é um Gerente, o seu método reescrito será invocado.
Reafirmando: não importa como nos referenciamos a um objeto, o método que será invocado é sempre
o que é dele.

  No dia em que criarmos uma classe Secretaria, por exemplo, que é filha de Funcionario, precisaremos
mudar a classe de ControleDeBonificacoes? Não. Basta a classe Secretaria reescrever os métodos que lhe


                              Capítulo 7 - Orientação a Objetos – herança, reescrita e polimorfismo - Polimorfismo - Página 78


[PAGINA 91]
                                                          Material do Treinamento Java e Orientação a Objetos




parecerem necessários. É exatamente esse o poder do polimorfismo, juntamente com a reescrita de método:
diminuir o acoplamento entre as classes, para evitar que novos códigos resultem em modificações em inúmeros
lugares.

   Repare que quem criou ControleDeBonificacoes pode nunca ter imaginado a criação da classe Secretaria
ou Engenheiro. Contudo, não será necessário reimplementar esse controle em cada nova classe: reaproveita-
mos aquele código.


             Herança versus acoplamento
           Note que o uso de herança aumenta o acoplamento entre as classes, isto é, o quanto uma classe
           depende de outra. A relação entre classe mãe e filha é muito forte e isso acaba fazendo com que
           o programador das classes filhas tenha que conhecer a implementação da classe pai e vice-versa
           - fica difícil fazer uma mudança pontual no sistema.
           Por exemplo, imagine se tivermos que mudar algo na nossa classe Funcionario, mas não quisés-
           semos que todos os funcionários sofressem a mesma mudança. Precisaríamos passar por cada
           uma das filhas de Funcionario verificando se ela se comporta como deveria ou se devemos, agora,
           sobreescrever o tal método modificado.
           Esse é um problema da herança, e não do polimorfismo, que resolveremos mais tarde com a ajuda
           de Interfaces.


 7.5 - Um outro exemplo
    Imagine que vamos modelar um sistema para a faculdade que controle as despesas com funcionários e
professores. Nosso funcionário fica assim:

class EmpregadoDaFaculdade {
    private String nome;
    private double salario;
    double getGastos() {
        return this.salario;
    }
    String getInfo() {
        return "nome: " + this.nome + " com salário " + this.salario;
    }
     // métodos de get, set e outros
}


   O gasto que temos com o professor não é apenas seu salário. Temos de somar um bônus de 10 reais por
hora/aula. O que fazemos então? Reescrevemos o método. Assim como o getGastos é diferente, o getInfo
também será, pois temos de mostrar as horas/aula também.

class ProfessorDaFaculdade extends EmpregadoDaFaculdade {
    private int horasDeAula;
    double getGastos() {
        return this.getSalario() + this.horasDeAula * 10;
    }
    String getInfo() {
        String informacaoBasica = super.getInfo();
        String informacao = informacaoBasica + " horas de aula: " + this.horasDeAula;
        return informacao;

                         Capítulo 7 - Orientação a Objetos – herança, reescrita e polimorfismo - Um outro exemplo - Página 79


[PAGINA 92]
                                                           Material do Treinamento Java e Orientação a Objetos




      }
      // métodos de get, set e outros
}


    A novidade, aqui, é a palavra chave super. Apesar do método ter sido reescrito, gostaríamos de acessar o
método da classe mãe, para não ter de copiar e colocar o conteúdo desse método e depois concatenar com a
informação das horas de aula.

     Como tiramos proveito do polimorfismo? Imagine que temos uma classe de relatório:

class GeradorDeRelatorio {
    public void adiciona(EmpregadoDaFaculdade f) {
        System.out.println(f.getInfo());
        System.out.println(f.getGastos());
    }
}


   Podemos passar para nossa classe qualquer EmpregadoDaFaculdade! Vai funcionar tanto para professor,
quanto para funcionário comum.

    Um certo dia, muito depois de terminar essa classe de relatório, resolvemos aumentar nosso sistema, e
colocar uma classe nova, que representa o Reitor. Como ele também é um EmpregadoDaFaculdade, será que
vamos precisar alterar alguma coisa na nossa classe de Relatorio? Não. Essa é a idéia! Quem programou a
classe GeradorDeRelatorio nunca imaginou que existiria uma classe Reitor e, mesmo assim, o sistema funciona.

class Reitor extends EmpregadoDaFaculdade {
     // informações extras
    String getInfo() {
        return super.getInfo() + " e ele é um reitor";
    }
     // não sobreescrevemos o getGastos!!!
}



    7.6 - Um pouco mais...

1) Se não houvesse herança em Java, como você poderia reaproveitar o código de outra classe?

2) Uma discussão muito atual é sobre o abuso no uso da herança. Algumas pessoas usam herança apenas
   para reaproveitar o código, quando poderiam ter feito uma composição. Procure sobre herança versus
   composição.

3) Mesmo depois de reescrever um método da classe mãe, a classe filha ainda pode acessar o método antigo.
   Isto é feito através da palavra chave super.método(). Algo parecido ocorre entre os construtores das classes,
   o que?




                           Capítulo 7 - Orientação a Objetos – herança, reescrita e polimorfismo - Um pouco mais... - Página 80


[PAGINA 93]
                                                                Material do Treinamento Java e Orientação a Objetos




               Mais sobre o mau uso da herança
              No blog da Caelum existe um artigo interessante abordando esse tópico:
              http://blog.caelum.com.br/2006/10/14/como-nao-aprender-orientacao-a-objetos-heranca/
              James Gosling, um dos criadores do Java, é um crítico do mau uso da herança. Nesta entrevista
              ele discute a possibilidade de se utilizar apenas interfaces e composição, eliminando a necessidade
              da herança:
              http://www.artima.com/intv/gosling3P.html


 7.7 - Exercícios: Herança e Polimorfismo

1) Vamos criar uma classe Conta, que possua um saldo, e os métodos para pegar saldo, depositar, e sacar.
   a) Crie a classe Conta:

      class Conta {

      }

   b) Adicione o atributo saldo

      class Conta {

            private double saldo;
      }

   c) Crie os métodos getSaldo(), deposita(double) e saca(double)

      class Conta {

            private double saldo;

            void deposita(double valor) {
                this.saldo += valor;
            }

            void saca(double valor) {
                this.saldo -= valor;
            }

            double getSaldo() {
                return this.saldo;
            }
      }


2) Adicione um método na classe Conta, que atualiza essa conta de acordo com uma taxa percentual fornecida.

   class Conta {

          private double saldo;

          // outros métodos aqui também ...

          void atualiza(double taxa) {

              Capítulo 7 - Orientação a Objetos – herança, reescrita e polimorfismo - Exercícios: Herança e Polimorfismo - Página 81


[PAGINA 94]
                                                                Material do Treinamento Java e Orientação a Objetos




              this.saldo += this.saldo * taxa;
        }
   }


3) Crie duas subclasses da classe Conta: ContaCorrente e ContaPoupanca. Ambas terão o método atualiza
   reescrito: A ContaCorrente deve atualizar-se com o dobro da taxa e a ContaPoupanca deve atualizar-se com
   o triplo da taxa.
   Além disso, a ContaCorrente deve reescrever o método deposita, afim de retirar uma taxa bancária de dez
   centavos de cada depósito.

       • Crie as classes ContaCorrente e ContaPoupanca. Ambas são filhas da classe Conta:

            class ContaCorrente extends Conta {

         }

         class ContaPoupanca extends Conta {
         }

       • Reescreva o método atualiza na classe ContaCorrente, seguindo o enunciado:

            class ContaCorrente extends Conta {

               void atualiza(double taxa) {
                   this.saldo += this.saldo * taxa * 2;
               }
         }

         Repare que, para acessar o atributo saldo herdado da classe Conta, você vai precisar trocar o modifi-
         cador de visibilidade de saldo para protected.
       • Reescreva o método atualiza na classe ContaPoupanca, seguindo o enunciado:

            class ContaPoupanca extends Conta {

               void atualiza(double taxa) {
                   this.saldo += this.saldo * taxa * 3;
               }
         }

       • Na classe ContaCorrente, reescreva o método deposita para descontar a taxa bancária de dez
         centavos:

            class ContaCorrente extends Conta {

               void atualiza(double taxa) {
                   this.saldo += this.saldo * taxa * 2;
               }

               void deposita(double valor) {
                   this.saldo += valor - 0.10;
               }
         }




              Capítulo 7 - Orientação a Objetos – herança, reescrita e polimorfismo - Exercícios: Herança e Polimorfismo - Página 82


[PAGINA 95]
                                                              Material do Treinamento Java e Orientação a Objetos




4) Crie uma classe com método main e instancie essas classes, atualize-as e veja o resultado. Algo como:

   class TestaContas {

       public static void main(String[] args) {
           Conta c = new Conta();
           ContaCorrente cc = new ContaCorrente();
           ContaPoupanca cp = new ContaPoupanca();

           c.deposita(1000);
           cc.deposita(1000);
           cp.deposita(1000);

           c.atualiza(0.01);
           cc.atualiza(0.01);
           cp.atualiza(0.01);

           System.out.println(c.getSaldo());
           System.out.println(cc.getSaldo());
           System.out.println(cp.getSaldo());

       }
   }

   Após imprimir o saldo (getSaldo()) de cada uma das contas, o que acontece?
5) O que você acha de rodar o código anterior da seguinte maneira:

   Conta c = new Conta();

   Conta cc = new ContaCorrente();
   Conta cp = new ContaPoupanca();

   Compila? Roda? O que muda? Qual é a utilidade disso? Realmente, essa não é a maneira mais útil do
   polimorfismo - veremos o seu real poder no próximo exercício. Porém existe uma utilidade de declararmos
   uma variável de um tipo menos específico do que o objeto realmente é.
   É extremamente importante perceber que não importa como nos referimos a um objeto, o método que
   será invocado é sempre o mesmo! A JVM vai descobrir em tempo de execução qual deve ser invocado,
   dependendo de que tipo é aquele objeto e não de acordo com como nos referimos a ele.

            Capítulo 7 - Orientação a Objetos – herança, reescrita e polimorfismo - Exercícios: Herança e Polimorfismo - Página 83


[PAGINA 96]
                                                               Material do Treinamento Java e Orientação a Objetos




 6) (opcional) Vamos criar uma classe que seja responsável por fazer a atualização de todas as contas
    bancárias e gerar um relatório com o saldo anterior e saldo novo de cada uma das contas.

    class AtualizadorDeContas {

        private double saldoTotal = 0;
        private double selic;

        AtualizadorDeContas(double selic) {
            this.selic = selic;
        }

        void roda(Conta c) {
            // aqui voce imprime o saldo anterior, atualiza a conta,
            // e depois imprime o saldo final
            // lembrando de somar o saldo final ao atributo saldoTotal
        }

        // outros métodos, colocar o getter para saldoTotal!
    }


 7) (opcional) No método main, vamos criar algumas contas e rodá-las:

    class TestaAtualizadorDeContas {

        public static void main(String[] args) {
            Conta c = new Conta();
            Conta cc = new ContaCorrente();
            Conta cp = new ContaPoupanca();

             c.deposita(1000);
             cc.deposita(1000);
             cp.deposita(1000);

             AtualizadorDeContas adc = new AtualizadorDeContas(0.01);

             adc.roda(c);
             adc.roda(cc);
             adc.roda(cp);

             System.out.println("Saldo Total: " + adc.getSaldoTotal());
        }

    }


 8) (Opcional) Use a palavra chave super nos métodos atualiza reescritos, para não ter de refazer o trabalho.

 9) (Opcional) Se você precisasse criar uma classe ContaInvestimento, e seu método atualiza fosse complica-
    díssimo, você precisaria alterar as classes Banco e AtualizadorDeContas?

10) (Opcional, Trabalhoso) Crie uma classe Banco que possui um array de Conta. Repare que num array de
    Conta você pode colocar tanto ContaCorrente quanto ContaPoupanca. Crie um método void adiciona(Conta
    c), um método Conta pegaConta(int x) e outro int pegaTotalDeContas(), muito similar a relação anterior
    de Empresa-Funcionario.


             Capítulo 7 - Orientação a Objetos – herança, reescrita e polimorfismo - Exercícios: Herança e Polimorfismo - Página 84


[PAGINA 97]
                                                                 Material do Treinamento Java e Orientação a Objetos




   Faça com que seu método main crie diversas contas, insira-as no Banco e depois, com um for, percorra
   todas as contas do Banco para passá-las como argumento para o AtualizadorDeContas.


 7.8 - Dicussões em aula: Alternativas ao atributo protected
   Discuta com o instrutor e seus colegas alternativas ao uso do atributo protected na herança. Preciso re-
almente afrouxar o encapsulamento do atributo por causa da herança? Como fazer para o atributo continuar
private na mãe e as filhas conseguirem de alguma formar trabalhar com ele?




Capítulo 7 - Orientação a Objetos – herança, reescrita e polimorfismo - Dicussões em aula: Alternativas ao atributo protected - Página
                                                                                                                                    85


[PAGINA 98]
                                                                                            C APÍTULO     8

Eclipse IDE
                                         “Dá-se importância aos antepassados quando já não temos nenhum.”
                                                                                   – François Chateaubriand

    Neste capítulo, você será apresentado ao Ambiente de Desenvolvimento Eclipse e suas principais funciona-
lidades.


 8.1 - O Eclipse
    O Eclipse (http://www.eclipse.org) é uma IDE (integrated development environment). Diferente de uma
RAD, onde o objetivo é desenvolver o mais rápido possível através do arrastar-e-soltar do mouse, onde monta-
nhas de código são gerados em background, uma IDE te auxilia no desenvolvimento, evitando se intrometer e
fazer muita mágica.

    O Eclipse é a IDE líder de mercado. Formada por um consórcio liderado pela IBM, possui seu código livre.
A última versão é a 3.4. Precisamos do Eclipse 3.1 ou posterior, pois a partir dessa versão é que a plataforma
dá suporte ao Java 5.0. Você precisa ter apenas a Java RE instalada.

    Veremos aqui os principais recursos do Eclipse. Você perceberá que ele evita ao máximo te atrapalhar
e apenas gera trechos de códigos óbvios, sempre ao seu comando. Existem também centenas de plugins
gratuitos para gerar diagramas UML, suporte a servidores de aplicação, visualizadores de banco de dados e
muitos outros.

    Baixe o Eclipse do site oficial http://www.eclipse.org. Apesar de ser escrito em Java, a biblioteca gráfica
usada no Eclipse, chamada SWT, usa componentes nativos do sistema operacional. Por isso você deve baixar
a versão correspondente ao seu sistema operacional.

   Descompacte o arquivo e pronto: agora basta rodar o executável.

             Outras IDEs
            Uma outra IDE open source famosa é o Netbeans, da Sun. (http://www.netbeans.org).
            Além dessas, Oracle, Borland e a própria IBM possuem IDEs comerciais e algumas versões mais
            restritas de uso livre.
            A empresa JetBrains desenvolve o IntelliJ IDEA, uma IDE paga que tem ganho muitos adeptos
            ultimamente.


 8.2 - Apresentando o Eclipse
   Clique no ícone do Eclipse no seu Desktop.

   A primeira pergunta que ele te faz é que workspace você vai usar. Workspace define o diretório em que as
suas configurações pessoais e seus projetos serão gravados.

                                                      86


[PAGINA 99]
                                                    Material do Treinamento Java e Orientação a Objetos




   Você pode deixar o diretório pré-definido.

    Logo em seguida, uma tela de Welcome será aberta, onde você tem diversos links para tutoriais e ajuda.
Clique em Workbench. A tela de Welcome do Eclipse 3.3 e do 3.2 (que está na figura abaixo) são um pouco
diferentes da do 3.1.




 8.3 - Views e Perspective
   Feche a tela de Welcome e você verá a tela abaixo. Nesta tela, destacamos as Views (em linha contínua) e
as Perspectives (em linha pontilhada) do Eclipse.




                                                            Capítulo 8 - Eclipse IDE - Views e Perspective - Página 87


[PAGINA 100]
                                                    Material do Treinamento Java e Orientação a Objetos




   Mude para a perspectiva Resource, clicando no ícone ao lado da perspectiva Java, selecionando Other e
depois Resource. Neste momento, trabalharemos com esta perspectiva, antes da de Java, pois ela possui um
conjunto de Views mais simples.




   A View Navigator mostra a estrutura de diretório assim como está no sistema de arquivos. A View Outline
mostra um resumo das classes, interfaces e enumerações declaradas no arquivo java atualmente editado (serve
também para outros tipos de arquivos).

    No menu Window -> Show View -> Other, você pode ver as dezenas de Views que já vem embutidas no
Eclipse. Acostume-se a sempre procurar novas Views, elas podem te ajudar em diversas tarefas.


                                                            Capítulo 8 - Eclipse IDE - Views e Perspective - Página 88


[PAGINA 101]
                                                  Material do Treinamento Java e Orientação a Objetos




8.4 - Criando um projeto novo
 Vá em File -> New -> Project. Seleciona Java Project e clique em Next.




                                                      Capítulo 8 - Eclipse IDE - Criando um projeto novo - Página 89


[PAGINA 102]
                                                    Material do Treinamento Java e Orientação a Objetos




   Crie um projeto chamado banco.

   Você pode chegar nessa mesma tela clicando com o botão da direta no espaço da View Navigator e seguindo
o mesmo menu. Nesta tela, configure seu projeto como na tela abaixo:




                                                        Capítulo 8 - Eclipse IDE - Criando um projeto novo - Página 90


[PAGINA 103]
                                                     Material do Treinamento Java e Orientação a Objetos




    Isto é, marque “create separate source and output folders”, desta maneira seus arquivos java e arquivos
class estarão em diretórios diferentes, para você trabalhar de uma maneira mais organizada.

   Clique em Finish. O Eclipse pedirá para trocar a perspectiva para Java; escolha “No” para permanecer em
Resource. Agora, na View Navigator, você verá o novo projeto e suas pastas e arquivos:




   Vamos iniciar nosso projeto criando a classe Conta. Para isso, vá em File -> New -> Other -> Class. Clique
em Next e crie a classe seguindo a tela abaixo:




   Clique em Finish. O Eclipse possui diversos wizards, mas usaremos o mínimo deles. O interessante é usar o
code assist e quick fixes que a ferramenta possui e veremos em seguida. Não se atente às milhares de opções
de cada wizard, a parte mais interessante do Eclipse não é essa.


                                                         Capítulo 8 - Eclipse IDE - Criando um projeto novo - Página 91


[PAGINA 104]
                                                     Material do Treinamento Java e Orientação a Objetos




    Escreva o método deposita como abaixo e note que o Eclipse reclama de erro em this.saldo pois este
atributo não existe.




   Vamos usar o recurso do Eclipse de quick fix. Coloque o cursor em cima do erro e aperte Ctrl + 1.




    O Eclipse sugerirá possíveis formas de consertar o erro; uma delas é, justamente, criar o campo saldo na
classe Conta, que é nosso objetivo. Clique nesta opção.




    Este recurso de quick fixes, acessível pelo Ctrl+1, é uma das grandes facilidades do Eclipse e é extrema-
mente poderoso. Através dele é possível corrigir boa parte dos erros na hora de programar e, como fizemos,
economizar a digitação de certos códigos repetitivos. No nosso exemplo, não precisamos criar o campo antes;
o Eclipse faz isso para nós. Ele até acerta a tipagem, já que estamos somando ele a um double. O private é
colocado por motivos que já estudamos.

   Vá ao menu File -> Save para gravar. Control + S tem o mesmo efeito.




                                                         Capítulo 8 - Eclipse IDE - Criando um projeto novo - Página 92


[PAGINA 105]
                                                      Material do Treinamento Java e Orientação a Objetos




 8.5 - Criando o main
    Crie uma nova classe chamada Principal. Vamos colocar um método main para testar nossa Conta. Em
vez de digitar todo o método main, vamos usar o code assist do Eclipse. Escreva só main e aperte Ctrl + Espaço
logo em seguida.




                                                                 Capítulo 8 - Eclipse IDE - Criando o main - Página 93


[PAGINA 106]
                                                     Material do Treinamento Java e Orientação a Objetos




    O Eclipse sugerirá a criação do método main completo; selecione esta opção. O control + espaço é chamado
de code assist. Assim como os quick fixes são de extrema importância. Experimente usar o code assist em
diversos lugares.

   Agora, dentro do método main, comece a digitar o seguinte código:

Conta conta = new Conta();
conta.deposita(100.0);


    Observe que, na hora de invocar o método sobre o objeto conta, o Eclipse sugere os métodos possíveis.
Este recurso é bastante útil, principalmente quando estivermos programando com classes que não são as
nossas, como da API do Java. O Eclipse aciona este recurso quando você digita o ponto logo após um objeto
(e você pode usar o Ctrl+Espaço para acioná-lo).

   Agora, vamos imprimir o saldo com System.out.println. Mas, mesmo nesse código, o Eclipse nos ajuda.
Escreva syso e aperte Ctrl+Espaço que o Eclipse escreverá System.out.println() para você.

   Para imprimir, chame o conta.getSaldo():

System.out.println(conta.getSaldo());


   Note que o Eclipse acusará erro em getSaldo() porque este método não existe na classe Conta. Vamos
usar Ctrl+1 em cima do erro para corrigir o problema:




    O Eclipse sugere criar um método getSaldo() na classe Conta. Selecione esta opção e o método será
inserido automaticamente.


                                                                Capítulo 8 - Eclipse IDE - Criando o main - Página 94


[PAGINA 107]
                                                  Material do Treinamento Java e Orientação a Objetos




public Object getSaldo() {
    // TODO Auto-generated method stub
    return null;
}


   Implemente o método getSaldo como segue:

public double getSaldo() {
    return this.saldo;
}


    Esses pequenos recursos do Eclipse são de extrema utilidade. Dessa maneira, você pode programar sem
se preocupar com métodos que ainda não existem, já que a qualquer momento ele pode gerar o esqueleto (a
parte da assinatura do método).


 8.6 - Rodando o main
   Vamos rodar o método main dessa nossa classe. No Eclipse, clique com o botão direito no arquivo
Principal.java e vá em Run as... Java Application.




   O Eclipse abrirá uma View chamada Console onde será apresentada a saída do seu programa:




                                                            Capítulo 8 - Eclipse IDE - Rodando o main - Página 95


[PAGINA 108]
                                                      Material do Treinamento Java e Orientação a Objetos




   Quando você precisar rodar de novo, basta clicar no ícone verde de play na toolbar, que roda o programa
anterior. Ao lado desse ícone tem uma setinha onde são listados os 10 últimos executados.


 8.7 - Pequenos truques
   O Eclipse possui muitos atalhos úteis para o programador. Alguns bem interessantes de saber:

   • Ctrl + 1 Aciona o quick fixes com sugestões para correção de erros.

   • Ctrl + Espaço Completa códigos

   • Ctrl + 3 Aciona modo de descoberta de menu. Experimente digitar Ctrl+3 e depois digitar ggas e enter.
     Ou então de Ctr + 3 e digite new class.

   • Alt + Shift + X e depois J Roda o main da classe atual. Péssimo atalho! Mais fácil você digitar Control+3
     e depois digitar Run!. Abuse do Control+3

   • Ctrl + F11 roda a última classe que você rodou. É o mesmo que clicar no ícone verde que parece um
     botão de play na barra de ferramentas.

   • Ctrl + PgUp e Ctrl + PgDown Navega nas abas abertas. Útil quando estiver editando vários arquivos ao
     mesmo tempo.

   • Ctrl + Shift + F Formata o código segundo as convenções do Java

   • Ctrl + M Expande a View atual para a tela toda (mesmo efeito de dar dois cliques no título da View)

   • Ctrl + Shift + L Exibe todos os atalhos possíveis.

   • Ctrl + O Exibe um outline para rápida navegação

   Veremos mais no decorrer do curso, em especial quando virmos pacotes.


 8.8 - Exercícios: Eclipse

1) Dentro do projeto banco, crie as classes ContaCorrente e ContaPoupanca no nosso projeto do Eclipse. Na
   classe Conta, crie os métodos atualiza e saca como no capítulo anterior. Desta vez, tente abusar do control
   + espaço e control + 1.
   Por exemplo:
   ContaCorr<ControlEspaco> <ControlEspaco> = new <ControlEspaco>();

                                                               Capítulo 8 - Eclipse IDE - Pequenos truques - Página 96


[PAGINA 109]
                                                       Material do Treinamento Java e Orientação a Objetos




   Repare que até mesmo nomes de variáveis, ele cria para você! Acompanhe as dicas do instrutor.
   Muitas vezes nem declaramos a variável:

   new ContaCorrente();



   Vá nessa linha e de control +1. Ele vai sugerir e declarará a variável pra você.

2) Imagine que queremos criar um setter do saldo para a classe Conta. Dentro da classe Conta, digite:
   setSa<ControlEspaco>
   O mesmo vale no caso de você querer reescrever um método. Dentro de ContaCorrente faça:
   atua<ControlEspaco>

3) Vá na sua classe que tem o main e segure o CONTROL apertado enquando você passa o mouse sobre
   o seu código. Repare que tudo virou hyperlink. Clique em um método que você está invocando na classe
   Conta.

4) Dê um clique da direita em um arquivo no navigator. Escolha Compare With -> Local History. O que é esta
   tela?




5) Use o Control + Shift + F para formatar o seu código. Dessa maneira, ele vai arrumar a bagunça de espaça-
   mento e enters do seu código.




                                                                Capítulo 8 - Eclipse IDE - Exercícios: Eclipse - Página 97


[PAGINA 110]
                                                      Material do Treinamento Java e Orientação a Objetos




6) (opcional) Crie no seu projeto a classe AtualizadorDeContas como no capítulo anterior.

7) (opcional) O que são os arquivos .project e .classpath? Leia o conteúdo deles.

8) (opcional) Clique da direita no projeto, propriedades. É uma das telas mais importantes do Eclipse, onde
   você pode configurar diversas funcionalidades para o seu projeto, como compilador, versões, formatador,
   cvs e outros.




 8.9 - Discussão em aula: Refactoring
   O instrutor irá mostrar o que é uma refatoração e como usar esse poderoso recurso no Eclipse.




                                                    Capítulo 8 - Eclipse IDE - Discussão em aula: Refactoring - Página 98


[PAGINA 111]
                                                                                             C APÍTULO   9

Orientação a Objetos – Classes Abstratas
                                          “Dá-se importância aos antepassados quando já não temos nenhum.”
                                                                                    – François Chateaubriand


     Ao término desse capítulo, você será capaz de utilizar classes abstratas, quando necessário.


    9.1 - Repetindo mais código?
    Neste capítulo, aconselhamos que você passe a usar o Eclipse. Você já tem conhecimento suficiente dos
erros de compilação do javac e agora pode aprender as facilidades que o Eclipse te traz ao ajudar você no
código com os chamados quick fixes e quick assists.

     Vamos recordar em como pode estar nossa classe Funcionario:

class Funcionario {

      protected String nome;
      protected String cpf;
      protected double salario;

      public double getBonificacao() {
          return this.salario * 1.2;
      }

      // outros métodos aqui

}


     Considere, agora, o nosso ControleDeBonificacao:

class ControleDeBonificacoes {

     private double totalDeBonificacoes = 0;

        public void registra(Funcionario f) {
           System.out.println("Adicionando bonificacao do funcionario: " + f);
           this.totalDeBonificacoes += funcionario.getBonificacao();
        }

        public double getTotalDeBonificacoes() {
           return this.totalDeBonificacoes;
        }


                                                       99


[PAGINA 112]
                                                        Material do Treinamento Java e Orientação a Objetos




}


   Nosso método registra recebe qualquer referência do tipo Funcionario, isto é, podem ser objetos do tipo
Funcionario e qualquer de seus subtipos: Gerente, Diretor e, eventualmente, alguma nova subclasse que
venha ser escrita, sem prévio conhecimento do autor da ControleDeBonificacao.

    Estamos utilizando aqui a classe Funcionario para o polimorfismo. Se não fosse ela, teríamos um grande
prejuízo: precisaríamos criar um método registra para receber cada um dos tipos de Funcionario, um para
Gerente, um para Diretor, etc. Repare que perder esse poder é muito pior do que a pequena vantagem que a
herança traz em herdar código.

    Porém, em alguns sistemas, como é o nosso caso, usamos uma classe com apenas esses intuitos: de
economizar um pouco código e ganhar polimorfismo para criar métodos mais genéricos, que se encaixem a
diversos objetos.

    Faz sentido ter um objeto do tipo Funcionario? Essa pergunta é diferente de saber se faz sentido ter uma
referência do tipo Funcionario: nesse caso, faz sim e é muito útil.

    Referenciando Funcionario temos o polimorfismo de referência, já que podemos receber qualquer coisa que
seja um Funcionario. Porém, dar new em Funcionario pode não fazer sentido, isto é, não queremos receber
um objeto do tipo Funcionario, mas sim que aquela referência seja ou um Gerente, ou um Diretor, etc. Algo
mais concreto que um Funcionario.

ControleDeBonificacoes cdb = new ControleDeBonificacoes();
Funcionario f = new Funcionario();
cdb.adiciona(f); // faz sentido?


    Vejamos um outro caso em que não faz sentido ter um objeto daquele tipo, apesar da classe existir: imagine
a classe Pessoa e duas filhas, PessoaFisica e PessoaJuridica. Quando puxamos um relatório de nossos
clientes (uma array de Pessoa por exemplo), queremos que cada um deles seja ou uma PessoaFisica, ou uma
PessoaJuridica. A classe Pessoa, nesse caso, estaria sendo usada apenas para ganhar o polimorfismo e herdar
algumas coisas: não faz sentido permitir instanciá-la.

     Para resolver esses problemas, temos as classes abstratas.


    9.2 - Classe abstrata
   O que, exatamente, vem a ser a nossa classe Funcionario? Nossa empresa tem apenas Diretores,
Gerentes, Secretárias, etc. Ela é uma classe que apenas idealiza um tipo, define apenas um rascunho.

    Para o nosso sistema, é inadmissível que um objeto seja apenas do tipo Funcionario (pode existir um
sistema em que faça sentido ter objetos do tipo Funcionario ou apenas Pessoa, mas, no nosso caso, não).

   Usamos a palavra chave abstract para impedir que ela possa ser instanciada. Esse é o efeito direto de se
usar o modificador abstract na declaração de uma classe:

abstract class Funcionario {

      protected double salario;

      public double getBonificacao() {
          return this.salario * 1.2;

                                        Capítulo 9 - Orientação a Objetos – Classes Abstratas - Classe abstrata - Página 100


[PAGINA 113]
                                                      Material do Treinamento Java e Orientação a Objetos




    }

    // outros atributos e metodos comuns a todos Funcionarios

}


    E, no meio de um código:

Funcionario f = new Funcionario(); // não compila!!!




   O código acima não compila. O problema é instanciar a classe - criar referência, você pode. Se ela não
pode ser instanciada, para que serve? Somente para o polimorfismo e herança dos atributos e métodos.

    Vamos então herdar dessa classe, reescrevendo o método getBonificacao:

class Gerente extends Funcionario {

    public String getBonificacao() {
        return this.salario * 1.4 + 1000;
    }
}




   Mas qual é a real vantagem de uma classe abstrata? Poderíamos ter feito isto com uma herança comum.
Por enquanto, a única diferença é que não podemos instanciar um objeto do tipo Funcionario, que já é de
grande valia, dando mais consistência ao sistema.

    Fique claro que a nossa decisão de transformar Funcionario em uma classe abstrata dependeu do nosso
negócio. Pode ser que, em um sistema com classes similares, faça sentido uma classe análoga a Funcionario
ser concreta.



                                      Capítulo 9 - Orientação a Objetos – Classes Abstratas - Classe abstrata - Página 101


[PAGINA 114]
                                                         Material do Treinamento Java e Orientação a Objetos




    9.3 - Métodos abstratos
   Se o método getBonificacao não fosse reescrito, ele seria herdado da classe mãe, fazendo com que devol-
vesse o salário mais 20%.

    Levando em consideração que cada funcionário em nosso sistema tem uma regra totalmente diferente para
ser bonificado, faz algum sentido ter esse método na classe Funcionario? Será que existe uma bonificação
padrão para todo tipo de Funcionario? Parece que não, cada classe filha terá um método diferente de bonifica-
ção pois, de acordo com nosso sistema, não existe uma regra geral: queremos que cada pessoa que escreve
a classe de um Funcionario diferente (subclasses de Funcionario) reescreva o método getBonificacao de
acordo com as suas regras.

   Poderíamos, então, jogar fora esse método da classe Funcionario? O problema é que, se ele não existisse,
não poderíamos chamar o método apenas com uma referência a um Funcionario, pois ninguém garante que
essa referência aponta para um objeto que possui esse método.

   Existe um recurso em Java que, em uma classe abstrata, podemos escrever que determinado método será
sempre escrito pelas classes filhas. Isto é, um método abstrato.

   Ele indica que todas as classes filhas (concretas, isto é, que não forem abstratas) devem reescrever esse
método ou não compilarão. É como se você herdasse a responsabilidade de ter aquele método.


              Como declarar um método abstrato
            Às vezes, não fica claro como declarar um método abstrato.
            Basta escrever a palavra chave abstract na assinatura do mesmo e colocar um ponto e vírgula em
            vez de abre e fecha chaves!



abstract class Funcionario {

      abstract double getBonificacao();

      // outros atributos e metodos

}


   Repare que não colocamos o corpo do método e usamos a palavra chave abstract para definir o mesmo.
Por que não colocar corpo algum? Porque esse método nunca vai ser chamado, sempre que alguém chamar o
método getBonificacao, vai cair em uma das suas filhas, que realmente escreveram o método.

   Qualquer classe que estender a classe Funcionario será obrigada a reescrever este método, tornando-o
“concreto”. Se não reescreverem esse método, um erro de compilação ocorrerá.

     O método do ControleDeBonificacao estava assim:

public void registra(Funcionario f) {
        System.out.println("Adicionando bonificacao do funcionario: " + f);
        this.totalDeBonificacoes += funcionario.getBonificacao();
    }


     Como posso acessar o método getBonificacao se ele não existe na classe Funcionario?

                                      Capítulo 9 - Orientação a Objetos – Classes Abstratas - Métodos abstratos - Página 102


[PAGINA 115]
                                                        Material do Treinamento Java e Orientação a Objetos




    Já que o método é abstrato, com certeza suas subclasses têm esse método, o que garante que essa
invocação de método não vai falhar. Basta pensar que uma referência do tipo Funcionario nunca aponta para
um objeto que não tem o método getBonificacao, pois não é possível instanciar uma classe abstrata, apenas as
concretas. Um método abstrato obriga a classe em que ele se encontra ser abstrata, o que garante a coerência
do código acima compilar.


 9.4 - Aumentando o exemplo
   E agora se, no nosso exemplo de empresa, tivéssemos o seguinte diagrama de classes com os seguintes
métodos:




   Ou seja, tenho a classe abstrata Funcionario, com o método abstrato getBonificacao; as classes Gerente e
Presidente extendendo Funcionario e implementando o método getBonificacao; e, por fim, a classe Diretor,
que estende Gerente, mas não implementa o método getBonificacao.

   Essas classes vão compilar? Vão rodar?

   A resposta é sim. E, além de tudo, farão exatamente o que nós queremos, pois, quando Gerente e
Presidente possuem os métodos perfeitamente implementados, a classe Diretor, que não possui o método
implementado, vai usar a implementação herdada de Gerente.




   E esse diagrama, no qual incluímos uma classe abstrata Secretaria sem o método getBonificacao, que é

                                Capítulo 9 - Orientação a Objetos – Classes Abstratas - Aumentando o exemplo - Página 103


[PAGINA 116]
                                                         Material do Treinamento Java e Orientação a Objetos




estendida por mais duas classes (SecretariaAdministrativa, SecretariaAgencia) que, por sua vez, implemen-
tam o método getBonificacao, vai compilar? Vai rodar?

    De novo, a resposta é sim, pois Secretaria é uma classe abstrata e, por isso, o Java tem certeza de que
ninguém vai conseguir instanciá-la e, muito menos, chamar o método getBonificacao dela. Lembrando que,
nesse caso, não precisamos nem ao menos escrever o método abstrato getBonificacao na classe Secretaria.

   Se eu não reescrever um método abstrato da minha classe mãe, o código não compilará. Mas posso, em
vez disso, declarar a classe como abstrata!


              java.io
             Classes abstratas não possuem nenhum segredo no aprendizado, mas quem está aprendendo
             orientação a objetos pode ter uma enorme dificuldade para saber quando utilizá-las, o que é muito
             normal.
             Estudaremos o pacote java.io, que usa bastantes classes abstratas, sendo um exemplo real de uso
             desse recurso, que vai melhorar o entendimento delas. (classe InputStream e suas filhas)


 9.5 - Para saber mais...

   • Uma classe que estende uma classe normal também pode ser abstrata! Ela não poderá ser instanciada,
       mas sua classe pai sim!

   • Uma classe abstrata não precisa necessariamente ter um método abstrato.


 9.6 - Exercícios: Classes Abstratas

1) Repare que a nossa classe Conta é uma excelente candidata para uma classe abstrata. Por quê? Que
   métodos seriam interessantes candidatos a serem abstratos?
   Transforme a classe Conta em abstrata, repare o que acontece no seu main já existente do TestaContas.

   abstract class Conta {

        // ...
   }


2) Para que o código do main volte a compilar, troque o new Conta() por new ContaCorrente().
   Se agora não podemos dar new em Conta, qual é a utilidade de ter um método que recebe uma referência a
   Conta como argumento? Aliás, posso ter isso?

3) Apenas pare efeito de entender melhor o abstract, remova (delete) o método atualiza() da ContaPoupanca,
   dessa forma ele herdará o método diretamente de Conta.
   Transforme o método atualiza() da classe Conta em abstrato. Repare que, ao colocar a palavra chave
   abstract ao lado do método, o Eclipse rapidamente vai sugerir que você deve remover o corpo (body) do
   método com um quick fix:




                                      Capítulo 9 - Orientação a Objetos – Classes Abstratas - Para saber mais... - Página 104


[PAGINA 117]
                                                         Material do Treinamento Java e Orientação a Objetos




   Sua classe Conta deve ficar parecido com:

   abstract class Conta {


       // atributos e metodos que já existiam

       abstract void atualiza(double taxaSelic);
   }


   Qual é o problema com a classe ContaPoupanca?

4) Reescreva o método atualiza() na classe ContaPoupanca para que a classe possa compilar normalmente.
   O eclipse também sugere isso como um quick fix:




5) (opcional) Existe outra maneira de a classe ContaCorrente compilar se você não reescrever o método abs-
   trato?

6) (opcional) Pra que ter o método atualiza na classe Conta se ele não faz nada? O que acontece se simples-
   mente apagarmos esse método da classe Conta e deixarmos o método atualiza nas filhas?

7) (opcional) Posso chamar um método abstrato de dentro de um outro método da própria classe abstrata? Um
   exemplo: o mostra do Funcionario pode invocar this.getBonificacao()?


 9.7 - Desafios

1) Não podemos dar new em Conta, mas por que, então, podemos dar new em Conta[10], por exemplo?




                                               Capítulo 9 - Orientação a Objetos – Classes Abstratas - Desafios - Página 105


[PAGINA 118]
                                                                                          C APÍTULO   10

Orientação a Objetos - Interfaces
                                             “Uma imagem vale mil palavras. Uma interface vale mil imagens.”
                                                                                          – Ben Shneiderman


     Ao término desse capítulo, você será capaz de:

     • dizer o que é uma interface e as diferenças entre herança e implementação;

     • escrever uma interface em Java;

     • utilizá-las como um poderoso recurso para diminuir acoplamento entre as classes.


    10.1 - Aumentando nosso exemplo
   Imagine que um Sistema de Controle do Banco pode ser acessado, além de pelos Gerentes, pelos Diretores
do Banco. Então, teríamos uma classe Diretor:

class Diretor extends Funcionario {

      public boolean autentica(int senha) {
          // verifica aqui se a senha confere com a recebida como parametro
      }

}


     E a classe Gerente:

class Gerente extends Funcionario {

      public boolean autentica(int senha) {
          // verifica aqui se a senha confere com a recebida como parametro
          // no caso do gerente verifica tambem se o departamente dele
          // tem acesso
      }

}




                                                      106


[PAGINA 119]
                                                      Material do Treinamento Java e Orientação a Objetos




   Repare que o método de autenticação de cada tipo de Funcionario pode variar muito. Mas vamos aos
problemas. Considere o SistemaInterno e seu controle: precisamos receber um Diretor ou Gerente como
argumento, verificar se ele se autentica e colocá-lo dentro do sistema.

class SistemaInterno {

    void login(Funcionario funcionario) {
        // chamar o método autentica? não da! Nem todo Funcionario tem
    }
}


    O SistemaInterno aceita qualquer tipo de Funcionario, tendo ele acesso ao sistema ou não, mas note
que nem todo Funcionario possui o método autentica. Isso nos impede de chamar esse método com uma
referência apenas a Funcionario (haveria um erro de compilação). O que fazer então?

class SistemaInterno {

    void login(Funcionario funcionario) {
        funcionario.autentica(); // não compila
    }
}


   Uma possibilidade é criar dois métodos login no SistemaInterno: um para receber Diretor e outro para
receber Gerente. Já vimos que essa não é uma boa escolha. Por quê?

class SistemaInterno {

    // design problemático
    void login(Diretor funcionario) {
        funcionario.autentica();
    }

    // design problemático
    void login(Gerente funcionario) {
        funcionario.autentica();
    }



                                 Capítulo 10 - Orientação a Objetos - Interfaces - Aumentando nosso exemplo - Página 107


[PAGINA 120]
                                                      Material do Treinamento Java e Orientação a Objetos




}


   Cada vez que criarmos uma nova classe de Funcionario que é autenticável, precisaríamos adicionar um
novo método de login no SistemaInterno.


            Métodos com mesmo nome
           Em Java, métodos podem ter o mesmo nome desde que não sejam ambíguos, isto é, que exista
           uma maneira de distinguir no momento da chamada.
           Isso se chama sobrecarga de método. (Overloading. Não confundir com overriding, que é um
           conceito muito mais poderoso).


   Uma solução mais interessante        seria criar uma classe no meio da árvores de herança,
FuncionarioAutenticavel:


class FuncionarioAutenticavel extends Funcionario {

    public boolean autentica(int senha) {
        // faz autenticacao padrao
    }

    // outros atributos e metodos

}


   As classes Diretor e Gerente passariam a estender de FuncionarioAutenticavel, e o SistemaInterno
receberia referências desse tipo, como a seguir:

class SistemaInterno {

    void login(FuncionarioAutenticavel fa) {

        int senha = //pega senha de um lugar, ou de um scanner de polegar

        // aqui eu posso chamar o autentica!
        // Pois todo FuncionarioAutenticavel tem
        boolean ok = fa.autentica(senha);

    }
}




                                 Capítulo 10 - Orientação a Objetos - Interfaces - Aumentando nosso exemplo - Página 108


[PAGINA 121]
                                                       Material do Treinamento Java e Orientação a Objetos




   Repare que FuncionarioAutenticavel é uma forte candidata a classe abstrata. Mais ainda, o método
autentica poderia ser um método abstrato.

   O uso de herança resolve esse caso, mas vamos a uma outra situação um pouco mais complexa: precisa-
mos que todos os clientes também tenham acesso ao SistemaInterno. O que fazer? Uma opção é criar outro
método login em SistemaInterno: mas já descartamos essa anteriormente.

    Uma outra, que é comum entre os novatos, é fazer uma herança sem sentido para resolver o problema,
por exemplo, fazer Cliente extends FuncionarioAutenticavel. Realmente, resolve o problema, mas trará
diversos outros. Cliente definitivamente não é FuncionarioAutenticavel. Se você fizer isso, o Cliente terá,
por exemplo, um método getBonificacao, um atributo salario e outros membros que não fazem o menor sentido
para esta classe! Não faça herança quando a relação não é estritamente “é um”.




   Como resolver essa situação? Note que conhecer a sintaxe da linguagem não é o suficiente, precisamos

                                  Capítulo 10 - Orientação a Objetos - Interfaces - Aumentando nosso exemplo - Página 109


[PAGINA 122]
                                                        Material do Treinamento Java e Orientação a Objetos




estruturar/desenhar bem a nossa estrutura de classes.


    10.2 - Interfaces
    O que precisamos para resolver nosso problema? Arranjar uma forma de poder referenciar Diretor, Gerente
e Cliente de uma mesma maneira, isto é, achar um fator comum.

   Se existisse uma forma na qual essas classes garantissem a existência de um determinado método, através
de um contrato, resolveríamos o problema.

     Toda classe define 2 itens:

     • o que uma classe faz (as assinaturas dos métodos)

     • como uma classe faz essas tarefas (o corpo dos métodos e atributos privados)

    Podemos criar um “contrato” que define tudo o que uma classe deve fazer se quiser ter um determinado
status. Imagine:


contrato Autenticavel:

          quem quiser ser Autenticavel precisa saber fazer:
              1.autenticar dada uma senha, devolvendo um booleano


   Quem quiser, pode “assinar” esse contrato, sendo assim obrigado a explicar como será feita essa autentica-
ção. A vantagem é que, se um Gerente assinar esse contrato, podemos nos referenciar a um Gerente como um
Autenticavel.

     Podemos criar esse contrato em Java!

interface Autenticavel {

      boolean autentica(int senha);

}


  Chama-se interface pois é a maneira pela qual poderemos conversar com um Autenticavel. Interface é a
maneira através da qual conversamos com um objeto.

    Lemos a interface da seguinte maneira: “quem desejar ser autenticável precisa saber autenticar dado um
inteiro e retornando um booleano”. Ela é um contrato onde quem assina se responsabiliza por implementar
esses métodos (cumprir o contrato).

   Uma interface pode definir uma série de métodos, mas nunca conter implementação deles. Ela só expõe
o que o objeto deve fazer, e não como ele faz, nem o que ele tem. Como ele faz vai ser definido em uma
implementação dessa interface.

   E o Gerente pode “assinar” o contrato, ou seja, implementar a interface. No momento em que ele imple-
menta essa interface, ele precisa escrever os métodos pedidos pela interface (muito parecido com o efeito de
herdar métodos abstratos, aliás, métodos de uma interface são públicos e abstratos, sempre). Para implementar
usamos a palavra chave implements na classe:

                                                   Capítulo 10 - Orientação a Objetos - Interfaces - Interfaces - Página 110


[PAGINA 123]
                                                    Material do Treinamento Java e Orientação a Objetos




class Gerente extends Funcionario implements Autenticavel {

    private int senha;

    // outros atributos e métodos

    public boolean autentica(int senha) {
        if(this.senha != senha) {
            return false;
        }
        // pode fazer outras possiveis verificacoes, como saber se esse
        // departamento do gerente tem acesso ao Sistema

         return true;
    }

}




   O implements pode ser lido da seguinte maneira: “A classe Gerente se compromete a ser tratada como
Autenticavel, sendo obrigada a ter os métodos necessários, definidos neste contrato”.

    A partir de agora, podemos tratar um Gerente como sendo um Autenticavel. Ganhamos mais polimor-
fismo! Temos mais uma forma de referenciar a um Gerente. Quando crio uma variável do tipo Autenticavel,
estou criando uma referência para qualquer objeto de uma classe que implemente Autenticavel, direta ou
indiretamente:

Autenticavel a = new Gerente();
// posso aqui chamar o metodo autentica!


    Novamente, a utilização mais comum, aqui, seria receber como argumento.

    Voltamos ao nosso SistemaInterno:

class SistemaInterno {
  void login(Autenticavel a) {
     int senha = //pega senha de um lugar, ou de um scanner de polegar
     boolean ok =    a.autentica(senha);
     // aqui eu posso chamar o autentica!

                                                Capítulo 10 - Orientação a Objetos - Interfaces - Interfaces - Página 111


[PAGINA 124]
                                                     Material do Treinamento Java e Orientação a Objetos




        // não necessariamente é um Funcionario! Mais ainda, eu não sei
        // que objeto a referência "a" está apontando exatamente! Flexibilidade.
    }
}


   Pronto! E já podemos passar qualquer Autenticavel para o SistemaInterno. Então precisamos fazer com
que o Diretor também implemente essa interface.

class Diretor extends Funcionario implements Autenticavel {

        // metodos e atributos, alem de obrigatoriamente ter o autentica

}




   Agora, podemos passar um Diretor. No dia em que tivermos mais um funcionário com acesso ao sistema,
basta que ele implemente essa interface, para se encaixar no sistema.

    Qualquer Autenticavel passado para o SistemaInterno está bom para nós. Repare que pouco importa
quem o objeto referenciado realmente é, pois ele tem um método autentica que é o necessário para nosso
SistemaInterno funcionar corretamente. Aliás, qualquer outra classe que futuramente implemente essa inter-
face poderá ser passada como argumento aqui.

Autenticavel diretor = new Diretor();
Autenticavel gerente = new Gerente();


    Ou, se agora achamos que o Fornecedor precisa ter acesso: basta que ele implemente Autenticavel. Olhe
só o tamanho do desacoplamento: quem escreveu o SistemaInterno só precisa saber que ele é Autenticavel.

class SistemaInterno {
  void login(Autenticavel a) {
    // não importa se ele é um gerente ou diretor
    // será que é um fornecedor?
    // Eu, o programador do SistemaInterno, não me preocupo
    // Invocarei o método autentica


                                                 Capítulo 10 - Orientação a Objetos - Interfaces - Interfaces - Página 112


[PAGINA 125]
                                                            Material do Treinamento Java e Orientação a Objetos




    }
}


   Não faz diferença se é um Diretor, Gerente, Cliente ou qualquer classe que venha por aí. Basta seguir o
contrato! Mais ainda, cada Autenticavel pode se autenticar de uma maneira completamente diferente de outro.

    Lembre-se: a interface define que todos vão saber se autenticar (o que ele faz), enquanto a implementação
define como exatamente vai ser feito (como ele faz).

    A maneira como os objetos se comunicam num sistema orientado a objetos é muito mais importante do que
como eles executam. O que um objeto faz é mais importante do que como ele faz. Aqueles que seguem
essa regra, terão sistemas mais fáceis de manter e modificar. Como você já percebeu, esta é uma das idéias
principais que queremos passar e, provavelmente, a mais importante de todo esse curso.


             Herança entre interfaces
            Diferentemente das classes, uma interface pode herdar de mais de uma interface. É como um
            contrato que depende que outros contratos sejam fechados antes deste valer. Você não herda
            métodos e atributos, mas sim responsabilidades.


    10.3 - Dificuldade no aprendizado de interfaces
   Interfaces representam uma barreira no aprendizado do Java: parece que estamos escrevendo um código
que não serve pra nada, já que teremos essa linha (a assinatura do método) escrita nas nossas classes imple-
mentadoras. Essa é uma maneira errada de se pensar. O objetivo do uso de uma interface é deixar seu código
mais flexível e possibilitar a mudança de implementação sem maiores traumas. Não é apenas um código de
prototipação, um cabeçalho!

   Os mais radicais dizem que toda classe deve ser “interfaceada”, isto é, só devemos nos referir a objetos atra-
vés de suas interfaces. Se determinada classe não tem uma interface, ela deveria ter. Os autores deste material
acham tal medida radical demais, porém o uso de interfaces em vez de herança é amplamente aconselhado.
Você pode encontrar mais informações sobre o assunto nos livros Design Patterns, Refactoring e Effective Java.

   No livro Design Patterns, logo no início, os autores citam 2 regras “de ouro”. Uma é “evite herança, prefira
composição” e a outra, “programe voltado a interface e não à implementação”.

    Veremos o uso de interfaces no capítulo de coleções, o que melhora o entendimento do assunto. O exemplo
da interface Comparable também é muito esclarecedor, onde enxergamos o reaproveitamento de código através
das interfaces, além do encapsulamento. Para o método Collections.sort(), pouco importa quem vai ser
passado como argumento. Para ele, basta que a coleção sejam de objetos comparáveis. Ele pode ordenar
Elefante, Conexao ou ContaCorrente, desde que implementem Comparable.


    10.4 - Exemplo interessante: conexões com o banco de dados
   Como fazer com que todas as chamadas para bancos de dados diferentes respeitem a mesma regra?
Usando interfaces!

   Imagine uma interface Conexao contendo todos os métodos necessários para a comunicação e troca de
dados com um banco de dados. Cada banco de dados fica encarregado de criar a sua implementação para
essa interface.



                          Capítulo 10 - Orientação a Objetos - Interfaces - Dificuldade no aprendizado de interfaces - Página 113


[PAGINA 126]
                                                        Material do Treinamento Java e Orientação a Objetos




    Quem for usar uma Conexao não precisa se importar com qual objeto exatamente está trabalhando, já que
ele vai cumprir o papel que toda Conexao deve ter. Não importa se é uma conexão com um Oracle ou MySql.




   Apesar do java.sql.Connection não trabalhar bem assim, a idéia é muito similar, porém as conexões vêm
de uma factory chamada DriverManager.

   Conexão a banco de dados está fora do escopo desse treinamento, mas é um dos primeiros tópicos abor-
dados no curso FJ-21, juntamente com DAO.


 10.5 - Um pouco mais...

1) Posso substituir toda minha herança por interfaces? Qual é a vantagem e a desvantagem?

2) Uma interface também pode declarar constantes (não atributos de objeto). Qual é a utilidade?


 10.6 - Exercícios: Interfaces

1) A sintaxe do uso de interfaces pode parecer muito estranha, à primeira vista.
   Vamos começar com um exercício para praticar a sintaxe. Crie um projeto interfaces e crie a interface
   AreaCalculavel:

   interface AreaCalculavel {

       double calculaArea();
   }

   Queremos, agora, criar algumas classes que são AreaCalculavel:

   class Quadrado implements AreaCalculavel {

       private int lado;

       public Quadrado(int lado) {
           this.lado = lado;


                                             Capítulo 10 - Orientação a Objetos - Interfaces - Um pouco mais... - Página 114


[PAGINA 127]
                                                         Material do Treinamento Java e Orientação a Objetos




       }

       public double calculaArea() {
           return this.lado * this.lado;
       }
   }


   class Retangulo implements AreaCalculavel {
       private int largura;
       private int altura;

       public Retangulo(int largura, int altura) {
           this.largura = largura;
           this.altura = altura;
       }

       public double calculaArea() {
           return this.largura * this.altura;
       }
   }

   Repare que, aqui, se você tivesse usado herança, não ia ganhar muita coisa, já que cada implementação
   é totalmente diferente da outra: um Quadrado, um Retangulo e um Circulo têm atributos e métodos bem
   diferentes.
   Mas, mesmo que eles tivessem atributos em comum, utilizar interfaces é uma maneira muito mais elegante
   de modelar suas classes. Elas também trazem vantagens em não acoplar as classes. Uma vez que herança
   através de classes traz muito acoplamento, muitos autores renomados dizem que, na maioria dos casos,
   herança quebra o encapsulamento, pensamento com o qual a equipe da Caelum concorda plenamente.
   Crie a seguinte classe de Teste. Repare no polimorfismo. Poderíamos estar passando esses objetos como
   argumento para alguém que aceitasse AreaCalculavel como argumento:

   class Teste {

       public static void main(String[] args) {
           AreaCalculavel a = new Retangulo(3,2);
           System.out.println(a.calculaArea());
       }
   }

   Opcionamente, crie a classe Circulo:

   class Circulo implements AreaCalculavel {

       // ... atributos (raio) e métodos (calculaArea)
   }

   Utilize Math.PI * raio * raio para calcular a área.
2) Nosso banco precisa tributar dinheiro de alguns bens que nossos clientes possuem. Para isso, vamos criar
   uma interface no nosso projeto já existente:

   interface Tributavel {

       double calculaTributos();

                                          Capítulo 10 - Orientação a Objetos - Interfaces - Exercícios: Interfaces - Página 115


[PAGINA 128]
                                                     Material do Treinamento Java e Orientação a Objetos




}


Lemos essa interface da seguinte maneira: “todos que quiserem ser tributável precisam saber calcular tribu-
tos, devolvendo um double”.
Alguns bens são tributáveis e outros não, ContaPoupanca não é tributável, já para ContaCorrente você precisa
pagar 1% da conta e o SeguroDeVida tem uma taxa fixa de 42 reais.
Aproveite o Eclipse! Quando você escrever implements Tributavel na classe ContaCorrente, o quick fix do
eclipse vai sugerir que você reescreva o método, escolha essa opção e depois preencha o corpo do método
adequadamente:

class ContaCorrente extends Conta implements Tributavel {


    // outros atributos e metodos

    public double calculaTributos() {
        return this.saldo * 0.01;
    }
}

E crie a classe SeguroDeVida, aproveitando novamente do Eclipse, para obter:

class SeguroDeVida implements Tributavel {

    public double calculaTributos() {
        return 42;
    }
}




Vamos criar uma classe TestaTributavel com um método main para testar o nosso exemplo:

class TestaTributavel {


    public static void main(String[] args) {
        ContaCorrente cc = new ContaCorrente();
        cc.deposita(100);
        System.out.println(cc.calculaTributos());

         // testando polimorfismo:


                                      Capítulo 10 - Orientação a Objetos - Interfaces - Exercícios: Interfaces - Página 116


[PAGINA 129]
                                                      Material do Treinamento Java e Orientação a Objetos




           Tributavel t = cc;
           System.out.println(t.calculaTributos());
       }
  }


  Tente, agora, chamar o método getSaldo através da referência t, o que ocorre? Por quê?
  A linha em que atribuímos cc a um Tributavel é apenas para você enxergar que é possível fazê-lo. Nesse
  nosso caso, isso não tem uma utilidade. Essa possibilidade será útil para o próximo exercício.

3) (opcional) Crie um GerenciadorDeImpostoDeRenda, que recebe todos os tributáveis de uma pessoa e soma
   seus valores, e inclua nele um método para devolver seu total:

   class GerenciadorDeImpostoDeRenda {

       private double total;

       void adiciona(Tributavel t) {
           System.out.println("Adicionando tributavel: " + t);

           this.total +=   t.calculaTributos();
       }

       public double getTotal() {
           return this.total;
       }
  }

  Crie um main para instanciar diversas classes que implementam Tributavel e passar como argumento para
  um GerenciadorDeImpostoDeRenda. Repare que você não pode passar qualquer tipo de conta para o método
  adiciona, apenas a que implementa Tributavel. Além disso, pode passar o SeguroDeVida.

   public class TestaGerenciadorDeImpostoDeRenda {

       public static void main(String[] args) {

           GerenciadorDeImpostoDeRenda gerenciador = new GerenciadorDeImpostoDeRenda();

           SeguroDeVida sv = new SeguroDeVida();
           gerenciador.adiciona(sv);

           ContaCorrente cc = new ContaCorrente();
           cc.deposita(1000);
           gerenciador.adiciona(cc);

           System.out.println(gerenciador.getTotal());
       }
  }


  Repare que, de dentro do GerenciadorDeImpostoDeRenda, você não pode acessar o método getSaldo, por
  exemplo, pois você não tem a garantia de que o Tributavel que vai ser passado como argumento tem
  esse método. A única certeza que você tem é de que esse objeto tem os métodos declarados na interface
  Tributavel.
  É interessante enxergar que as interfaces (como aqui, no caso, Tributavel) costumam ligar classes muito
  distintas, unindo-as por uma característica que elas tem em comum. No nosso exemplo, SeguroDeVida e

                                       Capítulo 10 - Orientação a Objetos - Interfaces - Exercícios: Interfaces - Página 117


[PAGINA 130]
                                                          Material do Treinamento Java e Orientação a Objetos




   ContaCorrente são entidades completamente distintas, porém ambas possuem a característica de serem
   tributáveis.
   Se amanhã o governo começar a tributar até mesmo PlanoDeCapitalizacao, basta que essa classe
   implemente a interface Tributavel!       Repare no grau de desacoplamento que temos: a classe
   GerenciadorDeImpostoDeRenda nem imagina que vai trabalhar como PlanoDeCapitalizacao. Para ela, a
   única coisa que importa é que o objeto respeite o contrato de um tributável, isso é, a interface Tributavel.
   Novamente: programe voltado a interface, não a implementação.
4) (opcional) Use o método printf para imprimir o saldo com exatamente duas casas decimais:

   System.out.printf("O saldo é: %.2f", conta.getSaldo());




 10.7 - Exercícios avançados opcionais
   Atenção: caso você faça esse exercício, faça isso num projeto à parte conta-interface pois usaremos a
Conta como classe em exercícios futuros.

1) (Opcional) Transforme a classe Conta em uma interface.

   interface Conta {

       double getSaldo();
       void deposita(double valor);
       void retira(double valor);
       void atualiza(double taxaSelic);
   }

   Adapte ContaCorrente e ContaPoupanca para essa modificação:

   class ContaCorrente implements Conta {

       // ...
   }


   class ContaPoupanca implements Conta {
       // ...
   }

   Algum código vai ter de ser copiado e colado? Isso é tão ruim?

2) (Opcional) Subinterfaces:
   Às vezes, é interessante criarmos uma interface que herda de outras interfaces.

   interface ContaTributavel extends Conta, Tributavel {

   }

   Dessa maneira, quem for implementar essa nova interface precisa implementar todos os métodos herdados
   das suas superinterfaces (e talvez ainda novos métodos declarados dentro dela):

   class ContaCorrente implements ContaTributavel {

                                 Capítulo 10 - Orientação a Objetos - Interfaces - Exercícios avançados opcionais - Página 118


[PAGINA 131]
                                                                Material do Treinamento Java e Orientação a Objetos




       // metodos
   }

   Conta c = new ContaCorrente();
   Tributavel t = new ContaCorrente();


   Repare que o código pode parecer estranho, pois a interface não declara método algum, só herda os métodos
   abstratos declarados nas outras interfaces.
   Ao mesmo tempo que uma interface pode herdar de mais de uma outra interface, classes só podem possuir
   uma classe mãe (herança simples).


 10.8 - Discussão em aula: Favorecer composição em relação à herança
   Discuta com o instrutor e seus colegas, alternativas à herança. Falaremos de herança versus composição e
porque herança é muitas vezes considerada maléfica.

    Numa entrevista, James Gosling, “pai do java”, fala sobre uma linguagem puramente de delegação e chega
a dizer:.

     Rather than subclassing, just use pure interfaces. It’s not so much that class inheritance is particularly bad.
It just has problems. - James Gosling, na mesma entrevista.

   http://www.artima.com/intv/gosling3P.html
   No blog da Caelum há tambem um post sobre o assunto: http://blog.caelum.com.br/2006/10/14/
como-nao-aprender-orientacao-a-objetos-heranca/




       Capítulo 10 - Orientação a Objetos - Interfaces - Discussão em aula: Favorecer composição em relação à herança - Página 119


[PAGINA 132]
                                                                                           C APÍTULO   11

Controlando os erros com Exceções
                                                                             “Quem pensa pouco, erra muito”
                                                                                         – Leonardo da Vinci


   Ao término desse capítulo, você será capaz de:

   • controlar erros e tomar decisões baseadas nos mesmos;

   • criar novos tipos de erros para melhorar o tratamento deles em sua aplicação ou biblioteca;

   • assegurar que um método funcionou como diz em seu “contrato”.


 11.1 - Motivação
    Voltando às Contas que criamos no capítulo 6, o que aconteceria ao tentar chamar o método saca com um
valor fora do limite? O sistema mostraria uma mensagem de erro, mas quem chamou o método saca não saberá
que isso aconteceu.

   Como avisar aquele que chamou o método de que ele não conseguiu fazer aquilo que deveria?

    Em Java, os métodos dizem qual o contrato que eles devem seguir. Se, ao tentar sacar, ele não consegue
fazer o que deveria, ele precisa, ao menos, avisar ao usuário de que o saque não foi feito.

    Veja no exemplo abaixo: estamos forçando uma Conta a ter um valor negativo, isto é, estar num estado
inconsistente de acordo com a nossa modelagem.

Conta minhaConta = new Conta();
minhaConta.deposita(100);
minhaConta.setLimite(100);
minhaConta.saca(1000);
//     o saldo é -900? É 100? É 0? A chamada ao método saca funcionou?


   Em sistemas de verdade, é muito comum que quem saiba tratar o erro é aquele que chamou o método e
não a própria classe! Portanto, nada mais natural do que a classe sinalizar que um erro ocorreu.

    A solução mais simples utilizada antigamente é a de marcar o retorno de um método como boolean e
retornar true, se tudo ocorreu da maneira planejada, ou false, caso contrário:

boolean saca(double quantidade) {
  if (quantidade > this.saldo + this.limite) { //posso sacar até            saldo+limite
        System.out.println("Não posso sacar fora do limite!");
        return false;


                                                    120


[PAGINA 133]
                                                     Material do Treinamento Java e Orientação a Objetos




    } else {
        this.saldo = this.saldo – quantidade;
        return true;
    }
}


    Um novo exemplo de chamada ao método acima:

Conta minhaConta = new Conta();
minhaConta.deposita(100);
minhaConta.setLimite(100);
if (!minhaConta.saca(1000)) {
    System.out.println("Não saquei");
}


   Repare que tivemos de lembrar de testar o retorno do método, mas não somos obrigados a fazer isso.
Esquecer de testar o retorno desse método teria consequências drásticas: a máquina de auto atendimento
poderia vir a liberar a quantia desejada de dinheiro, mesmo que o sistema não tivesse conseguido efetuar o
método saca com sucesso, como no exemplo a seguir:

Conta minhaConta = new Conta();
minhaConta.deposita(100);

// ...
double valor = 5000;
minhaConta.saca(valor); // vai retornar false, mas ninguem verifica!
caixaEletronico.emite(valor);


    Mesmo invocando o método e tratando o retorno de maneira correta, o que faríamos se fosse necessário
sinalizar quando o usuário passou um valor negativo como quantidade? Uma solução seria alterar o retorno
de boolean para int e retornar o código do erro que ocorreu. Isso é considerado uma má prática (conhecida
também como uso de “magic numbers”).

   Além de você perder o retorno do método, o valor retornado é “mágico” e só legível perante extensa docu-
mentação, além de não obrigar o programador a tratar esse retorno e, no caso de esquecer isso, seu programa
continuará rodando já num estado inconsistente.

    Repare o que aconteceria se fosse necessário retornar um outro valor. O exemplo abaixo mostra um caso
onde, através do retorno, não será possível descobrir se ocorreu um erro ou não, pois o método retorna um
cliente.

public Cliente procuraCliente(int id) {
    if (idInvalido) {
        // avisa o método que chamou este que ocorreu um erro
    } else {
        Cliente cliente = new Cliente();
        cliente.setId(id);
        // cliente.setNome(......);
        return cliente;
    }
}


                                              Capítulo 11 - Controlando os erros com Exceções - Motivação - Página 121


[PAGINA 134]
                                                           Material do Treinamento Java e Orientação a Objetos




   Por esses e outros motivos, utilizamos um código diferente em Java para tratar aquilo que chamamos de
exceções: os casos onde acontece algo que, normalmente, não iria acontecer. O exemplo do argumento do
saque inválido ou do id inválido de um cliente é uma exceção à regra.


             Exceção
            Uma exceção representa uma situação que normalmente não ocorre e representa algo de estranho
            ou inesperado no sistema.


 11.2 - Exercício para começar com os conceitos

1) Para aprendermos os conceitos básicos das exceptions do Java, teste o seguinte código você mesmo:

   class TesteErro {

       public static void main(String[] args) {
           System.out.println("inicio do main");
           metodo1();
           System.out.println("fim do main");
       }

       static void metodo1() {
           System.out.println("inicio do metodo1");
           metodo2();
           System.out.println("fim do metodo1");
       }

       static void metodo2() {
           System.out.println("inicio do metodo2");
           int[] array = new int[10];
           for (int i = 0; i <= 15; i++) {
               array[i] = i;
               System.out.println(i);
           }
           System.out.println("fim do metodo2");
       }
   }


   Repare o método main chamando metodo1 e esse, por sua vez, chamando o metodo2. Cada um desses
   métodos pode ter suas próprias variáveis locais, sendo que, por exemplo, o metodo1 não enxerga as variáveis
   declaradas dentro do main.
   Como o Java (e muitas das outras linguagens) faz isso? Toda invocação de método é empilhada... em uma
   estrutura de dados que isola a área de memória de cada um. Quando um método termina (retorna), ele volta
   para o método que o invocou. Ele descobre isso através da pilha de execução (stack). Basta jogar fora um
   gomo da pilha (stackframe):




                       Capítulo 11 - Controlando os erros com Exceções - Exercício para começar com os conceitos - Página 122


[PAGINA 135]
                                                       Material do Treinamento Java e Orientação a Objetos




Porém, o nosso metodo2 propositalmente possui um enorme problema: está acessando um índice de array
indevido para esse caso; o índice estará fora dos limites da array quando chegar em 10!
Rode o código. Qual é a saída? O que isso representa? O que ela indica?




Essa é o conhecido rastro da pilha (stacktrace). É uma saída importantíssima para o programador - tanto
que, em qualquer fórum ou lista de discussão, é comum os programadores enviarem, juntamente com a
descrição do problema, essa stacktrace.
Por que isso aconteceu? O sistema de exceções do Java funciona da seguinte maneira: quando uma
exceção é lançada (throws) a JVM entra em estado de alerta e vai ver se o método atual toma alguma
precaução ao tentar executar esse trecho de código. Como podemos ver, o metodo2 não toma nenhuma
medida diferente do que vimos até agora.
Como o metodo2 não está tratando esse problema, a JVM pára a execução dele anormalmente, sem esperar
ele terminar, e volta um stackframe pra baixo, onde será feita nova verificação: o metodo1 está se precavendo
de um problema chamado ArrayIndexOutOfBoundsException? Não... volta para o main, onde também não
há proteção, então a JVM morre (na verdade, quem morre é apenas a Thread corrente, veremos mais para
frente).



                   Capítulo 11 - Controlando os erros com Exceções - Exercício para começar com os conceitos - Página 123


[PAGINA 136]
                                                         Material do Treinamento Java e Orientação a Objetos




  Obviamente, aqui estamos forçando o erro, e não faria sentido tomarmos cuidado com ele. Seria fácil arrumar
  um problema desses. Basta navegarmos na array no máximo até o seu length.
  Porém, apenas para entender o controle de fluxo de uma Exception, vamos colocar o código que vai tentar
  (try ) executar o bloco perigoso e, caso o problema seja do tipo ArrayIndexOutOfBoundsException, ele será
  pego (catched). Repare que é interessante que cada exceção no Java tenha um tipo... ela pode ter atributos
  e métodos.

2) Adicione um try/catch em volta do for, pegando ArrayIndexOutOfBoundsException. O que o código
   imprime agora?

   try {

      for (int i = 0; i <= 15; i++) {
          array[i] = i;
          System.out.println(i);
      }
  } catch (ArrayIndexOutOfBoundsException e) {
      System.out.println("erro: " + e);
  }




  Em vez de fazer o try em torno do for inteiro, tente apenas com o bloco de dentro do for:

   for (int i = 0; i <= 15; i++) {

      try {
          array[i] = i;
          System.out.println(i);
      } catch (ArrayIndexOutOfBoundsException e) {
          System.out.println("erro: " + e);
      }
  }


  Qual é a diferença?



                     Capítulo 11 - Controlando os erros com Exceções - Exercício para começar com os conceitos - Página 124


[PAGINA 137]
                                                      Material do Treinamento Java e Orientação a Objetos




Agora retire o try/catch e coloque ele em volta da chamada do metodo2.

System.out.println("inicio do metodo1");

try {
    metodo2();
} catch (ArrayIndexOutOfBoundsException e) {
    System.out.println("erro: " + e);
}
System.out.println("fim do metodo1");




                  Capítulo 11 - Controlando os erros com Exceções - Exercício para começar com os conceitos - Página 125


[PAGINA 138]
                                                          Material do Treinamento Java e Orientação a Objetos




     Faça a mesma coisa, retirando o try/catch novamente e colocando em volta da chamada do metodo1. Rode
     os códigos, o que acontece?

     System.out.println("inicio do main");

     try {
         metodo1();
     } catch (ArrayIndexOutOfBoundsException e) {
         System.out.println("Erro : "+e);
     }
     System.out.println("fim do main");




     Repare que, a partir do momento que uma exception foi catched (pega, tratada, handled), a execução volta
     ao normal a partir daquele ponto.


    11.3 - Exceções de Runtime mais comuns
   Que tal tentar dividir um número por zero? Será que o computador consegue fazer aquilo que nós definimos
que não existe?

public class TestandoADivisao {

      public static void main(String args[]) {
          int i = 5571;
          i = i / 0;
          System.out.println("O resultado " + i);
      }
}


     Tente executar o programa acima. O que acontece?




                            Capítulo 11 - Controlando os erros com Exceções - Exceções de Runtime mais comuns - Página 126


[PAGINA 139]
                                                            Material do Treinamento Java e Orientação a Objetos




public class TestandoReferenciaNula {
    public static void main(String args[]) {
        Conta c = null;
        System.out.println("Saldo atual " + c.getSaldo());
    }
}


   Agora, tente executar este programa. O que acontece?




   Repare que um ArrayIndexOutOfBoundsException ou um NullPointerException poderia ser facilmente evi-
tado com o for corretamente escrito ou com ifs que checariam os limites da array.

    Outro caso em que também ocorre tal tipo de exceção é quando um cast errado é feito (veremos mais
pra frente). Em todos os casos, tais erros provavelmente poderiam ser evitados pelo programador. É por esse
motivo que o java não te obriga a dar o try/catch nessas exceptions e chamamos essas exceções de unchecked.
Em outras palavras, o compilador não checa se você está tratando essas exceções.


             Erros
            Os erros em Java são um tipo de exceção que também pode ser tratado. Eles representam pro-
            blemas na máquina virtual e não devem ser tratados em 99% dos casos, já que provavelmente o
            melhor a se fazer é deixar a JVM encerrar (ou apenas a Thread em questão).


 11.4 - Outro tipo de exceção: Checked Exceptions
    Fica claro, com os exemplos de código acima, que não é necessário declarar que você está tentando fazer
algo onde um erro possa ocorrer. Os dois exemplos, com ou sem o try/catch, compilaram e rodaram. Em um,
o erro terminou o programa e, no outro, foi possível tratá-lo.

    Mas não é só esse tipo de exceção que existe em Java. Um outro tipo, obriga a quem chama o método ou
construtor a tratar essa exceção. Chamamos esse tipo de exceção de checked, pois o compilador checará se
ela está sendo devidamente tratada.

   Um exemplo que podemos mostrar agora, é o de abrir um arquivo para leitura, onde pode ocorrer o erro do
arquivo não existir (veremos como trabalhar com arquivos em outro capítulo, não se preocupe com isto agora):

class Teste {
    public static void metodo() {

                     Capítulo 11 - Controlando os erros com Exceções - Outro tipo de exceção: Checked Exceptions - Página 127


[PAGINA 140]
                                                            Material do Treinamento Java e Orientação a Objetos




         new java.io.FileInputStream("arquivo.txt");
    }
}


   O código acima não compila e o compilador avisa que é necessário tratar o FileNotFoundException que
pode ocorrer:




    Para compilar e fazer o programa funcionar, precisamos tratar o erro de um de dois jeitos. O primeiro, é
tratá-lo com o try e catch do mesmo jeito que usamos no exemplo anterior, com uma array:

public static void metodo() {

    try {
        new java.io.FileInputStream("arquivo.txt");
    } catch (java.io.FileNotFoundException e) {
        System.out.println("Nao foi possivel abrir o arquivo para leitura");
    }

}


    A segunda forma de tratar esse erro, é delegar ele para quem chamou o nosso método, isto é, passar para
a frente.

public static void metodo() throws java.io.FileNotFoundException {

    new java.io.FileInputStream("arquivo.txt");

}


    No Eclipse é bem simples fazer tanto um try/catch como um throws:

    Tente digitar esse código no eclipse:

public class TestaException {
    public static void main(String[] args) {
        new java.io.FileInputStream("arquivo.txt");
    }
}


    O Eclipse vai reclamar :




                     Capítulo 11 - Controlando os erros com Exceções - Outro tipo de exceção: Checked Exceptions - Página 128


[PAGINA 141]
                                                            Material do Treinamento Java e Orientação a Objetos




   E você tem duas opções:

1) Add throws declaration, que vai gerar:

   public class TestaException {

       public static void main(String[] args) throws FileNotFoundException {
           new java.io.FileInputStream("arquivo.txt");
       }
   }


2) Surround with try/catch, que vai gerar:

   public class TestaException2 {

       public static void main(String[] args) {
           try {
               new java.io.FileInputStream("arquivo.txt");
           } catch (FileNotFoundException e) {
               // TODO Auto-generated catch block
               e.printStackTrace();
           }
       }
   }



    No início, existe uma grande tentação de sempre passar o erro pra frente para outros tratarem dele. Pode
ser que faça sentido, dependendo do caso, mas não até o main, por exemplo. Acontece que quem tenta abrir
um arquivo sabe como lidar com um problema na leitura. Quem chamou um método no começo do programa
pode não saber ou, pior ainda, tentar abrir cinco arquivos diferentes e não saber qual deles teve um problema!

    Não há uma regra para decidir em que momento do seu programa você vai tratar determinada exceção. Isso
vai depender de em que ponto você tem condições de tomar uma decisão em relação àquele erro. Enquanto
não for o momento, você provavelmente vai preferir delegar a responsabilidade para o método que te invocou.




                     Capítulo 11 - Controlando os erros com Exceções - Outro tipo de exceção: Checked Exceptions - Página 129


[PAGINA 142]
                                                          Material do Treinamento Java e Orientação a Objetos




               Boas práticas no tratamento de exceções
            No blog da Caelum há um extenso artigo discutindo as boas práticas em relação ao tratamento de
            exceções.
            http://blog.caelum.com.br/2006/10/07/lidando-com-exceptions/


 11.5 - Um pouco da grande famíla Throwable
   Uma pequena parte da Família Throwable:




 11.6 - Mais de um erro

   É possível tratar mais de um erro quase que ao mesmo tempo:

1) Com o try e catch:

   try {

       objeto.metodoQuePodeLancarIOeSQLException();
   } catch (IOException e) {
       // ..
   } catch (SQLException e) {
       // ..
   }


2) Com o throws:

   public void abre(String arquivo) throws IOException, SQLException {

       // ..
   }


                         Capítulo 11 - Controlando os erros com Exceções - Um pouco da grande famíla Throwable - Página 130


[PAGINA 143]
                                                        Material do Treinamento Java e Orientação a Objetos




3) Você pode, também, escolher tratar algumas exceções e declarar as outras no throws:

   public void abre(String arquivo) throws IOException {

       try {
           objeto.metodoQuePodeLancarIOeSQLException();
       } catch (SQLException e) {
           // ..
       }
   }



    É desnecessário declarar no throws as exceptions que são unchecked, porém é permitido e às vezes, facilita
a leitura e a documentação do seu código.


 11.7 - Lançando exceções
   Lembre-se do método saca da nossa classe Conta. Ele devolve um boolean caso consiga ou não sacar:

boolean saca(double valor){
    if (this.saldo < valor){
        return false;
    } else {
        this.saldo-=valor;
        return true;
    }
}


   Podemos, também, lançar uma Exception, o que é extremamente útil. Dessa maneira, resolvemos o pro-
blema de alguém poder esquecer de fazer um if no retorno de um método.

    A palavra chave throw, que está no imperativo, lança uma Exception. Isto é bem diferente de throws, que
está no presente do indicativo, e que apenas avisa da possibilidade daquele método lançá-la, obrigando o outro
método que vá utilizar deste de se preocupar com essa exceção em questão.

void saca(double valor){
    if (this.saldo < valor){
        throw new RuntimeException();
    } else {
        this.saldo-=valor;
    }
}


    No nosso caso, lança uma do tipo unchecked. RuntimeException é a exception mãe de todas as excep-
tions unchecked. A desvantagem, aqui, é que ela é muito genérica; quem receber esse erro não sabe dizer
exatamente qual foi o problema. Podemos então usar uma Exception mais específica:

void saca(double valor){
    if (this.saldo < valor){
        throw new IllegalArgumentException();
    } else {


                                        Capítulo 11 - Controlando os erros com Exceções - Lançando exceções - Página 131


[PAGINA 144]
                                                         Material do Treinamento Java e Orientação a Objetos




          this.saldo-=valor;
      }
}


    IllegalArgumentException diz um pouco mais: algo foi passado como argumento e seu método não gos-
tou. Ela é uma Exception unchecked pois estende de RuntimeException e já faz parte da biblioteca do java.
(IllegalArgumentException é a melhor escolha quando um argumento sempre é inválido como, por exemplo,
números negativos, referências nulas, etc).

   E agora, para pegar esse erro, não usaremos um if/else e sim um try/catch, porque faz mais sentido já
que a falta de saldo é uma exceção:

Conta cc = new ContaCorrente();
cc.deposita(100);

try {
    cc.saca(100);
} catch (IllegalArgumentException e) {
    System.out.println("Saldo Insuficiente");
}


   Podíamos melhorar ainda mais e passar para o construtor da IllegalArgumentException o motivo da exce-
ção:

void saca(double valor){
    if (this.saldo < valor){
        throw new IllegalArgumentException("Saldo insuficiente");
    } else {
        this.saldo-=valor;
    }
}


    O método getMessage() definido na classe Throwable (mãe de todos os tipos de erros e exceptions) vai
retonar a mensagem que passamos ao construtor da IllegalArgumentException.

try {
    cc.saca(100);
} catch (IllegalArgumentException e) {
    System.out.println(e.getMessage());
}



    11.8 - O que colocar dentro do try?
     Imagine que vamos sacar dinheiro de diversas contas:

Conta cc = new ContaCorrente();
cc.deposita(100);

Conta cp = new ContaPoupanca();


                                 Capítulo 11 - Controlando os erros com Exceções - O que colocar dentro do try? - Página 132


[PAGINA 145]
                                                        Material do Treinamento Java e Orientação a Objetos




cp.deposita(100);

// sacando das contas:

cc.saca(50);
System.out.println("consegui sacar da corrente!");

cp.saca(50);
System.out.println("consegui sacar da poupanca!");


   Podemos escolher vários lugares para colocar try/catch:

try {
    cc.saca(50);
} catch (IllegalArgumentException e) {
    System.out.println(e.getMessage());
}
System.out.println("consegui sacar da corrente!");

try {
    cp.saca(50);
} catch (IllegalArgumentException e) {
    System.out.println(e.getMessage());
}
System.out.println("consegui sacar da poupanca!");


    Essa não parece uma opção boa, pois a mensagem “consegui sacar” será impressa mesmo que o catch
seja acionado. Sempre que temos algo que depende da linha de cima para ser correto, devemos agrupá-lo no
try:


try {
    cc.saca(50);
    System.out.println("consegui sacar da corrente!");
} catch (IllegalArgumentException e) {
    System.out.println(e.getMessage());
}

try {
    cp.saca(50);
    System.out.println("consegui sacar da poupanca!");
} catch (IllegalArgumentException e) {
    System.out.println(e.getMessage());
}


   Mas há ainda uma outra opção: imagine que, para o nosso sistema, uma falha ao sacar da conta poupança
deve parar o processo de saques e nem tentar sacar da conta corrente. Para isso, agruparíamos mais ainda:

try {
    cc.saca(50);
    System.out.println("consegui sacar da corrente!");
    cp.saca(50);
    System.out.println("consegui sacar da poupanca!");

                                Capítulo 11 - Controlando os erros com Exceções - O que colocar dentro do try? - Página 133


[PAGINA 146]
                                                            Material do Treinamento Java e Orientação a Objetos




} catch (IllegalArgumentException e) {
    System.out.println(e.getMessage());
}


    O que você vai colocar dentro do try influencia muito a execução do programa! Pense direito nas
linhas que dependem uma da outra para a execução correta da sua lógica de negócios.


    11.9 - Criando seu próprio tipo de exceção

   É bem comum criar uma própria classe de exceção para controlar melhor o uso de suas exceções. Dessa
maneira, podemos passar valores específicos para ela carregar, que sejam úteis de alguma forma. Vamos criar
a nossa:

     Voltamos para o exemplo das Contas, vamos criar a nossa Exceção de SaldoInsuficienteException:

public class SaldoInsuficienteException extends RuntimeException{

      SaldoInsuficienteException(String message){
          super(message);
      }
}


  E agora, em vez de lançar um IllegalArgumentException, vamos lançar nossa própria exception, com uma
mensagem que dirá “Saldo Insuficiente":

void saca(double valor){
    if (this.saldo < valor){
        throw new SaldoInsuficienteException("Saldo Insuficiente, tente um valor menor");
    } else {
        this.saldo-=valor;
    }
}


     E, para testar, crie uma classe que deposite um valor e tente sacar um valor maior:

public static void main(String[] args) {
    Conta cc = new ContaCorrente();
    cc.deposita(10);

      try {
          cc.saca(100);
      } catch (SaldoInsuficienteException e) {
          System.out.println(e.getMessage());
      }
}


   Podemos transformar essa Exception de unchecked para checked, obrigando a quem chama esse método
a dar try-catch, ou throws:



                            Capítulo 11 - Controlando os erros com Exceções - Criando seu próprio tipo de exceção - Página 134


[PAGINA 147]
                                                         Material do Treinamento Java e Orientação a Objetos




public class SaldoInsuficienteException extends Exception{

         SaldoInsuficienteException(String message){
             super(message);
         }
}



    11.10 - Para saber mais: finally
   Os blocos try e catch podem conter uma terceira cláusula chamada finally que indica o que deve ser feito
após o término do bloco try ou de um catch qualquer.

    É interessante colocar algo que é imprescindível de ser executado, caso o que você queria fazer tenha dado
certo, ou não. O caso mais comum é o de liberar um recurso no finally, como um arquivo ou conexão com banco
de dados, para que possamos ter a certeza de que aquele arquivo (ou conexão) vá ser fechado, mesmo que
algo tenha falhado no decorrer do código.

   No exemplo a seguir, o bloco finally será executado - não importa se tudo ocorrer ok ou com algum
problema:

try {
    // bloco try
} catch (IOException ex) {
    // bloco catch 1
} catch (SQLException sqlex) {
    // bloco catch2
} finally {
    // bloco finally
}



    11.11 - Exercícios: Exceções

1) Na classe Conta, modifique o método deposita(double x): Ele deve lançar uma exception chamada
   IllegalArgumentException, que já faz parte da biblioteca do java, sempre que o valor passado como
   argumento for inválido (por exemplo, quando for negativo).

     void deposita(double valor){

           if (valor < 0) {
               throw new IllegalArgumentException();
           } else {
               this.saldo += valor - 0.10;
           }
     }


2) Crie uma classe TestaDeposita com o método main. Crie uma ContaPoupanca e tente depositar valores
   inválidos:

     public static void main(String[] args) {

           Conta cp = new ContaPoupanca();

                                     Capítulo 11 - Controlando os erros com Exceções - Para saber mais: finally - Página 135


[PAGINA 148]
                                                      Material do Treinamento Java e Orientação a Objetos




       cp.deposita(-100);
  }

  O que acontece? Uma IllegalArgumentException é lançada uma vez que tentamos depositar um valor
  inválido. Adicione o try/catch para tratar o erro:

   public static void main(String[] args) {

       Conta cp = new ContaPoupanca();

       try {
           cp.deposita(-100);
       } catch (IllegalArgumentException e) {
           System.out.println("Você tentou depositar um valor inválido");
       }
  }


  Atenção: se a sua classe ContaCorrente está reescrevendo o método deposita e não utiliza do
  super.deposita, ela não lançará a exception no caso do valor negativo! Você pode resolver isso utilizando o
  super.deposita, ou fazendo apenas o teste com ContaPoupanca.

3) Ao lançar a IllegalArgumentException, passe via construtor uma mensagem a ser exibida. Lembre que
   a String recebida como parâmetro é acessível depois via o método getMessage() herdado por todas as
   Exceptions.

   void deposita(double valor){

       if (valor < 0){
           throw new IllegalArgumentException("Você tentou depositar um valor negativo");
       } else {
           this.saldo += valor - 0.10;
       }
  }


4) Agora, altere sua classe TestaDeposita para exibir a mensagem da exceção através da chamada do
   getMessage():

   public static void main(String[] args) {

       Conta cp = new ContaPoupanca();

       try {
           cp.deposita(-100);
       } catch (IllegalArgumentException e){
           System.out.println(e.getMessage());
       }
  }


5) Crie sua própria Exception, ValorInvalidoException. Para isso, você precisa criar uma classe com esse
   nome que estenda de RuntimeException.

   class ValorInvalidoException extends RuntimeException {




                                     Capítulo 11 - Controlando os erros com Exceções - Exercícios: Exceções - Página 136


[PAGINA 149]
                                                       Material do Treinamento Java e Orientação a Objetos




   }


   Lance-a em vez de IllegalArgumentException.
   Atenção: nem sempre é interessante criarmos um novo tipo de exception! Depende do caso. Neste aqui,
   seria melhor ainda utilizarmos IllegalArgumentException. A boa prática diz que devemos preferir usar as já
   existentes do Java sempre que possível.

6) (opcional) Coloque um construtor na classe ValorInvalidoException que receba valor inválido que ele tentou
   passar (isto é, ele vai receber um double valor).
   Quando estendemos uma classe, não herdamos seus construtores, mas podemos acessá-los através da
   palavra chave super de dentro de um construtor. As exceções do Java possuem uma série de constru-
   tores úteis para poder popula-las já com uma mensagem de erro. Então vamos criar um construtor em
   ValorInvalidoException que delegue para o construtor de sua mãe. Essa vai guardar essa mensagem
   para poder monstra-la ao ser invocado o método getMessage:

   class ValorInvalidoException extends RuntimeException {


       ValorInvalidoException(double valor) {
           super("Valor invalido: " + valor);
       }

   }

   Dessa maneira, na hora de dar o throw new ValorInvalidoException você vai precisar passar esse valor
   como argumento:

   if (valor < 0) {

       throw new ValorInvalidoException(valor);
   }


   Atenção! Você pode se aproveitar do Eclipse para isso: comece já passando o valor como argumento para
   o construtor da exception, e o eclipse vai reclamar que não existe tal construtor. O quick fix vai sugerir que
   ele seja construindo, poupando-lhe tempo!

7) (opcional) Declare a classe ValorInvalidoException como filha direta de Exception em vez de
   RuntimeException. Ela passa agora a ser checked. O que isso resulta?
   Você vai precisar avisar que o seu método deposita() throws ValorInvalidoException, pois ela é uma
   checked exception. Além disso, quem chama esse método vai precisar tomar uma decisão entre try-catch
   ou throws. Utilize-se do quick fix do Eclipse novamente!
   Depois, retorne a exception para unchecked, isto é, para ser filha de RuntimeException, pois iremos utilizá-la
   assim em exercícios dos capítulos posteriores.


 11.12 - Desafios

1) O que acontece se acabar a memória da java virtual machine? Como forçar isso?




                                                  Capítulo 11 - Controlando os erros com Exceções - Desafios - Página 137


[PAGINA 150]
                                                           Material do Treinamento Java e Orientação a Objetos




 11.13 - Discussão em aula: catch e throws em Exception
   Existe uma péssima prática de programação em java que é a de escrever o catch e o throws com Exception.

    Existem códigos que sempre usam Exception pois isso cuida de todos os possíveis erros. O maior problema
disso é generalizar o erro. Se alguém joga algo do tipo Exception para quem o chamou, quem recebe não sabe
qual o tipo específico de erro ocorreu e não vai saber como tratar o mesmo.




               Capítulo 11 - Controlando os erros com Exceções - Discussão em aula: catch e throws em Exception - Página 138


[PAGINA 151]
                                                                                            C APÍTULO   12

Pacotes - Organizando suas classes e
bibliotecas
                                    “Uma discussão prolongada significa que ambas as partes estão erradas”
                                                                                                  – Voltaire


   Ao término desse capítulo, você será capaz de:

   • separar suas classes em pacotes e

   • preparar arquivos simples para distribuição.


 12.1 - Organização
   Quando um programador utiliza as classes feitas por outro, surge um problema clássico: como escrever
duas classes com o mesmo nome?

    Por exemplo: pode ser que a minha classe de Data funcione de um certo jeito, e a classe Data de um
colega, de outro jeito. Pode ser que a classe de Data de uma biblioteca funcione ainda de uma terceira maneira
diferente.

   Como permitir que tudo isso realmente funcione? Como controlar quem quer usar qual classe de Data?

   Pensando um pouco mais, notamos a existência de um outro problema e da própria solução: o sistema
operacional não permite a existência de dois arquivos com o mesmo nome sob o mesmo diretório, portanto
precisamos organizar nossas classes em diretórios diferentes.

    Os diretórios estão diretamente relacionados aos chamados pacotes e costumam agrupar classes de fun-
cionalidades similares ou relacionadas.

    Por exemplo, no pacote java.util temos as classes Date, SimpleDateFormat e GregorianCalendar; todas
elas trabalham com datas de formas diferentes.




                                                     139


[PAGINA 152]
                                                         Material do Treinamento Java e Orientação a Objetos




 12.2 - Diretórios
    Se a classe Cliente está no pacote banco, ela deverá estar no diretório com o mesmo nome: banco. Se ela
se localiza no pacote br.com.caelum.banco, significa que está no diretório br/com/caelum/banco.

   A classe Cliente, que se localiza nesse último diretório mencionado, deve ser escrita da seguinte forma:

package br.com.caelum.banco;

class Cliente {
    // ...
}


   Fica fácil notar que a palavra chave package indica qual o pacote/diretório contém esta classe.

   Um pacote pode conter nenhum ou mais subpacotes e/ou classes dentro dele.


             Padrão da nomenclatura dos pacotes
           O padrão da sun para dar nome aos pacotes é relativo ao nome da empresa que desenvolveu a
           classe:

            br.com.nomedaempresa.nomedoprojeto.subpacote

           br.com.nomedaempresa.nomedoprojeto.subpacote2
           br.com.nomedaempresa.nomedoprojeto.subpacote2.subpacote3

           Os pacotes só possuem letras minúsculas, não importa quantas palavras estejam contidas nele.
           Esse padrão existe para evitar ao máximo o conflito de pacotes de empresas diferentes.
           As classes do pacote padrão de bibliotecas não seguem essa nomenclatura, que foi dada para
           bibliotecas de terceiros.


 12.3 - Import
   Para usar uma classe do mesmo pacote, basta fazer referência a ela como foi feito até agora simplesmente
escrevendo o próprio nome da classe. Se existe uma classe Banco dentro do pacote br.com.caelum.banco, ela
deve ser escrita assim:

package br.com.caelum.banco;

class Banco {
    String nome;
    Cliente clientes[];
}


   A classe Cliente deve ficar no mesmo pacote da seguinte maneira:

package br.com.caelum.banco;

class Cliente {

                                     Capítulo 12 - Pacotes - Organizando suas classes e bibliotecas - Diretórios - Página 140


[PAGINA 153]
                                                       Material do Treinamento Java e Orientação a Objetos




    String nome;
    String endereco;
}


   A novidade chega ao tentar utilizar a classe Banco (ou Cliente) em uma outra classe que esteja em outro
pacote, por exemplo, no pacote br.com.caelum.util:

package br.com.caelum.banco.util;

class TesteDoBanco {

    public static void main(String args[]) {
      br.com.caelum.banco.Banco meuBanco = new br.com.caelum.banco.Banco();
      meuBanco.nome = "Banco do Brasil";
      System.out.println(meuBanco.nome);
    }

}


    Repare que precisamos referenciar a classe Banco com todo o nome do pacote na sua frente. Esse é o
conhecido Full Qualified Name de uma classe. Em outras palavras, esse é o verdadeiro nome de uma classe,
por isso duas classes com o mesmo nome em pacotes diferentes não conflitam.

    Mesmo assim, ao tentar compilar a classe anterior, surge um erro reclamando que a classe Banco não está
visível.

   Acontece que as classes só são visíveis para outras no mesmo pacote e, para permitir que a classe
TesteDoBanco veja e acesse a classe Banco em outro pacote, precisamos alterar essa última e transformá-la
em pública:

package br.com.caelum.banco;

public class Banco {
    String nome;
    Cliente clientes[] = new Cliente[2];
}


    A palavra chave public libera o acesso para classes de outros pacotes. Do mesmo jeito que o compilador
reclamou que a classe não estava visível, agora ele reclama que o atributo/variável membro também não está.
É fácil deduzir como resolver o problema - algo que já foi visto anteriormente:

package br.com.caelum.banco;

public class Banco {
    public String nome;
    public Cliente clientes[] = new Cliente[2];
}


    Agora já podemos testar nosso exemplo anterior.



                                       Capítulo 12 - Pacotes - Organizando suas classes e bibliotecas - Import - Página 141


[PAGINA 154]
                                                                Material do Treinamento Java e Orientação a Objetos




   Voltando ao código do TesteDoBanco, é necessário escrever todo o pacote para identificar qual classe que-
remos usar? O exemplo que usamos ficou bem complicado de ler:

br.com.caelum.banco.Banco meuBanco = new br.com.caelum.banco.Banco();


   Existe uma maneira mais simples de se referenciar a classe Banco:                           basta importá-la do pacote
br.com.caelum.banco:


package br.com.caelum.banco.util;

import br.com.caelum.banco.Banco; // agora podemos nos referenciar
                     // a Banco diretamente

class TesteDoBanco {

      public static void main(String args[]) {
          Banco meuBanco = new Banco();
          meuBanco.nome = "Banco do Brasil";
      }

}



               package, import, class
             É muito importante manter a ordem! Primeiro, aparece uma (ou nenhuma) vez o package; depois,
             pode aparecer um ou mais imports; e, por último, as declarações de classes.


              import x.y.z.*;
             É possível importar um pacote inteiro (todas as classes do pacote, exceto os subpacotes) através
             do *:

              import java.util.*;


             Importar todas as classes de um pacote não implica em perda de performance em tempo de exe-
             cução, mas pode trazer problemas com classes de mesmo nome! Além disso, importar de um em
             um é considerado boa prática, pois facilita a leitura para outros programadores.


    12.4 - Acesso aos atributos, construtores e métodos
  Os modificadores de acesso existentes em Java são quatro, e até o momento já vimos três, mas só explica-
mos dois.

     • public – Todos podem acessar aquilo que for definido como public. Classes, atributos, construtores e
       métodos podem ser public.

     • protected – Aquilo que é protected pode ser acessado por todas as classes do mesmo pacote e por
       todas as classes que o estendam, mesmo que essas não estejam no mesmo pacote. Somente atributos,
       construtores e métodos podem ser protected.

         Capítulo 12 - Pacotes - Organizando suas classes e bibliotecas - Acesso aos atributos, construtores e métodos - Página 142


[PAGINA 155]
                                                          Material do Treinamento Java e Orientação a Objetos




   • padrão (sem nenhum modificador) – Se nenhum modificador for utilizado, todas as classes do mesmo
     pacote têm acesso ao atributo, construtor, método ou classe.

   • private – A única classe capaz de acessar os atributos, construtores e métodos privados é a própria
     classe. Classes, como conhecemos, não podem ser private, mas atributos, construtores e métodos sim.


             Classes públicas
           Para melhor organizar seu código, o Java não permite mais de uma classe pública por arquivo e o
           arquivo deve ser NomeDaClasse.java.
           Uma vez que outros programadores irão utilizar essa classe, quando precisarem olhar o código da
           mesma, fica mais fácil encontrá-la sabendo que ela está no arquivo de mesmo nome.
           Classes podem ser protected ou private, mas esse é um tópico avançado que não será estudado
           nesse instante (classes internas).


 12.5 - Usando o Eclipse com pacotes
   Você pode, agora, usar a perspectiva Java do eclipse. A view principal de navegação é o package explorer,
que agrupa classes pelos pacotes em vez de diretórios (você pode usá-la em conjunto com a Navigator, basta
também abrí-la pelo Window/Show View/Package Explorer )




   Antes de movermos nossas classes, declare-as como públicas e coloque-as em seus respectivos arquivos:
um arquivo para cada classe.


                   Capítulo 12 - Pacotes - Organizando suas classes e bibliotecas - Usando o Eclipse com pacotes - Página 143


[PAGINA 156]
                                                         Material do Treinamento Java e Orientação a Objetos




   Você pode mover uma classe de pacote arrastando-a para o destino desejado. Repare que o Eclipse já
declara packages e imports necessários:




   No Eclipse nunca precisamos declarar um import, pois ele sempre vai sugerir isso quando usarmos o
Ctrl+Espaço no nome de uma classe.

   Você também pode usar o Ctrl+1 no caso da declaração de pacote possuir algum erro.


 12.6 - Exercícios: Pacotes
   Atenção: utilize os recursos do Eclipse para realizar essas mudanças. Use a view package-explorer.
Também utilize os quick fixes quando o Eclipse reclamar dos diversos problemas. de compilação. Da para fazer
esse exercício inteiro sem modificar uma linha de código manualmente. Aproveite para praticar e descobrir
o Eclipse, evite usa-lo apenas como um editor de texto.

     Por exemplo, com o Eclipse nunca precisamos nos preocupar com os imports: ao usar o auto complete ele
ja joga o import lá em cima. E se você não fez isso, ele sugere colocar o import.

1) Clique da direita no src do seu projeto e escolhendo File/New/Package, ponha o seu sistema de Contas
   para utilizar pacotes. Respeite a convenção de código da Sun, por exemplo:
   br.com.empresa.banco: colocar classes com o método main aqui (os Testes)
   br.com.empresa.banco.conta : colocar Conta, suas filhas e exceptions aqui
   br.com.empresa.banco.sistema : colocar AtualizadorDeContas aqui
   Antes de corrigir qualquer erro de compilação, primeiro mova todas as suas classes, sem deixar nenhuma
   no pacote default.

                            Capítulo 12 - Pacotes - Organizando suas classes e bibliotecas - Exercícios: Pacotes - Página 144


[PAGINA 157]
                                                         Material do Treinamento Java e Orientação a Objetos




2) Caso necessário, coloque cada classe em seu respectivo arquivo .java. Faça isso independente de ela ser
   pública (é uma boa prática).

3) O código não vai compilar prontamente, pois muitos métodos que declaramos são package-friendly quando,
   na verdade, precisaríamos que eles fossem public.
   O mesmo vale para as classes: algumas delas precisarão ser públicas.
   Use o recurso de quick fix do Eclipse aqui: ele mesmo vai sugerir que o modificador de acesso deve ser
   público. Para isso clique no quick fix que aparecerá no erro do import e das invocações de métodos.

4) Abra a view Navigator para ver como ficou os arquivos no sistema de arquivos do seu sistema operacional.
   Para isso, use o menu Window, Show View.




                            Capítulo 12 - Pacotes - Organizando suas classes e bibliotecas - Exercícios: Pacotes - Página 145


[PAGINA 158]
                                                                                             C APÍTULO    13

Ferramentas: jar e javadoc
          “Perder tempo em aprender coisas que não interessam, priva-nos de descobrir coisas interessantes”
                                                                             – Carlos Drummond de Andrade


   Ao término desse capítulo, você será capaz de:

   • criar o JAR do seu aplicativo;

   • colocar um JAR no build path do seu projeto;

   • ler um javadoc;

   • criar o javadoc do seu aplicativo.


 13.1 - Arquivos, bibliotecas e versões
    Assim que um programa fica pronto, é meio complicado enviar dezenas ou centenas de classes para cada
cliente que quer utilizá-lo.

   O jeito mais simples de trabalhar com um conjunto de classes é compactá-los em um arquivo só. O formato
de compactação padrão é o ZIP com a extensão do arquivo compactado JAR.


             O arquivo .jar
            O arquivo jar ou Java ARchive, possui um conjunto de classes (e arquivos de configurações) com-
            pactados, no estilo de um arquivo zip. O arquivo jar pode ser criado com qualquer compactador
            zip disponível no mercado, inclusive o programa jar que vem junto com o JDK.


    Para criar um arquivo jar do nosso programa de banco, basta ir ao diretório onde estão contidas as classes e
usar o comando a seguir para criar o arquivo banco.jar com todas as classes dos pacotes br.com.caelum.util
e br.com.caelum.banco:


jar -cvf banco.jar br/com/caelum/util/*.class br/com/caelum/banco/*.class                  diretório [bin]

   Para usar esse arquivo banco.jar para rodar o TesteDoBanco basta rodar o java com o arquivo jar como
argumento:


java -classpath banco.jar br.com.caelum.util.TesteDoBanco




                                                      146


[PAGINA 159]
                                                       Material do Treinamento Java e Orientação a Objetos




  Para adicionar mais arquivos .jar, que podem ser bibliotecas, ao programa basta rodar o java da seguinte
maneira:


java -classpath biblioteca1.jar;biblioteca2.jar NomeDaClasse


   Vale lembrar que o ponto e vírgula utilizado só é válido em ambiente Windows. Em Linux, Mac e outros
Unix, é o dois pontos (varia de acordo com o sistema operacional).

    Há também um arquivo de manifesto que contém informações do seu jar como, por exemplo, qual classe
ele vai rodar quando o jar for chamado. Mas não se preocupe pois, com o Eclipse, esse arquivo é gerado
automaticamente.

             Bibliotecas
           Diversas bibliotecas podem ser controladas de acordo com a versão por estarem sempre compac-
           tadas em um arquivo .jar. Basta verificar o nome da biblioteca (por exemplo log4j-1.2.13.jar)
           para descobrir a versão dela.
           Então é possível rodar dois programas ao mesmo tempo, cada um utilizando uma versão da biblio-
           teca através do parâmetro -classpath do java.


             Criando um .jar automaticamente
           Existem diversas ferramentas que servem para automatizar o processo de deploy, que consiste em
           compilar, gerar documentação, bibliotecas etc. As duas mais famosas são o ANT e o MAVEN,
           ambos são projetos do grupo Apache.
           O Eclipse pode gerar facilmente um jar, porém, se o seu build é complexo e precisa preparar e
           copiar uma série de recursos, as ferramentas indicadas acima possuem sofisticadas maneiras de
           rodar um script batch.


 13.2 - Gerando o jar pelo Eclipse
   Neste exemplo, vamos gerar o arquivo JAR do nosso projeto a partir do Eclipse.

1) Clique com o botão direito em cima do nome do seu projeto e selecione a opção Export.




                                         Capítulo 13 - Ferramentas: jar e javadoc - Gerando o jar pelo Eclipse - Página 147


[PAGINA 160]
                                                        Material do Treinamento Java e Orientação a Objetos




2) Na tela Export (como mostra a figura abaixo), selecione a opção “JAR file” e aperte o botão “Next”.




                                          Capítulo 13 - Ferramentas: jar e javadoc - Gerando o jar pelo Eclipse - Página 148


[PAGINA 161]
                                                         Material do Treinamento Java e Orientação a Objetos




3) Na opção “JAR file:”, selecione o local que você deseja salvar o arquivo JAR. E aperte “Next”.




                                           Capítulo 13 - Ferramentas: jar e javadoc - Gerando o jar pelo Eclipse - Página 149


[PAGINA 162]
                                                          Material do Treinamento Java e Orientação a Objetos




4) Na próxima tela, simplesmente clique em next, pois não há nenhuma configuração a ser feita.

5) Na tela abaixo, na opção “select the class of the apllication entry point”, você deve escolher qual classe será
   a classe que vai rodar automaticamente quando você executar o JAR.




                                            Capítulo 13 - Ferramentas: jar e javadoc - Gerando o jar pelo Eclipse - Página 150


[PAGINA 163]
                                                       Material do Treinamento Java e Orientação a Objetos




6) Entre na linha de comando: java -jar banco.jar

   É comum dar um nome mais signficativo aos jars, incluindo nome da empresa, do projeto e versão, como
caelum-banco-1.0.jar.


 13.3 - Javadoc
   Como vamos saber o que cada classe tem no Java? Quais são seus métodos, o que eles fazem?

   Aqui na Caelum, você pode acessar a documentação digitando na barra de endereço do Browser:

   /caelum/docs/api/index.html

   E, a partir da Internet, você pode acessar através do link:

                                                          Capítulo 13 - Ferramentas: jar e javadoc - Javadoc - Página 151


[PAGINA 164]
                                                      Material do Treinamento Java e Orientação a Objetos




   http://java.sun.com/javase/6/docs/api/
   No site da Sun, você pode (e deve) baixar a documentação das bibliotecas do Java, frequentemente referida
como “javadoc” ou API (sendo na verdade a documentação da API).




     Nesta documentação, no quadro superior esquerdo, você encontra os pacotes e, no inferior esquerdo, está
a listagem das classes e interfaces do respectivo pacote (ou de todos, caso nenhum tenha sido especificado).
Clicando-se em uma classe ou interface, o quadro da direita passa a detalhar todos atributos e métodos.

    Repare que métodos e atributos privados não estão aí. O importante é documentar o que sua classe
faz, e não como ela faz: detalhes de implementação, como atributos e métodos privados, não interessam ao
desenvolvedor que usará a sua biblioteca (ou, ao menos, não deveriam interessar).

   Você também consegue gerar esse javadoc a partir da linha de comando, com o comando: javadoc.


 13.4 - Gerando o Javadoc
   Para gerar o Javadoc a partir do Eclipse é muito simples, siga os passos abaixo:

1) Na barra de menu, selecione o menu Project, depois a opção “Generate Javadoc...”. (apenas disponível se
   estiver na perspectiva Java, mas você pode acessar o mesmo wizard pelo export do projeto).




                                               Capítulo 13 - Ferramentas: jar e javadoc - Gerando o Javadoc - Página 152


[PAGINA 165]
                                                   Material do Treinamento Java e Orientação a Objetos




2) Em seguida, aparecerão as opções para gerar a documentação do seu sistema, selecione todas as clas-
   ses do seu sistema e deixe as outras opções como estão. Não esqueça de marcar o caminho da opção
   “Destination”, pois é lá que estará sua documentação.




                                            Capítulo 13 - Ferramentas: jar e javadoc - Gerando o Javadoc - Página 153


[PAGINA 166]
                                                   Material do Treinamento Java e Orientação a Objetos




3) Abra a documentação através do caminho que você marcou e abra o arquivo index.html, que vai chamar
   uma página semelhante a essa da figura abaixo.




                                            Capítulo 13 - Ferramentas: jar e javadoc - Gerando o Javadoc - Página 154


[PAGINA 167]
                                                   Material do Treinamento Java e Orientação a Objetos




Para colocarmos comentários na documentação, devemos adicionar ao código, sob forma de comentário,
abrindo o texto com /** e fechando com */ e, nas outras linhas, apenas colocando *. Também podemos
definir algumas coisas neste texto, como: autor, versão, parâmetros, retorno, etc. Agora, adicione alguns
comentários ao seu Projeto como abaixo:

/**

 * Classe responsavel por moldar as Contas do Banco
 *
 * @author Manoel Santos da Silva
 */

public abstract class Conta{

Ou adicione alguns comentários em algum método seu:

/**

 * Metodo que incrementa o saldo.
 * @param valor
 */

public void deposita(double valor) {


Veja como ficou:


                                            Capítulo 13 - Ferramentas: jar e javadoc - Gerando o Javadoc - Página 155


[PAGINA 168]
                                                        Material do Treinamento Java e Orientação a Objetos




 13.5 - Exercícios: Jar e Javadoc

1) Gere um jar do seu sistema com o arquivo de manifesto. Execute-o com java -jar:

   java -jar caelum-banco-1.0.jar



   Se o Windows ou o Linux foi configurado para trabalhar com a extensão .jar, basta você dar um duplo clique
   no arquivo, que ele será “executado” (o arquivo de manifesto será lido para que ele possa descobrir qual é a
   classe com main que o java deve processar).

2) Gere o javadoc do seu sistema. Para isso va ao menu Project, depois a opção Generate Javadoc... se
   estiver na perspectiva Java, ou então de um clique com o botão direito no seu projeto, escolha Export e
   depois javadoc e siga o procedimento descrito na última seção deste capítulo.


             Interface versus implementacao novamente!
            Repare que a documentação gerada não mostra o conteúdo dos métodos, nem atributos e méto-
            dos privados! Essas coisas fazem parte da implementação, e o que importa para quem usa uma
            biblioteca é a interface: o que ela faz.




                                           Capítulo 13 - Ferramentas: jar e javadoc - Exercícios: Jar e Javadoc - Página 156


[PAGINA 169]
                                                                                           C APÍTULO    14

O pacote java.lang
                        “Nossas cabeças são redondas para que os pensamentos possam mudar de direção.”
                                                                                     – Francis Piacaba


   Ao término desse capítulo, você será capaz de:

   • utilizar as principais classes do pacote java.lang e ler a documentação padrão de projetos java;

   • usar a classe System para obter informações do sistema;

   • utilizar a classe String de uma maneira eficiente e conhecer seus detalhes;

   • usar as classes wrappers (como Integer) e boxing;

   • utilizar os métodos herdados de Object para generalizar seu conceito de objetos.


 14.1 - Pacote java.lang
   Já usamos, por diversas vezes, as classes String e System. Vimos o sistema de pacotes do Java e nunca
precisamos dar um import nessas classes. Isso ocorre porque elas estão dentro do pacote java.lang, que é
automaticamente importado para você. É o único pacote com esta característica.

   Vamos ver um pouco de suas principais classes.


 14.2 - Um pouco sobre a classe System
   A classe System possui uma série de atributos e métodos estáticos. Já usamos o atributo System.out, para
imprimir.

   Olhando a documentação, você irá perceber que o atributo out é do tipo PrintStream do pacote
java.io. Veremos sobre essa classe no próximo capítulo. Já podemos perceber que poderíamos quebrar o
System.out.println em duas linhas:


PrintStream saida = System.out;
out.println("ola mundo!");


   Ela também possui o atributo in, que lê da entrada padrão, porém só consegue captar bytes:

int i = System.in.read();




                                                    157


[PAGINA 170]
                                                        Material do Treinamento Java e Orientação a Objetos




   O código acima deve estar dentro de um bloco de try e catch, pois pode lançar uma exceção IOException.
É útil ficar lendo de byte em byte? Trabalharemos mais com a entrada padrão também no próximo capítulo.

   O System conta também com um método que simplesmente desliga a virtual machine, retornando um código
de erro para o sistema operacional, é o exit.

System.exit(0);


   Veremos também um pouco mais sobre a classe System no próximo capítulo e no de Threads. Consulte a
documentação do Java e veja outros métodos úteis da System.

             A classe Runtime
            A classe Runtime possui um método para fazer uma chamada ao sistema operacional e rodar
            algum programa:

            Runtime rt = Runtime.getRuntime();

            Process p = rt.exec("dir");

            Isto deve ser evitado ao máximo, já que gera uma dependência da sua aplicação com o sistema operacional
            em questão, perdendo a portabilidade entre plataformas. Em muitos casos, isso pode ser substituído por
            chamadas as bibliotecas do java. Nesse caso, por exemplo, você tem um método list na classe File do
            pacote de entrada e saída, que veremos posteriormente.
            O método exec te retorna um Process, onde você é capaz de pegar a saída do programa, enviar dados para
            a entrada, entre outros.



    14.3 - java.lang.Object
   Sempre quando declaramos uma classe, essa classe é obrigada a herdar de outra. Isto é, para toda classe
que declararmos, existe uma superclasse. Porém, criamos diversas classes sem herdar de ninguém:

class MinhaClasse {

}


   Quando o Java não encontra a palavra chave extends, ele considera que você está herdando da classe
Object, que também se encontra dentro do pacote java.lang. Você até mesmo pode escrever essa herança,
que é a mesma coisa:

class MinhaClasse extends Object {

}


    Todas as classes, sem exceção, herdam de Object, seja direta ou indiretamente, pois ela é a mãe, vó,
bisavó, etc de qualquer classe.

    Podemos também afirmar que qualquer objeto em Java é um Object, podendo ser referenciado como tal.
Então, qualquer objeto possui todos os métodos declarados na classe Object e veremos alguns deles logo após
o casting.



                                                           Capítulo 14 - O pacote java.lang - java.lang.Object - Página 158


[PAGINA 171]
                                                      Material do Treinamento Java e Orientação a Objetos




    14.4 - Casting de referências
    A habilidade de poder se referir a qualquer objeto como Object nos traz muitas vantagens. Podemos criar um
método que recebe um Object como argumento, isto é, qualquer coisa! Melhor, podemos armazenar qualquer
objeto:

public class GuardadorDeObjetos {
    private Object[] arrayDeObjetos = new Object[100];
    private int posicao = 0;

      public void adicionaObjeto(Object object) {
          this.arrayDeObjetos[this.posicao] = object;
          this.posicao++;
      }

      public Object pegaObjeto(int indice) {
          return this.arrayDeObjetos[indice];
      }
}


    Mas, e no momento que retirarmos uma referência a esse objeto, como vamos acessar os métodos e
atributos desse objeto? Se estamos referenciando-o como Object, não podemos acessá-lo como sendo Conta.
Veja o exemplo a seguir:

GuardadorDeObjetos guardador = new GuardadorDeObjetos();
Conta conta = new Conta();
guardador.adicionaObjeto(conta);

// ...

Object object = guardador.pegaObjeto(0); // pega a conta referenciado como objeto
object.getSaldo(); // classe Object nao tem método getSaldo! não compila!


  Poderíamos então atribuir essa referência de Object para Conta para depois invocar o getSaldo()? Tente-
mos:

Conta contaResgatada = object;


    Nós temos certeza de que esse Object se refere a uma Conta, já que fomos nós que o adicionamos na
classe que guarda objetos. Mas o compilador Java não tem garantias sobre isso! Essa linha acima não compila,
pois nem todo Object é uma Conta.

    Para realizar essa atribuição, para isso devemos “avisar” o compilador Java que realmente queremos fazer
isso, sabendo do risco que corremos. Fazemos o casting de referências, parecido com de tipos primitivos:

Conta contaResgatada = (Conta) object;


   Agora o código passa a compilar, mas será que roda? Esse código roda sem nenhum problema, pois em
tempo de execução a JVM verificará se essa referência realmente é para um objeto de tipo Conta, e está! Se
não estivesse, uma exceção do tipo ClassCastException seria lançada.

                                                    Capítulo 14 - O pacote java.lang - Casting de referências - Página 159


[PAGINA 172]
                                                          Material do Treinamento Java e Orientação a Objetos




   Poderíamos fazer o mesmo com Funcionario e Gerente. Tendo uma referência para um Funcionario que te-
mos certeza ser um Gerente, podemos fazer a atribuição, desde que o casting exista, pois nem todo Funcionario
é um Gerente.

Funcionario funcionario = new Gerente();

//       ... e depois

Gerente gerente = funcionario; // não compila!
                     // nem todo Funcionario é um Gerente


     O correto então seria:

Gerente gerente = (Gerente) funcionario;


     E agora vamos misturar algumas coisas:

Object object = new Conta();

//       ... e depois

Gerente gerente = (Gerente) object;


     Esse código compila? Roda?

    Compila, pois existe a chance de um Object ser um Gerente. Porém não roda, ele vai lançar uma Exception
(ClassCastException) em tempo de execução. É importante diferenciar tempo de compilação e tempo de exe-
cução.

    Neste exemplo, nós garantimos ao java que nosso Objeto object era um Gerente com o Casting, por isso
compilou, mas na hora de rodar, quando ele foi receber um Gerente, ele recebeu uma Conta, daí ele reclamou
lançando ClassCastException!


 14.5 - Métodos do java.lang.Object: equals e toString
  O primeiro método interessante é o toString. As classes podem reescrever esse método para mostrar uma
mensagem, uma String, que o represente. Você pode usá-lo assim:

Conta c = new Conta();
System.out.println(c.toString());


     O método toString do Object retorna o nome da classe @ um número de identidade:


Conta@34f5d74a


     Mas isso não é interessante para nós. Então podemos reescrevê-lo:



                                Capítulo 14 - O pacote java.lang - Métodos do java.lang.Object: equals e toString - Página 160


[PAGINA 173]
                                                          Material do Treinamento Java e Orientação a Objetos




class Conta {
    private double saldo;
    // outros atributos...

    public Conta(double saldo) {
        this.saldo = saldo;
    }

    public String toString() {
        return "Uma conta com valor: " + this.saldo;
    }
}


    Chamando o toString agora:

Conta c = new Conta(100);
System.out.println(c.toString()); //imprime: Uma conta com valor: 100.


   E o melhor, se for apenas para jogar na tela, você nem precisa chamar o toString! Ele já é chamado para
você:

Conta c = new Conta(100);
System.out.println(c); // O toString é chamado pela classe PrintStream


    Gera o mesmo resultado!

   Você ainda pode concatenar Strings em Java com o operador +. Se o Java encontra um objeto no meio da
concatenação, ele também chama o toString dele.

Conta c = new Conta(100);
System.out.println("descrição: " + c);


    O outro método muito importante é o equals. Quando comparamos duas variáveis referência no Java, o ==
verifica se as duas referem-se ao mesmo objeto:

Conta c1 = new Conta(100);
Conta c2 = new Conta(100);
if (c1 != c2) {
    System.out.println("objetos referenciados são diferentes!");
}


    E, nesse caso, realmente são diferentes.

   Mas, e se fosse preciso comparar os atributos? Quais atributos ele deveria comparar? O Java por si só
não faz isso, mas existe um método na classe Object que pode ser reescrito para criarmos esse critério de
comparação. Esse método é o equals.

    O equals recebe um Object como argumento e deve verificar se ele mesmo é igual ao Object recebido para
retornar um boolean. Se você não reescrever esse método, o comportamento herdado é fazer um == com o
objeto recebido como argumento.

                                Capítulo 14 - O pacote java.lang - Métodos do java.lang.Object: equals e toString - Página 161


[PAGINA 174]
                                                         Material do Treinamento Java e Orientação a Objetos




public class Conta {
    private double saldo;
    // outros atributos...

      public Conta(double saldo) {
          this.saldo = saldo;
      }

      public boolean equals(Object object) {
          Conta outraConta = (Conta) object;
          if (this.saldo == outraConta.saldo) {
              return true;
          }
          return false;
      }

      public String toString() {
          return "Uma conta com valor: " + this.saldo;
      }
}


    Um exemplo clássico do uso do equals é para datas. Se você criar duas datas, isto é, dois objetos diferentes,
contendo 31/10/1979, ao comparar com o == receberá false, pois são referências para objetos diferentes. Seria
correto, então, reescrever este método, fazendo as comparações dos atributos, e o usuário passaria a invocar
equals em vez de comparar com ==.

   Você poderia criar um método com outro nome em vez de reescrever equals que recebe Object, mas ele é
importante pois muitas bibliotecas o chamam através do polimorfismo, como veremos no capítulo do java.util.

    O método hashCode() anda de mãos dadas com o método equals() e é de fundamental entendimento no
caso de você utilizar suas classes com estruturas de dados que usam tabelas de espalhamento. Também
falaremos dele no capítulo de java.util.


                Regras para a reescrita do método equals
            Pelo contrato definido pela classe Object devemos retornar false também no caso do objeto pas-
            sado não ser de tipo compatível com a sua classe. Então antes de fazer o casting devemos verificar
            isso, e para tal usamos a palavra chave instanceof, ou teríamos uma exception sendo lançada.
            Além disso, podemos resumir nosso equals de tal forma a não usar um if:

             public boolean equals(Object object) {

                   if (!(object instanceof Conta))
                       return false;
                   Conta outraConta = (Conta) object;
                   return this.saldo == outraConta.saldo;
            }




    14.6 - Integer e classes wrappers (box)
   Uma pergunta bem simples que surge na cabeça de todo programador ao aprender uma nova linguagem é:
“Como transformar um número em String e vice-versa?”.

                                             Capítulo 14 - O pacote java.lang - Integer e classes wrappers (box) - Página 162


[PAGINA 175]
                                                     Material do Treinamento Java e Orientação a Objetos




    Cuidado! Usamos aqui o termo “transformar” porém o que ocorre não é uma transformação entre os tipos,
e sim uma forma de conseguirmos uma String dado um int e vice-versa. O jeito mais simples de transformar
um número em String é concatená-lo da seguinte maneira:

int i = 100;
String s = "" + i;
System.out.println(s);

double d = 1.2;
String s2 = "" + d;
System.out.println(s2);


    Para formatar o número de uma maneira diferente, com vírgula e número de casas decimais devemos utilizar
outras classes de ajuda (NumberFormat, Formatter).

   Para transformar uma String em número, utilizamos as classes de ajuda para os tipos primitivos correspon-
dentes. Por exemplo, para transformar a String s em um número inteiro utilizamos o método estático da classe
Integer:


String s = "101";
int i = Integer.parseInt(s);


   As classes Double, Short, Long, Float etc contêm o mesmo tipo de método, como parseDouble e parseFloat
que retornam um double e float respectivamente.

    Essas classes também são muito utilizadas para fazer o wrapping (embrulho) de tipos primitivos como
objetos, pois referências e tipos primitivos são incompatíveis. Imagine que precisamos passar como argumento
um inteiro para o nosso guardador de objetos. Um inteiro não é um Object, como fazer?

int i = 5;
Integer x = new Integer(i);
guardador.adiciona(x);


   E, dado um Integer, podemos pegar o int que está dentro dele (desembrulhá-lo):

int i = 5;
Integer x = new Integer(i);
int numeroDeVolta = x.intValue();



 14.7 - Autoboxing no Java 5.0
   Esse processo de wrapping e unwrapping é entediante. O Java 5.0 em diante traz um recurso chamado de
autoboxing, que faz isso sozinho para você, custando legibilidade:

Integer x = 5;
int y = x;




                                                  Capítulo 14 - O pacote java.lang - Autoboxing no Java 5.0 - Página 163


[PAGINA 176]
                                                       Material do Treinamento Java e Orientação a Objetos




   No Java 1.4 esse código é inválido. No Java 5.0 em diante ele compila perfeitamente. É importante ressaltar
que isso não quer dizer que tipos primitivos e referências agora são a mesma coisa, isso é simplesmente um
“açúcar sintático” (syntax sugar ) para facilitar a codificação.

   Você pode fazer todos os tipos de operações matemáticas com os wrappers agora, porém corre o risco de
tomar um NullPointerException.

   Você pode fazer o autoboxing diretamente para Object também, possibilitando passar um tipo primitivo para
um método que receber Object como argumento:

Object o = 5;



 14.8 - java.lang.String
   String é uma classe em Java. Variáveis do tipo String guardam referências a objetos, e não um valor, como
acontece com os tipos primitivos.

   Aliás, podemos criar uma String utilizando o new:

String x = new String("fj11");
String y = new String("fj11");


   Criamos aqui, dois objetos diferentes. O que acontece quando comparamos essas duas referências utili-
zando o ==?

if (x == y) {
    System.out.println("referência para o mesmo objeto");
}
else {
    System.out.println("referências para objetos diferentes!");
}


  Temos aqui dois objetos diferentes! E, então, como faríamos para verificar se o conteúdo do objeto é o
mesmo? Utilizamos o método equals, que foi reescrito pela String, para fazer a comparação de char em char.

if (x.equals(y)) {
    System.out.println("consideramos iguais no critério de igualdade");
}
else {
    System.out.println("consideramos diferentes no critério de igualdade");
}


    Aqui, a comparação retorna verdadeiro. Por quê? Pois quem implementou a classe String decidiu que
este seria o melhor critério de comparação. Você pode descobrir os critérios de igualdade de cada classe pela
documentação.

    Podemos também concatenar Strings usando o +. Podemos concatenar Strings com qualquer outra coisa,
até mesmo objetos e números:



                                                          Capítulo 14 - O pacote java.lang - java.lang.String - Página 164


[PAGINA 177]
                                                     Material do Treinamento Java e Orientação a Objetos




int total = 5;
System.out.println("o total gasto é: " + total);


    O compilador utilizará os métodos apropriados da classe String e das classes wrappers para realizar tal
tarefa.

   A classe String conta também com um método split, que divide a String em um array de Strings, dado
determinado critério.

String frase = "java é demais";
String palavras[] = frase.split(" ");


   Se quisermos comparar duas Strings, utilizamos o método compareTo, que recebe uma String como ar-
gumento e devolve um inteiro indicando se a String vem antes, é igual ou vem depois da String recebida.
Se forem iguais, é devolvido 0; se for anterior à String do argumento, devolve um inteiro negativo; e, se for
posterior, um inteiro positivo.

    Fato importante: uma String é imutável. O java cria um pool de Strings para usar como cache e, se a
String não fosse imutável, mudando o valor de uma String afetaria todas as Strings de outras classes que
tivessem o mesmo valor.

   Repare no código abaixo:

String palavra = "fj11";
palavra.toUpperCase();
System.out.println(palavra);


   Pode parecer estranho, mas ele imprime “fj11” em minúsculo. Todo método que parece alterar o valor de
uma String, na verdade, cria uma nova String com as mudanças solicitadas e a retorna! Tanto que esse
método não é void. O código realmente útil ficaria assim:

String palavra = "fj11";
String outra = palavra.toUpperCase();
System.out.println(outra);


   Ou você pode eliminar a criação de outra variável temporária, se achar conveniente:

String palavra = "fj11";
palavra = palavra.toUpperCase();
System.out.println(palavra);


   Isso funciona da mesma forma para todos os métodos que parecem alterar o conteúdo de uma String.

   Se você ainda quiser trocar o número 1 para 2, faríamos:

String palavra = "fj11";
palavra = palavra.toUpperCase();
palavra = palavra.replace("1", "2");
System.out.println(palavra);


                                                         Capítulo 14 - O pacote java.lang - java.lang.String - Página 165


[PAGINA 178]
                                                      Material do Treinamento Java e Orientação a Objetos




   Ou ainda podemos concatenar as invocações de método, já que uma String é devolvida a cada invocação:

String palavra = "fj11";
palavra = palavra.toUpperCase().replace("1", "2");
System.out.println(palavra);


    O funcionamento do pool interno de Strings do Java tem uma série de detalhes e você pode encontrar mais
informações sobre isto na documentação da classe String e no seu método intern().


             Outros métodos da classe String
           Existem diversos métodos da classe String que são extremamente importantes. Recomendamos
           sempre consultar o javadoc relativo a essa classe para aprender cada vez mais sobre a mesma.
           Por exemplo, o método charAt(i), retorna o caractere existente na posição i da String, o método
           length retorna o número de caracteres na mesma e o método substring que recebe um int e
           devolve a SubString a partir da posição passada por aquele int.
           O indexOf recebe um char ou uma String e devolve o índice em que aparece pela primeira vez na
           String principal (há também o lastIndexOf que devolve o índice da última ocorrência).
           O toUpperCase e o toLowerCase devolvem uma nova String toda em maiúscula e toda em minúscula,
           respectivamente.
           A partir do Java 6, temos ainda o método isEmpty, que devolve true se a String for vazia ou false
           caso contrário.
           Alguns métodos úteis para buscas são o contains e o matches.
           Há muitos outros métodos, recomendamos que você sempre consulte o javadoc da classe.


             java.lang StringBuffer e StringBuilder
           Como a classe String é imutável, trabalhar com uma mesma String diversas vezes pode ter um
           efeito colateral: gerar inúmeras Strings temporárias. Isto prejudica a performance da aplicação
           consideravelmente.
           No caso de você trabalhar muito com a manipulação de uma mesma String (por exemplo, dentro de
           um laço), o ideal é utilizar a classe StringBuffer. A classe StringBuffer representa uma sequência
           de caracteres. Diferentemente da String, ela é mutável, e não possui aquele pool.
           A classe StringBuilder tem exatamente os mesmos métodos, com a diferença dela não ser thread-
           safe. Veremos sobre este conceito no capítulo de Threads.


 14.9 - java.lang.Math
   Na classe Math, existe uma série de métodos estáticos que fazem operações com números como, por
exemplo, arredondar(round), tirar o valor absoluto (abs), tirar a raiz(sqrt), calcular o seno(sin) e outros.

double d = 4.6;
long i = Math.round(d);

int x = -4;
int y = Math.abs(x);


   Consulte a documentação para ver a grande quantidade de métodos diferentes.


                                                          Capítulo 14 - O pacote java.lang - java.lang.Math - Página 166


[PAGINA 179]
                                                     Material do Treinamento Java e Orientação a Objetos




   No Java 5.0, podemos tirar proveito do import static aqui:

import static java.lang.Math.*;


   Isso elimina a necessidade de usar o nome da classe, sob o custo de legibilidade:

double d = 4.6;
long i = round(d);
int x = -4;
int y = abs(x);



 14.10 - Exercícios: java.lang
   Aqui faremos diversos testes, além de modificar a classe Conta. Você pode fazer todos esses exercícios
dentro do próprio projeto banco.

1) Teste os exemplos desse capítulo, para ver que uma String é imutável. Por exemplo:

   public class TestaString {


       public static void main(String[] args) {
           String s = "fj11";
           s.replaceAll("1", "2");
           System.out.println(s);
       }

   }


   Como fazer para ele imprimir fj22?

2) Como fazer para saber se uma String se encontra dentro de outra? E para tirar os espaços em branco de
   uma String? E para saber se uma String está vazia? E para saber quantos caracteres tem uma String?
   Tome como hábito sempre pesquisar o javadoc! Conhecer a API, aos poucos, é fundamental para que você
   não precise reescrever a roda!

3) Crie uma classe TestaInteger e vamos fazer comparações com Integers:

   Integer x1 = new Integer(10);

   Integer x2 = new Integer(10);

   if (x1 == x2) {
       System.out.println("igual");
   } else {
       System.out.println("diferente");
   }


   E se testarmos com o equals?
   O que podemos concluir? Como verificar se a classe Integer também reescreve o método toString?


                                                     Capítulo 14 - O pacote java.lang - Exercícios: java.lang - Página 167


[PAGINA 180]
                                                      Material do Treinamento Java e Orientação a Objetos




   A maioria das classes do java que são muito utilizadas terão seus métodos equals e toString reescritos
   convenientemente.
   Aproveite e faça um teste com o método estático parseInt, recebendo uma String válida e uma inválida (com
   caracteres alfabéticos), e veja o que acontece!

4) Utilize-se da documentação do Java e descubra de que classe é o objeto referenciado pelo atributo out da
   System.
   Repare que, com o devido import, poderíamos escrever:

   // falta a declaração da saída

   saida = System.out;
   saida.println("ola");


   A variável saida precisa ser declarada de que tipo? É isso que você precisa descobrir. Se você digitar esse
   código no Eclipse, ele vai te sugerir um quickfix e declarará a variável para você.
   Estudaremos essa misteriosa classe no capítulo a seguir.

5) Crie e imprima uma referência para Conta (ContaCorrente ou ContaPoupanca, no caso de sua Conta ser
   abstrata):

   Conta conta = new ContaCorrente():

   System.out.println(conta);


   O que acontece?

6) Reescreva o método toString da sua classe Conta fazendo com que uma mensagem mais propícia seja
   devolvida. Lembre-se de aproveitar dos recursos do Eclipse para isto: digitando apenas o começo do nome
   do método a ser reescrito e pressionando Ctrl+espaço, ele vai sugerir reescrever o método, poupando você
   do trabalho de escrever a assinatura do mesmo, e de cometer algum engano.

   public abstract class Conta {


       private double saldo;

       public String toString() {
           return "esse objeto é uma conta com saldo R$" + this.saldo;
       }

       // restante da classe

   }


   Agora imprima novamente uma referência a Conta. O que aconteceu?

7) Reescreva o método equals da classe Conta para que duas contas com o mesmo número de conta sejam
   consideradas iguais. Para isso, você vai precisar de um atributo numero. Esboço:

   abstract class Conta {

       private int numero;

       public boolean equals(Object obj) {

                                                     Capítulo 14 - O pacote java.lang - Exercícios: java.lang - Página 168


[PAGINA 181]
                                                     Material do Treinamento Java e Orientação a Objetos




            Conta outraConta = (Conta) obj;

            return this.numero == outraConta.numero;
        }

        // restante     , colocar getter e setter para numero, usando Eclipse!
    }

    Você pode usar o Ctrl+espaço do eclipse para escrever o esqueleto do método equals, basta digitar dentro
    da classe equ e pressionar Ctrl+espaço.
    Crie uma classe TestaComparacaoConta, e dentro do main compare duas instâncias de ContaCorrente com
    ==, depois com equals, sendo que as instâncias são diferentes mas possuem o mesmo numero de conta (use
    o setNumero).

 8) Um double não está sendo suficiente para guardar a quantidade de casas necessárias em uma aplicação.
    Preciso guardar um número decimal muito grande! O que poderia usar? (consulte a documentação, tente
    adivinhar onde você pode encontrar algo desse tipo pelos nomes dos pacotes, veja como é intuitivo).
    O double também tem problemas de precisão ao fazer contas, por causa de arredondamentos da aritmética
    de ponto flutuante definido pela IEEE 754:
    http://en.wikipedia.org/wiki/IEEE_754
    Ele não deve ser usado se você precisa realmente de muita precisão (casos que envolvam dinheiro, por
    exemplo).
    Lembre-se: no Java há muita coisa já pronta. Seja na biblioteca padrão, seja em bibliotecas open source
    que você pode encontrar pela internet.

 9) (opcional) Agora faça com que o equals da sua classe Conta também leve em consideração a String do
    nome do cliente a qual ela pertence. Se sua Conta não possuir o atributo nome, crie-o. Teste se o método
    criado está funcionando corretamente.
10) (opcional) Crie a classe GuardadorDeObjetos como visto nesse capítulo. Crie uma classe TestaGuardador
    e dentro do main crie uma ContaCorrente e adicine-a num GuardadorDeObjetos. Depois teste pegar essa
    referência como ContaPoupanca, usando casting. Repare na exception que é lançada:

    GuardadorDeObjetos guardador = new GuardadorDeObjetos();

    ContaCorrente cc = new ContaCorrente();
    guardador.adicionaObjeto(cc);

    // vai precisar do casting para compilar!
    // use Ctrl+1 para o Eclipse gerar para você
    ContaPoupanca cp = guardador.pega(0);

    Teste também o autoboxing do java 5.0, passando um inteiro para nosso guardador.

11) (opcional) Escreva um método que usa os métodos charAt e length de uma String para imprimir a mesma
    caractere a caractere, com cada caractere em uma linha diferente.

12) (opcional) Reescreva o método do exercício anterior, mas agora imprima a String de trás para a frente.
    Teste-a para “Socorram-me, subi no ônibus em Marrocos” e “Anotaram a data da maratona”.

13) (opcional) Dada uma frase, reescreva essa frase com as palavras na ordem invertida. “Socorram-me, subi
    no ônibus em Marrocos” deve retornar “Marrocos em ônibus no subi Soccoram-me,”. Utilize o método split
    da String para te auxiliar.

                                                     Capítulo 14 - O pacote java.lang - Exercícios: java.lang - Página 169


[PAGINA 182]
                                                       Material do Treinamento Java e Orientação a Objetos




14) (opcional) Pesquise a classe StringBuilder (ou StringBuffer no java 1.4). Ela é mutável. Por que usá-la em
    vez da String? Quando usá-la? Repare que ela tem um étodo reverse e outros bem úteis!


  14.11 - Desafio

 1) Converta uma String para um número sem usar as bibliotecas do java que já fazem isso. Isso é, uma String
    x = “762"
    deve gerar um int i = 762.
    Para ajudar, saiba que um char pode ser “transformado” em int com o mesmo valor numérico fazendo:

     char c = ’3’;

    int i = c - ’0’; // i vale 3!


    Aqui estamos nos aproveitando do conhecimento da tabela unicode: os números de 0 a 9 estão em sequen-
    cia! Você poderia usar o método estático Character.getNumericValue(char) em vez disso.


  14.12 - Discussão em aula: O que você precisa fazer em Java?
    Qual é a sua necessidade com o Java? Precisa fazer algoritmos de redes neurais? Gerar gráficos 3D?
 Relatórios em PDF? Gerar código de barra? Gerar boletos? Validar CPF? Mexer com um arquivo do excel?

     O instrutor vai mostrar que para a maioria absoluta das suas necessidade, alguém já fez uma biblioteca e a
 disponibilizou.




                                                                 Capítulo 14 - O pacote java.lang - Desafio - Página 170


[PAGINA 183]
                                                                                             C APÍTULO   15

Pacote java.io
                                   “A benevolência é sobretudo um vício do orgulho e não uma virtude da alma.”
                                                                 – Doantien Alphonse François (Marquês de Sade)

   Ao término desse capítulo, você será capaz de:

   • ler e escrever bytes, caracteres e Strings de/para a entrada e saída padrão;
   • ler e escrever bytes, caracteres e Strings de/para arquivos;
   • utilizar buffers para agilizar a leitura e escrita através de fluxos;
   • usar Scanner e PrintStream.

 15.1 - Conhecendo uma API
   Vamos passar, agora, a conhecer APIs do Java. java.io e java.util possuem as classes que você mais
comumente vai usar, não importando se seu aplicativo é desktop, web, ou mesmo para celulares.

    Apesar de ser importante conhecer nomes e métodos das classes mais utilizadas, o interessante aqui é
que você enxergue que todos os conceitos previamente estudados são aplicados a toda hora nas classes da
biblioteca padrão.

   Não se preocupe em decorar nomes. Atenha-se em entender como essas classes estão relacionadas
e como elas estão tirando proveito do uso de interfaces, polimorfismo, classes abstratas e encapsulamento.
Lembre-se de estar com a documentação (javadoc) aberta durante o contato com esses pacotes.

    Veremos também threads e sockets em capítulos posteriores, que ajudarão a condensar nosso conheci-
mento, tendo em vista que no exercício de sockets utilizaremos todos conceitos aprendidos, juntamente com as
várias APIs.


 15.2 - Orientação a objetos
   Assim como todo o resto das bibliotecas em Java, a parte de controle de entrada e saída de dados (co-
nhecido como io) é orientada a objetos e usa os principais conceitos mostrados até agora: interfaces, classes
abstratas e polimorfismo.

    A idéia atrás do polimorfismo no pacote java.io é de utilizar fluxos de entrada (InputStream) e de saída
(OutputStream) para toda e qualquer operação, seja ela relativa a um arquivo, a um campo blob do banco
de dados, a uma conexão remota via sockets, ou até mesmo às entrada e saída padrão de um programa
(normalmente o teclado e o console).

    As classes abstratas InputStream e OutputStream definem, respectivamente, o comportamento padrão dos
fluxos em Java: em um fluxo de entrada, é possível ler bytes e, no fluxo de saída, escrever bytes.

                                                         171


[PAGINA 184]
                                                             Material do Treinamento Java e Orientação a Objetos




    A grande vantagem dessa abstração pode ser mostrada em um método qualquer que utiliza um
OutputStream recebido como argumento para escrever em um fluxo de saída. Para onde o método está es-
crevendo? Não se sabe e não importa: quando o sistema precisar escrever em um arquivo ou em uma socket,
basta chamar o mesmo método, já que ele aceitar qualquer filha de OutputStream!


 15.3 - InputStream, InputStreamReader e BufferedReader
   Vamos ler um byte de um arquivo:

1 class TestaEntrada {
2     public static void main(String[] args) throws IOException {
3         InputStream is = new FileInputStream("arquivo.txt");
4         int b = is.read();
5     }
6 }


    A classe InputStream é abstrata e FileInputStream, uma de suas filhas concretas. Essa última recebe
uma String como argumento no construtor, que é o nome do arquivo a ser lido. Ela vai procurar o arquivo
no diretório em que o java foi invocado (no caso do Eclipse, vai ser a partir de dentro do diretório do projeto).
Alternativamente você pode usar um caminho absoluto.

    Quando trabalhamos com java.io, diversos métodos lançam IOException, que é uma exception do tipo
checked - o que nos obriga a tratá-la ou declará-la. Nos exemplos aqui, estamos declarando IOException
através da clausula throws do main apenas para facilitar o exemplo. Caso a exception ocorra, a JVM vai parar,
mostrando a stacktrace. Esta não é uma boa prática em uma aplicação real: trate suas exceptions para sua
aplicação poder abortar elegantemente.

   InputStream   tem     diversas       outras     filhas,       como    ObjectInputStream,           AudioInputStream,
ByteArrayInputStream, entre outras.

    Para recuperar um caractere, precisamos traduzir os bytes com o encoding dado para o respectivo código
unicode, isso pode usar um ou mais bytes. Escrever esse decodificador é muito complicado, quem faz isso por
você é a classe InputStreamReader.

1 class TestaEntrada {
2     public static void main(String[] args) throws IOException {
3         InputStream is = new FileInputStream("arquivo.txt");
4         InputStreamReader isr = new InputStreamReader(is);
5         int c = isr.read();
6     }
7 }


     O construtor de InputStreamReader pode receber o encoding a ser utilizado como parâmetro, se desejado,
tal como UTF-8 ou ISO-8859-1.

             Encodings
            Devido a grande quantidade de aplicativos internacionalizados de hoje em dia, é imprecindível que
            um bom programador entenda bem o que são os character encodings e o Unicode. O blog da
            Caelum possui um bom artigo a respeito:
            http://blog.caelum.com.br/2006/10/22/entendendo-unicode-e-os-character-encodings/

                                 Capítulo 15 - Pacote java.io - InputStream, InputStreamReader e BufferedReader - Página 172


[PAGINA 185]
                                                         Material do Treinamento Java e Orientação a Objetos




  InputStreamReader é filha da classe abstrata Reader, que possui diversas outras filhas - são classes que
manipulam chars.

    Apesar da classe abstrata Reader já ajudar no trabalho de manipulação de caracteres, ainda seria difícil
pegar uma String. A classe BufferedReader é um Reader que recebe outro Reader pelo construtor e concatena
os diversos chars para formar uma String através do método readLine:

1 class TestaEntrada {
2     public static void main(String[] args) throws IOException {
3         InputStream is = new FileInputStream("arquivo.txt");
4         InputStreamReader isr = new InputStreamReader(is);
5         BufferedReader br = new BufferedReader(isr);
6         String s = br.readLine();
7     }
8 }


   Como o próprio nome diz, essa classe lê do Reader por pedaços (usando o buffer) para evitar realizar muitas
chamadas ao sistema operacional. Você pode até configurar o tamanho do buffer pelo construtor.

   É essa a composição de classes que está acontecendo:




   Esse padrão de composição é bastante utilizado e conhecido. É o Decorator Pattern.

   Aqui, lemos apenas a primeira linha do arquivo. O método readLine devolve a linha que foi lida e muda o
cursor para a próxima linha. Caso ele chegue ao fim do Reader (no nosso caso, fim do arquivo), ele vai devolver
null. Então, com um simples laço, podemos ler o arquivo por inteiro:


 1 class TestaEntrada {
 2     public static void main(String[] args) throws IOException {
 3         InputStream is = new FileInputStream("arquivo.txt");
 4         InputStreamReader isr = new InputStreamReader(is);
 5         BufferedReader br = new BufferedReader(isr);
 6
 7         String s = br.readLine(); // primeira linha
 8
 9         while (s != null) {
10             System.out.println(s);
11             s = br.readLine();
12         }
13
14         br.close();
15     }
16 }




                                Capítulo 15 - Pacote java.io - InputStream, InputStreamReader e BufferedReader - Página 173


[PAGINA 186]
                                                   Material do Treinamento Java e Orientação a Objetos




 15.4 - Lendo Strings do teclado
  Com um passe de mágica, passamos a ler do teclado em vez de um arquivo, utilizando o System.in, que é
uma referência a um InputStream o qual, por sua vez, lê da entrada padrão.

 1 class TestaEntrada {
 2     public static void main(String[] args) throws IOException {
 3         InputStream is = System.in;
 4         InputStreamReader isr = new InputStreamReader(is);
 5         BufferedReader br = new BufferedReader(isr);
 6         String s = br.readLine();
 7
 8         while (s != null) {
 9             System.out.println(s);
10             s = br.readLine();
11         }
12     }
13 }


   Apenas modificamos a quem a variável is está se referindo. Podemos receber argumentos do tipo
InputStream e ter esse tipo de abstração: não importa exatamente de onde estamos lendo esse punhado
de bytes, desde que a gente receba a informação que estamos querendo. Como na figura:




    Repare que a ponta da direita poderia ser qualquer InputStream, seja ObjectInputStream,
AudioInputStream, ByteArrayInputStream, ou a nossa FileInputStream. Polimorfismo! Ou você mesmo pode
criar uma filha de InputStream, se desejar.

    Por isso é muito comum métodos receberem e retornarem InputStream, em vez de suas filhas específicas.
Com isso, elas desacoplam as informações e escondem a implementação, facilitando a mudança e manutenção
do código. Repare que isso vai ao encontro de tudo o que aprendemos durante os capítulos que apresentaram
classes abstratas, interfaces, polimorfismo e encapsulamento.


 15.5 - A analogia para a escrita: OutputStream
   Como você pode imaginar, escrever em um arquivo é o mesmo processo:




                                                   Capítulo 15 - Pacote java.io - Lendo Strings do teclado - Página 174


[PAGINA 187]
                                                          Material do Treinamento Java e Orientação a Objetos




 1 class TestaSaida {
 2     public static void main(String[] args) throws IOException {
 3         OutputStream os = new FileOutputStream("saida.txt");
 4         OutputStreamWriter osw = new OutputStreamWriter(os);
 5         BufferedWriter bw = new BufferedWriter(osw);
 6
 7         bw.write("caelum");
 8
 9         bw.close();
10     }
11 }


    Lembre-se de dar refresh (clique da direita no nome do projeto, refresh) no seu projeto do Eclipse para que o
arquivo criado apareça. O FileOutputStream pode receber um booleano como segundo parâmetro, para indicar
se você quer reescrever o arquivo ou manter o que já estava escrito (append).

   O método write do BufferedWriter não insere o(s) caractere(s) de quebra de linha. Para isso, você pode
chamar o método newLine.

             Fechando o arquivo
            É importante sempre fechar o arquivo. Você pode fazer isso chamando diretamente o método close
            do FileInputStream/OutputStream, ou ainda chamando o close do BufferedReader/Writer. Nesse
            último caso, o close será cascateado para os objetos os quais o BufferedReader/Writer utiliza para
            realizar a leitura/escrita, além dele fazer o flush dos buffers no caso da escrita.
            É comum que o close esteja dentro de um bloco finally. Se um arquivo for esquecido aberto e a
            referência para ele for perdida, ele será fechado pelo garbage collector, que veremos mais a frente,
            por causa do finalize. Mas não é bom você se prender a isso. Se você esquecer de fechar o
            arquivo, no caso de um programa minúsculo como esse, o programa vai terminar antes que o tal
            do garbage collector te ajude, resultando em um arquivo não escrito (os bytes ficaram no buffer do
            BufferedWriter).
            Problemas similares podem acontecer com leitores que não forem fechados.


 15.6 - Uma maneira mais fácil: Scanner e PrintStream
   A partir do Java 5, temos a classe java.util.Scanner, que facilita bastante o trabalho de ler de um
InputStream. Além disso, a classe PrintStream possui um construtor que já recebe o nome de um arquivo
como argumento. Dessa forma, a leitura do teclado com saída para um arquivo ficou muito simples:

Scanner s = new Scanner(System.in);
PrintStream ps = new PrintStream("arquivo.txt");
while (s.hasNextLine()) {

                                    Capítulo 15 - Pacote java.io - Uma maneira mais fácil: Scanner e PrintStream - Página 175


[PAGINA 188]
                                                            Material do Treinamento Java e Orientação a Objetos




      ps.println(s.nextLine());
}


   Nenhum dos métodos lança IOException: PrintStream lança FileNotFoundException se você o construir
passando uma String. Essa exceção é filha de IOException e indica que o arquivo não foi encontrado. O
Scanner considerará que chegou ao fim se uma IOException for lançada, mas o PrintStream simplesmente
engole exceptions desse tipo. Ambos possuem métodos para você verificar se algum problema ocorreu.

   A classe Scanner é do pacote java.util. Ela possui métodos muito úteis para trabalhar com Strings, em
especial, diversos métodos já preparados para pegar números e palavras já formatadas através de expressões
regulares. Fica fácil parsear um arquivo com qualquer formato dado.


                  System.out
                Como vimos no capítulo passado, o atributo out da classe System é do tipo PrintStream (e, portanto,
                é um OutputStream).


    15.7 - Um pouco mais...

     • Existem duas classes chamadas java.io.FileReader e java.io.FileWriter. Elas são atalhos para a
          leitura e escrita de arquivos.

     • O do { .. } while(condicao); é uma alternativa para se construir um laço. Pesquise-o e utilize-o no
          código para ler um arquivo, ele vai ficar mais sucinto (você nao precisará ler a primeira linha fora do laço).


    15.8 - Exercícios: Java I/O

1) Crie um projeto novo chamado teste-io.
     Crie um programa (simplesmente uma classe com um main) que leia da entrada padrão. Para isso, você vai
     precisar de um BufferedReader que leia do System.in da mesma forma como fizemos.
     Não digite esses nomes de classes complicados! Use o ctrl+espaço para te auxiliar, porque além de te
     ajudar com o nome, ele colocará o import no devido lugar.
     Cuidado que existe mais de uma classe chamada InputStream: queremos a do pacote java.io.

      1 public class TestaEntrada {

      2
      3        // está faltando o throws IOException!! Peça auxílio para o Eclipse!
      4
      5        public static void main(String[] args) {
      6            InputStream is = System.in;
      7            InputStreamReader isr = new InputStreamReader(is);
      8            BufferedReader br = new BufferedReader(isr);
      9
     10             String linha = br.readLine(); // primeira linha
     11
     12             while (linha != null) {
     13                 System.out.println(linha);
     14                 linha = br.readLine();

                                                                   Capítulo 15 - Pacote java.io - Um pouco mais... - Página 176


[PAGINA 189]
                                                       Material do Treinamento Java e Orientação a Objetos




   15             }
   16      }
   17 }


   O compilador vai reclamar que você não está tratando algumas exceções (como java.io.IOException).
   Utilize a cláusula throws para deixar “escapar” a exceção pelo seu main, ou use os devidos try/catch. Utilize
   o quick fix do Eclipse para isso (Ctrl + 1). Deixar todas as exceptions passarem desapercebidas não é uma
   boa prática! Você pode usar aqui, pois estamos focando apenas no aprendizado da utilização do java.io.
   Rode sua aplicação. Através da View Console você pode digitar algumas linhas para que seu programa as
   capture.



                EOF
               Quando rodar sua aplicação, para encerrar a entrada de dados do teclado, é necessário enviarmos
               um sinal de fim de stream. É o famoso EOF, End Of File.
               No Linux/Mac/Solaris/Unix você faz isso com o CONTROL+D. No Windows, use o CONTROL+Z.

2) Vamos ler de um arquivo, em vez do teclado. Antes, vamos criar o arquivo que será lido pelo programa:

   a) Clique com o botão direito em cima do seu projeto e selecione New -> File:




   b) Nesta tela, digite o nome do arquivo no lugar indicado:




                                                           Capítulo 15 - Pacote java.io - Exercícios: Java I/O - Página 177


[PAGINA 190]
                                                    Material do Treinamento Java e Orientação a Objetos




   c) Troque na classe TestaEntrada o System.in por um new FileInputStream:

      InputStream is = new FileInputStream("arquivo.txt");



3) (conceitual) Seu programa agora lê todas as linhas desse arquivo. Repare na utilização do polimorfismo.
   Como ambos são InputStream, isso faz com que eles se encaixem no InputStreamReader.

4) Repare que, no final, só usamos mesmo o BufferedReader. As referências para InputStream e para
   InputStreamReader são apenas utilizadas temporariamente. Portanto, é comum encontrarmos o seguinte
   código nesses casos:

   BufferedReader br = new BufferedReader(

                             new InputStreamReader(
                                 new FileInputStream("arquivo.txt")));

   String linha = br.readLine(); // primeira linha


   Claro que devemos evitar um código mais sucinto em vez de sacrificar legibilidade, mas este código em

                                                        Capítulo 15 - Pacote java.io - Exercícios: Java I/O - Página 178


[PAGINA 191]
                                                       Material do Treinamento Java e Orientação a Objetos




   particular é bem comum e aceitável. Faça a alteração no seu programa!

5) Utilize a classe Scanner do Java 5 para ler de um arquivo e colocar na tela. O código vai ficar incrivelmente
   pequeno.

       1 class EntradaDeUmArquivo {

    2       public static void main(String[] args) throws IOException {
    3           InputStream is = new FileInputStream("arquivo.txt");
    4
    5           Scanner entrada = new Scanner(is);
    6           while (entrada.hasNextLine()) {
    7               System.out.println(entrada.nextLine());
    8           }
    9
   10           is.close();
   11       }
   12 }


   Depois troque a variável is para que ela se refira ao System.in. Agora você está lendo do teclado!

6) (opcional) Altere seu programa para que ele leia do arquivo e, em vez de jogar na tela, jogue em um outro
   arquivo. Você vai precisar, além do código anterior para ler de um arquivo, do código para escrever em um
   arquivo. Para isso, você pode usar o BufferedWriter ou o PrintStream, sendo este último de mais fácil
   manipulação.
   Se for usar o BufferedWriter, fazemos assim parar abri-lo:

   OutputStream os = new FileOutputStream("saida.txt");

   OutputStreamWriter osw = new OutputStreamWriter(os);
   BufferedWriter bw = new BufferedWriter(osw);

   Agora, dentro do loop de leitura do teclado, você deve usar bw.write(x), onde x é a linha que você leu. Use
   bw.newLine() para pular de linha. Não se esqueça de, no término do loop, dar um bw.close(). Você pode
   seguir o modelo:

   while (entrada.hasNextLine()) {

         String linha = entrada.nextLine();
         bw.write(linha);
         bw.newLine();
   }

   bw.close();


   Após rodar seu programa, dê um refresh no seu projeto (clique da direita no nome do projeto, refresh) e veja
   que ele criou um arquivo saida.txt no diretório.

7) (opcional) Altere novamente o programa para ele virar um pequeno editor: lê do teclado e escreve em arquivo.
   Repare que a mudança a ser feita é mínima!

8) (opcional) A classe Scanner é muito poderosa! Consulte seu javadoc para saber sobre o delimiter e os
   outros métodos next.




                                                           Capítulo 15 - Pacote java.io - Exercícios: Java I/O - Página 179


[PAGINA 192]
                                                          Material do Treinamento Java e Orientação a Objetos




 15.9 - Discussão em aula: Design Patterns e o Template Method
    Aplicar bem os conceitos de orientação a objetos é sempre uma grande dúvida. Sempre queremos encap-
sular direito, favorecer a flexibilidade, desacoplar classes, escrever código elegante e de fácil manutenção. E
ouvimos falar que a Orientação a Objetos ajuda em tudo isso.

   Mas, onde usar herança de forma saudável? Como usar interfaces? Onde o polimorfismo me ajuda? Como
encapsular direito? Classes abstratas são usadas em que situações?

    Muitos anos atrás, grandes nomes do mundo da orientação a objetos perceberam que criar bons designs
orientados a objetos era um grande desafio para muitas pessoas. Perceberam que muitos problemas de OO
apareciam recorrentemente em vários projetos; e que as pessoas já tinham certas soluções para esses proble-
mas clássicos (nem sempre muito elegantes).

    O que fizeram foi criar soluções padrões para problemas comuns na orientação a objetos, e chamaram
isso de Design Patters, ou Padrões de Projeto. O conceito vinha da arquitetura onde era muito comum ter
esse tipo de solução. E, em 1994, ganhou grande popularidade na computação com o livro Design Patterns:
Elements of Reusable Object-Oriented Software, um catálogo com várias dessas soluções escrito por Erich
Gamma, Ralph Johnson, Richard Helm e John Vlissides (a Gangue dos Quatro, GoF).

   Design Patterns tornou-se referência absoluta no bom uso da orientação a objetos. Outros padrões surgiram
depois, em outras literaturas igualmente consagradas. O conhecimento dessas técnicas é imprencindível para
o bom programador.

   Discuta com o instrutor como Design Patterns ajudam a resolver problemas de modelagem em sis-
temas orientados a objetos. Veja como Design Patterns são aplicados em muitos lugares do próprio
Java.

   O instrutor comentará do Template Method e mostrará o código fonte do método read() da classe
java.io.InputStream:


 1 public int read(byte b[], int off, int len) throws IOException {
 2     if (b == null) {
 3        throw new NullPointerException();
 4     } else if (off < 0 || len < 0 || len > b.length - off) {
 5        throw new IndexOutOfBoundsException();
 6     } else if (len == 0) {
 7        return 0;
 8     }
 9
10     int c = read();
11     if (c == -1) {
12        return -1;
13     }
14
15     b[off] = (byte) c;
16
17     int i = 1;
18     try {
19        for (; i < len ; i++) {
20           c = read();
21           if (c == -1) {
22              break;
23           }


                           Capítulo 15 - Pacote java.io - Discussão em aula: Design Patterns e o Template Method - Página 180


[PAGINA 193]
                                                         Material do Treinamento Java e Orientação a Objetos




24             b[off + i] = (byte)c;
25          }
26       } catch (IOException ee) {
27       }
28       return i;
29   }


    Discuta em aula como esse método aplica conceitos importantes da orientação a objetos e promove
flexibilidade e extensibilidade.




                          Capítulo 15 - Pacote java.io - Discussão em aula: Design Patterns e o Template Method - Página 181


[PAGINA 194]
                                                                                         C APÍTULO   16

Collections framework
   “A amizade é um contrato segundo o qual nos comprometemos a prestar pequenos favores para que no-los
                                                                                 retribuam com grandes.”
                                                                     – Baron de la Brede et de Montesquieu


   Ao término desse capítulo, você será capaz de:

   • utilizar arrays, lists, sets ou maps dependendo da necessidade do programa;

   • iterar e ordenar listas e coleções;

   • usar mapas para inserção e busca de objetos.


 16.1 - Arrays são trabalhosos, utilizar estrutura de dados
   A utilização de arrays é complicada em muitos pontos:

   • não podemos redimensionar um array em Java;

   • é impossível buscar diretamente por um determinado elemento cujo índice não se sabe;

   • não conseguimos saber quantas posições do array já foram populadas sem criar, para isso, métodos
     auxiliares.




    Na figura acima, você pode ver um array que antes estava sendo completamente utilizado e que, depois,
teve um de seus elementos removidos.

   Supondo que os dados armazenados representem contas, o que acontece quando precisarmos inserir uma
nova conta no banco?

   Precisaremos procurar por um espaço vazio?

   Guardaremos em alguma estrutura de dados externa, as posições vazias?

   E se não houver espaço vazio? Teríamos de criar um array maior e copiar os dados do antigo para ele?

   Há mais questões: como posso saber quantas posições estão sendo usadas no array? Vou precisar sempre
percorrer o array inteiro para conseguir essa informação?

                                                    182


[PAGINA 195]
                                                        Material do Treinamento Java e Orientação a Objetos




   Além dessas dificuldades que os arrays apresentavam, faltava um conjunto robusto de classes para suprir a
necessidade de estruturas de dados básicas, como listas ligadas e tabelas de espalhamento.

   Com esses e outros objetivos em mente, a Sun criou um conjunto de classes e interfaces conhecido como
Collections Framework, que reside no pacote java.util desde o Java2 1.2.


             Collections
            A API do Collections é robusta e possui diversas classes que representam estruturas de dados
            avançadas.
            Por exemplo, não é necessário reinventar a roda e criar uma lista ligada, mas sim utilizar aquela
            que a Sun disponibilizou.


 16.2 - Listas: java.util.List
   Um primeiro recurso que a API de Collections traz são listas. Uma lista é uma coleção que permite
elementos duplicados e mantém uma ordenação específica entre os elementos.

   Em outras palavras, você tem a garantia de que, quando percorrer a lista, os elementos serão encontrados
em uma ordem pré-determinada, definida na hora da inserção dos mesmos.

   Ela resolve todos os problemas que levantamos em relação ao array (busca, remoção, tamanho “infinito”,...).
Esse código já está pronto!

    A API de Collections traz a interface java.util.List, que especifica o que uma classe deve ser capaz
de fazer para ser uma lista. Há diversas implementações disponíveis, cada uma com uma forma diferente de
representar uma lista.

    A implementação mais utilizada da interface List é a ArrayList, que trabalha com um array interno para
gerar uma lista. Portanto, ela é mais rápida na pesquisa do que sua concorrente, a LinkedList, que é mais
rápida na inserção e remoção de itens nas pontas.


             ArrayList não é um array!
            É comum confundirem uma ArrayList com um array, porém ela não é um array. O que ocorre é
            que, internamente, ela usa um array como estrutura para armazenar os dados, porém este atributo
            está propriamente encapsulado e você não tem como acessá-lo. Repare, também, que você não
            pode usar [] com uma ArrayList, nem acessar atributo length. Não há relação!


   Para criar um ArrayList, basta chamar o construtor:

ArrayList lista = new ArrayList();


   É sempre possível abstrair a lista a partir da interface List:

List lista = new ArrayList();


   Para criar uma lista de nomes (String), podemos fazer:



                                                      Capítulo 16 - Collections framework - Listas: java.util.List - Página 183


[PAGINA 196]
                                                       Material do Treinamento Java e Orientação a Objetos




List lista = new ArrayList();
lista.add("Manoel");
lista.add("Joaquim");
lista.add("Maria");


   A interface List possui dois métodos add, um que recebe o objeto a ser inserido e o coloca no final da lista,
e um segundo que permite adicionar o elemento em qualquer posição da mesma.

    Note que, em momento algum, dizemos qual é o tamanho da lista; podemos acrescentar quantos elementos
quisermos, que a lista cresce conforme for necessário.

   Toda lista (na verdade, toda Collection) trabalha do modo mais genérico possível. Isto é, não há uma
ArrayList específica para Strings, outra para Números, outra para Datas etc. Todos os métodos trabalham
com Object.

   Assim, é possível criar, por exemplo, uma lista de Contas Correntes:

ContaCorrente c1 = new ContaCorrente();
c1.deposita(100);

ContaCorrente c2 = new ContaCorrente();
c2.deposita(200);

ContaCorrente c3 = new ContaCorrente();
c3.deposita(300);

List contas = new ArrayList();
contas.add(c1);
contas.add(c3);
contas.add(c2);


   Para saber quantos elementos há na lista, podemos usar o método size():

System.out.println(contas.size());


    Há ainda um método get(int) que recebe como argumento o índice do elemento que se quer recuperar.
Através dele, podemos fazer um for para iterar na lista de contas:

for (int i = 0; i < contas.size(); i++) {
    contas.get(i); // código não muito útil....
}


    Mas como fazer para imprimir o saldo dessas contas? Podemos acessar o getSaldo() diretamente após
fazer contas.get(i)? Não podemos; lembre-se que toda lista trabalha sempre com Object. Assim, a referência
devolvida pelo get(i) é do tipo Object, sendo necessário o cast para ContaCorrente se quisermos acessar o
getSaldo():


for (int i = 0; i < contas.size(); i++) {
    ContaCorrente cc = (ContaCorrente) contas.get(i);
    System.out.println(cc.getSaldo());


                                                     Capítulo 16 - Collections framework - Listas: java.util.List - Página 184


[PAGINA 197]
                                                     Material do Treinamento Java e Orientação a Objetos




}
// note que a ordem dos elementos não é alterada


   Há ainda outros métodos como remove() que recebe um objeto que se deseja remover da lista; e
contains(), que recebe um objeto como argumento e devolve true ou false, indicando se o elemento está
ou não na lista.
   A interface List e algumas classes que a implementam podem ser vistas no diagrama UML a seguir:




             Acesso aleatório e percorrendo listas com get
           Algumas listas, como a ArrayList, têm acesso aleatório aos seus elementos: a busca por um
           elemento em uma determinada posição é feita de maneira imediata, sem que a lista inteira seja
           percorrida (que chamamos de acesso sequencial).
           Neste caso, o acesso através do método get(int) e é muito rápido. Caso contrário, percorrer uma
           lista usando um for como esse que acabamos de ver, pode ser desastroso. Ao percorrermos uma
           lista, devemos usar sempre um Iterator ou enhanced for, como veremos.

   Uma lista é uma excelente alternativa a um array comum, já que temos todos os benefícios de arrays, sem
a necessidade de tomar cuidado com remoções, falta de espaço etc.
    A outra implementação muito usada (LinkedList), fornece métodos adicionais para obter e remover o pri-
meiro e último elemento da lista. Ela também tem o funcionamento interno diferente, o que pode impactar
performance, como veremos durante os exercícios no final do capítulo.

             Vector
           Outra implementação é a tradicional classe Vector, presente desde o Java 1.0, que foi adaptada
           para uso com o framework de Collections, com a inclusão de novos métodos.
           Ela deve ser tratada com cuidado pois lida de uma maneira diferente com processos correndo em
           paralelo e será mais lenta que uma ArrayList quando não houver acesso simultâneo aos dados.

                                                   Capítulo 16 - Collections framework - Listas: java.util.List - Página 185


[PAGINA 198]
                                                        Material do Treinamento Java e Orientação a Objetos




 16.3 - Listas no Java 5.0 com Generics
   Em qualquer lista, é possível colocar qualquer Object. Com isso, é possível misturar objetos:

ContaCorrente cc = new ContaCorrente();

List lista = new ArrayList();
lista.add("Uma string");
lista.add(cc);
...


    Mas e depois, na hora de recuperar esses objetos? Como o método get devolve um Object, precisamos
fazer o cast. Mas com uma lista com vários objetos de tipos diferentes, isso pode não ser tão simples...

   Geralmente, não nos interessa uma lista com vários tipos de objetos misturados; no dia-a-dia, usamos listas
como aquela de contas correntes. No Java 5.0, podemos usar o recurso de Generics para restringir as listas a
um determinado tipo de objetos (e não qualquer Object):

List<ContaCorrente> contas = new ArrayList<ContaCorrente>();
contas.add(c1);
contas.add(c3);
contas.add(c2);


    Repare no uso de um parâmetro ao lado de List e ArrayList: ele indica que nossa lista foi criada para
trabalhar exclusivamente com objetos do tipo ContaCorrente. Isso nos traz uma segurança em tempo de com-
pilação:

contas.add("uma string"); // isso não compila mais!!


   O uso de Generics também elimina a necessidade de casting, já que, seguramente, todos os objetos inseri-
dos na lista serão do tipo ContaCorrente:

for(int i = 0; i < contas.size(); i++) {
    ContaCorrente cc = contas.get(i); // sem casting!
    System.out.println(cc.getSaldo());
}



 16.4 - A importância das interfaces nas coleções
    Vale ressaltar a importância do uso da interface List: quando desenvolvemos, procuramos sempre nos
referir a ela, e não às implementações específicas. Por exemplo, se temos um método que vai buscar uma série
de contas no banco de dados, poderíamos fazer assim:

class Agencia {
    public ArrayList<Conta> buscaTodasContas() {
        ArrayList<Conta> contas = new ArrayList<Conta>();

         // para cada conta do banco de dados, contas.add

                                         Capítulo 16 - Collections framework - Listas no Java 5.0 com Generics - Página 186


[PAGINA 199]
                                                      Material do Treinamento Java e Orientação a Objetos




          return contas;
      }
}


    Porém, para que precisamos retornar a referência específica a uma ArrayList? Para que ser tão específico?
Dessa maneira, o dia que optarmos por devolver uma LinkedList em vez de ArrayList, as pessoas que estão
usando o método buscaTodasContas poderão ter problemas, pois estavam fazendo referência a uma ArrayList.
O ideal é sempre trabalhar com a interface mais genérica possível:

class Agencia {

      // modificacao apenas no retorno:
      public List<Conta> buscaTodasContas() {
          ArrayList<Conta> contas = new ArrayList<Conta>();

          // para cada conta do banco de dados, contas.add

          return contas;
      }
}


     É o mesmo caso de preferir referenciar aos objetos com InputStream como fizemos no capítulo passado.

   Assim como no retorno, é boa prática trabalhar com a interface em todos os lugares possíveis: métodos que
precisam receber uma lista de objetos têm List como parâmetro em vez de uma implementação em específico
como ArrayList, deixando o método mais flexível:

class Agencia {

      public void atualizaContas(List<Conta> contas) {
          // ...
      }
}


   Também declaramos atributos como List em vez de nos comprometer como uma ou outra implementação.
Dessa forma obtemos um baixo acoplamento: podemos trocar a implementação, já que estamos programando
para a interface! Por exemplo:

class Empresa {

      private List<Funcionario> empregados = new ArrayList<Funcionario>();

      // ...
}



    16.5 - Ordenação: Collections.sort
   Vimos anteriormente que as listas são percorridas de maneira pré-determinada de acordo com a inclusão
dos itens. Mas, muitas vezes, queremos percorrer a nossa lista de maneira ordenada.

                                            Capítulo 16 - Collections framework - Ordenação: Collections.sort - Página 187


[PAGINA 200]
                                                       Material do Treinamento Java e Orientação a Objetos




   A classe Collections traz um método estático sort que recebe um List como argumento e o ordena por
ordem crescente. Por exemplo:

List lista = new ArrayList();
lista.add("Sérgio");
lista.add("Paulo");
lista.add("Guilherme");

System.out.println(lista); //repare que o toString de ArrayList foi sobrescrito!

Collections.sort(lista);

System.out.println(lista);


    Ao testar o exemplo acima, você observará que, primeiro, a lista é impressa na ordem de inserção e, depois
de invocar o sort, ela é impressa em ordem alfabética.

   Mas toda lista em Java pode ser de qualquer tipo de objeto, por exemplo, ContaCorrente. E se quisermos
ordenar uma lista de ContaCorrente? Em que ordem a classe Collections ordenará? Pelo saldo? Pelo nome
do correntista?

ContaCorrente c1 = new ContaCorrente();
c1.deposita(500);

ContaCorrente c2 = new ContaCorrente();
c2.deposita(200);

ContaCorrente c3 = new ContaCorrente();
c3.deposita(150);

List<ContaCorrente> contas = new ArrayList<ContaCorrente>();
contas.add(c1);
contas.add(c3);
contas.add(c2);

Collections.sort(contas); // qual seria o critério para esta ordenação?


    Sempre que falamos em ordenação, precisamos pensar em um critério de ordenação, uma forma de
determinar qual elemento vem antes de qual. É necessário instruir o sort sobre como comparar nossas
ContaCorrente a fim de determinar uma ordem na lista. Para isto, o método sort necessita que todos seus
objetos da lista sejam comparáveis e possuam um método que se compara com outra ContaCorrente. Como é
que o método sort terá a garantia de que a sua classe possui esse método? Isso será feito, novamente, através
de um contrato, de uma interface!

    Vamos fazer com que os elementos da nossa coleção implementem a interface java.lang.Comparable, que
define o método int compareTo(Object). Este método deve retornar zero, se o objeto comparado for igual a
este objeto, um número negativo, se este objeto for menor que o objeto dado, e um número positivo, se este
objeto for maior que o objeto dado.

   Para ordenar as ContaCorrentes por saldo, basta implementar o Comparable:

public class ContaCorrente extends Conta implements Comparable<ContaCorrente> {


                                             Capítulo 16 - Collections framework - Ordenação: Collections.sort - Página 188


[PAGINA 201]
                                                       Material do Treinamento Java e Orientação a Objetos




    // ... todo o codigo anterior fica aqui

    public int compareTo(ContaCorrente outra) {

        if (this.saldo < outra.saldo) {
          return -1;
        }

        if (this.saldo > outra.saldo) {
          return 1;
        }

        return 0;
    }
}


    Com o código anterior, nossa classe tornou-se “comparável": dados dois objetos da classe, conseguimos
dizer se um objeto é maior, menor ou igual ao outro, segundo algum critério por nós definido. No nosso caso, a
comparação será feita baseando-se no saldo da conta.

    Repare que o critério de ordenação é totalmente aberto, definido pelo programador. Se quisermos orde-
nar por outro atributo (ou até por uma combinação de atributos), basta modificar a implementação do método
compareTo na classe.

    Agora sim, quando chamarmos o método sort de Collections, ele saberá como fazer a ordenação da lista;
ele usará o critério que definimos no método compareTo.

    Mas, e o exemplo anterior, com uma lista de Strings? Por que a ordenação funcionou, naquele caso, sem
precisarmos fazer nada? Simples: quem escreveu a classe String (lembre que ela é uma classe como qualquer
outras) implementou a interface Comparable e o método compareTo para Strings, fazendo comparação em ordem
alfabética. (Consulte a documentação da classe String e veja o método compareTo lá). O mesmo acontece com
outras classes como Integer, BigDecimal, Date, entre outras.


             Definindo outros critérios de ordenação
            É possível definir outros critérios de ordenação usando um objeto do tipo Comparator. Existe um
            método sort em Collections que recebe, além da List, um Comparator definindo um critério de
            ordenação específico. É possível ter vários Comparators com critérios diferentes para usar quando
            for necessário.




                                             Capítulo 16 - Collections framework - Ordenação: Collections.sort - Página 189


[PAGINA 202]
                                                        Material do Treinamento Java e Orientação a Objetos




             Outros métodos da classe Collections
            A classe Collections traz uma grande quantidade de métodos estáticos úteis na manipulação de
            coleções.

               • binarySearch(List, Object): Realiza uma busca binária por determinado elemento na lista
                  ordenada e retorna sua posição ou um número negativo, caso não encontrado.

               • max(Collection): Retorna o maior elemento da coleção.

               • min(Collection): Retorna o menor elemento da coleção.

               • reverse(List): Inverte a lista.

               • ...e muitos outros. Consulte a documentação para ver outros metódos.

            Existe uma classe análoga, a java.util.Arrays, que faz operações similares com arrays.
            É importante conhecê-las para evitar escrever código já existente.


 16.6 - Exercícios: Ordenação

1) Abra sua classe Conta e veja se ela possui o atributo numero. Se não possuir, adicione-o:

   private int numero;



   E gere o getter e o setter pelo Eclipse, caso necessário.

2) Faça sua classe ContaPoupanca implementar a interface Comparable<ContaPoupanca>. Utilize o critério de
   ordenar pelo número da conta ou pelo seu saldo (como visto no código deste capítulo).

   public class ContaPoupanca extends Conta implements Comparable<ContaPoupanca>{



   Repare que o Eclipse prontamente lhe oferecerá um quickfix, oferecendo a criação do esqueleto dos métodos
   definidos na interface Comparable:




   Agora deixe o seu método compareTo parecido com este:

   public class ContaPoupanca extends Conta

                implements Comparable<ContaPoupanca> {


                                                   Capítulo 16 - Collections framework - Exercícios: Ordenação - Página 190


[PAGINA 203]
                                                    Material do Treinamento Java e Orientação a Objetos




      // ... todo o codigo anterior fica aqui

      public int compareTo(ContaPoupanca o) {
          if (this.getNumero() < o.getNumero()) {
              return -1;
          }
          if (this.getNumero() > o.getNumero()) {
              return 1;
          }
          return 0;
      }
  }


           Outra implementação...
          O que acha da implementação abaixo?

           public int compareTo(ContaPoupanca outra) {

                     return this.getNumero() - outra.getNumero();
          }




3) Crie uma classe TestaOrdenacao, onde você vai instanciar diversas contas e adicioná-las a uma
   List<ContaPoupanca>. Use o Collections.sort() nessa lista:

   public class TestaOrdenacao {


      public static void main(String[] args) {

          List<ContaPoupanca> contas = new ArrayList<ContaPoupanca>();

          ContaPoupanca c1 = new ContaPoupanca();
          c1.setNumero(1973);
          contas.add(c1);

          ContaPoupanca c2 = new ContaPoupanca();
          c2.setNumero(1462);
          contas.add(c2);

          ContaPoupanca c3 = new ContaPoupanca();
          c3.setNumero(1854);
          contas.add(c3);

          Collections.sort(contas);
      }
  }

  Faça um laço para imprimir todos os números das contas na lista já ordenada:

   for (int i = 0; i < contas.size(); i++) {

      Conta atual = contas.get(i);

                                               Capítulo 16 - Collections framework - Exercícios: Ordenação - Página 191


[PAGINA 204]
                                                      Material do Treinamento Java e Orientação a Objetos




       System.out.println("numero: " + atual.getNumero());
   }


   Atenção especial: repare que escrevemos um método compareTo em nossa classe e nosso código nunca
   o invoca!! Isto é muito comum. Reescrevemos (ou implementamos) um método e quem o invocará será um
   outro conjunto de classes (nesse caso, quem está chamando o compareTo é o Collections.sort, que o usa
   como base para o algoritmo de ordenação). Isso cria um sistema extremamente coeso e, ao mesmo tempo,
   com baixo acoplamento: a classe Collections nunca imaginou que ordenaria objetos do tipo ContaPoupanca,
   mas já que eles são Comparable, o seu método sort está satisfeito.
   Você poderia escrever o for acima de uma maneira mais sucinta:

   for (int i = 0; i < contas.size(); i++) {

       System.out.println("numero: " + contas.get(i).getNumero());
   }


4) (opcional) Se preferir, insira novas contas através de um laço (for). Adivinhe o nome da classe para colocar
   saldos aleatórios? Random. Do pacote java.util. Consulte sua documentação para usá-la (utilize o método
   nextInt() passando o numero maximo a ser sorteado).

5) O que teria acontecido se a classe ContaPoupanca não implementasse Comparable<ContaPoupanca> mas
   tivesse o método compareTo?
   Faça um teste: remova temporariamente a sentença implements Comparable<ContaPoupanca>, não remova
   o método compareTo e veja o que acontece. Basta ter o método, sem assinar a interface?

6) Utilize uma LinkedList em vez de ArrayList:

   List<ContaPoupanca> contas = new LinkedList<ContaPoupanca>();



   Precisamos alterar mais algum código para que essa substituição funcione? Rode o programa. Alguma
   diferença?

7) Como posso inverter a ordem de uma lista? Como posso embaralhar todos os elementos de uma lista?
   Como posso rotacionar os elementos de uma lista?
   Investigue a documentação da classe Collections dentro do pacote java.util.

8) (opcional) Imprima a referência para essa lista. Repare que o toString de uma ArrayList/LinkedList é
   reescrito:

   System.out.println(contas);



9) (opcional) Mude o critério de comparação da sua ContaPoupanca. Adicione um atributo nomeDoCliente na
   sua classe (caso ainda não exista algo semelhante) e tente mudar o compareTo para que uma lista de
   ContaPoupanca seja ordenada alfabeticamente pelo atributo nomeDoCliente.
   Teste a ordenação.




                                                 Capítulo 16 - Collections framework - Exercícios: Ordenação - Página 192


[PAGINA 205]
                                                      Material do Treinamento Java e Orientação a Objetos




 16.7 - Conjunto: java.util.Set
   Um conjunto (Set) funciona de forma análoga aos conjuntos da matemática, ele é uma coleção que não
permite elementos duplicados.

   Outra característica fundamental dele é o fato de que a ordem em que os elementos são armazenados
pode não ser a ordem na qual eles foram inseridos no conjunto. A interface não define como deve ser este
comportamento. Tal ordem varia de implementação para implementação.




   Um conjunto é representado pela interface Set e tem como suas principais implementações as classes
HashSet, LinkedHashSet e TreeSet.

   O código a seguir cria um conjunto e adiciona diversos elementos, e alguns repetidos:

Set<String> conjunto = new HashSet<String>();

conjunto.add("paulo");


                                                 Capítulo 16 - Collections framework - Conjunto: java.util.Set - Página 193


[PAGINA 206]
                                                         Material do Treinamento Java e Orientação a Objetos




conjunto.add("guilherme");
conjunto.add("thadeu");
conjunto.add("cosen");
conjunto.add("sergio");
conjunto.add("guilherme"); // repetido!

// imprime na tela todos os elementos
System.out.println(conjunto);


   Aqui, o segundo guilherme não será adicionado e o método add lhe retornará false.

   O uso de um Set pode parecer desvantajoso, já que ele não armazena a ordem, e não aceita elementos
repetidos. Não há métodos que trabalham com índices, como o get(int) que as listas possuem. A grande
vantagem do Set é que existem implementações, como a HashSet, que possui uma performance incomparável
com as Lists quando usado para pesquisa (método contains por exemplo). Veremos essa enorme diferença
durante os exercícios.

             Ordem de um Set
           Seria possível usar uma outra implementação de conjuntos, como um TreeSet, que insere os
           elementos de tal forma que, quando forem percorridos, eles apareçam em uma ordem defi-
           nida pelo método de comparação entre seus elementos. Esse método é definido pela interface
           java.lang.Comparable. Ou, ainda, pode se passar um Comparator para seu construtor.
           Já o LinkedHashSet matém a ordem de inserção dos elementos.


   Antes do Java 5, não podíamos utilizar generics, e usavamos o Set de forma que ele trabalhava com Object,
havendo necessidade de castings.


 16.8 - Principais interfaces: java.util.Collection
   As coleções têm como base a interface Collection, que define métodos para adicionar e remover um
elemento, e verificar se ele está na coleção, entre outras operações, como mostra a tabela a seguir:




   Uma coleção pode implementar diretamente a interface Collection, porém normalmente se usa uma das
duas subinterfaces mais famosas: justamente Set e List.

   A interface Set, como previamente vista, define um conjunto de elementos únicos enquanto a interface List
permite elementos duplicados, além de manter a ordem a qual eles foram adicionados.

                                  Capítulo 16 - Collections framework - Principais interfaces: java.util.Collection - Página 194


[PAGINA 207]
                                                      Material do Treinamento Java e Orientação a Objetos




     A busca em um Set pode ser mais rápida do que em um objeto do tipo List, pois diversas implementações
utilizam-se de tabelas de espalhamento (hash tables), realizando a busca para tempo linear (O(1)).

   A interface Map faz parte do framework, mas não estende Collection. (veremos Map mais adiante).




   No Java 5, temos outra interface filha de Collection: a Queue, que define métodos de entrada e de saída
e cujo critério será definido pela sua implementação (por exemplo LIFO, FIFO ou ainda um heap onde cada
elemento possui sua chave de prioridade).


 16.9 - Percorrendo coleções no Java 5
    Como percorrer os elementos de uma coleção? Se for uma lista, podemos sempre utilizar um laço for,
invocando o método get para cada elemento. Mas e se a coleção não permitir indexação?

   Por exemplo, um Set não possui um método para pegar o primeiro, o segundo ou o quinto elemento do
conjunto, já que um conjunto não possui o conceito de “ordem”

   Podemos usar o enhanced-for (o “foreach”) do Java 5 para percorrer qualquer Collection sem nos preo-
cupar com essas coisas. Vimos antes o uso do for do Java 5 em listas, veja agora seu uso em um Set:

 1 Set conjunto = new HashSet();
 2
 3 conjunto.add("item 1");
 4 conjunto.add("item 2");
 5 conjunto.add("item 3");
 6
 7 // retorna o iterator
 8 for (Object elemento : conjunto) {
 9     String palavra = (String) elemento;
10     System.out.println(palavra);

                                        Capítulo 16 - Collections framework - Percorrendo coleções no Java 5 - Página 195


[PAGINA 208]
                                                             Material do Treinamento Java e Orientação a Objetos




11 }


    O Java vai usar o iterator da Collection dada para percorrer a coleção. Se você já estiver usando uma
coleção parametrizada, o for pode ser feito utilizando um tipo mais específico:

 1 Set<String> conjunto = new HashSet<String>();
 2
 3 conjunto.add("item 1");
 4 conjunto.add("item 2");
 5 conjunto.add("item 3");
 6
 7 // retorna o iterator
 8 for (String palavra : conjunto) {
 9     System.out.println(palavra);
10 }


   Em que ordem os elementos serão acessados?

   Numa lista, os elementos aparecerão de acordo com o índice em que foram inseridos, isto é, de acordo com
o que foi pré-determinado. Em um conjunto, a ordem depende da implementação da interface Set: você muitas
vezes não vai saber ao certo em que ordem os objetos serão percorridos.

   Por que o Set é, então, tão importante e usado?

    Para perceber se um item já existe em uma lista, é muito mais rápido usar algumas implementações de Set
do que um List, e os TreeSets já vêm ordenados de acordo com as características que desejarmos! Sempre
considere usar um Set se não houver a necessidade de guardar os elementos em determinada ordem e buscá-
los através de um índice.

     No eclipse, você pode escrever foreach e dar ctrl+espaço, que ele vai gerar o esqueleto desse enhanced
for! Muito útil!


 16.10 - Para saber mais: Iterando sobre coleções com java.util.Iterator
    Antes do Java 5 introduzir o novo enhanced-for, iterações em coleções eram feitas com o Iterator. Toda co-
leção fornece acesso a um iterator, um objeto que implementa a interface Iterator, que conhece internamente
a coleção e dá acesso a todos os seus elementos, como a figura abaixo mostra.




                Capítulo 16 - Collections framework - Para saber mais: Iterando sobre coleções com java.util.Iterator - Página 196


[PAGINA 209]
                                                             Material do Treinamento Java e Orientação a Objetos




   Ainda hoje (depois do Java 5) podemos usar o Iterator, mas o mais comum é usar o enhanced-for. E, na
verdade, o enhanced-for é apenas um açúcar sintático que usa iterator por trás dos panos.

   Primeiro criamos um Iterator que entra na coleção.

   A cada chamada do método next, o Iterator retorna o próximo objeto do conjunto.

   Um iterator pode ser obtido com o método iterator() de Collection, por exemplo:

Iterator i = lista.iterator();


    A interface Iterator possui dois métodos principais: hasNext() (com retorno booleano), indica se ainda
existe um elemento a ser percorrido; next(), retorna o próximo objeto.

   Voltando ao exemplo do conjunto de strings, vamos percorrer o conjunto:

 1 // Usando sintaxe de Java 1.4:
 2
 3 Set conjunto = new HashSet();
 4 conjunto.add("item 1");
 5 conjunto.add("item 2");
 6 conjunto.add("item 3");
 7
 8 // retorna o iterator
 9 Iterator i = conjunto.iterator();
10 while (i.hasNext()) {
11
12     // recebe a palavra
13     Object elemento = i.next();
14     String palavra = (String) elemento;
15
16     System.out.println(palavra);
17 }


   O while anterior só termina quando todos os elementos do conjunto forem percorridos, isto é, quando o
método hasNext mencionar que não existem mais itens.


             ListIterator
           Uma lista fornece, além de acesso a um Iterator, um ListIterator, que oferece recursos adicio-
           nais, específicos para listas.
           Usando o ListIterator, você pode, por exemplo, adicionar um elemento na lista ou voltar para o
           elemento que foi “iterado” anteriormente.


             Usar Iterator em Java 5
           O Iterator pode sim ainda ser útil no Java 5. Além de iterar na coleção como faz o enhanced-for, o
           iterator consegue remover elementos da coleção durante a iteração.
           Além disso, no Java 5, o Iterator foi parametrizado e usa generics, facilitando castings e evitando
           erros.




                Capítulo 16 - Collections framework - Para saber mais: Iterando sobre coleções com java.util.Iterator - Página 197


[PAGINA 210]
                                                    Material do Treinamento Java e Orientação a Objetos




 16.11 - Mapas - java.util.Map

    Um mapa é composto por um conjunto de associações entre um objeto chave a um objeto valor. É equiva-
lente ao conceito de dicionário, usado em várias linguagens. Algumas linguagens, como Perl ou PHP, possuem
suporte nativo a mapas, onde são conhecidos como matrizes associativas.

   java.util.Map é um mapa, pois é possível usá-lo para mapear uma chave, por exemplo: mapeie o valor
“Caelum” à chave “escola”, ou mapeie “Rua Vergueiro” à chave “rua”.




   O método put(Object, Object) da interface Map recebe a chave e o valor de uma nova associação. Para
saber o que está associado a um determinado objeto-chave, passa-se esse objeto no método get(Object).
Sem dúvida essas são as duas operações principais e mais frequentes realizadas sobre um mapa.

   Observe o exemplo: criamos duas contas correntes e as colocamos em um mapa associando-as aos seus
donos.

ContaCorrente c1 = new ContaCorrente();
c1.deposita(10000);

ContaCorrente c2 = new ContaCorrente();
c2.deposita(3000);

// cria o mapa
Map mapaDeContas = new HashMap();

// adiciona duas chaves e seus valores
mapaDeContas.put("diretor", c1);
mapaDeContas.put("gerente", c2);

// qual é a conta associada ao "diretor"?
Object elemento = mapaDeContas.get("diretor");

ContaCorrente contaDoDiretor = (ContaCorrente) elemento;
System.out.println(contaDoDiretor.getSaldo());



                                                Capítulo 16 - Collections framework - Mapas - java.util.Map - Página 198


[PAGINA 211]
                                                     Material do Treinamento Java e Orientação a Objetos




    Um mapa é muito usado para “indexar” objetos de acordo com determinado critério, para podermos busca-
los rapidamente através desse critério. Costuma aparecer juntamente com outras coleções, para poder realizar
essas buscas!

    Ele, assim como as coleções, trabalha diretamente com Objects (tanto na chave quanto no valor), o que
torna necessário o casting no momento que recuperar elementos.

   Suas principais implementações são o HashMap, o TreeMap e o Hashtable.

   Apesar do mapa fazer parte do framework, ele não estende a interface Collection, por ter um comporta-
mento bem diferente. Porém, as coleções internas de um mapa (a de chaves e a de valores, ver Figura 7) são
acessíveis por métodos definidos na interface Map.




   O método keySet() retorna um Set com as chaves daquele mapa e o método values() retorna a Collection
com todos os valores que foram associados a alguma das chaves.


Mapas no Java 5.0

   Assim como as coleções, um mapa no Java 5.0 é parametrizado. O interessante é que ele recebe dois
parâmetros: a chave e o valor:

 1 ContaCorrente c1 = new ContaCorrente();
 2 c1.deposita(10000);
 3
 4 ContaCorrente c2 = new ContaCorrente();
 5 c2.deposita(3000);

                                                 Capítulo 16 - Collections framework - Mapas - java.util.Map - Página 199


[PAGINA 212]
                                                      Material do Treinamento Java e Orientação a Objetos




 6
 7 // cria o mapa
 8 Map<String, ContaCorrente> mapaDeContas = new HashMap<String, ContaCorrente>();
 9
10 // adiciona duas chaves e seus valores
11 mapaDeContas.put("diretor", c1);
12 mapaDeContas.put("gerente", c2);
13
14 // qual a conta do diretor? (sem casting!)
15 ContaCorrente contaDoDiretor = mapaDeContas.get("diretor");


    Aqui, como no caso da Lista, se você tentar colocar algo diferente de String na chave e ContaCorrente no
valor, vai ter um erro de compilação.


 16.12 - Para saber mais: Properties
   Um mapa importante é a tradicional classe Properties, que mapeia strings e é muito utilizada para a confi-
guração de aplicações.

    A Properties possui, também, métodos para ler e gravar o mapeamento com base em um arquivo texto,
facilitando muito a sua persistência.

Properties config = new Properties();

config.setProperty("database.login", "scott");
config.setProperty("database.password", "tiger");
config.setProperty("database.url","jdbc:mysql:/localhost/teste");

// muitas linhas depois...

String login = config.getProperty("database.login");
String password = config.getProperty("database.password");
String url = config.getProperty("database.url");
DriverManager.getConnection(url, login, password);


    Repare que não houve a necessidade do casting para String no momento de recuperar os objetos asso-
ciados. Isto porque a classe Properties foi desenhada com o propósito de trabalhar com a associação entre
Strings.


 16.13 - Para saber mais: Equals e HashCode
   Muitas das coleções do java guardam os objetos dentro de tabelas de hash. Essas tabelas são utilizadas
para que a pesquisa de um objeto seja feita de maneira rápida.

    Como funciona? Cada objeto é “classificado” pelo seu hashCode e, com isso, conseguimos espalhar cada
objeto agrupando-os pelo hashCode. Quando buscamos determinado objeto, só vamos procurar entre os ele-
mentos que estão no grupo daquele hashCode. Dentro desse grupo, vamos testando o objeto procurado com o
candidato usando equals().

    Para que isso funcione direito, o método hashCode de cada objeto deve retornar o mesmo valor para dois
objetos, se eles são considerados equals. Em outras palavras:


                                            Capítulo 16 - Collections framework - Para saber mais: Properties - Página 200


[PAGINA 213]
                                                         Material do Treinamento Java e Orientação a Objetos




   a.equals(b) implica a.hashCode() == b.hashCode()

    Implementar hashCode de tal maneira que ele retorne valores diferentes para dois objetos considerados
equals quebra o contrato de Object e resultará em collections que usam espalhamento (como HashSet, HashMap
e Hashtable), não achando objetos iguais dentro de uma mesma coleção.


               No Eclipse...
              O Eclipse é capaz de gerar uma implementação correta de equals e hashcode baseado nos atri-
              butos que você queira comparar. Basta ir no menu Source e depois em Generate hashcode() and
              equals().


 16.14 - Para saber mais: Boas práticas
   As coleções do Java oferecem grande flexibilidade ao usuário. A perda de performance em relação à utili-
zação de arrays é irrelevante, mas deve-se tomar algumas precauções:

   • Grande parte das coleções usam, internamente, um array para armazenar os seus dados. Quando esse
        array não é mais suficiente, é criada um maior e o conteúdo da antiga é copiado. Este processo pode
        acontecer muitas vezes, no caso de você ter uma coleção que cresce muito. Você deve, então, criar uma
        coleção já com uma capacidade grande, para evitar o excesso de redimensionamento.

   • Evite usar coleções que guardam os elementos pela sua ordem de comparação quando não há necessi-
        dade. Um TreeSet gasta computacionalmente O(log(n)) para inserir (ele utiliza uma árvore rubro-negra
        como implementação), enquanto o HashSet gasta apenas O(1).

   • Não itere sobre uma List utilizando um for de 0 até list.size() e usando get(int) para receber os
        objetos. Enquanto isso parece atraente, algumas implementações da List não são de acesso aleatório
        como a LinkedList, fazendo esse código ter uma péssima performance computacional. (use Iterator)


 16.15 - Exercícios: Collections

1) Crie um código que insira 30 mil números numa ArrayList e pesquise-os. Vamos usar um método de
   System para cronometrar o tempo gasto:

    1 public class TestaPerformance {

    2
    3        public static void main(String[] args) {
    4            System.out.println("Iniciando...");
    5            long inicio = System.currentTimeMillis();
    6            Collection<Integer> teste = new ArrayList<Integer>();
    7
    8            int total = 30000;
    9
   10            for (int i = 0; i < total; i++) {
   11                teste.add(i);
   12            }
   13
   14            for (int i = 0; i < total; i++) {
   15                teste.contains(i);

                                           Capítulo 16 - Collections framework - Para saber mais: Boas práticas - Página 201


[PAGINA 214]
                                                       Material do Treinamento Java e Orientação a Objetos




   16          }
   17
   18          long fim = System.currentTimeMillis();
   19          long tempo = fim - inicio;
   20          System.out.println("Tempo gasto: " + tempo);
   21      }
   22 }

   Troque a ArrayList por um HashSet e verifique o tempo que vai demorar:

   Collection<Integer> teste = new HashSet<Integer>();



   O que é lento? A inserção de 30 mil elementos ou as 30 mil buscas? Descubra computando o tempo gasto
   em cada for separadamente.
   A diferença é mais que gritante. Se você passar de 30 mil para um número maior, como 50 ou 100 mil, verá
   que isso inviabiliza por completo o uso de uma List, no caso em que queremos utilizá-la essencialmente em
   pesquisas.

2) (conceitual, importante) Repare que, se você declarar a coleção e der new assim:

   Collection<Integer> teste = new ArrayList<Integer>();


   em vez de

   ArrayList<Integer> teste = new ArrayList<Integer>();



   É garantido que vai ter de alterar só essa linha para substituir a implementação por HashSet. Estamos aqui
   usando o polimorfismo para nos proteger que mudanças de implementação venham nos obrigar a alterar
   muito código. Mais uma vez: programe voltado a interface, e não à implementação! Esse é um excelente
   exemplo de bom uso de interfaces, afinal, de que importa como a coleção funciona? O que queremos é uma
   coleção qualquer, isso é suficiente para os nossos propósitos! Nosso código está com baixo acoplamento
   em relação a estrutura de dados utilizada: podemos trocá-la facilmente.
   Esse é um código extremamente elegante e flexível. Com o tempo você vai reparar que as pessoas tentam
   programar sempre se referindo a essas interfaces menos específicas, na medida do possível: os métodos
   costumam receber e devolver Collections, Lists e Sets em vez de referenciar diretamente uma implemen-
   tação. É o mesmo que ocorre com o uso de InputStream e OutputStream: eles são o suficiente, não há
   porque forçar o uso de algo mais específico.
   Obviamente, algumas vezes não conseguimos trabalhar dessa forma e precisamos usar uma interface mais
   específica ou mesmo nos referir ao objeto pela sua implementação para poder chamar alguns métodos. Por
   exemplo, TreeSet tem mais métodos que os definidos em Set, assim como LinkedList em relação a List.

3) Faça testes com o Map, como visto nesse capítulo:

    1 public class TestaMapa {

    2
    3      public static void main(String[] args) {
    4          Conta c1 = new ContaCorrente();
    5          c1.deposita(10000);
    6

                                                 Capítulo 16 - Collections framework - Exercícios: Collections - Página 202


[PAGINA 215]
                                                        Material do Treinamento Java e Orientação a Objetos




    7          Conta c2 = new ContaCorrente();
    8          c2.deposita(3000);
    9
   10          // cria o mapa
   11          Map mapaDeContas = new HashMap();
   12
   13          // adiciona duas chaves e seus valores
   14          mapaDeContas.put("diretor", c1);
   15          mapaDeContas.put("gerente", c2);
   16
   17          // qual a conta do diretor?
   18          Conta contaDoDiretor = (Conta) mapaDeContas.get("diretor");
   19          System.out.println(contaDoDiretor.getSaldo());
   20      }
   21 }


   Depois, altere o código para usar o generics, e não haver a necessidade do casting, além da garantia de que
   nosso mapa estará seguro em relação a tipagem usada.
   Você pode utilizar o quickfix do Eclipse para ele consertar isso, na linha em que você está chamando o put.
   Depois de mais um quickfix (descubra!) seu código deve ficar como segue:

   // cria o mapa

   Map<String, Conta> mapaDeContas = new HashMap<String, Conta>();


4) (opcional) Assim como no exercício 1, crie uma comparação entre ArrayList e LinkedList, para ver qual é a
   mais rápida para se adicionar elementos na primeira posição (list.add(0, elemento)), como por exemplo:

    1 public class TestaPerformance2 {

    2
    3      public static void main(String[] args) {
    4          System.out.println("Iniciando...");
    5          long inicio = System.currentTimeMillis();
    6
    7          // trocar depois por ArrayList
    8          List<Integer> teste = new LinkedList<Integer>();
    9
   10          for (int i = 0; i < 30000; i++) {
   11              teste.add(0, i);
   12          }
   13
   14          long fim = System.currentTimeMillis();
   15          double tempo = (fim - inicio) / 1000.0;
   16          System.out.println("Tempo gasto: " + tempo);
   17      }
   18 }


   Seguindo o mesmo raciocínio, você pode ver qual é a mais rápida para se percorrer usando o get(indice)
   (sabemos que o correto seria utilizar o enhanced for ou o iterator). Para isso, insira 30 mil elementos e depois
   percorra-os usando cada implementação de List.
   Perceba que aqui o nosso intuito não é que você aprenda quem é mais rápido que quem, o importante é
   perceber que podemos tirar proveito do polimorfismo para nos comprometer apenas com a interface. Depois,


                                                   Capítulo 16 - Collections framework - Exercícios: Collections - Página 203


[PAGINA 216]
                                                    Material do Treinamento Java e Orientação a Objetos




   quando necessário, podemos trocar e escolher uma implementação mais adequada as nossas necessida-
   des. Mais uma vez aqui vemos a vantagem de programar voltado a interface.

5) (opcional) Crie uma classe Banco que possui uma List de Conta chamada contas. Repare que numa lista
   de Conta, você pode colocar tanto ContaCorrente quanto ContaPoupanca por causa do polimorfisomo.
   Crie um método void adiciona(Conta c),            um método Conta pega(int x) e outro int
   pegaTotalDeContas(), muito similar à relação anterior de Empresa-Funcionário. Basta usar a sua
   lista e delegar essas chamadas para os métodos e coleções que estudamos.

6) (opcional) No Banco, crie um método Conta buscaPorNome(String nome) que procura por uma Conta cujo
   nome seja equals ao nome dado.
   Você pode implementar esse método com um for na sua lista de Conta, porém não tem uma performance
   eficiente.
   Adicionano um atributo privado do tipo Map<String, Conta> terá um impacto significativo. Toda vez que o
   método adiciona(Conta c) for invocado, você deve invocar .put(c.getNome(), c) no seu mapa. Dessa
   maneira, quando alguém invocar o método Conta buscaPorNome(String nome), basta você fazer o get no
   seu mapa, passando nome como argumento!
   Acontece às vezes de termos mais de um mapa, se precisarmos buscar por objetos por mais de um critério.

7) (opcional, avançado) Crie o método hashCode para a sua conta, de forma que ele respeite o equals de que
   duas contas são equals quando tem o mesmo número. Verifique se sua classe funciona corretamente num
   HashSet. Remova o método hashCode. Continua funcionando?
   Dominar o uso e o funcionamento do hashCode é fundamental para o bom programador.


 16.16 - Desafios

1) Gere todos os números entre 1 e 1000 e ordene em ordem decrescente utilizando um TreeSet.

2) Gere todos os números entre 1 e 1000 e ordene em ordem decrescente utilizando um ArrayList.




                                                          Capítulo 16 - Collections framework - Desafios - Página 204


[PAGINA 217]
                                                                                             C APÍTULO   17

Programação Concorrente e Threads
                                         “O único lugar onde o sucesso vem antes do trabalho é no dicionário.”
                                                                                              – Albert Einstein


   Ao término desse capítulo, você será capaz de:

   • executar tarefas simultaneamente;

   • colocar tarefas para aguardar até que um determinado evento ocorra;

   • entender o funcionamento do Garbage Collector.


 17.1 - Threads


“Duas coisas ao mesmo tempo"

    Em várias situações precisamos “rodar duas coisas ao mesmo tempo”. Imagine um programa que gera
um relatório muito grande em PDF. É um processo demorado e, para dar alguma satisfação para o usuário,
queremos mostrar uma barra de progresso. Queremos então gerar o PDF e ao mesmo tempo atualizar a
barrinha.

   Pensando um pouco mais amplamente, quando usamos o computador também fazemos várias coisas si-
multaneamente: queremos navegar na internet e ao mesmo tempo ouvir música.

   A necessidade de se fazer várias coisas simultaneamente, ao mesmo tempo, paralelamente aparece fre-
quentemente na computação. Para vários programas distintos, normalmente o próprio sistema operacional
gerencia isso através de vários processos em paralelo.

   Em um programa só (um processo só), se queremos executar coisas em paralelo, normalmente falamos de
Threads.


Threads em Java

   Em Java, usamos a classe Thread do pacote java.lang para criarmos linhas de execução paralelas. A classe
Thread recebe como argumento um objeto com o código que desejamos rodar. Por exemplo, no programa de
PDF e barra de progresso:

public class GeraPDF {
    public void rodar () {


                                                     205


[PAGINA 218]
                                                       Material do Treinamento Java e Orientação a Objetos




         // lógica para gerar o pdf...
    }
}

public class BarraDeProgresso {
    public void rodar () {
        // mostra barra de progresso e vai atualizando ela...
    }
}


    E, no método main, criamos os objetos e passamos para a classe Thread. O método start é responsável
por iniciar a execução da Thread:

public class MeuPrograma {
    public static void main (String[] args) {

         GeraPDF gerapdf = new GeraPDF();
         Thread threadDoPdf = new Thread(gerapdf);
         threadDoPdf.start();

         BarraDeProgresso barraDeProgresso = new BarraDeProgresso();
         Thread threadDaBarra = new Thread(barraDeProgresso);
         threadDaBarra.start();

    }
}


   O código acima, porém, não compilará. Como a classe Thread sabe que deve chamar o método roda?
Como ela sabe que nome de método daremos e que ela deve chamar esse método especial? Falta na verdade
um contrato entre as nossas classes a serem executadas e a classe Thread.

    Esse contrato existe e é feito pela interface Runnable: devemos dizer que nossa classe é “executável” e que
segue esse contrato. Na interface Runnable há apenas um método chamado run. Basta implementá-lo, “assinar”
o contrato e a classe Thread já saberá executar nossa classe.

public class GeraPDF implements Runnable {
    public void run () {
        // lógica para gerar o pdf...
    }
}

public class BarraDeProgresso implements Runnable {
    public void run () {
        // mostra barra de progresso e vai atualizando ela...
    }
}


   A classe Thread recebe no construtor um objeto que é um Runnable, e seu método start chama o método
run da nossa classe. Repare que a classe Thread não sabe qual é o tipo específico da nossa classe; para ela,
basta saber que a classe segue o contrato estabelecido e possui o método run.

    É o bom uso de interfaces, contratos e polimorfismo na prática!


                                                 Capítulo 17 - Programação Concorrente e Threads - Threads - Página 206


[PAGINA 219]
                                                           Material do Treinamento Java e Orientação a Objetos




            Estendendo a classe Thread
           A classe Thread implementa Runnable. Então, você pode criar uma subclasse dela e reescrever o
           run que, na classe Thread, não faz nada:

            public class GeraPDF extends Thread {

                public void run () {
                    // ...
                }
           }

           E, como nossa classe é uma Thread, podemos usar o start diretamente:

            GeraPDF gera = new GeraPDF();

           gera.start();

           Apesar de ser um código mais simples, você está usando herança apenas por “preguiça” (herdamos
           um monte de métodos mas usamos apenas o run), e não por polimorfismo, que seria a grande
           vantagem. Prefira implementar Runnable a herdar de Thread.


            Dormindo
           Para que a thread atual durma basta chamar o método a seguir, por exemplo, para dormir 3
           segundos:

            Thread.sleep(3 * 1000);




 17.2 - Escalonador e trocas de contexto
   Veja a classe a seguir:

 1 public class Programa implements Runnable {
 2
 3     private int id;
 4     // colocar getter e setter pro atributo id
 5
 6     public void run () {
 7         for (int i = 0; i < 10000; i++) {
 8             System.out.println("Programa " + id + " valor: " + i);
 9         }
10     }
11 }


   É uma classe que implementa Runnable e, no método run, apenas imprime dez mil números. Vamos usá-las
duas vezes para criar duas threads e imprimir os números duas vezes simultaneamente:

 1 public class Teste {
 2     public static void main(String[] args) {
 3


                             Capítulo 17 - Programação Concorrente e Threads - Escalonador e trocas de contexto - Página 207


[PAGINA 220]
                                                          Material do Treinamento Java e Orientação a Objetos




 4          Programa p1 = new Programa();
 5          p1.setId(1);
 6
 7          Thread t1 = new Thread(p1);
 8          t1.start();
 9
10          Programa p2 = new Programa();
11          p2.setId(2);
12
13          Thread t2 = new Thread(p2);
14          t2.start();
15
16     }
17 }


    Se rodarmos esse programa, qual será a saída? De um a mil e depois de um a mil? Provavelmente não,
senão seria sequencial. Ele imprimirá 0 de t1, 0 de t2, 1 de t1, 1 de t2, 2 de t1, 2 de t2 e etc? Exatamente
intercalado?

   Na verdade, não sabemos exatamente qual é a saída. Rode o programa várias vezes e observe: em cada
execução a saída é um pouco diferente.

   O problema é que no computador existe apenas um processador capaz de executar coisas. E quando
queremos executar várias coisas ao mesmo tempo, e o processador só consegue fazer uma coisa de cada vez?
Entra em cena o escalonador de threads.

    O escalonador (scheduler), sabendo que apenas uma coisa pode ser executada de cada vez, pega todas
as threads que precisam ser executadas e faz o processador ficar alternando a execução de cada uma delas. A
idéia é executar um pouco de cada thread e fazer essa troca tão rapidamente que a impressão que fica é que
as coisas estão sendo feitas ao mesmo tempo.

    O escalonador é responsável por escolher qual a próxima thread a ser executada e fazer a troca de contexto
(context switch). Ele primeiro salva o estado da execução da thread atual para depois poder retomar a execução
da mesma. Aí ele restaura o estado da thread que vai ser executada e faz o processador continuar a execução
desta. Depois de um certo tempo, esta thread é tirada do processador, seu estado (o contexto) é salvo e outra
thread é colocada em execução. A troca de contexto é justamente as operações de salvar o contexto da thread
atual e restaurar o da thread que vai ser executada em seguida.

   Quando fazer a troca de contexto, por quanto tempo a thread vai rodar e qual vai ser a próxima thread a ser
executada, são escolhas do escalonador. Nós não controlamos essas escolhas (embora possamos dar “dicas”
ao escalonador). Por isso que nunca sabemos ao certo a ordem em que programas paralelos são executados.

   Você pode pensar que é ruim não saber a ordem. Mas perceba que se a ordem importa para você, se é
importante que determinada coisa seja feita antes de outra, então não estamos falando de execuções paralelas,
mas sim de um programa sequencial normal (onde uma coisa é feita depois da outra, em uma sequência).

   Todo esse processo é feito automaticamente pelo escalonador do Java (e, mais amplamente, pelo escalo-
nador do sistema operacional). Para nós, programadores das threads, é como se as coisas estivessem sendo
executadas ao mesmo tempo.




                            Capítulo 17 - Programação Concorrente e Threads - Escalonador e trocas de contexto - Página 208


[PAGINA 221]
                                                       Material do Treinamento Java e Orientação a Objetos




             E em mais de um processador?
            A VM do Java e a maioria dos SOs modernos consegue fazer proveito de sistemas com vários
            processadores ou multi-core. A diferença é que agora temos mais de um processador executando
            coisas e teremos, sim, execuções verdadeiramente paralelas.
            Mas o número de processos no SO e o número de Threads paralelas costumam ser tão grandes
            que, mesmo com vários processadores, temos as trocas de contexto. A diferença é que o esca-
            lonador tem dois ou mais processadores para executar suas threads. Mas dificilmente terá uma
            máquina com mais processadores que threads paralelas executando.


 17.3 - Garbage Collector
   O Garbage Collector (coletor de lixo, lixeiro) é uma Thread responsável por jogar fora todos os objetos que
não estão sendo referenciados por nenhum outro objeto - seja de maneira direta ou indireta.

   Considere o código:

Conta conta1 = new ContaCorrente();
Conta conta2 = new ContaCorrente();


   Até este momento, sabemos que temos 2 objetos em memória. Aqui, o Garbage Collector não pode eliminar
nenhum dos objetos, pois ainda tem alguém se referindo a eles de alguma forma.

   Podemos, então, executar uma linha que nos faça perder a referência para um dos dois objetos criados,
como, por exemplo, o seguinte código:

conta2 = conta1;


   Quantos objetos temos em memória?

   Perdemos a referência para um dos objetos que foram criados. Esse objeto já não é mais acessível. Temos,
então, apenas um objeto em memória?

    Não podemos afirmar isso! Como o Garbage Collector é uma Thread, você não tem garantia de quando ele
vai rodar. Você só sabe que, em algum momento no futuro, aquela memória vai ser liberada.

    Algumas pessoas costumam atribuir null a uma variável, com o intuito de acelerar a passagem do Garbage
Collector por aquele objeto:

for (int i = 0; i < 100; i++) {
    List x = new ArrayList();
    // faz algumas coisas com a arraylist
    x = null;
}


   Isso rarissimamente é necessário. O Garbage Collector age apenas sobre objetos, nunca sobre variáveis.
Nesse caso, a variável x não existirá mais a cada iteração, deixando a ArrayList criada sem nenhuma referência
para ela.




                                        Capítulo 17 - Programação Concorrente e Threads - Garbage Collector - Página 209


[PAGINA 222]
                                                          Material do Treinamento Java e Orientação a Objetos




             System.gc()
            Você nunca consegue forçar o Garbage Collector, mas chamando o método estático gc da classe
            System, você está sugerindo que a Virtual Machine rode o Garbage Collector naquele momento.
            Se sua sugestão vai ser aceita ou não, isto depende de JVM para JVM, e você não tem garantias.
            Evite o uso deste método. Você não deve basear sua aplicação em quando o Garbage Collector vai
            rodar ou não.


             Finalizer
            A classe Object define também um método finalize, que você pode reescrever. Esse método será
            chamado no instante antes do Garbage Collector coletar este objeto. Não é um destrutor, você não
            sabe em que momento ele será chamado. Algumas pessoas o utilizam para liberar recursos “caros”
            como conexões, threads e recursos nativos. Isso deve ser utilizado apenas por segurança: o ideal
            é liberar esses recursos o mais rápido possível, sem depender da passagem do Garbage Collector.


 17.4 - Para saber mais: problemas com concorrência
    O uso de Threads começa a ficar interessante e complicado quando precisamos compartilhar objetos entre
várias Threads.

    Imagine a seguinte situação: temos um Banco com milhões de Contas Bancárias. Clientes sacam e depo-
sitam dinheiro continuamente, 24 horas por dia. No primeiro dia de cada mês, o Banco precisa atualizar o saldo
de todas as Contas de acordo com uma taxa específica. Para isso, ele utiliza o AtualizadorDeContas que vimos
anteriormente.

   O AtualizadorDeContas, basicamente, pega uma a uma cada uma das milhões de contas e chama seu
método atualiza. A atualização de milhões de contas é um processo demorado, que dura horas; é inviável
parar o banco por tanto tempo até que as atualizações tenham completado. É preciso executar as atualizações
paralelamente às atividades, de depósitos e saques, normais do banco.

   Ou seja, teremos várias threads rodando paralelamente. Em uma thread, pegamos todas as contas e
vamos chamando o método atualiza de cada uma. Em outra, podemos estar sacando ou depositando dinheiro.
Estamos compartilhando objetos entre múltiplas threads (as contas, no nosso caso).

    Agora imagine a seguinte possibilidade (mesmo que muito remota): no exato instante em que o atualizador
está atualizando uma Conta X, o cliente dono desta Conta resolve efetuar um saque. Como sabemos, ao
trabalhar com Threads, o escalonador pode parar uma certa Thread a qualquer instante para executar outra, e
você não tem controle sobre isso.

   Veja essa classe Conta:

 1 public class Conta {
 2
 3     private double saldo;
 4
 5         // outros metodos e atributos...
 6
 7         public void atualiza(double taxa) {
 8             double saldoAtualizado = this.saldo * (1 + taxa);
 9             this.saldo = saldoAtualizado;
10         }
11

                 Capítulo 17 - Programação Concorrente e Threads - Para saber mais: problemas com concorrência - Página 210


[PAGINA 223]
                                                          Material do Treinamento Java e Orientação a Objetos




12          public void deposita(double valor) {
13              double novoSaldo = this.saldo + valor;
14              this.saldo = novoSaldo;
15          }
16 }


    Imagine uma Conta com saldo de 100 reais. Um cliente entra na agência e faz um depósito de 1000 reais.
Isso dispara uma Thread no banco que chama o método deposita(); ele começa calculando o novoSaldo que
passa a ser 1100 (linha 13). Só que por algum motivo que desconhecemos, o escalonador pára essa thread.

   Neste exato instante ele começa a executar uma outra Thread que chama o método atualiza da mesma
Conta, por exemplo, com taxa de 1%. Isso quer dizer que o novoSaldo passa a valer 101 reais (linha 8). E,
nesse instante o escalonador troca de Threads novamente. Agora ele executa a linha 14 na Thread que fazia
o depósito; o saldo passa a valer 1100. Acabando o deposita, o escalonador volta pra Thread do atualiza e
executa a linha 9, fazendo o saldo valer 101 reais.

   Resultado: o depósito de mil reais foi totalmente ignorado e seu Cliente ficará pouco feliz com isso. Perceba
que não é possível detectar esse erro, já que todo o código foi executado perfeitamente, sem problemas. O
problema, aqui, foi o acesso simultâneo de duas Threads ao mesmo objeto.

    E o erro só ocorreu porque o escalonador parou nossas Threads naqueles exatos lugares. Pode ser que
nosso código fique rodando 1 ano sem dar problema algum e em um belo dia o escalonador resolve alternar
nossas Threads daquela forma. Não sabemos como o escalonador se comporta! Temos que proteger nosso
código contra esse tipo de problema. Dizemos que essa classe não é thread safe, isso é, não está pronta para
ter uma instância utilizada entre várias threads concorrentemente.

   O que queríamos era que não fosse possível alguém atualizar a Conta enquanto outra pessoa está deposi-
tando um dinheiro. Queríamos que uma Thread não pudesse mexer em uma Conta enquanto outra Thread está
mexendo nela. Não há como impedir o escalonador de fazer tal escolha. Então, o que fazer?

    Uma idéia seria criar uma trava e, no momento em que uma Thread entrasse em um desses métodos,
ela trancaria a entrada com uma chave. Dessa maneira, mesmo que sendo colocada de lado, nenhuma outra
Thread poderia entrar nesses métodos, pois a chave estaria com a outra Thread.

     Essa idéia é chamada de região crítica. É um pedaço de código que definimos como crítico e que não
pode ser executado por duas threads ao mesmo tempo. Apenas uma thread por vez consegue entrar na região
crítica.

    Podemos fazer isso em Java. Podemos usar qualquer objeto como um lock (trava, chave), para poder
sincronizar em cima desse objeto, isto é, se uma Thread entrar em um bloco que foi definido como sincronizado
por esse lock, apenas uma Thread poderá estar lá dentro ao mesmo tempo, pois a chave estará com ela.

    A palavra chave synchronized dá essa característica a um bloco de código e recebe qual é o objeto que
será usado como chave. A chave só é devolvida no momento em que a Thread que tinha essa chave sair do
bloco, seja por return ou disparo de uma exceção (ou ainda na utilização do método wait())..

   Queremos, então, bloquear o acesso simultâneo a uma mesma Conta:

public class Conta {

    private double saldo;

    // outros metodos e atributos...


                 Capítulo 17 - Programação Concorrente e Threads - Para saber mais: problemas com concorrência - Página 211


[PAGINA 224]
                                                            Material do Treinamento Java e Orientação a Objetos




      public void atualiza(double taxa) {
          synchronized (this) {
              double saldoAtualizado = this.saldo * (1 + taxa);
              this.saldo = saldoAtualizado;
          }
      }

      public void deposita(double valor) {
          synchronized (this) {
              double novoSaldo = this.saldo + valor;
              this.saldo = novoSaldo;
          }
      }
}


  Observe o uso dos blocos synchronized dentro dos dois métodos. Eles bloqueiam uma Thread utilizando o
mesmo objeto Conta, o this.

   Esses métodos agora são mutuamente exclusivos e só executam de maneira atômica. Threads que ten-
tam pegar um lock que já está pego, ficarão em um conjunto especial esperando pela liberação do lock (não
necessariamente numa fila).

             Sincronizando o bloco inteiro
            É comum sempre sincronizarmos um método inteiro, normalmente utilizando o this.

             public void metodo() {

                   synchronized (this) {
                       // conteudo do metodo
                   }
            }

            Para este mesmo efeito, existe uma sintaxe mais simples, onde o synchronized pode ser usado
            como modificador do método:

             public synchronized void metodo() {

                   // conteudo do metodo
            }




                Mais sobre locks e monitores e concorrência
            Se o método for estático, será sincronizado usando o lock do objeto que representa a classe
            (NomeDaClasse.class).
            Além disso, o pacote java.util.concurrent, conhecido como JUC, entrou no Java 5.0 para facilitar
            uma série de trabalhos comuns que costumam a aparecer em uma aplicação concorrente.



    17.5 - Para saber mais: Vector e Hashtable
   Duas collections muito famosas são Vector e Hashtable, a diferença delas com suas irmãs ArrayList e
HashMap é que as primeiras são thread safe.

                           Capítulo 17 - Programação Concorrente e Threads - Para saber mais: Vector e Hashtable - Página 212


[PAGINA 225]
                                                      Material do Treinamento Java e Orientação a Objetos




     Você pode se perguntar porque não usamos sempre essas classes thread safe. Adquirir um lock tem um
custo, e caso um objeto não va ser usado entre diferentes threads, não há porque usar essas classes que
consomem mais recursos. Mas nem sempre é fácil enxergar se devemos sincronizar um bloco, ou se devemos
utilizar blocos sincronizados.

   Antigamente o custo de se usar locks era altíssimo, hoje em dia isso custa pouco para a JVM, mas não é
motivo para você sincronizar tudo sem necessidade.


 17.6 - Um pouco mais...
   1-) Você pode mudar a prioridade de cada uma de suas Threads, mas isto também é apenas uma sugestão
ao escalonador.

   2-) Existe um método stop nas Threads, porque não é boa prática chamá-lo?

   3-) Um tópico mais avançado é a utilização de wait, notifiy e notifyAll para que as Threads comuniquem-se
de eventos ocorridos, indicando que podem ou não podem avançar de acordo com condições

    4-) O pacote java.util.concurrent foi adicionado no Java 5 para facilitar o trabalho na programação con-
corrente. Ele possui uma série de primitivas para que você não tenha de trabalhar diretamente com wait e
notify, além de ter diversas Collections thread safe.


 17.7 - Exercícios

1) Teste o exemplo deste capítulo para imprimir números em paralelo.
   Escreva a classe Programa:

    1 public class Programa implements Runnable {

    2
    3     private int id;
    4     // colocar getter e setter pro atributo id
    5
    6     public void run () {
    7         for (int i = 0; i < 10000; i++) {
    8             System.out.println("Programa " + id + " valor: " + i);
    9         }
   10     }
   11 }

   Escreva a classe de Teste:

    1 public class Teste {

    2     public static void main(String[] args) {
    3
    4          Programa p1 = new Programa();
    5          p1.setId(1);
    6
    7          Thread t1 = new Thread(p1);
    8          t1.start();
    9
   10          Programa p2 = new Programa();

                                        Capítulo 17 - Programação Concorrente e Threads - Um pouco mais... - Página 213


[PAGINA 226]
                                                            Material do Treinamento Java e Orientação a Objetos




   11             p2.setId(2);
   12
   13             Thread t2 = new Thread(p2);
   14             t2.start();
   15
   16      }
   17 }


   Rode várias vezes a classe Teste e observe os diferentes resultados em cada execução.


 17.8 - Exercícios avançados de programação concorrente e locks
    Exercícios só recomendados se você já tinha algum prévio conhecimento de programação concorrente,
locks, etc.

1) Vamos enxergar o problema ao se usar uma classe que não é thread safe: a LinkedList por exemplo.
   Imagine que temos um objeto que guarda todas as SQLs que uma aplicação precisa executar. Vamos usar
   uma LinkedList<String> para armazená-los. Nossa aplicação é multi thread, então diferentes threads vão
   inserir diferentes SQLs para serem executados. Não importa a ordem que elas sejam executadas, desde
   que elas um dia sejam!
   Vamos usar a seguinte classe para adicionar as queries:

   public class ProduzSQL implements Runnable{

       private int comeco;
       private int fim;
       private Collection<String> sqls;

       public ProduzSQL(int comeco, int fim, Collection<String> sqls) {
           this.comeco = comeco;
           this.fim = fim;
           this.sqls = sqls;
       }

       public void run() {
           for (int i = comeco; i < fim; i++) {
               sqls.add("SQL"+i);
           }
       }
   }

   Vamos criar três threads que rodem esse código, todas adicionando SQLs no mesmo HashSet. Em outras
   palavras, teremos threads compartilhando e acessando um mesmo objeto: é aqui que mora o perigo.

   public class BancoDeDados {

       public static void main(String[] args) throws InterruptedException {
           Collection<String> sqls = new HashSet<String>();

               ProduzSQL p1 = new ProduzSQL(0, 10000, sqls);
               Thread t1 = new Thread(p1);

               ProduzSQL p2 = new ProduzSQL(10000, 20000, sqls);

       Capítulo 17 - Programação Concorrente e Threads - Exercícios avançados de programação concorrente e locks - Página 214


[PAGINA 227]
                                                            Material do Treinamento Java e Orientação a Objetos




            Thread t2 = new Thread(p2);

            ProduzSQL p3 = new ProduzSQL(20000, 30000, sqls);
            Thread t3 = new Thread(p3);

            t1.start();
            t2.start();
            t3.start();

            // faz com que nós (nós = thread que roda o main)
            // aguardemos o fim dessas três threads
            t1.join();
            t2.join();
            t3.join();

            System.out.println("Threads produtoras de SQLs finalizadas!");

            // verifica se todas as SQLs foram
            for (int i = 0; i < 15000; i++) {
                if (!sqls.contains("SQL" + i)) {
                    throw new IllegalStateException("não encontrei a SQL" + i);
                }
            }

            // verifica se null nao se encontra!
            if (sqls.contains(null)) {
                    throw new IllegalStateException("não devia ter null aqui dentro! nao inserimos null")
            }

            System.out.println("Fim da execucao com sucesso");
       }
   }


2) Teste o código anterior, mas agora usando synchronized ao adicionar na coleção:

   public void run() {

       for (int i = comeco; i < fim; i++) {
           synchronized(sqls) {
               sqls.add("SQL"+i);
           }
       }
   }


3) Sem usar o synchronized teste com a classe Vector (que é uma Collection).

4) Novamente sem usar o synchronized, teste usar HashSet e ArrayList, em vez de Vector. Faça vários
   testes, pois as threads vão se entrelaçar cada vez de uma maneira diferente, podendo ou não ter um efeito
   inesperado.

   No capítulo de Sockets usaremos threads para solucionar um problema real de execuções paralelas.




       Capítulo 17 - Programação Concorrente e Threads - Exercícios avançados de programação concorrente e locks - Página 215


[PAGINA 228]
                                                                                           C APÍTULO   18

E agora?
                                                       “A primeira coisa a entender é que você não entende.”
                                                                                    – Soren Aabye Kierkegaard


   Onde continuar ao terminar o ‘Java e Orientação a Objetos’.


 18.1 - Exercício prático
    A melhor maneira para fixar tudo o que foi visto nos capítulos anteriores é planejar e montar pequenos
sistemas. Pense na modelagem de suas classes, como e onde usar herança, polimorfismo, encapsulamento e
outros conceitos. Pratique o uso das APIs mais úteis do Java integrando-as ao seus sistemas.


 18.2 - Certificação
   Entrar em detalhes nos assuntos contidos até agora, iriam no mínimo tornar cada capítulo quatro vezes
maior do que já é.

    Os tópicos abordados (com a adição e remoção de alguns) constituem boa parte do que é cobrado na
certificação oficial para programadores da Sun.

    Para maiores informações sobre certificações, consulte a própria Sun, o javaranch.com ou o guj.com.br,
que possui diversas informações sobre o assunto. A Caelum oferece um curso de preparação para a prova de
certificação como programador em Java pela Sun, o FJ-19.


 18.3 - Web
   Um dos principais focos de Java, hoje em dia, é onde a maior parte das vagas existem: programando para
a web. Entram aqui tecnologias como servlets, JSPs e ferramentas famosas do mercado, como o Struts.

   A Caelum oferece o curso FJ-21, onde você pode estudar os tópicos necessários para começar a trabalhar
com Java na web usando as melhores práticas, design patterns e tecnologias do mercado.


 18.4 - Revistas
   Diversas revistas no Brasil e no exterior estudam o mundo java como ninguém, e podem ajudar o iniciante a
conhecer muito do que está acontecendo lá fora nas aplicações comerciais.




                                                    216


[PAGINA 229]
                                                      Material do Treinamento Java e Orientação a Objetos




 18.5 - Grupos de Usuários
   Diversos programadores com o mínimo ou máximo de conhecimento se reúnem online para a troca de
dúvidas, informações e idéias sobre projetos, bibliotecas e muito mais. São os grupos de usuários de java.

   Um dos mais importantes e famosos no Brasil é o GUJ – http://www.guj.com.br


 18.6 - Falando em Java - Próximos módulos
   O ‘Falando em Java’ não pára por aqui. A Caelum oferece uma grande variedade de cursos que você pode
seguir:

   FJ-16: Laboratório Java com Design Patterns, XML e Testes

   FJ-19: Preparatório para Certificação Java

   FJ-21: Java para desenvolvimento Web

   FJ-26: Laboratório de MVC com JSF e Hibernate para Web

   FJ-27: Desenvolvimento para Web com JBoss Seam

   FJ-28: Desenvolvimento ágil para Web 2.0 com VRaptor, Hibernate e AJAX

   FJ-31: Enterprise JavaBeans (EJB)

   FJ-34: Desenvolvimento para Web com JBoss Seam

   FJ-55: Java para pequenos dispositivos (Java ME)

   FJ-91: Arquitetura e Design de Projetos Java

   RR-71: Desenvolvimento ágil para Web 2.0 com Ruby on Rails

   RR-75: Ruby e Rails avançados: lidando com problemas do dia a dia

   Consulte mais informações no nosso site e entre em contato conosco.




                                                             Capítulo 18 - E agora? - Grupos de Usuários - Página 217


[PAGINA 230]
                                                                                         C APÍTULO   19

Apêndice - Sockets
                                                                  “Olho por olho, e o mundo acabará cego.”
                                                                                         – Mohandas Gandhi


   Conectando-se a máquinas remotas.


 19.1 - Motivação: uma API que usa os conceitos aprendidos
   Neste capítulo, você vai conhecer a API de Sockets do java pelo pacote java.net.

   Mais útil que conhecer a API, é você perceber que estamos usando, aqui, todos os conceitos e bibliotecas
aprendidas durante os outros capítulos. Repare, também, que é relativamente simples aprender a utilizar uma
API, agora que temos todos os conceitos necessários para tal.

   Lembre-se de fazer esse apêndice com o javadoc aberto ao seu lado.


 19.2 - Protocolo
    Da necessidade de dois computadores se comunicarem, surgiram diversos protocolos que permitissem tal
troca de informação: o protocolo que iremos usar aqui é o TCP (Transmission Control Protocol).

   Através do TCP, é possível criar um fluxo entre dois computadores - como é mostrado no diagrama abaixo:




   É possível conectar mais de um cliente ao mesmo servidor, como é o caso de diversos banco de dados,
webservers, etc.

                                                   218


[PAGINA 231]
                                                     Material do Treinamento Java e Orientação a Objetos




   Ao escrever um programa em Java que se comunique com outra aplicação, não é necessário se preocupar
com um nível tão baixo quanto o protocolo. As classes que trabalham com eles já foram disponibilizadas para
serem usadas por nós no pacote java.net.

    A vantagem de se usar TCP, em vez de criar nosso próprio protocolo de bytes, é que o TCP vai garantir a
entrega dos pacotes que transferirmos e criar um protocolo base para isto é algo bem complicado.


 19.3 - Porta
    Acabamos de mencionar que diversos computadores podem se conectar a um só, mas, na realidade, é
muito comum encontrar máquinas clientes com uma só conexão física. Então, como é possível se conectar a
dois pontos? Como é possível ser conectado por diversos pontos?

    Todas as aplicações que estão enviando e recebendo dados fazem isso através da mesma conexão física,
mas o computador consegue discernir, durante a chegada de novos dados, quais informações pertencem a qual
aplicação. Mas como?




   Assim como existe o IP para indentificar uma máquina, a porta é a solução para indentificar diversas apli-
cações em uma máquina. Esta porta é um número de 2 bytes, varia de 0 a 65535. Se todas as portas de uma
máquina estiverem ocupadas, não é possível se conectar a ela enquanto nenhuma for liberada.

    Ao configurar um servidor para rodar na porta 80 (padrão http), é possível se conectar a esse servidor
através dessa porta que, junto com o ip, vai formar o endereço da aplicação. Por exemplo, o servidor web da
caelum.com.br pode ser representado por: caelum.com.br:80


 19.4 - Socket
   Mas se um cliente se conecta a um programa rodando na porta 80 de um servidor, enquanto ele não se
desconectar dessa porta, será impossível que outra pessoa se conecte?

    Acontece que, ao efetuar e aceitar a conexão, o servidor redireciona o cliente de uma porta para outra,
liberando novamente sua porta inicial e permitindo que outros clientes se conectem novamente.




                                                                 Capítulo 19 - Apêndice - Sockets - Porta - Página 219


[PAGINA 232]
                                                       Material do Treinamento Java e Orientação a Objetos




    Em Java, isso deve ser feito através de threads e o processo de aceitar a conexão deve ser rodado o mais
rápido possível.


 19.5 - Servidor
    Iniciando agora um modelo de servidor de chat, o serviço do computador que funciona como base deve,
primeiro, abrir uma porta e ficar ouvindo até alguém tentar se conectar.

 1 import java.net.*;
 2
 3 public class Servidor {
 4     public static void main(String args[]) throws IOException {
 5
 6         ServerSocket servidor = new ServerSocket(12345);
 7         System.out.println("Porta 12345 aberta!");
 8         // a continuação do servidor deve ser escrita aqui
 9
10     }
11 }


     Se o objeto for realmente criado, significa que a porta 12345 estava fechada e foi aberta. Se outro programa
possui o controle desta porta neste instante, é normal que o nosso exemplo não funcione, pois ele não consegue
utilizar uma porta que já está em uso.

    Após abrir a porta, precisamos esperar por um cliente através do método accept da ServerSocket. Assim
que um cliente se conectar, o programa continuará, por isso dizemos que esse método é blocante, segura a
thread até que algo o notifique.

Socket cliente = servidor.accept();
System.out.println("Nova conexão com o cliente " +
    cliente.getInetAddress().getHostAddress()
); // imprime o ip do cliente


   Por fim, basta ler todas as informações que o cliente nos enviar:

Scanner scanner = new Scanner(cliente.getInputStream());



                                                                Capítulo 19 - Apêndice - Sockets - Servidor - Página 220


[PAGINA 233]
                                                     Material do Treinamento Java e Orientação a Objetos




while (scanner.hasNextLine()) {
    System.out.println(scanner.nextLine());
}


   Agora fechamos as conexões, começando pelo fluxo:

in.close();
cliente.close();
servidor.close();


   O resultado é a classe a seguir:

 1 public class Servidor {
 2     public static void main(String[] args) throws IOException {
 3         ServerSocket servidor = new ServerSocket(12345);
 4         System.out.println("Porta 12345 aberta!");
 5
 6         Socket cliente = servidor.accept();
 7         System.out.println("Nova conexão com o cliente " +
 8             cliente.getInetAddress().getHostAddress()
 9         );
10
11         Scanner s = new Scanner(cliente.getInputStream());
12         while (s.hasNextLine()) {
13             System.out.println(s.nextLine());
14         }
15
16         s.close();
17         servidor.close();
18         cliente.close();
19     }
20 }



 19.6 - Cliente
   Agora, a nossa tarefa é criar um programa cliente que envie mensagens para o servidor... o cliente é ainda
mais simples do que o servidor.

    O código a seguir é a parte principal e tenta se conectar a um servidor no ip 127.0.0.1 (máquina local) e
porta 12345:

Socket cliente = new Socket("127.0.0.1",12345);
System.out.println("O cliente se conectou ao servidor!");


   Queremos agora ler os dados do cliente, da entrada padrão (teclado):

Scanner teclado = new Scanner(System.in);
while (teclado.hasNextLine()) {
    // lê a linha e faz alguma coisa com ela


                                                               Capítulo 19 - Apêndice - Sockets - Cliente - Página 221


[PAGINA 234]
                                                       Material do Treinamento Java e Orientação a Objetos




}


    Agora, basta ler as linhas que o usuário digitar através do buffer de entrada (in), e jogá-las no buffer de
saída:

PrintStream saida = new PrintStream(cliente.getOutputStream());
Scanner teclado = new Scanner(System.in);
while (teclado.hasNextLine()) {
    saida.println(teclado.nextLine());
}
saida.close();
teclado.close();


   Repare que usamos os conceito de java.io aqui novamente, para leitura do teclado e envio de mensagens
para o servidor. Para as classes Scanner e PrintWriter, tanto faz de onde que se lê ou escreve os dados: o
importante é que esse stream seja um InputStream / OutputStream. É o poder das interfaces, do polimorfismo,
aparecendo novamente.

    Nosso programa final:

 1 public class Cliente {
 2     public static void main(String[] args) throws UnknownHostException, IOException {
 3         Socket cliente = new Socket("127.0.0.1", 12345);
 4         System.out.println("O cliente se conectou ao servidor!");
 5
 6         Scanner teclado = new Scanner(System.in);
 7         PrintStream saida = new PrintStream(cliente.getOutputStream());
 8
 9         while (teclado.hasNextLine()) {
10             saida.println(teclado.nextLine());
11         }
12
13         saida.close();
14         teclado.close();
15         cliente.close();
16     }
17 }




   Para testar o sistema, precisamos rodar primeiro o servidor e, logo depois, o cliente. Tudo o que for digitado
no cliente será enviado para o servidor.




                                                                  Capítulo 19 - Apêndice - Sockets - Cliente - Página 222


[PAGINA 235]
                                                    Material do Treinamento Java e Orientação a Objetos




               Multithreading
           Para que o servidor seja capaz de trabalhar com dois clientes ao mesmo tempo é necessário criar
           uma thread logo após executar o método accept.
           A thread criada será responsável pelo tratamento dessa conexão, enquanto o loop do servidor
           disponibilizará a porta para uma nova conexão:

            while (true) {


                  Socket cliente = servidor.accept();

                  // cria um objeto que irá tratar a conexão
                  TratamentoClass tratamento = new TratamentoClass(cliente);

                  // cria a thread em cima deste objeto
                  Thread t = new Thread(tratamento);

                  // inicia a thread
                  t.start();

           }




 19.7 - Imagem geral




   A socket do cliente tem um InputStream, que recebe do OutputStream do servidor, e tem um OutputStream,
que transfere tudo para o InputStream do servidor. Muito parecido com um telefone!

   Repare que cliente e servidor são rótulos que indicam um estado. Um micro (ou melhor, uma JVM) pode ser
servidor num caso, mas pode ser cliente em outro caso.


 19.8 - Exercícios: Sockets

1) Crie um projeto sockets.
   Vamos fazer um pequeno sistema em que tudo que é digitado no micro cliente acaba aparecendo no micro
   servidor. Isto é, apenas uma comunicação unidirecional.
   Crie a classe Servidor como vimos nesse capítulo. Abuse dos recursos do Eclipse para não ter de escrever
   muito!

                                                          Capítulo 19 - Apêndice - Sockets - Imagem geral - Página 223


[PAGINA 236]
                                                     Material do Treinamento Java e Orientação a Objetos




    1 package br.com.caelum.chat;

    2
    3 import java.io.IOException;
    4 import java.net.ServerSocket;
    5 import java.net.Socket;
    6 import java.util.Scanner;
    7
    8 public class Servidor {
    9     public static void main(String[] args) throws IOException {
   10         ServerSocket servidor = new ServerSocket(12345);
   11         System.out.println("Porta 12345 aberta!");
   12
   13         Socket cliente = servidor.accept();
   14         System.out.println("Nova conexão com o cliente " +
   15             cliente.getInetAddress().getHostAddress());
   16
   17         Scanner entrada = new Scanner(cliente.getInputStream());
   18         while (entrada.hasNextLine()) {
   19             System.out.println(entrada.nextLine());
   20         }
   21
   22         entrada.close();
   23         servidor.close();
   24     }
   25 }


2) Crie a classe Cliente como vista anteriormente:

    1 package br.com.caelum.chat;

    2
    3 import java.io.IOException;
    4 import java.io.PrintStream;
    5 import java.net.Socket;
    6 import java.net.UnknownHostException;
    7 import java.util.Scanner;
    8
    9 public class Cliente {
   10     public static void main(String[] args) throws UnknownHostException, IOException {
   11         Socket cliente = new Socket("127.0.0.1", 12345);
   12         System.out.println("O cliente se conectou ao servidor!");
   13
   14         Scanner teclado = new Scanner(System.in);
   15         PrintStream saida = new PrintStream(cliente.getOutputStream());
   16
   17         while (teclado.hasNextLine()) {
   18             saida.println(teclado.nextLine());
   19         }
   20
   21         saida.close();
   22         teclado.close();
   23     }
   24 }




                                                     Capítulo 19 - Apêndice - Sockets - Exercícios: Sockets - Página 224


[PAGINA 237]
                                                       Material do Treinamento Java e Orientação a Objetos




   Utilize dos quick fixes e control espaço para os imports e o throws.

3) Rode a classe Servidor: repare no console do Eclipse que o programa fica esperando. Rode a classe
   Cliente: a conexão deve ser feita e o Eclipse deve mostrar os dois consoles para você (existe um pequeno
   ícone na view de Console para você alternar entre eles).
   Digite mensagens no cliente e veja se elas aparecem corretamente no servidor.

4) Teste seu programa com um colega do curso, usando comunicação remota entre as duas máquinas.
   Combinem entre si quem vai rodar o cliente e quem vai rodar o servidor. Quem for rodar o cliente deve editar
   o ip na classe para indicar o endereço da outra máquina (verifique também se estão acessando a mesma
   porta).



             Descobrindo o ip da máquina
            No Windows, abra o console e digite ipconfig para saber qual é o seu ip. No Linux (ou no BSD, Mac,
            Solaris), vá no console e digite ifconfig.

5) (Opcional) E se você quisesse, em vez de enviar tudo o que o cliente digitou, transferir um arquivo texto do
   micro do cliente para servidor? Seria difícil?
   Abuse do polimorfismo! Faça o cliente ler de um arquivo chamado arquivo.txt (crie-o!) e faça com que o
   servidor grave tudo que recebe num arquivo que chama recebido.txt.


 19.9 - Desafio: Múltiplos Clientes
   Quando o servidor aceita um cliente com a chamada ao accept, ele poderia chamar novamente este método
para aceitar um novo cliente. E, se queremos aceitar vários clientes, simultâneos, basta chamar o accept várias
vezes e tratar cada cliente em sua própria Thread (senão o método accept não será invocado novamente!).

   Um esboço de solução para a classe Servidor:

ServerSocket servidor = new ServerSocket(12345);

// servidor fica eternamente aceitando clientes...
while (true) {
    Socket cliente = servidor.accept();
    // dispara uma Thread que trata esse cliente e já espera o próximo
}



 19.10 - Desafio: broadcast das mensagens
    Agora que vários clientes podem mandar mensagens, gostaríamos que os clientes recebessem as mensa-
gens enviadas pelas outras pessoas. Ao invés do servidor simplesmente escrever as mensagens no console,
ele deve mandar cada mensagem para todos os clientes conectados.

   Precisamos manter uma lista de clientes conectados e, quando chegar uma mensagem (de qualquer cliente),
percorremos essa lista e mandamos para todos.

   Use um List para guardar os PrintStreams dos clientes. Logo depois que o servidor aceitar um cliente
novo, crie um PrintStream usando o OutputStream dele e adicione na lista. E, quando receber uma mensagem
nova, envia para todos na lista.

                                                 Capítulo 19 - Apêndice - Sockets - Desafio: Múltiplos Clientes - Página 225


[PAGINA 238]
                                                       Material do Treinamento Java e Orientação a Objetos




     Um esboço:

     Adicionando na lista:

while (true) {
    Socket cliente = servidor.accept();
    this.lista.add(new PrintStream(cliente.getOutputStream()));

      // dispara uma Thread que trata esse cliente e já espera o próximo
}


     Método que distribui as mensagens:

void distribuiMensagem(String msg) {
    for (PrintStream cliente : lista) {
        cliente.println(msg);
    }
}


    Mas agora nosso cliente também recebe mensagens. Então precisamos fazer com que o Cliente, além de
ler mensagens do teclado e enviar para o servidor, simultaneamente também possa receber mensagens de
outros clientes enviadas pelo servidor.

    Ou seja, precisamos de uma segunda Thread na classe Cliente que fica recebendo mensagens do InputS-
tream do servidor e imprimindo no console.

     Um esboço:

Scanner servidor = new Scanner(cliente.getInputStream());
while (servidor.hasNextLine()) {
    System.out.println(servidor.nextLine());
}


   Lembre que você precisará de no mínimo 2 threads para o cliente e 2 para o servidor. Então provavelmente
você irá ter que escrever 4 classes.

     Melhorias possíveis:

     • Faça com o a primeira linha enviada pelo cliente serja sempre o nick dele. E quando o servidor enviar a
       mensagem, faça ele enviar o nick de cada cliente antes da mensagem.

     • E quando um cliente desconectar? Como retirá-lo da lista?

     • É difícil fazer o envio de arquivos pelo nosso sistema de chats? Sabendo que a leitura de um arquivo é
       feita pelo FileInputStream, seria difícil mandar esse InputStream pelo OutputStream da conexão de rede?


    19.11 - Solução do sistema de chat
   Uma solução para o sistema de chat cliente-servidor com múltiplos clientes proposto nos desafios acima.
Repare que a solução não está nem um pouco elegante: o main já faz tudo, além de não tratarmos as exceptions.


                                                Capítulo 19 - Apêndice - Sockets - Solução do sistema de chat - Página 226


[PAGINA 239]
                                                       Material do Treinamento Java e Orientação a Objetos




O código visa apenas mostrar o uso de uma API. É uma péssima prática colocar toda a funcionalidade do seu
programa no main e também de jogar exceções para trás.

   Nesta listagem, faltam os devidos imports.

   Primeiro, as duas classes para o cliente. Repare que a única mudança grande é a classe nova, Recebedor:

 1 public class Cliente {
 2     public static void main(String[] args) throws UnknownHostException, IOException {
 3         // dispara cliente
 4         new Cliente("127.0.0.1", 12345).executa();
 5     }
 6
 7     private String host;
 8     private int porta;
 9
10     public Cliente (String host, int porta) {
11         this.host = host;
12         this.porta = porta;
13     }
14
15     public void executa() throws UnknownHostException, IOException {
16         Socket cliente = new Socket(this.host, this.porta);
17         System.out.println("O cliente se conectou ao servidor!");
18
19         // thread para receber mensagens do servidor
20         Recebedor r = new Recebedor(cliente.getInputStream());
21         new Thread(r).start();
22
23         // le msgs do teclado e manda pro servidor
24         Scanner teclado = new Scanner(System.in);
25         PrintStream saida = new PrintStream(cliente.getOutputStream());
26         while (teclado.hasNextLine()) {
27             saida.println(teclado.nextLine());
28         }
29
30         saida.close();
31         teclado.close();
32         cliente.close();
33     }
34 }



 1 public class Recebedor implements Runnable {
 2
 3     private InputStream servidor;
 4
 5     public Recebedor(InputStream servidor) {
 6         this.servidor = servidor;
 7     }
 8
 9     public void run() {
10         // recebe msgs do servidor e imprime na tela
11         Scanner s = new Scanner(this.servidor);
12         while (s.hasNextLine()) {


                                                Capítulo 19 - Apêndice - Sockets - Solução do sistema de chat - Página 227


[PAGINA 240]
                                                       Material do Treinamento Java e Orientação a Objetos




13               System.out.println(s.nextLine());
14          }
15     }
16 }


   Já o Servidor sofreu bastante modificações. A classe TrataCliente é a responsável por cuidar de cada cliente
conectado no sistema:

 1 public class Servidor {
 2
 3     public static void main(String[] args) throws IOException {
 4         // inicia o servidor
 5         new Servidor(12345).executa();
 6     }
 7
 8     private int porta;
 9     private boolean encerrar;
10     private List<PrintStream> clientes;
11
12     public Servidor (int porta) {
13         this.porta = porta;
14         this.clientes = new ArrayList<PrintStream>();
15     }
16
17     public void executa () throws IOException {
18         ServerSocket servidor = new ServerSocket(this.porta);
19         System.out.println("Porta 12345 aberta!");
20
21         while (!encerrar) {
22             // aceita um cliente
23             Socket cliente = servidor.accept();
24             System.out.println("Nova conexão com o cliente " +
25                 cliente.getInetAddress().getHostAddress()
26             );
27
28             // adiciona saida do cliente à lista
29             PrintStream ps = new PrintStream(cliente.getOutputStream());
30             this.clientes.add(ps);
31
32             // cria tratador de cliente numa nova thread
33             TrataCliente tc = new TrataCliente(cliente.getInputStream(), this);
34             new Thread(tc).start();
35         }
36
37     }
38
39     public void distribuiMensagem(String msg) {
40         // envia msg para todo mundo
41         for (PrintStream cliente : this.clientes) {
42             cliente.println(msg);
43         }
44     }
45 }




                                                Capítulo 19 - Apêndice - Sockets - Solução do sistema de chat - Página 228


[PAGINA 241]
                                                 Material do Treinamento Java e Orientação a Objetos




 1 public class TrataCliente implements Runnable {
 2
 3     private InputStream cliente;
 4     private Servidor servidor;
 5
 6     public TrataCliente(InputStream cliente, Servidor servidor) {
 7         this.cliente = cliente;
 8         this.servidor = servidor;
 9     }
10
11     public void run() {
12         // quando chegar uma msg, distribui pra todos
13         Scanner s = new Scanner(this.cliente);
14         while (s.hasNextLine()) {
15             servidor.distribuiMensagem(s.nextLine());
16         }
17         s.close();
18     }
19 }




                                          Capítulo 19 - Apêndice - Sockets - Solução do sistema de chat - Página 229


[PAGINA 242]
                                                                                           C APÍTULO   20

Apêndice - Instalação do Java
                                                                     “Quem pouco pensa, engana-se muito.”
                                                                                       – Leonardo da Vinci


   Instalação do Java Development Kit em ambiente Windows e Linux.


 20.1 - Escolhendo a VM
  Como vimos antes, a VM é apenas uma especificação e devemos baixar uma implementação. Há muitas
empresas que implementam uma VM, como a própria Sun, a IBM, a BEA e outras.

   A da Sun é a mais usada e possui versões para Windows, Linux e Solaris. Você pode baixar o SDK deles
acessando:

   http://java.sun.com/javase/downloads/index.jsp
    Nesta página, você tem a opção de baixar o JDK, JRE, JDK+Java EE, Documentação, Código Fonte e
outras coisas.


 20.2 - Instalando no Ubuntu e outros Linux
     Cada distribuição Linux tem sua própria forma de instalação. Algumas já trazem o Java junto, outras pos-
sibilitam que você instale pelos repositórios oficiais e em alguns casos você precisa baixar direto da Sun e
configurar tudo manualmente.

   No Ubuntu, a distribuição usada na Caelum e a mais usada no mundo, a instalação é bastante simples.
Basta ir no terminal e digitar:


sudo apt-get install sun-java6-jdk


    Há ainda outros pacotes disponíveis para o plugin no navegador (sun-java6-plugin), a documentação (sun-
java6-doc), o código fonte (sun-java6-source) ou apenas o jre (sun-java6-jre).

    Se você usa outra distribuição que não o Ubuntu, consulte a documentação da mesma para saber como
instalar o Java.


 20.3 - No Mac OS X e Solaris

   O Mac OS X já traz o Java instalado junto com o sistema operacional. É uma VM desenvolvida pela própria
Apple e baseada no código da Sun. Atualizações para a VM devem ser obtidas no site da Apple em:


                                                    230


[PAGINA 243]
                                                          Material do Treinamento Java e Orientação a Objetos




   http://developer.apple.com/java/
   O Solaris, por ser da própria Sun, também traz o Java instalado já de fábrica. É a própria VM da empresa,
que pode ser baixada também no site oficial:

   http://java.sun.com/javase/downloads/


 20.4 - Instalação do JDK em ambiente Windows

   Para instalar o JDK no Windows, primeiro baixe-o no site da Sun. É um simples arquivo executável que
contém o Wizard de instalação.


Instalação

1) Dê um clique duplo no arquivo “jdk-<versão>-windows-i586-p.exe” e espere até ele entrar no wizard de
   instalação.




2) Nesta tela, aceite o contrato da Sun, clicando em Accept:




3) Agora, devemos selecionar quais recursos instalaremos junto com o java (ferramentas de desenvolvimento,
   demonstrações, o código fonte e o próprio java) e onde ele será instalado (guarde esse caminho porque
   usaremos ele mais pra frente). Deixe como está e clique em “Next”.




                           Capítulo 20 - Apêndice - Instalação do Java - Instalação do JDK em ambiente Windows - Página 231


[PAGINA 244]
                                                          Material do Treinamento Java e Orientação a Objetos




4) Pronto, agora ele instalará o JDK, apenas aguarde.

5) Agora ele começará a instalar o JRE (Java Runtime Environment), se você já não tiver instalado. Assim
   como o JDK, ele também tem algumas opções. Deixe como está e clique em “Next”.




6) Aguarde até o fim da instalação e clique em Finish.


Configurando

   Precisamos configurar algumas variáveis de ambiente após a instalação.

1) Clique com o botão direito em cima do ícone “Meu Computador” e selecione a opção “Propriedades”.


                           Capítulo 20 - Apêndice - Instalação do Java - Instalação do JDK em ambiente Windows - Página 232


[PAGINA 245]
                                                           Material do Treinamento Java e Orientação a Objetos




2) Agora escolha a aba “Avançado” e depois clique no botão “Variáveis de Ambiente”




3) Nesta tela, você verá, na parte de cima, as variáveis de ambiente do usuário corrente e, embaixo, as variáveis
   de ambiente do computador (servem para todos os usuários). Clique no botão “Nova” da parte de baixo



                            Capítulo 20 - Apêndice - Instalação do Java - Instalação do JDK em ambiente Windows - Página 233


[PAGINA 246]
                                                          Material do Treinamento Java e Orientação a Objetos




4) Agora em “Nome da Variável” digite JAVA_HOME e, em valor da variável, digite o caminho que você anotou na
   instalação do Java. Provavelmente, será algo como: C:\Arquivos de programas\Java\jdk1.6.0_03




   E, depois, clique em OK.

5) Crie uma nova variável de ambiente repetindo o passo 11, porém, agora, defina o nome da variável como
   CLASSPATH e o valor com . (só um ponto).

6) Agora, não vamos criar outra variável, mas sim alterar. Para isso, procure a variável PATH, ou Path (dá no
   mesmo), e clique no botão de baixo “Editar”.




                           Capítulo 20 - Apêndice - Instalação do Java - Instalação do JDK em ambiente Windows - Página 234


[PAGINA 247]
                                                          Material do Treinamento Java e Orientação a Objetos




7) Não altere o nome da variável! Deixe como está e adicione no final do valor ;%JAVA_HOME%\bin, não esqueça
   do ponto-e-vírgula - assim, você está adicionando mais um caminho à sua variável Path.




8) Agora abra o prompt. Vá em Iniciar, Executar e digite cmd.

9) No console, digite javac -version. O comando deve mostrar a versão do Java Compiler e algumas opções.
   Caso isso não aconteça, reveja os passos e confira se não esqueceu ou pulou nenhum deles.




                           Capítulo 20 - Apêndice - Instalação do Java - Instalação do JDK em ambiente Windows - Página 235


[PAGINA 248]
                                                                                            C APÍTULO   21

Apêndice - Debugging
                                                                    “Olho por olho, e o mundo acabará cego.”
                                                                                           – Mohandas Gandhi


 21.1 - O que é debugar
    Debugging (em português, depuração ou depurar) é um processo de reduzir ou encontrar bugs no seu
sistema. De uma forma geral, debugging não é uma tarefa fácil de ser executada. Muitas variações podem
atrapalhar esse processo, por exemplo, a linguagem que estamos utilizando e ferramentas disponíveis para
fazermos debugging de um código.

    O Java em si facilita muito neste processo, pois nos fornece maneiras de sabermos se o código está errado,
por exemplo as exceptions. Em linguagens de baixo nível saber onde o bug estava era extremamente compli-
cado. Outra coisa que facilita nossa vida quando estamos a caça de bug são as ferramentas de debugging.


 21.2 - Debugando no Eclipse
   No curso utilizamos o Eclipse como IDE para desenvolvermos nosso código. Como foi dito ferramentas de
debugging facilitam muito nosso trabalho, o Eclipse é uma das IDEs mais poderosas do mercado e nos fornece
uma ferramenta que torna o processo extremamente simples.

    A primeira coisa que temos que conhecer quando começamos a debugar no Eclipse são os breakpoints.
Eles são pontos de partida em nosso código para iniciarmos o processo de debug. Por exemplo, no código
abaixo, imagine que desejamos debugar o comportamento do método saca da classe Conta, mais especifica-
mente do if que verifica se saldo é menor que o valor a ser sacado. Colocaríamos o breakpoint exatamente
na linha if (this.saldo < valor) {:


package br.com.caelum;

public class Conta {

    private double saldo;

    public boolean saca(double valor) {
        if (this.saldo < valor) {
            return false;
        } else {
            this.saldo = this.saldo - valor;
            return true;
        }
    }

                                                     236


[PAGINA 249]
                                                      Material do Treinamento Java e Orientação a Objetos




}


   Mas como faço isso? Muito simples, basta clicar na linha que deseja adicionar o breakpoint, depois clicar
no menu Run -> Toogle Breakpoint.




    Esse é o tipo mais clássico de breakpoint, veremos alguns outros ao longo do capítulo.

   Agora que já adicionamos o breakpoint que é o ponto de partida, vamos debugar nosso código. Precisamos
rodar nosso código, ou seja, chamar o método saca para que o breakpoint seja encontrado. Teremos um código
similar ao seguinte:


package br.com.caelum;

public class TestaConta {

    public static void main(String[] args) {
        Conta conta = new Conta();
        conta.saca(200);
    }

}


   O processo normal para executarmos esse código seria clicar no menu Run -> Run As -> Java Application.
Porém para rodar o nosso código em modo debug e ativar nosso breakpoint, devemos rodar o codigo no menu
Run -> Debug As -> Java Application. Quando um breakpoint for encontrado no código que está sendo
executado, o eclipse exibirá uma perspectiva específica de debug, apontando para a linha que tem o breakpoint.


                                                 Capítulo 21 - Apêndice - Debugging - Debugando no Eclipse - Página 237


[PAGINA 250]
                                                     Material do Treinamento Java e Orientação a Objetos




 21.3 - Perspectiva de debug
    Temos várias informações disponíveis nessa perspectiva, algumas coisas são essenciais e básicas para
trabalharmos com debug no nosso dia-a-dia, outras não tão relevantes e só usamos em casos muito específicos.

    Dentro da perspectiva de debug, temos uma aba chamada Variables. São exibidas todas as variáveis
encontradas dentro do código que você está debugando. Por exemplo, no debug que fizemos serão exibidas as
variáveis do método saca, neste caso, valor. Além dos atributos de instância do objeto.




                                                 Capítulo 21 - Apêndice - Debugging - Perspectiva de debug - Página 238


[PAGINA 251]
                                                  Material do Treinamento Java e Orientação a Objetos




   Podemos exibir mais informações sobre as variáveis, basta adicionarmos as colunas que desejamos na
tabela exibida.


                                              Capítulo 21 - Apêndice - Debugging - Perspectiva de debug - Página 239


[PAGINA 252]
                                                       Material do Treinamento Java e Orientação a Objetos




   É possível também adicionarmos constantes e variáveis estáticas da classe que está sendo debugada.




   Na aba Breakpoints são exibidos todos os breakpoints que seu workspace possui. Mas por que isso é
importante? É importante porque podemos vemos todos os pontos de debug presentes e melhor, podemos
desabilitá-los um a um ou todos de uma só vez.

   Existem mais alguma opções como exportar um breakpoint para um arquivo, para que depois ele seja
importado que não são muitas utilizadas. O principal aqui são as funcionalidades que foram mencionadas
acima.

   Para desabilitar ou habilitar todos breakpoint basta clicarmos no icone




   Skip All Breakpoints. Se quisermos desabilitar um a um, basta desmarcar o checkbox e o breakpoint será
desativado.

    As vezes encontrar o código onde o breakpoint foi colocado pode ser complicado, na aba Breakpoints isso
fica bem fácil de fazer, basta dar um duplo clique no breakpoint e o eclipse automaticamente nos mostra a classe
“dona” dele.

   Quando estamos debugando código, muitas vezes é interessante saber o valor de alguma expressão
ou método. Por exemplo, uma condição dentro de um if, %this.saldo > valor. Esse valor não está

                                                   Capítulo 21 - Apêndice - Debugging - Perspectiva de debug - Página 240


[PAGINA 253]
                                                    Material do Treinamento Java e Orientação a Objetos




em uma variável, ele está em uma expressão, o que pode tornar saber o valor dela complicado. A
feature de Expressions descomplica esse processo para nós. Na perspectiva de Debug temos a aba
Expressions




   E o resultado da expressão é exibido.

   Temos outra aba importante chamada de Debug. Dentre as funções dela estão:

   • Threads - Exibe as threads que estão sendo executadas, e melhor, mostra qual thread efetuou a chamada
     para o método onde está o debug. Além disso mostra a pilha de execução, o que nos permite voltar a
     chamada de um método

   • Barra de navegação - Que permite executarmos alterarmos os caminhos que o debug seguirá.




                                                Capítulo 21 - Apêndice - Debugging - Perspectiva de debug - Página 241


[PAGINA 254]
                                                  Material do Treinamento Java e Orientação a Objetos




 A tabela a seguir mostrar algumas teclas e botões que alteram o caminho natural dos nosss debug:


                                   Tabela 21.1: Barra de navegação


Comando   Descrição
F5        Vai para o próximo passo do seu programa. Se o próximo passo for um método, ele entrará no código as
F6        Também vai para o próximo passo, porém se o próximo passo for um método, ele não entrará no código
F7        Voltará e mostrará o método que fez a chamada para o código que está sendo debugado. No nosso cas
F8        Vai para o próximo breakpoint, se nenhum for encontrada o programa seguirá seu fluxo de execução nor



 Você também pode usar os botões que estão presentes na aba Debug.




                                              Capítulo 21 - Apêndice - Debugging - Perspectiva de debug - Página 242


[PAGINA 255]
                                                    Material do Treinamento Java e Orientação a Objetos




 21.4 - Degub avançado
   Depois que colocamos um breakpoint em algum ponto do nosso código, podemos colocar algumas proprie-
dades nele, por exemplo, usar alguma condição para restringir quando o breakpoint será ativado em tempo de
execução. Podemos restringir na propriedade Hit Count que o breakpoint só será ativado quando a linha em
que ele encontra-se for executada ‘X’ vezes.




                                                    Capítulo 21 - Apêndice - Debugging - Degub avançado - Página 243


[PAGINA 256]
                                                   Material do Treinamento Java e Orientação a Objetos




   Como na imagem acima o breakpoint só será ativado quando a linha de código em que ele se encontra for
executada ‘2’ vezes. Podemos também colocar alguma expressão condicional, um if, por exemplo.




                                                   Capítulo 21 - Apêndice - Debugging - Degub avançado - Página 244


[PAGINA 257]
                                                         Material do Treinamento Java e Orientação a Objetos




    O breakpoint, neste caso, somente será ativado quando o argumento valor que foi passado ao método
saca for maior que 100. O importante aqui é notarmos que devemos retornar sempre um valor booleano, se
não o fizermos, teremos um erro em tempo de execução. Essa propriedade é válida quando queremos colocar
aqueles famosos System.out.println(“entrou no if tal”) para efeito de log, podemos fazer isso colocando
o log dentro da expressão condicional nas propriedades do breakpoint.

    O display é uma das partes mais interessantes do debug do eclipse, ele provê uma maneira de execu-
tarmos qualquer código que quisermos quando estamos em debugging. Criar uma classe, instanciar objetos
dessa classe, utilizar if’s, for’s, while’s, todos os recursos do Java, além de poder utilizar as variáveis, métodos,
constantes da classe que estamos debugando.

    Um exemplo clássico é quando estamos em debugging e queremos saber o retorno de algum método do
qual não temos acesso, o que faríamos antes seria colocar um amontoado de System.out.println, poluindo
extremamente nosso código. No display o que fazemos é efetuar a chamada desse código e automaticamente
os resultados são exibidos.


                                                         Capítulo 21 - Apêndice - Debugging - Degub avançado - Página 245


[PAGINA 258]
                                                      Material do Treinamento Java e Orientação a Objetos




   Para vermos um efeito real disso, vamos alterar um pouco o comportamento da classe Conta, de modo que
agora o saldo para saque tenha que ser o saldo real mais o valor do limite. Nosso código fica assim:


package br.com.caelum;

public class Conta {

    private double saldoReal;
    private double limite;

    public Conta(double limite) {
        this.limite = limite;
    }

    public boolean saca(double valor) {
        if (!isSaldoSuficiente(valor)) {
            return false;
        } else {
            this.saldoReal = this.saldoReal - valor;
            return true;
        }
    }

    private boolean isSaldoSuficiente(double valor) {
        return (this.saldoReal + this.limite) > valor;
    }
}


   Repare que agora o if que verifica se o saldo é suficiente para efetuarmos o saque chama um método
isSaldoSuficiente, o que pode ser um problema quando estamos debugando, afinal agora a condição do if
é um método. Se utilizarmos o display podemos fazer a chamada do método isSaldoSuficiente, ver seu
resultado e o melhor, não afetamos o debug, apenas queremos ver o resultado do método, por exemplo.

   Para exibirmos a aba Display é bem simples. Tecle Ctrl + 3, digite Display e a aba será exibida. Quando
rodarmos nosso código em modo debug, podemos ir no display, digitarmos uma chamada para o método
isSaldoSuficiente, executamos esse código que foi digitado selecionando-o dentro do display e teclando Ctrl
+ Shift + D e o resultado será impresso, assim como na imagem abaixo:




     Muitas vezes queremos “seguir” alguma variável de instância, ou seja, qualquer chamada para essa variável
(leitura ou escrita) queremos ser notificados disso. Podemos usar o watchpoint, que fará nosso programa entrar
em modo debug, quando qualquer alteração na variável que estamos seguindo ocorrer, o programa entrará em
debug exatamente na linha que fez a alteração. Para colocarmos um watchpoint, basta dar um duplo clique no
atributo de instância que deseja colocá-lo.

                                                     Capítulo 21 - Apêndice - Debugging - Degub avançado - Página 246


[PAGINA 259]
                                                     Material do Treinamento Java e Orientação a Objetos




     É possível alterar esse comportamento padrão, e definir se você quer que o watchpoint seja ativado para
leitura ou somente para escrita.




                                                    Capítulo 21 - Apêndice - Debugging - Degub avançado - Página 247


[PAGINA 260]
                                                    Material do Treinamento Java e Orientação a Objetos




   A idéia desse tipo de breakpoint é fazer nosso programa entrar em debug quando alguma exceção específica
ocorrer. Quando definirmos essa exceção no Exception Breakpoint e a mesma ocorrer, automaticamente
nosso programa entra em debug na linha que gerou aquela exceção.

   Por exemplo, vamos alterar o codigo da classe TestaConta para que a mesma tenha uma
NullPointerException:


package br.com.caelum;

public class TestaConta {

    public static void main(String[] args) {
        Conta conta = null;
        conta.saca(10);
    }

                                                    Capítulo 21 - Apêndice - Debugging - Degub avançado - Página 248


[PAGINA 261]
                                                   Material do Treinamento Java e Orientação a Objetos




}


    É obvio que quando rodarmos o código acima, teremos uma NullPointerException. Pode ser útil nesses
casos debugar e saber onde a exceção está ocorrendo de fato, em qual linha mais especificamente. Para
fazermos isso podemos criar um Exception Breakpoint, que debugará códigos que eventualmente lancem uma
NullPointerException, por exemplo. Basta abrirmos a aba Breakpoints e clicarmos no ícone




    . Será aberta uma janela onde podemos buscar por uma exceção específica.




                                                   Capítulo 21 - Apêndice - Debugging - Degub avançado - Página 249


[PAGINA 262]
Material do Treinamento Java e Orientação a Objetos




Capítulo 21 - Apêndice - Debugging - Degub avançado - Página 250


[PAGINA 263]
                                                    Material do Treinamento Java e Orientação a Objetos




    Podemos definir um breakpoint que é ativado ou antes ou depois que o método é chamado. Para definirmos
ele, basta estar em qualquer parte do método que desejamos debugar, clicar no menu Run -> Toogle Method
Breakpoint. Podemos editar as propriedades desse breakpoint dizendo se queremos que ele seja ativado
antes(default) ou depois da execução do método. Basta acessar as propriedades do method breakpoint e
alterá-las.




    É util quando desejamos que um breakpoint seja ativado quando uma classe específica for carregada pela
primeira vez, chamamos esse breakpoint de Class Breakpoint. Basta clicarmos no menu Run -> Add Class
Load Breakpoint, uma janela será aberta e basta digitarmos o nome da classe e adicionarmos:




                                                    Capítulo 21 - Apêndice - Debugging - Degub avançado - Página 251


[PAGINA 264]
Material do Treinamento Java e Orientação a Objetos




Capítulo 21 - Apêndice - Debugging - Degub avançado - Página 252


[PAGINA 265]
                                                      Material do Treinamento Java e Orientação a Objetos




 21.5 - Profiling
    Um dos principais hábitos que nós desenvolvedores devemos evitar é a questão da otimização prematura, ou
seja, quando desenvolvemos uma aplicação para um cliente, devemos nos preocupar em atender o requisitos
funcionais de maneira mais rápida e mais simples possível. O passo seguinte é refatorar seu código para
que ele seja melhorado e para que no futuro possa se adaptar as possíveis mudanças.

   A regra é: “Deixe os problemas do futuro, para serem resolvidos no futuro”.

    Uma das ferramentas que nos auxiliam na questão de não otimizar nosso código prematuramente, são as
ferramentas de profiling, que tornam aparentes, por exemplo, os problemas de memória e cpu, que podem fazer
com que otimizemos nosso código. Atualmente devido as técnicas que utilizamos para entregar algo de valor
para o cliente, focamos principalmente na qualidade, aspectos funcionais, testes, etc. Porém, muitos problemas
que não fazem parte dos requisitos funcionais podem acontecer apenas quando a aplicação está em produção,
neste ponto as ferramentas de profiling também nos ajudam.


 21.6 - Profiling no Eclipse
    Juntamente com o Eclipse temos a opção de instalar e utilizar uma ferramenta de profiling conhecida como
Eclipse TPTP(Eclipse Test & Performance Tools Platform), que nos fornece opções para isolar e identificar pro-
blemas de performance, tais como: memória (memory leak), recursos e processamento. O TPTP nos permite
analisar de simples aplicações java até aplicações que rodam em múltiplas máquinas e em múltiplas platafor-
mas.

             Alternativas ao TPTP
            Existem algumas alternativas ao TPTP, os mais conhecidos são Netbeans Profiler (http://profiler.
            netbeans.org/) que é gratuito, e o JProfiler (http://www.ej-technologies.com/products/jprofiler/
            overview.html) que é pago.


  O TPTP não vem por padrão junto com o Eclipse. Portanto, para utilizarmos é necessário a instalação do
mesmo. Podemos fazer o processo de instalação de duas maneiras.

   A primeira e mais fácil é utilizando o Update Site do Eclipse que resolve as possíveis dependências e nos
possibilita escolher quais features queremos instalar. Para instalar o TPTP através desse recurso, basta ir no
menu: Help -> Install New Software, uma janela será aberta, basta clicar em Add... e preenchê-la conforme a
imagem a seguir:




                                                             Capítulo 21 - Apêndice - Debugging - Profiling - Página 253


[PAGINA 266]
                                                   Material do Treinamento Java e Orientação a Objetos




   Agora basta adicionar as ferramentas do TPTP em nosso eclipse, para isto, selecione o repositório que
acabamos de adicionar e a versão do TPTP que queremos instalar, neste caso, a versão 4.6.2.




                                                 Capítulo 21 - Apêndice - Debugging - Profiling no Eclipse - Página 254


[PAGINA 267]
                                                     Material do Treinamento Java e Orientação a Objetos




             Instalando pelo Zip
           Você tem a opção de instalar o TPTP baixando o zip do projeto e colocando manualmente no
           diretório de instalação do seu eclipse. Mais informações no link: http://www.eclipse.org/tptp/
           home/downloads/4.6.0/documents/installguide/InstallGuide46.html


   Um problema que pode acontecer em aplicações e que muitas pessoas não conhecem a fundo, é a questão
do pool de Strings que pode eventualmente ficar muito grande. Este problema pode ser causado porque objetos
do tipo String são imutáveis, sendo assim, se fizermos concatenações de Strings muitas vezes, cada uma
dessas concatenações produzirá uma nova String, que automaticamente será colocada no pool da JVM.

   A alternativa neste caso, seria trabalhar com objetos do tipo StringBuilder ou StringBuffer que funcionam
como Strings, mas que não produzem Strings novas em caso de uma concatenação. Mas como medir a tama-
nho do nosso pool de String?

    O TPTP possui uma aba de estatísticas que nos mostra o tempo que um método levou para ser executado,
quando processamento esse método gastou, quanto de memória foi gasto com cada método. Vamos analisar
algumas desses estatísticas criando um código que concatene várias Strings, de maneira que sobrecarregue o
pool, gere bastante processamento e consumo de memória.


                                                   Capítulo 21 - Apêndice - Debugging - Profiling no Eclipse - Página 255


[PAGINA 268]
                                                    Material do Treinamento Java e Orientação a Objetos




public class Teste {

    public static void main(String[] args) {
        for (int i = 0; i < 1000000; i++) {
            String x = "a" + i;
            System.out.println(x);
        }
    }

}


    Para analisarmos o resultado do código, vamos rodar o código do main através do menu Run -> Profile As
-> Java Application.


             Problemas
           Infelizmente o TPTP funciona somente no Windows. Versões para MacOS e Linux são prometidas,
           mas até hoje não existem.




                                                  Capítulo 21 - Apêndice - Debugging - Profiling no Eclipse - Página 256


[PAGINA 269]
Índice Remissivo

ABSTRACT, 100                       ELSE, 21
ANT, 147                            ENCAPSULAR, 60
ARGUMENTO, 32                       ENTRADA E SAÍDA, 171
ARQUIVOS, 171                       EQUALS, 161
ARRAY, 49                           ESCOPO, 24
atomicidade, 212                    EXCEPTION, 123
ATRIBUIÇÃO, 17                      Exception Breakpoint, 248
ATRIBUTO, 31                        Expressions, 240
AUTOBOXING, 163
                                    FILEINPUTSTREAM, 172
boolean, 16                         finalizer, 210
BREAK, 23                           FINALLY, 135
Breakpoint de classe, 251           FOR, 22
Breakpoint de Método, 251           FULL QUALIFIED NAME, 141
Breakpoints, 236, 240
bytecode, 6                         Garbage Collector, 209
                                    GETTERS, 62
CASTING, 19                         GUJ, 4
CASTING DE REFERÊNCIAS, 159
CHAR, 16                            HASHMAP, 199
CLASSE, 30                          HASHTABLE, 199
CLASSE ABSTRATA, 100                HERANÇA, EXTENDS, 73
COLLECTIONS, 183
                                    IF, 20
Começando o debug, 237
                                    IMPLEMENTS, 110
COMPARABLE, 188
                                    IMPORT, 142
COMPARE TO, 165
                                    INPUTSTREAM, 172
COMPOSIÇÃO, 80
                                    INPUTSTREAMREADER, 172
CONDIÇÃO BOOLEANA, 20
                                    Instalando, 253
CONSTRUTOR, 64
                                    int, 14
CONTINUE, 23
                                    INTERFACE, 110
CONTRATO, 110
                                    INVOCAÇÃO DE MÉTODO, 33
CTRL+ESPAÇO, 144
                                    ITERATOR, 197
Debug, 241
Decorator Pattern, 173              JAVA.IO, 171
Display, 245                        JAVA.LANG, 157
DOUBLE, 16                          java.lang.Object.finalize, 210
                                    java.lang.System.gc, 210
Eclipse, 86                         java.util.concurrent, 212

                              257


[PAGINA 270]
                                  Material do Treinamento Java e Orientação a Objetos




JAVADOC, 152                          TCP, 218
juc, 212                              Testando, 255
                                      THIS, 33
LAÇO, 22                              THROWS, 128
                                      TOSTRING, 160
MÁQUINA VIRTUAL, 5
                                      TREEMAP, 199
MÉTODO, 32
MÉTODO ABSTRATO, 102                  VALORES DEFAULT, 39
MAIN, 10                              Variáveis, 238
MAP, 195                              variáveis, 14
MATH, 166                             VOID, 32
MATRIZ, 49
MODIFICADOR DE ACESSO, 59             Watch Point, 246
                                      WHILE, 22
NEW, 31                               WRAPPING, 163
NULL, 41

OBJECT, 158
OPERADOR DE NEGAÇÃO, 21
OPERADORES ARITMÉTICOS, 15
OPERADORES LÓGICOS, 21
ORIENTAÇÃO A OBJETOS, 28

PACKAGE, 140
PACOTES, 139
PARÂMETRO, 32
plataforma java, 3
POLIMORFISMO, 77
PORTA, 219
PRIVATE, 58
Propriedades de Breakpoint, 243
PROTECTED, 74
PUBLIC, 59

REESCRITA, 76
REESCRITA DE MÉTODO, 75
REFERÊNCIA, 35
região crítica, 211
RETURN, 34

SERVERSOCKET, 220
SET, 193
SETTERS, 62
SOBRECARGA, 108
SOCKETS, 171
SPLIT, 165
STACKTRACE, 123
STATIC, 67
sun, 3
Super e sub classes, 74
SYSTEM.EXIT, 158


                                                 Índice Remissivo - Índice Remissivo - Página 258
