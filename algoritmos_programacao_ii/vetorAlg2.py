def inverte(v):
    j = len(v)
    vInv = [None]*j
    for i in range (0,j,1):
        vInv[i] = v[j-1 - i]
    return vInv

def inverteResolvido(v):
    i = 0
    j = len(v) - 1
    while i < j:
        aux = v[i]
        v[i] = v[j]
        v[j] = aux
        i += 1
        j -= 1
        
def interseccao(A,B):
    print("{", end=" ")
    for i in range (0, len(A), 1):
        for j in range(0, len(B), 1):
            if A[i] == B[j]:
                resp = A[i]
                print(resp, end=" ")
    print("}", end = " ")

def diferenca(A,B):
    print("{", end=" ")
    for i in range (0, len(A), 1):
        for j in range(0, len(B), 1):
            if A[i] == B[j]:
                resp = A[i]
                print(resp, end=" ")
    print("}", end = " ")
A = [7,2,5,8,4]
B = [4,2,9,5]
interseccao(A,B)
        
        
