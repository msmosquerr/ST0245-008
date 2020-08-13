x=int(input("Ingrese la base "))
y=int(input("Ingrese el exponente "))
def potencia(x,y):
    if(y==0):
         return 1
    else:
        Potencia = x * potencia(x,y-1)

    return Potencia
print(potencia(x,y))