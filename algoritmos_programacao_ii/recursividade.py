#RECURSIVIDADE

def fatorial(n):
    if n == 0: #BASE DA RECURSÃO (CONDIÇÃO DE PARADA)
        return 1
    else:
        return n*fatorial(n-1)
    '''
    fat = fatorial(n-1)
    fat = fat*n
    return fat
    '''

def fibs(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibs(n-1)+fibs(n-2)

def recursao(n):
    if n <=10:
        return n*2
    else:
        return recursao(recursao(n/3))

def main():
    n = int(input())
    #print(fatorial(n))
    #print(fibs(n))
    print(recursao(n))


main()
