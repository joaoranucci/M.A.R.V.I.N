# GUIA_SCRUM

Arquivo original: most_similar_papers_to_this_one/GUIA_SCRUM.pdf
SHA-256 do original: 558d09e35d95dc96b0414af6db09fb322b841f15da047b9ef90035a2bef224cb

Texto extraido para consulta. As paginas abaixo usam a ordem do arquivo PDF, incluindo capas.
Parte preparada: 1/1


[PAGINA 1]


[PAGINA 2]
2   Agilidade nas empresas. Guia Scrum para quem não é de TI.


           Agilidade nas empresas. Guia Scrum para quem não é de TI. VOLUME I

                                     Roberto NAVAS Pinheiro

                    PMP, PRINCE2, Agile, Coach, Trainer, Mentor, PMO-CC, ...



                      Baseado na versão do Guia Scrum atualizada em Julho/2016.


[PAGINA 3]
                                                                                   Indice     3


                          Direitos autorais do texto original © 2017.

                                   Roberto NAVAS Pinheiro

                                 Todos os direitos reservados.

      Foto da capa obtida no Wikipedia, referente ao feito de Ashrita Furman quando bateu o
recorde Guinness de maior distância percorrida com uma bicicleta subaquática (3,03 km) em
                uma piscina em Coimbra, Portugal em Setembro de 2011.




                                           3


[PAGINA 4]
4    Agilidade nas empresas. Guia Scrum para quem não é de TI.


            Para o pessoal de casa, esposa e filhos a quem eu muitas vezes deixei na
    sala, vendo TV, enquanto no escritório eu escrevia mais este livro para somar-se aos 2
    anteriores. Bom, para ser sincero, tem também os Webinários e os Workshops do
    PMRAD, do Projetando VOCÊ, e dos Nossos Comportamentos RADIOATIVOS, os
    happy-hours, palestras, congressos, imersão de 2 a 8 dias em algumas formações
    profissionais de Gestão de Projetos e Pessoas e, 120 livros lidos em 5 anos. + ou -
    isso.

           Fiz isto para ser congruente com meus propósitos.

           Sei que é bonito falar de propósito, etc. Mas para se praticar o que se fala (ou
    neste caso, se escreve), tem de ser congruente.

           Meu muito obrigado à minha família pela paciência, muito acima da média


[PAGINA 5]
                                                                                                                                          Indice         5



            Indice

Indice ............................................................................................................................................. 5
Prefácio de Vitor L. Massari .......................................................................................................... 6
Introdução ao tema Agilidade nas empresas ................................................................................ 7
Glossário de termos em Inglês .................................................................................................... 11
Notação usada neste livro ........................................................................................................... 12
I age sà fala à aisà ueàpalavras ............................................................................................. 13
O Propósito do Guia Scrum ......................................................................................................... 20
Definição do Scrum ..................................................................................................................... 21
Teoria do Scrum .......................................................................................................................... 23
Transparência .............................................................................................................................. 24
Inspeção ...................................................................................................................................... 28
Adaptação ................................................................................................................................... 29
Valores do Scrum ........................................................................................................................ 31
O time Scrum ............................................................................................................................... 33
O Product Owner......................................................................................................................... 40
O Time de Desenvolvimento ....................................................................................................... 44
O tamanho do Time de Desenvolvimento .................................................................................. 47
O Scrum Master .......................................................................................................................... 49
Eventos Scrum ............................................................................................................................. 55
A Sprint ........................................................................................................................................ 57
Planejamento da Sprint ............................................................................................................... 63
Reunião Diária ............................................................................................................................. 71
Revisão da Sprint ......................................................................................................................... 73
Retrospectiva da Sprint ............................................................................................................... 75
Artefatos do Scrum / Backlog do Produto .................................................................................. 78
Artefatos do Scrum / Backlog da Sprint ...................................................................................... 86
Incremento .................................................................................................................................. 91
Transparência do Artefato .......................................................................................................... 92
Defi içãoàdeà P o to .................................................................................................................. 93
Notas finais .................................................................................................................................. 95
Conclusão .................................................................................................................................... 97
CV do autor, Roberto NAVAS Pinheiro ........................................................................................ 98
PLA Solutions ............................................................................................................................... 99
VCPRO training .......................................................................................................................... 100
CAPIE Mentoring ....................................................................................................................... 101
PMO encontros Ágeis / tech Talks / People sharing toughts .................................................... 103
PMO Global Alliance & PMO VALUE RING ................................................................................ 105




                                                                         5


[PAGINA 6]
6    Agilidade nas empresas. Guia Scrum para quem não é de TI.



           Prefácio de Vitor L. Massari

            Como um grande entusiasta e praticante da metodologia ágil é sempre uma
    enorme honra poder contribuir com algumas palavras de abertura, ainda mais quando
    se trata de um querido amigo como o NAVAS.


           Pude acompanhar de perto a trajetória Ágil do amigo NAVAS, desde uma das
    primeiras edições do PMO Encontros (evento muito bacana organizado por ele), onde
    mostrei alguns conceitos básicos e iniciais de Agilidade em um quase papo de bar, até
    encontrá-lo em treinamentos, palestras e ouvir com muita alegria os resultados que
    vinha obtendo ao explorar este método de trabalho.



           Mais alegria ainda quando vi que o amigo se tornou um entusiasta como eu,
    ajudando pessoas e empresas a darem estes passos rumo a este universo de muito
    trabalho, pouco desperdício, que foca em pessoas e entregas rápidas de valor.



            E agora o amigo NAVAS proporciona a você leitor um ótimo livro que servirá
    como guia para você dar seus primeiros passos rumo à agilidade. Neste livro em
    específico, o foco é no framework Scrum, mas NAVAS se preocupa em te revelar logo
    no início do livro a grande essência, o grande “tempero” dos métodos ágeis: o Lean
    Management e o trabalho através de ciclos PDCAs (Kaizen) curtos.



           Incorporando Lean e Kaizen curto na sua forma de pensar e no seu método de
    trabalho, torna-se “mamão com açúcar” incorporar as “sopas de letrinhas” ou os
    chamados frameworks/métodos ágeis (Scrum, XP, FDD) em qualquer área de trabalho
    e não somente TI. Neste livro, a bola da vez é o Scrum que, como o próprio NAVAS
    mencionará daqui a pouco é fácil de entender e difícil de dominar.



             Então do fundo do coração espero que, com este livro, você comece a
    entender e a praticar para valer! Tenho certeza que muito em breve não será mais
    difícil de dominar e você obterá grandes resultados em seus projetos!



           Vitor L. Massari

           CEO e Agile Coach da Hiflex Consultoria


[PAGINA 7]
                                              Introdução ao tema Agilidade nas empresas   7



       Introdução ao tema Agilidade nas empresas

        Quando eu li o livro a 5ª Disciplina de Peter Senge na década de 90, ficou para
mim a importância do pensamento sistêmico. O pensamento sobre o qual como é que
existem sistemas (relacionamentos) em todos os lugares, todos os lados e de todos os
tipos, como somos influenciados por estes sistemas e como podemos usar destes
sistemas em nosso benefício. Serviu para entender que podemos atuar em um ponto
aqui do sistema, para influenciar outros lados e resultados nos quais tenhamos
interesse. Isto me lembra também a Teoria das Restrições (TOC) de Eliyahu Goldrat,
“corrige uma restrição aqui, aparece outra lá”.

       Pessoalmente, sou praticante (ser praticante é mais que ser favorável, certo?)
do pensamento ecológico, digo, não é ecológico, saudável e sustentável, você ir
contra os sistemas no qual você está inserido, por que você acha que seria saudável e
produtivo defender algo que só você faz num grupo que caminha unificado para outra
direção? É fácil nadar contra a correnteza? É correto ser desrespeitoso com nossos
pais, não sermos exemplo nas ações da vida pessoal e cobrarmos atitudes corretas
dos nossos filhos? Isto não é sistêmico, não é ecológico.

        Ainda, as direções mudam conforme alguns ciclos terminam e outros
começam, os períodos de adoção, uso e descontinuidade de algo são cíclicos e não
são infinitos. A adoção a novos jeitos de fazer as mesmas coisas ou coisas
completamente novas, disruptivas, acontecem em ondas, quando novas ondas
chegam, você tem 2 opções, ou pega uma prancha e surfa a onda ou pega uma
estaca, finca no chão e torce parar continuar ali e respirando depois que o Tsunami
passar. A primeira opção, adaptar-se e seguir o fluxo é alinhada, ecológica, sistêmica
e saudável. A segunda opção, resistir à mudança e permanecer estático no ponto que
está, é contraproducente, conflitante e pode não ser saudável, muitas vezes, pode não
ser possível.

        Outro ensinamento da década de 90 novamente, agora de um dos bons
professores que tive, alguns oriundos da ‘indústria automotiva do ABC’, é sobre a
síndrome do sapo fervido, uma metáfora, mas que ficou comigo até hoje – como toda
boa metáfora – por favor, neste momento, convido você a suspender o julgamento de
valor quanto a ‘fritar sapos’. Diz-se que se você colocar um sapo numa panela com
água em temperatura ambiente ele ficará tranquilo lá. Se esta panela for levada ao
fogo, a temperatura da água vai subir aos poucos e o sapo não vai perceber as
evoluções na temperatura. Quando a temperatura subir mais, o sapo vai continuar lá,
resistindo, até que a água entre em ponto de fervura e o sapo seja ‘frito’. Agora, se
você jogar o sapo em água fervente de uma vez só, ele vai sentir o choque e vai sair
pulando para fora da panela no mesmo momento, salvando a sua vida, digo, a vida
dele.

        Trazendo para o nosso tema, nas nossas profissões, empresas e vidas,
precisamos estar ‘atentos às mudanças’ que acontecem todos os dias no mercado,
nas tecnologias, nas empresas, na profissão, na vida. Elas podem ser pequenas (nem
sempre) tal como constantes mudanças de ‘temperatura’ que se nós não percebemos
como éramos, como estamos e qual a projeção para como seremos, podemos ficar
estáticos, como o sapo, e quando a água ferver, aí já será tarde demais para reagir.




                                          7


[PAGINA 8]
8       Agilidade nas empresas. Guia Scrum para quem não é de TI.


            Voltando ao tema indústria automotiva como ícone da era industrial, este foi
    (me arrisco a dizer assim, com um ‘foi’) um tempo fundamentado em produtos físicos e
    coisas analógicas, onde a noção de ‘serviço’ agregado aos produtos era mais
    insipiente que hoje e a concorrência era muito, muito, muito menor. Pense por um
    minuto em quantas fábricas de automóveis tínhamos no Brasil na década de 80 e
    quantas temos hoje. Em ordem de grandeza, 5 antes e 25 agora?

           Lembro-me da célebre frase atribuída a Henry Ford de que “o cliente pode ter o
    carro da cor que quiser, contanto que a cor seja preto”, oriunda do pensamento da
    época de ganho de escala pela padronização de tudo. Nesta época os lançamentos de
    novos carros ou novos modelos aconteciam em ciclos longos, se não me engano, da
    minha época de Volkswagen na década de 90, chegava-se a gastar uma década para
    lançar um carro novo e uns 4 anos para uma remodelação de um já em linha de
    produção.

           No rastro deste cenário de quando o mercado te dava tempo de sobra para
    lançar novos produtos (com menos concorrência) e sendo estes produtos físicos e
    analógicos, as técnicas de planejamento foram evoluindo junto, ficando cada vez
    melhores em dar precisão de longo alcance para o lançamento de produtos, com a
    possiblidade de altos níveis de detalhamento e precisão no planejamento nos mínimos
    detalhes. WBS, Gant e PERT são termos conhecidos dos especialistas em gestão de
    projetos. Até porque a demanda não era tão alta, mas principalmente, porque a
    concorrência era baixa, a indústria tinha a oportunidade de ter tempo de planejar os
    próximos produtos com alto nível de detalhe, desde a concepção dos produtos, e até
    de certo modo, desacoplado dos serviços que circundavam os produtos.

           Convido você a pensar agora, em empresas de classe mundial famosas que
    seguem se reinventando e se transformando para sobreviver num mercado muito,
    muito, muito diferente e, algumas que até nem existem mais – em ordem alfabética
    (novamente, sem julgamento de valor Ok?):

           - Atari, Bamerindus, BCP, BlockBuster, Compaq, Ford, GM, Gurgel, GVT,
    Honda, Kodak, Kolynos, Manchete, Mappin, Mesbla, Nacional, Orkut, Telefônica,
    Toyota, VARIG, VASP, Volks, Volvo.

           Esta lista me remete uma outra lista de empresas, empresas da era do
    conhecimento (de novo, sem julgamento de valor, Ok? É só um brainstorming rápido e
    superficial).

              - Airbnb, Alibaba, Amazon, eBay, Facebook, Google, Tesla, Uber, Zappo.

           Pense em como tem sido o desenvolvimento de carros elétricos (Tesla1), e
    autônomos (Google entre outros players) nos últimos tempos. Como podem gigantes
    de hospedagem (Airbnb), vendas (Alibaba), conteúdo (Facebook) e transporte (Uber)
    não terem em seus ativos, imóveis, centros de distribuição, redações e veículos?

           Para estas empresas – e outras que não surgiram nesta minha lista super
    reduzida, talvez os Produtos possam ser considerados Commodities e o seu grande
    diferencial competitivo ou até mesmo seu core business sejam os Serviços. Seja pela


    1
     Tesla, comumente conhecida com Tesla Motors, retirou a palavra Motors do seu nome e agora
    denomina-se uma empresa com foco em projetos de inovação em tecnologia energética. Veja mais em
    http://tesla.com


[PAGINA 9]
                                              Introdução ao tema Agilidade nas empresas   9


sua incrível capacidade de se colocar no lugar dos clientes e resolver seus mais
importantes problemas, até criar necessidades que nós nem sabíamos que tínhamos e
criar mercados inteiros do zero. Pense 1 minuto nisto.

        Nesta nossa era de conhecimento e informação digital, os Serviços e as suas
facilidades são tão ou talvez até mais importantes que os Produtos (Airbnb e Uber são
empresas que só tem Serviços! Nenhum produto físico tipo tijolo, cimento, metal,
borracha e combustível você encontra lá).

        Ainda, a concorrência é brutal hoje em dia. Ideias inovadoras são copiadas
rapidamente. Algumas cópias conseguem ser até melhores que as ideias originais.
Então a chance de uma inovação ser superada pela próxima ‘cópia’ é uma realidade,
cruel, mas real.

       Quer seja porque você tem uma grande operação e precisa fazer melhoria
contínua sempre (Kaizen) e prover melhor eficiência operacional sendo sempre uma
operação mais enxuta (Lean Manufatura ou Lean Transacional). Quer seja porque
você está desenvolvendo um Produto ou Serviço diferente, inovador e precisa testar
rápido suas ideias, obter feedback do mercado e adaptar as suas próximas ações
(Lean Startup).

       Seja lá por qual das razões sistêmicas acima for (ou por todas as outras razões
e coisas que você acredita, conhece, sabe e percebe que estão acontecendo na sua
‘panela’), o imperativo é responder às mudanças, é adaptar-se. Já dizia Darwin, que
“não é o mais forte que sobrevive, mas o que melhor se adapta às mudanças”.

      É neste contexto de agilidade em inovar e responder às mudanças, que o
Scrum se apresentou na década de 90 como um conjunto de regras, papéis,
responsabilidades e formas de fazer as coisas no TI das empresas. Virtualmente,
qualquer empresa.

       Vamos explorar neste livro o Guia do Scrum atualizado para a sua versão mais
nova (de Julho/2016), traduzido oficialmente para o Português aqui no Brasil pelo
colega Fábio Cruz autor de best sellers sobre Scrum. Comento e faço uma ampliação
pessoal do Guia neste livro com conteúdo fortemente relacionado aos benefícios do
Scrum para os negócios. Como o título diz, é um livro para quem não é de Tecnologia.

       Não espere um texto preparatório para certificações de Scrum Master ou
mesmo Product Owner, ou um texto técnico sobre desenvolvimento e operação de
ambientes de TI de forma ágil (DevOps), que embora sejam pilares importantes da
Agilidade, não é o foco do livro.

       Faço votos que você possa perceber valor, em um texto que ajuda você a
entender como extrair o melhor resultado possível dos seus investimentos em
Tecnologia da Informação – TI. O grande foco deste Guia Scrum para quem não é de
Tecnologia, é para com os Donos de Produtos, sobre como ser beneficiado pelo
ganho de performance, produtividade e qualidade que seus times de TI vão lhe
proporcionar, quando usando Scrum.

      Tem o texto, objetivo de ser uma tradução para quem não é de tecnologia
entender alguns termos técnicos sobre os quais podem eventualmente haver dúvidas.

       Vamos ao Guia?




                                          9


[PAGINA 10]
10   Agilidade nas empresas. Guia Scrum para quem não é de TI.


[PAGINA 11]
                                                                 Glossário de termos em Inglês   11



          Glossário de termos em Inglês

          Alguns termos do Guia do Scrum foram mantidos original em Inglês por falta de
uma equivalência direta do seu significado em Língua Portuguesa. A lista abaixo dá uma
explicação geral destes termos (a maior parte traduzida do Cambridge Dictionary) e
todas as vezes que estes termos em Inglês aparecerem no texto, estes serão grafados,
em itálico. Vale citar que Scrum não é um termo em Inglês, uma sigla ou um acrônimo.
Seu significado será explicado no texto.

 Termo em Inglês           Significado em Português (traduzido do Cambridge Dictionary)

 Framework            Um conjunto de regras, ideias ou crenças que é usado para planejar ou
                      decidir algo

 Sprint               Correr a toda velocidade uma distância curta ou em um tempo
                      determinado

 Stakeholder          Uma pessoa ou um grupo de pessoas tais como empregados, clientes
                      ou cidadãos que são envolvidos com uma organização, sociedade ou
                      assunto e, portanto, tem responsabilidades sobre este, interesse no
                      sucesso de algo, sendo impactado positiva ou negativamente.
                      Comumente traduzido como ‘partes interessadas’ (em algo sobre o qual
                      se está fazendo) nas publicações de projetos

 Backlog              Uma certa quantidade de coisas aguardando para serem feitas, uma
                      lista de coisas a fazer numa certa prioridade

 Container            Algo vazio, tal como uma caixa, que pode ser usado para acomodar
                      algo de modo especial, para fins de transportar ou armazenar. Algo que
                      serve para encaixar outras coisas dentro

 Time-box ou time-    Um termo comum ao meio ágil com significado de atividades com
 boxed                duração fixa (tal como Sprint), nem mais nem menos que o previsto, de
                      modo que o time de trabalho possa, de modo repetível, fixo e previsível,
                      finalizar atividades sempre num tempo programado e tornar-se mais
                      produtivo à cada novo time-box. A lógica (adiantando um pouco o livro)
                      é que o tempo permanece o mesmo, mas a quantidade de trabalho
                      produzido no mesmo tempo, time-box, aumenta, significando um
                      aumento da velocidade, da produtividade




                                             11


[PAGINA 12]
12       Agilidade nas empresas. Guia Scrum para quem não é de TI.



                Notação usada neste livro

                Em todos os capítulos do livro, considere que o texto principal em fonte ‘Arial’
     (utilizada até agora neste ponto) é o texto padrão do Guia Scrum 2016, traduzido da
     versão Inglês pelo amigo autor Fábio Cruz, sem acréscimos, nem alterações.

                       Nos trechos identados à direita e escritos em fonte ‘Times New Roman’ e
              cor azul, considere que são as minhas contribuições para o seu entendimento do
              Guia Scrum caso você não seja de TI.

                       Por motivos de diagramação e para nem sempre interromper uma narrativa
              e facilitar o seu entendimento, a sua linha de raciocínio, também poderá ser feito
              uso de Notas de Rodapé2.

                Recado dado, vamos ao Guia!




     2
         Por exemplo, assim ...


[PAGINA 13]
                                                      I age sà fala   à aisà ueàpalav as   13



 I age s falam              ais ue palav as

        Opa, alarme falso, antes de iniciar nosso mergulho no Guia propriamente
dito, vamos usar um conjunto de imagens, para você passear pelo Scrum numa
‘rápida passada de olhos’. Dizem que imagens são ‘autoexplicativas’, então vamos
fazer uso delas.




        Agora sim, ficou bem claro tudo. Scrum é isso! Pronto! Da esquerda para a
direita, um conjunto de papéis, responsabilidades, eventos e artefatos, um
refinamento constante das coisas e tarefas que há para fazer, um tempo
determinado para ter algo pronto, um acompanhamento diário e próximo do
trabalho, uma aceitação do produto por quem o pediu e o definiu e oportunidades
recorrentes de melhorar a tudo e a todos e, começar de novo.

Onde tudo começa?




                                        13


[PAGINA 14]
14   Agilidade nas empresas. Guia Scrum para quem não é de TI.




                 1º papel envolvido é o Product Owner, uma pessoa que representa outras
         pessoas na organização ou ainda fora dela – clientes finais, interessadas num certo
         assunto (um produto ou um serviço, uma característica ou funcionalidade). Esta
         pessoa mantém atualizado uma “lista de coisas para fazer” – neste momento, algo
         tão simples quanto isso. Uma lista em ordem de prioridade, no topo da lista, em
         detalhes está o que há de mais importante e prioritário, pois é o que mais agrega
         valor para o seu negócio, produto, operação, serviço, etc.

                 Este Product Owner é atendido por uma equipe de trabalho, então vamos a
         ela.


[PAGINA 15]
                                                    I age sà fala   à aisà ueàpalav as   15




       Uma equipe dedicada para atender a tal “lista de coisas para fazer” –
chamada de Product Backlog, seleciona alguns dos itens da lista e desdobra em
uma lista com tarefas, chamada Sprint Backlog, com as partes de produto que a
equipe se compromete como sendo possível deixar pronto num espaço
determinado, e curto, de tempo (time box). Isto é um trabalho chamado
planejamento da Sprint.




                                      15


[PAGINA 16]
16    Agilidade nas empresas. Guia Scrum para quem não é de TI.


             Chegamos ao 3º papel, o Scrum Master, que como o próprio nome já é
     autoexplicativo, é alguém com Master domínio e conhecimento deste modo de atuar
     chamado Scrum, daí Scrum Master, e vai ajudar as pessoas anteriores (Product Owner e
     Equipe Dedicada - Team) a fazer o seu trabalho de forma aderente ao que está dito como
     “o jeito Scrum de ser”.




                   Como colocado antes, uma Sprint (uma força-tarefa de tiro curto, digamos)
           acontece com uma duração de tempo fixa, algo entre a cada 1 ou 4 semanas uma
           Sprint encerra-se começando outra. Ou seja, em 1 ou 4 semanas a equipe Dedicada
           (Team) executa todas as tarefas com a qual ela havia se comprometido compor a
           Sprint Backlog. É importante que não ocorram alterações do conteúdo da Sprint
           Backlog, durante a Sprint, digo, nem encurtar nem prorrogar a duração, ou incluir
           coisas novas que não estavam previstas de fazer.


[PAGINA 17]
                                                      I age sà fala   à aisà ueàpalavras   17




        Uma das atribuições do Scrum Master na busca por manter “o jeito Scrum
de ser” ativo, é proporcionar que o planejamento feito pela Equipe Dedicada –
Team, no início da Sprint, possa ir sendo acompanhado diariamente pelo Time.
Este acompanhamento diário é seguido de perto pelo Product Owner (interessado
no produto final, lembra-se?) e, é normal que aconteçam refinamentos daquele
“Product Backlog” definido de forma mais alto nível no início. Isto não significa
trazer novas prioridades de outros temas, mas significa refinar as definições dos
assuntos já priorizados e já programados para serem entregues num horizonte de
tempo de 1 a 4 semanas (time box).




                                        17


[PAGINA 18]
18   Agilidade nas empresas. Guia Scrum para quem não é de TI.




                 Quase no final da Sprint, o Time obtém do Product Owner uma avaliação
         final do que ficou pronto. Com a aprovação do Product Owner, o que está
         finalmente considerado pronto é encaminhado para ser liberado, ajustes finais
         pontuais são feitos. Se o novo pedaço de produto (incremento de produto)
         apresentado for recusado pelo Product Owner, o item volta, ..., lá para a Product
         Backlog, a “lista de coisas para fazer”.


[PAGINA 19]
                                                      I age sà fala   à aisà ueàpalav as   19


        Bom, de posse destes 2 possíveis feedbacks, um bom, de aceitação do
incremento de produto (de mais uma parte pronta do produto) e outro ruim, de
rejeição do trabalho feito e a necessidade de retrabalho, o Scrum Master ajuda o
Time a resgatar em forma de retrospectiva (olhando ‘pelo retrovisor’ sobre os fatos
incorridos durante a Sprint), o que é que foi feito de bom, gerou bons resultados e
precisa ser repetido mais vezes e até compartilhado com outros times Ágeis da
empresa e, o que é que não foi bom, não funcionou e precisa ser evitado repetir até
mesmo no próprio time, já na próxima Sprint que agora vai começar, reiniciando os
trabalhos com os novos itens mais prioritários da Product Backlog, planejando e
combinado outra Sprint Backlog, já levando em consideração as lições aprendidas
na anterior e assim por diante nas demais Sprints.



        Agora que você entendeu tudo de forma rápida e clara , agora sim,
vamos em definitivo ao Guia do Scrum!




                                        19


[PAGINA 20]
20    Agilidade nas empresas. Guia Scrum para quem não é de TI.



            O Propósito do Guia Scrum

            Scrum é um framework para desenvolvimento e sustentação de produtos
     complexos. Este Guia contém a definição do Scrum. Esta definição consiste dos
     papéis, eventos, artefatos e regras que ligam tudo isso junto. Ken Schwaber e Jeff
     Sutherland desenvolveram o Scrum; o Guia do Scrum é originalmente escrito por eles.
     Juntos, Ken e Jeff são as pessoas que apoiam o Guia do Scrum.

                  Ken Schwaber e Jeff Sutherland difundiram o Scrum no desenvolvimento
          de software em empresas de TI nos Estados Unidos na década de 90, baseado no
          estilo de gerenciamento de produtos em empresas automotivas Japonesas à partir
          de um estudo publicado pelos professores Hirotaka Takeuchi e Ikujiro Nonaka, no
          artigo “The New New Product Development Game” (Harvard Business Review, de
          Janeiro/1986).

                  Scrum é derivado do pensamento Lean Manufacturing surgido do Sistema
          Toyota de Produção. Em tempo, Scrum não é uma sigla, um acrônimo. Scrum é o
          nome da formação do Rugby usada para reiniciar o jogo em certos casos.
          Falaremos mais disso mais à frente.

                  Importante destacar aqui a citação de aplicabilidade do Scrum para o
          desenvolvimento de produtos complexos, quando não se tem uma visão ‘clara e
          completa de tudo’ que se deseja alcançar. Veja mais abaixo.


[PAGINA 21]
                                                                                 Definição do Scrum         21



        Definição do Scrum

        Scrum (substantivo): Um framework dentro do qual pessoas podem tratar e
resolver problemas complexos de forma adaptativa3, enquanto entregam produtos com
o mais alto valor possível, de forma produtiva e criativa.

        Scrum é algo:

                         Leve;
                         Simples de entender e
                         Difícil de dominar4


        Scrum é um framework estruturado de forma processual, que vem sendo usado
para gerenciar o desenvolvimento de produtos complexos desde o início da década de
90. Scrum não é um processo ou uma técnica para construir produtos; em vez disso, é
um framework dentro do qual você pode empregar vários processos ou técnicas. O
Scrum deixa claro a eficácia relativa às práticas de gerenciamento e desenvolvimento
de produtos, de modo que você possa melhorar.

        O framework Scrum consiste de Times Scrum e seus papéis, eventos, artefatos
e regras associadas. Cada componente dentro do framework serve a um propósito
específico e é essencial para o uso e o sucesso do Scrum.

        As regras do Scrum integram de forma unificada os eventos, os papéis e os
artefatos e governam os relacionamentos e interações entre eles. As regras do Scrum
são descritas ao longo do texto.

        Táticas específicas para uso do framework Scrum variam e são descritas em
outros documentos.

               Neste ponto, mora uma complicação. O termo framework é amplo, um
      monte de ‘coisas’ encaixa-se como ‘framework’, então até aqui foi possível
      entender que o Scrum é fácil de entender por não ser prescritivo é difícil de
      dominar pelas mudanças culturais (você vai entender bem isto). Atenção seja dada

3
  A forma adaptativa tem relação com a necessidade de adaptar-se rápido em resposta às mudanças que
ocorrem.
4
  Leveàsig ifi aàse àpou oàp ofu doàeà ãoàp es itivoà ãoàdizà o o àfaze .àPo à ãoàse àp ofu do,àeleà à
simples de entender os princípios, regras, papéis, eventos. Por não ser prescritivo e, como o jeito Scrum
ou Ágil de fazer pode ser uma ruptura no modo que você e seu time fazem hoje o trabalho, ele será
naturalmente difícil de dominar num primeiro momento. O fato de você aceitar isto, já é um 1º passo
importante na direção de aprender. Faça algo diferente na próxima chance que você tiver de fazer algo.
A mudança é movimento.



                                                  21


[PAGINA 22]
22   Agilidade nas empresas. Guia Scrum para quem não é de TI.


         ao ponto, de que “one size does not fits all” – não considere que existam respostas
         prontas e sempre iguais para todos os problemas.


[PAGINA 23]
                                                                                   Teoria do Scrum    23



        Teoria do Scrum

        Scrum é fundamentado nas teorias de controle empírico5 de processos. O
controle empírico afirma que o conhecimento vem da experiência e a tomada de
decisões é baseada no que é conhecido. O Scrum emprega uma abordagem iterativa
e incremental para otimizar a previsibilidade e o controle de riscos. Três pilares apoiam
toda implementação de processo empírico de controle: transparência, inspeção e
adaptação.

                 Este parágrafo traz consigo um mundo de diferenças, pois controle empírico e
        adaptação são inversamente opostos às estruturas tradicionais de gestão preditivas e de
        comando e controle. No modelo preditivo todo o plano é previsto em detalhes e com
        antecedência, predominando a partir daí o modelo de comandar e controlar a realização
        das atividades conforme planejado antes de iniciar a execução.

                 Bom, ser empírico e adaptativo é o oposto de preditivo, é acreditar em não fazer
        toda a projeção do futuro, mas concentrar-se em realizar partes do todo, de modo a
        aprender na prática sobre o que se está fazendo, como se está fazendo e com quais
        capacidades se conta no time e então, ir adaptando tudo (a expectativa de produto final
        pronto, utilizável e rentável – seja lá qual for sua medição de sucesso; o modo de
        trabalho e principalmente a capacidade das pessoas envolvidas com o trabalho).

                 Esta mudança de paradigma não acontece por “decreto”, mas pelo uso
        consistente de 3 pilares do Scrum, a transparência, a inspeção e a adaptação. Vejamos.




5
 Empírico, significa dizer que algo é baseado do que foi experimentado ou visto ao invés de um dado
teórico, presumido ou projetado



                                                 23


[PAGINA 24]
24    Agilidade nas empresas. Guia Scrum para quem não é de TI.



            Transparência

            Transparência diz respeito ao fato de que aspectos significativos do processo
     devem ser visíveis para aqueles que são responsáveis pelos resultados.
     Transparência requer que aspectos sejam definidos por um padrão comum de modo
     que os observadores compartilhem um mesmo entendimento do que está sendo visto.

            Por exemplo:

                            Uma linguagem comum referindo-se ao processo de ser
            compartilhada por todos os participantes e;
                            Uma definição comum de “Pronto” deve ser compartilhada por
            aqueles que realizam o trabalho e por aqueles que aceitam o resultado do
            trabalho.

                       Transparência de aspectos importantes (o progresso de um trabalho em
             andamento – por exemplo) para aqueles que são responsáveis pelo resultado (o dono
             de algo que será entregue e usado para trazer ganhos financeiros para a empresa – por
             exemplo) é um pilar do Scrum muito relacionado às análises de Takeuchi e Nonaka na
             década de 80 onde estes sugeriram a sobreposição de fases (e também seus times
             especialistas) originalmente estanques (menor interação) e sequenciais (uma fase
             posterior somente começa com o fim integral da anterior), como forma de aceleração
             dos resultados.


                       Para que isto seja verdade e realmente produtivo (esta sobreposição, este
             paralelismo de trabalhos iterativos das equipes), é necessário que a forma de trabalhar
             por todos seja comum e amplamente entendida, além do que a definição de o que
             significa estar pronto para uma equipe B seja o mesmo entendimento de estar pronto
             para a equipe A. Voltando à linha de produção, um time que espera uma roda
             parafusada com torção suficiente para o carro pegar uma estrada, não pode receber
             uma roda com parafusos apertados somente o suficiente para pendurar o pneu,
             imaginando que passos posteriores fariam esta tarefa.


                       Exemplificando uma forma de transparência, você verá equipes Scrum
             utilizando quadros branco, paredes ou então painéis digitais em software de trabalho
             em equipe, visíveis ao time de trabalho e aos responsáveis pelo resultado, com
             quadros Kanban indicando:


[PAGINA 25]
                                                                         Transparência    25


        - o que há para o time de pessoas fazer – trabalho que ainda não começou,
- o que está sendo feito e em andamento neste momento e,
- o que já foi feito e está considerado pronto para entrega e não requer mais trabalho.

        Técnicas de quadro tipo Kanban (a fazer, fazendo, verificando e feito) e outros
quadros do tipo burn down chart (de tudo que temos para fazer, onde estamos hoje, o
que ainda falta para se fazer e até quando estará tudo feito) ou burn up chart (um
quadro acumulativo de o que já foi e o que está sendo gerado de benefício), são
exemplos de ferramentas chamadas de Administração à vista. Ou seja, sempre à vista
e transparente para os responsáveis pelos resultados.


        Exemplo de um quadro Kanban muito simples, com atividades que fluem da
coluna a fazer, para fazendo e indicando as finalizadas. O quadro Kanban dá senso de
fluxo, de movimento e também de gargalos para o time.




                          Figura 1 – quadro Kanban


        Faça uso de um Kanban no seu dia-a-dia qualquer que seja o assunto (estudar
algo – por exemplo) e confirme o senso de movimento que o Kanban proporciona. Se
quiser conhecer uma aplicação de Scrum na Educação – por exemplo, veja o site
http://eduscrum.nl/en e faça suas analogias.


        Exemplo de um quadro Burn Down, onde fica demonstrado a “eterna luta”
entre as linhas azul (esperado) e vermelha (realizado). Se elas estão juntas, então o



                                     25


[PAGINA 26]
26   Agilidade nas empresas. Guia Scrum para quem não é de TI.


            realizado está em linha com a expectativa. Se a linha vermelha está acima, então o
            trabalho está aquém da expectativa. Se a linha vermelha está abaixo da azul, então o
            trabalho está adiantado e pode terminar antes.




                                  Figura 2 – gráfico de Burn Down


                    A próxima vez que você tiver uma bateria de coisas a fazer em 10 dias
            (exemplo da figura 2), faça um gráfico de burn down e vá plotando para acompanhar
            como é que a sua velocidade está em relação ao seu objetivo de terminar tudo em 10
            dias.


                    Exemplo de um quadro Burn Up, onde fica demonstrado a expectativa do total
            de benefícios que será entregue até o final de ‘n’ iterações, Sprints ou time-boxes (a
            linha vermelha), a linha azul com o trabalho que está completo iteração a iteração
            (acumulado), a linha verde com uma projeção média das entregas até o ponto final e,
            fotos do caminho em situações hora à além do plano hora aquém do plano.


[PAGINA 27]
                                Transparência   27




Figura 3 – gráfico de Burn Up




             27


[PAGINA 28]
28    Agilidade nas empresas. Guia Scrum para quem não é de TI.



            Inspeção

            Os usuários Scrum devem inspecionar frequentemente os artefatos Scrum e o
     progresso rumo às metas da Sprint para detectar variações indesejáveis. As inspeções
     são mais benéficas quando realizadas de forma diligente por inspetores
     especializados no trabalho a ser verificado.

                    Inspeção é um 2º pilar, pois pressupõe uma proximidade constante do principal
            responsável pelos resultados, do time, dos trabalhos e principalmente dos resultados
            intermediários. Ao avaliar com frequência o progresso e os resultados intermediários,
            pode ser possível identificar variações (entre a expectativa de resultado futuro – um
            skate rodando por exemplo, e a realidade que está se apresentando – uma prancha de
            madeira sem lixa e acabamento nas bordas por exemplo) o mais cedo possível e
            corrigir o rumo em tempo.

                    Quanto mais propriedade, interesse e responsabilidade sobre o produto final
            esperado o revisor tiver (mais responsável pelo benefício resultante ele for), melhor e
            mais criterioso será seu interesse em fazer o acompanhamento do progresso. O time que
            está atuando aproveita as inspeções para entender se, na velocidade atual, o time
            atingirá todo o progresso esperado até o final da Sprint.

                    Vem daí então o conceito de time-box, um período pré-determinado de tempo,
            para entregar uma parte ou uma versão intermediária de produto pronto e passível de
            uso pelo seu responsável, já obtendo resultados e benefícios para a organização e
            obtendo feedback da efetividade do que já está em uso – o melhor skate possível dentro
            de um período determinado de tempo.

                    Portanto, neste momento surgiram já alguns conceitos importantes, como:
            Sprint, um tiro-curto de algumas semanas para entregar algo utilizável; time-box, um
            tempo determinado para duração das Sprints, o que traz previsibilidade para quem está
            interessado no produto final e; velocidade, o ritmo com o qual o time está fazendo
            entregas aceitas como prontas pelo principal interessado no resultado final dos
            trabalhos.


[PAGINA 29]
                                                                                    Adaptação     29



       Adaptação

Se um inspetor determina que um ou mais aspectos de um processo desviou para fora
dos limites aceitáveis, e que o produto resultante será inaceitável, o processo ou o
material sendo processado deve ser ajustado. O ajuste deve ser feito o mais breve
possível para minimizar mais desvios.

       Neste trecho, com uma linguagem próxima de industrial, e trazendo agora para outros
       contextos também, podemos dizer que ao se fazer inspeções frequentes e transparentes
       (pilares anteriores) pode ser constatado que o produto resultante do trabalho parece não
       estar progredindo na direção entendida inicialmente e que poderá não ser aceito como
       pronto e entregue, requerendo que o time de trabalho faça adaptações para corrigir o
       rumo: quer seja, melhorando as definições do produto a ser entregue, refinando,
       alinhando em maiores detalhes as expectativas (se os cantos do skate tem de ser
       abaulados, se a lixa tem de ser integral no shape) ou; quer seja, alterando o modo como
       o trabalho está sendo feito, retirando algum impedimento ou dificuldade que possa
       aumentar a chance de entregar o produto final que já está claro (se a lixa não tem grip
       suficiente, se a manipulação da madeira está tomando um tempo excessivo, etc).

       De um modo ou de outro, o importante a destacar é a vinculação do conceito de
       inspeção frequente e transparente e, principalmente da capacidade de adaptação, ao
       contexto do processo empírico, no qual se aprende com a execução e se corrige (adapta)
       o produto final e principalmente o processo de elaboração e as pessoas envolvidas, com
       a observação (a inspeção) da realidade em andamento.

O Scrum prescreve quatro eventos formais para inspeção e adaptação, como descrito
na sessão de Eventos Scrum deste documento:


      Reunião de Planejamento da Sprint
      Reunião Diária
      Reunião de revisão da Sprint
      Retrospectiva da Sprint

       Estes eventos serão descritos em detalhes à frente, mas em resumo, eles são as seguintes
       ações:


               Planejar o que será feito numa unidade determinada de tempo, uma Sprint;
               Acompanhar diariamente o trabalho que está para fazer, sendo feito e o que já
                está pronto;



                                             29


[PAGINA 30]
30   Agilidade nas empresas. Guia Scrum para quem não é de TI.


                 Rever e negociar que algo está considerado pronto pelo responsável pelo
                  resultado final;
                 Rever as lições aprendidas na Sprint que acabou, e como elas podem ser
                  aproveitadas já no planejamento do que será feito na próxima unidade de
                  tempo, na próxima Sprint.


[PAGINA 31]
                                                                         Valores do Scrum      31



       Valores do Scrum

       Quando os valores de comprometimento, coragem, foco, abertura e respeito
estão incorporados e são vividos pelo time Scrum, os pilares de transparência,
inspeção e adaptação do Scrum tornam-se vivos e criam confiança para todos. Os
membros do time Scrum aprendem e exploram estes valores enquanto trabalham com
os eventos, papéis e artefatos Scrum.

       O uso bem-sucedido do Scrum depende das pessoas tornarem-se mais
proficientes em viver estes cinco valores. As pessoas são comprometidas em atingir
as metas do time Scrum. Os membros do time Scrum tem coragem de fazer a coisa
certa e trabalhar em problemas difíceis. Todos focam no trabalho da Sprint e nas
metas do time Scrum. O time Scrum e seus stakeholders concordam em ser abertos
sobre o trabalho e os desafios de fazer o trabalho. Os membros do time Scrum
respeitam-se mutuamente como pessoas capazes e independentes.

              Esta sessão Valores foi acrescida agora na versão de Julho/2016 do Guia Scrum,
       talvez até mesmo como uma forma de trazer “luz” e atenção ao grande desafio na
       implementação de métodos ágeis nas empresas, que tem sido amplamente relacionado
       às mudanças culturais que acontecem.


              Como toda mudança cultural, a responsabilidade primária pela mudança,
       começa nas pessoas, “as pessoas” são os agentes da mudança que querem “ver” nas suas
       organizações, não existem outros “organismos” nas organizações capazes de fazer a
       mudança acontecer, só as “pessoas” envolvidas podem fazer isso, e os 5 valores vem
       neste sentido. Vejamos como cada um dos 5 valores Scrum se encaixa em nosso dia-a-
       dia:


                             Comprometimento: ou você tem o compromisso pessoal com a
              meta de usar e beneficiar sua empresa e por consequência você com o uso do
              Scrum ou; você contribui com o assunto quando requerido. Fazendo uma
              analogia com a preparação de ovos mexidos com bacon para o café da manhã
              da fazenda, comprometido está o porco que dá o seu próprio corpo para gerar
              o bacon enquanto a galinha contribui botando ovos. “Nós podemos fazer isso
              na nossa equipe também” VS “Depois me conta com foi aí? Se precisar de algo
              me fala, Ok?”
                             Coragem: bom, depois da explicação do café da manhã com
              ovos mexidos com bacon, talvez tenha ficado claro que você precisa ter



                                              31


[PAGINA 32]
32   Agilidade nas empresas. Guia Scrum para quem não é de TI.


                  coragem para assumir uma postura de comprometimento, precisa ter coragem
                  para correr riscos e até sair da sua zona de conforto “quentinha” e agir no frio
                  da experimentação. “Vamos combinar uma duração de 3 semanas e começar a
                  repetir isso algumas vezes até sabermos se foi o melhor time-box para nós e
                  compartilharmos com os demais times os resultados” VS “Depois de definido
                  corporativamente vamos analisar a aplicabilidade ao nosso cenário”.
                                 Foco: como dito anteriormente que o Scrum é fácil de entender
                  e difícil de praticar, é preciso ter foco para fazer ao menos uma coisa diferente
                  de cada vez, poder conscientizar-se da mudança, dos benefícios intermediários e
                  então incorporar novas práticas, como novos hábitos. “Nós temos feito reuniões
                  diárias sobre o trabalho em andamento e todos estão mais cientes de tudo,
                  depois começamos a colocar a informação visível para todos, isto tem
                  melhorado a comunicação entre as pessoas, o fato de sempre terminarmos algo
                  concreto em tempos determinados, tem dado um senso de ritmo para o time”
                  VS “São tantas coisas novas a fazer que não sei por onde começo”, “Melhor
                  não mexer agora”.
                                 Abertura: bom, de novo, por isso que os valores são um bloco
                  de 5 mudanças, se você não estiver aberto a mudanças, aberto a fazer pequenas
                  mudanças na sua rotina e incorporar o pensamento de que melhoria contínua é
                  possível e que você está aberto a isso, você continuará parado, fixo e talvez
                  defendendo um status-quo – que talvez você não tenha mais. “Eu tenho feito as
                  minhas tarefas usuais A, B e C e reportado o progresso num mapa na parede
                  do meu lado para que todos possam acompanhar a minha fila de trabalho” VS
                  “Prefiro ver os resultados de alguns testes antes de começar a mudar”.
                                 Respeito: de modo similar, permita entender que mesmo você
                  estando comprometido, focado e corajosamente aberto a aprender novas
                  práticas, nem todas as pessoas ao seu redor, no seu círculo de relacionamento
                  poderão estar no mesmo nível de aceitação à mudança, mesmo você entendendo
                  e “comprando ou fazendo buy-in” dos benefícios da mudança. Portanto, vale
                  entende-las, respeitá-las e ajudá-las e ver também elas o benefício, bem como
                  meios de fazer a transição para métodos ágeis também do ponto de vista desta
                  outra pessoa. “Vou compartilhar os benefícios que eu estou tendo com os
                  demais como forma de exemplo e deixar que eles percebam, do ponto de vista
                  deles, que é possível mudar e melhorar também” VS “Vou demonstrar os meus
                  resultados para forçar que os outros mostrem os deles também”.


[PAGINA 33]
                                                                                 O time Scrum    33



       O time Scrum

       O time Scrum é composto de um Product Owner – o dono do Produto, do time
de Desenvolvimento e de um Scrum Master – o mestre Scrum. Times Scrum são auto
organizáveis e multifuncionais. Times auto organizáveis escolhem qual a melhor forma
para completar o seu trabalho, ao invés de serem dirigidos por outros de fora do time.
Times multifuncionais possuem todas as competências necessárias para completar o
trabalho sem depender de outros que não fazem parte do time. O modelo de time no
Scrum é projetado para aperfeiçoar a flexibilidade, a criatividade e a produtividade das
pessoas.

               Os papéis de Dono de Produto e Scrum Master serão explicados
       individualmente, então vamos nesta parte direto ao ponto central da auto-organização e
       multifuncionalidade dos times Scrum, pois é onde reside uma ruptura grande de
       modelos, entre a estrutura de comando e controle - de certo modo relativamente mais
       comumente conhecida e utilizada em múltiplas indústrias, e entre a estrutura de auto-
       organização. Para falar destes dois paradigmas mas com outras palavras – tire você
       também as suas próprias conclusões, vamos recorrer à um trabalho da década de 50 do
       professor e economista Americano Douglas McGregor intitulado Aspectos Humanos na
       Empresa.

               MgGregor escreveu sobre as Teorias X e Y, dois conceitos antagônicos que
       norteiam as relações entre as empresas e os trabalhadores, tratando dois perfis de
       personalidade e comportamento de funcionários, que muitas vezes os próprios
       indivíduos não percebem que possuem. Em uma das teorias o funcionário é relaxado,
       preguiçoso e gosta pouco de trabalhar, precisando de comando e controle. Já na outra, o
       funcionário gosta de responsabilidade e a busca ele mesmo dentro da empresa.

               Se você já conhece as Teorias X e Y de McGregor não perca seu tempo e vá
       direto à conclusão.




                                             33


[PAGINA 34]
34       Agilidade nas empresas. Guia Scrum para quem não é de TI.




                                          Figura 4 – Teorias X e Y

                       -/ -/ -/

                       Teoria X – “O trabalho é em si mesmo desagradável para a maioria das
               pessoas”

                       Nesta teoria, chamada por McGregor de “Hipótese da mediocridade das
               massas”, parte-se do pressuposto de que os trabalhadores possuem aversão nata à
               responsabilidade e às tarefas do trabalho, necessitando sempre de ordens superiores para
               render no trabalho. Ordens acompanhadas de punição, elogios, dinheiro, coação, etc.;
               artifícios utilizados pelos gestores para tentar gerar um empenho maior do colaborador.

                       McGregor acreditava que as necessidades de ordem inferior6 dominavam as
               pessoas nesta Teoria. Assim, as organizações precisavam colocar a ênfase de sua gestão
               na satisfação dos fatores higiênicos dos trabalhadores, estudados na Teoria dos Dois
               Fatores de Herzberg.

                       Os princípios básicos da Teoria X são:




     6
       Lembrar que necessidades de ordem inferior do Herzberg não significam serem menos importantes,
     sig ifi a àse e à e osàdu adou asàeàai daàexte asà àpessoa,à e essita doàout oàestí uloà exte o à
     logo para continuar motivado – geram dependência; enquanto que necessidades superiores na escala
     de Herzberg, significam motivações mais próprias ou internas à pessoa, mais duradouras e mais auto
     motivadoras independentemente de outros estímulos externos – gerem independência.


[PAGINA 35]
                                                                         O time Scrum    35


               Um indivíduo comum, em situações comuns, evitará sempre que
possível o trabalho;
               Alguns indivíduos só trabalham sob forte pressão. Eles precisam ser
forçados, controlados e às vezes ameaçados com punições severas para que se esforcem
em cumprir os objetivos estabelecidos pela organização;
               O ser humano ordinário é preguiçoso e prefere ser dirigido, evita as
responsabilidades, tem ambições e, acima de tudo, deseja sua própria segurança.



        Teoria Y – “O trabalho é tão natural como o lazer, se as condições forem
favoráveis”.

        Nesta teoria a coisa muda de figura. Aqui os trabalhadores são encarados como
pessoas altamente competentes, responsáveis e criativas, que gostam de trabalhar e o
fazem como diversão. Sendo necessário que as empresas proporcionem meios para que
estas pessoas possam dar o seu melhor, com mais desafios, participações e influências
na tomada de decisão. McGregor acreditava que as necessidades de ordem superior
dominavam as pessoas nesta Teoria.

        Os princípios básicos da Teoria Y são:

               O esforço físico e mental empregado no trabalho é tão natural quanto o
empregado em momentos de lazer
               O atingimento dos objetivos da organização está ligado às recompensas
associadas e não ao controle rígido e às punições;
               O indivíduo comum não só aceita a responsabilidade do trabalho, como
também a procura;
               Os indivíduos são criativos e inventivos, buscam sempre a solução para
os problemas da empresa;
               Os trabalhadores tem a capacidade de se auto gerirem nas tarefas que
visam atingir objetivos pessoais e estratégicos da organização. Sem a necessidade de
ameaças ou punições;
               O trabalhador normalmente não faz aquilo que não acredita. Por isso
exige cada vez mais benefícios para compensar o incômodo de desempenhar uma
função desagradável.

        Desta forma, podemos perceber que na Teoria X o indivíduo é motivado pelo
menor esforço, demandando um acompanhamento maior por parte do líder. Já na Teoria




                                      35


[PAGINA 36]
36       Agilidade nas empresas. Guia Scrum para quem não é de TI.


               Y, as pessoas são motivadas pelo máximo esforço, demandando uma participação maior
               nas decisões e negociações inerentes ao seu trabalho.

                       -/ -/ -/ fim da citação

                       Ou seja, voltando ao nosso tema, o paralelo feito aqui é entre métodos
               tradicionais de comando e controle e pessoas do tipo X e, entre métodos Ágeis como o
               Scrum de times auto organizáveis e multifuncionais e pessoas do tipo Y. Suspendendo o
               julgamento se um modelo é melhor que o outro, o fato que temos é que são padrões
               distintos.

                       É importante destacar do texto acima sobre as teorias X e Y de McGregor,
               somados aos Dois Fatores de Herzberg, que estes são perfis comportamentais pessoais e
               individuais, que muitas vezes nós nem sabemos que temos. Portanto, sem a
               oportunidade de se examinar e de conhecer a si próprio, podem vir grandes problemas
               com as grandes responsabilidades de usar Scrum nos nossos times.

                       Imagine quanto de conflito existirá num cenário de um gestor do tipo X (as
               pessoas precisam ser controladas) que tenha um time de pessoas todas Y praticando
               Scrum! O time supostamente vai adotar as novas responsabilidades e vai buscar acelerar
               em produtividade. Mas, como será que ficará o gestor controlador com um time Y em
               um ambiente que proporciona ser auto gerenciável?

                       Num cenário inverso, como será um time de pessoas X (o trabalho é
               desagradável e precisa ser evitado) que agora se vê diante do contexto de ter de ser
               auto gerenciável e ter de buscar meios por sí próprio de atingir as metas da empresa, do
               time e pessoais, sem estímulos forçados de comando e controle para os quais estavam,
               eventualmente, até habituados.

                       Novamente, independentemente do juízo de valor sobre os padrões de
               comportamentos X e Y, o fato é que nós os temos. Algumas pessoas são mais
               destacadas num deles, outras flutuam entre X e Y de acordo com o ambiente, a
               necessidade e a conveniência. Outras pessoas podem não saber como são, como atuam.
               É importante saber que estes padrões comportamentais existem e vão influenciar você e
               o time nas suas ações diárias, muitas vezes sem você perceber7.

                       Adicionalmente, este parágrafo do Guia do Scrum também fala de o time Scrum
               ser multifuncional, o que também pode ser uma ruptura das estruturas hierárquicas
               tradicionalmente agrupadas por função e isolada em silos, com interações definidas

     7
      Há uma frase atri uídaàaàCa làGustavàJu gà ueàdiz,à át àvo àseàto a à o s ie te,àoàseuài o s ie teà
     vaiàdi igi àsuaàvidaàeàvo àvaià ha a àissoàdeàdesti o .àE tão,àestude-se.


[PAGINA 37]
                                                                           O time Scrum     37


através de processos de acione (abertura de chamados, tickets, demandas, acordos de
níveis de serviço, etc).

        Segundo o Guia, um time Scrum é multifuncional e possui ‘dentro’ do time,
toda a competência necessária para completar o trabalho e entregar o produto final ao
dono do produto, sem depender de outras pessoas, outros times ou áreas que não façam
parte do time.

        Este passo da multifuncionalidade é um desafio para que as empresas passem a
utilizar-se dos benefícios do Scrum, onde profissionais especialistas de times funcionais
diferentes, tem de deixar os seus ‘silos’ e juntar-se a outras ‘pessoas’ (de tipos X e Y
misturados e desconhecidos), para realizar tarefas não somente as relacionadas à sua
função ‘origem’, deixando talvez a zona de conforto onde estava, para ‘pisar’ num local
fora do conforto habitual, um local lá fora, onde ocorre a aprendizagem e o
desenvolvimento pessoal.

        Um exemplo de multifuncionalidade que vem ocorrendo na prática e de forma
cada vez mais frequente nas empresas –e eu não vou me aprofundar demais neste
‘parêntesis’ para ser coerente com o público não Tecnologia, é a organização do time de
TI (Tecnologia da Informação) de forma conjunta entre desenvolvimento de sistemas e
operações da infraestrutura (Development & Operations).

        Por décadas estas 2 áreas das organizações de TI trabalham seguindo estratégias
distintas e de certo modo conflitantes. Development tem normalmente 2 objetivos
primários de manter os serviços de TI em produção, mas principalmente, desenvolver
novos serviços de TI alterando os atuais em resposta às necessidades das áreas de
negócios ou suporte que demandam serviços. A estratégia de Dev, é que quanto mais
rápido puder mudar para atender a operação, melhor. Operations trabalha habitualmente
sobre a ótica de manter em operação o que está em produção. A estratégia de Ops é que
quanto menos mudar e mais estável ficar, melhor.

        Em linhas gerais, você deve ter percebido o conflito das 2 estratégias entre
mudar e manter. Um pilar de agilidade que vem auxiliar no carácter de equipes
multifuncionais, é o fato de um número crescente de empresas estar adotando uma
estratégia denominada DevOps (significando Development and Operations juntos).
Onde um time com pessoas oriundas de funções de Desenvolvimento de Sistemas e
também de Operações da Infraestrutura de TI, trabalham juntas num time único para
entregar o trabalho necessário.




                                       37


[PAGINA 38]
38    Agilidade nas empresas. Guia Scrum para quem não é de TI.


                    Fechando o parêntesis do exemplo de DevOps, citei somente para exemplificar
            a você que times multifuncionais vão trazer também mudanças nas estruturas
            organizacionais e como tal, precisarão ocorrer com alinhamento estratégico e apoio da
            alta direção. Não será suficiente que os profissionais estejam corajosamente
            comprometidos em trabalhar de um modo novo, se a direção da empresa não estiver
            aberta a patrocinar uma estrutura diferente, mais enxuta.

                    Depois de um longo trecho, voltemos ao Guia.

            Times Scrum entregam produtos de forma iterativa e incremental, maximizando
     as oportunidades para aprender com a experiência. Entregas incrementais de
     produtos “Prontos” garantem que uma versão potencialmente funcional do produto
     esteja sempre disponível.

                    Adicionalmente às equipes serem auto gerenciáveis e terem múltiplas
            capacidades, o fato de times Scrum trabalharem em Sprints (períodos determinados de
            tempo – time-box), faz com o que os produtos resultantes do seu trabalho sejam
            entregues de forma incremental (aos pedaços, em versões intermediárias com as
            funcionalidades mais importantes primeiro), seguido de entregas posteriores de outras
            versões mais evoluídas e com mais funcionalidades.

                    Retorna neste parágrafo do Guia, o carácter empírico do Scrum, de aprender
            com a experiência, ou seja, entregar algo completo o suficiente mas já pronto para uso e
            aprender com o feedback de quem passou a utilizar as primeiras funcionalidades,
            melhorando a chance de assertividade das próximas entregas.

                    Importante destacar também o objetivo de ter sempre algo “potencialmente
            funcional que esteja sempre disponível” citado no Guia, o que me remete ao ambiente
            de negócios citado na introdução do livro, de que os Serviços acabam sendo tão ou até
            mais importantes que os Produtos.

                    Dizem que o Gmail, serviço de e-mails grátis do Google, ficou anos – talvez
            esteja até hoje, em versões beta (de testes), sempre “potencialmente funcional” e sempre
            “disponível e pronto”.

                    Há uma lógica desencadeada pelo Scrum: um produto potencialmente funcional
            (já despertando o interesse através das funcionalidades mais importantes entregues
            primeiro), sempre disponível (à disposição para ser usado e receber feedback por isto),
            evoluído de forma incremental (constantemente recebendo novos investimentos em


[PAGINA 39]
                                                                                       O time Scrum     39


        importantes funcionalidades) e iterativa (que aprende a partir do feedback recebido de
        quem já está usando e obtendo benefício e retorno financeiro8).

                 O time Scrum é então responsável por seguir entregando em tempos pré-
        determinados (Sprints time-box) evoluções funcionais cada vez maiores do produto e
        com mais velocidade, sempre em acordo com o principal responsável por direcionar o
        rumo do produto, o dono do produto.




8
  Isto me lembra do movimento feito pelo Google criando a sua holding Alphabet, tendo como
significado a mais pura gestão de portfólio, onde Alpha significa o investimento de melhor retorno de
uma carteira e Bet significa aposta. Eles apostam alto. Veja mais em http://abc.xyz



                                                 39


[PAGINA 40]
40    Agilidade nas empresas. Guia Scrum para quem não é de TI.



            O Product Owner

            O Product Owner – o Dono do Produto, é responsável por maximizar o valor do
     produto e do trabalho do time de desenvolvimento. A forma como isso é feito pode
     variar amplamente através das organizações, dos times Scrum e dos indivíduos.

                    Vamos pensar num ‘serviço de ingressos online para sessões de cinema’ onde
            as pessoas gostariam da comodidade de poder apresentar seus ingressos através de um
            App nos seus próprios celulares. Em termos de rentabilidade para a rede de cinemas,
            não vai adiantar muito o time Scrum entregar uma solução impecável de impressão de
            tickets em papel com cores vibrantes, etc, etc. Se, o interesse do público era ter um
            simples ticket no celular que possa ser carregado no bolso e apresentado para ingressar
            no cinema, lido através de um QR Code.

                    Neste cenário, entregar uma solução correta, rápida, estável e confiável de
            tickets é responsabilidade do time Scrum e seu Scrum Master, mas é responsabilidade
            primordial do Dono do Produto que a solução seja amplamente percebida pelos
            visitantes do cinema como útil e valiosa a estes, que a solução seja mais um dos
            diferenciais da rede de cinemas e que a solução possa contribuir ativamente em ajudar
            os clientes a optar por uma rede de cinemas em detrimento de outras redes, na hora da
            sua atividade de lazer. Pode ser uma decisão até subliminar e imperceptível para o
            cliente, mas pode ajudar a fazer diferença para a rentabilidade da rede de cinemas.
            Maximizar o retorno sobre os investimentos da rede de cinemas em tecnologia, é
            responsabilidade do Dono do Produto. Papéis distintos, responsabilidades claras.

            O Dono do Produto, é a única pessoa responsável por gerenciar o Backlog do
     Produto. O gerenciamento do Backlog do Produto inclui:


                           Expressar claramente os itens do Backlog do Produto;
                           Ordenar os itens do Backlog do Produto para alcançar melhor as
            metas e missões;
                           Otimizar o valor do trabalho realizado pelo time de
            Desenvolvimento;
                           Garantir que o Backlog do Produto seja visível, transparente,
            claro para todos e que mostra no que o time Scrum vai trabalhar a seguir; e
                           Garantir que o time de Desenvolvimento entenda os itens do
            Backlog do Produto no nível necessário de detalhe.


[PAGINA 41]
                                                                               O Product Owner       41


                  Como foi dito no Glossário, backlog é uma lista de ‘coisas a fazer’. No caso,
          uma lista de coisas novas que o Produto ou o Serviço do qual o Dono do Produto é
          responsável precisará fazer em algum momento no tempo, breve ou mais à frente. O
          Dono do Produto pode utilizar-se de várias ferramentas para chegar às definições de o
          que é esperado do Produto ou Serviço. Desde pesquisas de mercado, focus groups,
          legislação, benchmark e até mesmo sua intuição pessoal.

                  É importante o Dono do Produto preocupar-se com a clareza da comunicação
          que está fazendo ao time de desenvolvimento9.


                  Para obter o máximo valor do investimento feito com o time de
          desenvolvimento, é importante que os itens de backlog do produto sejam priorizados
          com a mais alta prioridade dada para os itens que mais trazem resultados para os
          usuários do produto ou serviço. O dono do produto precisar deixar claro para o time de
          desenvolvimento que devemos definir em detalhes agora para um certo time-box, uma
          Sprint, uma Iteração próxima de começar, um item de backlog do produto, de um jeito
          que seja minimamente viável para iniciar o uso assim que estiver pronto mas; que há
          uma linha de evolução clara para novos itens e também evoluções dos itens já
          entregues.

                  Um suposto “serviço de locomoção diária individual e uso compartilhado em
          grandes cidades”, pode começar com um skate compartilhado entre amigos, uma
          agenda unificada para fazer as reservas, passar por bikes disponíveis em
          estacionamentos próximos de estações do Metrô, expandir-se para uso de carros
          compartilhados retirados e entregues em postos similares e chegar a carros autônomos,
          solicitados via App no celular que te recebem e te deixam nos locais solicitados
          enquanto você lê, descansa, se alimenta, etc.


          O Dono do Produto, deve fazer o trabalho acima, ou delegar para o time de
Desenvolvimento fazê-lo. No entanto, o Dono do Produto continua sendo o
responsável pelos trabalhos.




9
    Há uma regra na comunicação de que a responsabilidade sobre o entendimento correto da mensagem
    àdoà e isso ,àok?



                                                41


[PAGINA 42]
42    Agilidade nas empresas. Guia Scrum para quem não é de TI.




                                   Figura 5 – O Product Owner (PO)

                    Diferentemente da figura acima, o Dono do Produto / Product Owner (PO), não
            precisa ter “superpoderes” e fazer todo o trabalho, mas ele precisa ter “superpoderes” e
            usar todas as suas habilidades de trabalho em equipe e trabalho colaborativo com o
            Time Scrum, pois no bottom line, ele é o responsável pela rentabilidade do produto.

                    Brincadeiras à parte, o Dono do Produto trabalha mesmo muito, pois ele tem de
            estar junto ao time Scrum sempre que requerido pelo time, esclarecendo algo e
            refinando algum conceito e precisa também estar trabalhando nos próximos passos que
            virão, trabalhando sempre que necessário e factível no backlog do Produto.

            O Dono do Produto, é uma pessoa, não um comitê. O Dono do Produto pode
     representar os desejos de um comitê no Backlog do Produto, mas aqueles que
     quiserem uma alteração nas prioridades dos itens de Backlog, devem convencer o
     Dono do Produto.

            Para que o Dono do Produto tenha sucesso, toda a organização deve respeitar
     as suas decisões. As decisões do Dono do Produto, são visíveis no conteúdo e na
     prioridade do Backlog do Produto. Ninguém tem permissão para falar com o time de
     Desenvolvimento sobre diferentes configurações de requisitos, e o time de
     Desenvolvimento não tem permissão de agir sobre o que outras pessoas disserem –
     que não o Dono do Produto.

                    Importante esta questão de que o PO é uma pessoa, não um comitê. E
            continuará sendo comum o Dono do Produto precisar de ‘n’ pessoas e até ‘n’ comitês
            para obter aprovações para suas ideias de novos produtos e as suas evoluções. Mas,


[PAGINA 43]
                                                                                 O Product Owner        43


        cumprido estas atividades do Dono do Produto como sendo um proxy, um
        representante, de comitês internos, focus groups, pesquisas públicas e de mercado,
        aprovações junto a órgãos reguladores e qualquer outra atividade de gestão de
        stakeholders (pessoas interessadas) que continua sendo necessária ser feita, o Dono do
        Produto é a fonte da verdade para o time Scrum. Se o Dono do Produto seguiu todos os
        passos corporativos e regulamentares para aprovar uma ideia ou, se o Dono do Produto
        teve um insight e passou a ideia direto para o time de Scrum, por sua conta e risco,
        valerá para o time Scrum a definição do Dono do Produto. Faz parte do
        empoderamento ser assim10.

                O time de desenvolvimento Scrum tem a obrigação de fazer o seu trabalho
        alinhado com as decisões do Dono do Produto. O Dono do Produto tem a obrigação de
        fazer o melhor uso possível da força de trabalho do time de desenvolvimento Scrum e
        de fazer o seu trabalho alinhado com as demais partes interessadas interna e
        externamente à organização. Novamente, papéis distintos, responsabilidades claras.




10
  J àdiziaàoà“upe àHe ói,à ueà com grandes poderes vem grandes responsabilidades ,àpoisàoàpapelàdoà
time de Desenvolvimento é entregar certo, rápido e mais. O Dono do Produto precisa saber o que pedir.



                                                43


[PAGINA 44]
44    Agilidade nas empresas. Guia Scrum para quem não é de TI.



            O Time de Desenvolvimento

            O Time de Desenvolvimento consiste de profissionais que realizam o trabalho
     de entregar uma versão potencialmente utilizável, incrementando o produto “Pronto”
     ao final de cada Sprint. Somente os integrantes do time de desenvolvimento criam
     incrementos de produto.

                    O time de desenvolvimento é quem executa o trabalho que produz uma ‘versão
            potencialmente utilizável de um novo incremento de produto pronto’. Nossa, quantos
            termos e conceitos, vamos por partes.

                    Como o objetivo é que o time seja multifuncional (lembra-se?), durante uma
            Sprint, ele produz uma parte com início, meio e fim do produto esperado, de modo que
            esta entrega possa ser utilizável por quem o Dono do Produto representa.

                    Como uma meta a alcançar, as entregas de produtos intermediários realizadas
            Sprint a Sprint, tem o objetivo de serem potencialmente utilizáveis. Pode acontecer de
            no espaço de tempo (padronizado, time-box) de 2 ou 3 Sprints – por exemplo, não ser
            possível produzir-se algo ‘efetivamente’ utilizável na forma de um produto final
            comercializável – por exemplo. Esta, ‘falha semântica’ digamos, não invalida a lógica
            maior de fazer entregas parciais, recorrentes, validadas de forma incremental (cada vez
            com mais funcionalidades consideradas ‘prontas para uso’) e ‘ir juntando’
            funcionalidades até que uma ‘versão maior’ seja efetivamente liberada para uso público.

                    Por ‘ir juntando funcionalidades’ você pode entender, e esperar também, que as
            entregas das primeiras Sprints de um trabalho possam ser itens mais relacionados a
            infraestrutura e a arquitetura da solução, como forma de alicerce sobre o qual será
            formado um produto com ‘n’ funcionalidades que interessam ao Dono do Produto.

                    Outra possibilidade de ‘ir juntando funcionalidades’ é quando a empresa tem
            uma visão clara de administração dos seus serviços por processos, com passos de
            oferecimento, originação / iniciação, processamento / efetivação, finalização /
            liquidação, controles e contabilizações. Talvez uma entrega inicial de um serviço possa
            atender ao passo de oferecimento, mas não permita iniciar negócios – o que pode ser ou
            frustrante para o cliente ou deixá-lo motivado a conhecer mais do serviços e vir a
            contratá-lo. Assim como pode ser um desafio para o Dono do Produto ter uma
            funcionalidade que inicie negócios mas que não os processe, liquide e contabilize de
            forma automática. Em qualquer uma das situações, o Dono do Produto precisa de uma
            visão dos Processos de Negócios e das Operações que estão consumindo o serviço, para


[PAGINA 45]
                                                                 O Time de Desenvolvimento       45


       tomar decisões sobre qual é o produto que é minimamente viável, já traz exposição ao
       mercado e resultados, com riscos controlados para a operação do negócio.

               Há também outra razão de ‘ir juntando funcionalidades’ mas vamos explorar lá
       no trecho de cancelamento de Sprint.

       Os times de Desenvolvimento são estruturados e autorizados pela organização
para organizar e gerenciar o seu próprio trabalho. A sinergia resultante otimiza a
eficiência e a eficácia do time de Desenvolvimento como um todo.

       Os times de Desenvolvimento tem as seguintes características:

                      Eles são auto-organizados. Ninguém (nem mesmo o Scrum
       Master) diz ao time de Desenvolvimento como transformar o Backlog do
       Produto em um incremento de funcionalidade potencialmente utilizável;

               Importante esta parte de que é o time de desenvolvimento que faz o trabalho, é
       ele que transforma o Backlog do Produto em um incremento de funcionalidade
       utilizável. Importante entender estas duas ‘instancias de coisas’, sendo o ‘Backlog do
       Produto’ de responsabilidade do Dono do Produto e o ‘incremento de funcionalidade’
       de responsabilidade do time de desenvolvimento.


               O backlog do produto pode ser algo de alto nível, definido pelo dono em termos
       mesmo que genéricos e amplos, sejam claros e desafiadores. Exemplo (um shape de
       skate com desenho diferenciado do mercado que ajuda a manter os pés do skatista
       preso à prancha).

               O incremento de funcionalidade deve ser algo específico, definido e produzido
       pela equipe de desenvolvimento na forma de algo que possa ser efetivamente utilizável
       pelo Dono do produto ou, ainda, pelo público alvo almejado (uma prancha de madeira
       cortada no tamanho certo, de peso adequado para manuseio, com densidade forte o
       suficiente para resistir a torções e impactos de pessoas até 100 kilos, que proporcione
       bom grip ao praticante que vai usá-la pela parte superior e que proporcione fixação
       firme e duradoura do eixo na sua parte inferior).


               O Time de Desenvolvimento não deve eximir-se de detalhar o incremente, mas
       sim, agregar o seu valor de especialista.


                      Times de Desenvolvimento são multifuncionais, possuindo todas
       as habilidades necessárias enquanto time, para criar o incremento do Produto;



                                              45


[PAGINA 46]
46   Agilidade nas empresas. Guia Scrum para quem não é de TI.


                         O Scrum não reconhece títulos para os integrantes do time de
           Desenvolvimento que não seja o Desenvolvedor, independentemente do
           trabalho que está sendo realizado pela pessoa. No Scrum, não há exceções
           para esta regra;
                         O Scrum não reconhece sub-times no time de Desenvolvimento,
           independentemente de domínios que precisam ser endereçados tais como
           testes ou análise de negócios. No Scrum, não há exceções para esta regra, e;
                         Individualmente os integrantes do time de desenvolvimento
           podem ter habilidades especializadas e áreas de especialização, mas a
           responsabilidade pertence ao time de Desenvolvimento como um todo.

                   Acabamos já adiantando informação sobre o time de desenvolvimento nas
           partes que falamos de times auto organizados e multidisciplinares. Vale destacar aqui a
           importância da característica de ‘time’ (todos jogando juntos na mesma direção) e da
           condição de interdependência entre os integrantes para que a potencialização da
           produtividade e criatividade do time seja máxima. Novamente baseado em
           conhecimentos da teoria dos múltiplos canais de comunicação possíveis num grupo, o
           Guia Scrum irá preconizar times pequenos, vamos falar o porquê disto em detalhes.


[PAGINA 47]
                                                          O tamanho do Time de Desenvolvimento           47



           O tamanho do Time de Desenvolvimento

           O tamanho ideal do time de Desenvolvimento é pequeno o suficiente para
manter-se ágil e grande o suficiente para completar uma parcela significativa de
trabalho dentro de uma Sprint. Menos de 3 integrantes no time de Desenvolvimento
diminuem a interação e resultam em um menor ganho de produtividade. Times de
Desenvolvimento pequenos podem encontrar restrições de habilidades durante a
Sprint, gerando um time de Desenvolvimento incapaz de entregar um incremento
potencialmente utilizável. Havendo mais de nove integrantes é exigido muita
coordenação. Times de Desenvolvimento grandes geram muita complexidade para um
processo empírico gerenciar. Os papéis de Dono do Produto e Scrum Master não são
incluídos nesta contagem, a menos que eles também executem o trabalho do Backlog
da Sprint.

                   Ufa, vamos lá. ‘Pequeno o suficiente ... e grande o suficiente ...’ é para manter a
           comunicação mais ativa possível, essa é a preocupação do Guia. Vejamos:

                   Ponto 1) convenhamos, a chance de um par de pessoas conseguir ser
           multifuncional de modo a desenvolver algo do início até o fim e entregar um produto
           efetivamente pronto e operacional é pequena, pouco provável e até improdutivo, dado a
           necessidade de tantos papéis que temos hoje em dia, providos por somente 2 pessoas,
           por isso da recomendação (do entendimento) que na prática um time mínimo comece
           com ao menos 3 pessoas. Ponto 2) pode ser que 3 pessoas em múltiplos papéis vão
           gerar trabalho em uma velocidade inferior ao que poderia ser considerado um ritmo
           viável economicamente. Ponto 3) Seguindo a lei da natureza de que 9 mulheres não
           fazem a gestação de 1 criança em 1 mês, mesmo que fossem infinitos os recursos
           financeiros (R$) nas nossas empresas, a quantidade de recursos humanos não seria
           exatamente infinita, ainda; Ponto 4) onde o Guia Scrum quer chegar com um número
           mágico para o tamanho do time?


                   O que há por trás deste alerta de que quanto mais pessoas, maior a dificuldade
           de coordenação11?


           - Valor do Manifesto Ágil que diz “interação entre pessoas sobre processos e
           ferramentas”;
           - Princípio do Manifesto Ágil que diz “o método mais eficiente e eficaz de transmitir

11
     Você tem o hábito de participar de assembleias de condomínio? Faça um paralelo.



                                                   47


[PAGINA 48]
48    Agilidade nas empresas. Guia Scrum para quem não é de TI.


            informação é a conversa face-a-face”;
            - Regra da teoria da comunicação que diz que o número de canais de comunicação
            cresce conforme o grupo aumenta, entre 3 pessoas – por exemplo, há 3 canais de
            comunicação, 4 pessoas são 6 canais, 5 pessoas 10 canais, 6 são 15, 7/21, 8/28, 9/36 e
            10/45.

                     Em resumo, quanto mais pessoas juntas, mais difícil é manter a comunicação
             boa com tantos canais possíveis de a comunicação se estabelecer. A confusão aumenta e
             a produtividade que havia atingido um patamar ideal com um time menor do que 10
             pessoas, cai.


             A maioria das recomendações é de que os times Scrum tenham de 3 a 5 pessoas, o
     importante a considerar é que poucas pessoas vão produzir pouco trabalho e muitas pessoas
     juntas vão dificultar a comunicação. Caberá ao Scrum Master encontrar o equilíbrio entre a
     quantidade de pessoas e a velocidade de produção.


[PAGINA 49]
                                                                            O Scrum Master      49



       O Scrum Master

       O Scrum Master é responsável por garantir que o Scrum seja entendido e
aplicado. O Scrum Master faz isto para garantir que o time Scrum aderiu às teorias,
práticas e regras do Scrum.

       O Scrum Master é um líder servidor para o time Scrum. O Scrum Master ajuda
que está fora do time Scrum a entender quais das suas interações com o time Scrum
são úteis e quais não são. O Scrum Master ajuda todos a mudar estas interações para
maximizar o valor criado pelo time Scrum.

              O Scrum Master é o profissional responsável por fazer com que este framework
       de gestão ágil chamado Scrum seja entendido e praticado no dia a dia das organizações.
       Em seu(s) time(s) Scrum, numa área, numa empresa, num mercado. É um profissional
       que tem um papel de ser um apoiador para que os outros papéis executem bem as suas
       próprias responsabilidades. É um resolvedor de problemas e um otimizador de pessoas e
       processos em benefício da organização. Bom, não é alguém do tipo X (lembra-se?). Não
       é alguém de TI. Não é aplicável somente a TI. Vamos voltar à este tema ao falar do
       planejamento da Sprint.




       O Scrum Master servindo ao Product Owner

       O Scrum Master serve ao Dono do Produto de várias maneiras, incluindo:

                     Encontrando técnicas para um efetivo gerenciamento do Backlog
       do Produto;
                     Ajudando o time Scrum a entender a necessidade de Backlogs
       de Produto claros e concisos;
                     Entendendo o planejamento de produto em um ambiente
       empírico;
                     Garantindo que o Dono do Produto sabe como organizar o
       Backlog do Produto de forma a maximizar o valor;
                     Entendendo e praticando agilidade; e,
                     Facilitando os eventos Scrum quando requerido ou necessário.

              Resumindo, aquela pessoa da ‘capa’:




                                            49


[PAGINA 50]
50   Agilidade nas empresas. Guia Scrum para quem não é de TI.




                                     Figura 06 – Scrum Master (SM)

                   São mesmos tantas atribuições do Scrum Master que ele(a) precisa mesmo ser
           alguém do tipo Y para não entrar em pânico com tantos desafios!


                   Se o Dono do Produto não está conseguindo chegar a termo com um Product
           Backlog, tem que auxiliá-lo com técnicas que possam fazer com que o PO chegue à
           boas decisões e que estas decisões possam agregar valor, ou então pode ‘faltar tijolo na
           obra’, faltar o que o time fazer.


                   Se o time não entende os Product Backlogs do PO, podemos ter itens não
           aceitos como “prontos”, gerando retrabalho, menor produtividade, confusão,
           desperdício e desgaste.


[PAGINA 51]
                                                                                   O Scrum Master       51


                 Se não há como demonstrar planos de como estamos indo e para onde estamos
        indo (gráficos de Burn Down e Burn Up – por exemplo, lembra-se?). Com qual
        informação a organização será comunicada? Como ficará a transparência?

                 Se a Agilidade não é praticada pelo Scrum Master para servir de exemplo, então
        como ficará a relação de confiança com o Dono do Produto e o time Scrum? Só no
        discurso? Produtiva12?




        Scrum Master servindo ao Time de Desenvolvimento

        O Scrum Master serve ao time de Desenvolvimento de várias maneiras,
incluindo:


                        Treinando o time de Desenvolvimento em auto-organização e
        interdisciplinaridade;
                        Ajudando o time de Desenvolvimento a criar produtos de alto
        valor;
                        Removendo impedimentos ao progresso do time de
        Desenvolvimento;
                        Facilitando os eventos Scrum quando requerido ou necessário;
        e,
                        Treinando o time de Desenvolvimento em ambientes
        organizacionais nos quais Scrum não é totalmente adotado e entendido.

                 Ser ‘Master’ no Scrum me arrisco a dizer que em Japonês13 poderíamos chamar
        de Sensei (pois é um título honroso para tratar com respeito um professor ou mestre).
        Em Inglês fica mais fácil contextualizar como Coach (um treinador ou instrutor).


                 Independente da nomenclatura, a questão é que ele tem de ser um facilitador do
        time, um técnico, um treinador, um mestre nos métodos Ágeis para que a prática do
        time Scrum, e na empresa especificamente, possa confirmar a teoria e trazer agilidade
        para a organização.



12
   Você sabe que a confiança é um acelerador nas negociações não sabe? Você se recorda de situações
onde negociou a manutenção do seu carro ou da sua casa com profissionais nos quais você tinha total
confiança e com profissionais nos quais você não podia confiar? Qual foi o seu nível de controle e de
stress nestes 2 contextos?
13
   Definições em www.significados.com.br/sensei e www.significados.com.br/coach



                                                 51


[PAGINA 52]
52        Agilidade nas empresas. Guia Scrum para quem não é de TI.


                        É responsabilidade do Scrum Master fazer o time ser cada vez mais rápido,
                produtivo, de alta performance à cada nova Sprint. Motivos para enxergar
                impedimentos à performance e a excelência, muitos terão nos times, mas compete ao
                Scrum Master auxiliar o time a remover os impedimentos, otimizando e acelerando a
                performance do time14.

                        Com a atuação na ponta Dono do Produto o Scrum Master ajuda o Dono do
                Produto a gerar itens de backlog do produto que vão agregar valor. Com a atuação na
                ponta Time Scrum o Scrum Master ajuda o time a gerar os incrementos de produto de
                modo eficiente. A soma das duas atuações gera eficácia e traz resultados para a
                organização.


                        Bom, fechando o assunto time, há um pensamento que diz que “um time não é
                um grupo de pessoas que trabalham juntas, é um grupo de pessoas que confiam uns nos
                outros” – então só mesmo sendo um ‘sensei coach’.




     14
       Out aàalusãoàta      ,à à ueàoà“ u àMaste à àalgu à ueàpassouàaàatua à o oà age te àdeà
     t a sfo açãoàeàsaiuàdoàg upoà aàge te àdaà e la ação. Ser Scrum Master é ser alguém que decidiu ser
     parte da Solução, não do Problema.


[PAGINA 53]
                                                                      O Scrum Master     53



Scrum Master servindo à Organização

O Scrum Master serve à organização de várias maneiras, incluindo:

               Liderando e treinando a organização na sua própria adoção de
Scrum;
               Planejando implementações Scrum dentro da organização;
               Ajudando empregados e stakeholders entender e tornar aplicável
o Scrum e o desenvolvimento empírico de produtos;
               Causando mudanças que aumentam a produtividade do time
Scrum; e,
               Trabalhando com outros Scrum Masters para aumentar a
eficácia da aplicação do Scrum nas organizações.

         Retomando a ideia da ‘pessoa da capa’, e extrapolando a atuação em ‘um’ time
Scrum, o Scrum Master deve ser alguém com vontade de liderar a organização na
adoção do Scrum, primeiro em iniciativas isoladas para dar resultados práticos e
concretos que serão usados como motivadores para os céticos obterem resultados
maiores, depois planejando expansões de adoção do Scrum em um maior número de
times agora já baseado no conhecimento empírico (lembra-se) adquirido na própria
organização, com as próprias pessoas envolvidas, demonstrando quanto de aumento de
produtividade estão tendo os times que já fizeram o movimento de transição e
trabalhando com outros Scrum Masters da empresa para reutilizar as lições e acelerar
novas adoções na organização.

         O Scrum Master (a pessoa da capa) é um agente de mudanças e de promoção de
melhoria contínua, não no estilo ‘grandes rupturas’ (a partir de hoje somos Ágeis) mas
no estilo Kaizen de melhoria contínua. O importante é demonstrar objetivamente
benefício e retornos tangíveis, para que o suporte à iniciativa de Agilidade do Scrum
somente seja reforçada pela administração sênior, e não fique num discurso bonito mas
subjetivo.


         Alguns profissionais que atuam como Scrum Masters com a experiência
adquirida, acabam atuando também como Agile Coaches e Agile Trainers, em ações de
treinamento de novos times Scrum e no acompanhamento da evolução de pessoas nos
papeís de Scrum Master, Donos de Produtos, time Scrum, DevOps, automações de
testes, build e deploy de sistemas – por exemplo.




                                      53


[PAGINA 54]
54   Agilidade nas empresas. Guia Scrum para quem não é de TI.


[PAGINA 55]
                                                                                Eventos Scrum    55



       Eventos Scrum

       Eventos prescritos são usados no Scrum para criar regularidade e para
minimizar a necessidade de reuniões não definidas no Scrum. Todos os eventos são
eventos time-box, de tal modo que todo evento tem uma duração máxima. Uma vez
que a Sprint começa, sua duração é determinada e fixa e não pode ser reduzida ou
aumentada. Os eventos restantes podem terminar sempre que o propósito do evento é
alcançado, garantindo que uma quantidade adequada de tempo seja gasta sem
permitir perdas no processo.

                Os eventos Scrum (reuniões) são todos time-box (de tempo determinado), de
       modo que toda oportunidade seja aproveitada para desenvolver o hábito da cadência,
       sempre no mesmo horário começa, no máximo com a mesma duração encerra-se,
       sempre igual, sem necessidade de controle. Por definição no Scrum, ou recomendação
       lógica de eficácia, somente a Sprint deve ser mantida sempre do mesmo tamanho.
       Finalizado uma Sprint, se algo não foi possível chegar ao estado final de pronto, a
       Sprint encerra-se e uma nova começa – não se prorroga uma Sprint para esperar algo
       que não ficou pronto, Ok?.

                Se tudo que estava previsto inicialmente para a Sprint ficou pronto antes da
       Sprint terminar, pode ser sinal que a velocidade do time aumentou desde a Sprint
       anterior, então mais incrementos de produtos podem ser incluídos na Sprint para
       completá-la e o time saberá, pela experiência, que a próxima Sprint poderá então prever
       entregar mais produtos, pois a velocidade e a produtividade do time está melhor que
       antes.

       Além da Sprint propriamente, que é um container para outros eventos, cada
evento no Scrum é uma oportunidade formal de inspecionar e de adaptar alguma
coisa. Estes eventos são especificamente projetados para permitir uma transparência
e uma inspeção criteriosa. A falha em não incluir qualquer um dos eventos resultará na
redução da transparência e na perda de oportunidade para inspecionar e adaptar.

                Alinhado aos pilares transparência para inspecionar e adaptar, o conjunto de
       eventos Scrum são pensados para que o Dono do Produto possa inspecionar o progresso
       dos trabalhos de forma frequente e transparente e que o time possa adaptar, quer seja
       refinando o entendimento do produto, quer seja adaptando a forma de trabalho (o
       processo) ou auxiliando os envolvidos no trabalho a realizar melhor seu trabalho.




                                              55


[PAGINA 56]
56   Agilidade nas empresas. Guia Scrum para quem não é de TI.


                     Se você é Dono de um Produto, não perca a oportunidade de prover e de
           aproveitar da transparência dos eventos do Scrum e não deixe de adaptar seu produto
           para as soluções que seu time poderá te apresentar, esteja aberto e direcione seu time
           sempre.

                     Se você é Scrum Master, não deixe de prover a transparência e a cadência de
           eventos que o Scrum preconiza e de auxiliar o time Scrum a entender e entregar o
           produto dos trabalhos. É responsabilidade do time de desenvolvimento entregar o
           melhor produto possível dentro do Sprint. Mas é responsabilidade sua auxiliar o time de
           desenvolvimento a fazer isso da melhor maneira possível. E é responsabilidade sua
           auxiliar o Dono do Produto a fazer o melhor produto possível. Como sempre, papéis
           distintos, responsabilidades claras.


[PAGINA 57]
                                                                                        A Sprint    57



       A Sprint

       O coração do Scrum é a Sprint, um evento time-box de um mês ou menos,
durante o qual um incremento de produto “Pronto” e potencialmente utilizável do
produto, é criado. Sprints tem durações consistentes em todo o período de
desenvolvimento. Uma nova Sprint inicia imediatamente após a conclusão da Sprint
anterior.

                Muita discussão ocorre nos times que implementam Scrum sobre a ‘duração
       ideal’ de uma Sprint (4, 3, 2 semanas). Mais importante que projetar a melhor duração
       possível é experimentar as primeiras Sprints e seguir adaptando a duração, o processo e
       as pessoas para o que melhor se aplica ao seu caso. Lembre-se das características
       ‘empírico’ e ‘adaptativo’ do Scrum, aprenda com a experiência do time e faça adaptação
       do que precisar. Neste sentido, de aprender com a experiência, então quanto menor for a
       Sprint (2 semanas?) talvez melhor seja para fins de aprender rapidamente com os
       feedbacks que vão surgir.

                Pode (e talvez vá mesmo acontecer) de uma 1ª Sprint parecer um grande
       pesadelo, o tempo (time-box) ter passado e pouco (ou quem sabe até mesmo nada)
       ‘potencialmente utilizável’ ter ficado pronto, mas, para a próxima Sprint, ajuste tudo
       que você conseguiu aceitar que errou e faça de novo. Aprenda e adapte. Aprenda mais,
       adapte e fique melhor. Como o passar das Sprints a velocidade do time vai aumentar.

       As Sprints são compostas por uma reunião de planejamento da Sprint, pelas
reuniões diárias, o trabalho de desenvolvimento, uma revisão da Sprint e a
retrospectiva da Sprint.

                Dividindo o elefante em partes menores (opa, sugiro novamente suspender o
       julgamento sobre ‘dividir o elefante em partes’ e ficar só com a analogia, ok?), uma
       Sprint é composta por 5 partes, tão igualmente importantes e fundamentais como os
       órgãos do corpo:

                       Planejar o que ‘cabe’ ser feito em 1 Sprint – lembre-se do Kanban, é
            levar algo da situação de A FAZER até a situação de FEITO, pronto e
            ‘potencialmente utilizável’;
                       Reunir-se diariamente, todos os dias, todo o time, e ‘cada pessoa do
            time’ saber o que ele tem ‘na sua própria fila’ para fazer, o que está ‘em suas mãos’
            e fazendo e como é que o Scrum Master pode ajudar o time a fazer sem os
            impedimentos, sem gargalos;




                                              57


[PAGINA 58]
58        Agilidade nas empresas. Guia Scrum para quem não é de TI.


                                 Trabalhar todos os dias e produzir o incremento de produto objetivo da
                    Sprint;
                                 Revisar diariamente a velocidade em produzir o incremento de produto
                    e decidir o que está pronto e poderá receber o selo de ‘feito’ e o que poderá não ser
                    considerado pronto e precisará voltar para a lista de coisas a fazer15;
                                 Rever a Sprint em retrospectiva, entender o que funcionou bem e o que
                    não funcionou, como fazer mais vezes o que funciona bem no seu contexto, aceitar
                    o que foi aprendido com os erros e como evitar a reincidência deles na próxima
                    Sprint que começa agora, com o Planejamento da próxima Sprint.

                Durante a Sprint:

                                 Não são feitas mudanças que possam por em perigo o objetivo
                da Sprint;
                                 As metas de qualidade não diminuem; e,
                                 O escopo pode ser clarificado e renegociado entre o Dono do
                Produto e o Time de Desenvolvimento quanto mais for aprendido.

                        3 pontos importantes: Sprint tem objetivos específicos, a qualidade do produto a
                ser entregue não é negociável, e escopo se negocia.


                        Um dos objetivos de as Sprint serem curtas é o fato de isto forçar que as
                entregas sejam pontuais e específicas o suficiente (para caber no time-box) e evitar que
                incertezas futuras impeçam os primeiros trabalhos de acontecer, permitindo que o
                movimento (os ciclos de melhoria contínua) se inicie.


                        Um ponto importante esperado dos trabalhos, é que o produto entregue tenha
                qualidade e que qualidade seja algo a ser buscado e não negligenciado. Uma entrega de
                pouca qualidade na Sprint de hoje, reduz a capacidade produtiva do time de
                desenvolvimento em fazer coisas ‘novas’ nas próximas Sprints, pois o tempo do time de
                desenvolvimento terá de ser compartilhado em resolver problemas. Fora que
                experiência de quem estará usando o Produto será superior ao usar um Produto livre de




     15
        Há um vídeo do Alpacino, trecho do filme Any Given Sunday de 1.999 onde ele fala discurso para um
     ti eàdeàfoot al,àeàdizà ueàu àjogoàseàga haà inch-by-inch ,ào deàaà a ge àpa aàe oà à so small àeàdizà
       ueà The inches we need are everywhere around us .àPo ta to,à aà i haàopi ião,àu àti eàdeveà
      aproveitar cada uma das oportunidades todos os dias para ganhar como equipe ou sucumbir como
     indivíduos .àássistaàoàvídeoàtodosàos dias antes de começar o trabalho! Veja mais em
     https://youtu.be/BL2CsP5JG2Y


[PAGINA 59]
                                                                                             A Sprint    59


       defeitos. Um cliente desencantado, procura outros produtos e serviços e seus
       fornecedores para encantá-lo.

               O terceiro ponto é que o produto se clarifica e se negocia. Os itens de backlog
       do Produto não são detalhados em todo o nível de detalhe possível antes da Sprint
       começar (ou então teríamos voltado ao modelo preditivo / waterfall anterior, ok?).
       Clarificar significa que mais detalhe sobre um mesmo assunto se define ao longo do
       desenvolvimento do incremento de produto. Negociado significa que se for necessário,
       um item de backlog de produto pode entrar na Sprint e outro pode sair, desde que duas
       situações sejam satisfeitas: o item que entrou tenha o mesmo tamanho e exija o mesmo
       esforço para ficar pronto do item que saiu e; que esta repriorização tenha sido feita com
       o acordo do Dono do Produto.


       Cada Sprint pode ser considerada um projeto com horizonte não maior que um
mês. Como os projetos, as Sprints são utilizadas para realizar algo. Cada Sprint tem a
definição do que é para ser construído, um plano projetado e flexível que irá guiar sua
construção, o trabalho e o produto resultante.

       Sprints são limitadas a um mês corrido. Quando o horizonte da Sprint é muito
longo, a definição do que será construído pode mudar, a complexidade pode aumentar
e o risco pode crescer. Sprints permitem a previsibilidade que garante a inspeção e
adaptação do progresso em direção à meta pelo menos a cada mês corrido. Sprints
também limitam o risco ao custo de um mês corrido.

               Fazendo um paralelo, Sprints são pensadas para estimular os times de desenvolvimento
       e os Donos dos Produtos a criarem o hábito de fazerem entregas parciais a mais concreta
       possível (potencialmente utilizável) em curto e repetíveis espaços de tempo, entregas time-box
       de 1 mês – por exemplo, como forma alternativa ao modelo waterfall / sequencial de 1 entrega
       única ao final ‘x’ meses após começar.

               A possibilidade de poder fazer entregas frequentes mesmo que parciais (em
       funcionalidade), tem relação direta com a estratégia de habilitar a empresa com a capacidade de
       adaptação e rápida resposta frente às mudanças que o mercado exigir. Por isso de pensar em
       pequenos incrementos de funcionalidade disponíveis para uso do mercado de modo a conquistar
       sua atenção, seu interesse e até sua predileção para com a empresa nas próximas entregas.

               O trecho abaixo sobre Cancelamento da Sprint (uma situação extrema mas possível),
       pode ajudar a entender a importância dos ciclos serem curtos e frequentes.




       Cancelamento da Sprint


                                                59


[PAGINA 60]
60    Agilidade nas empresas. Guia Scrum para quem não é de TI.


            Uma Sprint pode ser cancelada antes do time-boxed da Sprint terminar.
     Somente o Dono do Produto tem a autoridade para cancelar a Sprint, embora ele (ou
     ela) possa fazer isso sob influência de outras partes interessadas, do Time de
     Desenvolvimento ou do Scrum Master.

            Uma Sprint poderá ser cancelada se o objetivo da Sprint se tornar obsoleto.
     Isto pode ocorrer se a organização mudar sua direção ou se as condições do mercado
     ou das tecnologias mudarem. Geralmente a Sprint deve ser cancelada se ela não faz
     mais sentido dadas certas circunstâncias. No entanto, devido a curta duração da
     Sprint, raramente cancelamentos fazem sentido.

            Quando uma Sprint é cancelada, qualquer item de Backlog do Produto
     completo e “Pronto” é revisado. Se uma parte do trabalho estiver potencialmente
     utilizável, tipicamente o Dono do Produto o aceita. Todos os itens de Backlog do
     Produto incompletos são reestimados e colocados de volta no Backlog do Produto. O
     trabalho feito neles se deprecia rapidamente e deve ser frequentemente reestimado.

            O cancelamento de uma Sprint consome recursos, já que todos tem que se
     reagrupar em outra reunião de planejamento da Sprint para iniciar outra Sprint.
     Cancelamentos de Sprints são frequentemente traumáticos para o Time Scrum, e são
     muito incomuns.

                    Indo direto ao ponto, se é possível perder uma parte do trabalho, que esta parte,
            ou que essa perda, seja pequena para se desperdiçar e jogar fora. Este é um benefício
            que há por traz da lógica das Sprints serem curtas e serem pequenos os incrementos de
            produto entregues. A comparação é, o que é mais custoso, perder? 2 semanas de
            trabalho de um grupo de 5 pessoas – por exemplo, que consumiu supostamente 5
            pessoas * 10 dias * 8 horas/dia = 400 horas de trabalho para produzir 5 coisas novas?
            Ou um grupo médio de 6 pessoas com picos de 10 pessoas, que trabalharam 6 meses
            para produzir 55 coisas que agora podem não valer mais?

                    Pode acontecer de as prioridades do mercado, do negócio, da empresa e do
            Dono do Produto mudarem e o Product Backlog ser repriorizado e descontinuar a
            necessidade de algo (ou tornar-se obsoleto como diz o Guia) e aumentar a prioridade de
            algo que estava lá no fundo da lista. Portanto, quanto antes o Time puder concluir (ou
            até mesmo suspender) um trabalho e passar a atender outras prioridades, melhor, mais
            rápida a resposta à mudança será dada ao mercado – por exemplo, e menos custosa a
            adaptação terá sido.

                    Visualmente é algo mais ou menos assim ...


[PAGINA 61]
                                                                            A Sprint   61




        ... (Figura 7A) temos um acordo, um acordo sobre algo extenso, demorado,
desafiador e complexo ...




        ... (Figura 7B) então ‘mergulhamos’ no árduo trabalho de produzir
absolutamente tudo que precisa ser feito ...




                                       61


[PAGINA 62]
62   Agilidade nas empresas. Guia Scrum para quem não é de TI.




                   ... (Figura 7C) então, finalmente, quando o produto resultante do trabalho está
           pronto e você coloca ele no mercado, ..., opa! o mercado mudou! E não está mais lá!

                   Finalizando e olhando numa escala menor (menos catastrófica), se o objetivo de
           uma Sprint pode mudar então pode acontecer de ela ter de ser cancelada, devido ao isto,
           melhor que ela seja a menor possível para ter a menor perda possível.


[PAGINA 63]
                                                                     Planejamento da Sprint      63



       Planejamento da Sprint

       O trabalho a ser realizado na Sprint é planejado na reunião de planejamento da
Sprint. Este plano é criado com o trabalho colaborativo de todo o Time Scrum.

       A reunião de planejamento da Sprint possui um time-box com no máximo oito
horas para uma Sprint de um mês de duração. Para Sprints menores, este evento é
usualmente menor. O Scrum Master garante que o evento ocorra e que os
participantes entendam seu propósito. O Scrum Master ensina o Time Scrum a
manter-se dentro dos limites do time-box.

       A reunião de planejamento da Sprint Planning responde às seguintes questões:

                     O que pode ser entregue como resultado do incremento de
       produto da próxima Sprint?
                     Como o trabalho necessário para entregar o incremento de
       produto será realizado?

               A reunião de planejamento da Sprint é um primeiro ponto de mudança para o
       Time Scrum, para nos certificarmos de que o Time não será um time “Ágil mas só até a
       primeira página!” (termo usado oportunamente pelo colega Thiago Simões da IBM).


               O ponto central aqui está no 1º parágrafo, onde consta que “Este plano é criado
       com o trabalho colaborativo de todo o time Scrum”, pois denota-se aqui a característica
       de auto-organização do time Scrum, pois fica à cargo de todo o Time Scrum fazer o
       planejamento e não sob responsabilidade segregada junto ao Scrum Master ou um
       Gerente de Projetos. É o próprio time que faz o plano (Sprint Planning) de o que cabe
       numa Sprint. O time que teve a oportunidade de fazer o próprio plano de entregas, será
       motivado e comprometido a cumprir o plano com uma chance maior do que um time
       que recebeu um plano pronto.


       Tópico Um: O que pode ser feito nesta Sprint?

       O Time de Desenvolvimento trabalha para prever as funcionalidades que serão
desenvolvidas durante a Sprint. O Dono do Produto debate o objetivo que a Sprint
deve realizar e os itens de Backlog do Produto que, se completados na Sprint,
atingiriam o objetivo da Sprint. Todo o Time Scrum colabora com o entendimento do
trabalho da Sprint.




                                            63


[PAGINA 64]
64        Agilidade nas empresas. Guia Scrum para quem não é de TI.


                        Um ponto importante a destacar aqui é que “existe trabalho fora da Sprint” (eu
                costumo dizer que “existe vida fora da Sprint”). Esta é uma questão importante, pois os
                times ágeis podem passar a generalizar de que tudo na vida agora são Sprints e que “só
                existe vida dentro das Sprints” e, até mesmo por este parágrafo do Guia, isso não é
                verdade, há trabalho antes de iniciar uma Sprint, atuando-se no refinamento do Backlog
                do Produto, nas revisões de Stories, em sessões de Planning Poker, em descoberta e
                ordenação de itens de Backlog do Produto para compor uma lista mínima de
                funcionalidades com as quais já é possível dar partida numa equipe de desenvolvimento,
                sem o risco de ficar sem “escopo” logo após a primeira Sprint. Não pode “faltar tijolo
                na obra”. Este trabalho é responsabilidade principal do Product Owner, suportado pelo
                Scrum Master como vimos nas sessões anteriores mas, como citado neste parágrafo do
                Guia Scrum, o time de desenvolvimento tem um papel ativo na proposição de novas
                funcionalidades a serem desenvolvidas numa Sprint futura. Ou seja, é natural que se
                tenha trabalho antes da primeira Sprint e também durante as Sprints, preparando
                trabalho para as próximas. Cerca de 10% do tempo de uma Sprint deveria ser usado em
                planejamentos e refinamentos da(s) próxima(s) Sprint(s). Não pode ‘faltar tijolo na
                obra’ ou o ritmo será perdido.

                A entrada para a reunião de planejamento da Sprint é o Backlog do Produto, o
     mais recente incremento do produto, a capacidade projetada do Time de
     Desenvolvimento durante a Sprint e o desempenho passado do Time de
     Desenvolvimento. O número de itens selecionados do Backlog do Produto para a
     Sprint é o único trabalho do Time de Desenvolvimento. Somente o Time de
     Desenvolvimento pode avaliar o que pode ser completado ao longo da próxima Sprint.

                        Corroborando com a colocação anterior de que “existe trabalho fora da Sprint”
                o Guia Scrum define que há varíaveis que o time de desenvolvimento deve avaliar para
                decidir-se sobre O QUÊ é possível aceitar entregar numa Sprint:

                        a) os itens de Backlog do Produto que são mais prioritários16 (que trazem mais
                valor) ao negócio;

                        b) a capacidade do time de desenvolvimento, pois “em geral” a capacidade dos
                times é finita, acredite, basta pensar que um time de desenvolvimento ideal terá de 5 a 9

     16
       Importante destacar que os itens de mais alta prioridade devem ser combinados ENTRE o Dono do
     Produto E o time de Desenvolvimento. Se depender do Dono do Produto, ele vai sempre priorizar novas
     Funcionalidades que ele mesmo entende serem necessárias no produto ou serviço mas, o time de
     desenvolvimento precisa negociar que haverá situações que em algumas Sprints, itens que Não
     representam Funcionalidades (conhecidas com requisitos não-funcionais – por exemplo, ou melhorias
     nos processos internos), precisarão ser atendidos em prol da manutenção de um software em bom
     estado de uso e na ampliação contínua da velocidade das entregas


[PAGINA 65]
                                                                      Planejamento da Sprint     65


       recursos, portanto a “capacidade” deste time de desenvolvimento, mesmo que 100%
       dedicado ao Backlog de um Produto, é finita, “mesmo em times ágeis ainda há
       restrições de recursos e as pessoas continuarão fazendo algumas atividades não
       relacionadas à Sprint”;

               c) o desempenho deste time (destes indivíduos) em Sprints anteriores (quando
       aplicável) pois sempre haverá uma 1ª vez, uma 1ª Sprint desta formação de time neste
       desenvolvimento, pessoas que saíram outras que entraram, novas versões de
       ferramentas, novos processos & procedimentos;

               d) a disponibilidade deste time (destas pessoas) para as próximas Sprints, pois
       sempre há oportunidade de alguém sair em férias, estar em treinamento, ou ainda ter sua
       alocação compartilhada com outro trabalho / outra demanda.

               Bom, de posse destas variáveis: o valor e o tamanho do que há de mais
       importante para fazer agora, quem vai trabalhar e qual a velocidade deste time de
       desenvolvimento nos últimos trabalhos, qual a disponibilidade do time para a(s)
       próxima(s) Sprint(s), o time decide quais serão os incrementos de produto da próxima
       Sprint passíveis de o time comprometer-se a entregar.

               Novamente, perceba a condição de negociação que deve existir entre quem
       espera por um novo incremento de produto (o Dono do Produto) e o time que é o
       responsável por fazer estes incrementos acontecerem. Pode haver conflito entre o senso
       de prioridades e valor do Dono do Produto e o tamanho do esforço entendido pelo Time
       de Desenvolvimento (e o Scrum Master precisa ajudar o time e o Dono do Produto nesta
       equação).

       Após o Time de Desenvolvimento prever os itens de Backlog do Produto que
irá entregar na Sprint, o Time Scrum determina a meta da Sprint. A meta da Sprint é o
objetivo que será atendido dentro da Sprint através da implementação do Backlog do
Produto, e a Meta da Sprint fornece orientação para o Time de Desenvolvimento sobre
o porquê de ele estar construindo o incremento.

               Perceba que negociado o QUÊ será feito uma Sprint, o time de desenvolvimento
       toma para sí a responsabilidade por entregar aquele incremento dentro do timebox
       combinado. Então agora o Time de Desenvolvimento precisará combinar entre si o
       COMO este trabalho será realizado e, algo importante é o Time de Desenvolvimento
       estabelecer entre eles, uma meta da Sprint, para que esta meta seja também a Meta
       pessoal de todos, de modo que todos estejam comprometidos com as suas metas e a
       Meta da Sprint.




                                             65


[PAGINA 66]
66    Agilidade nas empresas. Guia Scrum para quem não é de TI.




            Tópico Dois: como o trabalho escolhido será considerado
     Pronto?

            Tendo definido o objetivo da Sprint e selecionado os itens de Backlog do
     Produto para a Sprint, o Time de Desenvolvimento decide como irá construir essas
     funcionalidades durante a Sprint e transformá-las em um incremento de produto
     “Pronto”. Os itens de Backlog do Produto selecionados para a Sprint, junto com o
     plano de entrega destes itens é chamado de Backlog da Sprint.

                   Derivado então de uma ‘parte’ de Backlog do Produto que ‘entrou’ para a Sprint
            como a definição de O QUÊ será feito, o Time de Desenvolvimento elabora o Backlog
            da Sprint como a definição de COMO isto será feito. Como dito anteriormente, o Dono
            do Produto é responsável por fazer definições de alto-nível para o Backlog do Produto
            sobre as coisas que são necessárias de ter no Produto, e o Time de Desenvolvimento é
            responsável por determinar o como as atividades transcorrerão (levando em
            consideração as tecnologias relacionadas ao produto em questão e os procedimentos
            disponíveis na empresa). Novamente, papéis distintos, responsabilidades claras.

            O Time de Desenvolvimento frequentemente inicia o desenho do sistema e do
     trabalho necessário para converter o Backlog do Produto em um incremento do
     produto utilizável. O trabalho pode ser de tamanho variável ou esforço estimado.
     Contudo, trabalho suficiente é planejado durante o planejamento da Sprint pelo Time
     de Desenvolvimento para prever o que esta acredita que poderá fazer durante a
     próxima Sprint. O trabalho planejado pelo Time de Desenvolvimento para os primeiros
     dias da Sprint, é decomposto até o final desta reunião, frequentemente em unidades
     de um dia de duração ou menos. O Time de Desenvolvimento se auto-organiza para
     realizar todo o trabalho do Backlog da Sprint, durante o planejamento da Sprint e
     quando for necessário durante a Sprint.

                   O Dono do Produto é responsável por definir O QUE é necessário e o Time de
            Desenvolvimento por definir O COMO isto será feito, portanto, o Product Backlog é
            uma lista de COISAS a fazer no Produto – novas funcionalidades esperadas, e esta lista
            NÃO contém atividades e tarefas. O modo de fazer o Incremento de Produto chegar ao
            estado de “Pronto” é determinado pelo Time de Desenvolvimento.

                   Neste sentido, para enriquecer seu entendimento sobre Backlog do Produto ( O
            QUÊ, coisas ou funcionalidades) e Backlog da Sprint ( COMO, atividades ou trabalho
            ), é importante lembrar que o Scrum é passível de utilização em trabalhos não


[PAGINA 67]
                                                                        Planejamento da Sprint   67


       relacionados ao desenvolvimento de Software, há no livro “Scrum – a arte de fazer o
       dobro do trabalho na metade do tempo. De Jeff Sutherland” exemplos de aplicação do
       processo de gestão Scrum em contextos relacionados à educação, em casos de cobertura
       jornalística de guerra, trabalhos sociais, entre outros, registrando-se ganhos de
       produtividade de até 1.200%.

       O Dono do Produto pode ajudar a clarificar os itens de Backlog do Produto
selecionados e nas decisões conflituosas de troca. Se o Time de Desenvolvimento
determina que tem excesso ou falta de trabalho, os itens do Backlog da Sprint podem
ser renegociados com o Dono do Produto. O Time de Desenvolvimento também pode
convidar outras pessoas para participar desta reunião de forma a fornecer opinião
técnica ou de domínios específicos.

               Utilizando o contexto de um Serviço de TI, o Time de Desenvolvimento é o
       responsável pela confidencialidade, disponibilidade e integridade do Serviço de TI que
       materializa um Produto cujo Dono tem interesse em obter benefícios para a organização
       (quer seja um sistema de uso interno na organização ou um produto de Software
       comercializável). Neste sentido, entenda-se o termo em Português do Scrum ‘decisões
       conflituosas de trocas’ para o caso já citado, de quando o Time de Desenvolvimento
       precisa negociar que uma Sprint compreenda atender – por exemplo, um requisito não
       funcional de Segurança da Informação que surgiu em detrimento a produzir uma
       funcionalidade de negócios nova (daí as decisões conflituosas de trocas).

               Ainda, o Time de Desenvolvimento, de posse de sua atuação auto-organizada,
       pode precisar demonstrar ao Dono do Produto que ele está com excesso ou ainda com
       falta de trabalho para uma Sprint, combinando com o Dono do Produto postergar ou
       ainda antecipar a entrega de algo na Sprint em planejamento.

       No final do planejamento da Sprint, o Time de Desenvolvimento deve ser capaz
de explicar ao Dono do Produto e ao Scrum Master como pretende trabalhar como
equipe auto-organizada para completar o objetivo da Sprint e criar o incremento
previsto.

               Voltando ao tema de que “há vida fora da Sprint”, vale comentar aqui no
       fechamento do planejamento da Sprint, que um time Scrum trabalhando com métodos
       Ágeis, não é um time que não faz planejamento, mas sim, que faz planejamento em
       camadas. Não é feito planejamento ‘up front’, ou todo ele antes da execução, mas sim,
       de forma incremental e evolutiva. Não é que não tenha planejamento no Scrum, é que
       ele não é feito no modelo Preditivo / Waterfall / Up Front. Em primeiro lugar, por




                                              67


[PAGINA 68]
68        Agilidade nas empresas. Guia Scrum para quem não é de TI.


                definição o trabalho já está intrinsicamente ligado à um Produto17 da organização que
                existe devido à sua estratégia e que dá retorno para a empresa.

                        Ainda, grosso modo, se temos Sprints mensais, no mínimo as equipes Ágeis
                fazem planejamentos macro de forma a distribuir novas features / novas demandas pelas
                iterações ao longo dos próximos meses de horizonte, fazendo atualização e
                acompanhamento diário do andamento das demandas através da Administração à vista,
                com seus quadros Kanban e gráficos de Burn Down e Burn Up.




                                     Figura 8 – planejamento em camadas




                Objetivo ou meta da Sprint

                A meta da Sprint é um objetivo definido para a Sprint que pode ser satisfeito
     através da implementação do Backlog do Produto. O objetivo fornece uma direção
     para o Time de Desenvolvimento sobre o porquê de estar construindo o incremento. O
     objetivo é criado durante a reunião de planejamento da Sprint. O objetivo da Sprint dá
     ao Time de Desenvolvimento alguma flexibilidade a respeito da funcionalidade que
     será completada dentro dos limites da Sprint. Os itens do Backlog do Produto
     selecionados entregam algo de funcionamento coerente (claro, conciso e consistente),
     que pode ser o objetivo da Sprint. O objetivo da Sprint pode ser qualquer outro item de


     17
       Por Produto entenda um produto físico ou um serviço prestado, para público interno à organização ou
     comercializado para clientes finais e até mesmo utilizável pelas partes necessárias da sua cadeira de
     valor


[PAGINA 69]
                                                                      Planejamento da Sprint   69


funcionamento coerente (claro, conciso e consistente) que faça o Time de
Desenvolvimento trabalhar em conjunto em vez de em iniciativas separadas.

       Conforme o Time de Desenvolvimento trabalha, ele mantém o objetivo da
Sprint em mente. A fim de satisfazer o objetivo da Sprint, implementam funcionalidade
e tecnologia. Caso o trabalho acabe por ser diferente do esperado pelo Time de
Desenvolvimento, então eles colaboram com o Dono do Produto para negociar o
escopo do Backlog da Sprint dentro da Sprint.

               Dependendo da complexidade e do tamanho do Incremento de Produto a
       entregar, pode ser necessário organizar um release que para ele possa acontecer, pode
       ser que exista a necessidade de mais de uma iteração (Sprint) ou até mesmo Sprints
       (iterações) de mais de um Produto feitas até mesmo simultaneamente. Veja o diagrama.




                Figura 9 – planejamento de releases entre diferentes produtos

               Quando um Time de Desenvolvimento trabalha de forma independente, esta
       análise de interdependência entre Produtos pode não ser aplicável – ficando restrito
       somente ao planejamento de Releases após múltiplos Sprints. Já num contexto de
       múltiplos Produtos e múltiplos times Scrum trabalhando em paralelo, existe a
       necessidade de os Donos de Produtos conciliarem as suas demandas entre si, permitindo
       que múltiplos Times de Desenvolvimento possam fazer seus planejamentos em
       camadas, do portfólio de iniciativas que fazem a estratégia acontecer, passando pelo
       planejamento de releases no tempo – com antecedência e suas dependências, chegando
       ao planejamento das Sprints e seu acompanhamento diário – para não perder o objetivo
       ou meta da Sprint do ‘radar’.



                                             69


[PAGINA 70]
70   Agilidade nas empresas. Guia Scrum para quem não é de TI.


[PAGINA 71]
                                                                        Reunião Diária   71



       Reunião Diária

       A Reunião Diária do Scrum é um evento time-boxed de 15 minutos, para que o
Time de Desenvolvimento sincronize atividades e crie um plano para as próximas 24
horas. Esta reunião é feita para inspecionar o trabalho desde a última Reunião Diária,
e prever o trabalho que deverá ser feito antes da próxima Reunião Diária.

       A Reunião Diária é mantida no mesmo horário e local todo dia para reduzir a
complexidade. Durante a reunião os membros do Time de Desenvolvimento
esclarecem:


                     O que eu fiz ontem que ajudou o Time de Desenvolvimento a
       atender a meta da Sprint?
                     O que eu farei hoje para ajudar o Time de Desenvolvimento
       atender a meta da Sprint?
                     Eu vejo algum obstáculo que impeça a mim ou o Time de
       Desenvolvimento no atendimento da meta da Sprint?

       O Time de Desenvolvimento usa a Reunião Diária para inspecionar o
progresso em direção ao objetivo da Sprint e para inspecionar se o progresso tende
para completar o trabalho do Backlog da Sprint. A Reunião Diária aumenta a
probabilidade do Time de Desenvolvimento de atingir o objetivo da Sprint. Todos os
dias, o Time de Desenvolvimento deve entender como o mesmo pretende trabalhar
em conjunto, como um time auto-organizado, para completar o objetivo da Sprint e
criar o incremento esperado até o final da Sprint. O Time de Desenvolvimento ou
membros da equipe frequentemente se encontram imediatamente após a Reunião
Diária para discussões detalhadas, ou para adaptar, ou re-planejar, o restante do
trabalho da Sprint.

       O Scrum Master assegura que o Time de Desenvolvimento tenha a reunião,
mas o Time de Desenvolvimento é responsável por conduzir a Reunião Diária. O
Scrum Master ensina o Time de Desenvolvimento a manter a Reunião Diária dentro do
time-box de 15 minutos.

       O Scrum Master reforça a regra de que somente os integrantes do Time de
Desenvolvimento participem da Reunião Diária.

       Reuniões Diárias melhoram as comunicações, eliminam outras reuniões,
identificam e removem impedimentos para o desenvolvimento, destacam e promovem




                                         71


[PAGINA 72]
72        Agilidade nas empresas. Guia Scrum para quem não é de TI.


     rápidas tomadas de decisão, e melhoram o nível de conhecimento do Time de
     Desenvolvimento. Esta é uma reunião chave para inspeção e adaptação.

                        As Reuniões Diárias (as Daily Meetings) são uma reunião do Time de
                Desenvolvimento, o Dono do Produto pode mesmo participar das Daily, mas é uma
                reunião do Time e para o Time de Desenvolvimento manter-se organizado e
                sincronizado. As Daily podem parecer um excesso de reuniões, mas o fato de ser rápida
                (não exceder 15 minutos) e de o Scrum Master ajudar o Time a manter-se todos
                intrínsecos às 3 respostas (qual trabalho eu já fiz, qual trabalho em tenho para fazer, o
                que está impedindo meu trabalho), faz com que o time precise estar todos os dias ciente
                do seu trabalho em andamento (WIP – Work In Progress) – é o que está em suas mãos,
                cientes de o que está na sua fila, na sua ‘caixa’ de entrada (e vai ficar parado somando
                ‘tempo de fila’) e a posicionar-se sobre se há algo que esteja impedindo os trabalhos
                (possibilidade de pedir ajuda para que não seja interrompido o fluxo de trabalho).

                        De modo similar as pessoas que estão ‘com pouca atuação’ podem ajudar outras
                que estão super atarefadas e gerando gargalo para a realização do trabalho.

                        A reunião diária é um momento de uso da informação de Administração à vista,
                pois o andamento do trabalho é acompanhado por todos no quadro Kanban18 da Sprint,
                no gráfico de Burn Down produzido pelo Scrum Master, e outros acompanhamentos
                visuais que a atividade do time requerer para dar transparência à inspeção do seu
                próprio trabalho.

                        A reunião diária é uma oportunidade de o time de desenvolvimento inspecionar
                se o trabalho está progredindo conforme o objetivo da Sprint, se há alguma adaptação a
                fazer em processos ou nas pessoas, se algo precisa ser corrigido na qualidade do
                produto19 ou ainda se algum refinamento do entendimento ou renegociação com o Dono
                do Produto precisa acontecer – por exemplo, nos casos de trabalho em excesso ou
                faltando.




     18
        O quadro Kanban é atualizado diariamente, não nos 15 minutos da Daily. Uma atividade que saiu do
     status TO DO e passou a DOING, é atualizada no Kanban no momento que isso aconteceu. Se a atividade
     acabou e precisa ser conferida, então muda para VERIFY.
     19
        Vamos falar mais disso num gráfico mais à frente, so eàaà efetividade do que se está produzindo .


[PAGINA 73]
                                                                            Revisão da Sprint   73



       Revisão da Sprint

       A Revisão da Sprint é feita no final da Sprint para inspecionar o incremento e
adaptar o Backlog do Produto se necessário. Durante a reunião de Revisão da Sprint o
Time Scrum e os stakeholders colaboram sobre o que foi feito na Sprint. Com base
nisso e em qualquer mudança no Backlog do Produto durante a Sprint, os
participantes colaboram nas próximas coisas que podem ser feitas para otimizar valor.
Esta é uma reunião informal, não uma reunião de status, e a apresentação do
incremento destina-se a motivar e obter comentários e promover a colaboração.

               A Revisão da Sprint (Sprint Review) é uma reunião chave para o Dono do
       Produto inspecionar antes do release, o incremento de produto (seja ele qual for, uma
       nova versão de um produto físico ou software, uma matéria jornalística elaborada, um
       treinamento realizado, ..., o que estiver sendo entregue iterativamente). O Dono do
       Produto e o Time de Desenvolvimento podem precisar de obter aprovações de outros
       interessados num tema, antes de considerar um incremento de produto como “Pronto”
       para a Operação. A revisão da Sprint serve também como oportunidade de atualizar o
       time com os novos itens de Backlog do Produto para ser usado já no Planejamento da
       próxima Sprint.

       Esta é uma reunião time-boxed de 4 horas de duração para uma Sprint de um
mês. Para Sprints menores, este evento é usualmente menor. O Scrum Master
garante que o evento ocorra e que os participantes entendam o seu objetivo. O Scrum
Master ensina a todos a manter a reunião dentro dos limites do time-box.

       A Reunião de Revisão inclui os seguintes elementos:

                        Os participantes incluem o Time Scrum e os stakeholders
       chaves convidados pelo Dono do Produto;
                        O Dono do Produto esclarece quais itens do Backlog do Produto
       foram considerados “Prontos” e quais não foram considerados “Prontos”;
                        O Time de Desenvolvimento discute o que foi bem durante a
       Sprint, quais problemas ocorreram dentro da Sprint, e como estes problemas
       foram resolvidos;
                        O Time de Desenvolvimento demonstra o trabalho que está
       “Pronto” e responde a questões sobre o incremento;




                                             73


[PAGINA 74]
74    Agilidade nas empresas. Guia Scrum para quem não é de TI.


                            O Dono do Produto discute o Backlog do Produto tal como está.
            Ele (ou ela) projeta as prováveis datas de conclusão baseado no progresso até
            a data (se necessário);
                            O grupo todo colabora sobre o que fazer a seguir, e é assim que
            a Reunião de Revisão da Sprint fornece valiosas entradas para a Reunião de
            Planejamento da próxima Sprint;
                            Análise de como o mercado ou o uso potencial do produto pode
            ter mudado e o que é a coisa mais importante a se fazer a seguir; e,
                            Análise da linha do tempo, orçamento, potenciais capacidades, e
            mercado para a próxima versão esperada do produto

                    A Revisão da Sprint (Sprint Review) é o evento limite para o Dono do Produto
            aceitar um incremento de Produto (uma entrega) como ‘pronto’ ou ‘não pronto’ para a
            Operação. Como o Dono do Produto participou ativamente da definição, revisão e testes
            do incremento de produto durante os trabalhos da Sprint, a entrega não é uma
            ‘novidade’ para o Dono do Produto, sendo a Sprint Review uma oportunidade final de
            aceitá-lo como Pronto ou Não-Pronto. No contexto de Desenvolvimento de Software –
            por exemplo, atenção especial é dada ao risco de o incremento de Produto poder ser
            considerado como ‘não-pronto’, pois devido às questões de gerenciamento de versão de
            código-fonte, nem sempre é livre de riscos o trabalho de ‘retirar’ um incremento de
            produto do código-fonte de um software, podendo até ser uma tarefa complexa que
            pode gerar novos defeitos no código-fonte, e até mesmo desestabilizá-lo.

            O resultado da Reunião de Revisão da Sprint é um Backlog do Produto
     revisado que define o provável Backlog do Produto para a próxima Sprint. O Backlog
     do Produto pode também ser ajustado completamente para atender novas
     oportunidades.

                    A Revisão da Sprint (Sprint Review) também traz a oportunidade de o Dono do
            Produto compartilhar com o Time de Desenvolvimento, as mais novas prioridades do
            Product Backlog obtidas à partir da Operação do Dia a Dia ou ainda dos clientes finais
            da organização (em última análise, do mercado), servindo como entrada para reunião de
            Planejamento da próxima Sprint, não sem antes o time olhar a última Sprint em
            retrospectiva.


[PAGINA 75]
                                                                      Retrospectiva da Sprint    75



       Retrospectiva da Sprint

       A Retrospectiva da Sprint é uma oportunidade para o Time Scrum inspecionar
a si próprio e criar um plano para melhorias a serem aplicadas na próxima Sprint.

               Muito importante esta oportunidade de as pessoas poderem de forma constante
       (time-box) saírem da rotina por um momento, olharem para si mesmos e os últimos
       trabalhos feitos e, de posse desta auto avaliação, proporem melhorias no seu próprio
       jeito de trabalhar em equipe, melhorias na própria equipe, nos relacionamentos entre as
       pessoas que fazem o trabalho acontecer – que fazem o produto ser incrementado, nos
       processos e ferramentas utilizadas para tal. Tudo de forma que a implementação da
       mudança esteja ‘nas mãos’ das pessoas. Não precisa ser um evento tão estruturado
       como um evento de Kaizen da melhoria contínua utilizado no Lean Management, mas é
       uma oportunidade de melhorar.

       A Retrospectiva da Sprint ocorre depois da Revisão da Sprint e antes da
reunião de planejamento da próxima Sprint. Esta é uma reunião time-boxed de três
horas para uma Sprint de um mês. Para Sprint menores, este evento é usualmente
menor. O Scrum Master garante que o evento ocorra e que os participantes entendam
seu propósito. O Scrum Master ensina todos a mantê-lo dentro do time-box. O Scrum
Master participa da reunião como um membro auxiliar do time devido a sua
responsabilidade pelo processo Scrum.

       O propósito da Retrospectiva da Sprint é:

                      Inspecionar como a última Sprint foi em relação às pessoas, aos
       relacionamentos, aos processos e às ferramentas;
                      Identificar e ordenar os principais itens que foram bem e as
       potenciais melhorias; e,
                      Criar um plano para implementar melhorias no modo como o
       Time Scrum faz seu trabalho.

               A Retrospectiva da Sprint é um momento para avaliar como as coisas estão indo
       na equipe. Usando a linguagem do Lean Management, como é que o ‘trabalho está
       fluindo’. Há várias perguntas chaves que podem ser usadas de âncora para iniciar
       discussões que ajudam a trazer temas à mesa. Vamos ver algumas possibilidades de
       perguntas para auto avaliação:

                      O que está indo bem?




                                              75


[PAGINA 76]
76   Agilidade nas empresas. Guia Scrum para quem não é de TI.


                          O que não está indo bem?
                          Quais impedimentos estamos tendo?
                          Quais riscos temos para com o processo Scrum no nosso time?
                          De modo similar, quais oportunidades podemos aproveitar melhor?
                          Se você puder resumir o time numa Meta, qual é ela?
                          Há impedimentos no nível do time?
                          Há impedimentos no nível da organização?
                          O que você gostou de fazer?
                          O que você não gostou de fazer?
                          O que você aprendeu?
                          O que você pode fazer para melhorar isso em você?
                          O que você perdeu?
                          O que você esperava e não viu acontecer?
                          Alguma fraqueza pessoal?
                          Qual sua meta pessoal de melhoria para a próxima Sprint?
                          Que compromisso pessoal você faz para a próxima Sprint?
                          Quais lições você aprendeu?
                          Quais foram suas realizações?
                          Há áreas de problemas?
                          Alguma consideração para as Sprints futuras?
                          Cite questões específicas com relação a: pessoas, produtos, processos,
               ferramentas, infraestrutura, local de trabalho.

                   Esta lista não é para ser usada na íntegra, siga a lógica de que menos é mais, e
           escolha umas 4 – máximo 5 questões por sessão de Retrospectiva e vá variando as
           questões à cada reunião para usar estimular a criatividade da equipe ao explorar
           diferentes questões. Para falhas que estejam trazendo maiores impactos para a
           produtividade do trabalho, você pode inclusive fazer uma análise FMEA, do tipo:

                                  A falha
                                  A causa raiz
                                  A consequência ou implicação
                                  A ação de prevenção para não reincidência
                                  Como saber que a solução foi efetiva


[PAGINA 77]
                                                                     Retrospectiva da Sprint    77


              Fazendo novo link com os valores do Scrum, é importante que a equipe
       participe das reuniões de Retrospectiva de forma aberta a receber feedback e aprenda
       com eles, bem como que dê feedback de forma respeitosa aos demais colegas da equipe.

       O Scrum Master encoraja o Time Scrum a melhorar, dentro do framework do
processo Scrum, o processo de desenvolvimento e as práticas para fazê-lo mais
efetivo e agradável para a próxima Sprint. Durante cada Retrospectiva da Sprint, o
Time Scrum planeja formas de aumentar a qualidade do produto, adaptando a
definição de “Pronto” quando apropriado.

       Ao final da Retrospectiva da Sprint, o Time Scrum deverá ter identificado
melhorias que serão implementadas na próxima Sprint. A implementação destas
melhorias na próxima Sprint é uma foram de adaptação à inspeção que o Time Scrum
faz a si próprio. A Retrospectiva da Sprint fornece um evento dedicado e focado na
inspeção e adaptação, no entanto, as melhorias podem ser adotadas a qualquer
momento.

              Uma reunião de Retrospectiva deve terminar sempre, sempre é sempre, Ok?
       com uma lista de ações combinadas pelo time Scrum, ações que serão tomadas por estas
       pessoas já na próxima Sprint. É a institucionalização do processo de melhoria contínua
       no time Scrum, Sprint a Sprint, de modo que o time seja mais produtivo e que o
       incremento de produto gerado tenha sua qualidade melhorada.




                                            77


[PAGINA 78]
78    Agilidade nas empresas. Guia Scrum para quem não é de TI.



            Artefatos do Scrum / Backlog do Produto

            Os artefatos do Scrum representam o trabalho ou o valor para o fornecimento
     de transparência e oportunidades para inspeção e adaptação. Os artefatos definidos
     para o Scrum são especificamente projetados para maximizar a transparência das
     informações chave de modo que todos tenham o mesmo entendimento dos artefatos.




            Backlog do Produto

            O Backlog do Produto é uma lista ordenada de tudo que deve ser necessário
     no produto, e é uma origem única dos requisitos para qualquer mudança a ser feita no
     produto. O Dono do Produto é responsável pelo Backlog do Produto, incluindo seu
     conteúdo, disponibilidade e ordenação.

                    Como colocado em pontos anteriores, o Backlog do Produto (lista de coisas a
            fazer) é um ‘funil de entrada’ de novas ideias e características para um Produto em
            questão. Tudo que o Dono do Produto pretender fazer em algum momento, vai para a
            lista – inicialmente, pode ser tão simples quanto uma nota ou lembrete, o Backlog do
            Produto vai sendo ordenado, refinado e melhor estruturado pelo Dono do Produto
            conforme o seu senso de prioridade para os negócios. Vejamos.

            Um Backlog do Produto nunca está completo. Os primeiros desenvolvimentos
     apenas estabelecem os requisitos inicialmente conhecidos e melhor entendidos. O
     Backlog do Produto evolui tanto quanto o produto e o ambiente no qual ele será
     utilizado evoluem. O Backlog do Produto é dinâmico; mudando constantemente para
     identificar o que o produto necessita para ser mais apropriado, competitivo e útil. O
     Backlog do Produto existirá enquanto o produto também existir.

                    Fazendo um paralelo com o mundo de Product Management – Gestão de
            Produtos, um conceito existente no mercado de produtos (extensível a serviços), é a
            ‘curva da banheira’, onde, quando do lançamento de um produto há uma fase conhecida
            como ‘infância’ onde a Taxa de Falhas é alta e o produto ainda está amadurecendo –
            podendo ser necessário que vários itens de Backlog do Produto sejam abertos para
            ‘completar’, ‘melhorar’ ou ainda ‘corrigir’ o produto que já tem adesão do mercado, e
            segue rumo a consolidar. A fase intermediária conhecida como ‘vida útil’ é uma fase
            que as empresas esperam que seja a mais longa possível, para que o produto, agora
            estável, possa ser ‘consumido pelo mercado’ e trazer retorno para a empresa, até que ele
            chegue à fase final em que o ‘desgaste’ passa a ser maior e a taxa de falhas sobe


[PAGINA 79]
                                             Artefatos do Scrum / Backlog do Produto      79


novamente, tornando o produto inviável e forçando clientes a uma atualização para
outro produto mais moderno – melhor ainda se for da mesma empresa!




                         Figura 10 – curva da banheira

        Durante a ‘vida útil’ do produto ou serviço, o desejo da empresa que o lançou
ao mercado é que passado a ‘infância’ este já esteja recebendo atenção e demandas aos
montes do mercado, e que a sua ‘vida útil’ seja sempre a maior possível, maximizando o
retorno sobre os investimentos feitos. Porém, em produtos físicos e muito mais ainda
em serviços, voltando lá na abertura do livro ‘introdução ao tema agilidade’, a
volatilidade do mercado é cada vez mais alta, significando que ‘nem sempre’ a vida útil
do produto ou serviço é tão ‘calma como uma linha reta’ sem falhas e ainda sem
necessidade de novos investimentos para responder às pressões do mercado (clientes e
concorrentes), então a empresa precisa fazer novos investimentos, mudanças no
produto, e gerar novos itens de Backlog do Produto. É neste sentido que o Guia do
Scrum diz que ‘o Backlog do Produto existirá enquanto o Produto também existir’.




                 Figura 11 – curva da banheira (com mudanças)

        Uma pesquisa recente do MIT demonstrou que na década de 1960 as empresas
duravam uma média de 60 anos e que nos dias atuais a média de duração é 10 anos. Tão
cruel quanto real.



                                      79


[PAGINA 80]
80    Agilidade nas empresas. Guia Scrum para quem não é de TI.


            O Backlog do Produto lista todas as características, funções, requisitos,
     melhorias e correções que formam as mudanças que devem ser feitas no produto nas
     futuras versões. Os itens do Backlog do Produto possuem os atributos de descrição,
     ordem, estimativa e valor.

                    Este parágrafo embora pequeno é importante, pois pode parecer que somente
            grandes evoluções dos produtos e serviços, só coisas novas, são feitas através do
            método que há no Guia do Scrum, mas não, novas características, funções ou
            funcionalidades passam pelo funil do Scrum, bem como melhorias em características ou
            funcionalidades já existentes e até mesmo correções de erros vão sendo priorizados nas
            Sprint Backlog, portanto o time Scrum é um time integrado que entrega correções,
            melhorias e evoluções no Produto, tudo por um grupo só.

                    Esta é uma mudança cultural grande. Fazendo um 2º parêntesis, Scrum não
            acontece no mundo de TI desacompanhado de práticas como: XP, TDD, FDD, Crystal
            Clear, Peer Programming, Refactoring, Automação de Build, de Testes, de Deploy e
            DevOps. Portanto, para ‘passar da primeira página’ na sua implementação de Scrum,
            para fazer mais que o Scrum. Fecha o parêntesis.

            Enquanto um produto é usado, ele ganha valor, e o mercado oferece retorno, o
     Backlog do Produto então torna-se uma lista maior e mais completa. Requisitos nunca
     param de mudar, então o Backlog do Produto é um artefato vivo. Mudanças nos
     requisitos de negócio, condições de mercado ou tecnologia podem causar mudanças
     no Backlog do Produto.

                    A estratégia do gerenciamento Ágil de Produtos e Serviços é encontrar um
            ponto inicial de características para um produto, de modo que ele seja ‘minimamente
            viável’ – ou seja, possa ser comercializável, desperte interesse de usuários por já
            agregar algum valor a estes, e possa ao ser experimentado pelo mercado, prover
            feedbacks e insights ao Dono do Produto sobre o que mais é importante incorporar no
            produto, nas suas próximas versões. Estes (insights) vindos do mercado ou mesmo
            stakeholders internos da organização (setas azuis) são capturados pelo Dono do Produto
            no Backlog do Produto (funil) e vão sendo entregues pelo time Scrum (seta vermelha)
            conforme o senso de prioridade do Dono do Produto e limitadas à sua (capacidade). O
            desafio de todos nós e fazermos o (vermelho) do lado direito do funil (capacidade)
            maior para atendermos mais coisas do lado esquerdo (azul).


[PAGINA 81]
                                                  Artefatos do Scrum / Backlog do Produto   81




                          Figura 12 – funil de ideias e trabalho

       Múltiplos Times Scrum frequentemente trabalham juntos no mesmo produto.
Um Backlog do Produto é usado para descrever o trabalho previsto para o produto.
Um atributo do Backlog do Produto que agrupe itens pode ser então aplicado.

       O refinamento do Backlog do Produto é a ação de adicionar detalhes,
estimativas e ordem aos itens no Backlog do Produto. Este é um processo contínuo
em que o Dono do Produto e o Time de Desenvolvimento colaboram nos detalhes dos
itens do Backlog do Produto. Durante o refinamento do Backlog do Produto, os itens
são analisados e revisados. O Time de Desenvolvimento decide como e quando o
refinamento está “Pronto”. Este refinamento usualmente não consome mais de 10% da
capacidade do Time de Desenvolvimento. Contudo, os itens do Backlog do Produto
podem ser atualizados a qualquer momento pelo PO ou a critério do PO.




                                          81


[PAGINA 82]
82        Agilidade nas empresas. Guia Scrum para quem não é de TI.


                                Figura 13 – refinamento do Backlog do Produto

                        A figura 13 (acompanhe a leitura da esquerda para a direita) explica o trabalho
                contínuo de refinamento do Backlog do Produto, onde a lista de coisas para fazer tem
                prioridade – quanto mais acima na lista mais prioritário, portanto quanto mais prioritário
                é o item, mais detalhe – mais informação se tem dele.

                        Os itens mais altos da lista estão mais refinados e detalhados em partes menores
                – mais precisas de o time Scrum entender, e são aqueles que serão mesmo entregues
                dentro do time-box já de uma próxima Sprint.

                        Os itens do meio da lista ‘podem’ vir a ser feitos e os do final, provavelmente
                podem até mesmo nunca ganhar prioridade para serem refinados – podendo ficar na
                lista lá em baixo como “uma ideia de algo grande ainda sem muito detalhe”.

                        Finalizando a figura do lado direito você vê também que os itens mais
                prioritários foram refinados e detalhados, mas também foram divididos em ‘pedaços’
                menores de incremento de produto. Você vê pela parte mais azul do lado direito que os
                itens que estão prontos para o próximo Sprint tem ‘tamanhos’20 menores (de 2 a 13
                ‘tamanhos’ cada) e que os itens menos prioritários, ainda não estão prontos o suficiente
                (grau de detalhe suficiente) para uma Sprint e são itens de ‘tamanhos’ supostamente
                maiores (20, 40, G, GG).

                        Este processo contínuo de priorizar, refinar, detalhar, dimensionar é importante
                porque todos dão foco no detalhe do que é importante para estar pronto agora já para a
                próxima Sprint sem perder do radar que outras características e funcionalidades serão
                brevemente incorporadas ao produto nas próximas Sprints. (você se recorda dos 10% de
                trabalho no refinamento dos itens das próximas Sprints? Então, é isso).

                        Este mecanismo contínuo de trabalho é um instrumento útil para o Dono do
                Produto pelo o fato de que após uma Sprint de 3 a 4 semanas – por exemplo, entregando
                o que foi ‘topo prioritário’ da lista, o time Scrum vai precisar ter um novo ‘topo
                prioritário’ pronto para ser desenvolvido, então caso as necessidades ou condições do
                mercado tenham mudado, o Dono do Produto tem a oportunidade de repriorizar o

     20
       Oàte oà ta a ho àpa aàoà“ u à àu aàfo aàdeà ediçãoàe à Story Poi ts’ ouà po tos de estória’. No
     “ u ,àosàite sàdeà a klogàsãoà es itos à aàfo aàdeà estó ias à– algoàassi à como administrador do App
     de chamado de carros autônomos eu quero uma consulta de carga das baterias para saber se algum
     veículo está perigosamente perto demais de ficar sem energia em trânsito até o próximo posto de
     abastecimento àeàestasàestó iasàte àta a hosàpa aàse e àfeitas.à“eào exemplo foi bom, você entendeu
     que o tema é extenso e que será coberto em outro Volume do livro que não este introdutório do tema.
     Exe plo,àesta osàa evia doàa uiàaài fo açãoàdeà ueàu aàestó iaàpa aà entrar na Sprint ,àp e isaà
     esta à pronta àpa aàau e ta àaà ha eàdeàelaàesta à feita àaoàfi alàdaà“p i t.àNoàVolu eàIIàvo à
     e te de àaàdife e çaàdeà pronta àeà feita .


[PAGINA 83]
                                                        Artefatos do Scrum / Backlog do Produto          83


        Backlog do Produto e trazer para a parte do topo prioritário o refinamento de alguns
        novos incrementos de produto que antes estavam lá em baixo nesta lista dinâmica de
        coisas a fazer no Produto ou Serviço e ter estes itens refinados, dimensionados e
        entendidos pelo time Scrum e prontos para serem feitos na próxima Sprint de 3 a 4
        semanas – por exemplo.

        Os itens do Backlog do Produto de ordem mais alta (topo da lista) devem ser
mais claros e mais detalhados que os itens de ordem mais baixa. Estimativas mais
precisas são feitas baseadas em maior clareza e maior detalhamento, quanto menor a
ordem na lista, menos detalhes. Os itens do Backlog do Produto que irão ocupar o
desenvolvimento na próxima Sprint são os mais refinados, de modo que todos os itens
possam ser “Prontos” dentro do time-boxed da próxima Sprint. Os itens do Backlog do
Produto que podem ser “Prontos” pelo Time de Desenvolvimento dentro da Sprint são
considerados como “Preparados” para seleção no Planejamento da Sprint. Itens do
Backlog do Produto geralmente adquirem este grau de transparência através das
atividades de refinamento descritas acima.

        O Time de Desenvolvimento é responsável por todas as estimativas. O Dono
do Produto deve influenciar o Time, ajudando no entendimento e nas concessões, mas
as pessoas que irão realizar o trabalham fazem a estimativa final.

                 Ainda na figura 13, lá no canto direito foi dito sobre o ‘tamanho’ das coisas que
        estão prontas para serem feitas durante uma Sprint. O time de Desenvolvimento é
        responsável por ‘dimensionar o tamanho’ dos incrementos de produto que poderão
        caber o time-box de 1 Sprint. O fato de o item de Backlog de Produto se quebrado em
        partes menores e detalhado em conjunto com o Dono do Produto é para facilitar a
        assertividade do time de Desenvolvimento em estimar o tamanho dos itens.

                 O time de Desenvolvimento precisa saber qual é a sua capacidade produtiva
        para uma Sprint – quanto de trabalho é possível fazer num período de tempo de 3 a 4
        semanas por exemplo, de modo que a sua capacidade de trabalho dentro de uma Sprint,
        possa ser preenchida com ‘n’ incrementos de produtos cuja soma dos ‘tamanhos’ seja
        inferior21 à capacidade do time de Desenvolvimento (para fins de reservas para
        imprevistos por exemplo).



21
   Masà po ueài fe io ?àLe       e-se que o time Scrum faz coisas novas mas também resolve defeitos /
incidentes em ambiente produtivo. Sem uma reserva feita na partida / no planejamento, seu time pode
vir a fazer muito overtime e as suas próximas entregas – de coisas novas, podem atrasar ou ainda vir a
serem entregues sem testes adequados de qualidade, podendo gerar mais incidentes e alimentando um
 í uloàvi iosoà ui .àIstoà ãoàse à“ u ,àpoisà ualidadeà àu à ust have’.



                                                 83


[PAGINA 84]
84    Agilidade nas empresas. Guia Scrum para quem não é de TI.


                      Como o Scrum pressupõe um processo empírico – de aprender com a
            experiência realizada, um time Scrum (Desenvolvimento, Scrum Master e Dono do
            Produto) vai trabalhar algumas Sprints até aprender com sucesso qual é e como
            melhorar o seu ritmo de trabalho, sua capacidade produtiva à cada Sprint e quantos
            incrementos de Produtos prontos por Sprint eles podem fazer.

                      O funcionamento das Sprints é como as partidas e chegadas de um trem nas
            estações. O trem tem hora e minuto programados para chegar e sair das estações (as
            Sprints). O trem tem uma capacidade de carga por viagem. As pessoas conforme a sua
            própria prioridade de horários, precisam estar prontas na estação quando o trem chegar,
            para que o seu transporte até a próxima estação seja feito. Voltaremos ao trem mais a
            frente.




            Monitorando o progresso a caminho do objetivo

            Em qualquer ponto do tempo, o total de trabalho restante para alcançar um
     objetivo pode ser somado. O Dono do Produto acompanha o total de trabalho restante
     pelo menos a cada Reunião de Revisão da Sprint. O Dono do Produto compara este
     valor com o trabalho restante na Reunião de Revisão da Sprint anterior, para avaliar o
     progresso na direção de completar todo o trabalho previsto, com o tempo estimado
     para alcançar um objetivo. Esta informação deve ser transparente para todas as partes
     interessadas.

            Várias práticas de projeção de tendências como burndown, burnup e outras
     práticas de estimativa tem sido usadas para prever o progresso. Estas práticas tem se
     provado úteis. Contudo, não substituem a importância do empirismo. Em ambientes
     complexos, o que acontecerá é desconhecido. Somente o que tem acontecido pode
     ser usado para uma tomada de decisão a respeito do que virá.


[PAGINA 85]
                                             Artefatos do Scrum / Backlog do Produto     85




                        Figura 14 – Gráfico de Burn Up

        No simples gráfico de Burnup exemplo acima, é possível o time Scrum
demonstrar de forma transparente para o Dono do Produto, quanto de esfoço em
‘pontos’ é esperado fazer em um produto ou serviço (a linha preta Escopo/Scope), como
tem sido a velocidade de entregas nas primeiras 6 Sprints (as colunas em cor azul) de
realizado/actual, baseado na experiência do time que está atuando, uma projeção (linha
pontilhada em cinza) de quando os itens de Backlog do Produto já priorizados e
estimados estarão prontos para uso. É responsabilidade do Dono do Produto demandar
incrementos de produto que realmente tragam valor para a organização – fazendo o
melhor uso possível do tempo e do custo do time de Desenvolvimento. É
responsabilidade do time de Desenvolvimento ampliar sua capacidade produtiva e
manter a qualidade da entrega sempre em nível ótimo, para que a experiência do usuário
com o produto ou serviço seja sempre a melhor possível. É responsabilidade do Scrum
Master auxiliar ambos os lados. O Dono de Produto a demandar o melhor produto
possível e, o time de Desenvolvimento a fazer o melhor produto possível. Isso mesmo,
aquela pessoa da capa, lembra-se?




                                      85


[PAGINA 86]
86    Agilidade nas empresas. Guia Scrum para quem não é de TI.



            Artefatos do Scrum / Backlog da Sprint

            O Backlog da Sprint é um conjunto de itens do Backlog do Produto
     selecionados para a Sprint, juntamente com o plano para entregar o Incremento do
     produto e atingir o objetivo da Sprint. O Backlog da Sprint é a previsão do Time de
     Desenvolvimento sobre qual funcionalidade estará no próximo Incremento e sobre o
     trabalho necessário para entregar essa funcionalidade em um Incremento “Pronto”.

            O Backlog da Sprint torna visível todo o trabalho que o Time de
     Desenvolvimento identifica como necessário para atingir o objetivo da Sprint.

            O Backlog da Sprint é um plano com detalhes suficientes que as mudanças no
     progresso posam ser entendidas durante a Reunião Diária. O Time de
     Desenvolvimento modifica o Backlog da Sprint ao longo de toda a Sprint, e o Backlog
     da Sprint vai surgindo durante a Sprint. Este surgimento ocorre quando o Time de
     Desenvolvimento trabalha segundo o plano e aprende mais sobre o trabalho
     necessário para alcançar o objetivo da Sprint.

            Sempre que um novo trabalho é necessário, o Time de Desenvolvimento
     adiciona este ao Backlog da Sprint. Conforme o trabalho é realizado ou completado, a
     estimativa do trabalho restante é atualizada. Quando elementos do plano são
     considerados desnecessários, eles são removidos. Somente o Time de
     Desenvolvimento pode alterar o Backlog da Sprint durante a Sprint. O Backlog da
     Sprint é altamente visível, uma imagem em tempo real do trabalho que o Time de
     Desenvolvimento planeja completar durante a Sprint, e pertence exclusivamente ao
     Time de Desenvolvimento.


[PAGINA 87]
                                                Artefatos do Scrum / Backlog da Sprint     87




                    Figura 15 – item do Backlog do Produto

        Enquanto o Backlog (lista de coisas, características ou funcionalidades a fazer)
no Produto é mantido pelo Dono do Produto, o Backlog da Sprint (lista de trabalhos a
fazer) é mantido pelo time de Desenvolvimento.

        O Backlog da Sprint é composto pelos itens do Backlog do Produto definidos e
priorizados pelo Dono do Produto e dimensionados pelo time de Desenvolvimento,
acrescido das atividades relacionados ao trabalho do time de Desenvolvimento para
fazer o incremento do produto – como o trabalho será feito, qual o progresso, os
problemas ou defeitos que a versão intermediária do incremento de produto tem para
serem resolvidos, documentação para gestão do conhecimento neste e nas próximas
Sprints – por exemplo.

        Relembrando o que vimos da reunião de planejamento da Sprint, o Backlog do
Produto diz respeito ao O QUÊ precisa ser produzido no produto – esta definição é do
Dono do Produto e será a sua base de julgamento se o produto (até o final da Sprint)
será considerado pronto ou não, e o Backlog da Sprint diz respeito a COMO isto será
feito – é a forma de trabalho do time de Desenvolvimento.

        Fazendo uma alusão à pintura de uma casa, a definição de quais serão as cores
de paredes, tetos, portas e janelas é feita pelo Dono do Produto / Dono do Imóvel e, o
acordo sobre quais serão os procedimentos para preparação, pintura, acabamento e



                                      87


[PAGINA 88]
88    Agilidade nas empresas. Guia Scrum para quem não é de TI.


            limpeza dos locais é feita pelo time de Pintores. Ainda, o esforço, o custo do time de
            Pintores e a qualidade esperada para pinturas do tipo fosco, brilho, alto-brilho, verniz,
            tinta-óleo, acrílico, patina, laqueado, entre outras possibilidades, pode variar em
            tamanho, mas principalmente, para o Dono do Imóvel o valor percebido para cada um
            dos tipos de acabamento pode variar significativamente. Novamente, é responsabilidade
            do Scrum Master (a pessoa da capa!) auxiliar o time Scrum a chegar nestes acordos de
            modo eficaz, buscando o melhor benefício para o Dono do Imóvel e a melhor
            rentabilidade e também produtividade para o time de Pintores.

     Monitorando o Progresso da Sprint

             Em qualquer ponto do tempo na Sprint, o total do trabalho remanescente dos
     itens do Backlog da Sprint pode ser somado. O Time de Desenvolvimento monitora o
     total de trabalho restante pelo menos a cada Reunião Diária. O Time de
     Desenvolvimento acompanha estes resumos diários e projeta a probabilidade de
     alcançar o objetivo da Sprint. Com o rastreamento do trabalho restante em toda a
     Sprint, o Time de Desenvolvimento pode gerenciar o seu progresso.




                                   Figura 16 – gráfico de Burn Down

            Monitorar o progresso do trabalho durante a Sprint é importante para o time Scrum
            para: 1º garantir a entrega do que foi combinado numa Sprint e subsidiar a característica
            de processo empírico (aprender com a experiência) do Scrum.

            Caso a monitoração do trabalho em andamento não seja feita de modo deliberado e
            consciente (o que e quanto estamos fazendo, como estamos indo, que velocidade temos,


[PAGINA 89]
                                               Artefatos do Scrum / Backlog da Sprint    89


estamos adiantados ou atrasados em relação ao time-box, qual a qualidade do que nós
estamos gerando, qual está sendo a efetividade do que está ficando pronto), o time
Scrum corre o risco e ‘entrar num modo automático’, não aprender, não evoluir em
capacidade, produtividade e qualidade, não entregar algo de real valor. Trabalhar
automática e mecanicamente. Isto não será Scrum.

        Sendo coerente com os 3 Pilares do Scrum que falamos no início:
Transparência, Inspeção e Adaptação, o gráfico de acompanhamento do trabalho a
seguir, dá transparência ao trabalho, demonstra quanto de inspeção vem sendo feito e
proporciona que adaptação aconteça com a meta de atingir o objetivo da Sprint.




                      Figura 17 – progresso dos trabalhos

        Um acompanhamento do progresso dos trabalhos neste formato acima, promove
a transparência sobre 4 informações:

                a) a quantidade total de incrementos de produto que está se buscando
        realizar em 14 dias (linha em cor preta com 25 ‘Story Points’);

                b) a quantidade de incrementos de produto que está ‘desenvolvido’ pelo
        time de Desenvolvimento, e supostamente pronto, (linha amarela);




                                       89


[PAGINA 90]
90   Agilidade nas empresas. Guia Scrum para quem não é de TI.


                           c) a quantidade de incrementos de produto que está feito QA (Quality
                   Assurance) ou inspeção de qualidade pelo próprio time de Desenvolvimento, e
                   provavelmente pronto, (linha laranja);

                           d) a quantidade de incrementos de produto que está efetivamente
                   inspecionado e agora aceito como ‘pronto’ pelo Dono do Produto ou outros
                   interessados relevantes, (linha azul).

                   Perceba como que as 3 linhas inferiores evoluem em ritmo diferente rumo ao
           topo (quantidade total de incrementos de produto a integrar em uma ou mesmo mais
           Sprints). 1º passo – amarelo, finalizado a sua construção, montagem ou execução e
           ‘supostamente’ pronto. 2º passo – laranja, finalizado os testes de verificação de
           qualidade e solução de defeitos, ‘provavelmente’ pronto. 3º passo – azul, ‘efetivamente’
           aceito como pronto e passível de utilização real por usuários em ambiente produtivo ou
           na operação da empresa no mercado.

                   Perceba pelo gráfico, como que as inspeções frequentes (pelo time de
           Desenvolvimento e depois pelo Dono do Produto), possibilita que o time de
           Desenvolvimento possa fazer adaptação (do produto final, da forma, processo,
           velocidade e/ou procedimentos de trabalho), de modo que o objetivo de entregar
           incrementos de produtos no tamanho total de 25 unidades (Story Points) de tamanho,
           seja atingido. É uma forma de garantir o foco no que está sendo feito.

                   No exemplo do gráfico da figura 17, ao final de 14 dias de trabalho para
           produzir 25 ‘coisas’, todas estão finalizadas, 23.5 estão verificadas a qualidade e
           somente 5.5 estão efetivamente aceitas como prontas. Se estes 14 dias eram o prazo
           final do time-box de Sprint, então somente 22% do trabalho ficou pronto! Denotando
           que a velocidade real do time de Desenvolvimento é 78% inferior ao projetado, sendo
           necessário analisar-se as causas raiz dos problemas durante a reunião de Retrospectiva,
           e adaptar-se tudo que for causa raiz para que o time Scrum possa ser mais assertivo no
           planejamento do próximo time-box.


[PAGINA 91]
                                                                           Incremento    91



       Incremento

       O incremento é a soma de todos os itens do Backlog do Produto completados
durante a Sprint e o valor dos incrementos de todas as Sprints anteriores. Ao final da
Sprint um novo incremento deve estar “Pronto”, o que significa que deve estar na
condição utilizável e atender a definição de “Pronto” do Time Scrum. Este deve estar
na condição utilizável independente do Dono do Produto decidir por liberá-lo realmente
ou não.




                                          91


[PAGINA 92]
92    Agilidade nas empresas. Guia Scrum para quem não é de TI.



            Transparência do Artefato

            Scrum invoca transparência. Decisões para otimizar o valor e o controle de
     riscos são feitos com base na percepção existente do estado dos artefatos. Na medida
     em que a transparência é plena, estas decisões tem uma base sólida. Na medida em
     que os artefatos não são completamente transparentes, estas decisões podem ser
     falhas, valores podem diminuir e riscos podem aumentar.

            O Scrum Master deve trabalhar com o Dono do Produto, Time de
     Desenvolvimento, e outras partes envolvidas para entender se os artefatos estão
     plenamente transparentes. Há práticas para lidar com transparência incompleta, o
     Scrum Master deve ajudar todos a aplicar a mais apropriada prática na falta de uma
     transparência plena. O Scrum Master pode detectar transparência incompleta pela
     inspeção dos artefatos, percebendo padrões, ouvindo atentamente o que está sendo
     dito, e detectando diferenças entre o esperado e o resultado real.

            O trabalho do Scrum Master é trabalhar com o Time Scrum e a organização
     para aumentar a transparência dos artefatos. Este trabalho geralmente envolve
     aprendizagem, convencimento e mudança. Transparência não ocorre de um dia para o
     outro, mas é um caminho.


[PAGINA 93]
                                                                         Defi içãoàdeà P o to   93



       Defi ição de P o to

       Quando o item do Backlog do Produto ou um incremento é descrito como
“Pronto”, todos devem entender o que o “Pronto” significa. Embora, isso varie
significativamente de um extremo a outro para cada Time Scrum, os integrantes
devem ter um entendimento compartilhado do que significa o trabalho estar completo,
assegurando a transparência. Esta é a “Definição de Pronto” para o Time Scrum e é
usado para assegurar quando o trabalho está completo no incremento do produto.

       A mesma definição orienta o Time de Desenvolvimento em saber quantos itens
do Backlog do Produto podem ser selecionados durante a Reunião de Planejamento
da Sprint. O propósito de cada Sprint é entregar incrementos de funcionalidades
potencialmente utilizáveis que aderem à definição atual de “Pronto” do Time Scrum.

       O Time de Desenvolvimento entrega um incremento de funcionalidade do
produto a cada Sprint. Este incremento é utilizável, assim o Dono do Produto pode
escolher por liberá-lo imediatamente. Se a definição de “pronto” para um incremento é
parte das convenções, padrões ou diretrizes de desenvolvimento da organização,
todos os Times Scrum devem segui-la como um mínimo. Se “pronto” para um
incremento não é uma convenção de desenvolvimento da organização, o Time de
Desenvolvimento do Time Scrum deve definir uma definição de “pronto” apropriada
para o produto. Se há múltiplos Times Scrum trabalhando no lançamento do sistema
ou produto, os times de desenvolvimento de todos os Times Scrum devem
mutuamente definir a definição de “Pronto”.

       Cada incremento é adicionado a todos os incrementos anteriores e
completamente testado, garantindo que todos os incrementos funcionam juntos.

       Com um Time Scrum maduro, é esperado que a sua definição de “Pronto” seja
expandida para incluir critérios mais rigorosos de alta qualidade.

       Qualquer produto ou Sistema deve ter uma definição de “Pronto” que seja um
padrão para qualquer trabalho feito nele.

               Ao final do time-box da Sprint, quando da reunião de Revisão da Sprint, é
       esperado que o incremento de produto produzido na Sprint esteja em condição de
       ‘pronto’, é esperado que o item seja ‘passível’ de utilizar em ambiente produtivo, na
       operação ou ainda, por clientes no mercado.

               É importante que o Scrum Master atue diligentemente no entendimento da
       definição de ‘pronto’ ou de ‘em condições de operação’ entre o Dono do Produto e do



                                             93


[PAGINA 94]
94        Agilidade nas empresas. Guia Scrum para quem não é de TI.


                time de Desenvolvimento, ou então o cenário apresentado na figura anterior – só 22%
                do trabalho aceito como pronto, pode repetir-se e tornar o trabalho do time Scrum
                inviável. Se o que está sendo ‘supostamente’ entregue não está sendo ‘efetivamente’
                aceito e utilizado pelo usuário final, então não está sendo Scrum.

                        Em desenvolvimento de software – por exemplo, pode ser necessário negociar
                que o produto esteja testado22, que a documentação dos clientes esteja atualizada com as
                novas funcionalidades, que o material de marketing esteja pronto, que os canais de
                suporte e de feedback pelo usuário estejam atualizados, que requisitos regulatórios
                estejam atendidos, entre outros, dependendo do contexto e do produto.

                        Outro ponto a destacar é que mesmo considerando o incremento de produto
                como ‘pronto’ o Dono do Produto pode optar por segurar e liberar para a Operação mais
                à frente, junto com mais funcionalidades, dentro de uma campanha de marketing, junto
                à um evento de grande atenção, por exemplo. Neste caso, o time Scrum inicia os
                trabalhos em outra Sprint e atua na produção de mais incrementos de produto para a
                aceitação do Dono do Produto.




     22
       Em verdade, em um serviço de TI, uma gama de testes pode ocorrer, tais como: de unidade, smoke’,
     de funcionalidade, de sistema, de integração entre sistemas, de aceitação, performance, estabilidade,
     usabilidade, stress,à shake ,àPEN)


[PAGINA 95]
                                                                            Notas finais   95



       Notas finais

       O Scrum é livre e oferecido neste guia. Papéis, artefatos, eventos e regras do
Scrum são imutáveis e embora seja possível implementar somente partes do Scrum, o
resultado não é Scrum. Scrum existe somente na sua totalidade, funcionando bem
como um container para outras técnicas, metodologias e práticas.




Agradecimentos

Pessoas

       Das milhares de pessoas que tem contribuído com o Scrum, nós devemos
destacar aquelas que foram fundamentais nos primeiros dez anos. Os primeiros foram
Jeff Sutherland trabalhando com Jeff McKenna, e Ken Schwaber trabalhando com
Mike Smith e Chris Martin. Muitos outros contribuíram nos anos subsequentes e sem a
ajuda deles o Scrum não teria sido refinado tanto quanto está hoje.

       No Brasil, Fábio Cruz é o tradutor oficial do Guia Scrum, escritor e consultor
reconhecido no tema Scrum. Fábio Cruz é consultor e Agile Coach especialista em
gerenciamento ágil de projetos pela FabioCruz.com.




História

       Ken Schwaber e Jeff Sutherland fizeram a primeira co-apresentação do Scrum
na conferência OOPSLA de 1995. Esta apresentação essencialmente documentou o
aprendizado que Ken e Jeff tiveram ao longo dos anos anteriores aplicando o Scrum.

       A história do Scrum já é considerada longa. Para homenagear os primeiros
lugares onde ele foi experimentado e refinado, nós reconhecemos a Individual, Inc.,
Fidelity Investments, e IDX (atual GE Medical).

       O Guia do Scrum documenta o Scrum conforme desenvolvido e sustentado por
mais de 20 anos por Jeff Sutherland e Ken Schwaber. Outras fontes fornecem
padrões, processos, e percepções que complementam o Framework Scrum. Estas
otimizam produtividade, valor, criatividade e satisfação.




                                           95


[PAGINA 96]
96    Agilidade nas empresas. Guia Scrum para quem não é de TI.


             ©2016 Scrum.Org and Scrum Inc. Offered for license under the Attribution Share-Alike license of
     Creative Commons, accessible at http://creativecommons.org/licenses/by-sa/4.0/legalcode and also
     described in summary form at http://creativecommons.org/licenses/by-sa/4.0/. By utilizing this Scrum
     Guide you acknowledge and agree that you have read and agree to be bound by the terms of the
     Attribution ShareAlike license of Creative Commons.


[PAGINA 97]
                                                                                      Conclusão   97



        Conclusão

        Como dito no Guia Scrum ele é simples de entender (espero ter contribuído com você) e
difícil de aplicar (posso te ajudar com isso também).


        Como método empírico é mais importante aprender com a experiência que projetar
todos os próximos passos de todos os 365 dias do próximo ano. É importante fazer planos
(visões, roadmaps, walking skeletons, MVP) tudo isso é muito importante e a muitos importa,
mas sem dar o primeiro passo você vai continuar onde está. Coloque-se em movimento.
Permita-se experimentar e evoluir. Já dizia Darwin que ‘não é o mais forte que sobrevive, mas
sim o mais adaptável’.


        Voltando aos temos do começo do livro, você vê hoje em dia a Ford fabricando carros
do mesmo jeito que fazia o Ford-T? Tudo evoluiu? Você tem ‘modem externo’ em casa hoje em
dia? (até tem, mas eu digo aquele que fazia um sonzinho ao discar!?).


        Tudo muda o tempo todo! Aproveite! Quando chega a onda da mudança, VOCÊ, tem 2
escolhas, ‘você’ pega uma prancha e surfa a novidade / o tsunami, ou ‘você’ finca uma estaca no
chão, se agarra nela e torce para estar lá – e respirando, depois que a onda passar. Entendeu a
parte do ‘você’?


        Boa mudança para você!


        Se der medo, vai com medo mesmo!


        []s


        Roberto




                                               97


[PAGINA 98]
98    Agilidade nas empresas. Guia Scrum para quem não é de TI.



             CV do autor, Roberto NAVAS Pinheiro

             28 anos em IT & Operações, 23 em Bancos internacionais. 21 gerenciando projetos.
     Certificações PMP e PRINCE2. Posições seniores em empresas internacionais como IBM e
     Amazon. Gestão de mudanças de negócios, com equipes distribuídas em múltiplos países.
     Profissional experiente em Centros de Serviços Compartilhados. Habituado ao gerenciamento
     de equipes multidisciplinares em projetos e programas de milhões de R$ de orçamento.

             Habituado a liderar projetos prioritários que requerem recursos consideráveis e
     integração de equipes multifuncionais. Lidera projetos desde a concepção, entrega de produtos
     iniciais até a utilização final em operação, produção e/ou mercado. Faz interface com todas as
     áreas participantes dos projetos incluindo patrocinadores, usuários, clientes e fornecedores, em
     modelos contratuais tipo virada de chave, preço fixo e alocação. Faz garantia de qualidade,
     aderência a processos de negócios e experiência do cliente. Conduz comitês de direção com
     executivos seniores. Gerencia um conjunto de projetos de maneira a otimizar o retorno sobre o
     investimento e garantir o alinhamento com a estratégia da organização, administrando o
     nivelamento de recursos para resolver problemas de capacidade.

             Trabalha de modo eficiente em ambientes desafiadores. Flexível, confiável e
     comprometido. Tem uma liderança orientada à entrega, autocontrole, autoconhecimento e
     motivação, pragmático, diplomático e Coach (treinador).

             Experiente em disciplinas de Requisitos, Arquitetura, Desenho & Construção, Testes e
     Implementação em produção. Habituado a utilizar contagem FPA/NESMA, métodos Ágeis,
     gestão Scrum, práticas XP & OpenUP, CAPEX e OPEX, BABOK, BPM CBOK, SOX e
     Segurança da Informação. Profundo conhecimento de PMBOK, BABOK, PRINCE2, ITIL e
     COBIT.

             Agile Coach e Trainer de Scrum Masters e Product Owners.

             Resumindo:

             PMP, PRINCE2, Agile, Coach, Trainer, Mentor, PMO-CC ... (oba, mudança)


[PAGINA 99]
                                                                                  PLA Solutions   99



        PLA Solutions

        Somos um grupo de profissionais experientes nas áreas de operação de escritório de
projetos e programas do portfólio de iniciativas (alinhados com a estratégia e a gestão da
capacidade de entrega). Temos certificações de reconhecimento internacional em projetos
através do PMI/USA (PMP) e UK Government (PRINCE2).

        Conhecimentos certificados no mundo Lean Management (Six Sigma Black Belt) e
Métodos Ágeis de desenvolvimento de produtos e serviços (Scrum Master, Product Owner,
Agile Coach, Trainer e Scaled Expert).

        Além das certificações, temos experiência PRÁTICA em implementações de sucessos
em gestão de PMOs, seguindo o pensamento Lean enxuto e usando métodos Ágeis de
desenvolvimento de Produtos e Serviços.

        Nós somos bons de planejamento, mas temos especial disciplina na Execução com
qualidade e eficiência.

        Atuamos de modo profissional em processos de Coaching e Mentoring com
certificações internacionais, e sabemos maximizar o desenvolvimento das pessoas durante as
transformações organizacionais que promovemos. Afinal, empresas são o resultado de pessoas.

        Fazemos gestão de Mudanças de forma certificada pelo HUCMI conveniado do ACMP
Global. Tecnologia, Negócios, Produtos, Serviços e Operações de excelência são vitais, mas
somos especializados em gestão das pessoas, que fazem isso tudo acontecer.

        Vamos tomar um bom café?

        contato@plasolutions.com.br

        (11) 3280-4771 Skype

        (11) 98125-6429 WhatsApp




                                              99


[PAGINA 100]
100    Agilidade nas empresas. Guia Scrum para quem não é de TI.



              VCPRO training

              VCPRO é uma marca do grupo PLA Solutions. Nosso foco está em treinamentos
      comportamentais, de modo a auxiliar pessoas e empresas a atingir mais resultados e mais
      rápido, ainda, com maiores controles e menos riscos.

              VCPRO contribui com empresas e profissionais no desenvolvimento de competências,
      habilidades e atitudes dos líderes de sucesso.

              Através de um programa de treinamentos comportamentais para desenvolvimento de
      líderes com experiência prática em componentes da inteligência emocional, o workshop
      PMRAD Profissional Moderno RADioativo, desenvolve e auxilia pessoas e empresas a adquirir
      hábitos e atitudes vencedoras.

                             PMRAD Módulo I – liderança, inteligência emocional (12 horas)
                             PMRAD Módulo II – autoconhecimento (28 horas)
                             PMRAD Módulo III – performance pessoal (10 horas)
                             PMRAD Módulo IV – performance empresarial (encontros mensais)


[PAGINA 101]
                                                                                CAPIE Mentoring   101



        CAPIE Mentoring

        Entre os anos de 2013 e 2015 a PLA Services desenvolveu um programa de Mentoring
com metologia própria* denominado C.A.P.I.E.

- Criar um relacionamento de Mentoring
- Analisar a performance
- Preparar um plano de desenvolvimento de competências
- Implementar ações de melhoria
- Encerrar o relacionamento de Mentoring

                * por própria entenda o trabalho de compilação de parte do material de
        institutos nacionais e internacionais como: PMI - Project Management Institute, The
        IIBA - International Institute of Business Analysis, IBC - Instituto Brasileiro de
        Coaching, IFT - Instituto de Formação de Treinadores, Management Mentors USA -
        Mentores profissionais.

        O programa de Mentoring CAPIE da PLA Solutions é disponibilizado através do
Workshop Projetando VOCÊ, em duas versões: 1to1 e Group Mentoring. No relacionamento
individual 1to1, Mentor e cliente fazem um trabalho de avaliação dos skills pessoais,
mapeamento de situação As Is e To Be, desenvolvimento de metas e acompanhamento do plano
de ação até formalizar o resultado das ações no próximo ciclo de revisão de desempenho (seja
ele na periodicidade que a empresa do cliente adotar). A versão Group Mentoring do
Projetando VOCÊ, concentra o trabalho em um dia inteiro de trabalho, com avaliações
pessoais de autoconhecimento, levantamento do As Is e projeção do To Be utilizando-se de
frameworks do tipo Business Model You e Estratégia do Oceano Azul.

        Assessments específicos do PMI Competence Development Framework e
Competências do PMO VALUE RING são feitos na versão 1to1 somente.

        O Workshop Projetando VOCÊ acontece nas modalidades presencial e à distância
(Hangouts ou Skype).




                                               10
                                                1


[PAGINA 102]
102   Agilidade nas empresas. Guia Scrum para quem não é de TI.


[PAGINA 103]
                                    PMO encontros Ágeis / tech Talks / People sharing toughts   103



         PMO encontros Ágeis / tech Talks / People sharing toughts

         Ciclo de palestras presenciais e também webinários com eventos temáticos. O PMO
encontros Ágeis acontece em São Paulo/SP desde 2015, em continuação à um ciclo de palestras
realizados inicialmente em Curitiba/PR.

         São encontros descontraídos do tipo Happy-Hours mas com muito compartilhamento de
conteúdo e oportunidade de ampliar seu Networking e fazer negócios.

         Em 2017 o PMO encontros Ágeis está incorporando também duas trilhas temáticas, a
saber:

               Change Management – people sharing toughts. Encontro de profissionais do
meio de ‘Human Change Management’, que compartilham ideias e pensamentos
transformadores.
               Fintechs, Insurtechs and Agritechs – tech Talks. Encontro voltado para o
ecosistema de empresas de tecnologia que empreendem soluções de digitalização dos serviços
financeiros, de seguros e do mundo agrícola. Tão amplo quanto isto. E disruptivo do jeito que
você imagina. Venha ver isso!

         Para manter-se informado das palestras, use nosso Whats http://bit.do/whatsapp-
pmoencontrosageis – para recados, informação, link dos webinars, perfis no LinkedIn, e o
“esquenta” das palestras.

         O calendário de palestras gratuitas de PMO encontros Ágeis está neste link,
http://bit.do/pmoencontrosageis

         Traga o seu conhecimento e leve o nosso com você!

         Seja você também um palestrante.

         Roberto NAVAS Pinheiro
         contato@plasolutions.com.br
         (11) 3280-4772 (Skype)
         (11) 98125-6429 (WhatsApp)

         linkedin.com/in/navas




                                              10
                                               3


[PAGINA 104]
104   Agilidade nas empresas. Guia Scrum para quem não é de TI.


[PAGINA 105]
                                                      PMO Global Alliance & PMO VALUE RING      105



        PMO Global Alliance & PMO VALUE RING




        A PMO Global Alliance é gestora de uma comunidade global de profissionais em
PMOs com mais de 5.000 membros, em diversos países. A PMO Global Alliance provê serviços
e produtos desenvolvidos a partir do trabalho colaborativo e da inteligência coletiva desta
comunidade, dentre eles, a metodologia PMO VALUE RING.




        PMO VALUE RING é uma metodologia internacional, fundamentada por um amplo
estudo com a consolidação da experiência de profissionais maduros de diversos países, apoiada
por uma ferramenta comercializada na modalidade SaaS (Software as a Service), com a
possibilidade de adoção de modo simplificado pelas organizações, sem investimento em TI.

        PMO VALUE RING apoia a criação, a revisão e a operação do PMO, com foco na
geração de valor efetivo para a organização




                                               10
                                                5


[PAGINA 106]
106    Agilidade nas empresas. Guia Scrum para quem não é de TI.


              PMO VALUE RING fornece recomendações e orienta a configuração do PMO a partir
      de experiências que foram bem sucedidas, e semelhantes a situação real da organização.

              Parte fundamental e indissociável da PMO VALUE RING é que o seu mind-set propõe:

              - que o PMO seja visto como um “prestador de serviços”;

              - que como tal, ele possui “clientes”, seus stakeholders, cada qual com necessidades e
      também expectativas, normalmente, específicas;

              - que atender as expectativas dos stakeholders é a melhor forma de gerar valor
      percebido;

              - que o PMO cumprirá esse objetivo provendo “serviços” (funções) da melhor forma
      possível.

              A metodologia e ferramenta PMO VALUE RING não é vendida isolada somente como
      licença de uso de software, mas sim acompanhada de profissionais acreditados para operá-la e
      obter o maior benefício para os stakeholders. Há 3 certificações no programa. A saber:


[PAGINA 107]
                                             PMO Global Alliance & PMO VALUE RING   107




       Para garantir e maximizar o retorno sobre os seus investimentos em PMO,
procure um professional certificado em PMO-CC (PMO VALUE RING Certified
Consultant) através de um dos RSP (Regional Solution Partner).

      O amigo Américo Pinto é Presidente do Conselho da PMO Global Alliance.




                                       10
                                        7


[PAGINA 108]
108   Agilidade nas empresas. Guia Scrum para quem não é de TI.
