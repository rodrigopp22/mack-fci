#include <stdio.h>  
#include <stdlib.h>  
#include <omp.h>
#include <time.h>

int *vetor;
long arr_size = 16000;

void merge(int arr[], int l, int m, int r)  
{  
    int i, j, k;  
    int n1 = m - l + 1;  
    int n2 = r - m;  
    int L[n1], R[n2];  
    for (i = 0; i < n1; i++)  
        L[i] = arr[l + i];  
    for (j = 0; j < n2; j++)  
        R[j] = arr[m + 1 + j];  
    i = 0; j = 0; k = l; 
    while (i < n1 && j < n2) {  
        if (L[i] <= R[j]) {  
            arr[k] = L[i];  
            i++;  
        }  
        else {  
            arr[k] = R[j];  
            j++;  
        }  
        k++;  
    }  
    while (i < n1) {  
        arr[k] = L[i];  
        i++;  
        k++;  
    }  
    while (j < n2) {  
        arr[k] = R[j];  
        j++;  
        k++;  
    }  
}  
  
int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

void mergesort(int arr[], int l, int r)  
{  
    if (l < r) {  
        if(r-l >= 32){
            unsigned long m = (l+r)/2;
            #pragma omp taskgroup
            {
            #pragma omp task shared(arr) untied if(r-l >= (1<<14))
            mergesort(arr, l, m);
            #pragma omp task shared(arr) untied if (r-l >= (1<<14))  
            mergesort(arr, m + 1, r);
            #pragma omp taskyield  
            }
            merge(arr, l, m, r);  
        }else{
            qsort(arr, arr_size, sizeof(long), cmpfunc);
        }

    }  
}  

void print(int v[], int arr_size){
    for(int i = 0; i < arr_size; i++){
        printf(" %d", v[i]);
    }
    printf("\n");
}

int main()  
{  
    vetor = malloc(arr_size*sizeof(int));
    /* inicializa o vetor para o pior caso */
    for(int i = 0; i < arr_size; i++){
        vetor[i] = arr_size - i;
    }
    //print(vetor, arr_size);
    double start = omp_get_wtime();
    #pragma omp parallel
    #pragma omp single
    mergesort(vetor, 0, arr_size-1);
    double stop = omp_get_wtime();
    printf("tempo: %g", stop-start);
    return 0;  
}  
