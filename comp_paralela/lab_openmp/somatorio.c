/*    UNIVERSIDADE PRESBITERIANA MACKENZIE
 *    FACULDADE DE COMPUTAÇÃO E INFORMÁTICA
 *    LABORATÓRIO DE COMPUTAÇÃO PARALELA OPENMP
 *    
 *    NOME: RODRIGO PIGATTO PASQUALE
 *    TIA: 41816080
 * 
*/

#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define MAX 1073741824

int main(int argc, char *argv[]){
    long long soma = 0.0;
    int vetor[MAX];
    int i;
    #pragma omp parallel for private(i)
    for (i = 0; i < MAX; i++) vetor[i] = 1;
    #pragma omp parallel for private(i)
    for (i = 0; i < MAX; i++) soma += vetor[i];
    printf("%lld", soma);
}
