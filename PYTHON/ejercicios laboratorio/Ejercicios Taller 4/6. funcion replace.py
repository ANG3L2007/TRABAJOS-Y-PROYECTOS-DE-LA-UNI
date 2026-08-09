def mi_replace (cadena,buscar,reemplazar):
    resultado=""
    i=0
    while i< len(cadena):
        if cadena[i:i+len(buscar)] == buscar:
            resultado += reemplazar
            i += len(buscar)
        else:
            resultado += cadena[i]
            i+=1
            
    return resultado

cadena=input("ingrese una cadena de texto ")
buscar=input("ingrese el texto que desea reemplazar ")
reemplazar=input("ingrese el nuevo texto que desea ingresar ")

print(mi_replace(cadena,buscar,reemplazar))

