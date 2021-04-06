#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int *vetor;

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
    i = 0;
    j = 0;
    k = l;
    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            arr[k] = L[i];
            i++;
        }
        else
        {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
    while (i < n1)
    {
        arr[k] = L[i];
        i++;
        k++;
    }
    while (j < n2)
    {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void mergesort(int arr[], int l, int r)
{
    if (l < r)
    {
        int m = (l + r) / 2;
#pragma omp parallel sections
        {
#pragma omp section
            {
                mergesort(arr, l, m);
            }
#pragma omp section
            {
                mergesort(arr, m + 1, r);
            }
        }
        merge(arr, l, m, r);
    }
}

void print(int v[], int arr_size)
{
    for (int i = 0; i < arr_size; i++)
    {
        printf(" %d", v[i]);
    }
    printf("\n");
}

int main()
{
    long arr_size = 1000000;
    vetor = malloc(arr_size * sizeof(int));
    /* inicializa o vetor para o pior caso */
    for (int i = 0; i < arr_size; i++)
    {
        vetor[i] = arr_size - i;
    }
    //print(vetor, arr_size);
    mergesort(vetor, 0, arr_size - 1);
    //print(vetor, arr_size);
    free(vetor);
    return 0;
}
