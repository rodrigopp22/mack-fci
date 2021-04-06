/*  UNIVERSIDADE PRESBITERIANA MACKENZIE
 *  FACULDADE DE COMPUTAÇÃO E INFORMÁTICA
 *  
 *  NOME: RODRIGO PIGATTO PASQUALE
 *  TIA: 41816080
 *  TURMA: 05N11
 * 
 *
*/

#include<pthread.h>
#include<stdio.h>
#include<stdlib.h>


void* fib(void *n)
{
  long n_ant=0,n_atual=1,soma;
  if(atoi(n)==0){
    printf("%d\n",n_ant);
    exit(0);
  }
  if(atoi(n)==1){
    printf("%ld\t%ld",n_ant,n_atual);
    exit(0);
  }
    printf("%ld\t%ld",n_ant,n_atual);
    for(int i=0;i<atoi(n)-2;i++)
    {
      soma=n_ant+n_atual;
      printf("\t%ld",soma);
      n_ant=n_atual;
      n_atual=soma;
    }
    pthread_exit(0);
}

int main(int argc,char* argv[])
{
  pthread_t *thread_handles;

  pthread_create(&thread_handles,NULL,fib,NULL);
  pthread_create(&thread_handles, NULL, fib, NULL);
  pthread_join(thread_handles,NULL);

  return 0;
}