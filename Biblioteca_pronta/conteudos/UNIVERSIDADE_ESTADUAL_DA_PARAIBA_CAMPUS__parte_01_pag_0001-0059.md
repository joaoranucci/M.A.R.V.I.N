# UNIVERSIDADE_ESTADUAL_DA_PARAIBA_CAMPUS

Arquivo original: most_similar_papers_to_this_one/UNIVERSIDADE_ESTADUAL_DA_PARAIBA_CAMPUS.pdf
SHA-256 do original: 1af654ea667483a061ab37f4d808345f732f353782a2e5b2972e707e7fbdd385

Texto extraido para consulta. As paginas abaixo usam a ordem do arquivo PDF, incluindo capas.
Parte preparada: 1/1


[PAGINA 1]
                                           1




        UNIVERSIDADE ESTADUAL DA PARAÍBA
           CAMPUS I – CAMPINA GRANDE
        CENTRO DE CIÊNCIAS E TECNOLOGIA
      CURSO DE BACHARELADO EM COMPUTAÇÃO




        ADALCINO JUNIOR ARAUJO TAVARES




GUIA PARA DEFINIÇÃO DE UMA ARQUITETURA
      BASEADA EM MICROSSERVIÇOS




                CAMPINA GRANDE
                 AGOSTO DE 2019


[PAGINA 2]
                                                                2
                                          SUMÁRIO

Quando uma Arquitetura Baseada em Microsserviços faz Sentido?    4
   O Domínio do Problema                                        4
   A Estrutura Organizacional                                   5
   Outros Aspectos                                              6
Padrões por Categoria                                            6
   Identificação/Delimitação                                     6
   Armazenamento                                                 8
   Comunicação                                                   9
   Exposição                                                    11
   Descoberta                                                   12
   Monitoramento                                                14
   Tolerância a Falhas                                          16
   Resumo dos Padrões                                           17
Catálogo de Padrões                                             19
   Consistência                                                 19
       SAGA                                                     19
           Choreography-Based                                   19
           Orchestration-Based                                  20
   Comunicação                                                  20
       Messaging                                                20
       Remote Procedure Invocation                              22
       Shared Data Microservice                                 22
   Delimitação/Decomposição                                     23
       Decompose by Business Capability                         23
       Decompose by Subdomian                                   25
   Descoberta                                                   26
       Client-Side Discovery                                    26
       Server-Side Discovery                                    27
       Self-Registration                                        28
       3rd Party Registration                                   29
   Exposição                                                    30
       Aggregator Microservice                                  30
       Backends For Frontends                                   31
       Branch Microservice                                      32
       Chained Microservice                                     33
       API Gateway                                              34
       Proxy Microservice                                       35
   Interesses Transversais                                      36
       Ambassador                                               36


[PAGINA 3]
                                  3
     Externalized Configuration   37
     Microservice Chassis         38
     Sidecar                      39
  Mensagens Transacionais         40
     Polling Publisher            40
     Transactional Outbox         41
     Transaction Log Tailing      42
  Migração                        43
     Anti-Corruption Layer        43
     Strangler                    44
  Monitoramento                   45
     Application Metrics          45
     Audit Logging                46
     Distributed Tracing          48
     Exception Tracking           49
     Health Check API             50
     Log Aggregation              51
  Tolerância a Falhas             53
     Bulkhead                     53
     Circuit Breaker              54
     Tolerant Reader              55
REFERÊNCIAS                       57


[PAGINA 4]
                                                                                                                     4
    1.     Quando uma Arquitetura Baseada em Microsserviços faz Sentido?
       Antes de entramos de fato nos motivos que levam a uma adoção de uma arquitetura baseada
em microsserviços, é preciso ressaltar que os pontos elencados abaixo não são necessariamente
forças isoladas que implicam na utilização da mesma. Ou seja, quanto mais fatores forem
detectados no contexto observado, mais prováveis serão os benefícios ao adotar uma arquitetura de
microsserviços.
       Para esta pesquisa foram identificados alguns aspectos relevantes que impulsionam a adoção
de uma arquitetura baseada em microsserviços. Considerando a literatura sobre o assunto
(FOWLER, 2015; NEWMAN, 2015; CHEN, 2018; RICHARDSON, 2019) é possível deduzir que a
escolha por uma arquitetura baseada em microsserviços deve ser fundamentada com base em três
categoria de aspectos: os relacionados ao domínio do problema; os relacionados à estrutura
organizacional e os aspectos externos.

           1.1.     O Domínio do Problema
        Martin Fowler em uma de suas publicações diz: “[...] nem considere microsserviços, a
menos que você tenha um sistema complexo demais para ser gerenciado como um
monolito.”(FOWLER, 2015, tradução nossa)1. O mesmo autor defende que o ideal a ser feito é
começar com um sistema monolítico e somente após perceber que a arquitetura do sistema está
impossibilitando sua evolução deve-se pensar sobre a decomposição do sistema. Este pensamento é
válido principalmente para projetos em fase inicial que ainda não possuem um grande número de
usuários ou que exploram setores incertos de mercado. Podemos utilizar como exemplo as empresas
do tipo startups que criam produtos de software sem a certeza de que seu produto terá um mercado
efetivo. Portanto investir em uma arquitetura baseada em microsserviços pode não ser a melhor
escolha para esta realidade.
        Em contrapartida, alguns autores, defendem que o ideal é iniciarmos a construção do
sistema já com uma arquitetura distribuída, pois o processo de decomposição nem sempre é
realizado com sucesso, graças ao alto nível de acoplamento introduzido no projeto (TILKOV,
2015). Arquiteturas monolíticas, em geral, estão mais expostas a facilidade de inserção de
acoplamento entre os módulos. E o melhor momento para criarmos serviços autônomos é na fase
inicial dos projetos, pois, o limite físico garante ou pelo menos dificulta o alto acoplamento entre os
serviços.
        Se os dados evidenciam que o sistema terá um alto volume de acesso, alta demanda de
disponibilidade e o investimento inicial em uma arquitetura baseada em microsserviços é viável
para a realidade do projeto, tudo indica que a adoção por uma arquitetura distribuída baseada em
microsserviços beneficiará o desenvolvimento do sistema em questão.
        Um fator presente no domínio do problema que pode refletir a necessidade de uma
arquitetura de microsserviços, além dos pontos discutidos anteriormente, é a existência de muitos
modelos de interação utilizados para tratar a mesma entidade de formas diferente entre os diferentes
módulos da aplicação. Por exemplo, a entidade Cliente possui diferentes representações dentro de
uma aplicação do tipo e-commerce. O módulo de cadastro representa um Cliente como um conjunto



1
    “[...] don't even consider microservices unless you have a system that's too complex to manage as a monolith.”


[PAGINA 5]
                                                                                                                         5
de informações pessoais. Já para o módulo de Newsletter o Cliente é basicamente um endereço de
email, por exemplo.
        Quando trabalhamos com arquiteturas monolíticas todos os módulos compartilham a mesma
representação das entidades envolvidas no domínio do sistema. Já para aplicações baseadas em
Microsserviços, o comum é termos representações próprias para cada microsserviço. Além de
representações próprias, uma arquitetura baseada em Microsserviços permite a adoção de uma
persistência poliglota. A capacidade de armazenar os dados de diferentes formas de acordo com a
necessidade do serviço e utilizando a tecnologia de armazenamento mais adequada é um grande
benefício. Isso não significa que aplicações monolíticas não podem utilizar persistência poliglota,
porém, é mais frequente em aplicações baseada em microsserviços.
        Portanto, a complexidade inserida no projeto por uma arquitetura de microsserviços faz com
que apenas projetos que lidam com domínios complexos e grandes aplicações percebam os reais
benefícios providos pela arquitetura. Quando utilizados de maneira prematura seus benefícios
podem não ser nitidamente identificados acarretando uma sobrecarga operacional não
recompensada.

         1.2.     A Estrutura Organizacional
        A estrutura organizacional ao qual o projeto está inserido possui grande influência em
decisões arquiteturais e deve ser cuidadosamente observada antes de uma definição final sobre a
arquitetura projetada.
        Melvin E. Conway, em sua tese, definiu que “[...] as organizações que projetam sistemas (no
sentido amplo usado aqui) são constrangidas a produzir projetos que são cópias das estruturas de
comunicação dessas organizações.”(CONWAY, 1968, p. 31, tradução nossa). Pesquisas recentes
comprovam a hipótese levantada por Melvin e especificam a forte relação entre a estrutura
organizacional e os produtos produzidos por tais organizações. “Encontramos fortes evidências para
apoiar a hipótese de que a arquitetura de um produto tende a espelhar a estrutura da organização na
qual ela é desenvolvida.”(MACCORMACK; RUSNAK;BALDWIN, 2011, p. 24, tradução nossa)2.
        Podemos considerar que organizações que possuem múltiplas equipes localizadas em
diferentes regiões estão mais aptas a desenvolverem sistemas de software que possuem uma
arquitetura baseada em microsserviços. MacCormack, Rusnak e Baldwin (2011) corroboram a esta
ideia quando afirmam que organizações com equipes fracamente acopladas produzem produtos com
design mais modular comparando com organizações que possuem equipes fortemente acopladas.
        Vale ressaltar que em nenhum momento está sendo defendida a ideia de que apenas
organizações com equipes distribuídas são capazes de desenvolver um produto de software
utilizando uma arquitetura baseada em microsserviços. A preocupação aqui apresentada é a de
expor aspectos pertencente a estrutura organizacional que impulsionam a adoção de uma arquitetura
baseada em microsserviços.




2
 “We find strong evidence to support the hypothesis that a product’s architecture tends to mirror the structure of the
organization in which it is developed.”


[PAGINA 6]
                                                                                                                     6
         1.3.    Outros Aspectos
        O mercado competitivo pode ter uma grande influência sobre a definição da arquitetura de
um software. Esse fenômeno ocorre devido a necessidade de resposta rápida aos clientes e a
capacidade de se adaptar às mudanças de mercado.
        Chen (2018) reforça que essas necessidades têm impulsionado muitas empresas a adotarem
a cultura DevOps, especialmente, no sentido de implementarem entrega contínua aos seus projetos.
Entretanto, a adoção ao movimento DevOps e implementação de técnicas, como a entrega contínua,
pode ser dificultada pela arquitetura do sistema. Algumas características são necessárias à
arquitetura da aplicação para que a implementação de entrega contínua seja possível. Chen (2018),
identificou duas dessas características: implantabilidade e modificabilidade. Segundo o autor a
capacidade de implantação e a modificabilidade tornam-se mais exigentes em projetos que aplicam
o conceito de entrega contínua.
        Além das características, Chen (2018), identificou grandes benefícios, acerca de
implantabilidade e modificabilidade, após adotarem uma arquitetura baseada em microsserviços.
“Depois de movermos nossos aplicativos para uma arquitetura de microsserviços, observamos uma
maior capacidade de implantação, modificabilidade e resiliência à erosão da arquitetura
[...]”(CHEN, 2018,n.p, tradução nossa)3.
        Portanto, conhecer o mercado no qual o software está inserido e identificar a existência dos
impulsos mencionados anteriormente, demonstram ser fatores de grande relevância nas decisões
arquiteturais e muitos autores (FOWLER, 2015; NEWMAN, 2015; CHEN, 2018; RICHARDSON,
2019) acreditam que microsserviços são uma ótima escolha.

    2.   Padrões por Categoria
        Definir a arquitetura de um sistema é uma tarefa muito desafiadora, pois, exige a
compreensão completa sobre o contexto em que o software será inserido. Além de experiência, o
arquiteto deve possuir a sensibilidade para, dentre as diversas restrições que o projeto possui,
identificar quais têm maior relevância sobre as decisões arquiteturais.
        A construção deste guia foi motivada pela vontade de compartilhar o conhecimento
adquirido durante o período de pesquisa e tem como objetivo auxiliar a compreensão dos princípios
por trás da arquitetura de microsserviços. Além de direcionar as decisões, são apresentados alguns
padrões encontrados durante o período de pesquisa. Portanto, é válido supor que utilização deste
guia em conjunto à arquitetura de referência (YU;SILVEIRA;SUNDARAM, 2016, p. 1858)
apresentem um ótimo ponto de partida.
        Nas seções seguintes são abordados os principais padrões utilizados nas diversas categorias
de componentes existentes em uma arquitetura baseada em microsserviço.

         2.1.    Identificação/Delimitação
        A delimitação dos limites existentes no domínio do problema é o passo inicial para a
construção dos microsserviços. Entretanto, não existe uma regra geral que possa ser utilizada para
identificar esses limites. O primeiro ponto a ser considerado é o conhecimento completo sobre o


3
 “After we moved our applications to a Microservices architecture, we observed increased deployability, modifiability,
and resilience to architecture erosion, [...]”


[PAGINA 7]
                                                                                                                     7
domínio do problema para qual será desenvolvido o software. Este conhecimento auxiliará a
identificação através do uso de algumas técnicas.
        Segundo Newman (2015) um bom microsserviço deve ser fracamente acoplado e altamente
coeso. Para que essas características consigam ser alcançadas é importante que durante o processo
de delimitação alguns princípios sejam observados.
        O primeiro é o princípio da responsabilidade única. “Uma classe deve ter apenas uma razão
para mudar” (MARTIN; MARTIN, 2006, p. 115, tradução nossa)4. Aplicando ao contexto de
microsserviço, significa que devemos criar microsserviços que possuam única responsabilidade.
Dessa forma, reduzimos o tamanho de cada serviço e construímos componentes mais coesos e
estáveis.
        O segundo princípio é o princípio do fechamento comum. “As classes de um pacote devem
ser fechadas em conjunto contra os mesmos tipos de alterações. Uma alteração que afeta um pacote
afeta todas as classes desse pacote.” (MARTIN; MARTIN, 2006, p. 419, tradução nossa)5.
Aplicando ao contexto de microsserviços, significa que devemos organizar no mesmo
microsserviço os componentes que mudam pela mesma razão. Consequentemente, deve-se
organizar em microsserviços separados os componentes que mudam por razões distintas.
        Utilizando os princípios mencionados anteriormente temos a base para identificarmos os
limites de candidatos a microsserviços. Considerando que já existe uma modelagem do domínio do
problema, uma ótima estratégia que pode ser utilizada é a identificação de contextos limitados.
        “Um CONTEXTO LIMITADO delimita a aplicabilidade de um modelo específico para que
os membros da equipe tenham uma compreensão clara e compartilhada do que deve ser consistente
e como se relacionar com outros CONTEXTOS.”(EVANS, 2003, p. 217, grifo do autor, tradução
nossa)6.
        A ideia é que cada modelo esteja em um limite explícito onde o mesmo é consistente e
válido, ou seja, possui um significado único e uma aplicabilidade restrita ao contexto. Neste ponto
surge uma dúvida: o que fazer quando um contexto precisa se comunicar com outro contexto?
        Segundo Newman (2015, p. 31, tradução nossa) “Cada contexto limitado possui uma
interface explícita, onde decide quais modelos compartilhar com outros contextos.”7. Portanto,
através das interfaces e do uso de modelos compartilhados os contextos conseguem se comunicar.
Neste momento é muito importante esclarecer dois pontos: dentro de cada contexto existem
modelos que não precisam ser comunicados externamente; assim como existem modelos que
precisam ser compartilhados com outros contextos.
        Inicialmente, a identificação de contextos limitados pode parecer uma tarefa complexa.
Realmente, demanda uma alta sensibilidade e um alto nível de conhecimento sobre o domínio do
problema. E isso pode ser um problema maior para domínios com definições instáveis. Nestes
casos, somente o amadurecimento a respeito do conhecimento do domínio poderá resolver.
        Porém, quando identificados, os contextos limitados oferecem ótimos pontos de partida para
candidatos a microsserviços. A afirmação anterior é baseada em Newman (2015, p. 33) quando diz
que de forma geral, os microsserviços se alinham muito claramente aos contextos limitados.

4
  “A class should have only one reason to change.”
5
  “The classes in a component should be closed together against the same kinds of changes. A change that affects a
component affects all the classes in that component and no other components.”
6
  “A BOUNDED CONTEXT delimits the applicability of a particular model so that team members have a clear and
shared understanding of what has to be consistent and how it relates to other CONTEXTS.”
7
  “ Each bounded context has an explicit interface, where it decides what models to share with other contexts.”


[PAGINA 8]
                                                                                                           8
Entretanto, não significa que todos os contextos limitados precisam ser convertidos em
microsserviços. Nestas situações faz-se necessário utilizar os princípios citados anteriormente para
escolher quais contextos limitados estão mais adequados a serem convertidos em microsserviços.
        Richardson (2019), descreve dois padrões que podem ser utilizados para a identificação dos
limites e a construção dos microsserviços. O primeiro padrão é chamado de “Decompose by
Business Capability”, que significa “Decompor por Capacidade de Negócio”, seu objetivo é definir
microsserviços que correspondam aos recursos de negócios do software em questão. O conceito
chave neste padrão é a ideia de recurso de negócio, para Richardson (2019, p. 51, tradução nossa),
“[...] um recurso de negócios é algo que uma empresa faz para gerar valor.”8. Ou seja, são os
serviços prestados pela organização que geram valor e que definem o que a organização
essencialmente faz.
        O segundo padrão é chamado de “Decompose by Subdomain”, que significa “Decompor por
Subdomínio”, o objetivo deste padrão é utiliza o conceito de subdomínio, provido do DDD, para
identificar os limites e desenvolver os microsserviços. A aplicação deste padrão exige o
conhecimento mínimo de DDD, especificamente, os conceitos de domínio e subdomínio. Utilizando
este padrão cada subdomínio identificado é mapeado em um, ou mais, microsserviços. Richardson
(2019) esclarece que, independente do padrão utilizado, o essencial da abordagem deve ser analisar
o domínio de negócio e identificar as diferentes áreas de especialização, sejam através das
capacidades de negócio ou dos subdomínios.
        A tabela abaixo reúne os padrões descritos, além de links, disponíveis na coluna “FONTE”,
que podem ser utilizados para acessar o respectivo padrão no catálogo desenvolvido.
                                    Tabela 1 - Padrões Para Delimitação de Microsserviços

                           PADRÃO                                                         FONTE

           Decompose by Business Capability                                     Richardson (2019, p. 51)

                  Decompose by Subdomain                                        Richardson (2019, p. 54)
                                                     Fonte: Própria (2019).


           2.2.      Armazenamento
        A utilização de um banco de dados compartilhado é, segundo Newman (2015), a forma
mais comum de integração em qualquer sistema de software. Nesse cenário todos os serviços
compartilham o mesmo modelo de representação das entidades de negócios. E quando um serviço
precisa de informações de um outro serviço ele acessa o banco de dados e busca as informações
necessárias. Em termos de simplicidade é a melhor maneira, e a mais rápida, de permitir a troca de
informações em um sistema de software. Entretanto, o armazenamento centralizado adiciona
grandes problemas, principalmente, quando trata-se de uma abordagem baseada em microsserviços.
Newman (2015) destaca três principais problemas deste tipo de integração.
        O primeiro problema refere-se a vinculação e visualização dos detalhes internos de
implementação dos serviços. Quando permitimos que outros serviços acessem os dados internos de
um serviço em particular, expomos os detalhes de implementação do mesmo. Se futuramente surgir
a necessidade de mudança no modelo de representação, será preciso realizar a alteração em várias
partes, pois, todos os serviços que estejam ligados ao serviço alterado será impactado de alguma
8
    “[..] a business capability is something that a business does in order to generate value.”


[PAGINA 9]
                                                                                                  9
forma. Com isso o princípio de alta coesão e perdido e o sistema torna-se frágil, pois, pequenas
mudanças podem quebrar o sistema por completo.
        O segundo problema, refere-se ao alto acoplamento tecnológico resultante. Inicialmente
pode parecer a melhor escolha armazenar os dados em um banco de dados relacional, o que obriga a
todos os serviços utilizarem um driver específico para realizar a conexão com o banco de dados.
Porém, se futuramente surgir a necessidade de modificar a tecnologia de persistência, e passar a
utilizar um banco de dados não relacional, todos os serviços terão que ser modificados. O que
implica na perda do princípio de baixo acoplamento e adiciona mais fragilidade ao sistema,
impedindo que os serviços evoluam de forma independente.
        O terceiro, e último problema, refere-se a total perda de coesão. Pois, a lógica associada a
manipulação dos dados armazenados no banco estará distribuída entre todos os serviços. O que
consequentemente, adiciona mais fragilidade ao sistema, pois, uma simples mudança no modelo de
representação, implicaria na mudança em todos os serviços que manipulasse o modelo alterado.
        Com o objetivo de evitar os problemas citados, abordagens baseadas em microsserviços
costumam utilizar um armazenamento descentralizado. O que significa que cada serviço possuirá
seu próprio modelo de representação das entidades de negócios. Além de possuir sua própria base
de dados, que por sua vez pode utilizar qualquer tecnologia de armazenamento. Assim, cada serviço
consegue expor apenas as informações necessárias aos demais serviços, ocultando detalhes internos
de implementação. No caso de um serviço precisar de informações de um outro serviço, o mesmo
realizará uma solicitação ao respectivo serviço e receberá uma resposta com as informações
solicitadas.
        A forma de comunicação entre os serviços pode variar de acordo com as decisões tomadas
durante a fase de projeto e definição da arquitetura. Algumas das opções e pontos a serem
considerados são discutidos no próximo tópico deste guia.

       2.3.   Comunicação
        O que define a forma de interação entre os serviços são as escolhas tomadas a respeito do
estilo de interação que pretende-se adotar. Para Newman (2015) uma das decisões mais
importantes, em termos de colaboração entre serviços, é a escolha entre uma comunicação síncrona
ou assíncrona. Segundo o autor, com a comunicação síncrona é mais fácil de desenvolver o
software ,pois, sabe-se quando as coisas foram concluídas. Entretanto, o agente que realizou a
solicitação fica bloqueado até a solicitação ser finalizada.
        Já com a comunicação assíncrona, não existe bloqueio durante a operação, porém, projetar e
desenvolver software utilizando comunicação assíncrona é razoavelmente mais complexo. Além da
escolha entre sincrono e assincrono, Richardson (2019), adiciona uma dimensão, que deve ser
considerada nas decisões sobre a forma de interação entre serviços. O mesmo define, portanto, duas
dimensões a serem consideradas para a definição do estilo de interação. A primeira, trata se a
comunicação será de um-para-um ou de um-para-muitos. Quando a comunicação é do tipo
um-para-um, significa que cada solicitação será processada por apenas um serviço. Já para o tipo
um-para-muitos, significa que as solicitações podem ser processadas por mais de um serviço.
        De acordo com as escolhas tomadas serão habilitados tipos específicos de interação, a tabela
2 identifica os estilos de interação com base nas dimensões abordadas.
                                     Tabela 2 - Estilos de Interação


[PAGINA 10]
                                                                                                   10

                                 um-para-um                              um-para-muitos

   Sincronismo              Requisição/Resposta                                    ---

  Assincronismo       Requisição/Resposta assíncrono                  Publicação/Assinatura
                       Notificações unidimensionais               Publicação/Resposta assíncrono

                            Fonte: Adaptado de RICHARDSON (2019, p. 67).
           ● Requisição/Resposta: o cliente realiza uma solicitação e aguarda até receber uma
              resposta;
           ● Requisição/Resposta assíncrono: segue o mesmo princípio da requisição/resposta,
              porém, o cliente não é bloqueado durante a operação;
           ● Notificações unidimensionais: o cliente envia uma solicitação para um serviço,
              entretanto, nenhuma resposta é esperada;
           ● Publicação/Assinatura: o cliente publica uma mensagem de notificação, que é
              consumida por nenhum ou mais de um serviços interessados. Os serviços
              interessados são chamados de assinantes;
           ● Publicação/Resposta assíncrono: o cliente utiliza a publicação de uma mensagem
              para realizar uma solicitação e aguarda um período de tempo enquanto recebe as
              respostas dos serviços interessados.
       A tabela abaixo reúne os padrões descritos por Richardson (2019), além de links,
disponíveis na coluna “FONTE”, que podem ser utilizados para acessar o respectivo padrão no
catálogo desenvolvido.
                        Tabela 3 - Padrões Para Comunicação Entre Microsserviços

                   PADRÃO                                                  FONTE

         Remote Procedure Invocation                               Richardson (2019, p. 72)

                  Messaging                                        Richardson (2019, p. 85)
                                         Fonte: Própria (2019).

        Além da escolha a respeito do tipo de interação, o formato de dado utilizado durante a
comunicação é outro ponto a ser definido, e possui igual importância para uma colaboração bem
sucedida entre serviços.
        Para Richardson (2019) existem duas principais categorias em relação aos formatos de
dados utilizados: os formatos baseados em texto e os formatos binários. Segundo Newman (2015) a
utilização de formatos de dados baseado em texto, como XML e JSON, oferecem uma alta
flexibilidade no processo de colaboração entre serviços. O mesmo autor esclarece que o JSON tem
se tornado mais popular, principalmente, quando utilizado em conjunto ao protocolo HTTP.
Richardson (2019) destaca que uma das vantagens da utilização de formatos textuais é que eles são
facilmente compreendidos pelos humanos e são auto-descritivos.
        A simplicidade e a compactação tem aumentado o uso de JSON como formato padrão para
troca de dados em aplicações web. Entretanto, Newman (2015) destaca que o XML possui algumas
vantagens sobre o JSON, como por exemplo, o controle de link que pode ser utilizado como
controle de hipermídia.


[PAGINA 11]
                                                                                                   11
        Como desvantagens a utilização de formatos baseados em texto, Richardson (2019), destaca
a sobrecarga adicionada aos dados, pois, toda mensagem precisa conter além dos valores o nome de
cada atributo. Portanto, se a eficiência e o desempenho forem altamente importantes, Richardson
(2019), aconselha considerar o uso de formato binário.
        Sobre os formatos binário, para Richardson (2019), os dois formatos mais populares são
Protocol Buffers e o Avro. O autor enfatiza que ambos os formatos fornecem uma Linguagem de
Definição de Interfaces (IDL) utilizada para definir a estrutura de seus dados. Depois de definidas
as estruturas, um compilador, gera o código que será utilizado para serializar e desserializar as
mensagens.
        Uma possível desvantagem no uso de formatos binário é a exigência em adotar uma
abordagem de primeiro definir totalmente a interface dos serviços antes de iniciar o
desenvolvimento dos mesmo. A tabela 4 reúne os formatos de dados discutidos além de conter
referências para obtenção de mais detalhes a respeito da utilização dos respectivos formatos de
dados.
                                Tabela 4 - Principais Formatos de Dados

   FORMATO             CATEGORIA                                    REFERÊNCIA

      XML             Formato Textual                      www.w3.org/XML/Schema

      JSON            Formato Textual                            http://json-schema.org

 Protocol Buffers     Formato Binário       https://developers.google.com/protocol-buffers/docs/
                                                                  overview

      Avro            Formato Binário                            https://avro.apache.org
                                        Fonte: Própria (2019).

       2.4.   Exposição
        A forma como os clientes consomem os microsserviços, da camada de domínio, tem grande
importância dentro de uma arquitetura de microsserviços. Quando feita corretamente, simplifica o
desenvolvimento dos aplicativos consumidores e desacopla os consumidores da arquitetura interna,
permitindo que os microsserviços evoluam sem afetar os consumidores.
        Alguns padrões propõem que os consumidores realizem solicitações diretamente aos
microsserviços da camada de domínio, por exemplo o padrão conhecido como “Aggregator”.
Entretanto, muitos problemas surgem como consequência da utilização de alguns desses padrões.
Richardson (2019) destaca alguns desses problemas, o primeiro problema é que os clientes precisam
realizar várias solicitações para conseguir montar uma visualização, o que prejudica a experiência
do usuário. O segundo problema é com muitas solicitações o cliente precisa realizar um processo de
composição ao reunir as resposta e montar a visualização, processo conhecido como “Composição
de API”. Tarefa que claramente não deveria ser responsabilidade dos aplicativos consumidores,
pois, além de acoplar os consumidores à arquitetura interna, aumenta a complexidade dos
aplicativos consumidores.
        Outro problema é a falta de encapsulamento entre os consumidores e a arquitetura interna,
prejudicando a evolução dos microsserviços. Já que alterações nos microsserviços podem resultar
em problemas nos consumidores, impedindo que os microsserviços da camada de domínio evoluam


[PAGINA 12]
                                                                                                12
de forma autônoma. E por último, os microsserviços da camada de domínio podem exigir a
utilização de protocolos de comunicação que podem não ser bem aceitos pelos aplicativos
consumidores.
        Objetivando resolver os problemas descritos, ou pelos menos mitigá-los, Richardson (2019)
descreve dois padrões que podem ser utilizados para externalizar os microsserviços da camada de
domínio.
        O primeiro padrão é conhecido como “API Gateway”, que especifica a criação de um
serviço responsável em ser o único ponto de entrada para os microsserviços da camada de domínio,
realizando tarefas como composição da API, roteamento de solicitações, autenticação e autorização,
monitoramento entre outras. Segundo Richardson (2019) um API Gateway funciona como uma
fachada que encapsula a arquitetura interna do software e expõem uma API pública aos
consumidores.
        O uso do API Gateway permite que diversos tipos de consumidores acessem as
funcionalidades implementadas pelos microsserviços da camada de domínio sem que haja um alto
acoplamento entre consumidores e a arquitetura interna e sem a obrigação em realizar várias
solicitações. Entretanto, Richardson (2019) destaca que o uso do API Gateway possui algumas
desvantagens, como a inserção de mais um componente na arquitetura a ser desenvolvido,
implantado e mantido. Além do risco do API Gateway acaba se tornando um gargalo dentro da
arquitetura do software.
        O segundo padrão é conhecido como “Backends for Frontends”, e funciona como uma
variação do padrão API Gateway. Porém, seu uso descreve a criação de um API Gateway para cada
tipo de consumidor, permitindo explorar características e suprir necessidades específicas para cada
tipo de consumidor. Richardson (2019) destaca como principais benefícios deste padrão a definição
mais clara das responsabilidades, o maior isolamento entre os consumidores e a arquitetura interna,
o isolamento de falhas, a capacidade de escalar cada um dos API Gateway de forma independente
além da redução no tempo de inicialização, já que cada API Gateway dentro do BFF é um
aplicativo menor e mais simples.
        A tabela abaixo reúne os padrões descritos, além de links, disponíveis na coluna “FONTE”,
que podem ser utilizados para acessar o respectivo padrão no catálogo desenvolvido.
                           Tabela 5 - Padrões Para Exposição dos Microsserviços

                 PADRÃO                                                    FONTE

                API Gateway                                        Richardson (2019, p. 259)

          Backends for Frontends                 Newman (2015, p. 71) e Richardson (2019, p. 265)
                                          Fonte: Própria (2019).

       2.5.   Descoberta
        Arquiteturas distribuída clássicas utilizam, normalmente, endereços estáticos permitindo
total conhecimento das localizações dos componentes. Já arquiteturas baseada em microsserviços
tendem a utilizar endereçamento dinâmico, principalmente, devido ao escalonamento automático, as
falhas e as atualizações nos microsserviços.
        Por consequência, algum mecanismo de descoberta de serviço deve ser disponibilizado aos
os aplicativos consumidores. Esse mecanismo é geralmente implementado na forma de um “Service


[PAGINA 13]
                                                                                                   13
Registry”, que possui a responsabilidade de registrar a localização de todas as instâncias disponíveis
na arquitetura. Conceitualmente a tarefa deste serviço é armazenar em um banco de dados os
endereços de rede e a porta onde funciona cada instância dos processos dos microsserviços
disponíveis.
         Onde acontece a descoberta dos microsserviços e como funciona a dinâmica de registro das
instâncias, definem o par de padrões a serem utilizados. Richardson (2019), descreve um conjunto
de quatro padrões que podem ser utilizados para a implementação de um Service Registry.
         O primeiro padrão é conhecido como “Client-side Discovery”, que atribui ao aplicativo
cliente a responsabilidade em consultar o Service Registry. Dessa forma, quando um aplicativo
cliente/consumidor precisa realizar alguma solicitação aos microsserviços da arquitetura, primeiro,
acessa o Service Registry e obtêm a localização de uma instância disponível do microsserviço
desejado. Depois de obter a localização o cliente pode realizar a solicitação, seja, comunicando-se
diretamente com os microsserviços ou solicitando ao API Gateway.
         O segundo padrão é conhecido como “Server-side Discovery”, que atribui a
responsabilidade em consultar o Service Registry à um dos componentes da arquitetura interna,
normalmente ao API Gateway. Dessa forma, o cliente/consumidor realiza a solicitação ao API
Gateway, que acessa o Service Registry e obtêm a localização de uma instância disponível do
microsserviço desejado. Depois de obter a localização o API Gateway encaminha a solicitação a
respectiva instância e retorna a resposta ao cliente/consumidor. A mesma dinâmica é válida caso
utilize o padrão “Backends for Frontends”.
         Essencialmente a diferença entre os dois padrões descritos é, a quem deve ser atribuída a
responsabilidade em consultar o Service Registry, cliente ou servidor? Com base na resposta
obtém-se o padrão a ser utilizado. Os próximos dois padrões definem diferentes formas como as
instâncias podem ser registradas e “des-registradas” no Service Registry.
        O padrão conhecido como “Self-Registration” atribui a cada instância de serviço a
responsabilidade em registrar-se no Service Registry, devendo fazê-la durante o processo de
inicialização da própria instância. Atualizando, periodicamente o status do registro através de
periódicas solicitações ao Service Registry. E consequentemente, durante o processo de
encerramento da instância deve-se realizar o cancelamento do registro.
        E finalizando os padrões de descoberta de serviços, temos o padrão conhecido como “3rd
Party Registration” que atribui a responsabilidade em registrar cada instância de serviço à um
terceiro serviço conhecido como “Registrador”. Na verdade, não é necessariamente um terceiro
serviço, pode ser o próprio Service Registry ou algum serviço provido pela plataforma de
implantação. A dinâmica de registrar durante a inicialização e cancelar o registro durante o
encerramento continua sendo utilizada, porém, as instâncias não mais se preocupam em fazê-la.
        A tabela abaixo reúne os padrões descritos, além de links, disponíveis na coluna “FONTE”,
que podem ser utilizados para acessar o respectivo padrão no catálogo desenvolvido.
                           Tabela 6 - Padrões Para Descoberta dos Microsserviços

                    PADRÃO                                                   FONTE

              Client-side Discovery                                Richardson (2019, p. 83)

              Server-side Discovery                                Richardson (2019, p. 85)

                Self-Registration                                  Richardson (2019, p. 82)


[PAGINA 14]
                                                                                                 14

              3rd Party Registration                             Richardson (2019, p. 85)
                                        Fonte: Própria (2019).

       2.6.    Monitoramento
        Conhecer o estado operacional de um software permite, não só, a identificação mas também
a resolução de problemas. E preferencialmente, antes que os problemas afetem os usuários do
software. Tradicionalmente, a tarefa de monitorar a saúde de um sistema em produção é
direcionada à uma equipe exclusiva, conhecida como equipe de operações.
        Adotar alguns padrões ao projetar componentes de monitoramento pode facilitar os
processos e expor melhores informações a respeito do comportamento de um sistema em produção.
Richardson (2019) descreve um conjunto de seis padrões amplamente adotados em sistemas com
arquiteturas baseadas em microsserviços, alguns deles podem inclusive ser utilizados em conjunto.
        O primeiro padrão é conhecido como “Health Check API”, que atribui ao próprio
microsserviço a responsabilidade em expor informações de integridade da instância em
funcionamento. Através da definição de um endpoint específico, que pode ser consultado
periodicamente, expõe informações atualizadas sobre a saúde da instância. Quais informações e
como elas devem ser expostas são decisões que os próprios desenvolvedores, em conjunto com a
equipe de operações, devem tomar.
        O segundo padrão é conhecido como “Log Aggregation”. Uma das melhores maneiras de
rastrear erros e obter informações sobre o estado de um componente de software e consultando seus
arquivos de log, entretanto, em um sistema baseado em microsserviço esta tarefa é um pouco mais
complexa. Isso, pois, a execução de uma operação gerar diversos registros de logs distribuídos entre
as várias instâncias de serviços. Neste cenário é necessário utilizar um serviço de agregação para
reunir em um banco de dados os registros de logs de todos os serviços em execução. O
armazenamento centralizado dos registros de logs permite a utilização de ferramentas gráficas para
visualizar, pesquisar e analisar o comportamento do sistema de forma mais eficaz.
         O terceiro padrão é conhecido como “Distributed Tracking”, utilizado para rastrear todo o
ciclo de vida de cada solicitação, incluindo informações de cada serviço necessário para
completá-la. Para tanto, o padrão define a atribuição a cada solicitação de entrada de um
identificador exclusivo, que deve ser repassado a todas as chamadas de serviços, permitindo o
rastreio nos registros de logs e em ferramentas gráficas. Além do identificador, outras informações
podem ser adicionadas como hora de início e hora de término da solicitação.
        A utilização de arquivos de logs são úteis para acompanhar as operações e o estado do
aplicativo. Entretanto, quando tratamos sobre as exceções, existe pouco aproveitamento dos
arquivos de log. Exceções são sinais de possíveis falhas, ou erros, e registrá-las adequadamente
permite um melhor acompanhamento das mesmas. Gerar alertas e rastrear exceções não resolvidas
são alguns dos benefícios em utilizar um padrão de rastreamento de exceções. Com a finalidade de
suportar o monitoramento personalizado das exceções temos o quarto padrão, "Exception
Tracking", que atribui ao Serviço de Monitoramento a responsabilidade em registrar todas as
exceções ocorridas. Além do simples armazenamento, o serviço deve remover duplicidade nas
exceções, gerar alertas e gerenciar a resolução das exceções ocorridas. Essas funcionalidades podem
ser expostas através de uma API, ou fornecendo bibliotecas de integração aos demais serviços
permitindo o registro das exceções.


[PAGINA 15]
                                                                                                    15
        Richardson (2019) destaca duas soluções que utilizam o padrão Exception Tracking. A
primeira é uma solução baseada em nuvem chamada HoneyBadger 9e a segunda , um projeto de
código aberto, Sentry.io10, de fácil implantação em uma infraestrutura própria.
        Além do acompanhamento das exceções, alguns aplicativos precisam registrar as ações de
cada um de seus usuário. O acompanhamento dos usuários fornece um conjunto de informações que
podem ser utilizadas em operações de ajuda e suporte ao cliente, garantia de conformidade dos
serviços e detecção de usuários suspeitos. O padrão, "Audit logging", descreve um conjunto de
ações a fim de registrar as operações realizadas por cada usuário do sistema. Cada entrada no log de
auditoria deve ser composta pela identificação do usuário, a ação que o usuário executou e os
recursos de negócios manipulados.
        Segundo Richardson (2019), existem basicamente três formas de implementar o padrão de
auditoria, a primeira possibilidade seria adicionando o código de log de auditoria diretamente na
camada de lógica de negócios, corresponde a forma mais simples, porém, acopla a lógica de
negócio com interesses transversais, dificultando evolução e manutenção. Outra possibilidade é
utilizar a programação orientada a aspectos, isolando a lógica de geração de logs de auditoria em
um componente específico e invocado a intercalação quando necessário. Uma terceira
possibilidade, é utilizar a programação baseada em eventos, adicionando a identificação do usuário
durante cada operação e realizando a emissão dos eventos de logs.
        E finalizando os padrões de monitoramento temos o padrão “Application Metrics”, que
descreve o comportamento de um serviço de monitoramento centralizado que armazena todas as
métricas coletadas e prover funcionalidades como agregação, visualização e emissão de alertas.
Normalmente as métricas reunidas fornecem informações críticas sobre a integridade do aplicativo,
reportando informações de todas as camadas do mesmo. Em seu nível mais baixo, reportando
métricas a respeito da infraestrutura, como consumo de CPU, memória, e disco. Até o nível mais
alto, reportando métricas em nível do aplicativo como números de solicitações, latência nas
solicitações etc.
        Segundo Richardson (2019), as métricas costumam possuir três informações básicas: o
nome da métrica; o valor coletado; e o timestamp, especificando o horário da coleta. Entretanto,
outras informações podem e devem ser adicionadas de acordo com as necessidades do projeto.
Alguns sistemas de monitoramento costuma adotar o conceito de dimensões para fornecer
informações como o nome da máquina ou o nome do serviço além de identificadores de instância
dos serviços.
        A tabela abaixo reúne os padrões descritos, além de links, disponíveis na coluna “FONTE”,
que podem ser utilizados para acessar o respectivo padrão no catálogo desenvolvido.
                                         Tabela 7 - Padrões Para Monitoramento

                            PADRÃO                                               FONTE

                      Application Metrics                                Richardson (2019, p. 373

                         Audit Logging                                  Richardson (2019, p. 377)

                      Distributed Tracing                               Richardson (2019, p. 370)


9
    h​ ttp://www.honeybadger.io/
10
       h​ ttps://sentry.io/welcome/


[PAGINA 16]
                                                                                                                      16

                   Exception Tracing                                       Richardson (2019, p. 376)

                   Health Check API                                        Richardson (2019, p. 366)

                   Log Aggregation                                         Richardson (2019, p. 368)
                                                 Fonte: Própria (2019).

         2.7.     Tolerância a Falhas
        Um dos benefícios em utilizar sistemas distribuídos é a capacidade de decompor o sistema
em várias partes. E tratando-se de uma arquitetura de microsserviços as partes são implementadas
em formas de serviços autônomos, e como discutidos na s​ eção 2.1 sobre identificação e delimitação
dos microsserviços, um dos princípios de um bom microsserviço é o conceito de baixo
acoplamento.
        Garantir o mínimo de acoplamento permite que os serviços evoluam de forma autônoma e
sem desencadear erros aos seus consumidores. Entretanto, segundo Fowler (2011, n. p., tradução
nossa), "[...] não é possível eliminar completamente o acoplamento, pois os serviços ainda precisam
se comunicar entre si por meio de suas interfaces."11. Com o objetivo de reduzir o acoplamento
causado pela comunicação Fowler (2011) recomenda adotar uma estratégia conhecida como
“Tolerant Reader”, segundo o autor, a comunicação entre os serviços deve ser regida pela lei de
Postel.
        A lei de Postel diz, “seja conservador no que você faz, seja liberal no que você aceita dos
outros.”(POSTEL, 1981, p. 13, tradução nossa)12. Este é o princípio do Tolerant Reader, cada
serviço deve expor o mínimo de detalhe sobre o funcionamento interno e deve prosseguir em
funcionamento usando apenas os elementos que precise e ignorando tudo que não seja necessário
para a conclusão da operação. Mesmo que os serviços retornem respostas em desacordo com o
especificado na interface, os seus consumidores devem manter-se em funcionamento e continuar
com a operação, exceto quando as resposta não contiverem os elementos mínimos necessário para
executar a respectiva lógica de negócio.
        Outra recomendação trazida por Fowler (2011) é realizar o mínimo de suposições possíveis
sobre a estrutura das respostas recebidas, dessa forma, alterações nas estruturas dos dados terão o
mínimo de impacto. Uma forma de reduzir as suposições é utilizar consultas XPath13 para extrair as
propriedades desejadas das cargas úteis XML ou JSONPath14 para JSON e o mesmo princípio para
outros tipos de dados possíveis.
        Além do acoplamento causado pela comunicação, outro problema oriundo da distribuição
dos serviços é a possibilidade de falhas parciais ocasionarem falhas em cascata causando uma
interrupção em todo o sistema. Esse fenômeno acontece, principalmente, quando utiliza-se
mecanismo de comunicação síncrono onde um dos serviços torna-se incapaz de responder às
solicitações em tempo hábil bloqueado indefinidamente até o recebimento da resposta.



11
   "[...] you cannot eliminate the coupling completely because the services still have to communicate to each other
through their interfaces."
12
    “be conservative in what you do, be liberal in what you accept from others.”
13
   ​https://www.w3schools.com/xml/xml_xpath.asp
14
   ​https://goessner.net/articles/JsonPath/


[PAGINA 17]
                                                                                                17
        Muitos são os motivos para um serviço demorar a responder uma solicitação. O mesmo
pode encontrar-se inoperante devido a uma falha ou manutenção, ou o serviço encontrar-se
sobrecarregado e respondendo de forma extremamente lenta.
        Objetivando reduzir a ocorrência de falhas em cascata e construir arquiteturas distribuídas
resilientes, o padrão Circuit Breaker descreve um conjunto de medidas a serem adotadas e
implementadas pelos serviços que compõem a arquitetura interna. Basicamente, o Circuit Breaker
funciona como uma máquina de estado que permite a passagem das solicitações aos serviços
quando seu estado é DESATIVADO. E consequentemente, quando o Circuit Breaker encontra-se
ATIVADO, todas as solicitações são imediatamente recusadas. Após um período de tempo o estado
do Circuit Breaker é atualizado e, dependendo da disponibilidade do serviço, volta para o estado
DESATIVADO.
        O ativamento é feito rastreando a quantidade de solicitações bem sucedidas e com falhas, e
calculando uma taxa de erro. Quando a taxa excede um limite predefinido o Circuit Breaker é
ativado e após um período de tempo seu estado é atualizado. O funcionamento desse padrão é
fundamentado na ideia de que se um grande número de solicitações retornam falha sugere que o
respectivo serviço encontra-se indisponível e encaminhar novas solicitações ao mesmo é inútil.
        Além do padrão Circuit Breaker, Richardson (2019), específica a utilização de outros dois
mecanismos para lidar com falhas. O autor refere-se a abordagem descrita por Christensen (2012) e
adotada pela Netflix, que combina o Circuit Breaker com o uso de timeouts e limites de solicitações
pendentes por cliente. Os "Network timeouts" garantem que os recursos nunca sejam bloqueados
indefinidamente, especificando um tempo limite ao aguardar uma resposta. E limitando o número
de solicitações pendentes garante-se que não ocorra o acúmulo de solicitações inúteis a serviços
indisponíveis.
        A tabela abaixo reúne os padrões descritos, além de links, disponíveis na coluna “FONTE”,
que podem ser utilizados para acessar o respectivo padrão no catálogo desenvolvido.
                               Tabela 8 - Padrões Para Tolerância a Falhas

                   PADRÃO                                                    FONTE

                Tolerant Reader                                       Fowler (2011, n. p.)

                Circuit Breaker                                    Richardson (2019, p. 78)
                                          Fonte: Própria (2019).

       2.8.   Resumo dos Padrões
        A figura 5 reúne todos os padrões citados nas seções anteriores, esquematizados e separados
por categoria, com o objetivo de facilitar a compreensão dos mesmos. Para correta compreensão da
figura 5 é necessário entender de antemão a legenda utilizada na construção da figura.
        O retângulo de linhas contínua representa o padrão especificado na descrição contida no
centro do mesmo. A figura abaixo demonstra a representação de um padrão de nome “Padrão”.
                                  Figura 1 - Representação de um Padrão.




                                  Fonte: Adaptado de Richardson (2019).


[PAGINA 18]
                                                                                               18
        O retângulo de linhas tracejada representa uma categoria especificada na descrição contida
no topo do mesmo. É dentro dos retângulos de categoria que estarão os seus respectivos padrões. A
figura abaixo demonstra a representação de uma categoria de nome “Categoria”.
                               Figura 2 - Representação de uma Categoria.




                                 Fonte: Adaptado de Richardson (2019).
       As linhas tracejada com setas em ambas as extremidades representam um condicional, onde,
apenas um dos padrões ligados por elas poderá ser escolhido. Lembrando que as linhas podem
aparecer na horizontal ou na vertical mas o significado permanece o mesmo. A figura abaixo
demonstra a representação de um condicional, onde, aplica-se a “Alternativa A” ou a “Alternativa
B”.
                               Figura 3 - Representação de um Condicional.



                                 Fonte: Adaptado de Richardson (2019).
        Já as linhas contínua com seta em uma única extremidade representam uma relação de
Predecessor e Sucessor, onde, o padrão do lado sem seta representa o padrão predecessor e,
consequentemente, o padrão do lado com seta representa o padrão sucessor. Lembrando que as
linhas podem aparecer na horizontal ou na vertical mas o significado permanece o mesmo. A figura
abaixo demonstra a representação discutida.
                      Figura 4 - Representação de uma Relação Predecessor/Sucessor.



                                 Fonte: Adaptado de Richardson (2019).
       Enfim, a figura abaixo, contém todos os padrões discutidos e esquematizados segundo as
representações explicadas anteriormente.
                                     Figura 5 - Resumo dos Padrões.




                                 Fonte: Adaptado de Richardson (2019).


[PAGINA 19]
                                                                                              19
     3.    Catálogo de Padrões
           3.1.     Consistência
                  3.1.1.       SAGA
Problema:
        Arquiteturas baseadas em microsserviços costuma utilizar uma abordagem diferente para a
persistência dos dados, essa abordagem é conhecida como “Gerenciamento de Dados
Descentralizado”15. Nessa abordagem cada serviço tem seu próprio banco de dados. Algumas
transações comerciais, no entanto, abrangem vários serviços, de modo que você precisa de um
mecanismo para garantir a consistência dos dados nos serviços. Como manter a consistência dos
dados nos serviços em transações que abrangem vários serviços?

                           3.1.1.1.   Choreography-Based
                                       Figura 6 - SAGA Baseada em Coreografia.




                                               Fonte: Richardson (s.d.).


Descrição do Padrão:
       Utilizando saga com coreografia, cada transação local publica eventos de domínio que
acionam transações locais em outros serviços.

Consequência do Uso:
        A aplicação do padrão permite que um aplicativo mantenha consistência de dados em vários
serviços sem usar transações distribuídas. Porém, o modelo de programação é mais complexo,
sendo necessário implementar transações compensadoras que explicitamente desfazem alterações
feitas anteriormente em uma saga.

Exemplos de Uso:
       Projeto do próprio Chris Richardson que implementa o padrão SAGA. Tram Saga,
disponível em: h​ ttps://github.com/eventuate-tram/eventuate-tram-sagas

15
     h​ ttps://www.martinfowler.com/articles/microservices.html#DecentralizedDataManagement


[PAGINA 20]
                                                                                             20


Referências:
      Richardson (s.d.), disponível em: h​ ttps://microservices.io/patterns/data/saga.html

                       3.1.1.2.   Orchestration-Based
                                   Figura 7 - SAGA Baseada em Orquestração.




                                           Fonte: Richardson (s.d.).
Descrição do Padrão:
       Utilizando saga com orquestração, um orquestrador (objeto) informa aos participantes que
transações locais devem ser executadas.

Consequência do Uso:
        A aplicação do padrão permite que um aplicativo mantenha consistência de dados em vários
serviços sem usar transações distribuídas. Porém, o modelo de programação é mais complexo,
sendo necessário implementar transações compensadoras que explicitamente desfazem alterações
feitas anteriormente em uma saga.

Exemplos de Uso:
       Projeto do próprio Chris Richardson que implementa o padrão SAGA. Tram Saga,
disponível em: ​https://github.com/eventuate-tram/eventuate-tram-sagas

Referências:
      Richardson (s.d.), disponível em: h​ ttps://microservices.io/patterns/data/saga.html

       3.2.     Comunicação
              3.2.1.      Messaging
                                         Figura 8 - Padrão Messaging.


[PAGINA 21]
                                                                                                 21




                                   Fonte: Adaptado de Gupta (2015).
Problema:
       Para concluir uma determinada operação do cliente um serviço pode precisar invocar
funcionalidades de outros serviços. Como esses serviços devem se comunicar para realizar as
operações? Qual deve ser o estilo das mensagens trocadas entre os serviços?

Descrição do Padrão:
       O padrão de mensagens assíncronas define um ponto central de comunicação onde os
microsserviços “conversam”, tornando a comunicação assíncrona e não bloqueando os clientes.
Esse ponto central pode ser uma fila de mensagens utilizando protocolos específicos como amqp ou
websockets, ou outros mecanismos e serviços que forneçam tal funcionalidade.

Consequência do Uso:
       O uso do padrão de mensagens assíncronas adiciona complexidades trazidas pelo
assincronismo, como responsabilidades descentralizadas. Muitas vezes necessitam de protocolos de
comunicação específicos, o que pode se tornar um problema para os desenvolvedores. Em
contrapartida, os cliente não são mais bloqueados durante as operações e adicionam uma maior
confiabilidade durante a comunicação entre os microsserviços. Em alguns casos, o uso misto de
sincronismo e assincronismo costuma se bem proveitoso.

Exemplos de Uso:
        Richardson (2015, p. 92) cita as principais tecnologias utilizadas para implementar o padrão
Messaging, são elas:
            ● ActiveMQ, disponível em: h​ ttp://activemq.apache.org
            ● RabbitMQ, disponível em: h​ ttps://www.rabbitmq.com
            ● ZeroMQ, disponível em: h​ ttp://zeromq.org
            ● Apache Kafka, disponível em: ​http://kafka.apache.org
            ● AWS Kinesis, disponível em: ​https://aws.amazon.com/kinesis/
            ● AWS SQS, disponível em: h​ ttps://aws.amazon.com/sqs/
Referências:
        Gupta (2015), disponível em: h​ ttp://blog.arungupta.me/microservice-design-patterns/
        Richardson (s.d.), disponível em:
https://microservices.io/patterns/communication-style/messaging.html


[PAGINA 22]
                                                                                                22




             3.2.2.   Remote Procedure Invocation
Problema:
        Ao utilizar uma arquitetura baseada em microsserviços é necessário escolher mecanismos
que permitam aos clientes invocar as funcionalidades expostas pelos serviços. Além disso, os
próprios serviços precisam, às vezes, colaborar entre si para completar algumas das solicitações
feitas pelos clientes. Portanto, é necessário o uso de um protocolo de comunicação entre processos.

Descrição do Padrão:
        O padrão Remote Procedure Invocation - RPI define a utilização de protocolos RPI para
permitir a comunicação entre serviços. O cliente usa um protocolo baseado em solicitação / resposta
para fazer solicitações a um serviço.

Consequência do Uso:
        Ao aplicar o padrão RPI os serviços passam a ser comunicar de forma simples e fácil de
implementar, pois, como citado por Richardson (s.d.) existem várias tecnologias que fornecem
mecanismos para comunicação entre processos. Entretanto, o uso de solicitação/resposta muitas
vezes não permite o uso de outros padrões de interação como notificações, solicitação/resposta
assíncrono, publicação/assinatura, entre outros.
        Além disso, no quesito disponibilidade há uma certa redução, pois, durante o período de
interação este tipo de comunicação exige que tanto o cliente como o serviço estejam ambos
amplamente disponíveis. E, dependendo de como este padrão é implementado, muitas vezes
torna-se necessário o uso de mecanismos para descoberta dos serviços, fornecendo aos clientes
formas de descobrir os locais de instâncias dos serviços.

Exemplos de Uso:
        Richardson (s.d.) cita as principais tecnologias utilizadas para implementar o padrão RPI,
são elas:
           ● REST
           ● gRPC, disponível em: ​http://www.grpc.io/
           ● Apache Thrift, disponível em: h​ ttps://thrift.apache.org/

Referências:
        Richardson (s.d.), disponível em:
https://microservices.io/patterns/communication-style/rpi.html

             3.2.3.   Shared Data Microservice
                                    Figura 9 - Padrão Shared Data.


[PAGINA 23]
                                                                                              23




                                   Fonte: Adaptado de Gupta (2015).
Problema:
       Durante o processo de migração alguns serviços acabam tendo que compartilhar
informações em cache ou em base da dados. E muitas vezes mesmo depois da total separação em
microsserviços, os mesmos continuam utilizando bases compartilhadas. O processo de separação e
normalização em vários banco de dados pode ser demorado.

Descrição do Padrão:
       Vale ressaltar que o compartilhamento de bases de dados entre microsserviços não é
aconselhável pela maioria dos autores por ferir os princípios da arquitetura de microsserviços.
Porém, o compartilhamento de dados pode se útil durante processo de migração, onde os serviços
ainda possuem base da dados compartilhados. Muito utilizado junto ao padrão de ramificação, pois,
normalmente microsserviços da mesma categoria compartilham dados, sejam em cache e de banco
de dados.

Consequência do Uso:
        O uso do padrão de dados compartilhados implica um forte acoplamento entre alguns
serviços. Torna-se útil, principalmente, durante uma fase de transição até que os microsserviços
serem totalmente autônomos. Ou, quando utilizado em conjunto com o padrão de ramificação, pois,
muitas vezes serviços no mesmo “pipeline” precisam compartilhar base de dados ou dados em
cache. Pelo alto acoplamento, mudanças nos schemas da base de dados pode “quebrar” os serviços.
Questões como coesão também são afetadas, já que serviços acabam conhecendo detalhes que não
são de sua responsabilidade.

Referências:
      Gupta (2015), disponível em: h​ ttp://blog.arungupta.me/microservice-design-patterns/

       3.3.     Delimitação/Decomposição
              3.3.1.   Decompose by Business Capability
                          Figura 10 - Padrão Decompose by Business Capability.


[PAGINA 24]
                                                                                                 24




                                  Fonte: Adaptado de Richardson (s.d.).
Problema:
       Em uma arquitetura baseada em microsserviços, tudo gira em torno dos serviços fornecidos
pela camada de domínio do negócio. É nesta camada onde estão os microsserviços que implementa
as funcionalidades providas pelo sistema em questão. Entretanto, identificar claramente os serviços
ou mesmo decompor uma aplicação monolítica pode ser altamente custoso e problemático. Quais
funcionalidades devem se tornar microsserviços? E mais, qual o tamanho adequado de um
microsserviço?

Descrição do Padrão:
        .O padrão Decompose by Capability Business define a criação de um serviço para cada
capacidade de negócio identificado no domínio do problema. Este padrão baseia-se no alinhamento
natural entre os conceitos de recursos de negócios e os serviços. No entanto, existem situações onde
um único recurso de negócio pode ser composto por vários serviços ou vice versa, mas começar a
modelagem baseando-se em um serviço para cada capacidade de negócio tem-se mostrado uma
ótima maneira de delimitar os serviços. Conforme a modelagem amadurece pode-se unir ou
dissociar os serviços conforme as demandas exigirem.

Consequência do Uso:
       Ao utilizar a decomposição por capacidade de negócio os serviços resultante são, na sua
grande maioria, altamente estáveis. Pois, normalmente, os recurso de negócios de uma
organização/empresa são relativamente estáveis. Portanto, quanto mais estáveis forem os recurso de
negócios da organização/empresa melhores serão os benefícios de se aplicar a decomposição por
capacidade de negócio. Além disso, a utilização do padrão habilita o desenvolvimento de equipes
multifuncionais e autônomas, visto que, os serviços resultantes são altamente coesos e fracamente
acoplados.
       Entretanto, identificar os recursos de negócios da organização/empresa pode ser uma tarefa
complexa, pois, demanda uma alta compreensão do domínio do problema. Muitas vezes torna-se
necessário uma detalhada análise do propósito, da estrutura, dos processos e das áreas de
especialização da organização/empresa. Richardson (s.d.) destaca que a estrutura da organização e o
modelo de domínio de alto nível, são bons pontos de partida para identificar recursos de negócios.

Referências:
        Richardson (s.d.), disponível em:
https://microservices.io/patterns/decomposition/decompose-by-business-capability.html


[PAGINA 25]
                                                                                                25


            3.3.2.    Decompose by Subdomian
                              Figura 11 - Padrão Decompose by Subdomain.




                                 Fonte: Adaptado de Richardson (s.d.).
Problema:
       Em uma arquitetura baseada em microsserviços, tudo gira em torno dos serviços fornecidos
pela camada de domínio do negócio. É nesta camada onde estão os microsserviços que implementa
as funcionalidades providas pelo sistema em questão. Entretanto, identificar claramente os serviços
ou mesmo decompor uma aplicação monolítica pode ser altamente custoso e problemático. Quais
funcionalidades devem se tornar microsserviços? E mais, qual o tamanho adequado de um
microsserviço?

Descrição do Padrão:
        O padrão Decompose by Subdomain define a criação de um serviço para cada subdomínio
identificado no domínio do problema. Este padrão baseia-se na utilização das técnica trazidas por
Evans (2003) em seu livro sobre DDD. Evans (2003) refere-se ao espaço do problema do sistema
como um domínio composto por vários subdominios, onde, cada um corresponde a uma área de
especificação do sistema que possui seus próprios modelos de representação e linguagem.

Consequência do Uso:
       Similar ao que acontece com o padrão de decomposição por capacidade de negócios, quanto
mais estáveis forem os subdomínios identificados, melhores serão os serviços resultantes em termos
de estabilidade, coesão e acoplamento. Entretanto, a identificação dos subdomínios pode ser tornar
uma tarefa complexa, pois, também demanda uma alta compreensão do domínio do problema.
Richardson (s.d.) destaca que a estrutura da organização e o modelo de domínio de alto nível, são
bons pontos de partida para a identificação dos subdomínios.
       O uso de DDD em arquiteturas baseada em microsserviços vai além da utilização dos
subdomínios. Outras técnicas são amplamente utilizadas como os Contextos Limitados e os
Relacionamentos entre os mesmo, entretanto, a correta aplicação dessas técnicas só resultam em
benefícios quando se tem um conhecimento profundo das técnicas trazidas por Evans (2003) e do
domínio do problema.

Referências:
        Richardson (s.d.), disponível em:
https://microservices.io/patterns/decomposition/decompose-by-subdomain.html


[PAGINA 26]
                                                                                                26
       3.4.     Descoberta
              3.4.1.   Client-Side Discovery
                                Figura 12 - Padrão Client-Side Discovery.




                                        Fonte: Richardson (s.d.).
Problema:
       Aplicações distribuídas clássicas utilizam um conjunto de host e portas bem conhecidas e,
consequentemente, endereçamento fixo. Já aplicações baseadas em microsserviços costumam ser
executados em ambientes virtualizados ou contêineres, onde, o número de instâncias de um
microsserviço e suas localizações mudam dinamicamente. Como resultado da localização dinâmica,
como o cliente de um serviço - o gateway de API ou outro serviço qualquer - descobre a localização
de uma instância de serviço?

Descrição do Padrão:
        O padrão Client-Side Discovery, define que antes de fazer uma solicitação a um serviço, o
cliente deve obter o local de uma instância do serviço consultando o Service Registry, que conhece
os locais de todas as instâncias de serviço. Após receber a resposta do Service Registry o cliente
possuirá a localização de uma instância disponível do serviço requisitado e poderá continuar com a
solicitação desejada.

Consequência do Uso:
       Com a descoberta do lado do cliente, menos partes móveis (microsserviços) e menos saltos
são necessários para terminar uma solicitação, isso, quando comparando com a descoberta no lado
do servidor. Porém, você precisa implementar a lógica de descoberta de serviço do lado do cliente
para cada linguagem de programação utilizada.

Exemplos de Uso:
       Richardson (s.d.), cita como exemplo, da utilização deste padrão, a utilização dos
componentes do Netflix OSS como o Eureka e o Ribbon que fornece mecanismos para descoberta
de serviços para cliente JVM, em especial aos que utilizam a pilha de tecnologia do Spring, onde, a
descoberta de serviço do lado do cliente é configurada usando várias anotações do Spring Cloud. E


[PAGINA 27]
                                                                                                   27
para os clientes não-JVM, o Netflix Prana fornece uma abordagem baseada em proxy HTTP para a
descoberta de serviço no lado do cliente.
       Netflix OSS, disponível em: h​ ttp://netflix.github.io/
       Eureka, disponível em: ​https://github.com/Netflix/eureka/wiki/Eureka-at-a-glance
       Ribbon, disponível em: ​https://github.com/Netflix/ribbon
       Netflix Prana, disponível em: h​ ttps://github.com/Netflix/Prana

Referências:
      Richardson (s.d.), disponível em: h​ ttps://microservices.io/patterns/client-side-discovery.html

             3.4.2.   Server-Side Discovery
                                Figura 13 - Padrão Server-Side Discovery.




                                        Fonte: Richardson (s.d.).
Problema:
       Aplicações distribuídas clássicas utilizam um conjunto de host e portas bem conhecidas e,
consequentemente, endereçamento fixo. Já aplicações baseadas em microsserviços costumam ser
executados em ambientes virtualizados ou contêineres, onde, o número de instâncias de um
microsserviço e suas localizações mudam dinamicamente. Como resultado da localização dinâmica,
como o cliente de um serviço - o gateway de API ou outro serviço qualquer - descobre a localização
de uma instância de serviço?

Descrição do Padrão:
        O padrão Server-Side Discovery, define que a responsabilidade em realizar a consulta ao
Service Registry e obter a localização de uma instância disponível deve ser do servidor e não do
cliente. Portanto, ao fazer uma solicitação a um serviço, o cliente faz uma solicitação por meio de
um roteador (também conhecido como balanceador de carga) que é executado em um local bem
conhecido. O roteador consulta um Service Registry, que pode ser incorporado ao roteador, e
encaminha a solicitação a uma instância de serviço disponível.

Consequência do Uso:


[PAGINA 28]
                                                                                                   28
        A principal consequência da descoberta no lado do servidor é a simplificação do código do
cliente, pois, o mesmo não precisa se preocupar com nenhum detalhe sobre a descoberta dos
serviços. Porém, cada solicitação acaba tendo vários saltos até ser completada. E, a menos que seja
parte do ambiente de infraestrutura em nuvem, a descoberta no lado do servidor adiciona um
serviço a mais para ser desenvolvido, escalado e monitorado.

Referências:
      Richardson (s.d.), disponível em:​https://microservices.io/patterns/server-side-discovery.html

             3.4.3.   Self-Registration
Problema:
       Após a aplicação de um dos padrões disponivéis para descoberta dos serviços, Descoberta
de Serviço no Lado do Cliente ou Descoberta de Serviço no Lado do Servidor, surge um novo
problema. As instâncias de serviço devem ser registradas, no Service Registry, durante o processo
de inicialização, para que possam ser descobertas e, “des-registradas” durante o processo de
desligamento, para que não sejam solicitadas erroneamente. Além disso, instâncias em execução
mas incapazes de manipular solicitações ou que estejam em falha, devem ter o registro cancelado no
Service Registry. Como as instâncias de serviço devem ser registradas e “des-registradas” no
Service Registry? Quem deve ter a responsabilidade de registrar e “des-registradas” cada instância?

Descrição do Padrão:
        O padrão Self-Registration, define que cada instância de serviço deve ser responsável por se
registrar no Service Registry. Na inicialização, a instância de serviço registra-se informando ao
Service Registry o host através do endereço IP e porta onde estará funcionando o serviço,
tornando-se disponível para a descoberta. Devendo, a mesma, renovar periodicamente seu registro
para que o Service Registry saiba que a instância continua ativa e funcionando corretamente.
        E consequentemente, antes da instância ser completamente desligada a mesma deve solicitar
ao Service Registry o cancelamento do registro, e somente depois da confirmação do cancelamento
a instância deve completar o processo de encerramento.

Consequência do Uso:
        Com a utilização do padrão Self-Registration, é possível implementar um modelo de estados
mais completo do que simplesmente “UP” e “DOWN”, pois, cada instância conhece mais detalhes
sobre seu próprio estado. Exceto nos casos em que uma instância de serviço em execução, fica
incapaz de lidar com solicitações, e geralmente não tem o autoconhecimento para cancelar o
registro do Service Registry.
        Entretanto, a aplicação do Self-Registration produz serviços altamente acoplamento ao
Service Registry, pois, é necessário implementar a lógica de registro para cada serviço e em cada
linguagem de programação utilizada. Richardson (s.d.), destaca que geralmente esses detalhes de
implementação são desenvolvidos utilizando o padrão M  ​ icoservice Chassis​, que permite reutilizar a
lógica de registro para os serviços desenvolvidos com a mesma linguagem de programação. Outros
padrões que podem ser amplamente utilizados nesta situação estão disponíveis na categoria de
Interesses Transversais.


[PAGINA 29]
                                                                                                     29


Referências:
      Richardson (s.d.), disponível em: h​ ttps://microservices.io/patterns/self-registration.html

             3.4.4.    3rd Party Registration
Problema:
       Após a aplicação de um dos padrões disponivéis para descoberta dos serviços, Descoberta
de Serviço no Lado do Cliente ou Descoberta de Serviço no Lado do Servidor, surge um novo
problema. As instâncias de serviço devem ser registradas, no Service Registry, durante o processo
de inicialização, para que possam ser descobertas e, “des-registradas” durante o processo de
desligamento, para que não sejam solicitadas erroneamente. Além disso, instâncias em execução
mas incapazes de manipular solicitações ou que estejam em falha, devem ter o registro cancelado no
Service Registry. Como as instâncias de serviço devem ser registradas e “des-registradas” no
Service Registry? Quem deve ter a responsabilidade de registrar e “des-registradas” cada instância?

Descrição do Padrão:
        O padrão 3rd Party Registration, define que, a responsabilidade em registrar e cancelar o
registro de cada uma das instância de serviço, deve ser de um terceiro serviço, conhecido como
“Registrador”. Um registrador é responsável por registrar cada instância após a inicialização da
mesma e, consequentemente, cancelar o registro de uma instância de serviço que tenha sido
encerrada ou esteja em estado de falha ou indisponível. O registrador realiza as tarefas descritas
através da comunicação com o Service Registry, isso, quando o mesmo não faz parte do próprio
Service Registry.

Consequência do Uso:
        O registro de terceiros implica em códigos de microsserviços menos complexos, isso,
quando comparado ao padrão de auto-registro. Além disso, possibilita ao registrador executar
verificações de integridade em cada uma das instâncias de serviços. Porém, o registrador tem
conhecimento superficial do estado das instâncias, como por exemplo “RUNNING” ou “NOT
RUNNING”. E, a menos que o registrador seja parte da infraestrutura de implantação, é outro
componente para ser desenvolvido, implantado, configurado e mantido. E por ser um componente
crítico do sistema, ele precisa estar altamente disponível.

Exemplos de Uso:
       Richardson (s.d.), cita como exemplo, da utilização deste padrão, os seguintes projetos e
tecnologias:
           ● Netflix Prana: um componente do tipo Sidecar que é anexado aos serviços e fornece
              funcionalidades de registro e descoberta de serviços. Disponível em:
              https://github.com/Netflix/Prana
           ● AWS AutoScaling: um grupo de serviços disponíveis na AWS que fornece
              escalonamento automático da AWS e registram automaticamente as instâncias do
              EC2 com o Elastic Load Balancer. Mais informações disponível em:
              http://aws.amazon.com/autoscaling/


[PAGINA 30]
                                                                                                  30
           ● Joyent's Container: um sistema de inicialização para aplicativos distribuídos nativos
             em nuvem que automatiza o processo de descoberta de serviços, configuração e
             gerenciamento do ciclo de vida dentro do contêiner. Disponível em:
             https://github.com/joyent/containerbuddy
           ● Registrator: um serviço que registrar e cancela automaticamente os registros de
             serviços executando em qualquer container do Docker. Disponível em:
             https://github.com/gliderlabs/registrator
           ● Estruturas de cluster como Kubernetes e Marathon que possuem serviços internos
             para realizar tarefas de registro e cancelamento de instâncias de serviço.
                 ○ Kubernetes disponível em:
                     https://github.com/GoogleCloudPlatform/kubernetes/blob/master/docs/servic
                     es.md
                 ○ Marathon disponível em:
                     https://mesosphere.github.io/marathon/docs/service-discovery-load-balancing
                     .html

Referências:
      Richardson (s.d.), disponível em:​https://microservices.io/patterns/3rd-party-registration.html

       3.5.     Exposição
              3.5.1.   Aggregator Microservice
                                     Figura 14 - Padrão Aggregator.




                                          Fonte: Gupta (2015).
Problema:
        Como consequência da decomposição do sistema em um conjunto de serviços, algumas
operações só são realizadas inteiramente após a realização de consultas em vários serviços.
Portanto, às vezes, para executar uma única tarefa um cliente pode ter que fazer várias chamadas
para vários serviços de back-end. Como o cliente deve se comportar para realizar várias
solicitações? E qual deve ser o tratamento aplicado após o recebimento das várias respostas obtidas?

Descrição do Padrão:
       O padrão Aggregator define uma estratégia de agregação de respostas e pode ser
implementado, basicamente de duas formas. A primeira com o cliente sendo o agregador e
conhecendo os locais dos serviços realizando a comunicação com cada serviço, neste caso, toda a


[PAGINA 31]
                                                                                                 31
lógica de agregação é responsabilidade do cliente, ou seja, o cliente é o próprio agregador. A
segunda forma é desenvolver um serviço específico para realizar o papel de agregador, neste caso,
os clientes não precisam conhecer os locais dos serviços apenas conhecem o serviço agregador, que
é responsável por invocar os serviços e agregar as respostas em um único retorno. (neste segundo
caso existe alguns desacordos, pois, acaba sendo o mesmo que o padrão proxy). O padrão
aggregator é o mais simples, porém, inviável quando possui-se maiores quantidades de serviços,
principalmente, quando utilizado da primeira maneira.

Consequência do Uso:
        Com a utilização do Aggregator o cliente torna-se responsável em realizar várias chamadas
e agregar os resultados, criando-se um forte acoplamento entre os serviços e o cliente. Caso a
localização dos serviços mudem, ou os serviços implantem novas versões o cliente corre o risco de
não funcionar corretamente. Quebrando uma das principais característica da arquitetura , que são
serviços autônomos em relação à implantação, pois, sempre que for necessário implantar uma nova
versão terá que modificar os clientes.
        E mesmo que a agregação passe a ser executada em um serviço específico, todos os
problemas descritos anteriormente continuaram existindo. Além da possibilidade do serviço
agregador acabar se tornando um gargalo na arquitetura e poder introduzir um único ponto de falha.

Referências:
      Gupta (2015), disponível em: h​ ttp://blog.arungupta.me/microservice-design-patterns/

             3.5.2.   Backends For Frontends
                               Figura 15 - Padrão Backends for Frontends.




                                       Fonte: Richardson (s.d.).
Problema:
        Como consequência da decomposição do sistema em um conjunto de serviços, algumas
operações só são realizadas inteiramente após a realização de consultas em vários serviços.
Portanto, às vezes, para executar uma única tarefa um cliente pode ter que fazer várias chamadas
para vários serviços de back-end. Como o cliente deve se comportar para realizar várias
solicitações? E qual deve ser o tratamento aplicado após o recebimento das várias respostas obtidas?


[PAGINA 32]
                                                                                                 32
       Além disso, é muito provável a existência de vários tipos de aplicações cliente (Desktop,
Web, App Móvel, etc), como esses clientes acessam os serviços individuais? Como atender as
necessidades de cada tipo de cliente?

Descrição do Padrão:
        Implemente um gateway de API que seja o único ponto de entrada para cada tipo de cliente.
O padrão backends for frontends é uma variação do API Gateway, seguindo a ideia da Netflix de
respeitar as diferenças entre os dispositivos.

Consequência do Uso:
        A aplicação do padrão Backends for Frontends, assim como o API Gateway, isola os
clientes de como o aplicativo é particionado em microsserviços, remove a complexidade de várias
chamadas no lado do cliente e isola os cliente do problema de determinar os locais das instâncias de
serviços. Entretanto, a complexidade é centralizada em cada tipo de API Gateway tornando um
ponto potencial de falhas, além de adicionar saltos para completar uma solicitação o que aumentar o
tempo de resposta. Sem falar na necessidade de desenvolver um API Gateway para cada tipo de
cliente, o que vai adicionar maior número de componentes a serem gerenciados(desenvolvidos,
implantados, testados, etc).

Referências:
        Docs Microsoft (2017), disponível em:
https://docs.microsoft.com/pt-br/azure/architecture/patterns/backends-for-frontends
        Richardson (s.d.), disponível em: ​https://microservices.io/patterns/apigateway.html

             3.5.3.   Branch Microservice
                                       Figura 16 - Padrão Branch.




                                          Fonte: Gupta (2015).
Problema:
        Como consequência da decomposição do sistema em um conjunto de serviços, algumas
operações só são realizadas inteiramente após a realização de consultas em vários serviços.
Portanto, às vezes, para executar uma única tarefa um cliente pode ter que fazer várias chamadas
para vários serviços de back-end. Como o cliente deve se comportar para realizar várias
solicitações? E qual deve ser o tratamento aplicado após o recebimento das várias respostas obtidas?


[PAGINA 33]
                                                                                                 33


Descrição do Padrão:
       O padrão Branch é uma espécie de junção do padrão Chained com o Aggregator, com a
diferença de que permite o processamento de respostas simultânea de duas cadeias de
microsserviços provavelmente mutuamente exclusivas. A ideia é criar uma espécie de categorização
para as chamadas, e de acordo com a sua categoria a chamada é direcionada para uma das
ramificações de serviços. Uma característica importante é que dentro de uma mesma ramificação os
serviços podem compartilhar recursos como cache e banco de dados.

Consequência do Uso:
        O uso do padrão Branch demonstra ser útil quando é possível identificar categorias de
microsserviços mutuamente exclusivos. Por ter características dos padrões agregador e encadeado,
algumas de suas consequências também serão “herdadas”, como: o “Serviço A”, representado na
Figura 16, passa a ser um ponto central de falhas e um possível gargalo para a arquitetura. Além
disso, dentro de cada ramificação existe uma alta dependência entre os serviços o que resulta em
alta fragilidade.

Referências:
      Gupta (2015), disponível em: h​ ttp://blog.arungupta.me/microservice-design-patterns/

             3.5.4.   Chained Microservice
                                      Figura 17 - Padrão Chained.




                                         Fonte: Gupta (2015).
Problema:
        Como consequência da decomposição do sistema em um conjunto de serviços, algumas
operações só são realizadas inteiramente após a realização de consultas em vários serviços.
Portanto, às vezes, para executar uma única tarefa um cliente pode ter que fazer várias chamadas
para vários serviços de back-end. Como o cliente deve se comportar para realizar várias
solicitações? E qual deve ser o tratamento aplicado após o recebimento das várias respostas obtidas?

Descrição do Padrão:
       O padrão Chained utiliza a comunicação entre os serviços para criar um fluxo de solicitação
e resposta, na maioria das vezes de forma síncrona. Criando-se um encadeamento de serviços
através da comunicação entre cada um, direcionando a responsabilidade de responder a requisição


[PAGINA 34]
                                                                                                 34
ao serviço específico. Um dos serviços acaba sendo o ponto inicial do encadeamento e passa a
requisição para o próximo serviço se necessário. O fluxo de resposta funciona de forma similar,
onde, o serviço responsável em responder a solicitação envia a resposta para o serviço antecessor
até chegar na extremidade do encadeamento e consequentemente ser enviado ao cliente.

Consequência do Uso:
        A grande desvantagem do padrão encadeador é que durante o processo de requisição e
resposta, normalmente, o cliente acaba ficando bloqueado. Para os casos onde existe poucos
serviços essa pode ser uma solução viável, porém, quando o número de serviços começa a aumentar
o tempo de resposta cairá bastante. Sem falar na alta fragilidade existente entre os serviços que
compõem o encadeamento, caso um dos serviços precise ser reimplantado ou entre em estado de
falha, toda o encadeamento será afetado.

Referências:
      Gupta (2015), disponível em: h​ ttp://blog.arungupta.me/microservice-design-patterns/

             3.5.5.   API Gateway
                                    Figura 18 - Padrão API Gateway.




                                       Fonte: Richardson (s.d.).
Problema:
        Como consequência da decomposição do sistema em um conjunto de serviços, algumas
operações só são realizadas inteiramente após a realização de consultas em vários serviços.
Portanto, às vezes, para executar uma única tarefa um cliente pode ter que fazer várias chamadas
para vários serviços de back-end. Como o cliente deve se comportar para realizar várias
solicitações? E qual deve ser o tratamento aplicado após o recebimento das várias respostas obtidas?
        Além disso, é muito provável a existência de vários tipos de aplicações cliente (Desktop,
Web, App Móvel, etc), como esses diversos tipos de clientes acessam os serviços individuais de
maneira uniforme?


[PAGINA 35]
                                                                                              35
Descrição do Padrão:
        O padrão API Gateway, define a implementação de um único ponto de entrada para todos os
clientes. O API Gateway torna-se o serviço responsável em manipular todas as solicitações e
encaminhá-las aos respectivos serviços, expondo uma API pública que reúne todas as
funcionalidades expostas pelos serviços da camada de domínio. Algumas solicitações são
simplesmente intermediadas e roteadas para o serviço apropriado, já outras podem precisar ser
manipuladas a fim de transformar dados ou protocolos de comunicação. Por ser o ponto central na
arquitetura, o API Gateway, também pode implementar verificações de segurança, por exemplo,
verificar se o cliente está autorizado a executar a operação solicitada.
Consequência do Uso:
        A aplicação do padrão API Gateway, isola os clientes de como o aplicativo é particionado
em microsserviços, remove a complexidade de várias chamadas no lado do cliente e isola os cliente
do problema de determinar os locais das instâncias de serviços. Entretanto, a complexidade é
centralizada no API Gateway tornando um ponto potencial de falhas, além de adicionar saltos para
completar uma solicitação o que pode aumentar o tempo de resposta.

Exemplos de Uso:
     API Gateway da Netflix denominado Zuul, disponível em: h​ ttps://github.com/Netflix/zuul
     AWS API Gateway, disponível em: h​ ttps://aws.amazon.com/pt/api-gateway/
     Express Gateway, disponvel em: h​ ttps://www.express-gateway.io/
     Kong, disponível em: ​https://konghq.com/kong/
     Spring Cloud Gateway, disponível em: ​https://spring.io/projects/spring-cloud-gateway

Referências:
      Richardson (s.d.), disponível em: h​ ttps://microservices.io/patterns/apigateway.html

             3.5.6.   Proxy Microservice
                                       Figura 19 - Padrão Proxy.




                                         Fonte: Gupta (2015).
Problema:
       Como consequência da decomposição do sistema em um conjunto de serviços, algumas
operações só são realizadas inteiramente após a realização de consultas em vários serviços.
Portanto, às vezes, para executar uma única tarefa um cliente pode ter que fazer várias chamadas


[PAGINA 36]
                                                                                                  36
para vários serviços de back-end. Como o cliente deve se comportar para realizar várias
solicitações? E qual deve ser o tratamento aplicado após o recebimento das várias respostas obtidas?

Descrição do Padrão:
        O padrão Proxy funciona como uma variação do padrão Aggregator. Porém, neste caso
nenhuma agregação precisa acontecer no cliente, mas um microsserviço passar a ser responsável em
realizar a agregação. Este microsserviço passar a ser um ponto central por onde os cliente
consomem as funcionalidades dos microsserviços de back-end. Existem, basicamente, duas formas
de implementar o padrão Proxy, a primeira onde o serviço de proxy pode é “burro”, ou seja, quando
apenas delega o pedido para um dos microserviços de back-end. E a segunda, onde o serviço de
proxy é “inteligente”, pois, o mesmo realiza algum tipo de manipulação antes da resposta ser
entregue ao cliente. Diversas manipulações podem ser realizadas antes da entrega ao cliente, as
mais comuns são transformação de dados, validações de segurança, etc.

Consequência do Uso:
        Após a aplicação do padrão Proxy obtém-se o seguinte contexto, por ser um ponto
centralizador, o serviço de proxy pode acabar se tornando um gargalo na arquitetura, pois,
representa um único ponto de falha. Em contrapartida: podemos escalar o serviço de proxy de forma
independente; os microsserviços de back-end podem evoluir sem afetarem os clientes; criamos um
ponto central para os consumidores, independente do dispositivo (apps, aplicações web, aplicações
desktop, etc).

Referências:
      Gupta (2015), disponível em: h​ ttp://blog.arungupta.me/microservice-design-patterns/



       3.6.     Interesses Transversais
              3.6.1.   Ambassador
                                    Figura 20 - Padrão Ambassador.




                                        Fonte: Microsoft (2019).
Problema:
        Algumas funcionalidades relacionadas a tolerância a falhas, monitoramento e conectividade
exigem a implementação desses recursos diretamente no serviços. Entretanto, adicionar lógica de
interesses transversais aos serviços, possui grandes desvantagens, como repetição de código, perda
de coesão nos serviços e etc. E mais, se surgir alterações nesses interesses transversais as mudanças
terão que ser realizadas em cada um dos serviços, o que torna inviável de se manter e evoluir.


[PAGINA 37]
                                                                                                  37
        Os problemas descritos tornam-se maiores quando muitas linguagens de programação e
pilhas tecnológicas são utilizadas no desenvolvimento dos serviços, exigindo o desenvolvimento da
mesma lógica para todas as linguagens utilizadas.
        Portanto, como descarregar tarefas comuns de conectividade, tolerância a falhas,
monitoramento, geração de logs... de maneira independente da linguagem utilizada nos serviços,
tornando reutilizável e fácil de manter e evoluir?

Descrição do Padrão:
        O padrão Ambassador define a criação de um serviço autônomo utilizado para auxiliar
tarefas comuns (conectividade, geração de logs, tolerância a falhas e etc), normalmente, realiza as
solicitações de rede em nome de um serviço específico.
        O serviço Ambassador é desenvolvido com todas as tarefas comuns e deve ser implantado
no mesmo ambiente de host do serviço que irá utilizá-lo, entretanto, o mesmo não faz parte o
processo onde roda o serviço consumidor. Ou seja, o Ambassador é co-localizado ao processo do
serviço principal e geralmente é utilizado com sistemas herdados ou outros serviços que não possam
ser facilmente modificados.

Consequência do Uso:
        Após aplicar o padrão Ambassador todas as tarefas comuns passam a estar implementadas
em um único componente que é instanciado várias vezes ao lado dos serviços consumidores. Isso
permite que as funcionalidades possam evoluir de forma autônoma, pois, os serviços conseguem
evoluir suas funcionalidades sem impactar o Ambassador, e quando necessário o Ambassador é
atualizado e implantado sem afetar as funcionalidades dos serviços principais.
        O uso deste padrão tem seus benefícios maximizados quando existem muitos interesses
comuns entre os serviços e muitas linguagens de programação e pilhas tecnológicas são utilizadas,
pois, criando um componente reutilizável economiza-se tempo e esforços de desenvolvimento, além
de habilitar a possibilidade de direcionar o desenvolvimento dos Interesses Transversais a equipes
especializadas.
        Entretanto, a utilização de um processo separado pode incluir latência significativa ao tempo
de solicitação e resposta dos processos. Portanto, em sistemas onde o tempo de resposta seja
requisito crítico outras opções devem ser consideradas.

Referências:
        Docs Microsoft (2017), disponível em:
https://docs.microsoft.com/pt-br/azure/architecture/patterns/ambassador

             3.6.2.   Externalized Configuration
Problema:
       Um aplicativo geralmente usa uma ou mais infraestruturas e serviços de terceiros. Exemplos
de serviços de infraestrutura incluem: um registro de serviço , um intermediário de mensagem e um
servidor de banco de dados. Exemplos de serviços de terceiros incluem: processamento de
pagamentos, email e mensagens, etc. Como habilitar um serviço para ser executado em vários


[PAGINA 38]
                                                                                               38
ambientes sem modificação? Onde as configurações desses serviços devem ser acomodadas, de
forma que permita rápido provisionamento independente da infraestrutura de implantação?

Descrição do Padrão:
       O padrão Externalized Configuration está mais alinhado a um conjunto de boas práticas a
serem seguidas ao utilizar arquitetura baseada em microsserviços. Portanto, externalize todas as
configurações do aplicativo/serviço, incluindo as credenciais do banco de dados, localizações de
rede, dados de acesso de serviços de terceiros e etc. E durante a inicialização, o serviço lê as
configurações de uma fonte externa, por exemplo, variáveis ​de ambiente do sistema operacional.

Consequência do Uso:
        A utilização do padrão Externalized Configuration resulta em um aplicativo que pode ser
executado em vários ambientes sem modificação e /ou recompilação de código, pois, o que
diferenciam os ambientes de execução são as configurações. O único problema é que não existe
garantia de que, quando o aplicativo é implementado, a configuração fornecida corresponda ao
esperado para o ambiente em questão.

Referências:
        Richardson (s.d.), disponível em:
https://microservices.io/patterns/externalized-configuration.html

             3.6.3.   Microservice Chassis
Problema:
        Em uma arquitetura baseada em microsserviços, será freqüentemente necessário criar novos
microsserviços, cada um dos quais podem levar dias ou semanas para ser desenvolvido. Não é
viável passar vários dias configurando mecanismos para lidar com questões transversais, pois,
muitas vezes essas configurações básicas são as mesmas para todos os serviços da infraestrutura.
Portanto, como acelerar o desenvolvimento de novos microsserviços sem perder tempo com
interesses transversais?

Descrição do Padrão:
       De acordo com o padrão Microservice Chassis, deve-se desenvolver um microsserviço
chassi que trate todas as questões transversais necessárias e depois construir seus microsserviços
usando essa estrutura de chassi de microsserviço pré-configurada. O microsserviço chassi passa a
ser uma espécie de projeto base que fornece todas as tarefas comuns devidamente implementadas e
configuradas, permitindo o total redirecionamento de esforços ao desenvolvimento da lógica de
negócio do novo serviço a ser implementado.

Consequência do Uso:
       Após a aplicação do padrão Microservice Chassis o principal benefício obtido é a
capacidade começar a desenvolver um microsserviço de maneira rápida e fácil, sem preocupações
transversais. Porém, você precisará desenvolver um microsserviço chassi para cada linguagem de
programação e pilha tecnológica que deseja utilizar. Em alguns contextos esse tempo de


[PAGINA 39]
                                                                                                  39
desenvolvimento extra pode se tornar um obstáculo para a adoção de novas linguagens de
programação.

Exemplos de Uso:
        Spring Boot para desenvolvedores Java, disponível em: ​http://projects.spring.io/spring-boot/
        Gizmo para desenvolvedores Go, disponível em:
http://open.blogs.nytimes.com/2015/12/17/introducing-gizmo/?_r=2

Referências:
      Richardson (s.d.), disponível em: h​ ttps://microservices.io/patterns/microservice-chassis.html

             3.6.4.   Sidecar
                                       Figura 21 - Padrão Sidecar.




                                        Fonte: Microsoft (2019).
Problema:
        Algumas funcionalidades relacionadas a tolerância a falhas, monitoramento e conectividade
exigem a implementação desses recursos diretamente no serviços. Entretanto, adicionar lógica de
interesses transversais aos serviços, possui grandes desvantagens, como repetição de código, perda
de coesão nos serviços e etc. E mais, se surgir alterações nesses interesses transversais as mudanças
terão que ser realizadas em cada um dos serviços, o que torna inviável de se manter e evoluir.
        Os problemas descritos tornam-se maiores quando muitas linguagens de programação e
pilhas tecnológicas são utilizadas no desenvolvimento dos serviços, exigindo o desenvolvimento da
mesma lógica para todas as linguagens utilizadas.
        Portanto, como descarregar tarefas comuns de conectividade, tolerância a falhas,
monitoramento, geração de logs... de maneira independente da linguagem utilizada nos serviços,
tornando reutilizável e fácil de manter e evoluir?

Descrição do Padrão:
       O padrão Sidecar descreve a implantação de um componente com um conjunto consistente
de funcionalidades de suporte em um processo ou container separado, objetivando fornecer
isolamento e encapsulamento as funcionalidades comuns. O sidecar não faz parte do serviço
principal, mas está anexado ao mesmo e compartilha todo o ciclo de vida do serviço principal.
Entretanto, devido ao isolamento fornecido pela dissociação dos processos ou containers os sidecars
podem ser atualizados de maneira independente sem impactar os serviços principais.


[PAGINA 40]
                                                                                                  40
Consequência do Uso:
        Após aplicar o padrão Sidecar todas as tarefas comuns passam a estar implementadas em um
único componente que é instanciado várias vezes ao lado dos serviços principais, sejam através de
processos próprios ou contêineres separados. Isso permite que as funcionalidades possam evoluir de
forma autônoma, pois, os serviços conseguem evoluir suas funcionalidades sem impactar o Sidecar,
e quando necessário o Sidecar é atualizado e implantado sem afetar as funcionalidades dos serviços
principais.
        Similar ao que acontece com o padrão Ambassador, o padrão Sidecar tem seus benefícios
maximizados quando existem muitos interesses comuns entre os serviços e muitas linguagens de
programação e pilhas tecnológicas são utilizadas, pois, criando um componente reutilizável
economiza-se tempo e esforços de desenvolvimento, além de habilitar a possibilidade de direcionar
o desenvolvimento dos Interesses Transversais a equipes especializadas.
        Entretanto, a utilização de um processo separado pode incluir latência significativa ao tempo
de solicitação e resposta dos processos. Portanto, em sistemas onde o tempo de resposta seja
requisito crítico outras opções devem ser consideradas. Além disso, o padrão Sidecar é mais comum
de ser aplicado quando utiliza-se ambiente de conteinerização como infraestrutura de implantação.

Referências:
        Docs Microsoft (2017), disponível em:
https://docs.microsoft.com/pt-br/azure/architecture/patterns/sidecar

       3.7.     Mensagens Transacionais
              3.7.1.   Polling Publisher
Problema:
       O padrão Polling Publisher surge como consequência da aplicação do padrão Transactional
Outbox. Pois, para ser confiável, cada etapa de uma ​SAGA deve atualizar atômicamente o banco de
dados e publicar mensagens/eventos fornecendo informações sobre a execução da respectiva etapa.
Entretanto, não é viável usar uma única transação distribuída que abranja o banco de dados e o
intermediário de mensagens. Portanto, como publicar mensagens/eventos na caixa de saída no
banco de dados para o intermediário de mensagens de forma confiável?

Descrição do Padrão:
       O padrão Polling Publisher descreve uma maneira de coletar mensagens na caixa de saída
(Outbox) do banco de dados e publicar mensagens/eventos no intermediário de mensagens. O
processo resume-se a pesquisar as mensagens na caixa de saída no banco de dados (Outbox) e para
cada mensagem encontrada deve-se realizar a publicação de uma mensagem/evento no
intermediário de mensagens e logo após excluir a mensagem publicada da caixa de saída (Outbox).
Dessa forma, todas as mensagens persistidas na caixa de mensagem do banco de dados serão
publicadas no intermediário de mensagens.

Consequência do Uso:
      A correta aplicação do Polling Publisher resulta em um mecanismo eficiente de publicação
de mensagens/eventos, pois, para cada mensagem persistida no banco de dados será publicado uma


[PAGINA 41]
                                                                                                41
mensagem/evento no intermediário de mensagem. Entretanto, a aplicação do padrão é restrita a
banco de dados SQL. Infelizmente, nem todos bancos NoSQL suportam a aplicação do Polling
Publisher. Além disso, é difícil garantir que a publicação dos eventos ocorra em ordem e o alto
nível de acesso ao banco de dados pode impactar na performance do sistema.

Exemplos de Uso:
     Eventuate Tram Framework, disponível em:
     https://github.com/eventuate-tram/eventuate-tram-core

Referências:
        Richardson (s.d.), disponível em:
https://microservices.io/patterns/data/polling-publisher.html

             3.7.2.   Transactional Outbox
                                  Figura 22 - Padrão Transaction Outbox.




                                         Fonte: Richardson (s.d.).
Problema:
        Após aplicar o padrão ​SAGA​, normalmente, um serviço precisa atualizar atômicamente o
banco de dados e publicar mensagens/eventos fornecendo informações sobre a execução da
respectiva etapa. Entretanto, não é viável usar uma única transação distribuída que abranja o banco
de dados e o intermediário de mensagens para atualizar atômicamente o banco de dados e publicar
mensagens/eventos. Portanto, como atualizar de forma confiável e atômica o banco de dados e
ainda publicar mensagens/eventos no intermediário de mensagens?

Descrição do Padrão:
       O padrão Transactional Outbox define a criação de uma caixa de saída (Outbox) dentro do
banco de dados com o objetivo de armazenar as mensagens que devem ser publicadas no
intermediário de mensagens. E através de um serviço de Message Relay as mensagens são
publicadas no intermediário e removidas do banco de dados.
       Para um serviço que usa um banco de dados relacional, deve-se criar uma tabela (por
exemplo MESSAGE) que represente a caixa de saída das mensagens e durante as etapas das
operações inserir as mensagens na caixa de saída como parte da transação local. O mesmo deve ser
implementado para os serviços que usam banco de dados NoSQL, porém, pela flexibilidade a caixa
de saída pode ser composta por informações (mensagens/eventos) anexadas aos atributos do registro
(por exemplo, documento ou item) que está sendo atualizado. Dessa forma todas as mensagens que
precisam ser publicadas no intermediário estarão salvas em uma base de dados.


[PAGINA 42]
                                                                                               42


Consequência do Uso:
        Após a aplicação do Transactional Outbox, todas as mensagens, que precisam ser publicadas
no intermediário, estarão salvas em uma base de dados. Como consequência, um novo serviço
precisará ser implementado, o Message Relay. Para a implementação do Message Relay existem
                                                 ​ olling Publisher​ ou ​Transaction Log Tailing​.
basicamente duas abordagens a serem aplicadas: o P
        Além disso, a utilização do padrão torna-se potencialmente propensa a erros, pois, os
desenvolvedores podem facilmente esquecer de publicar a mensagem/evento após atualizar o banco
de dados. Porém, quando bem utilizado o Transactional Outbox consegue fornecer mecanismos de
implementação de eventos de domínio de alto nível.

Referências:
        Richardson (s.d.), disponível em:
https://microservices.io/patterns/data/transactional-outbox.html

             3.7.3.   Transaction Log Tailing
                                Figura 23 - Padrão Transaction Log Tailing.




                                         Fonte: Richardson (s.d.).
Problema:
       O padrão Transaction Log Tailing surge como consequência da aplicação do padrão
Transactional Outbox. Pois, para ser confiável, cada etapa de uma S      ​ AGA deve atualizar
atômicamente o banco de dados e publicar mensagens/eventos fornecendo informações sobre a
execução da respectiva etapa. Entretanto, não é viável usar uma única transação distribuída que
abranja o banco de dados e o intermediário de mensagens. Portanto, como publicar
mensagens/eventos na caixa de saída no banco de dados para o intermediário de mensagens de
forma confiável?

Descrição do Padrão:
       O padrão Transaction Log Tailing utiliza-se dos recursos de logs fornecidos pelos banco de
dados como “gatilhos” para publicar mensagens/eventos no intermediário de mensagem. Para tanto,


[PAGINA 43]
                                                                                                43
é preciso que o banco de dados forneça tais funcionalidades, permitindo o ativamento dos logs de
transações. Quando fornecido, os logs das transações informam quais mensagens foram inseridas na
caixa de saída (Outbox) do banco de dados permitindo que, para cada mensagem inserida, sejam
publicadas mensagem/evento no intermediário de mensagens.

Consequência do Uso:
       A correta aplicação do Transaction Log Tailing resulta em um mecanismo eficiente de
publicação de mensagens/eventos, pois, os logs de transações dos bancos de dados fornecem de
uma forma mais segura a garantia de que para cada mensagem persistida no banco de dados será
publicado uma mensagem/evento no intermediário de mensagem.
       Entretanto, é difícil impedir que ocorra publicações duplicadas. Além disso, a aplicação do
padrão depende do mecanismo utilizado para rastrear os logs das transações e, consequentemente,
cada banco de dados possui seus próprios mecanismos. Resultando em diferentes formas de
implementar o padrão.

Exemplos de Uso:
     Eventuate Tram Framework, disponível em:
     https://github.com/eventuate-tram/eventuate-tram-core

Referências:
        Richardson (s.d.), disponível em:
https://microservices.io/patterns/data/polling-publisher.html

       3.8.     Migração
              3.8.1.   Anti-Corruption Layer
                                Figura 24 - Padrão Anti-Corruption Layer.




                                        Fonte: Microsoft (2019).
Problema:
       Durante um processo de migração, entre um sistema legado o seu substituto moderno, é
comum a necessidade de manter em funcionamento ambos os sistemas. Algumas funcionalidades
terão que utilizar serviços de ambos os sistemas, porém, os protocolos de comunicação e os tipos de
dados que os sistemas manipulam são diferentes entre si. O mesmo contexto pode acontecer com
sistemas ou serviços externos que a organização utilize e que não seja controlada pela mesma.


[PAGINA 44]
                                                                                               44
        Portanto, como integrar ambos os sistemas de forma a garantir que a a troca de informações
entre eles sejam realizadas com sucesso? E como proteger o sistema moderno para não acoplar-se
indevidamente ao sistema legado?

Descrição do Padrão:
        O padrão Anti-Corruption Layer define a criação de uma camada intermediária entre os
sistemas. Internamente a camada possuir toda a lógica necessária para permitir a comunicação entre
os diferentes sistemas, realizando todas as transformações necessárias como traduções de
protocolos, transformação de dados e etc.
        A função da camada é isolar os sistemas e permitir que o sistema legado permaneça
inalterado e o sistema moderno não se corrompa tentando adequar-se ao sistema legado.

Consequência do Uso:
        Após a aplicação da Anti-Corruption Layer diferentes sistemas poderam comunicar-se,
permitindo troca de informações e uso de serviços entre ambos. Se o padrão foi aplicado devido a
um processo de migração, a camada poderá ser totalmente removida após a finalização do processo.
E se necessário, a camada poderá ser parte do sistema final sem comprometer o funcionamento do
respectivo sistema.
        Entretanto, funcionalidades que precisem passar pela camada de anti-corrupção terão o
tempo de execução um pouco maior, devido a latência adicionada às chamadas. Além disso, a
camada passa a ser um outro componente dentro da arquitetura que deve ser desenvolvido,
implantado e mantido. Portanto, é importante analisar se os benefícios em implementar o padrão
realmente superam os custos, e se necessário providenciar outra estratégia.

Referências:
        Docs Microsoft (2017), disponível em:
https://docs.microsoft.com/pt-br/azure/architecture/patterns/anti-corruption-layer

             3.8.2.   Strangler
                                      Figura 25 - Padrão Strangler.




                                        Fonte: Microsoft (2019).
Problema:
        Durante um processo de migração, entre um sistema legado o seu substituto moderno, é
comum a necessidade de manter em funcionamento ambos os sistemas. Devido a inviabilidade, uma
substituição completa do sistema legado encontra-se fora de questão. Além disso, algumas
funcionalidades terão que utilizar serviços de ambos os sistemas.


[PAGINA 45]
                                                                                               45
        Portanto, como habilitar um processo de migração incremental de forma que possam ser
utilizados os recursos já implementados no sistema novo? E como integrar ambos os sistemas de
forma a permitir que solicitações à recursos antigos, sejam devidamente direcionadas ao sistema
legado?

Descrição do Padrão:
        O Padrão Strangler define a criação de uma fachada responsável em interceptar todas as
solicitações e realizar o devido encaminhamento aos respectivos sistemas. Dessa forma, os recursos
que já tiverem sidos implementados no sistema novo poderão ser utilizados, e solicitações as
funcionalidades que ainda estiverem em fase de desenvolvimento serão direcionadas ao sistema
legado.
        É importante que a interface definida na fachada seja o mais proxima, senão idêntica, da
interface projetada para o sistema moderno final. O uso do Strangle reduz o risco da migração e
distribui o esforço de desenvolvimento ao longo do tempo.

Consequência do Uso:
        Após aplicar o padrão Strangler será possível desenvolver um processo de migração com
menos risco e de forma incremental. O esforço de uma migração completa será distribuído durante
um longo período de tempo, permitindo que novas funcionalidades possam ser implantadas o mais
rápido possível. Além disso, os consumidores do sistema terão o mínimo de impacto e continuaram
utilizando o sistema normalmente.
        A fachada do Strangler poderá ser completamente removida após o processo de migração
com o mínimo de impacto ao sistema final. Entretanto, alguns custos são adicionados ao utilizar-se
do Strangler. Por exemplo, a fachada criada pode torna-se um ponto único de falha ou gargalo de
desempenho. Além disso, sempre que novas funcionalidades forem implantadas o Strangler terá que
ser devidamente atualizado.

Referências:
        Docs Microsoft (2017), disponível em:
https://docs.microsoft.com/pt-br/azure/architecture/patterns/strangler

       3.9.     Monitoramento
              3.9.1.   Application Metrics
                                 Figura 26 - Padrão Application Metrics.




                                    Fonte: Richardson (2019, p.365).
Problema:


[PAGINA 46]
                                                                                              46
        A responsabilidade em produzir software não encerra-se ao fim do processo de
desenvolvimento. Logo após implantar o sistema em produção um ponto muito importante é
conhecer a saúde do sistema em funcionamento, pois, permite que os problemas sejam facilmente
resolvidos e em alguns casos evitados. Isso é feito através da correta coleta de métricas e
informações críticas sobre a aplicação em funcionamento. Portanto, como obter informações sobre
o sistema em produção? E qual a melhor forma de observar o comportamento do sistema em
produção permitindo solucionar os problemas identificados?

Descrição do Padrão:
         O padrão Application Metrics define o desenvolvimento de um serviço para reunir
estatísticas sobre operações individuais do sistema em produção. Este serviço deverá realizar a
agregação das métricas de forma centralizadas, além de fornecer relatórios e emissão de alertas.
Existem dois modelos utilizados para realizar a agregação das métricas, o primeiro denominado
“push” descreve que os serviços em funcionamento deverão enviar as métricas para o serviço de
métricas periodicamente. E o segundo modelo é denominado “pull”, que direciona a
responsabilidade de coletar as métricas dos serviços em funcionamento ao próprio serviço de
métricas, tarefa essa realizada através de um processo chamado extração de métricas dos serviço.

Consequência do Uso:
       Após aplicar o padrão Application Metrics será possível obter ótimas informações sobre o
sistema em funcionamento, pois, o mesmo consegue fornecer uma visão profunda sobre o
comportamento do aplicativo. Em contrapartida, quando o modelo push é aplicado resulta em um
forte entrelaçamento entre a lógica de negócio do serviço e o código de extração de métricas
tornando o serviço mais complicado de desenvolver e evoluir. Além disso, a aplicação do padrão de
poderá exigir um certo investimento em infraestrutura, já que o serviço de métricas será mais um
componente a ser desenvolvido, implantado e mantido.

Exemplos de Uso:
     Bibliotecas de Instrumentação:
         ● Coda Hale/Yammer Java Metrics Library, disponível em:
            http://metrics.dropwizard.io/3.1.0/
         ● Prometheus Client Libraries, disponível em:
            https://prometheus.io/docs/instrumenting/clientlibs/
     Serviços de Agregação de Métricas:
         ● Prometheus, disponível em: ​https://prometheus.io/docs/introduction/overview/
         ● AWS Cloud Watch, disponível em: h​ ttps://aws.amazon.com/cloudwatch/

Referências:
        Richardson (s.d.), disponível em:
https://microservices.io/patterns/observability/application-metrics.html

             3.9.2.   Audit Logging
                                    Figura 27 - Padrão Audit Logging.


[PAGINA 47]
                                                                                                 47




                                    Fonte: Richardson (2019, p.365).
Problema:
        A responsabilidade em produzir software não encerra-se ao fim do processo de
desenvolvimento. Logo após implantar o sistema em produção um ponto muito importante é
conhecer a saúde do sistema em funcionamento, pois, permite que os problemas sejam facilmente
resolvidos e em alguns casos evitados. Além disso, realizar suporte aos clientes pode se torna uma
tarefa muito difícil, pois, não sabemos ao certo quais funcionalidades do sistema o usuário utilizou
durante suas últimas interações.
         Portanto, como obter informações relevantes sobre o sistema em produção? E qual a
melhor forma de entender, não só o comportamento do sistema em produção, mas também o
comportamento dos usuários permitindo solucionar os problemas identificados?

Descrição do Padrão:
        O padrão Audit Logging descreve a implementação de um serviço responsável em
armazenar os registros de atividade dos usuário em um banco de dados. Onde cada entrada de
registro deve conter obrigatoriamente a identificação do usuário, a ação executada pelo usuário e os
objetos de negócios manipulados durante as operações realizadas.
        Existem basicamente três formas de implementar o padrão Audit Logging, a primeira é
adicionando a lógica de auditoria diretamente na camada de lógica de negócios dos serviços. A
segunda é utilizando a programação orientada a aspectos. E por fim, a terceira maneira é utilizar a
programação baseada em eventos.

Consequência do Uso:
        Após aplicar o padrão Audit Logging será possível obter informações personalizadas sobre
as ações de cada usuário do sistema, permitindo melhores estratégias de suporte ao cliente. Além
disso, com base nas informações coletadas tarefas como garantia de conformidade dos serviços e
detecção de usuários suspeitos serão mais fáceis de serem realizadas. Entretanto, dependendo da
estratégia utilizada para implementar a lógica de auditoria, o código de auditoría poderá fica
entrelaçado com a lógica de negócios, o que torna a lógica de negócio mais complicada e o serviço
mais difícil de manter e evoluir.

Exemplos de Uso:


[PAGINA 48]
                                                                                                  48


Referências:
        Richardson (s.d.), disponível em:
https://microservices.io/patterns/observability/audit-logging.html

             3.9.3.   Distributed Tracing
                                  Figura 28 - Padrão Distributed Tracing.




                                     Fonte: Richardson (2019, p.365).
Problema:
        A responsabilidade em produzir software não encerra-se ao fim do processo de
desenvolvimento. Logo após implantar o sistema em produção um ponto muito importante é
conhecer a saúde do sistema em funcionamento, pois, permite que os problemas sejam facilmente
resolvidos e em alguns casos evitados.
        Entretanto, sistema desenvolvidos com arquitetura baseada em microsserviços consistem em
um conjunto de instâncias de serviço que estão sendo executados em vários processos/máquinas
distintos. E cada solicitação, geralmente, abrangem várias instâncias de serviço, exigindo que cada
serviço lide com a solicitação executando uma ou mais operações, e invocando outros serviços
quando necessário.
         Portanto, como obter informações úteis sobre o sistema em produção? E qual a melhor
estratégia para observar o comportamento do sistema, já que as operações são resolvidas por vários
serviços e os logs das operações estão distribuídos em vários locais? Como identificar os logs
pertencente a mesma solicitação?

Descrição do Padrão:
        O padrão Distributed Tracing descreve uma estratégia para rastrear as solicitações e
consequentemente os logs das operações necessárias para completar cada solicitação. A aplicação
do Distributed Tracing define a adição das seguintes informações em cada solicitação recebida:
primeiro atribua a cada solicitação externa um identificador - ID - de solicitação externa exclusivo;
segundo, passe o ID da solicitação externa para todos os serviços envolvidos no tratamento da
solicitação; terceiro, inclua o ID da solicitação externa em todas as mensagens de log realizadas;
quarto, registre informações adicionais como, hora de início e hora de término, para cada solicitação
e operação realizada ao manipular uma solicitação externa em um serviço centralizado.


[PAGINA 49]
                                                                                                   49
Consequência do Uso:
       Após aplicar o padrão Distributed Tracing será possível obter informações úteis sobre o
comportamento do sistema, incluindo as fontes de latência. Além disso, permite que os
desenvolvedores vejam como uma solicitação individual é gerenciada durante o ciclo de vida da
mesma. Isso é feito pesquisando em logs de agregação seu ID de solicitação externa ou utilizando
ferramentas específicas para apresentação gráfica de rastreamento distribuído. Entretanto, agregar e
armazenar todos os dados de rastreamento pode exigir infraestrutura significativa, além de adicionar
mais um componente a arquitetura que deverá ser devidamente desenvolvido, implantado e
mantido.

Exemplos de Uso:
         Zipkin: serviço para gravação e exibição de informações de rastreamento. Disponível em:
http://zipkin.io/
         Open Tracing: API padronizada para rastreamento distribuído. Disponível em:
http://opentracing.io/

Referências:
        Richardson (s.d.), disponível em:
https://microservices.io/patterns/observability/distributed-tracing.html

             3.9.4.    Exception Tracking
                                  Figura 29 - Padrão Exception Tracking.




                                     Fonte: Richardson (2019, p.365).
Problema:
        A responsabilidade em produzir software não encerra-se ao fim do processo de
desenvolvimento. Logo após implantar o sistema em produção um ponto muito importante é
conhecer a saúde do sistema em funcionamento, pois, permite que os problemas sejam facilmente
resolvidos e em alguns casos evitados.
        Entretanto, sistema desenvolvidos com arquitetura baseada em microsserviços consistem em
um conjunto de instâncias de serviço que estão sendo executados em vários processos/máquinas
distintos. E cada solicitação, geralmente, abrangem várias instâncias de serviço, exigindo que cada
serviço lide com a solicitação executando uma ou mais operações, e invocando outros serviços
quando necessário. Além disso, durante a resolução de algumas solicitações erros podem acontecer


[PAGINA 50]
                                                                                                 50
e quando ocorre um erro a instância de serviço lança uma exceção, que contém uma mensagem de
erro e um rastreamento de pilha.
         Portanto, como obter informações úteis sobre as exceções que ocorrem no sistema em
produção? E qual a melhor estratégia para rastrear as exceções ocorridas durante a manipulação das
solicitações, e identificar quais foram resolvidas e quais não foram?

Descrição do Padrão:
        O padrão Exception Tracking descreve a implementação de um serviço centralizador de
exceções, responsável em armazenar todas as exceções relatadas pelos serviços, e realizar tarefas de
agregação, desduplicação de exceção e rastreamento de exceções. Além de fornecer mecanismos de
alertas e notificações aos desenvolvedores.

Consequência do Uso:
       Após aplicar o padrão Exception Tracking será possível obter informações úteis sobre a
ocorrência de exceções, além de permitir uma completa visualização e acompanhamento das
exceções resolvidas e não resolvidas. Porém, a aplicação do padrão prevê a implementação de um
serviço exclusivo para o registro de exceções o que implica em um investimento em infra-estrutura
adicional, pois, o serviço de rastreamento de exceções passa a ser mais um serviço para ser
desenvolvido, implantado, testado e mantido.

Exemplos de Uso:
     Honeybadger: serviço baseado em nuvem. Disponível em: h​ ttps://www.honeybadger.io
     Sentry.io: projeto open source. Disponível em: h​ ttps://sentry.io/welcome/

Referências:
        Richardson (s.d.), disponível em:
https://microservices.io/patterns/observability/exception-tracking.html

             3.9.5.   Health Check API
                                  Figura 30 - Padrão Health Check API.




                                    Fonte: Richardson (2019, p.365).
Problema:
      A responsabilidade em produzir software não encerra-se ao fim do processo de
desenvolvimento. Logo após implantar o sistema em produção um ponto muito importante é


[PAGINA 51]
                                                                                                  51
conhecer a saúde do sistema em funcionamento, pois, permite que os problemas sejam facilmente
resolvidos e em alguns casos evitados.
        Entretanto, sistema desenvolvidos com arquitetura baseada em microsserviços consistem em
um conjunto de instâncias de serviço que estão sendo executados em vários processos/máquinas
distintos. E às vezes, uma instância de serviço pode tornar-se incapaz de manipular solicitações e
ainda estar em execução. Por exemplo, a instância pode ter ficado sem conexão com o banco de
dados. O sistema de monitoramento deve ser capaz de identificar esses tipos de situações e deve
gerar algum tipo de alerta.
         Portanto, como obter informações úteis sobre o sistema em produção? E qual a melhor
estratégia para observar o comportamento das instâncias de serviço em execução? Como obter
detalhes do funcionamento interno de cada instância? E como identificar se as instâncias são
capazes ou não de lidar com solicitações?

Descrição do Padrão:
        O padrão Health Check API descreve o desenvolvimento, em cada serviço, de um ponto de
extremidade da API para ser utilizado como verificação de integridade (‘/health’, por exemplo). O
retorno do endpoint deve conter informações sobre a integridade e o funcionamento da instância de
serviço. Internamente, as verificações que devem ser feitas por cada instância de serviço e logo após
retornadas são: o status das conexões para os serviços de infraestrutura usados ​pela instância de
serviço; o status do host contendo informações como consumo de cpu, memória, espaço em disco e
etc; além de informações sobre o status da lógica específica da aplicação. Com isso, um cliente de
verificação de integridade como um serviço de monitoramento, serviço de registro ou balanceador
de carga poderá chamar periódicamente o endpoint definido e extrair informações de integridade da
instância de serviço.

Consequência do Uso:
        Após a aplicação do padrão Health Check API será possível obter informações úteis sobre o
estado operacional de cada instância de serviço, além de habilitar a execução de consultas
periódicas por agentes externos como serviços de tolerância a falhas. Além disso, as informações
relatadas pelo padrão Health Check API costumam ser mais precisas e com mais detalhes, pois,
ninguém melhor que a própria instância para reportar seu estado operacional.
        Entretanto, a verificação de integridade, feita pela própria instância, pode não ser
suficientemente abrangente ou a instância de serviço pode entrar em estado de falha e não conseguir
informar o real estado em que se encontra.

Referências:
        Richardson (s.d.), disponível em:
https://microservices.io/patterns/observability/health-check-api.html

             3.9.6.   Log Aggregation
                                   Figura 31 - Padrão Log Aggregation.


[PAGINA 52]
                                                                                                 52




                                    Fonte: Richardson (2019, p.365).
Problema:
        A responsabilidade em produzir software não encerra-se ao fim do processo de
desenvolvimento. Logo após implantar o sistema em produção um ponto muito importante é
conhecer a saúde do sistema em funcionamento, pois, permite que os problemas sejam facilmente
resolvidos e em alguns casos evitados.
        Entretanto, sistema desenvolvidos com arquitetura baseada em microsserviços consistem em
um conjunto de instâncias de serviço que estão sendo executados em vários processos/máquinas
distintos. Além disso, cada instância de serviço gera informações sobre o que está fazendo em um
arquivo de log em um formato padronizado. O arquivo de log contém erros, avisos, informações e
mensagens de depuração.
        Portanto, como obter informações sobre o sistema em produção? Qual a melhor forma de
armazenar os arquivos de log das instâncias? E qual a melhor forma de observar os diversos
arquivos de logs gerados pelas instâncias de serviços?

Descrição do Padrão:
         O padrão Log Aggregation descreve a implementação de um serviço centralizador de log,
que agrega os diversos arquivos de logs de cada instância de serviço e fornece mecanismos de
pesquisa e análise dos logs coletados. Para cada instância de serviço reúna os arquivos de logs e os
armazene de forma padronizada em uma base de dados, com isso, será possível utilizar ferramentas
de apresentação graficas para realizar tarefas de pesquisa e análise dos dados armazenados. Além
disso, com o uso do Log Aggregation algumas configurações para emissão de alertas podem ser
feitas e serem acionadas quando certas mensagens aparecem nos registros.

Consequência do Uso:
        Após a aplicação do padrão Log Aggregation será possível obter informações úteis sobre as
tarefas executadas por cada instância de serviço, além de habilitar a capacidade de monitorar em
tempo real o estado e o comportamento de todo o sistema em produção. Entretanto, a aplicação do
padrão Log Aggregation exige um certo investimento em infra-estrutura, pois, conforme o tempo
maior será o volume de dados de logs que serão necessários armazenar e manipular.


[PAGINA 53]
                                                                                              53


Exemplos de Uso:
        AWS Cloud Watch, disponível em: ​https://aws.amazon.com/cloudwatch/
        ELK Stack, disponível em: ​https://www.elastic.co/pt/what-is/elk-stack
Referências:
        Richardson (s.d.), disponível em:
https://microservices.io/patterns/observability/application-logging.html

      3.10.      Tolerância a Falhas
              3.10.1.   Bulkhead
                                       Figura 32 - Padrão Bulkhead.




                                         Fonte: Microsoft (2019).
Problema:
       Em um sistema de arquitetura baseada em microsserviços as funcionalidades fornecidas pelo
sistema estão distribuídas entre várias instâncias de serviço. Uma instância afetada por carga
excessiva, devido ao alto número de solicitações realizadas por um mesmo consumidor, pode ter
seus recursos completamente esgotado. Além disso, uma instância de serviço que esteja em estado
de falha, poderá afetar todos os consumidores do serviço e, em um nível mais alarmante, até mesmo
consumidores de outros serviços, causando um efeito de falha em cascata.
       Portanto, como impedir que erros e sobrecarga causados por um consumidor afete os demais
consumidores? E como evitar a ocorrência de falhas em cascata?

Descrição do Padrão:
        O padrão Bulkhead define o particionamento das instâncias de serviços em um conjunto de
diferentes grupos. E para realizar o particionamento e a definição dos grupos devem ser
considerados a carga de consumidores do serviços e os requisitos de disponibilidade do sistema. A
mesma abordagem pode ser aplicado no lado dos consumidores, principalmente, os consumidores
que precisam chamar vários serviços. Neste caso definir um pool de conexão para cada serviço
permite que a ocorrência de uma falha na chamada em um dos serviços não afete os demais.

Consequência do Uso:


[PAGINA 54]
                                                                                                 54
        Após a aplicação do padrão Bulkhead existirá um isolamento entre os consumidores e os
serviços evitando a ocorrência de falhas em cascata. Além disso, caso ocorra alguma falha em um
dos grupos do particionamento apenas aquele grupo poderá ser afetado, os outros grupos de
serviços continuarão funcionando normalmente.
        Outro benefício em aplicar o Bulkhead é que ele permite a construção de grupos de serviços
com diferentes níveis de disponibilidade. Dessa forma é possível oferecer diferentes tipos de planos
de serviços aos clientes do sistema.
        Entretanto, o padrão exige um certo nível de sobrecarga em termos de custos, desempenho e
capacidade de gerenciamento, pois, cada grupo de instâncias funcionará como um sistema
independente.

Referências:
        Docs Microsoft (2017), disponível em:
https://docs.microsoft.com/pt-br/azure/architecture/patterns/bulkhead

           3.10.2.    Circuit Breaker
                                   Figura 33 - Padrão Circuit Breaker




                                        Fonte: Microsoft (2019).
Problema:
       As funcionalidades fornecidas por um sistema, que possui uma arquitetura baseada em
microsserviços, estão distribuídas entre várias instâncias de serviço. E normalmente, grande parte
das operações dos consumidores envolve várias instâncias de serviço. Exigindo que os serviços
colaborem entre si para conseguirem concluir com sucesso as solicitações dos consumidores.
       Entretanto, por utilizar a comunicação em rede, é comum que ocorram falhas durante o
processo de comunicação e troca de informações entre os serviços. Em alguns casos a lentidão pode
ser o motivo por trás de algumas falhas, já em outros, pode significar que a instância de serviço
encontra-se temporariamente indisponível. Neste segundo caso, permitir o encaminhamento de
novas solicitações pode agravar ainda mais a situação da instância, podendo ocasionar um
esgotamento completo dos seus recursos. Além disso, uma instância de serviço que esteja em estado


[PAGINA 55]
                                                                                                  55
de falha, poderá afetar todos os consumidores do serviço e, em um nível mais alarmante, até mesmo
consumidores de outros serviços, causando um efeito de falha em cascata.
        Portanto, como detectar que uma instância de serviço em execução é incapaz de lidar com
solicitaçõe? Como isolar temporariamente uma instância em estado de falhar, para que a mesma
tenha tempo de se recuperar? E como evitar a ocorrência de falhas em cascata?

Descrição do Padrão:
        O padrão Circuit Breaker define um conjunto de estratégias utilizadas para tornar uma
arquitetura distribuída o mais resiliente possível. O mesmo especifica a utilização de um
componente responsável em habilitar/desabilitar o encaminhamento de solicitações em cada
instância de serviço. Este componente funciona como uma máquina de estados que controla a
passagem de solicitações ao serviço ao qual está anexado. Realizando o rastreador da quantidade de
solicitações bem sucedidas e com falhas, e calculando uma taxa de erro. Quando a taxa excede um
limite predefinido o Circuit Breaker passa para o estado 'aberto' e após um período de tempo seu
estado é atualizado. Basicamente, o componente possui três estados possíveis, são eles:
        1. Fechado: as solicitações são encaminhadas normalmente aos serviços. Cada solicitação e
monitorada a fim de obter status da operação e incrementar a respectiva contagem (solicitações bem
sucedidas e com falhas). Ambas as contagens são utilizadas para determinar o acionamento do
Circuit Breaker e caso necessário seu estado será atualizado para 'Aberto'. No momento que entra
em estado 'Aberto', inicia-se um temporizador e ao expirar o estado é atualizado para 'Semi-aberto'.
        2. Aberto: às solicitações são imediatamente canceladas e uma exceção é retornada. Neste
estado, a instância de serviço encontra-se isolada e inacessível aos consumidores.
        3. Semi-aberto: apenas uma pequena quantidade de solicitações são encaminhadas ao
serviço. Se as solicitações forem bem sucedidas , considera-se que o problema foi resolvido e o
Circuit Breaker tem seu estado atualizado para 'Fechado' (as contagens são resetadas assim como os
temporizadores). E se alguma solicitação falhar, considera-se que a instância ainda está indisponível
e o Circuit Breaker voltará para o estado 'Aberto' reiniciando o temporizador e permitindo que a
instância consiga se recuperar.

Consequência do Uso:
        Após a aplicação do padrão Circuit Breaker os serviços passarão a contar com um
intermediador que acrescentará maior estabilidade e resiliência a todo o sistema. Além de evitar a
ocorrência de falhas em cascata, a aplicação do padrão, evitará que solicitações com alta
possibilidade de falha sejam encaminhadas a instâncias de serviços em recuperação.
        Entretanto, é necessário que os serviços estejam preparados para lidar com as possíveis
exceções lançadas pelo Circuit Breaker, com isso, aumenta-se a complexidade no desenvolvimento
dos serviços. Além disso, quando não desenvolvido em um componente independente, a aplicação
do Circuit Breaker pode exigir o desenvolvimento do componente para cada linguagem de
programação utilizada no desenvolvimento dos serviços. Uma maneira de resolver esse desafio é
aplicar um dos padrões de ​Interesses Transversais e desenvolver o Circuit Breaker com um
componente independente e reutilizável.

Exemplos de Uso:
     Hystrix, disponível em: h​ ttps://github.com/Netflix/Hystrix


[PAGINA 56]
                                                                                                56


Referências:
        Docs Microsoft (2017), disponível em:
https://docs.microsoft.com/pt-br/azure/architecture/patterns/circuit-breaker
        Richardson (s.d.), disponível em:
https://microservices.io/patterns/reliability/circuit-breaker.html

            3.10.3.   Tolerant Reader
Problema:
       Em um sistema de arquitetura baseada em microsserviços as funcionalidades fornecidas pelo
sistema estão distribuídas entre várias instâncias de serviço. As operações dos consumidores,
geralmente, envolve várias instâncias de serviço. Exigindo que os serviços colaborem entre si para
conseguirem concluir com sucesso as solicitações dos consumidores.
       Os serviços conseguem comunicar-se entre si por meio de suas interfaces - API. Entretanto,
quando os serviços conhecem as interfaces uns dos outros acaba-se gerando um certo nível de
acoplamento, e em alguns casos, muitas equipes tornam esse acoplamento maior do que deveria ser.
       Portanto, em um ambiente de colaboração entre serviços, como manter o nível de
acoplamento aceitável de modo que permita a evolução dos serviços com o mínimo de impacto aos
seus consumidores?

Descrição do Padrão:
        O padrão Tolerant Reader especifica o comportamento dos serviços que colaboram entre si,
inclusive os consumidores. Todos devem ser conservadores nas tarefas que fazem, entretanto,devem
ser liberais no que aceitam dos outros serviços. Isso significa, que ao invocar funcionalidades dos
outros serviços deve-se usar apenas os elementos necessários para executar a lógica do serviço e o
restante dos elementos devem ser completamente ignorados.
        Além disso, ao receber a resposta de um serviço, o mínimo de suposições sobre a estrutura
da resposta deve ser feito. Por exemplo, sistemas que utilizam XML para a troca de informações
podem utilizar consultas XPath para extrair as propriedades desejadas das cargas úteis, e o mesmo
princípio deve ser aplicado para outros tipos de dados possíveis. Dessa forma, permite-se que os
serviços evoluam suas funcionalidades e interfaces resultando no mínimo de impacto aos seus
consumidores. Este padrão é baseado na lei de Postel que rege os princípios para a correta
colaboração entre serviços.

Consequência do Uso:
        Após a aplicação do padrão Tolerant Reader a colaboração entre os serviços seguirá o
princípio definido pela lei de Postel. Isso permite que os serviços evoluam suas funcionalidades e
interfaces, com o mínimo de impacto aos seus consumidores, pois, o acoplamento gerado pela
comunicação será o mínimo possível. Além disso, caso a resposta de um serviço contenha algum
nível de incoerência será possível que os seus consumidores continuem com as suas operações,
desde que as informações essenciais estejam na resposta, o que diminui a possibilidade de
ocorrência de falhas em cascata.


[PAGINA 57]
                                                                                                57
    Entretanto, a aplicação do padrão Tolerant Reader pode ser dificultada por alguns tipos de
protocolos de transferência de dados, principalmente, os que exigem uma definição fixa da estrutura
da carga transportada (por exemplo, ligação orientada por esquema).

Referências:
      Fowler (2011), disponível em: ​https://martinfowler.com/bliki/TolerantReader.html


[PAGINA 58]
                                                                                              58
REFERÊNCIAS

CONWAY, Melvin E. ​HOW DO COMMITTEES INVENT?. ​Datamation magazine. p. 28-31,
abr., 1968. Disponível em: <​http://www.melconway.com/Home/pdf/committees.pdf​> Accesso em:
22 mai. 2019.


CHRISTENSEN, Ben. ​Fault Tolerance in a High Volume, Distributed System​. The Netflix Tech
Blog, 2012. Disponível em:
<​https://medium.com/netflix-techblog/fault-tolerance-in-a-high-volume-distributed-system-91ab4fa
ae74a​> Acesso em: 25 jul. 2019.


CHEN, Lianping. ​Microservices: Architecting for Continuous Delivery and DevOps.​ In: 2018
IEEE International Conference on Software Architecture (ICSA), 2018, Seattle. Conferência...
Seattle: IEEE, 2018. n. p. Disponível em:
<​https://www.researchgate.net/publication/323944215_Microservices_Architecting_for_Continuou
s_Delivery_and_DevOps​> Acesso em: 23 mai. 2019.


EVANS, Eric. ​Domain-Driven Design: Tackling complexity in the heart of software. ​Boston:
Addison-Wesley, 2003. Disponível em:
<​https://github.com/p0w34007/ebooks/blob/master/Eric%20Evans%202003%20-%20Domain-Driv
en%20Design%20-%20Tackling%20Complexity%20in%20the%20Heart%20of%20Software.pdf​>
Acesso em: 28 jun. 2019.


FOWLER, Martin.​TolerantReader.​ Martinfowler, 2011. Disponível em:
<​https://martinfowler.com/bliki/TolerantReader.html​> Acesso em: 24 jun. 2019.


FOWLER, Martin.​Microservice Premium.​ Martinfowler, 2015. Disponível em:
<​https://martinfowler.com/bliki/MicroservicePremium.html​> Acesso em: 22 mai. 2019.


GUPTA, Arun. ​Microservice Design Patterns.​ ArunGupta, 2015. Disponível em:
<​http://blog.arungupta.me/microservice-design-patterns/​> Acesso em: 22 mai. 2019.

MARTIN, R. C.; MARTIN, M. ​Agile Principles, Patterns, and Practices in C#.​ New Jersey:
Prentice Hall, 2006.


MACCORMACK, A.; RUSNAK, J.;BALDWIN, C. ​Exploring the Duality between Product and
Organizational Architectures: A Test of the “Mirroring” Hypothesis.​ Harvard Business School,
2011. Disponível em:
<​https://www.hbs.edu/faculty/Publication%20Files/08-039_1861e507-1dc1-4602-85b8-90d71559d
85b.pdf​> Acesso em: 22 mai. 2019.


[PAGINA 59]
                                                                                                59
MICROSOFT, Docs. ​Padrões de design dos microsserviços​. DocsMicrosoft, 2019. Disponível
em:<​https://docs.microsoft.com/pt-br/azure/architecture/microservices/design/patterns​> Acesso em:
26 jun. 2019.


NEWMAN, Sam. ​Building Microservices: DESIGNING FINE-GRAINED SYSTEMS: ​1. ed.
Gravenstein: O’Reilly Media, 2015.


POSTEL, Jon.​TRANSMISSION CONTROL PROTOCOL.​ IETF, 1981. Disponível em:
<​https://tools.ietf.org/html/rfc793​> Acesso em: 24 jun. 2019.


RICHARDSON, Chris. ​Microservices Patterns: With examples in Java. ​Shelter Island: Manning
Publications, 2019.


RICHARDSON, Chris. ​A pattern language for microservices.​ Microservices.io, s.d. Disponivel
em: <​https://microservices.io/patterns​> Acesso em: 22 mai. 2019.


TILKOV, Stefan. ​Don’t start with a monolith​. Martinfowler, 2015. Disponível em:
<​https://martinfowler.com/articles/dont-start-monolith.html​> Acesso em: 22 mai. 2019.


YU, Y.; SILVEIRA, H.; SUNDARAM, M. ​A Microservice Based Reference Architecture Model
in the Context of Enterprise Architecture.​ In: 2016 IEEE Advanced Information Management,
Communicates, Electronic and Automation Control Conference (IMCEC), 2016, Xi’an.
Conferência...​ Xi’an: IEEE, 2016. p. 1856-1860. Disponível em:
<​https://ieeexplore.ieee.org/document/7867539​> Acesso em: 23 mai. 2019.
