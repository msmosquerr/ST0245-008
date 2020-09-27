aux=[]
def eliminar(lista):
    lista2=list(lista)
    for i in lista2:
        if i not in aux:
           aux.append(i)
        else:
           lista.remove(i)

lista=[4,4,2,11,4,9,5,4,2,11,7,3,5]
eliminar(lista)
print(lista)