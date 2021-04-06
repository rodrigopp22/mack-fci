/*  UNIVERSIDADE PRESBITERIANA MACKENZIE
 *  FACULDADE DE COMPUTAÇÃO E INFORMÁTICA
 *  COMPUTAÇÃO PARALELA - TURMA 05N11
 * 
 *  RODRIGO PIGATTO PASQUALE
 *  TIA: 41816080
 * 
 */ 

#include <stdlib.h>
#include <stdio.h>

int main(){
    double pi;
    double factor = 1.0;
    double sum = 0.0;
    for(int i = 0; i < 100000000; i++, factor = -factor){
        sum += factor/(2*i+1);
    }
    pi = 4.0*sum;
    printf("%f", pi);
    return 0;
}