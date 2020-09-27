import time

lista=[-3,-2,-1,-4,-3,-2,-3,-1]

def Negativos(lista):
    listaN=[]
    for i in lista:
        if i<0:
            listaN.append(i)
    return listaN

print(Negativos(lista))
start_time = time.time()
Negativos(lista)
print("Negativos--- %s seconds ---" % (time.time() - start_time))