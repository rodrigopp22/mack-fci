
'''
UNIVERSIDADE PRESBITERIANA MACKENZIE - FACULDADE DE COMPUTAÇÃO E INFORMÁTICA
ALGORITMOS E PROGRAMAÇÃO II
ATIVIDADE 02: "PISCINAS E BALDES"

--DISCENTES:
RODRIGO PIGATTO PASQUALE TIA: 41816080

GABRIEL FERREIRA DE CARVALHO TIA: 41806107

--

DESCRIÇÃO:

O programa consiste em três funções básicas: uma para criar um vetor de tamanho N, outra
para ordenar este vetor e a última que mostra o resultado do jogo, baseando-se no resultado obtido pela variável [cont], que é retornada da função ordenaVetor.

- Função criaVetor: ela cria um vetor de tamanho [N], sendo [N] um valor dado pelo usuario, e depois com um loop for preencher esse vetor com os valores desejados pelo usuario.

- Função ordenaVetor: ela recebe o vetor obtido na função criaVetor e, através de dois laços aninhados, percorre-o inteiramente, verificando para cada posição, se a próxima é maior que a anterior, caso isso ocorra, ele faz a substituição da posição delas em (1) e um contador faz a soma para cada instância de ocorrência da condição. Ao final, ela retorna o valor do contador.

- Função mostraResultado: faz exatamente o que o nome diz, recebe como parâmetro o contador da função anterior, ordenaVetor, e através de uma condicional determina o vencedor e imprime para o usuário.
'''

def criaVetor():

    N = int(input("Digite o tamanho da sequência: "))

    vetor = [0]*N

    for i in range(0,len(vetor),1):

        vetor[i] = int(input("Digite um inteiro:"))

    return vetor   

def ordenaVetor(vetor):

    cont = 0
    
    contadorVencedor = 0

    for i in range (len(vetor)):

        for j in range (len(vetor)-1):

            if vetor[j] > vetor[j+1]:

                vetor[j],vetor[j+1] = vetor[j+1],vetor[j] #(1)

                cont += 1

    return(cont-1)

def mostraResultado(resultado):

  if ((resultado%2) == 0):

    print("Marcelo ganhou!")

  else:

    print("Carlos ganhou!")

  
                

#-----MAIN

mostraResultado(ordenaVetor(criaVetor()))
