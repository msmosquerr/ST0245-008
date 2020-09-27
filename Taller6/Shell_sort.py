cont = 0
def ordenamientoDeShell(lista):
    global cont
    sublista=len(lista)//2
   
    while sublista>0:
        for inicio in range(sublista):
            pass
            ordenamiento_Insercion(lista,inicio,sublista)
        sublista=sublista//2
        cont+=1   
    return lista

def ordenamiento_Insercion(lista,inicio,espacio):
    
    for i in range(inicio+espacio,len(lista),espacio):
        #Espacio, es en cuanto se decrementa el for
        valorActual=lista[i]
        pos=i
        while pos>=espacio and lista[pos-espacio]>valorActual:
            #Si su orden es inverso cambio el signo de mayor a menor
            lista[pos]=lista[pos-espacio]
            pos=pos-espacio
        lista[pos]=valorActual
        
        print(lista)
    
lista4=[8,43,17,6,40,16,18,97,11,7]
print(ordenamientoDeShell(lista4))
print("El número de pasadas es ",cont)