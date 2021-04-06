/*  
    * UNIVERSIDADE PRESBITERIANA MACKENZIE - 04/10/2020
    * CIENCIA DA COMPUTACAO - TURMA 5N11
    * LINGUAGENS FORMAIS E AUTOMATOS
    * 
    * Projeto 1 - Implementacao de AFD
    * Grupo:
    * Gabriel Tardochi Salles - TIA 41822730
    * Rodrigo Pigatto Pasquale - TIA 41816080
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
    * A funcao scanner recebe uma string de palavras e o indice i que deveria marcar sempre o caractere anterior
    * ao inicio da palavra que deve ser avaliada. Se o i+1 nao marcar o inicio de uma palavra, eh retornado -1.
    * Caso contrario, a funcao percorrera ela fazendo as transicoes de estado, retornando 0 para rejeitada, 
    * 1 para aceita como <INTEIRO> e 2 para aceita como <P.FLUTUANTE>.
*/
int scanner(char palavras[], int *i)
{
    if (palavras[*i + 1] == '\0' || palavras[*i + 1] == ' ')
    {
        ++*i;
        return (-1);
    }
q0:
    ++*i;
    if (palavras[*i] == '0')
        goto q4;
    else if (palavras[*i] == '.')
        goto q2;
    else if (palavras[*i] == '1' || palavras[*i] == '2' || palavras[*i] == '3' || palavras[*i] == '4' || palavras[*i] == '5' || palavras[*i] == '6' || palavras[*i] == '7' || palavras[*i] == '8' || palavras[*i] == '9')
        goto q1;
    else
        goto q3;
q1:
    ++*i;
    if (palavras[*i] == '0' || palavras[*i] == '1' || palavras[*i] == '2' || palavras[*i] == '3' || palavras[*i] == '4' || palavras[*i] == '5' || palavras[*i] == '6' || palavras[*i] == '7' || palavras[*i] == '8' || palavras[*i] == '9')
        goto q1;
    else if (palavras[*i] == '.')
        goto q2;
    else if (palavras[*i] == '\0' || palavras[*i] == ' ')
        return (1);
    else
        goto q3;
q2:
    ++*i;
    if (palavras[*i] == '0' || palavras[*i] == '1' || palavras[*i] == '2' || palavras[*i] == '3' || palavras[*i] == '4' || palavras[*i] == '5' || palavras[*i] == '6' || palavras[*i] == '7' || palavras[*i] == '8' || palavras[*i] == '9')
        goto q2;
    else if (palavras[*i] == '\0' || palavras[*i] == ' ')
        return (2);
    else
        goto q3;
q3:
    ++*i;
    if (palavras[*i] == '\0' || palavras[*i] == ' ')
        return (0);
    else
        goto q3;
q4:
    ++*i;
    if (palavras[*i] == '.')
        goto q2;
    else if (palavras[*i] == '\0' || palavras[*i] == ' ')
        return (1);
    else
        goto q3;
}

int main(void)
{
    /* i = indice que vai percorrer a string de palavras */
    int i = -1;
    char palavras[] = " 21 +45.67 0.123 .456  -42  xx  00.123   0";
    int tam_string = strlen(palavras);
    FILE *f = fopen("file.txt", "w");
    if (f == NULL)
    {
        printf("Erro ao tentar abrir o arquivo!\n");
        return EXIT_FAILURE;
    }

    /* enquanto nao temos resultado para todas as palavras passadas na string, chama a funcao scanner e armazena seus resultados em um arquivo */
    while (i < tam_string)
    {
        int res = scanner(palavras, &i);
        if (res == 0)
            fprintf(f, "<ERRO>\n");
        else if (res == 1)
            fprintf(f, "<INTEIRO>\n");
        else if (res == 2)
            fprintf(f, "<P.FLUTUANTE>\n");
    }

    fclose(f);
    return EXIT_SUCCESS;
}