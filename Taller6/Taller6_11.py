import random
A=[]
B=[]
C=[]
def almacenar(lista,n):
    for i in range(0,n):
        lista.append(random.randint(1,10))
    return lista
almacenar(A,100)
almacenar(B,60)
C.extend(A)
C.extend(B)
def QuickSort(lista):
    izq=[]
    der=[]
    centro=[] 
    if len(lista)>1:
        pivote=lista[len(lista)-1]
        for i in lista:
            if i<pivote:
                izq.append(i)
            elif i==pivote:
                centro.append(i)
            else:
                der.append(i)
        return QuickSort(izq) + centro + QuickSort(der)
    
    else:
        return lista
lista1=A
lista2=B
lista3=C
print("Lista A ordenada: ",QuickSort(lista1))
print("Lista B ordenada: ",QuickSort(lista2))
print("Lista C ordenada: ",QuickSort(lista3))
print("La lista C tiene",len(C),"elementos")
