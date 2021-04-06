def exercicio3():
    for i in range (0,10,1):
        print()
        for j in range(0,i+1,1):
            print(j, end=" ")
def exercicio4():
    for i in range (0,10,1):
        print(end=" \n")
    for j in range(0,i+1,1):
        j = 9-j
        print(j, end=" ")
        j = i
exercicio3()
exercicio4()
