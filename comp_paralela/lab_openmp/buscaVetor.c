/*UNIVERSIDADE PRESBITERIANA MACKENZIE
 *FACULDADE DE COMPUTAÇÃO E INFORMÁTICA
 * 
 *NOME: RODRIGO P PASQUALE
 *TIA: 41816080 
 * 
 */

#include <stdio.h>
#include <stdlib.h>
#define MAX 65536

int vet[MAX];

int main(){
	int i;
    int n = 65534;
    for(i = 0; i < MAX; i++) vet[i] = i;
    //busca
    for(i = 0; i < MAX; i++){
        if(vet[i] == n){
            printf("Elemento encontrado na posicao: %d\n", i);
            break;
        }
    }


}
