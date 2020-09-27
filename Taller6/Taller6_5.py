
listaC=[1,1,1,1,1,3,3,3,3,3,2,2,2,2,2,2]
print(listaC.sort())
print(listaC)

def Votos(listaC):
    mayor = listaC[0] #Considerando el primero como ganador
    a = votos = listaC.count(mayor) #Cuenta la cantidad de votos
    for i in range(a,len(listaC)): #Inicia desde a, porque ya tenemos los votos del hasta en el momento ganador
        if votos < listaC.count(listaC[i]):
            mayor = listaC[i]   #Si hay un candidato supera a otro se vuelve el ganador por el momento
            votos = listaC.count(mayor)
            print("El ganador es el candidato",mayor ,"con :",votos,"votos")
Votos(listaC)