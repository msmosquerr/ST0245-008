lista=[3,4,4,2,1,3,2]
lista.sort()

aux=[]
def eliminar(lista):
    lista2=list(lista)
    for i in lista2:
        if i not in aux:
            aux.append(i)
        else:
           lista.remove(i)

eliminar(lista)
print(lista)