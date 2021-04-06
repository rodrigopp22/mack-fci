/*  UNIVERSIDADE PRESBITERIANA MACKENZIE
 *  FACULDADE DE COMPUTAÇÃO E INFORMÁTICA
 *  COMPUTAÇÃO PARALELA - TURMA 05N11
 * 
 *  RODRIGO PIGATTO PASQUALE
 *  TIA: 41816080
 * 
 */ 

#include<stdio.h>
#include<stdlib.h>

long double saldo;

void* depositos(void *rank){
    for(long i = 0; i < 2147483000; i++){
        saldo -= 5;
    }
}

void* saques(void *rank){
    for(long i = 0; i < 2147483000; i++){
        saldo += 2;
    }
}

int main(int argc, char* argv[]) {

    pthread_t* thread_handles;
    

    saldo = 1000.00;

    pthread_create(&thread_handles, NULL, depositos, NULL); // a mesma funcao depositos() anterior

    pthread_create(&thread_handles, NULL, saques, NULL); // a mesma funcao saques() anterior

    pthread_join(thread_handles, NULL);

    printf("Saldo final: %.2Lf\n", saldo);

    return 0;  
}