'''

ATIVIDADE 01: SISTEMAS DE COORDENADAS 2D
NOME: RODRIGO PIGATTO PASQUALE
TIA: 41816080

--DOCUMENTAÇÃO--

Este programa tem o objetivo de escrever um programa que, a partir de uma origem
transladada (x,y) do sistema de coordenadas cartesianas e uma quantidade N de
pontos, informa para cada ponto qual seu quadrante transladado, os pontos de
maior e menor valor junto de suas respectivas distâncias e o percentual de pontos
por quadrante (sem considerar os pontos que estão na abscissa ou ordenada transla-
dadas.)

- Os pontos que estão na abscissa ou na ordenada transladada serão tratados como
pontos pertencentes à origem.
    Exemplo de saída: "Ponto ( i , j ) está na origem."

-Há três funções:
    * distanciaPontos: calcula a distância entre os pontos (i,j) da origem (x,y)
    * porcentagemPontos: calcula a porcentagem de pontos em cada quadrante, a partir
    do total de coordenadas de entrada e do número de pontos em cada quadrante.
    * qualQuadrante: determina em qual quadrante está a coordenada (i,j) em relação
    à origem (x,y)

- As coordenadas, para terem sua entrada padrão (x,y) com vírgula, são lidas como
string, separadas com .split e depois convertidas para int.
'''
import math

#FUNÇÔES:

def distanciaPontos(i,j,x,y):
    
    distancia = math.sqrt((((i-x)**2))+((j-y)**2))
    
    return distancia


def porcentagemPontos(cont1Q, cont2Q, cont3Q, cont4Q, N):
    
    porcentagem1Q = (cont1Q/N)*100

    porcentagem2Q = (cont2Q/N)*100

    porcentagem3Q = (cont3Q/N)*100

    porcentagem4Q = (cont4Q/N)*100

    print("Porcentagem de pontos do 1o quadrante: ", porcentagem1Q,"%")

    print("Porcentagem de pontos do 2o quadrante: ", porcentagem2Q,"%")

    print("Porcentagem de pontos do 3o quadrante: ", porcentagem3Q,"%")

    print("Porcentagem de pontos do 4o quadrante: ", porcentagem4Q,"%")

    
def qualQuadrante(i,j,x,y):

    cont1Q, cont2Q, cont3Q, cont4Q = 0,0,0,0

    if ( i > x and j > y ):

        print("Ponto (", i,",", j,") está no 1o quadrante.")

        cont1Q += 1

    elif  ( i < x and j > y ):

        print("Ponto (", i,",", j,") está no 2o quadrante.")

        cont2Q += 1

    elif ( i < x and j < y ):

        print("Ponto (", i,",", j,") está no 3o quadrante.")

        cont3Q += 1

    elif ( i > x and j < y ):

        print("Ponto (", i,",", j,") está no 4o quadrante.")

        cont4Q += 1

    else:

        print("Ponto (", i,",", j,") está na origem.")

    return cont1Q, cont2Q, cont3Q, cont4Q

#PROGRAMA PRINCIPAL:

x,y = input("Digite a coordenada transladada:").split(',')

x = int(x)

y = int(y)

#X e Y são  são recebidas como string e tratadas como inteiro através da função int()

numeroCoords = int(input("Digite o numero de coordenadas que serão inseridas: "))

cont, cont1Q,cont2Q,cont3Q,cont4Q = 0,0,0,0,0

while cont < numeroCoords:
    
    i,j = input("Digite a coordenada: ").split(",")

    i = int(i)

    j = int(j)

    cont1,cont2,cont3,cont4 = qualQuadrante(i,j,x,y)
    
#contNQ, com N de 1 a 4, são as variáveis contadoras de pontos localizados em seu enésimo quadrante

    cont1Q = cont1 + cont1Q

    cont2Q = cont2 + cont2Q

    cont3Q = cont3 + cont3Q

    cont4Q = cont4 + cont4Q

    distancia = distanciaPontos(i,j,x,y)
    
#as condicionais abaixo comparam as distâncias e obtém a maior e menor, a partir de da função distanciaPontos    
    if ( cont == 0 ):

        menor = distancia

        maior = distancia

        pontoMaiorA = i

        pontoMaiorB = j

        pontoMenorA = i

        pontoMenorB = j

    elif ( distancia < menor ):

        menor = distancia

        pontoMenorA = i

        pontoMenorB = j

    elif ( distancia > maior ):

        maior = distancia

        pontoMaiorA = i

        pontoMaiorB = j

    cont += 1
    

print("\n\n")

print("Ponto (", pontoMenorA,",", pontoMenorB,") é o mais próximo. Distância =%.2f"% menor)

print("Ponto (", pontoMaiorA,",", pontoMaiorB,") é o mais distante. Distância =%.2f"% maior)

print("\n\n")

porcentagemPontos(cont1Q, cont2Q, cont3Q, cont4Q, numeroCoords)
