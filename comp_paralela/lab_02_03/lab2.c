/*
*UNIVERSIDADE PRESBITERIANA MACKENZIE
*FACULDADE DE COMPUTACAO E INFORMATICA
*COMPUTACAO PARALELA - ATV. PROGRAMACAO
*
*NOME: RODRIGO PIGATTO PASQUALE
*TIA: 41816080
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct{
   char nome[100];
   int idade;
   float altura;
}Pessoa;

int leArquivo(FILE *arquivo, Pessoa pessoas[100]){
    char str[100];
    int i = 0;
    fseek(arquivo, 0, SEEK_SET);
    while(feof(arquivo)==0){
        fgets(str, 100, arquivo);
        strcpy(pessoas[i].nome, str);
        
        fgets(str, 100, arquivo);
        pessoas[i].idade = atoi(str);
        
        fgets(str, 100, arquivo);
        pessoas[i].altura = atof(str);
        i++;
    }
    return i;
}

int comparePessoa(const void * a, const void * b)
{
  if (((Pessoa*)a)->altura <  ((Pessoa*)b)->altura ) return -1;
  if (((Pessoa*)a)->altura ==  ((Pessoa*)b)->altura) return 0;
  if (((Pessoa*)a)->altura >  ((Pessoa*)b)->altura ) return 1;
}

int main()
{
    Pessoa pessoas[100], pessoa;
    int num_pessoas = 0;
    FILE *fptr;

    if ((fptr = fopen("pessoas.txt","r")) == NULL){
        printf("Erro ao abrir o arquivo!");
        exit(1);
    }
    num_pessoas = leArquivo(fptr, pessoas);
    fclose(fptr);
    qsort(pessoas, num_pessoas,sizeof(pessoa),comparePessoa);
    fptr = fopen("pessoas_ordenado.txt", "w");
    for(int i = 0; i < num_pessoas; i++){
        fprintf(fptr, pessoas[i].nome);
    }
    fclose(fptr);
    return 0;
}