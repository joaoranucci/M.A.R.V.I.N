# Grafos_Em_Linguagem_de_Programacao_C

Arquivo original: most_similar_papers_to_this_one/Grafos_Em_Linguagem_de_Programacao_C.docx
SHA-256 do original: 99712911f7ed1a0610efddc1ab5f9f5ad6adbe675ce41883ee6ddef136c73885

Texto extraido para consulta. As paginas abaixo usam a ordem do arquivo PDF, incluindo capas.
Parte preparada: 1/1


[DOCUMENTO WORD - TEXTO E TABELAS]
Grafos
(Em Linguagem de Programação C)
Kevim Brasil Maciel
Kevim_brasil@hotmail.com/kevim.maciel@gamail.com
Graduando Em Ciência Da Computação
Manaus/AM 2013


Grafos é um conjunto não-vazio de vértices e arestas, tais que cada arco conecta dois nós, ou seja G(V,A). De forma mais simples, um grafo é um conjunto de pontos e arcos, e esses arcos conectam esses pontos (ou nós).
                                         

Nesta apostila estudaremos a implementação do algoritmo para grafos não direcionados, não trabalharemos com grafos ponderados, pois ao final das explicações o leitor terá a capacidade de implementa-la facilmente.
Então dividimos assim o estudo dos grafos:
Grafo não direcionado:
Registro;
Main;
Menu;
Inserção das Arestas;
Impressão da lista de adjacência;
Busca em largura;
Busca em profundidade;
Para o garfo direcionado, a única coisa que mudará será a inserção das arestas, você utilizara somente o primeiro teste que é demonstrado na função. 
                                Registro
O registro é onde ficara as informações sobre o que cada espaço de memória terá que armazenar. Em relação ao registro você pode utilizar duas formas simples, uma consiste em apenas um espaço de memória de um ponteiro para uma lista de encadeada, o outro armazenará não só um ponteiro mais também qual ponto é aquele. Daremos ênfase somente a que possui dois campos, pois sua lista de adjacência será do mesmo tipo que ela, logo não precisaremos criar outro registro.
Registro com dois campos. Um para guardar o ponto do grafo e outro um ponteiro para uma lista de adjacência, lista de adjacência são todos os pontos para qual aquele ponto está ligado:
typedef struct x{
 int num;
 struct x *prox;
}x;
Aqui chamamos o tipo abstrato de dado de “x”, mas você pode colocar o nome que desejar. O registro consiste somente nisso. Mas como trabalhamos com busca em largura e em profundidade teremos mais alguns registros, um será utilizado na busca em profundidade e ambos serão utilizados na busca em largura.
typedef struct pilha{
 int num;
 struct pilha *prox;
}pilha;
Esse registro será utilizado em ambas as buscas, vale lembrar que a busca em profundidade trabalha com a ideia da pilha (LIFO) o primeiro que entra é o último a sair, e a busca em largura trabalha coma ideia da fila (FIFO) o primeiro que entra é o primeiro que sai.
typedef struct sentinela{
 struct pilha *inicio;
 struct pilha *fim;
}sentinela;
A sentinela, caso você não lembre, guarda o início e o final da fila, e é com o auxílio dela que trabalharemos a busca em largura.

                                           Main
Na main criaremos o ponteiro para o grafo, pois até agora não sabemos o tamanho dele, digo-lhes que é muito mais prático fazer um grafo dinamicamente, caso contrário toda vez que seu professor mudar o tamanho do grafo você terá que alterar seu código.
Nela havemos de ler do usuário o tamanho do grafo, ou seja, quantos pontos ele possui, e chamamos a função menu, que ficara encarregada da continuação do algoritmo.
Vejamos a Main:
int main(){
  x *grafo=NULL;
  int tam;
  printf("Tamanho do vetor: ");
  scanf("%d",&tam);
  
  grafo=(x *)malloc(tam * sizeof(x)); 
  
  if(!grafo){
   puts("ERRO\n");system("pause");exit(0); 
  }   
  system("cls");

  menu(grafo,tam);
}

                                Menu
A função menu, consiste apenas em inicializar todos os campos do nosso grafo e ler do usuário qual a opção desejada e a parti daí chamar as funções correspondente a escolha.
void menu(x *grafo, int tam){
   int op,i;

    
    for(i=0;i<tam;i++){
     grafo[i].num=i;
     grafo[i].prox=NULL;
    }
    system("cls");
    
   do{ 
    printf("\t 1 - Inserir Arestas\n");
    printf("\t 2 - Imprimir\n");  
    printf("\t 3 - Busca em Profundidade\n");   
    printf("\t 4 - Busca em Largura\n");  
    printf("\t 5 - Sair\n\n");
    printf("Opcao: ");	
    scanf("%d",&op);
    switch(op){
      case 1: grafo=insere_aresta(grafo,tam);break;
      case 2: imprime(grafo,tam);break;
      case3: busca_em_prof(grafo,tam,grafo[0].num);break;
      case4: busca_largura(grafo,tam,grafo[0].num);break;
      case 5:exit(0);break;
      default: printf(erro);break;
    }
    system("pause");
    system("cls");
   }while(op!=5);    
}
Na função menu recebemos um ponteiro para o grafo e o tamanho do grafo, utilizamos esse método de receber o tamanho do grafo por parâmetro para que não ocorra o caso de excedermos o tamanho do grafo e consequentemente ocasionar um erro gravíssimo. Feito isso as funções são chamadas segundo a ordem do usuário.

Inserção das Arestas
O objetivo desta função é criar uma lista de adjacência, lista de adjacência são todas as arestas que partem, ou chegam em determinado ponto (ou nó), você deve ter estudado isso ou em estrutura de dados avançada ou em matemática.
Assim como na função menu, recebemos um ponteiro para o garfo, e o valor do tamanho do grafo justificado anteriormente. Depois disso lemos do usuário os dois pontos, é isso que irá dizer ao programa, de onde parte a aresta e qual é o seu extremo.
Para entendermos melhor vamos olhar a imagem do início da apostila.

                                       



Ok, depois de lermos o primeiro e o segundo ponto, vamos inserir a lista de adjacência, a lista de adjacência será explicada a imagem abaixo. Possuímos nosso grafo, e a lista de adjacência será uma lista encadeada com todos os pontos para qual aquele ponto está ligado. Para explicar, usamos como exemplo, um grafo com quatro pontos, vamos explica-lo e em seguida mostrar sua lisa de adjacência.


                                      

Começamos por 0 porque como usamos um vetor, vetor em C sempre começa do zero. Aqui o ponto 0 liga o ponto 1, 2 e 3, como não é um grafo direcionado, então os pontos 1,3 e 2 também apontam para o ponto 0.

                                     
A lista de adjacência do ponto 0 será todos esses pontos que ele está ligado, mas como não é direcionado, esses pontos também vão apontar para o ponto 0
0 | 
1 | 
2 | 
3 | 

	Agora, vamos fazer a lista de adjacência do ponto 1, o ponto 1 aponta para o ponto 0, 2 e 3, mas observe na lista que o ponto 1 já possui o 0 na lista de adjacentes, então não é necessário repeti-lo. Apenas coloca-se os novos.

0 | 
1 | 
2 | 
3 | 
                                 
                                              
Como não é um grafo direcionado, esses pontos também apontam para o ponto 1.

0 | 
1 | 
2 | 
3 | 

Agora, vamos fazer a lista de adjacência do ponto 2. O ponto 2 aponta para o ponto 0, 1 e 3, mas observe na lista que o ponto 2 já possui o 0 e 1 na lista de adjacentes, então não é necessário repeti-lo. Apenas coloca-se os novos.

0 | 
1 | 
2 | 
3 | 

                                      
Como não é um grafo direcionado, esses pontos também apontam para o ponto 2. Todavia o ponto 2 já está na lista de adjacentes dos outros pontos, exceto do ponto 3, logo será o único lugar que necessário inseri-lo. 
0 | 
1 | 
2 | 
3 | 


	Observe que a lista está completa, se fossemos conferir as arestas do grafo verificaríamos que concluímos a lista de adjacentes.
A função de inserção de arestas, ou lista de adjacentes, depois de ler dois números do usuário, que são os pontos, faz dois testes, ele verifica se esses números são iguais, quando ocorre este caso, o ponto aponta para ele próprio, se essa condição for verdadeira alocamos apenas um espaço de memória, e fazemos o grafo na posição daquele número receber um novo elemento com o seu próprio valor.
if(n1==n2){
   novo=(x *)malloc(sizeof(x));       
   novo->num=n2;
   novo->prox=NULL;
   novo->prox=grafo[n1].prox;
   grafo[n1].prox=novo; 
 }
	Caso contrário, ele aloca dois espaços em memória, um para cada número, lembrando novamente de que como não é um grafo direcionado, ambos apontam para ambos.
else{
   novo=(x *)malloc(sizeof(x));
   novo->prox=NULL;
   novo->num=n2;
   novo->prox=grafo[n1].prox;
   grafo[n1].prox=novo;
   
   out=(x *)malloc(sizeof(x));
   out->prox=NULL;
   out->num=n1;
   out->prox=grafo[n2].prox;
   grafo[n2].prox=out;
 }
Depois de feito isso, a função retorna o grafo, com a lista de adjacentes alterada.
return grafo;

Função completa:
x *insere_aresta(x *grafo, int tam){
  int n1,n2,i;
  x *novo, *out;
  x *aux; 
  printf("Insira a aresta\n");
  printf("1 Ponto: ");
  scanf("%d",&n1);
  printf("2 Ponto: ");
  scanf("%d",&n2);
 
  if(n1==n2){
   novo=(x *)malloc(sizeof(x));       
   novo->num=n2;
   novo->prox=NULL;
   novo->prox=grafo[n1].prox;
   grafo[n1].prox=novo;
 }
 else{
   novo=(x *)malloc(sizeof(x));
   novo->prox=NULL;
   novo->num=n2;
   novo->prox=grafo[n1].prox;
   grafo[n1].prox=novo;
   
   out=(x *)malloc(sizeof(x));
   out->prox=NULL;
   out->num=n1;
   out->prox=grafo[n2].prox;
   grafo[n2].prox=out;
 }
   printf("\n\tOK\n\n");
   return grafo;
}

Impressão da lista de adjacentes

	Essa é uma função simples e pequena, ela consiste em receber por parâmetro um ponteiro para o grafo, e a criação de uma variável auxiliar que percorrerá toda a lista de adjacente imprimindo todos os valores enquanto a lista não for vazia, ele percorre todas as posições do vetor do grafo, imprimindo toda a lista.
void imprime(x *grafo, int tam){
  x *aux;
  int i;
  for(i=0;i<tam;i++){
   printf("Lista do Numero: %d :",grafo[i].num);
   if(grafo[i].prox==NULL)
      continue;
   aux=grafo[i].prox;
   while(aux!=NULL){
    printf(" ->%d",aux->num);
    aux=aux->prox;
   }
   puts("\n\n");
  }
}

Essa função funciona assim, pegamos a primeira posição do vetor, e sua lista de adjacente. Vamos ver um exemplo com apenas três pontos.
0 | 
1 | 
2 | 

Depois de pegarmos essa posição, uma variável auxiliar recebe a lista de adjacência.


0 | 
1 | 
2 | 

A função ira imprimir o valor que está na variável auxiliar, depois passará para a próximo da lista de adjacência, até que o próximo seja nulo, quando isso ocorrer a função passará para a próxima posição do grafo, se ele estava na posição 0 vai para 1, se estava na 1 vai para a posição 2 assim sucessivamente, até que tenha imprimido todas as posições do grafo.

                          Busca em largura

Para utilizamos a busca em largura, precisamos de duas funções que são encarregadas do controle da busca, são elas insere_fila e desenfila aqui utilizaremos ambos os registros mostrados no início desta apostila.
Vejamos a função de insere fila:
sentinela *insere_fila(sentinela *sent, int num){
  pilha *aux=(pilha *)malloc(sizeof(pilha));  
  aux->num=num;
  aux->prox=NULL;
  if(sent->fim==NULL){
   sent->inicio=aux;
   sent->fim=aux;
 }else{
    sent->fim->prox=aux;
    sent->fim=aux; 
  }
  return sent;
}

Recebemos por parâmetro a nossa sentinela que contém o início e o fim da fila, e o número que deseja-se inserir na fila. A parti daí aloca-se um espaço de memória para o novo elemento. Verifica se o fim da fila é vazio, se for, significa que a fila está vazia, então tanto o início e o fim da sentinela receberam o mesmo valor. Caso contrário o próximo do fim (sent->fim->prox) receberá o novo elemento, e atualizamos o último elemento da fila.
Vejamos a função desenfila:
sentinela *desenfila(sentinela *fila){
 pilha *aux;
  if(fila->inicio == fila->fim){
  free(fila->inicio);
  fila->inicio=NULL;
  fila->fim=NULL;
 } else{
  aux=fila->inicio;
  fila->inicio=fila->inicio->prox;
  free(aux);
 }     
return fila;
}
Também recebemos a sentinela por parâmetro, a parti daí são testes. Verificamos se o inicio e o fim da sentinela são iguais, se forem é porque a fila só tem um elemento, ambos então recebem o valor nulo, senão, utiliza-se um auxiliar para receber o início da fila, e passa o início para o próximo elemento, em seguida libera-se a memória da variável auxiliar que contém o antigo início da fila.
Agora vejamos a função de busca em largura:
Recebemos por parâmetro três dados: o ponteiro para o grafo, o tamanho do grafo, e o início, que é nele que obtemos a informação de onde iniciar a busca em largura. Alocamos a sentinela, e inicializamos seus campos. Criamos um vetor chamado visitado para manter o controle de quais elemento já foram visitados para que não o fiquemos repetindo.
Logo de início chamamos a função para inserir na fila o início que foi escolhido pelo usuário. Em seguida entramos no principal loop do programa, sua condição é enquanto o fim da sentinela for diferente de vazio, “while(sent->fim!=NULL)”. Então em uma variável receberá o número que está no início da fila e desalocamos o início da fila, e verifica se o vetor de visitado naquela posição é diferente de 0, se for colocamos o valor 1 nele, o 1 significa que ele já foi visitado. Imprimimos esse valor, pronto já começamos a busca em largura.
Uma variável auxilia vai receber a lista de adjacência daquela posição do grafo. Entramos então no próximo teste da função, enquanto a variável auxiliar for diferente de nulo, “while(aux!=NULL)”. Enquanto essa condição não é verdadeira verificamos se o vetor de visitados na posição que há no campo número da variável auxiliar já foi visitado “if(visitados[aux->num]!=1)”, se ele ainda não foi visitado, a função insere_fila é chamada, enviando o valor da variável auxiliar que está caminhando na lista adjacente.

void busca_largura(x *grafo, int tam, int inicio){
   int visitados[tam];
   sentinela *sent=(sentinela *)malloc(sizeof(sentinela));
   sent->inicio=NULL;
   sent->fim=NULL;
   int i,pos,y;
   x *aux;
   for(i=0;i<tam;i++){
    visitados[i]=0;
   }    
   
   sent=insere_fila(sent,inicio);
   
   while(sent->fim!=NULL){
     pos=sent->inicio->num;
     sent=desenfila(sent);
     if(visitados[pos]!=1){
       visitados[pos]=1;
       printf(" %d ",pos);
       }
     aux = grafo[pos].prox;
     while(aux!=NULL){
       if(visitados[aux->num]!=1){
         y=aux->num;                          
         sent=insere_fila(sent,y);
         }
      aux=aux->prox;
      }
    }
  }

Busca em profundidade

	A busca em profundidade é semelhante a busca em profundidade, aqui não utilizaremos a sentinela, vamos utilizar somente a pilha. Também utilizaremos duas funções, a empilha e desempilha.

pilha *empilha(pilha *p, int num){
  pilha *aux=(pilha *)malloc(sizeof(pilha));
  aux->num=num;
  if(p!=NULL)
    aux->prox=p;
  else
   aux->prox=NULL;
  return aux;
}

Essa função simples, recebe um ponteiro para a pilha, aloca um espaço em memória, e faz dois testes simples: verifica se a pilha não está vazia, se sim, o novo valor no campo próximo receberá o início da pilha, senão o auxiliar é considerado instantaneamente o início da pilha.

pilha *desempilha(pilha *p){
  pilha *aux=p;
  
  p=p->prox;
  free(aux);
  return p;
}

A função desempilha simplesmente passa o início da pilha para o próximo elemento e libera a memória.
A busca em profundidade é idêntica a função de busca em largura, somente alguns detalhes foram retirados.
void  busca_em_prof(x *grafo, int tam, int inicio){
   int visitados[tam];
   pilha *p=NULL;
   int i,pos,y;
   x *aux;
   
   for(i=0;i<tam;i++){
    visitados[i]=0;
   }    
   
   p=empilha(p,inicio); 
   while(p!=NULL){
     pos=p->num;
     p=desempilha(p);
     if(visitados[pos]!=1){
       visitados[pos]=1;
       printf(" %d ",pos);
       }
     aux = grafo[pos].prox;
     while(aux!=NULL){
       if(visitados[aux->num]!=1){
         y=aux->num;                          
         p=empilha(p,y);
         }
      aux=aux->prox;
      }
    }
  }
	Toda ideia logica das buscas em profundidade e largura são as mesmas.

Código completo Grafo
#include<stdio.h>
#include<stdlib.h>
/************************************************************/
typedef struct x{
 int num;
 struct x *prox;
}x;

typedef struct sentinela{
 struct pilha *inicio;
 struct pilha *fim;
}sentinela; 

typedef struct pilha{
 int num;
 struct pilha *prox;
}pilha;
/************************************************************/
char erro[]={"Opcao Invalida!\n"};

/************************************************************/
void menu(x *grafo, int tam);
x *insere_aresta(x *grafo, int tam);
void imprime(x *grafo, int tam);
void busca_em_prof(x *grafo, int tam, int inicio);
pilha *desempilha(pilha *p);
pilha *empilha(pilha *p, int num);
sentinela *insere_fila(sentinela *filas, int num);
sentinela *desenfila(sentinela *filas);
void busca_largura(x *grafo, int tam, int inicio);
/************************************************************/
int main(){
  x *grafo=NULL;
  int tam;
  
  printf("Tamanho do vetor: ");
  scanf("%d",&tam);
  
  grafo=(x *)malloc(tam * sizeof(x));
  
  if(!grafo){
   puts("ERRO\n");system("pause");exit(0);
  }   
  system("cls");
  menu(grafo,tam);
}
/************************************************************/
void menu(x *grafo, int tam){
   
   int op,i;
    
    for(i=0;i<tam;i++){
     grafo[i].num=i;
     grafo[i].prox=NULL;
    }
    system("cls");
    
   do{ 
    printf("\t 1 - Inserir Arestas\n");
    printf("\t 2 - Imprimir\n");  
    printf("\t 3 - Busca em Profundidade\n");   
    printf("\t 4 - Busca em Largura\n");  
    printf("\t 5 - Sair\n\n");
    printf("Opcao: ");
    scanf("%d",&op);
    switch(op){
      case 1: grafo=insere_aresta(grafo,tam);break;
      case 2: imprime(grafo,tam);break;
      case 3: busca_em_prof(grafo,tam,grafo[0].num);break;
      case 4: busca_largura(grafo,tam,grafo[0].num);break;
      case 5:exit(0);break;
      default: printf(erro);break;
    }
    system("pause");
    system("cls");
   }while(op!=5);    
}
/************************************************************/

x *insere_aresta(x *grafo, int tam){
  
  int n1,n2,i;
  x *novo, *out;
  x *aux;
  
  printf("Insira a aresta\n");
  printf("1 Ponto: ");
  scanf("%d",&n1);
  printf("2 Ponto: ");
  scanf("%d",&n2);
 
  if(n1==n2){
   novo=(x *)malloc(sizeof(x));       
   novo->num=n2;
   novo->prox=NULL;
   novo->prox=grafo[n1].prox;
   grafo[n1].prox=novo;
 }
 else{
   novo=(x *)malloc(sizeof(x));
   novo->prox=NULL;
   novo->num=n2;
   novo->prox=grafo[n1].prox;
   grafo[n1].prox=novo;
   
   out=(x *)malloc(sizeof(x));
   out->prox=NULL;
   out->num=n1;
   out->prox=grafo[n2].prox;
   grafo[n2].prox=out;
 }
   printf("\n\tOK\n\n");
   return grafo;
}

/************************************************************/
void imprime(x *grafo, int tam){
  x *aux;
  int i;
  for(i=0;i<tam;i++){
   printf("Lista do Numero: %d :",grafo[i].num);
   if(grafo[i].prox==NULL)
      continue;
   aux=grafo[i].prox;
   while(aux!=NULL){
    printf(" ->%d",aux->num);
    aux=aux->prox;
   }
   puts("\n\n");
  }
}
/************************************************************/
pilha *empilha(pilha *p, int num){
  pilha *aux=(pilha *)malloc(sizeof(pilha));
  aux->num=num;
  if(p!=NULL)
    aux->prox=p;
  else
   aux->prox=NULL;
  return aux;
}

/************************************************************/
pilha *desempilha(pilha *p){
  pilha *aux=p;
  
  p=p->prox;
  free(aux);
  return p;
}
/************************************************************/
void  busca_em_prof(x *grafo, int tam, int inicio){
   int visitados[tam];
   pilha *p=NULL;
   int i,pos,y;
   x *aux;
   
   for(i=0;i<tam;i++){
    visitados[i]=0;
   }    
   
   p=empilha(p,inicio);
   while(p!=NULL){
     pos=p->num;
     p=desempilha(p);
     if(visitados[pos]!=1){
       visitados[pos]=1;
       printf(" %d ",pos);
       }
     aux = grafo[pos].prox;
     while(aux!=NULL){
       if(visitados[aux->num]!=1){
         y=aux->num;                          
         p=empilha(p,y);
         }
      aux=aux->prox;
      }
    }
  } 
/************************************************************/
sentinela *insere_fila(sentinela *sent, int num){
   pilha *aux=(pilha *)malloc(sizeof(pilha));
  aux->num=num;
  aux->prox=NULL;
  
  if(sent->fim==NULL){
   sent->inicio=aux;
   sent->fim=aux;
 }else{
    sent->fim->prox=aux;
    sent->fim=aux; 
  }
  return sent;
}
/************************************************************/
sentinela *desenfila(sentinela *fila){
 pilha *aux;
 
 if(fila->inicio == fila->fim){
  free(fila->inicio);
  fila->inicio=NULL;
  fila->fim=NULL;
 } else{
  aux=fila->inicio;
  fila->inicio=fila->inicio->prox;
  free(aux);
 }     
return fila;
}
/************************************************************/
void busca_largura(x *grafo, int tam, int inicio){
   int visitados[tam];
   sentinela *sent=(sentinela *)malloc(sizeof(sentinela));
   sent->inicio=NULL;
   sent->fim=NULL;
   int i,pos,y;
   x *aux;
   
   for(i=0;i<tam;i++){
    visitados[i]=0;
   }    
   
   sent=insere_fila(sent,inicio);
   while(sent->fim!=NULL){
     pos=sent->inicio->num;
     sent=desenfila(sent);
     if(visitados[pos]!=1){
       visitados[pos]=1;
       printf(" %d ",pos);
       }
     aux = grafo[pos].prox;
     while(aux!=NULL){
       if(visitados[aux->num]!=1){
         y=aux->num;                          
         sent=insere_fila(sent,y);
         }
      aux=aux->prox;
      }
    }
  }