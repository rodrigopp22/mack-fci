#EXERCÍCIOS DE RECURSIVIDADE

def exercicio04(a,n): #POTENCIAÇÃO
    '''
    Implemente uma função recursiva para calcular a potência an,
    supondo que tanto a quanto n sejam números inteiros positivos.
    '''
    if n == 0:
        return 1
    return a*exercicio04(a,n-1)

def exercicio07(m,n): #MDC
    '''
    A função abaixo calcula o máximo divisor comum dos inteiros
    positivos m e n. Escreva uma função recursiva.
    '''
    if n == 0:
        return m
    return exercicio07(n,m%n)

def exercicio08(a,b): #a*b
    if b == 1:
        return a
    else:
        return a + exercicio08(a,b-1)

#def exercicio09(n):
    
def exercicio10(a,b):
    if a == 0:
        return 0
    if a%2 != 0:
        a -= 1
        return b+exercicio10(a//2,b*2)
    else:
        return exercicio10(a//2,b*2)

def main():
    a = 10
    b = 5
    #print(exercicio04(a,b))
    #print(exercicio07(a,b))
    #print(exercicio08(a,b))
    #print(exercicio09(v,n))
    a = 27
    b = 82
    print(exercicio10(a,b))
main()
