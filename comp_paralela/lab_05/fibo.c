#include <stdio.h>

#define N 10

int main(){
        int i;
        int n_ant = 0, n_atual = 1, n_ant_ant;
        for(i = 0; i < N; i++){
            n_ant_ant = n_ant;
            n_ant = n_atual;
            n_atual = n_ant_ant + n_ant;
            printf(" %d",n_atual);
        }
    return 0;
}
