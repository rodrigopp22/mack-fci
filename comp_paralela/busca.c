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

#define base 2
#define exp 16

int* vetor;
long N = 55555;

void Busca(long tamanho_vetor){
    int t_id = omp_get_thread_num();
    int num_threads = omp_get_num_threads();
    long start_index = t_id * (tamanho_vetor / num_threads);
    long end_index = (t_id+1) * (tamanho_vetor / num_threads);
    if(t_id == num_threads-1) end_index = tamanho_vetor;
    int i;
    for(i = start_index; i < end_index; i++){
        if(vetor[i] == N) printf("\nElemento encontrado na posicao: %d",i);
    } 
}

int main(int argc, char* argv[]){
    int thread_count = strtol(argv[1], NULL, 10);
    int tamanho_vetor = 65536;
    vetor = malloc(tamanho_vetor*sizeof(int));
    # pragma omp parallel for num_threads(thread_count)
    for(int n=0; n<tamanho_vetor; ++n){
        vetor[n] = n;
    }
    # pragma omp parallel num_threads(thread_count)
    Busca(tamanho_vetor);
    return 0;
}