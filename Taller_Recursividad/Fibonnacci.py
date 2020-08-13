n=int(input("Ingrese el número de iteraciones"))
def fibonacci(n):
    if(n==0):
        print("El número debe ser mayor que cero")
        return
    if(n>0 and n<=2):
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)

print("La sucesión para ",n,"es ", fibonacci(n))
