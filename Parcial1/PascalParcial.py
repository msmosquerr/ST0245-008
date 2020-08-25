

def  pascal(column,row):

        if row < 0 and column < 0:
                return 0
        elif row == 0 and column == 0:
                return 1                             

        elif column==row:
                return 1
        else:
            return pascal(column-1,row-1) + pascal(column,row-1)
def Pascal(num):

    for f in range(num):
        for c in range(f+1):
            print(str(pascal(c,f)), end=" ")
        print('\n')
num=int(input("Ingrese el exponente correspondiente a la fila del triangulo "))
print(Pascal(num+1))