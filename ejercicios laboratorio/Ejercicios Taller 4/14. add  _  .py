def guion (cadena):
    resultado="_"
    i=0
    while i<len(cadena):
        if cadena[i]==" ":
            resultado += cadena[i]
            resultado+= "_"
            i+=1
        else:
            resultado +=cadena[i]
            i+=1
        
    return resultado

cadena=input("ingrese una cadena de texto ")

print(guion(cadena))