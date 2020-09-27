n=(int(input("Ingrese el valor a buscar")))
matriz =[[1,2,3],[4,5,6]]
def busqueda(matriz,dato):
    for i in matriz:
        for j in range(len(i)):
            if(dato == i[j]):
                return "Si"
    return "No"                
print(busqueda(matriz,n))
