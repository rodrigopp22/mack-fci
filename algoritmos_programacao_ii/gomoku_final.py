'''
UNIVERSIDADE PRESBITERIANA MACKENZIE
FACULDADE DE COMPUTAÇÃO E INFORMÁTICA

ALGORITMOS E PROGRAMAÇÃO II
ATIVIDADE 06: GOMOKU


--DISCENTES:

GABRIEL FERREIRA DE CARVALHO - TIA: 41806107
RODRIGO P. PASQUALE - TIA: 41816080

--DESCRIÇÃO:
    - inicializarTabuleiro(): cria o tabuleiro para o jogo, uma matriz 15x15 preenchida por 0s;

    - decidirJogador(): essa função, a partir da biblioteca random, decide qual jogador irá iniciar o jogo;

    - inputDeCoordenadas(): recebe como argumento o tabuleiro do jogo e insere nele as coordenadas escolhidas pelo
    jogador. Utilizando a função step() consegue validar as entradas. Retorna a linha e coluna inseridas pelo jogador;

    - game(): executa a lógica do jogo, em essência, alterna o turno dos jogadores, checa o estado do jogo - se há um
    empate ou uma vitória - e imprime o tabuleiro a cada turno passado. Anuncia o ganhador da partida;

    - printTabuleiro(): é chamada na função game() para imprimir o tabuleiro com as coordenadas novas;

    - step(): recebe como parâmetro a posição que o jogador deseja inserir e checa se está livre ou não. Retorna
    True ou False;

    - status(): essa função executa quatro outras funções para checar se há um vencedor. Caso haja, retorna 1, caso
    contrário, retorna 0. As funções executadas são:
        - verificarColunas(): checa na coluna selecionada pelo jogador se há cinco pontos, do mesmo jogador, seguidos;

        - verificarLinhas(): checa na linha selecionada pelo jogador se há cinco pontos, do mesmo jogador, seguidos;

        - verificarDiagonais(): checa as diagonais possíveis de haver cinco pontos, do mesmo jogador, seguidos;

        - verificarEmpate(): checa se há espaços disponíveis no tabuleiro, caso não haja ele retorna 3;
'''
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
    lin = int(input("Digite a linha: "))
    col = int(input("Digite a coluna: "))
    while (lin > 14) or (col>14):
        lin = int(input("Coordenadas inválidas! Por favor, digite uma nova coordenada para a linha (entre 0 e 14): "))
        col = int(input("Coordenadas inválidas! Por favor, digite uma nova coordenada para a coluna (entre 0 e 14): "))
    varStep = step(tabuleiro, lin, col)
    while varStep == False:
        lin = int(input("Posição já ocupada! Por favor, digite uma nova coordenada para a linha: "))
        col = int(input("Posição já ocupada! Por favor, digite uma nova coordenada para a coluna: "))
        while (lin > 14) or (col > 14):
            lin = int(input("Coordenadas inválidas! Por favor, digite uma nova coordenada para a linha (entre 0 e 14): "))
            col = int(input("Coordenadas inválidas! Por favor, digite uma nova coordenada para a coluna (entre 0 e 14): "))
        varStep = step(tabuleiro, lin,col)
    return lin,col

def game(tabuleiro,jogador):
    v = 0
    while v == 0:
        if jogador%2 == 0:
            print("É a vez do jogador branco: ")
        else:
            print("É a vez do jogador preto: ")
        lin, col = inputDeCoordenadas(tabuleiro)
        tabuleiro[lin][col] = jogador
        v = status(tabuleiro, lin, col, jogador)
        if jogador%2 != 0:
            jogador += 1
        else:
            jogador -= 1
        printTabuleiro(tabuleiro)
    if v == 1:
        print("O jogador preto venceu!")
    elif v == 2:
        print("O jogador branco venceu!")
    else:
        print("Empate!")
def printTabuleiro(A):
    N = len(A)
    M = len(A[0])
    print('     0    1    2    3    4    5    6    7    8    9    10   11   12   13   14')
    for i in range(len(A)):
        print('{:{align}{width}}'.format(i, align='^', width='3'), end='')
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
    empate = verificarEmpate(tabuleiro)
    if (coluna == 1 or linha == 1 or diagonal == 1) and empate != 3:
        return jogador
    if empate == 3:
        return 3
    return 0

def verificarColunas(tabuleiro,posicao2,jogador):
    contC = 0 #contC é a variável que conta a sequência de colunas
    for i in range(15): #percorre a coluna da coordenada selecionada
        if tabuleiro[i][posicao2] == jogador:
            contC += 1
            if contC == 5:
                return 1
        else:
            contC = 0
    return 0
def verificarLinhas(tabuleiro,posicao1,jogador):
    contL = 0 #contL é a variável que conta a sequência de linhas
    for j in range(15): #percorre a linha da coordenada selecionada
        if tabuleiro[posicao1][j] == jogador:
            contL += 1
            if contL == 5:
                return 1
        else:
            contL = 0
    return 0

def verificarDiagonais(tabuleiro,posicao1,posicao2,jogador):
    contD, contD2 = 0,0 #contD, contD2 são variáveis que conta a sequência nas diagonais
    i, j = posicao1,posicao2
    m,n = posicao1, posicao2
    while i != 0 and j != 0: #retorna para o começo da diagonal da esquerda da coordenada selecionada
        i -= 1
        j -= 1
    while m != 0 and n != 14: #retorna para o começo da diagonal da direita da coordenada selecionada
        m -= 1
        n += 1
    while i <= 14 and j <= 14: #percorre a diagonal da esquerda
        if tabuleiro[i][j] == jogador:
            contD += 1
            if contD == 5:
                return 1
        else:
            contD = 0
        i += 1
        j += 1
    while m<=14 and n>= 0: #percorre a diagonal da direita
        if tabuleiro[m][n] == jogador:
            contD2 += 1
            if contD2 == 5:
                return 1
        else:
            contD2 = 0
        m += 1
        n -= 1

    return 0

def verificarEmpate(tabuleiro):
    contE = 0 #contE é a variável que conta se há espaços disponíveis
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[0])):
            if tabuleiro[i][j] == 1 or tabuleiro[i][j] == 2:
                contE += 1
    if contE == (len(tabuleiro)*len(tabuleiro[0])):
        return 3

def main():
    tabuleiro = inicializarTabuleiro()
    printTabuleiro(tabuleiro)
    jogador = decidirJogador()
    game(tabuleiro, jogador)

#----MAIN

main()