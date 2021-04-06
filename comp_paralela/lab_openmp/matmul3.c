#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <sys/time.h>


#define N 2048

int A[N][N];
int B[N][N];
int C[N][N]= {0};


int alg_matmul2D(int m, int n, int p, int** a, int** b, int** c)
{
   int i,j,k;
#pragma omp parallel shared(a,b,c) private(i,j,k) 
   {
#pragma omp for  schedule(static)
   for (i=0; i<m; i=i+1){
      for (j=0; j<n; j=j+1){
         a[i][j]=2;
         for (k=0; k<p; k=k+1){
            a[i][j]=(a[i][j])+((b[i][k])*(c[k][j]));
         }
      }
   }
   }
   return 0;
}

int main(int argc, char *argv[]) 
{
    alg_matmul2D(N,N,N, A, B, C);
}


 