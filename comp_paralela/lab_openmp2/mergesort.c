#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <omp.h>


void inicializaVetor(int * x, int n) {
   int i,j,t;
   for (i = 0; i < n; i++)
     x[i] = i;
   for (i = 0; i < n; i++) {
     j = rand() % n;
     t = x[i];
     x[i] = x[j];
     x[j] = t;
   }
}

void print(int * x, int n) {
   int i;
   for (i = 0; i < n; i++) {
      printf("%d ",x[i]);
   } 
}

void merge(int * X, int n, int * tmp) {
   int i = 0;
   int j = n/2;
   int ti = 0;

   while (i<n/2 && j<n) {
      if (X[i] < X[j]) {
         tmp[ti] = X[i];
         ti++; i++;
      } else {
         tmp[ti] = X[j];
         ti++; j++;
      }
   }
   while (i<n/2) {
      tmp[ti] = X[i];
      ti++; i++;
   }
      while (j<n) { 
         tmp[ti] = X[j];
         ti++; j++;
   }
   memcpy(X, tmp, n*sizeof(int));

} 

void mergesort(int * X, int n, int * tmp)
{
   if (n < 2) return;
   #pragma omp task firstprivate (X, n, tmp)
   mergesort(X, n/2, tmp);
   #pragma omp task firstprivate (X, n, tmp)
   mergesort(X+(n/2), n-(n/2), tmp);
   #pragma omp taskwait
   merge(X, n, tmp);
}


int main()
{
   int n = 16000000;
   double i, f;
   int* vetor, tmp;
   vetor = malloc(n*sizeof(int));

   inicializaVetor(vetor, n);
   //print(vetor, n);
   i = omp_get_wtime();
   #pragma omp parallel
   {
      #pragma omp single
      mergesort(vetor, n, tmp);
   }
   f = omp_get_wtime();
   printf("\ntempo: %g\n",f-i);
}