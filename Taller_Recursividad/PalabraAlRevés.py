palabra=input("ingresa una palabra ")
def InvPalabra(palabra):
    if len(palabra)==1:
        return palabra
    else: 
        return palabra[len(palabra)-1] + InvPalabra(palabra[:-1])
print(InvPalabra(palabra))
