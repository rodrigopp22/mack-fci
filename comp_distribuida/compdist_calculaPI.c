/* 
 * UNIVERSIDADE PRESBITERIANA MACKENZIE
 * FACULDADE DE COMPUTAÇÃO E INFORMÁTICA
 * COMPUTAÇÃO DISTRIBUÍDA - CALCULA PI
 *
 * NOME: RODRIGO PIGATTO PASQUALE
 * TIA: 41816080
*/

#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define QTD_PONTOS 20000000


int main(int argc, char **argv)
{
	int myid, numprocs;
    double x,y,quad,pi;
    long i;
	long ponto_em_maquina, pontos_totais_rec, recebido_ptos_circulo = 0; 
	long resultado_total, resultado_em_circulo, pontos_em_circulo_maquina = 0;

	MPI_Init(&argc,&argv);
	MPI_Comm_size(MPI_COMM_WORLD,&numprocs);
	MPI_Comm_rank(MPI_COMM_WORLD,&myid);
	
	ponto_em_maquina = QTD_PONTOS/numprocs;

    srand(myid * 3);
    for (i = 0; i < ponto_em_maquina; i++){
                x = (double)rand() / (double)RAND_MAX;
                y = (double)rand() / (double)RAND_MAX;

                quad = ((x*x) + (y*y));
                if (quad <= 1){
                        pontos_em_circulo_maquina++; 
                }
    }
	if (myid == 0) {
        resultado_total = ponto_em_maquina;
        resultado_em_circulo = pontos_em_circulo_maquina;
        printf("Master tem  %ld pontos, o total eh %ld\n", pontos_em_circulo_maquina, ponto_em_maquina);
        for (i = 1; i < numprocs; i++) {
            MPI_Recv(&pontos_totais_rec, 1, MPI_LONG, i, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            MPI_Recv(&recebido_ptos_circulo, 1, MPI_LONG, i, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            resultado_total += pontos_totais_rec;
            resultado_em_circulo += recebido_ptos_circulo;
            printf("Worker %ld tem  %ld pontos, o total eh %ld\n", i, recebido_ptos_circulo, pontos_totais_rec);
        }
        pi = ((double)resultado_em_circulo/(double)resultado_total) * 4.0;
        printf("O valor de PI calculado: %f\n", pi);
    }else{
        MPI_Send(&ponto_em_maquina, 1, MPI_LONG, 0, 0, MPI_COMM_WORLD);
        MPI_Send(&pontos_em_circulo_maquina, 1, MPI_LONG, 0, 0, MPI_COMM_WORLD);
    }

	MPI_Finalize();
	return 0;
}
