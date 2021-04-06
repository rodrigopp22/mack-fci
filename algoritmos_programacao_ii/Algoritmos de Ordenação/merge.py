def mergeSort(A,B):
  lenC = len(A) + len(B)
  C = [0]*lenC
  j=0
  k=0
  i = 0
  while j < len(A) and k < len(B):
    if A[j] < B[k]:
      C[i] = A[j]
      j += 1
    else:
      C[i] = B[k]
      k += 1
    i += 1
  while j<len(A):
    C[i] = A[j]
    j+=1
    i+=1
  while k<len(B):
    C[i] = B[k]
    k+=1
    i += 1
  return C


A = [1,3,6,7]
B = [2,4,5]

C = mergeSort(A,B)
print(C)