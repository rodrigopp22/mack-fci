def criaVetor(n):
    vetor = [0]*n
    for i in range (len(vetor)):
        vetor[i] = i+1
    return vetor

def buscaBinaria(x,v):
    i = 0
    f = len(v)-1
    while i <= f:
        m = (i+f)//2
        if x == v[m]:
            return m
        if x > v[m]:
            i = m + 1
        else:
            f = m - 1
    return -1        

def buscaLinear(k,v):
    for i in range (1,len(v)-1,1):
        if k == v[i]:
            return k
    return -1
n = int(input("Digite o tamanho do vetor: "))
v = criaVetor(n)
x = int(input("Digite o numero que esta buscando: "))
b = buscaBinaria(x, v)
l = buscaLinear(x, v)
print(v)
print("Posição:",b)
print("Posição:",l)
