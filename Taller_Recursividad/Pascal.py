import sys

def posiciones(colum,fila):
    if(colum == 0) or (fila ==colum):
        return 1
    else:
        return posiciones(colum-1,fila-1) + posiciones(colum,fila-1)

def Pascal(num):
    
    for f in range(num):
        for c in range(f+1):
            sys.stdout.write(str(posiciones(c,f))+' ')
        print('\n')
num=int(input("Ingrese el exponente correspondiente a la fila del triangulo "))
print(Pascal(num+1))