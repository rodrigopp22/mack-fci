/*
 * Daniel Matrone
 * TIA: 41826213
 */

#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#define TAMANHO 100000 //tamanho da sequencia de fibonacci

int thread_count; //contador das threads
int *seq_fibo; //vetor com os valores da sequencia de fibonacci

void *fibo_threads(void *arg){
    if(thread_count == 0){
		seq_fibo[thread_count] = 0;
        pthread_exit(0);
    }   

   	if(thread_count == 1){
		seq_fibo[thread_count] = 1;
        pthread_exit(0);
    }

    seq_fibo[thread_count] = seq_fibo[thread_count - 1] + seq_fibo[thread_count - 2];
    pthread_exit(0);
}

int main()
{
	seq_fibo = (int *) malloc(TAMANHO * sizeof(int));
	pthread_t *threads = (pthread_t *) malloc(TAMANHO * sizeof(pthread_t));
	pthread_attr_t attr;

	pthread_attr_init(&attr);

	for(thread_count = 0; thread_count < TAMANHO; thread_count++){
		pthread_create(&threads[thread_count], &attr, fibo_threads, NULL);
		pthread_join(threads[thread_count], NULL);
	}

	printf("A sequencia Fibonacci:");

	for(int k = 0; k < TAMANHO; k++){
		printf("%d ", seq_fibo[k]);
	}
	printf("\n");

    return 0;
}

