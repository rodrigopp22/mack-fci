/*UNIVERSIDADE PRESBITERIANA MACKENZIE
 *FACULDADE DE COMPUTAÇÃO E INFORMÁTICA
 * 
 *NOME: RODRIGO P PASQUALE
 *TIA: 41816080 
 * 
 */

#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int* vet;
long N = 55555; //numero para buscar

void busca_linear(long tamanho_vet){
    int my_rank = omp_get_thread_num();
    int num_threads = omp_get_num_threads();
    long start_index = my_rank * (tamanho_vet / num_threads);
    long end_index = (my_rank+1) * (tamanho_vet / num_threads);
    if(my_rank == num_threads-1) end_index = tamanho_vet;
    int i;
    for(i = start_index; i < end_index; i++){
        if(vet[i] == N) printf("\nElemento encontrado na posicao: %d",i);
    } 
}

int main(int argc, char* argv[]){
    int thread_count = strtol(argv[1], NULL, 10);
    int tamanho_vet = 65536;
    vet = malloc(tamanho_vet*sizeof(int));
    # pragma omp parallel for num_threads(thread_count)
    for(int n=0; n<tamanho_vet; ++n) vet[n] = n;
    # pragma omp parallel num_threads(thread_count)
    busca_linear(tamanho_vet);
    return 0;
}