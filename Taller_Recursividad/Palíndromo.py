palabra=input("Ingrese una frase, palabra o número ")
def palindromo(palabra):
    if len(palabra)<1:
       return "Es palindromo"
    else:
        if palabra[0]==palabra[-1]:
           return palindromo(palabra[1:-1])
        else:
           return "No es palindromo"

print(palindromo(palabra))
