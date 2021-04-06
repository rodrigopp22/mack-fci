def bubbleSort(v):
    j = 0
    while j < len(v) - 1:
        i = 0
        while i < len(v) - 1:
            if (v[i] > v[i+1]):
                temp = v[i]
                v[i] = v[i+1]
                v[i+1] = temp
            i+=1
        j+=1
    return v

def insert(v):
    for j in range (1, len(v)):
        i = j - 1
        x = v[j]
        while (i >= 0) and (x < v[i]):
            v[i+1] = v[i]
            i -= 1
        v[i+1] = x
    return v

v = [5,1,3,7,9,10,4]
bolha = bubbleSort(v)
insercao = insert(bolha)
print(bolha)
print(insercao)
