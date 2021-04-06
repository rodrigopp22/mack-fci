/*  UNIVERSIDADE PRESBITERIANA MACKENZIE
 *  FACULDADE DE COMPUTAÇÃO E INFORMÁTICA
 *  COMPUTAÇÃO PARALELA - TURMA 05N11
 * 
 *  RODRIGO PIGATTO PASQUALE
 *  TIA: 41816080
 * 
 */ 
#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>
int thread_count;
double sum;
int n = 10000;
pthread_mutex_t mutex;

void *Thread_sum(void* rank){
    long my_rank = (long) rank;
    double factor;
    long long i;
    long long my_n = n/thread_count;
    long long my_first_i = my_n*my_rank;
    long long my_last_i = my_first_i + my_n;
    double my_sum = 0.0;

    if(my_first_i%2 == 0) factor = 1.0;
    else factor = -1.0;

    for(i = my_first_i; i < my_last_i; i++, factor = -factor) my_sum += factor/(2*i+1);
    pthread_mutex_lock(&mutex);
    sum += my_sum;
    pthread_mutex_unlock(&mutex);
    return NULL;
}


int main(int argc, char* argv[]){
    long thread;
    pthread_t* thread_handles;

    thread_count = strtol(argv[1], NULL, 10);
    thread_handles = malloc(thread_count*sizeof(pthread_t));
    for(thread = 0; thread < thread_count; thread++) pthread_create(&thread_handles[thread], NULL, Thread_sum, (void*)thread);
    for(thread = 0; thread < thread_count; thread++) pthread_join(thread_handles[thread], NULL);
    printf("%f", 4*sum);
    free(thread_handles);
    return 0;
}