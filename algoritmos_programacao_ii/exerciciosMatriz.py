def exercicio01(M):
    
    '''
    Dado a matriz Anxm, faça uma função que recebe a matriz Anxm por
    parâmetro, em seguida a função aloca e devolve sua transposta At,
    onde A[i][j] = At[j][i] para qualquer i e j.
    '''
    Mt = [None]*len(M)
    for i in range(len(M)):
        Mt[i] = [0]*len(M)
    print(Mt)
    for j in range(len(Mt[0])):
        for k in range(len(Mt)):
            Mt[j][k]=M[k][j]
    return Mt

def exercicio02(M):

    '''
    Escreva uma função que receba uma matriz nxm de números inteiros
    e devolva o maior valor presente nesta matriz.
    '''
    maior = 0
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] > maior:
                maior = M[i][j]
    return maior

def exercicio03(M):
    
    '''
    O traço de uma matriz é a soma dos elementos de sua diagonal principal.
    Implemente uma função que receba uma matriz quadrada
    (número de linhas = número de colunas) e devolva o seu traço.
    ''' 
    traco = 0
    for i in range(len(M)):
        for j in range(len(M[0])):
            if i == j:
                traco += M[i][j]
    return traco

def exercicio04(M):

    '''
    Dizemos que uma matriz quadrada A é simétrica se e somente se
    A[i][j] = A[j][i]. Implemente uma função para verificar se uma
    matriz de números inteiros é simétrica, se a matriz for simétrica
    sua função retorna true e false caso contrário.
    '''
    cont = 0
    cont1 = 0
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == M[j][i]:
                cont += 1
            cont1 += 1
    if cont == cont1:
        return True
    else:
        return False

def exercicio05(a,b):
    

    '''
    Escreva uma função que recebe por parâmetros duas matrizes, A e B,
    com n linhas e m colunas. Sua função deve calcular a soma de A + B
    e armazena na matriz Cnxm e ao final retornar a matriz C.
    '''
    c = [None]*len(a)
    for i in range(len(a)):
        c[i] = [0]*len(a)
    for j in range(len(c)):
        for k in range(len(c[0])):
            c[j][k] = a[j][k] + b[j][k]
            
    return c

def exercicio06(a,b):
    
    '''
    Dadas a matriz Anxn e o vetor B com n elementos,
    calcule a multiplicação de A por B, e armazene na matriz Cnx1.
    '''
    c = [0]*len(a)
    for i in range(len(a)):
       for j in range(len(a[0])):
           aux = a[i][j]*b[i]
           c[i] = c[i] + aux
    return c

def exercicio07(a,b):
    
    '''
    Dadas duas matrizes Amxn e Bnxp. Obter a matriz Cmxp onde C = AxB.
    '''
    c = [0]*len(a)
    for i in range(len(b[0])):
        c[i] = [0]*len(b[0])
    for j in range(len(a)):
       for k in range(len(b[0])):
           for l in range(len(a[0])):
               c[j][k] += a[j][l]*b[l][k]
               
    return c

def exercicio08(q):
    '''
    Dizemos que uma matriz quadrada inteira é um quadrado mágico se a
    soma dos elementos de cada linha, a soma dos elementos de cada coluna
    e a soma dos elementos das diagonais principal e secundária são todas
    iguais.
    Escreva uma função que recebe uma matriz quadrada Anxn e retorna true se a
    matriz for um quadrado mágico e false caso contrário
    '''
    cont = 0
    qntSomas = len(q)*2+2
    somas = [0]*qntSomas
    for i in range(len(q)):
        soma = 0
        for j in range(len(q[0])):
            soma += q[j][i]
        somas[i] = soma

    for i in range(len(q)):
        soma = 0
        for j in range(len(q)):
            soma += q[i][j]
        somas[(i+len(q))] = soma

    soma = 0
    for i in range(len(q)):
        for j in range(len(q)):
            if i == j:
                soma += q[i][j]
        somas[(len(q)*2)] = soma

    for i in range(len(q)-1,0,-1):
        soma = 0
        for j in range(len(q)):
            soma += q[i][j]
        somas[(len(q)*2+1)] = soma

    for i in range(len(somas)-1):
        if somas[i] == somas[i+1]:
            cont += 1
            print(cont)
    print(somas)
    if cont == len(somas)-1:
        return True
    else:
        return False
    
    return somas

def exercicio09(m):
    soma = 0
    percurso = "1,2,3,2,5,1,4"
    percurso = percurso.split(",")
    for j in range(len(percurso)):
        percurso[j] = int(percurso[j])-1
    print(percurso)
    print(m)
    
    for i in range(len(percurso)-1):
        posicao = percurso[i] 
        soma += m[posicao][percurso[i-1]]
        
    return soma
            
    
            
def main():
    #matriz1 = [[0,-1,5],[6,2,0]]
    matriz = [[1,2,3990],[7,10,11]]
    matrizQuadrada = [[1,1,1],[1,1,1],[1,1,1]]
    matrizA = [[1,2,3],[4,5,6]]
    matrizB = [[1,2],[3,4],[5,6]]
    quadradoMagico = [[8,0,7],[4,5,6],[3,10,2]]
    quadradoMagico2 = [[16,2,3,13],[5,11,10,8],[9,7,6,12],[4,14,15,1]]
    vetorM = [2,3]
    distanciaCidades = [[0,15,30,5,12],[15,0,10,17,28],[30,10,0,3,11],[5,17,3,0,80],[12,28,11,80,0]]
    print(exercicio09(distanciaCidades))
    #print(exercicio08(quadradoMagico2))
    #print(exercicio07(matrizA, matrizB))
    #print(exercicio06(matrizA,vetorM))
    #print(exercicio05(matrizA,matrizB))
    #print(exercicio04(matrizQuadrada))
    #print(exercicio01(matriz1))
    #print(exercicio02(matriz))
    #print(exercicio03(matrizQuadrada))
    
    


main()
