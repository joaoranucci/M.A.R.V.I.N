# LINGUAGEM_DE_PROGRAMACAO_ESTRUTURADA_CAP

Arquivo original: most_similar_papers_to_this_one/LINGUAGEM_DE_PROGRAMACAO_ESTRUTURADA_CAP.pdf
SHA-256 do original: ac82dee8c2d2d6f7d8fa76b4bbb7e5da980d847fc30386c2b8ad3530fd04beda

Texto extraido para consulta. As paginas abaixo usam a ordem do arquivo PDF, incluindo capas.
Parte preparada: 1/1


[PAGINA 1]
                LINGUAGEM DE PROGRAMAÇÃO ESTRUTURADA
                            CAPÍTULO 1 – APRESENTANDO O C#

1.1 - Apresentação
       Quando fazemos nossas compras em um supermercado, é comum encontrarmos um
código de barras impresso nos produtos expostos em suas prateleiras. Este código nada mais é
do que um código de identificação do produto (tal qual o nosso conhecido RG). Ao passarmos
este produto em um dos diversos caixas do supermercado, este código é submetido a uma
leitura, via leitora ótica. Identificado e reconhecido como um registro de um banco de dados,
que representa todos os produtos a venda nesta empresa, é então efetuada a venda. Este
processo consiste na informação e inclusão do preço, quantidade e valor final do produto na
lista de compra do cliente, emissão de nota fiscal e/ou de compra do produto e, conseqüente
baixa do produto no banco de dados do supermercado. Ao lermos e entendermos este
processo pode-se identificar a figura do computador como o principal protagonista desta
história e de diversas outras. Através destas máquinas é possível controlar o fluxo de
passageiros de todas as linhas de metrô de uma cidade, controlar o fluxo de trens do metrô em
função de sua demanda, controlar e visualizar milhares de contas bancárias de uma instituição
financeira, bem como da movimentação de todas elas, editar e armazenar uma receita de bolo
em um arquivo texto, fazer a leitura de sinais eletrônicos enviados por um satélite
geoestacionário e transformá-los em uma imagem para fins de previsão meteorológica de uma
cidade, país ou até continente e muito mais.
       Podemos reconhecer que o computador faz parte de nossas vidas. Ele executa, com
maestria, muitas tarefas que seriam impossíveis de serem realizadas manualmente em um
tempo recorde, podendo repetí-las indefinidamente.
       Assim como nos seres humanos, um computador precisa ser ensinado antes de realizar
tais tarefas. Por exemplo, antes de realizar uma operação matemática simples deve ser
inserido na sua memória um modelo que represente, passo a passo, como esta operação será
realizada, ou seja, como ele receberá estes dados, onde eles serão armazenados, como e qual
operação matemática será realizada com estes dados, para quais valores de dados esta
operação será válida e, para finalizar, como o resultado desta operação será armazenado e/ou
apresentado ao usuário. Este modelo é também conhecido como programa de computador,
código computacional, ou simplesmente programa e consiste em um conjunto de instruções
elaboradas por um programador que resulte na realização de uma tarefa.




                              Linguagem de Programação Estruturada                         3


[PAGINA 2]
       A elaboração, implementação e execução de um programa de computador pode ser um
processo bastante complexo e requer profissionais especializados com bons conhecimentos
sobre as formas que um computador opera, bem como das linguagens de programação que
permitem que compõe os programas de computadores. Também é necessário o conhecimento
e a familiaridade com uma plataforma de desenvolvimento de programas em uma linguagem
de programação.


1.2 – Linguagens de Programação


       Um programa de computador em execução está realizando um conjunto de instruções
que foram armazenadas em sua memória sob a forma de uma linguagem apropriada ao seu
entendimento, denominada linguagem de máquina. Programas com estas propriedades são
denominados programas executáveis e apresentam como característica própria a extensão
.exe no nome do arquivo em que foi escrito (ou implementado). Programar em uma
linguagem de máquina é uma tarefa muito complexa em função de suas características. Para
contornar este problema é que foram desenvolvidas as linguagens de programação.
       Linguagens de programação consistem em um conjunto de formas e regras para se
escrever instruções, denominadas sintaxes, que submetidas a algumas transformações
(compilação e linkagem) resultam na linguagem de máquina. É segundo este processo que
programas de computadores são elaborados, Figura 1.



             Programa                                                     Programa
                                             Programa
                Fonte                                                     Executável
                                                Objeto
            (Linguagem     Compilação                         Linkagem   (Linguagem
                                            (Linguagem
                 de                                                           de
                                               Objeto)
           Programação)                                                    Máquina)


         Figura 1 – Representação esquemática dos processos de Compilação e Linkagem



       Para que estas transformações sejam realizadas de uma forma prática e com poucos,
ou nenhum erro, uma plataforma (ou ferramenta) de desenvolvimento é utilizada. No nosso
caso empregaremos a plataforma Visual C# Express. Esta plataforma faz parte de um
conjunto de plataformas denominado Visual Studio Express e pode ser “baixado” (em
inglês-download:termo comum quando carregamos, ou copiamos, um arquivo via internet)
gratuitamente do site da Microsoft. Tanto o Visual C# Express como o Visual Studio


                            Linguagem de Programação Estruturada                       4


[PAGINA 3]
Express, são ferramentas disponibilizadas gratuitamente pela Microsoft e seu uso permite o
desenvolvimento de uma infinidade de programas em sua linguagem apropriada. O
procedimento para baixar estas plataformas será detalhado posteriormente.
         A linguagem “C#” (pronuncia-se C- Sharp) é uma evolução da linguagem “C” e é
reconhecida pela infinidade de recursos que ela dispõe. Trata-se de uma linguagem
estruturada, pois, permite que um programa possa ser elaborado segundo estruturas de
programação pré-estabelecidas.


1.3 – Procedimentos para download da plataforma Microsoft Visual C# Express

         Para baixar e instalar a plataforma Visual C# Express precisamos acessar, via um
navegador da internet, a página correspondente da Microsoft com este recurso. Para tanto,
acesse o endereço: http://www.microsoft.com/express/download/
         Será apresentada uma página conforme a figura abaixo:




        Figura 2 – Apresentação inicial da página de download do Visual Studio Express

Role a página através da barra de rolagem lateral até aparecer uma “etiqueta” ou “banner”
indicado como uma área de download do Visual C# Express (a única opção de download é na
                                              versão em inglês), Figura 3.

                                                                       Observe que ao lado da janela que indica o
                                                                       idioma desejado para download e instalação
                                                                       da plataforma aparece o hipertexto
                                                                       Download.      Posicione o ponteiro do
                                                                       “mouse” sobre este hipertexto e clique com o
                                                                       botão esquerdo do mouse para iniciar o
                                                                       processo. Aparecerá uma caixa com uma

  Figura 3 – “Etiqueta” ou “Banner” de download do Visual C# Express

                                              Linguagem de Programação Estruturada                               5


[PAGINA 4]
mensagem para execução ou instalação de um arquivo (executável) denominado vcssetup.exe,
Figura 4. Este arquivo, quando executado, realiza a instalação do Visual C# Express em seu
computador. Selecione e clique na opção salvar. Salve o arquivo em sua área de trabalho
(Desktop) ou na pasta “Meus Documentos” (recomendado). Aguarde a finalização do
processo e pode finalizar a execução de seu navegador.




                      Figura 4 – Caixa de Mensagem do Instalador



A partir deste momento o arquivo executável necessário para instalação do Visual C# Express
já está gravado em sua pasta “Meus Documentos” (ou na área de trabalho, denominada
“Desktop”). Localize este arquivo e clique duas vezes sobre ela. Siga as instruções de
instalação e aceite o contrato de acordo para instalação do programa.


1.4 – Executando o Microsoft Visual C# 2008 Express Edition


 “Programas”  “Microsoft Visual C# 2008 Express Edition” e aguarde a tela inicial da
        Para a execução do Visual C# Express, localize clicando seqüencialmente em “Início”

plataforma aparecer, Figura 5.




                      Figura 5 – Página inicial do Visual C# Express




                             Linguagem de Programação Estruturada                        6


[PAGINA 5]
        Esta é a página inicial do Visual C# Express. Esta página de apresentação nada mais é
do que uma página de Boas Vindas. Clique no “X” localizado canto superior direito da página
e vamos diretamente ao ambiente de programação. Aparecerá uma tela escura sem conteúdo
algum. Clique seqüencialmente em “File” – “New Project” e, posteriormente na janela que se
abrirá, clique duas vezes no ícone “Console Application”. A partir deste momento estaremos
visualizando a configuração básica que iremos utilizar ao longo deste curso, Figura 6.




                                            Menú de opções




                     Área de Edição de programas




                        Figura 6 – Configuração básica de programação


        Observe que a área de edição de programas já vem previamente preenchida. Vamos
alterar e inserir o programa abaixo nesta área conforme as instruções abaixo:
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication1
{
    /// <summary>
    /// Primeiro Programa em C#
    /// </summary>
    class PrimeiroPrograma
    {
        static void Main(string[] args)
        {
            //
            // Aqui sera inserido o codigo do programa
            //
            Console.WriteLine("Olá - Este é o meu primeiro programa em C# ");
        }
    }
}


        Selecione o item de menu “Debug  Start Without Debugging”. Após alguns
instantes irá aparecer uma tela conforme a figura a seguir:




                                    Figura 7 – Console de saída


                              Linguagem de Programação Estruturada                         7


[PAGINA 6]
Esta é a tela de saída (ou console de saída) do Visual C# Express. Existem outras formas de
apresentação de saída de dados, porém, ainda estão fora do escopo deste curso. Pressione
qualquer tecla e a tela de console irá desaparecer.
        Saia do aplicativo salvando (gravando) seu projeto para acessá-lo novamente quando

modo de programação, clique em “File” ”Open Project” e procure na pasta do projeto que
desejar. Para executar este mesmo programa, execute o Visual C# Express e ao entrar no

você nomeou (ao sair do projeto) o arquivo denominado “Program.cs”. Clique duas vezes
sobre este arquivo e verá que o programa que você editou foi novamente carregado na área de
edição do Visual C# Express.




                             Linguagem de Programação Estruturada                        8


[PAGINA 7]
                                      TAREFA 1 – Introdução
Nome:


RA.:                         Curso:                                     Turma:


       1) Porque um programa escrito em uma linguagem de programação deve ser convertido
          para um modelo executável ? Qual (is) são os processos que este programa deve sofrer
          até atingir este estágio ?




       2) Acesse o site de “download do Visual Studio Express e instale o Microsoft Visual C#
          2008 Express Edition. Faça o registro de sua instalação no site da Microsoft e baixe e
          execute o pacote de conversão de língua para o Português. Faça uma impressão da tela
          inicial da plataforma e cole nesta folha de tarefa.




                                Linguagem de Programação Estruturada                          9


[PAGINA 8]
3) Baseado no exemplo da apostila elabore um programa que apresente como resultado a
   seguinte mensagem no console:
   Meu nome é (Escreva na saída seu nome). Este é o meu primeiro programa em C#.
   Copie o código de seu programa abaixo.




                        Linguagem de Programação Estruturada                     10
