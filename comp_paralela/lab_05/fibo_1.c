#include <stdio.h>
#include <pthread.h>
#define n 10

int fib_1;
int fib_2;
pthread_mutex_t mutex;


 void* fib(void *rank)                             
 {                                          
     if (n == 0) return 0;
     else if (n == 1) return 1;
     pthread_mutex_lock(&mutex);
     fib_1 = fib(n-1);
     pthread_mutex_unlock(&mutex);
     pthread_mutex_lock(&mutex);
     fib_2 = fib(n-2);
     pthread_mutex_lock(&mutex);
     return NULL;
 }                                          

 int main(int argc,char* argv[])
  {
    pthread_t *thread_handles;
    int fibo;
    pthread_create(&thread_handles,NULL,fib,NULL);
    pthread_create(&thread_handles, NULL, fib, NULL);
    pthread_join(thread_handles,NULL);
    fibo = fib_1 + fib_2;
    printf("%d\n", fibo);
    return 0;
  }