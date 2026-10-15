# RESOLUCAO_DO_PLANO_DE_ESTIVA_INTEGRADO_A

Arquivo original: most_similar_papers_to_this_one/RESOLUCAO_DO_PLANO_DE_ESTIVA_INTEGRADO_A.pdf
SHA-256 do original: 0182041221677b2cf8eea7aadeaeeaf5365ebed49b16196f6e528a0a6ea95c32

Texto extraido para consulta. As paginas abaixo usam a ordem do arquivo PDF, incluindo capas.
Parte preparada: 1/1


[PAGINA 1]
     RESOLUÇÃO DO PLANO DE ESTIVA INTEGRADO À PROGRAMAÇÃO DE
        GUINDASTES PORTUÁRIOS VIA REPRESENTAÇÃO POR REGRAS



                                 Anibal Tavares de Azevedo
                                          UNICAMP
                                anibal.azevedo@fca.unicamp.br

                                 Luiz Leduino de Salles Neto
                                           UNIFESP
                                   luiz.leduino@unifesp.br

                                  Antônio Augusto Chaves
                                          UNIFESP
                                  antonio.chaves@unifesp.br

                                   Antônio Carlos Moretti
                                         UNIFESP
                               antonio.moretti@fca.unicamp.br




                                          RESUMO
A eficiência de um terminal portuário depende um planejamento apropriado da movimentação de
contêineres, também chamado de plano de estiva. A partir do plano de estiva é possível estimar o
tempo, e assim também o custo, para realizar os processos de carregamento e descarregamento de
contêineres de um navio. Para tanto, este artigo propõe uma nova abordagem para resolver o
problema de planejamento de estiva 3D integrado ao problema de programação ou scheduling de
guindastes portuários. Ambos os problemas são NP-Hard e demanda grande número de variáveis
binárias para representar uma solução em uma formulação inteira. A alternativa empregada neste
trabalho é a aplicação sucessiva da representação por regras para o problema de estiva e o
programação de guindastes portuários com um algoritmo genético. Soluções para problemas de
grande porte que demandam aproxidamente 44 milhões de restrições e 42 milhões de variáveis
são obtidas em menos de 15 minutos.




PALAVARAS-CHAVE: Plano de estiva, Programação de Guindastes Portuários,
Representação por Regras, Algoritmo Genético.


[PAGINA 2]
1. Introdução
          De acordo com (Guan et al. 2013; Steenken et al. 2004), as operações em um terminal
portuário de contêineres podem ser divididas em cinco problemas principais:

         (1) Alocação de berços: a saída deste problema é a programação de qual navio será
             atendido em qual berço de modo que uma distância mínima de segurança seja
             respeitada entre dois navios, e dois navios não podem compartilhar o mesmo berço
             no mesmo período de tempo;
         (2) Plano de estiva: este problema consiste em determinar como organizar os
             contêineres em um navio de modo a minimizar o número de movimentos de
             carregamento e descarregamento;
         (3) Designação de Guindastes no Cais: o tempo que o navio porta-contêiner leva para
             carregar ou descarregar depende da programação de guindastes portuários alocados
             para cada seção do navio. Os guindastes não podem ultrassapar uns aos outros por
             terem seus movimentos limitados a um trilho comum. Além disso, uma distância de
             segurança entre eles também deve ser observada;
         (4) Transporte do Cais: é necessário determinar que máquinas serão empregadas e
             quais serão suas trajetórias ligando o navio ao pátio do porto e vice-versa;
         (5) Transporte do Pátio: A organização de pilhas no pátio do porto depende de como
             realizar operações eficientes para empilhar e desempilhar os contêineres que são
             trazidos ou levados por caminhões e trens.

          Este trabalho irá abordar a resolução conjunta dos problemas (2) e (3). Para a resolução
do problema (2) é necessário definir um plano de estiva que é fortemente relacionado com a
estrutura especial do navio porta-contêiner como dado na Figura 1.




         Figura 1: Estrutura de um navio porta-contêiner (Source: Wilson and Roach 2000).

          O passo seguinte ao plano de estiva, é a definição da programação de guindastes
portuários tal como dado na Figura 2.


[PAGINA 3]
         Figura 2: Problema de programação de guindastes portuários (Source: Lee et al. 2008).

           Para evidenciar a complexidade de realizar a otimização conjunta de tais problemas, na
   literatura são encontradas ou abordagens que tratam do problema de estiva (Ambrosino et al.,
   2006 e 2010; Avriel et al., 1993, 1998; Botter e Brinati, 1991; Dubrovsky et al., 2002; Fan et
   al., 2010, Imai et al., 2006; Wilson e Roach, 2000) ou do problema de programação de
   guindastes portuários (Guan et al., 2013; Homayouni et al., 2011; Javanshir e Ganji, 2010;
   Lee et al, 2008; Legato et al., 2008; Mak e Sun, 2009). A otimização conjunta desses dois
   problemas é a contribuição original deste artigo.


2. Modelo Matemático
         O mesmo modelo adotado para o plano de estiva em (Azevedo et al. 2012) será
empregado neste artigo de modo que apenas a descrição do que as restrições representam será
apresentada aqui. As seguintes considerações foram adotadas:

  (a) O navio porta-contêiner possui um formato rectangular e pode ser representado por uma
matriz com linhas (r = 1, 2,…, R), colunas (c = 1, 2, …, C) e baias (d = 1, 2,…, D) totalizando
uma capacidade máxima de R x C x D contêineres;

   (b) Todos os contêineres possuem o mesmo peso e tamanho;

   (c) Todos os navios começam a ser carregados no porto 1 e sem nenhuma carga inicial;

   (d) O navio visita os portos 2, 3, …, N tal que o navio estará vazio no último porto, pois é
considerado que o mesmo realiza uma rota circular onde o porto N, na verdade, representa o
porto 1;

   (e) Em cada porto i = 1, 2, …, N, o navio deve ser carregado com contêineres cujo destino são
portos i+1, …, N.

   (f) O navio porta-contêineres pode sempre carregar todos os contêineres disponíveis em cada
porto e isto não irá exceder sua capacidade máxima.

   A formulação matemática correspondente às restrições (a)-(f) estão descritas no modelo
matemático dado pelas Eqs (1)-(8).


[PAGINA 4]
        f ( x) = ฀฀1 ( x) + ฀฀2 ( y )
Min                                                                                                                        (1)

s.a:      j     R    C          D                 i ฀1 R     C      D

        ฀ ฀ ฀ ฀ x ( r , c, d ) ฀ ฀ ฀ ฀ ฀ x ( r , c, d ) = T
       v = i +1 r =1 c =1 d =1
                                     ijv
                                                  k =1 r =1 c =1 d =1
                                                                          kji   ij

                                                                                     i = 1,, N ฀ 1, j = i + 1,, N ;      (2)

          j     N           j                                                        i = 1,, N ฀ 1, r = 1,, R;
       ฀ ฀ ฀ x ( r , c, d ) = y ( r , c, d )
        k =1 j = i +1 v = i +1
                                    kjv                i

                                                                                     c = 1,, C ; d = 1,, D               (3)


        yi (r , c, d ) ฀ yi (r + 1, c, d ) ฀ 0                                       i = 1,, N ฀ 1, r = 1,, R ฀ 1;

                                                                                     c = 1,, C ; d = 1,, D               (4)

        j ฀1 N                             j ฀1    N        p                        i = 2,, N , r = 1,, R ฀ 1;
       ฀ ฀ x (r , c, d ) + ฀ ฀ ฀ x (r + 1, c, d ) ฀ 1
        i =1 p = j
                      ipj
                                           i =1 p = j +1 v = j +1
                                                                    ipv

                                                                                     c = 1,, C ; d = 1,, D               (5)


        xijv (r , c, d ) = 0 ou 1 ; yi (r , c, d ) = 0 ou 1                          i, j , v = 1,  , N , r = 1,  , R;   (6)

                                                                                     c = 1,, C ; d = 1,, D



        onde: a variável binária xijv (r , c, d ) é definida de forma que assume o valor 1 se existir
um contêiner no compartimento (r, c, d) que foi ocupado no porto i e tem como destino final o
porto j e movido no porto v; caso contrário assume valor zero. Por compartimento (r, c, d)
entende-se a linha r, a coluna c e a baia d no compartimento de carga do navio. É necessário
salientar que a numeração das linhas é feita de baixo para cima, assim a linha de número 5 está
acima da linha de número 4, a numeração das colunas é feita da esquerda para a direita e a
profundidade é iniciada da popa até a proa. Similarmente, a variável yi (r , c, d ) possui valor 1 se
saindo do porto i o compartimento (r, c, d) for ocupado por um contêiner; caso contrário assume
valor 0.
         A restrição (2) é a restrição de conservação de fluxo, onde T ij é o elemento da matriz de
transporte que representa o número de contêineres que embarcam no porto i com destino ao porto
j. A restrição (3) garante que cada segmento de rota tem pelo menos um único contêiner. A
restrição (4) é necessária para garantir que existem contêineres embaixo do contêiner que ocupa o
compartimento (r, c). A restrição (5) é responsável por definir a movimentação dos contêineres:
se um contêiner que ocupa a posição (r, c, d) é descarregado no porto j, então, ou não existem
contêineres acima dele, ou o índice v do contêiner que ocupa o compartimento (r+1, c, d) não é
maior que j. A função objetivo da Eq. (1) possui é uma composição de dois diferentes critérios: o
primeiro depende da movimentação dos contêineres, ฀1 ( x) , e o segundo depende posição
ocupada pelos contêineres em cada porto, ฀2 ( y ) . Os dois critérios podem ser combinados
através de valores escalares fornecidos para os pesos ฀e ฀dentro de um modelo de otimização
bi-objetivo.


[PAGINA 5]
        O termo ฀1 ( x) relativo ao custo total de movimentação dos contêineres (assumindo que a
movimentação de um contêiner possui um custo unitário e igual para todos os portos) em todos
os portos é dado pela Eq. (7).

                                                   N ฀1   N     j ฀1 R     C      D
                                         ฀1s ( x) = ฀ ฀ ฀ ฀ ฀ ฀ x s (r , c, d )         ijv
                                                   i =1 j =i +1v =i +1 r =1 c =1 d =1         (7)



         O termo ฀2 ( y ) é relativo à estabilidade do navio de acordo com a posição dos
                     s

contêineres (assumindo que cada contêiner possui um peso unitário e igual para todos os portos)
em todos os portos no cenário s e é dado pela Eq. (8).

                         N    D                       D                                             (8)
            ฀2s ( y ) = ฀ ฀ (฀xcmdis ) + ฀ (฀zcmdis )
                                               2                            2

                         i =1 d =1                   d =1




    onde:   ฀zcmdis = zcmdis ฀ R / 2 ,             ฀xcmdis = xcmdis ฀ C / 2 e


                      ฀R C                             ฀ ฀R C                 ฀
                                     (                                    )
             zcmdis = ฀฀ ฀ yis (r , c, d ) ฀ (r ฀ 0.5) ÷ ฀฀ ฀ yis (r , c, d ) ÷
                      ฀r =1 c =1                       ฀ ฀r =1 c =1           ฀

                      ฀C R                              ฀ ฀R C                  ฀
                                     (                                        )
             xcmdis = ฀฀ ฀ yis ( r , c, d ) ฀ (c ฀ 0.5) ÷ ฀฀ ฀ yis ( r , c, d ) ÷
                      ฀c =1 r =1                        ฀ ฀r =1 c =1            ฀

   Observe na Eq. (8), que em cada cenário s para se calcular a soma dos desvios ฀xcmdis e
฀zcmdis entre as coordenadas do centro de massa ( xcmds , zcmds ) e as coordenadas do centro
geométrico (R/2,C/2) de cada baia d, é necessário calcular as coordenadas do centro de massa
xcmdis e zcms di , relativas respectivamente ao eixo das colunas c e linhas r de cada baia d.

   Para a programação dos guindastes portuários o modelo descrito em (Lee et al. 2008) foi
adotado e as seguintes considerações foram realizadas sob a forma de restrições e função
objetivo:

   (a) Ao invés de se considerar o navio dividido em seções como em (Lee et al. 2008), foi
considerada cada baia do navio. Dessa forma, é possível transformar a informação de
movimentação de contêineres fornecida pelo plano de estiva sob a forma do total de esforço
necessário por baia;

   (b) Foi assumido que o esforço total equivale ao número de contêineres que devem ser
movidos e que cada container demanda uma unidade de tempo para ser carregado ou
descarregado;

   (c) Cada baia no navio só pode ter um único guindastes em um dado período de tempo;


[PAGINA 6]
  (d) Uma vez que um guindaste começou o serviço (carregamento ou descarregamento) em
uma baia, o mesmo só irá parar quando não houver mais serviço para realizar;

   (e) Quando um guindaste troca sua operação de uma baia para outra, ele leva um tempo
constante e igual a três unidades de tempo para mover um contêiner;
   (f) Uma distância minima entre os guindastes deve ser observada. Isto significa que, às vezes,
um guindaste não pode ser movido e não pode começar o seu serviço até que um segundo
guindaste termine o seu trabalho e mova-se para uma nova posição que garanta a distância
mínima entre os guindastes;

   (g) Um guindaste não deve ultrapassar outro, pois eles compartilham o mesmo trilho;

  (h) Todos os guindastes possuem a mesma e constant taxa de serviço de movimentação de
uma unidade de trabalho por unidade de tempo.

   O modelo matemático em termos de programação linear com variáveis binárias para o
problema de programação de Guindastes Portuários proposto por (Lee et al. 2008) é dado pelas
Eqs. (9)-(21).


   Min ฀                                                                                                                                (9)
   tx jt ฀ ฀ ,                                                                                        j = 1,...,S; t = 1, ..., T       (10)
   w jt ฀ Mx jt ฀ 0 ,                                                                                 j = 1,...,S; t = 1, ..., T       (11)
   w jt ฀1 ฀ ฀y tj฀, 1j , t ฀ w jt ,                                                                  j = 1,...,S; t = 2, ..., T       (12)

   z tj,,tj++11 + z tj,,tj+฀11 + z tj,,tj+1 = b j ,                                                   j = 1,...,S; t = 1               (13)

   z tj฀฀11,,tj + z tj฀, 1j , t + z tj฀+11,,t j ฀ z tj,,tj++11 ฀ z tj,,tj+฀11 ฀ z tj,,tj+1 = 0 ,      j = 1,...,S; t = 2, ..., T-1     (14)

   z tj฀฀11,,tj + z tj฀, 1j , t + z tj฀+11,,t j = z tj,,tj++11                                        j = 1,...,S; t = T               (15)
    S                      S                                                                          t=T+1                            (16)
   ฀ z tj฀,11,t = ฀ b j ,
    j =1                  j =1

   z   t ฀1, t
                 +z   t ฀1, t
                                + z tj฀+11,,t j ฀ 1                                                   j = 1,...,S; t = 2, ..., T       (17)
       j ฀1, j        j, j

   z tj฀฀11,,tj + z tj฀, 1j , t ฀ 1                                                                   j = 1,...,S; t = 2, ..., T       (18)

   y tj฀, 1j , t ฀ z tj฀, 1j , t ฀ 0                                                                  j = 1,...,S; t = 2, ..., T       (19)

   y tj฀, 1j , t + x jt ฀ y tj,,tj+1 ฀ 1                                                              j = 1,...,S; t = 2, ..., T-1     (20)

   w jt ฀ 0 with w j1 = W j , x jt , y tj,,tj+1 , z tj,,tj+, 1' ฀ [0,1].                           j , j' = 1,...,S; t = 1, ..., T-1   (21)


   Onde: M é um valor grande, t é o índice relativo aos períodos de tempo, T é o horizonte de
tempo que pode ser qualquer valor maior que o Makespan ฀, ฀é uma ponderação acerca da carga
de trabalho em uma dada seção j no período t, b j = 1 se um guindaste está originalmente
localizado na seção j e 0 caso contrário, W j é a carga inicial de trabalho na seção j.
   Para o modelo dado pelas Eqs (9)-(21) as seguintes variáveis de decisão foram consideradas:

   (i) Uma variável binária x jt tem valor 1, se ainda existir carga de trabalho na baia j no
           início do período t e 0, caso contrário;
   (ii) A variável inteira w jt representa a carga de trabalho remanescente na baia j no início do
                  período de tempo t;


[PAGINA 7]
   (iii) A variável inteira z tj,,tj+'1 representa o número de guindastes que se movem da baia j para a
           baia j’ durante o período de tempo t;
   (iv) A variável inteira y tj,,tj+1 representa o número de guindastes na baia j durante o período de
           tempo t.

   A função objetivo consiste na minimização do tempo necessário para terminar os serviços no
navio, incluindo movimentos de carregamento e descarregamento, e mudança de posição do
guindaste. Assim, a função objetivo é a minimização do makespan. A restrição (10) determina
que o tempo de término da última unidade de trabalho, i.e., o makespan. A restrição (11)
estabelece a existência ou não da carga de trabalho restante na seção j no tempo t. A restrição
(12) representa o balanceamento do fluxo de carga de trabalho da seguinte forma: para cada
seção j existe uma carga inicial de trabalho w j1 = W j . Para cada período de tempo escolhido, a
carga de trabalho remanescente será reduzida em unidades ฀antes de atingir zero, se houver um
guindaste portuário operando durante o período de tempo selecionado. As restrições (13) até (16)
são relativas a conservação do fluxo de guindastes. A restrição (17) indica que para cada unidade
de tempo, cada seção pode comportar no máximo um único guindaste. A restrição (18) indica que
um guindaste não pode cruzar outro. A restrição (19) indica que o guindaste que um guindaste
pode permanecer inativo em uma seção j durante um período t. Finalmente, a restrição (20)
representa restrições de não-preempção, isto é, um guindaste não pode começar uma nova tarefa
até que a tarefa atual para qual foi alocado esteja terminada.

   Deve ser destacado que os modelos matemáticos são apresentados para ilustrar a
complexidade e o modo com os dois problemas podem ser acoplados. Neste sentido, pela
primeira vez na literatura, os dois modelos descritos anteriormente foram acoplados ao se utilizar
baias ao invés de seções no problema dos guindastes. Dessa forma, foi possível empregar a
observação de que o resultado do problema de estiva (P), o número de movimentos por baia,
pode ser transformado na entrada do problema de operação de guindastes (O), o esforço total por
baia, tal como dado na Fig. 3.




         Figura 3: Acoplando o plano de estiva (P) com a operação de guindastes (O).

     É importante observar que ao realizar o acoplamento entre o plano de estiva (P) e a operação
de guindastes (O), a resolução do problema (P) dependerá, em cada porto, da resolução do
problema de guindastes (O). Assim, uma instância que considere um problema conjunto de (P) e
(O) com um horizonte de 30 portos deverá resolver não só o problema (P) dado pelas Eqs. (1)-
(8), mas, também, 60 sub-problemas (O) dado pelas Eqs. (9)-(21). Isto se deve ao fato de que, no
problema conjunto, as operações de carregamento e descarregamento em cada porto devem ser
realizadas através da programação e operação de guindastes portuários.


[PAGINA 8]
3. Método de Solução
     Como demonstrado em (Avriel e Penn 2000), o modelo matemático com variáveis binárias
para o problema de estiva (P) não é adequado para problemas de grande porte. Caso a
representação por variáveis binárias seja empregada, mesmo com a adoção de meta-heurísticas, o
número de variáveis a serem empregadas cresce de forma proibitiva. No artigo (Azevedo et al.
2012, 2014), ao invés de empregar uma meta-heurística que usa variáveis binárias, é empregada
uma representação alternativa na resolução do problema de estiva (P) através integrada dos dois
problemas através da representação por regras. Neste artigo, além de empregar a representação
por regras, pela primeira vez, também para o problema de operação de guindastes (O), estas
foram combinadas às regras do problema de estiva (P) para permitir a resolução integrada de
ambos os problemas. A combinação entre as regras para carregamento e descarregamento de
navios descritas em (Azevedo et al. 2012, 2014) com quatro regras de operações de guindastes
tal como dado na Tabela 1.

RG                                               Q1
RC         C1            C2        C3       C4        C5         C6        C7       C8
RD    D1        D2 D1 D2 D1 D2 D1 D2 D1 D2 D1 D2 D1 D2 D1 D2
 R    1          2    3     4    5    6   7     8   9    10 11 12 13 14 15 16
                Tabela 1: Regras produzidas pela combinação das regras de carregamento,
                        descarregamento e movimentação de guindastes portuários.

        Na Tabela 1, RG representam as regras de alocação de guindastes, RC as regras de
carregamento, RD as regras de descarregamento e R as regras finais que são combinações das
demais. A Tabela 1 mostra apenas as primeiras 16 combinações das 64 possíveis de regras finais,
pois foram utilizadas 4 regras de programação de guindastes.
         A Fig. 4 ilustra o passo-a-passo do funcionamento de uma das regras de operação de
dois guindastes portuários.




(A) Programação inicial de dois guindastes.           (B) Manter distância mínima de segurança.




(C) Movimento        sincronizada   entre   os   dois (D)A regra de movimentação é tal que respeita a
guindastes.                                           restrição de distância mínima de segurança.


[PAGINA 9]
(E) Fim de serviço no guindaste 2, mas não no 1. (F) Tempo total é a operação dos dois guindastes.
Figura 4: Descrição detalhada do funcionamento da regra 1 de operação de dois guindastes
portuários.

           Apesar do uso da representação por regras reduzir consideravelmente a complexidade
do problema a ser resolvido, a decisão de qual regra, das que estão descritas naTabela 1, deve ser
aplicada em cada porto resulta em um problema combinatório. Para um problema que considera
um horizonte de 30 portos, existem 6430, ou seja, aproximadamente 1,54 x 1054, possíveis
soluções. Assim, emprega-se um algoritmo genético para resolver o problema combinatório
resultante.
           A estrutura do algoritmo genético empregado neste trabalho é similar a descrita em
(Azevedo et al., 2014), com a única diferença em relação à codificação que mapeia as soluções e
os indivíduos da população.
           Uma representação compacta da solução pode ser realizada através de um vetor S cujo
elemento s[j] de valor igual a k indica qual regra (daquelas fornecidas na Tabela 1) foi utilizada
para o porto j tal como dado na Figura 3. Então, no exemplo da Figura 5, tem-se que no porto 1,
foi utilizada a regra 4, no porto 2 a regra 3 e assim sucessivamente.
                                                       P1 4
                                                       P2 3
                                                       P3 2
         Figura 5: Codificação do algoritmo genético para relacionar indivíduos e soluções.

         A diferença entre a codificação apresentada em (Azevedo et al., 2014) e a deste artigo é
que agora as regras não só definem a disposição dos contêineres no navio, mas, também, como
deverá ser realizada a operação dos guindastes portuários, tal como ilustrado na Figura 4.


4. Resultados Computacionais
          Foram obtidos resultados para instância com até cerca de 44 milhões de restrições e 42
milhões de variáveis binárias utilizando um programa criado em Matlab 7.0, e uma máquina com
um processador 1.66 GHz Core Duo Intel Processor, memória RAM memory de 2 GB e sistema
operacional Windows Vista Operational System com Service Pack 2.Duas funções objetivos
foram testadas: uma que busca minimizar o tempo total de operação (Fig. 6) e outra que busca
minimizar a instabilidade do arranjo dos contêineres no navio (Fig. 7) para uma instância que
considera a movimentação de cargas para um número de portos igual a 30. Sem perda de
generalidade foi suposto que o tempo de deslocamento do guindaste de uma baia para outra e o
tempo de movimentação de uma carga seja para carga ou descarga no navio são iguais. Também
foi suposto que os pesos e as dimensões de todos os contêineres são iguais. Além disso, tanto o
problema de estiva (Fig. 6(A), (C); Fig. 7(A), (C)) quanto o problema de alocação de guindastes
(Fig. 6(B), (D); Fig. 7(B), (D)) foram resolvidos de forma integrada, isto é, a resolução do
problema de estiva (P) observa o impacto da aplicação das regras em termos do problema de
alocação de guindastes (O). As soluções mostradas nas Figuras 6 e 7 correspondem aos melhores
valores de função objetivo obtidos para a minimização do número de movimentos e a
minimização da instabilidade das baias dos navios, respectivamente.


[PAGINA 10]
   (A) Minimizando movimentos.                   (B) Operação resultante de (A) no porto 2.




    (C) Minimizando movimentos.                 (D) Operação resultante de (C) no porto 3.
Figura 6: Solução em termos plano de estiva e operação de guindastes para (฀, ฀)=(1, 0) na Eq.
(1) de modo a minimizar o número de movimentos.




      (A) Minimizando instabilidade.              (B) Operação resultante de (C) no porto.




       (C) Minimizando instabilidade.             (D) Operação resultante de (C) no porto.
Figura 7: Solução em termos plano de estiva e operação de guindastes para (฀, ฀)=(0, 1) na Eq.
(1) de modo a minimizar a instabilidade.

    Para o problema com maior número de portos, isto é trinta, foi possível resolver o problema
de modo a obter soluções factíveis, bem como melhorar sua qualidade, em menos de 15 minutos,
mesmo que o problema resultante tenha dimensão de 44 milhões de restrições e 42 milhões de
variáveis apenas para o problema de estiva.


[PAGINA 11]
5. Conclusões e perspectivas futuras
          Neste trabalho, foi apresentado pela primeira vez, a resolução conjunta do problema de
estiva e de alocação de guindastes, isto é, determinar o arranjo dos contêineres em um navio, mas
de modo a observar o correspondente impacto em termos de tempo de operação dos guindastes.
Para tanto, a representação por regras foi extendida para ser aplicada não só no problema do
plano de estiva, mas também para determinar a programação de guindastes em um terminal
portuário de contêineres. A metodologia proposta conseguiu obter soluções para problemas cujo
modelo matemático correspondente possui cerca de 44 milhões de restrições e 42 milhões de
variáveis em menos de 15 minutos. Diante da velocidade computacional para obter soluções
factíveis e de boa qualidade para problemas complexos integrados, uma perspectiva futura é
ampliar a utilização da representação por regras de modo a incluir outras operações portuárias
tais como a movimentação de contêineres no pátio do porto, bem como considerar diferentes
tipos de contêineres em termos de pesos, dimensões e conteúdo (carga tóxica, refrigerada, dentre
outros).
       Agradecimentos à FAPESP pelo apoio financeiro através dos processos 2010/51274-5 e
2014/03258-1.




Referências
Ambrosino, D., Schiomachen, A., Tanfani, E., (2006). A decomposition heuristics for the
   container ship stowage problem”, Journal of Heuristics 12, pp. 211-233.
Ambrosino, D., Anghinolfi, D., Paolucci, M., Sciomachen, A. (2010). An Experimental
   Comparison of Different Heuristics for the Master Bay Plan Problem, Lecture Notes in
   Computer Science 6049, pp. 314-325.
Avriel, M., Penn, M., (1993). Container ship stowage problem, Computers and Industrial
   Engineering, 5, pp. 271-274.
Avriel, M., Penn, M., Shpirer, N., Wittenboon, S. (1998). Stowage planning for container ships to
   reduce the number of shifts, Annals of Operations Research 76, pp. 55-71.
Avriel, M., Penn, M., Shpirer, N. (2000). Container ship stowage problem: complexity and
   connection to the coloring of circle graphs, Discrete Applied Mathematics 103, pp. 271-279.
Azevedo, A., Ribeiro, C., Sena, G., Chaves, A., Salles, L., Moretti, A. (2012). Solving the 3D
   Container Ship Loading Planning Problem by Representation by Rules and Beam Search, in
   ICORES’12, pp. 132-141.
Azevedo, A., Ribeiro, C., Sena, G., Chaves, A., Salles, L., Moretti, A. (2014). Solving the 3D
   Container Ship Loading Planning Problem by Representation by Rules and Meta-heuristics,
   International Journal of Data Analysis Techniques and Strategies – Special issue on:
   'Optimization and Simulation Real-life Scenarios', Vol. 6, no. 3, pp. 228-260.
Botter, R., Brinati, M., (1991). Stowage Container Planning: a model for get-ting optimal
   solution. In: International Conference of Computer Applications in the Automation of Ship-
   yard Operation and Ship Design, Rio de Janeiro, pp. 217-229.
Dubrovsky, O.; Levitin, G., Penn, M. (2002). A Genetic Algorithm with a Compact Solution
   Encoding for the Containership Stowage Problem, Journal of Heuristics 8, pp. 585-599.
Fan, L., Low, M., Ying, H., Jing, H., Min, Z., Aye, W. (2010). Stowage Planning of Large
   Containership with tradeoff between Crane Workload Balance and Ship Stability,
   Proceedings of the International MultiConference of Engineers and Computers Scientists III,
   pp. 1-7.
Guan, Y., Yang, K-H., Zhou, Z. (2013). The Crane Scheduling: models and solution
   approaches”, Annals of Operations Research 203, p. 119-139.


[PAGINA 12]
Homayouni, S., Tang, S., Ismail, N., and Ariffin, M. (2011). Using simulated annealing
   algorithm for optimization of quay cranes and automated guided vehicles scheduling,
   International Journal of the Physical Sciences 6(27), pp. 6286-6294.
Imai, A., Sasaki, K., Nishimura, E., Papadimitriou, S. (2006) Multi-objetive simultaneous
   stowage and loading planning for a container ship with container rehandle in yard stacks,
   European Journal of Operational Research 171, pp. 373-389.
Javanshir, H., Ganji, S. (2010) Yard crane scheduling in port container terminals using genetic
   algorithm, J. Ind. Eng. Int. 6 (11), pp. 39-50.
Lee, D., Wang, D., Miao, L. (2008). Quay crane scheduling with non-interference constraints in
   port container terminals, Transportation Research E 44, pp. 124–135.
Legato, P., Mazza, R., Trunfio, R. (2008). Simulation-Based Optimization for the Quay Crane
   Scheduling Problem, WSC '08 Proceedings of the 40th Conference on Winter Simulation, pp.
   2717-2725.
Mak, K., Sun, D. (2009). Scheduling Yard Cranes in a Container Terminal Using a New Genetic
   Approach, Engineering Letters 17(4), pp.274-280.
Steenken, D., Voss, S., Stahlbock, R. (2004). Container terminal operation and operations
   research - a classiﬁcation and literature review, OR Spectrum 26 (1), pp. 3–49.
Wilson, I.,. Roach, P. (2000). Container stowage planning: a methodology for generating
   computerised solutions, Journal of the Operational Research Society 51, pp. 1248-1255.
