import random

def inicializarTabuleiro():
    tabuleiro = [None]*15
    for i in range(15):
        tabuleiro[i] = [0]*15
    return tabuleiro

def decidirJogador():
    jogador = random.randint(1,2)
    return jogador

def inputDeCoordenadas(tabuleiro):
    varStep = False
    while varStep == False:
        lin = int(input("Digite a linha: "))
        col = int(input("Digite a coluna: "))
        varStep = step(tabuleiro, lin,col)
    return lin,col

def game(tabuleiro,jogador):
    v = 0
    while v == 0:
        if jogador%2 == 0:
            print("É a vez do jogador preto: ")
        else:
            print("É a vez do jogador branco: ")
        lin, col = inputDeCoordenadas(tabuleiro)
        tabuleiro[lin][col] = jogador
        v = status(tabuleiro, lin, col, jogador)
        if jogador%2 != 0:
            jogador += 1
        else:
            jogador -= 1
        printTabuleiro(tabuleiro)
    if v == 1:
        print("O jogador branco venceu!")
    else:
        print("O jogador preto venceu!")

def printTabuleiro(A):
    N = len(A)
    M = len(A[0])
    for i in range(len(A)):
        for j in range(len(A[0])):
            print("[", A[i][j], "]", end="")

        print()

def step(tabuleiro, linha,coluna):
    if tabuleiro[linha][coluna] == 0:
        return True
    else:
        return False

def status(tabuleiro,posicao1,posicao2,jogador):

    coluna = verificarColunas(tabuleiro,posicao2,jogador)
    linha = verificarLinhas(tabuleiro,posicao1,jogador)
    diagonal = verificarDiagonais(tabuleiro,posicao1,posicao2,jogador)

    if coluna == 1 or linha == 1 or diagonal == 1:
        return jogador

    return 0

def verificarColunas(tabuleiro,posicao2,jogador):
    contC = 0
    for i in range(15):
        if tabuleiro[i][posicao2] == jogador:
            contC += 1
            if contC == 5:
                return 1
        else:
            contC = 0
    return 0
def verificarLinhas(tabuleiro,posicao1,jogador):
    contL = 0
    for j in range(15):
        if tabuleiro[posicao1][j] == jogador:
            contL += 1
            if contL == 5:
                return 1
        else:
            contL = 0
    return 0

def verificarDiagonais(tabuleiro,posicao1,posicao2,jogador):
    contD, contD2 = 0,0
    i, j = posicao1,posicao2
    m,n = posicao1, posicao2
    while i != 0 and j != 0:
        i -= 1
        j -= 1
    while m != 0 and n != 14:
        m -= 1
        n += 1
    while i <= 14 and j <= 14:
        if tabuleiro[i][j] == jogador:
            contD += 1
            if contD == 5:
                return 1
        else:
            contD = 0
        i += 1
        j += 1
    while m<=14 and n>= 0:
        if tabuleiro[m][n] == jogador:
            contD2 += 1
            print(contD2)
            if contD2 == 5:
                return 1
        else:
            contD2 = 0
        m += 1
        n -= 1

    return 0

def main():
    tabuleiro = inicializarTabuleiro()
    printTabuleiro(tabuleiro)
    jogador = decidirJogador()
    game(tabuleiro, jogador)

#----MAIN

main()