def imprimeTabela(m,n):
    for i in range (m):
        print('')
        for j in range (n):
            print('* ', end='')

m = int(input("Digite o número de linhas: "))
n = int(input("Digite o número de colunas: "))
imprimeTabela(m,n)
