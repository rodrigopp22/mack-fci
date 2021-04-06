#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <sys/time.h>


#define N 2000

int A[N][N];
int B[N][N];
int C[N][N]= {0};

void matmul(){
    int i, j, k;
    #pragma omp parallel for private(i,j,k)
    for (i = 0; i < N; i++) {
        for (k = 0; k < N; k++) {
            for (j = 0; j < N; j++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

int main(int argc, char *argv[]) 
{
    int i,j;

    for (i= 0; i< N; i++)
        for (j= 0; j< N; j++)
	{
        A[i][j] = B[i][j] = (i * N) + j + 1;
	}

# pragma omp paralell num_threads(thread_count)
matmul();

    if(N<= 3){
	for(i = 0; i < N; i++){
		for(j = 0; j < N; j++){
			printf("%d ", C[i][j]);
		}
		printf("\n");
	}
	}else{
		printf("%d\n", C[0][0]);
	}

}


 