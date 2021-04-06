/* 
 * REPRESENTACAO DE GRAFOS - Versao 2021/1
 * Discentes:
 * 	 - Daniel Matrone - TIA: 41826213
 *   - Gabriel Tardochi Salles - TIA: 41822730
 *   - Rodrigo Pigatto Pasquale - TIA: 41816080
 */
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <memory.h>

/* 
 * Estrutura de dados para representar grafos
 */
typedef struct a{ /* Celula de uma lista de arestas */
	int    nome;
	struct a *prox;
}Aresta;

typedef struct vert{  /* Cada vertice tem um ponteiro para uma lista de arestas incidentes nele */
	int nome;
	int marca;
	Aresta *prim;
}Vertice;

/*
 * Declaracoes das funcoes para manipulacao de grafos 
 */
void criaGrafo(Vertice **G, int ordem);
void destroiGrafo(Vertice **G, int ordem);
int  acrescentaAresta(Vertice G[], int ordem, int v1, int v2);
int  calculaTamanho(Vertice G[], int ordem);
void imprimeGrafo(Vertice G[], int ordem);
int eConexo(Vertice G[], int ordem);
int eArvore(Vertice G[], int ordem);

/*
 * Implementacao das funcoes para manipulacao de grafos 
 */
 
/*
 * Criacao de um grafo com ordem predefinida (passada como argumento),
 *   e, inicilamente, sem nenhuma aresta 
 */
void criaGrafo(Vertice **G, int ordem){
	int i;
	*G= (Vertice*) malloc(sizeof(Vertice)*ordem); /* Alca?ao dinamica de um vetor de vertices */
	
	for(i=0; i<ordem; i++){
		(*G)[i].nome= i;
		(*G)[i].marca= 0; /* representa nao manipulado*/
		(*G)[i].prim= NULL;    /* Cada vertice sem nenua aresta incidente */
	}
}

/*
 * Deasaloca a memoria dinamica usada para armazenar um grafo.
 */
void destroiGrafo(Vertice **G, int ordem){
	int i;
    Aresta *a, *n;
    
	for(i=0; i<ordem; i++){ /* Remove lista de adjacencia de cada v?rtice */
	    a= (*G)[i].prim;
        while (a!= NULL){
              n= a->prox;
              free(a);
              a= n;
        }
	}
    free(*G);
}

/*  
 * Acrescenta uma nova aresta em um grafo previamente criado. 
 *   Devem ser passados os extremos v1 e v2 da aresta a ser acrescentada 
 * Como o grafo n?o ? orientado, para uma aresta com extremos i e j
 *   ser?o criadas, na estrutura de dados, arestas (i,j) e (j,i)
 */
int acrescentaAresta(Vertice G[], int ordem, int v1, int v2){
    Aresta * A1, *A2;
    
	if (v1<0 || v1 >= ordem) /* Testo se v?rtices sao validos */
	   return 0;
	if (v2<0 || v2 >= ordem)
	   return 0;
	
	/* Acrescento aresta na lista do vertice v1 */
	A1= (Aresta *) malloc(sizeof(Aresta));
	A1->nome= v2;
	A1->prox= G[v1].prim;
	G[v1].prim= A1;

	/* Acrescento aresta na lista do vertice v2 se v2 != v1 */
	if (v1 == v2) return 1;
	
	A2= (Aresta *) malloc(sizeof(Aresta));
	A2->nome= v1;
	A2->prox= G[v2].prim;
	G[v2].prim= A2;
	
	return 1;
}

/*  
 * Funcao que retorna o tamanho de um grafo
 */
int  calculaTamanho(Vertice G[], int ordem){
	int i;
	int totalArestas=0;
	
	for (i=0; i<ordem; i++){
		int j;
		Aresta *aux= G[i].prim;
		for(j=0; aux != NULL; aux= aux->prox, j++)
            if (aux->nome == i) j++; /* laco "conta em dobro" */
		totalArestas += j;	
	}
	return totalArestas/2 + ordem;
}

/*  
 * Imprime um grafo com uma nota??o similar a uma lista de adjac?ncia.
 */
void imprimeGrafo(Vertice G[], int ordem){
	int i;
	Aresta *aux;

	printf("\nOrdem:   %d",ordem);
	printf("\nLista de Adjacencia:\n");

	for (i=0; i<ordem; i++){
		printf("\n    V%d (Marca:%d): ", i, G[i].marca);
		aux= G[i].prim;
		for( ; aux != NULL; aux= aux->prox)
			printf("%3d", aux->nome);
	}
	printf("\n\n");
}
/* Recebe um grafo G como argumento
 * e retorna a soma das marcas dos
 * vértices de G.
 */
int verificaMarca(Vertice G[], int ordem){
	int i;
	int soma = 0;
	Vertice *aux;
	aux = G;
	for(i = 0; i < ordem; i++){
		soma += aux[i].marca;
	}
	return soma;
}

/* Recebe um grafo G como argumento e
 * retorna:
 * 1, se o grafo for conexo; ou
 * 0, se o grafo não for conexo.
 */
int eConexo(Vertice G[], int ordem){
    G[0].marca = 1; /* inicializando qualquer vertice em 1 */
	int i, trocou;
	Aresta *aux;

	while(1){
		trocou = 0;
		for (i=0; i<ordem; i++){ /*  */
			aux = G[i].prim;
			for( ; aux != NULL; aux= aux->prox){ /* percorre arestas do vertice */
				if(G[i].marca != G[aux->nome].marca){ /* se possuirem marcas diferentes, ambas necessitam ser 1 */
					G[i].marca = 1;
					G[aux->nome].marca = 1;
					trocou = 1; /* sinalizando para que o loop nao seja interrompido */
				}
			}
		}
		if(trocou == 0) break; /* se nao houverem novas arestas para marcar com 1, interrompa o programa */
	}
	printf("\n\n");
	
	if(verificaMarca(G, ordem) == ordem){
		return 1;
	}
	return 0;
}


/* Recebe um grafo G como argumento e
 * calcula seu número de arestas e
 * retorna:
 * 1, se o grafo for uma árvore; ou
 * 0, se o grafo não for árvore.
 */
int eArvore(Vertice G[], int ordem){
	int tamanho = calculaTamanho(G, ordem);
	int numArestas = tamanho - ordem;
	if(eConexo(G, ordem) && (numArestas == (ordem - 1))){
		return 1;
	}
	return 0;
}

/*
 * Programinha simples para testar a representacao de grafo
 */
int main(int argc, char *argv[]) {
	Vertice *G;
	int ordemG = 6;
		
	criaGrafo(&G, ordemG);
	acrescentaAresta(G,ordemG,0,1);
	acrescentaAresta(G,ordemG,1,2);
	acrescentaAresta(G,ordemG,1,3);
	acrescentaAresta(G,ordemG,3,4);
	acrescentaAresta(G,ordemG,3,5);

	if(eArvore(G, ordemG)){
		printf("\nEh arvore.");
	}
	else{
		printf("\nNao eh arvore.");
	}

	imprimeGrafo(G, ordemG);

	destroiGrafo(&G, ordemG);
    system("PAUSE");
	return 0;
}
