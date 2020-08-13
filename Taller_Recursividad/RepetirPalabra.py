palabra = input("Ingrese la palabra: ")
def imprimir(palabra, n):
    if n < len(palabra):
        print(palabra[0:n])
        imprimir(palabra, n+1)
    else:
        print(palabra)

print(imprimir(palabra, 0))