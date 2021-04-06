import math
#def distanciaPontos():

#def porcentagemPontos(cont1Q, cont2Q, cont3Q, cont4Q, N):
    


x,y = input("Digite a coordenada:").split(',')
x = int(x)
y = int(y)
print (x,y)
cont1Q, cont2Q, cont3Q, cont4Q = 0,0,0,0
numeroCoords = int(input("Digite o numero de coordenadas que serão inseridas: "))
cont = 0
while cont < numeroCoords:
    i,j = input("Digite a coordenada: ").split(",")
    i = int(i)
    j = int(j)
    if ( i > x and j > y ):
        print("Ponto (", i,",", j,") está no 1o quadrante.")
        cont1Q += 1
    elif  ( i < x and j > y ):
        print("Ponto (", i,",", j,") está no 2o quadrante.")
        cont2Q += 1
    elif ( i < x and j < y ):
        print("Ponto (", i,",", j,") está no 3o quadrante.")
        cont3Q += 1
    elif ( i > x and y < 0 ):
        print("Ponto (", i,",", j,") está no 4o quadrante.")
        cont4Q += 1
    else:
        print("Ponto (", i,",", j,") está na origem.")

    distMenor = math.sqrt((((x-i)**2))+((y-j)**2)))
    menor = distMenor
    if ( distMenor < menor ):
        
    cont += 1
