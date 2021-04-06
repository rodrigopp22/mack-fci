/*UNIVERSIDADE PRESBITERIANA MACKENZIE
 *FACULDADE DE COMPUTAÇÃO E INFORMÁTICA
 * 
 *NOME: RODRIGO P PASQUALE
 *TIA: 41816080 
 * 
 */

#include <stdio.h>
#include <stdlib.h>
#define MAX 1000

int A[MAX][MAX];
int B[MAX][MAX];
int C[MAX][MAX] = {0};

int main(){
	int i, j, k;

	// iniciando as matrizes
	for(i = 0; i < MAX; i++){
		for(j = 0; j < MAX; j++){
			A[i][j] = B[i][j] = (i * MAX) + j + 1;
		}
	}

	// multiplicacao
	for(i = 0; i < MAX; i++){
		for(k = 0; k < MAX; k++){
            for(j = 0; j < MAX; j++){
			    C[i][j] += A[i][k] * B[k][j];
            }
		}
	}
	// impressao
	if(MAX <= 3){
		for(i = 0; i < MAX; i++){
			for(j = 0; j < MAX; j++){
				printf("%d ", C[i][j]);
			}
			printf("\n");
		}
	} else{
		printf("%d\n", C[0][0]);
	}

}
