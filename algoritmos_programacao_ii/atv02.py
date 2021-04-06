'''
UNIVERSIDADE PRESBITERIANA MACKENZIE - FACULDADE DE COMPUTAÇÃO E INFORMÁTICA
ALGORITMOS E PROGRAMAÇÃO II
ATIVIDADE 02: "PISCINAS E BALDES"

NOME: RODRIGO PIGATTO PASQUALE
TIA: 41816080

DESCRIÇÃO:

'''

def criaVetor(N):
    vetor = [0]*N
    for i in range(0,len(vetor),1):
        vetor[i] = int(input("Digite um inteiro:"))
    return vetor   

def ordenaVetor(vetor):
    cont = 0
    for i in range (len(vetor)):
        for j in range (len(vetor)-1):
            if vetor[j] > vetor[j+1]:
                vetor[j],vetor[j+1] = vetor[j+1],vetor[j]
                cont += 1
                print(cont)
                print(vetor)


#-----MAIN

N = int(input("Digite o tamanho da sequência: "))
vetor = criaVetor(N)
cont = 0
ordenaVetor(vetor)
