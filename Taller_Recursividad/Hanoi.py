n=int(input("Ingrese el número de discos "))  
def Hanoi(n,torreI,torreF,torreAux):
    if(n==1):
        print("Mover el disco de la torre ", torreI, "a la torre ", torreF)

    else:
        Hanoi(n-1,torreI,torreAux,torreF)
        print("Mover el disco de la torre ",torreI, "a la torre ",torreF)
        Hanoi(n-1,torreAux,torreF,torreI)

print(Hanoi(n,1,3,2))