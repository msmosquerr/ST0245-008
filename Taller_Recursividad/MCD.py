n=int(input("Ingrese el número mayor "))
m=int(input("Ingrese el número menor "))
def mcd(n, m):
    if m%n==0:
        print("El máximo común divisor entre ellos es ", n)
    else:
        return mcd(m,n%m)

print(mcd(m,n))