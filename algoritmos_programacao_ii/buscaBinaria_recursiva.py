#BUSCA BINÁRIA ITERATIVA:
def BuscaBinaria( v, x ):
    i = 0 #inicio do vetor
    f = len(v)-1 #fim do vetor
    while i <= f:
        m = (i + f)//2 #divisao inteira
        if v[m] == x:
            return m
        if v[m] < x:
            i=m+1
        else: f=m-1
    return -1

#BUSCA BINÁRIA RECURSIVA
def busca(v,x,i,f):
    m = (i+f)//2
    if i > f:
        return -1
    if v[m] == x:
        return m 
    elif v[m] < x:
        i = m + 1
        return busca(v,x,i,f)
    else: #v[m] > x:
        f = m - 1
        return busca(v,x,i,f)

#---MAIN
def main():

    v = [0]*200
    for i in range(len(v)):
        v[i] = i*3 + 7*(i**2) + 12
    n = int(input("Número p/ buscar: "))
    i = 0
    f = len(v)-1
    print("Posição de",n,"é:",busca(v,n, i, f), "feito por recursão")
    print("Posição de",n,"é:",BuscaBinaria(v,n), "feito pelo método iterativo.")
    #print(v)

main()
