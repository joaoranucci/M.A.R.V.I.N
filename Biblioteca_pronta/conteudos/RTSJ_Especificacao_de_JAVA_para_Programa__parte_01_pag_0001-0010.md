# RTSJ_Especificacao_de_JAVA_para_Programa

Arquivo original: most_similar_papers_to_this_one/RTSJ_Especificacao_de_JAVA_para_Programa.pdf
SHA-256 do original: 7b4bc7b90172368c5dc697d6e355f690ea7356211e54466c3dac97a823ce0904

Texto extraido para consulta. As paginas abaixo usam a ordem do arquivo PDF, incluindo capas.
Parte preparada: 1/1


[PAGINA 1]
                                                                                                                                         1




                     RTSJ - Especificação de JAVA para
                       Programação em Tempo-Real
                                                    Paulo Roberto M. Cunha
                                                   paulo.cunha@tj.pa.gov.br




     Abstract— Este trabalho1 aborda a especificação de               dos Estados Unidos, iniciando em junho de 1998 e cul-
JAVA para programação em Tempo-Real(RTSJ), que tem                    minando em novembro de 20012 com a publicação da es-
sido um processo realizado pela comunidade Java, patroci-             pecificação de Java para Tempo Real – Real Time Spe-
nado pela empresa Sun Microsystems. Nele são sumariza-                cification for Java (RTSJ). A Sun não vai produzir uma
dos aspectos ligados à modificações na especificação da lin-
                                                                      implementação da especificação – esta tarefa ficou a cabo
guagem (necessárias para atender os requisitos de progra-
mação para sistemas em Tempo-Real e distribuídos). Neste              da empresa americana TimeSys (www.timesys.com).
trabalho são apresentadas ainda a definição de termos li-
gados a sistemas de Tempo-Real, as motivações que impul-                  Um mérito especial desse grupo foi ter definido, de
sionaram a escolha da linguagem, e o estado atual de sua              forma clara e precisa, um vocabulário para Tempo-Real,
disponibilidade comercial.                                            com conceitos antes usados pela comunidade de usuários
                                                                      e vendedores (practitioners) de forma contraditória, e as
                                                                      vezes até errônea.

                       I. I NTRODUÇÃO
                                                                           II. D IFICULDADES NO D ESENVOLVIMENTO PARA
                                                                                           T EMPO -R EAL

U     MA questão natural que surge espontaneamente
      com o título deste trabalho é perguntar-se por que
usar Java para aplicações de Tempo-Real.
                                                                 Portabilidade: Desenvolvedores de sistemas em-
                                                             barcados (embedded) de tempo-real freqüentemente
                                                             encontram-se tendo de lidar com um certo número de mi-
     A plataforma Java tem valor potencial significativo croprocessadores diferentes. É comum encontrar-se mis-
no espaço de aplicações de Tempo–Real, tanto como uma turas de hosts dotados de Motorola 68000, PowerPC, e
linguagem de programação produtiva, quanto como uma Intel 960 em um único laboratório de desenvolvimento.
plataforma portátil de aplicações dentro da miríade de Mesmo dentro de uma família de processadores, a geração
processadores e sistemas operacionais de Tempo–Real. A de código tem de ser direcionada para hosts específicos
perspectiva de reaproveitamento de projetos e de perícia objetivando alcançar altas performances (ex: O PowerPC
de profissionais sob diversas plataformas de processado- 604 necessita de código diferente do que o PowerPC 601).
res e sistemas operacionais na arena de desenvolvimento Isso é importante na área de produtos eletrônicos onde
para tempo-real é bastante bem vinda, seja devido a difi- tanto hardware quanto software mudam durante o ciclo
culdade de se treinar novos profissionais, seja pelos custos de vida da família dos produtos. A manutenção das fer-
de adaptar um sistema já existente para uma nova plata- ramentas apropriadas para trans-desenvolvimento (cross-
forma.                                                       development) para todos esses diferentes hosts é que se
                                                             pode chamar de um “ pesadelo administrativo.” Garan-
     Reconhecendo isso, o grupo de peritos em Tempo– tir que todas as combinações componentes de hardware e
Real para Java (Real-Time for Java Expert Group - RT- software trabalhem corretamente no sentido de tempo-real
JEG) organizou uma série de workshops, sob o patrocí- é um desafio bastante difícil. O processo de desenvolvi-
nio do Instituto Nacional de Padrões e Tecnologia (NIST) mento seria muito mais fácil se os programadores pudes-
                                                             sem escrever seus códigos em uma linguagem que fosse
  ½
    Trabalho apresentado na disciplina Programação de Objetos Dis-
                                                                       ¾
tribuídos no Curso de Mestrado em Engenharia Elétrica (Computação         O RTSJ teve a distinção de ser a primeira Java Specification Re-
Aplicada) ministrada pelo Prof. Dr. Rodrigo Quites, na Universidade   quest (JSR 1), embora não tenha sido a primeira requisição a ter sido
Federal do Pará (UFPa), Jan.,2003.                                    feita.


[PAGINA 2]
                                                                                                                     2


portátil entre todas essas arquiteturas, mantendo uma ver-    ¯ Java empresta das linguagens C e C++ a sintaxe fa-
são única de seus sistemas.                                     miliar. Tal como C++, Java é orientada para objetos,
                                                                embora seja mais simples que C++ por decisão inten-
     Adaptabilidade Dinâmica:          Outra dificuldade        cional de seus projetistas em descartar características
freqüente na manutenção de sistemas em tempo-real em-           que, segundo [9], estavam presentes primeiramente
barcados é que os refinamentos de software incrementais         para dar suporte à retrocompatibilidade com código
tem de ser instalados sem que o sistema seja desligado          legado. Um benefício adicional da sua simplicidade
para uma reinicialização completa. Isso inclui aplicações       é o tamanho pequeno do seu sistema de tempo-de-
que tem de prover serviços ininterruptos para sua comu-         execução. Existem relatos da Sun alegando que o
nidade de usuários (ex.: controle de tráfego aéreo, cen-        interpretador básico tem cerca de 40 Kbytes, e a bi-
trais comutadoras de telefonia, e reconhecimento militar),      blioteca básica e o suporte à thread somam aproxi-
e aplicações para as quais o custo de desligamento (down-       madamente 175 Kbytes [11].
time) são proibitivos (ex.: controle de reatores nucleares,   ¯ O ciclo de desenvolvimento tende a ser mais rápido
e sistemas de automação de manufatura).                         devido ao fato de Java suportar implementações in-
     Tolerância à Falhas: Na presença de falhas no nó           terpretadas e compiladas através do método just-in-
ou na rede, freqüentemente torna-se necessário redistri-        time. Durante o desenvolvimento e prototipação rá-
buir informações e carga de trabalho. Seria bastante de-        pida os desenvolvedores podem economizar tempo
sejável poder dispor de um ambiente de execução no qual         usando o interpretador.
                                                              ¯ Os softwares aplicativos são mais portáteis porque o
fosse permitido, de forma transparente (ou o mais sim-
ples possível), realizar essa transferência, mesmo consi-       ambiente Java especifica cuidadosamente uma repre-
derando que os outros nós podem conter arquiteturas e           sentação intermediária baseada em byte-code inde-
sistemas operacionais heterogêneos, tornando-os capazes         pendente de máquina a qual pode ser transferida en-
de executar quaisquer das tarefas que precisem ser execu-       tre nós heterogêneos de rede e interpretada ou compi-
tadas.                                                          lada sob demanda para código-nativo pelo ambiente
                                                                local de tempo-de-execução Java.
                                                              ¯ Os softwares aplicativos são mais robustos devido ao
                  III. P OR QUE JAVA ?                          fato de o ambiente de tempo-de-execução prover ge-
                                                                rência de memória (garbage-collection) automática.
     O que poucas pessoas sabem, ou lembram, é que ori-         Embora essa seja uma característica bastante dese-
ginalmente a linguagem Java foi criada como parte de            jável por eliminar a possibilidade de ocorrência de
um projeto de pesquisa para desenvolvimento de software         ponteiros perdidos e vazamento de memória, para
avançado para uma larga variedade de “dispositivos” in-         sistemas em tempo-real essa gerência deve ser re-
terconectados em rede e sistemas “embarcados” (embed-           pensada devido às implicações que ela causa devido
ded systems). O objetivo era desenvolver um ambiente            a sua natureza não determinística no modelo inicial
operacional pequeno, confiável, portátil, distribuído, e de     proposto pela Sun Microsystems.
tempo–real [11], uma resposta aos desafios de desenvolvi-     ¯ Aplicações são adaptáveis à ambientes em mudança
mento de aplicações dentro do contexto de ambientes dis-        já que é possível baixar (download) dinamicamente
tribuídos em redes, e heterogêneos. Dentre os desafios, a       módulos de código a partir de outros nós da rede sem
entrega segura de aplicações que consumissem o mínimo           necessidade de reiniciar o sistema.
de recursos, fossem capazes de rodar em qualquer plata-       ¯ A segurança é imposta por proteções embutidas no
forma de harware e software, e pudessem ser estendidas          ambiente contra vírus e outras tentativas indevidas de
dinamicamente eram as de maior relevância [11].                 interferência. Essa proteção é implementada através
                                                                de simples “provadores de teoremas” que analisam
     O projeto de pesquisa inicialmente escolheu usar C++
                                                                módulos de byte-code baixados através da rede antes
para o desenvolvimento.Subseqüentemente os desenvol-
                                                                de tentar executá-los.
vedores encontraram tantas dificuldades com C++ até o
ponto de decidirem que seria melhor projetar um ambi-
                                                          Resumindo, o Grupo de Requerimentos considerou as
ente de linguagem totalmente novo. Passando por alguns
                                                          pontuações abaixo como sendo uma base para os reque-
percalços iniciais, Java surge a partir dessa decisão.
                                                          rimentos e motivações para uso de Java pela comunidade
     Java oferece um certo número de melhoras em rela- de Tempo–Real [4]:
ção ao desenvolvimento de software em linguagens popu-
lares como C e C++ [9]:                                      ¯ O alto nível de abstração presente em Java conduz


[PAGINA 3]
                                                                                                                   3


    a uma melhora na produtividade dos programadores pela criação da especificação de Java para Programação
    (embora reconheça que o compromisso (trade–off) em Tempo-Real:
    comprometa a eficiência de tempo de execução (run-
    time efficiency).                                     ¯ Advanced Logic Corp.
  ¯ Java é relativamente mais fácil de ser dominada do    ¯ Bay Networks / Bay Architecture Lab
    que C++.                                              ¯ Hewlett-Packard Company
  ¯ Java é relativamente segura, mantendo componentes     ¯ Honeywell Inc.
                                           3
    de software (incluindo a própria JVM ) protegidos     ¯ IBM Corp.
    entre si.                                             ¯ Lexmark International, Inc.
  ¯ Java suporta o carregamento dinâmico de novas clas-   ¯ Microsoft
    ses.                                                  ¯ The Mitre Corporation
  ¯ Java é altamente dinâmica, oferecendo suporte à cri-  ¯ Mitsubishi Electric Corporation
    ação de objetos e dethreads em tempo de execução.     ¯ Motorola, Inc.
  ¯ Java foi projetada para dar suporte à integração de   ¯ Nokia Research
    componentes e reutilização.                           ¯ Nortel
  ¯ As tecnologias ligadas à Java foram desenvolvidas     ¯ QNX Software Systems, Ltd.
    com considerações criteriosas, utilizando conceitos e ¯ Rockwell Collins
    técnicas que foram escrutinizadas pela comunidade.    ¯ Siemens AG, A&D
  ¯ A linguagem de programação Java e a plataforma        ¯ Sony
    Java dão suporte à portabilidade de aplicações.       ¯ SRI International
  ¯ As tecnologias ligadas à Java dão suporte a criação   ¯ Sun Microsystems, Inc.
    de aplicações distribuídas.                           ¯ The MITRE Corporation
  ¯ Java oferece uma semântica de execução bem-           ¯ The Open Group
    definida.                                             ¯ Xerox Corporation


                                                           Muito embora isso não seja um fator decisivo no sucesso
                                                           ou fracasso de uma tecnologia (e sim as forças de mer-
            IV. O G RUPO DE R EQUISITOS
                                                           cado) mas o aval de grandes empresas em uma especifica-
                                                           ção empresta um pouco de suas reputações a ela.
     O Instituto Nacional de Padrões e Tecnologia (NIST)
dos Estados Unidos patrocinou o Grupo de Requisitos
para Extensões de Tempo-Real para Plataforma Java. O         V. P RINCÍPIOS NORTEADORES DO T RABALHO DO
Grupo de Requisitos (Requirements Group) incluiu repre-                             RTJEG
sentantes das companhias e organizações cuja capacidade
técnica abrangem a indústria da computação e a academia         Os princípios norteadores são declarações de alto ní-
[4].                                                       vel que delimitam o escopo do trabalho do RTJEG e intro-
                                                           duzem requisitos de compatibilidade para A Especificação
     O objetivo do grupo foi desenvolver requisitos inter-
                                                           de Tempo-Real para Java.
disciplinares para funcionalidades voltadas para Tempo-
Real necessárias para uso em aplicações escritas na lin-        Aplicabilidade a um Ambiente Java em Particu-
guagem de programação Java e sendo executadas em vá- lar: O RTSJ não deverá incluir especificações que restrin-
rias plataformas diferentes.                               jam seu uso a ambientes Java específicos, tais como uma
                                                           versão particular do Java Development Kit (JDK), o Em-
                                                           bedded Java Application Environment, ou o Java 2 Micro
A. Empresas Participantes da Especificação                 Edition .

      Um indicador do grau de importância de uma dada         Retrocompatibilidade: O RTSJ não deverá impedir
tecnologia é o número de empresas (especialmente gran- que programas Java já existentes, escritos de forma apro-
des empresas) interessadas nela. Cada uma das empre- priada e sem a característica de Tempo-Real, sejam exe-
sas listadas abaixo participou diretamente, através de um cutados em implementações do RTSJ.
ou mais representantes, do grupo de trabalho responsável
                                                              Write Once, Run Anyware: O RTSJ deve reco-
  ¿
    Java Virtual Machine                                  nhecer a importância do paradigma “Write Once, Run


[PAGINA 4]
                                                                                                                    4


Anywhere” – (WORA) (escreva uma vez, execute em qual-       ser entregues dentro de um intervalo de tempo bem defi-
quer lugar), mas também deverá reconhecer a dificuldade     nido. Um resultado entregue fora desse tempo (tarde de-
de se alcançar WORA para programas de tempo-real, e         mais) é tão ruim quanto, ou até mesmo pior do que, um
não tentar aumentar ou manter portabilidade binária às      resultado que não é entregue. Os aspectos de temporali-
custas de presibilidade.                                    dade de aplicações para Tempo-Real fazem com que estes
                                                            sistemas sejam notoriamente complexos.
     Práticas Atuais versus Características Avançadas:
O RTSJ deve considerar as práticas correntes usadas em          Os termos chave de computação de Tempo-Real, tais
sistemas de tempo-real, assim como permitir futuras im-    como   real–time, hard real–time, soft real–time, determi-
plementações para inclusão de características avançadas. nismo, e predisível são freqüentemente usados na comuni-
                                                           dade de Tempo–Real de forma mal definida, indefinida ou
     Execução Predizível: O RTSJ referenciará a capa- contraditória. Nessa comunidade não existe um consenso
cidade de execução predizível como sua primeira priori- quanto ao significado de “hard” real-time (embora as pes-
dade em todos os compromissos (tradeoffs); Isto poderá soas pareçam acreditar que sabem o significado quando
acontecer, algumas vezes, às custas de medidas típicas de vêem), e “soft real–time” normalmente tido como sendo
performance computacional de propósito geral.              do tipo “o que será, será” (um conceito que normalmente
                                                           se aplica à sistemas que não sejam de tempo–real).
     Nenhuma Extensão Sintática: Objetivando facilitar
o trabalho dos desenvolvedores de ferramentas, e assim
aumentar as chances de se ter implementações dentro de          VII. RTSJ E AS Á REAS A MPLIADAS DE JAVA
prazos razoáveis, o RTSJ não introduzirá novas palavras
reservadas (keywords) ou fará outras extensões sintáticas
                                                                A especificação final, fruto dos encontros do grupo de
na linguagem Java.
                                                           trabalho de paritos (RTJEG), resultou no que ficou conhe-
                                                           cido como Real-Time Specification for Java (RTSJ) [3], e
     Permitir Variação nas Decisões de Implementa-
                                                           nela são feitas algumas ampliações na definição original
ção: O RTJEG reconhece que as implementações do
                                                           da linguagem Java, as quais são descritas abaixo:
RTSJ podem variar em um número de decisões de imple-
mentação, tais como o uso de algoritmos eficientes ou não,
compromissos entre eficiência de tempo ou de espaço, in-
clusão de algoritmos de escalonamento não requisitados A. Escalonamento de Thread e Despacho:
na implementação mínima, e variação no comprimento do
caminho para o código para execução de byte-codes. O            Projeto: Em face da significante diversidade de mo-
RTSJ não deve obrigar algoritmos ou constantes de tempo delos de escalonamento e despacho, e do reconhecimento
específicas para tal, mas requerer que a semântica da im- de que cada modelo tem ampla aplicabilidade na diversa
plementação seja atingida. O RTSJ oferece aos implemen- indústria de sistemas de tempo-real, ficou definido que
tadores a flexibilidade de criar implementações adequadas deveria haver um mecanismo interno de escalonamento,
para atender os requisitos de seus clientes.               mas não seria especificada previamente a natureza de to-
                                                           dos (ou mesmo de alguns) possíveis mecanismos de esca-
                                                           lonamento. A especificação foi construída permitindo às
                                                           implementações proverem algoritmos de escalonamento
            VI. C ONCEITOS DE T EMPO -R EAL
                                                           não antecipados. As implementações devem permitir a
                                                           designação através de programa de parâmetros apropri-
     Software para aplicações de Tempo-Real reage a es- ados para o mecanismo de escalonamento subjacente, as-
tímulos de seu ambiente. O estado da aplicação é deter- sim bem como prover quaisquer métodos necessários para
minado pelo ambiente, enquanto que o estado do ambi- a criação, gerenciamento, admissão, e término de threads
ente, a sua vez, é determinado pelo estado da aplicação. Java. Bastante flexibilidade foi deixada no arcabouço de
A aplicação de controle de processo freqüentemente inte- escalonamento de thread objetivando permitir que futu-
rage fortemente com algum processo físico (processo este ras versões da especificação pudessem ser construídas a
sob controle).                                             partir desta versão e permitir o carregamento dinâmico de
                                                           módulos de políticas de escalonamento. Um escalonador
     Os resultados de uma aplicação para Tempo-Real não base é requerido em todas as implementações, e este deve
somente tem de ser funcionalmente corretos, eles têm de ser familiar aos programadores de tempo-real. Ele será


[PAGINA 5]
                                                                                                                      5


baseado em prioridades, preemptivo, e deve ter no mínimo usada (tal como atraso médio) e pode aceitar vários valo-
28 prioridades únicas.                                   res para a métrica em uso.

     Especificação: Uma das preocupações de programa-             Muitos sistemas usam prioridade de thread em uma
ção para tempo-real é a garantia da execução em tempo,       tentativa de determinar uma escala. Prioridade tipica-
ou previsível, de seqüências de instruções de máquina.       mente é um número inteiro associado com a thread. Es-
Vários esquemas de escalonamento nomeiam diferente-          ses inteiros informam ao sistema a ordem na qual as thre-
mente essas seqüências de instruções. Nomes comumente        ads devem ser executadas. A generalização do conceito
usados incluem threads, tarefas, módulos, e blocos. O        de prioridade é a elegibilidade de execução. Usa-se o
RTSJ introduz o conceito de objeto escalonável. Qual-        termo despachar dispatching para referir-se à porção do
quer instância de qualquer classe que implemente a inter-    sistema que seleciona a thread com a mais alta elegibi-
face Schedulable é um objeto escalonável e seu escalo-       lidade de execução do conjunto de threads que estejam
namento e despacho serão gerenciados pela instância de       prontas para serem executadas. Na prática corrente de sis-
Scheduler da qual ele tenha uma referência. O RTSJ re-       temas de tempo-real, a atribuição de prioridades está tipi-
quer três classes que são objetos escalonáveis:              camente sob controle do programador em oposto ao con-
                                                             trole do sistema. No RTSJ cabe ao programador também
  ¯ RealtimeThread,                                          a atribuição de prioridades.
  ¯ NoHeapRealtimeThread,
                                                                  O RTSJ requer um número de classes com nomes no
  ¯ AsyncEventHandler.
                                                             formato <string>Parameters (tais como Scheduling-
                                                             Parameters). Uma instância de uma dessas classes de
Por execução temporalmente adequada de thread
                                                             parâmetros contém uma característica de demanda por re-
subentende-se que o programador pode determinar por
                                                             curso em particular para ser usada por um ou mais ob-
análise do programa, teste do programa em uma imple-
                                                             jetos escalonáveis. Por exemplo, a subclasse PriorityPa-
mentação particular, ou ambos, se threads particulares
                                                             rameters contém a métrica de elegibilidade de execução
sempre completarão sua execução antes de alguma res-
                                                             do escalonador básico, ou seja, prioridade. Em algumas
trição temporal. Essa é a essência da programação para
                                                             momentos (tempo de criação ou configuração (ou recon-
tempo-real:
                                                             figuração) de thread), outras instâncias de classes de pa-
                                                             râmetros são ligadas à um objeto escalonável. O objeto
      A adição de restrições temporais às condições          escalonável então assume as características dos valores
      de corretude para a computação.                        presentes no objeto parâmetro. Por exemplo, se uma ins-
                                                             tância de PriorityParameter que tinha em seu campo de
     Por exemplo, para que um programa compute a soma        prioridade o valor representante da mais alta prioridade
de dois números, não poderá mais ser aceitável compu-        disponível for ligada a um objeto escalonável, então esse
tar apenas a resposta aritmeticamente correta, mas a res-    objeto assumirá a característica de que ele executará sem-
posta deverá ser computada antes de um tempo particular.     pre que estiver pronto preferencialmente à todos os outros
Tipicamente, restrições temporais são prazos (deadlines)     objetos escalonáveis ( exceto, é claro, àqueles que tam-
expressos em tempo relativo ou absoluto.                     bém possuirem a mais alta prioridade).

     Usa-se o termo escalonamento (scheduling) ou algo-           O RTSJ especifica ao menos um algoritmo de escalo-
ritmo de escalonamento para referir-se à produção de uma     namento e mudança semântica na JVM que suporta exe-
seqüência, ou ordenação, para a execução de uma con-         cução previsível, e este deve estar disponível em todas as
junto de threads, uma escala (schedule). Essa escala tenta   implementações de RTSJ. O algoritmo de escalonamento
otimizar uma métrica particular ( uma métrica que possa      inicial e default é prioridade-fixa preemptiva com pelo
medir quão bem o sistema está atingindo as restrições        menos 28 níveis únicos, e será representado em todas as
temporais). Uma análise de realização (feasibility analy-    implementações pela classe PriorityScheduler subclasse
sis) determina se uma escala tem um valor aceitável para     de Scheduler.
a métrica.

     Por exemplo, em sistemas de tempo-real crítico (hard B. Gerenciamento de Memória:
real-time) a métrica é “número de prazos perdidos”, e o
único valor aceitável para essa métrica é zero. Em siste-     Projeto: É reconhecido que o gerenciamento auto-
mas de tempo-real leves (soft real-time) outra métrica é mático de memória é uma característica particularmente


[PAGINA 6]
                                                                                                                      6


importante do ambiente de programação Java, e foi bus-            definido pelo escopo sintático (o tempo de vida dos
cada uma direção que permitisse, tanto quanto possível,           objetos no heap).
que o serviço de gerencia automática de memória pudesse        2) Physical Memory: permite que objetos sejam cri-
ser implementado automaticamente pelo sistema subja-              ados em regiões de específicas de memória física
cente e não se intrometesse na tarefa de programação.             que tenham características particulares importantes,
                                                                  tais como memória que tenha velocidade de acesso
     Existem diversos algoritmos de gerenciamento auto-           substancialmente mais rápida, ou áreas de memória
mático de memória, também conhecidos como garbage                 destinadas a mapeamento de dispositivos.
collection (GC), e muitos deles acomodam-se a certas           3) Immortal Memory: representa uma área de me-
classes de estilos e sistemas de programação para tempo-          mória que contém objetos que, uma vez alocados,
real. Em uma tentativa de acomodar um conjunto diverso            passam a existir durante toda a execução da apli-
de algoritmos de GC foi buscado definir-se uma especifi-          cação, ou seja, os objetos são imortais. Imortal-
cação alocação e retomada de memória que:                         Memory é um recurso de memória compartilhado
                                                                  entre todas as threads em uma aplicação. Obje-
  ¯ fosse independente de qualquer algoritmo de GC em             tos alocados em ImortalMemory só são liberados
    particular,                                                   quando o ambiente de execução Java (Java run-time
  ¯ permitisse o programa caracterizar de forma precisa           environment) termina, e nunca são alvo de garbage-
    o efeito de um algoritmo implementado de GC no                collecting ou de movimentação.
    tempo de execução, preempção, e despacho de thre-          4) Heap Memory: representa uma área de memória
    ads Java de tempo- real, e                                    que é o heap. O RTSJ não muda o determinante
  ¯ permitisse a alocação e retomada de objetos fora de           do tempo de vida dos objetos presentes no heap.
    qualquer interferência de qualquer algoritmo de GC.           O tempo de vida ainda é determinado pela visibi-
                                                                  lidade.
     Especificação: Garbage-collected memory heaps
sempre foram considerados um obstáculo para programa-
ção para tempo-real devido às latências imprevisíveis in-    C. Sincronização e Compartilhamento de Recursos:
troduzidas pelo garbage-collector. O RTSJ responde essa
questão provendo várias extensões ao modelo de memó-              Projeto: A lógica de programação freqüentemente
ria as quais dêem suporte ao gerenciamento de memória        necessita compartilhar recursos serializáveis. Sistemas
de uma forma que não interfira com a habilidade do có-       para tempo-real introduzem uma complexidade adicio-
digo de tempo-real prover comportamento determinístico.      nal: inversão de prioridade. Foi decidido que a especi-
Este objetivo é alcançado através da permissão da aloca-     ficação menos intrusiva para permitir sincronização se-
ção de objetos fora do heap do garbage-collector tanto       gura em tempo-real é requerer qua as implementações de
para objetos de curto quanto de longo tempo de vida:         synchronized (palavra reservada da linguagem Java)
                                                             inclua um ou mais algoritmos que previnam inversão de
     Memory Areas: O RTSJ introduz o conceito de área        prioridade entre threads Java de tempo-real que compar-
de memória. Uma área de memória representa uma área          tilhem o recurso serializado. Foi notado também que em
da memória que pode ser usada para alocação de obje-         alguns casos o uso da palavra reservada synchronized
tos. Algumas áreas de memória existem fora do heap e         implementando o algoritmo requerido de inversão de pri-
impõem restrições sobre o que o sistema e o garbage-         oridade não é suficiente nem para prevenir inversão de pri-
collector podem com os objetos alocados nestas áreas.        oridade nem permitir uma thread ter uma elegibilidade de
Objetos em algumas áreas de memória nunca são co-            execução logicamente mais alta que o carbage collector.
letados pelo garbage-collector, entretanto, o garbage-       É provido um conjunto de classes de filas livres de espera
collector tem de ser capaz de vasculhar essas áreas de me-   (wait-free queue classes) a serem usadas em tais situações.
mória em busca de referências a quaisquer objetos dentro
do heap para preservar a integridade do heap.              Especificação: Em particular o termo highest
                                                      priority thread indica meramente a thread mais elegível,
     Existem quatro tipos básicos de áreas de memó- ou seja, a thread a qual o despachante (ıdispatcher)
ria:                                                  escolheria entre todas as threads que estão prontas
                                                      para serem executadas, e não presume necessariamente
   1) Scoped Memory: provê mecanismos para tratar um mecanismo de despacho baseado estritamente em
      com classes de objetos que tem um tempo de vida prioridade.


[PAGINA 7]
                                                                                                                           7


                                                                     tida por uma thread com prioridade ainda mais
Wait Queues: Threads esperando para adquirir con-                    baixa ).
trole sobre um recurso devem ser liberadas em ordem                       Questões associadas à sincronização entre
de elegibilidade de execução. Isso tanto se aplica ao                thread de tempo-real e threads regulares de
processador quanto a blocos sinconizados. Caso threads               Java podem surgir nesse contexto. O RTSJ
com a mesma elegibilidade de execução sejam possíveis                provê três filas do tipo livre-de-espera (wait-free
dentro da política de escalonamento ativa, tais threads são          queue) para prover acesso compartilhado a ob-
acordadas em ordem FIFO. Por exemplo:                                jetos acessados tanto por threads Java regulares
                                                                     quanto por NoHeapRealtimeThreads. Essas
  ¯ Threads esperando para entrar em blocos synchroni-               classes são providas explicitamente para permi-
    zed tem acesso garantido ao bloco sincronizado em                tir comunicação entre a execução de tempo-real
    ordem de elegibilidade de execução.                              de NoHeapRealtimeThreads e threads Java
  ¯ Uma thread bloqueada que se torna pronta para exe-               regulares.
    cutar recebe acesso ao processador em ordem de ele-
    gibilidade de execução.
  ¯ Uma thread cuja elegibilidade de execução é expli-        D. Gerenciamento de Eventos Assíncronos
    citamente configurada (set) por si mesma ou por ou-
    tra thread recebe acesso ao processador em ordem de            Projeto: Sistemas de tempo-real tipicamente intera-
    elegibilidade de execução.                                gem de perto com o mundo real. A respeito da execução
  ¯ Uma thread que executa o comando yeld( ) abrindo
                                                              da lógica, o mundo real é assíncrono. Isso compeliu o
    mão de seu uso do processador receberá novamente          RTJEG a incluir mecanismos eficientes para disciplinas
    acesso ao processador após esperar por threads de         de programação que pudessem acomodar essa assincronia
    mesma elegibilidade de execução.                          inerente. O RTSJ generaliza o mecanismo da linguagem
  ¯ Threads que sejam relocadas (preempted) em favor
                                                              Java de gerencia de eventos assíncronos. Classes reque-
    de uma thread com maior elegibilidade de execução         ridas representam coisas que possam acontecer e a lógica
    podem receber acesso ao processador em qualquer           que é executada quando essas coisas acontecem. Uma ca-
    momento assim determinado por uma implementa-             racterística notável é que a execução da lógica é escalo-
    ção particular. A implementação é requisitada em          nada e despachada por uma escalonador implementado.
    prover documentação declarando exatamente o algo-
    ritmo usado para garantir tal acesso.                        Espeficifcação: A estrutura de eventos assíncronos é
                                                              composta de duas classes:
essa é a lógica a ser seguida.
                                                                ¯    AsyncEvent
Evitando Inversão de Prioridade: Todas as imple-                ¯    AsyncEventHandler
mentações de RTSJ devem prover uma implementação
da primitiva synchronized com um comportamento                Um objeto AsyncEvent representa algo que possa acon-
padrão que garanta que não ocorra inversão de prioridade      tecer, como um signal POSIX, uma interrupção de hard-
descontrolada. Além disso, essa regra deve aplicar-se à       ware, ou um evento computado tal como um avião en-
código se for executado com a implementação assim bem         trando em uma região específica. Quando um desses even-
como com threads de tempo-real. O protocolo de herança        tos ocorre, que é indicado pela execução do método fire( ),
de prioridade tem de ser implementado por default. O          os métodos associados handleAsyncEvent( ) de instân-
protocolo de herança de prioridade é um algoritmo bem         cias de AsyncEventHandler são escalonados e dessa
conhecido dentro da literatura de escalonamento de            forma realizam a lógica requerida.
tempo-real e tem o seguinte efeito:
                                                                     Uma instância de AsyncEvent gerencia duas coi-
          Caso a thread ½ tente ganhar controle so-          sas:
      bre um lock que está sendo mantido por uma
      thread ¾ de prioridade mais baixa, então a pri-          1) o desbloqueio de handlers quando o evento é dispa-
      oridade de ¾ é elevada ao nível da de ½ en-                rado,
      quanto ¾ mantenha controle sobre o lock ( e              2) o conjunto de handlers assossiados ao evento. Este
      recursivamente caso a própria ¾ esteja espe-                conjunto pode ser questionado, ter handlers adicio-
      rando para ganhar controle sobre uma lock man-               nados ou removidos.


[PAGINA 8]
                                                                                                                            8


Uma instância de AsyncEventHandler pode ser pensada             do mecanismo tradicional, inseguro, e obsoleto da lingua-
como bastante similar a uma thread. Quando um evento é          gem Java de parar threads, o mecanismo do RTSJ para
disparado, os handlers são executados assincronamente,          tratamento de eventos assíncronos e transferência de con-
escalonados de acordo com os ReleaseParameters e                trole é seguro.
SchedulingParameters de uma forma que parece como
se o handler tenha assumido a sua própria thread.
                                                                G. Acesso à Memória Física:
     Pretende-se que o sistema possa lidar bem com si-
tuações onde haja um grande número de instâncias de                  Embora não seja diretamente uma questão de tempo-
AsyncEvent e AsyncEventHandler (dezenas de milha-               real, acesso à memória física é algo desejável para mui-
res). O número de handlers disparados (em processo) deve        tas das aplicações que pudessem produtivamente fazer uso
ser menor. Uma forma especializada de AsyncEvent é a            de uma implementação do RTSJ. Foi definida então uma
classe Timer a qual representa um evento cuja ocorrên-          classe que permite aos programadores acesso à memória
cia é dirigida pelo tempo. Existem dois tipos de Timers:        física ao nível dos bytes, assim bem como uma classe que
O tipo OneShotTimer e o PeriodicTimer. Instancias de            permite a construção de objetos na memória física.
OneShotTimer disparam uma vez, em um momento es-
pecífico. Timers periódicos disparam em momentos espe-
cíficos e então periodicamente de acordo com um inter-                     VIII. R EAL -T IME JAVA EM AÇÃO
valo especificado.
                                                                     Recentemente (26 de março de 2002) a revista Ja-
    Os Timers são dirigidos por objetos do                      vaWorld realizou uma reportagem sobre o uso de Java para
tipo Clock.       Existe um objeto Clock especial,              programação para tempo-real. No artigo Tim Rohaly [10]
Clock.getRealtimeClock( ) que representa o reló-                faz referência a uma apresentação feita durante a SunOne4
gio de tempo-real. A classe Clock pode ser extendida            de uma aplicação projetada para “capturar a imaginação”
para representar outros clocks que o sistema possa              do público e enfatizar a integração de várias tecnologias
tornar disponíveis (tais como um soft clock com alguma          chave da Sun (Web Services, Java para Tempo-Real, e
granularidade).                                                 aplicações Wireless).

                                                                     A aplicação é composta de uma “luta” ente robôs que
E. Transferência Assíncrona de Controle:                        foi chamada de “sumo de Robôs” (Fig.1). O sumo de
                                                                robôs segue regras semelhantes as da luta de sumo real.
     As vezes o mundo real muda tão drasticamente (e as-        Dois robôs se enfrentam em uma arena circular, cada qual
sincronamente) que o ponto atual da execução da lógica          tentando forçar o outro para fora do ringue. Diferente-
deve ser imediatamente e eficientemente transferido para        mente de Battlebots e outros shows de televisão populares
                                                                nos Estados Unidos, os competidores do sumo de robôs
outra localização. O RTSJ inclui um mecanismo o qual
                                                                não são violentos. A tentativa intencional de causar da-
estende o mecanismo de tratamento de exceção para per-
                                                                nos ao oponente é expressamente proibida. Da mesma
mitir às aplicações mudar, através de programação, o local
                                                                forma, os robôs não são controlados por seres humanos.
(locus) de controle de outra thread Java. É importante no-
                                                                Ao invés disso eles se baseiam em comportamentos pre-
tar que o RTSJ restringe essa transferência assíncrona de
                                                                programados (comportamento autônomo) – software é tão
controle à lógica especificamente escrita sob a presunção
                                                                importante quanto hardware.
de que o seu local de controle pode mudar assincrona-
mente.                                                          O público presente pôde configurar os robôs atra-
                                                          vés de “Java-powered wireless phones”, utilizando Sun
                                                          ONE (One Network Environment) Web services e wire-
F. Término Assíncrono de Thread:                          less Ethernet. O 1público poderia escolher enfatizar velo-
                                                          cidade sobre agilidade de uma forma familiar aos entusi-
     Novamente, devido às mudanças, as vezes drásticas e astas de jogos do tipo role-playing através da divisão de
assíncronas, ocorridas no mundo real, a lógica da aplica- 100 pontos entre as duas categorias.
ção pode ter necessidade de fazer com que uma thread        
                                                              Festival anual patrocinado pela empresa Sun Microsystems inc. na
Java de tempo-real transfira segura e convenientemente qual são apresentador seminários de pesquisadores proeminentes, ex-
seu controle para seu escopo mais externo e assim ter- postas aplicações e novas tecnologias emergentes dentro do universo
mine de forma normal. Deve-se notar que diferentemente de produtos da empresa, em especial a linguagem Java.


[PAGINA 9]
                                                                                                                                             9


     Os robôs também podiam transmitir vídeo a partir de maduro e portátil de desenvolvimento de aplicações den-
câmeras instaladas sobre si, transmitido através de wire- tro do espaço de aplicação intrinsecamente complexo e
less Ethernet para apresentação ao público. Já que os dispendioso como são as aplicações de tempo-real.
robôs eram autônomos, toda a estratégia e as ações tem
de ser preprogramadas.                                         Este esforço foi bem sucedido em seu intento de criar
                                                          uma especificação (RTJEG), posteriormente uma padro-
                                                          nização (RTSJ), e por último uma implementação para o
                                                          padrão, mas se o RTSJ sobreviverá e onde ele se encai-
                                                          xará dentro das teconologias da Sun ainda é algo a ser
                                                          visto. Experiências passadas nesta área sugerem que a
                                                          Sun MicroSystems tem um bom caminho a trilhar antes
                                                          que as “forças de mercado” em última instância tornem
                                                          RTSJ bem sucedida.



                                                                                                  R EFERENCES

Fig. 1. Corrida de robôs programados com diversas tecnologias Java.     [1] Allen, D., Standards for Real-Time Distributed Object Compu-
                                                                            ting. The Edge. MITRE Corporation, 2000.
                                                                        [2] Bollella, G., Real-Time Java: Status and Architecture.
                      IX. C ONCLUSÕES                                       (www.rtj.org/rtas99/rtas.htm), 1999.
                                                                        [3] Bollella, G., et. al., The Real-Time Specification for Java - The
                                                                            Real-Time for Java Expert Group. Addison-Wesley,Upper Sad-
     Aplicações como as do robô lutador de sumo citadas                     dle River, NJ, 2000.
anteriormente deixam claro que a linguagem Java pode                    [4] Carnahan,        L.,Ruark,       M.     (eds.),     Requirements
ser aplicada fim-a-fim, do banco de dados, através do ser-                  for Real-Time Extensions for the Java Platform.
                                                                            (www.nist.gov/itl/div897/ctg/real-time/rt-doc/rtj-final-draft.pdf),
vidor de aplicações, web services, conectividade sem fio,                   National Institute of Standards and Technology, 1999.
até o interfaceamento Java com o mundo real através de                  [5] Hilderink, G., Bakkers, A., Broenink, J., A Distributed Real-Time
J2ME/real-time acomodando diversos clientes fim-a-fim.                      Java System Based on CSP. 3rd IEEE International Symposium
                                                                            on Object-Oriented Real-Time Distributed Computing, pp. 400-
     Embora muitas companhias5 ofereçam soluções de                         407, California, 2000.
tempo-real para Java, neste momento apenas uma (aJile                   [6] Interoperable         Objects      for      Distributed       Real
                                                                            Time      Systems.       Embedded      Systems      Programming
Systems6 ) oferece suporte à RTSJ em seus produtos. A                       (www.embedded.com/97/feat9703.htm), 2002.
maioria das empresas que vendem máquinas vituais em-                    [7] Jensen, E., The Distributed Real-Time Specification for Java - A
barcadas (embedded VM) e hardware parecem estar con-                        Proposed Initial Approach.(www.drtsj.org), Real-Time and Per-
centrando seus esforços mais em J2ME7 e não tem planos                      formance Engineering Section The MITRE Corporation,2000.
                                                                        [8] Lamport, L. - LATEX A Document Preparation System – User´s
para embarcarem em Java de Tempo-Real. Uma das ra-
                                                                            Guide & Reference Manual. Addison-Wesley, Reading, Massa-
zões para isso é que todas elas já oferecem alguma capa-                    chusetts, 1986.
cidade de tempo-real, portanto não identificam qualquer                 [9] Nilsen, K., Issues in the Design and Implementation of Real-
razão que as obrigue ou motive para dar suporte imediato                    Time Java.1996.
                                                                       [10] Rohaly, T., Real-Time Java takes the Stage. JavaWorld,
à nova especificação RTSJ. Muitas estão considerando dar
                                                                            march,2002.
suporte ao RTSJ para o futuro (nos próximos 12-18 me-                  [11] Sun Microsystems Inc., The Java Language Environment: A
ses), mas a maioria está esperando para ver a demanda de                    White Paper. Sun Microsystems Inc.:Mountain View, CA, 1995.
mercado antes de se comprometer com esta nova API.

    Concluímos que a RTSJ é o resultado de um esforço
conjunto, criterioso da comunidade de tempo-real (acade-                                           A PPENDIX
mia e empresas) para prover a criação de um ambiente
 
    aJile Systems, Esmertec, NewMonics, Zucotto Wireless, etc. . .                            AGRADECIMENTOS
 
    A empresa aJile Systems (www.ajile.com) participou no Grupo
de Peritos para Especificação de Java para Tempo-Real (RTJEG) e atu-
almente trabalha em uma implementação de RTSJ para seus processa-
                                                                           Este trabalho foi feito usando LATEX. Falar sobre seus
dores Java aJ-80 e aJ-100.                                             méritos quanto à preparação de documentos é chover no
  
    Java 2 Platform, Micro Edition                                     molhado, mas gostaria de deixar registrada aqui minha


[PAGINA 10]
                                                                                                                                   10


profunda admiração pelos autores dos pacotes TEX, Do-
nald E. Knuth e LATEX, Leslie Lamport. Aprender a usá-
los certamente não é uma tarefa trivial, mas certamente o
resultado de longe compensa o trabalho do aprendizado.
Espero que as gerações futuras saibam reconhecer o valor
dessas ferramentas, tão profundamete associadas aos ide-
ais mais nobres que sustentam e promovem o avanço da
ciência da computação.

     Agradecemos também ao Prof. Dr. Rodrigo Qui-
tes, do Curso sobre Programação de Objetos Distribuídos,
pelo seu empenho, paciência, profissionalismo e esforço
em tornar esta disciplina interessante e capaz de contribuir
para a formação dos alunos da nossa turma de Mestrado
em Engenharia Elétrica (Computação Aplicada).                Fig. 2. O livro do grupo que definiu o RTSJ. O seu conteúdo inteiro
                                                                 encontra-se disponível na Internet em formato PDF.


            L IVROS SOBRE R EAL -T IME JAVA

     Em pesquisa recente encontramos os seguintes títulos
realcionados à Programação para Tempo Real e a lingua-
gem Java.

  ¯   Bolela, G., Goslin, J. et. al., "The Real-Time Specifi-
      cation for Java - The Java Series". Addison-Wesley,
      2000. (Fig. 2).

  ¯   Dibble, P., "Real-Time Java Platform Programming".
      Java Series - Prentice-Hall, 2000. (Fig. 3).

  ¯   Burns, A., Welling, A., "Real-Time Systems and
      Programming Languages - Ada95, Real-Time Java              Fig. 3. Outro livro sobre Java para Tempo-Real da série Java patroci-
      and Real-Time POSIX".      Addison-Wesley, ¿             nada pela Sun.
      edition, 2001. (Fig. 4).




                                                                 Fig. 4. Com uma abordagem mais genérica, o livro acima aborda
                                                                 outras linguagens de programação para tempo-real além de Java.
