def rereplace(cadena, buscar,  reemplazar):
    cont = 0
    nueva_cadena = ""
    while cont != len(cadena):
        if buscar == cadena[cont:cont+len(buscar)]:
            nueva_cadena += reemplazar
            cont += len(buscar)
        else:
            nueva_cadena += cadena[cont] 
            cont += 1
            
    return nueva_cadena

cadena = input("Ingrese una cadena de texto\n")
buscar = input("Ingrese el texto que desea reemplazar?\n")
reemplazar = input("Ingrese el nuevo texto que desea ingresar\n")
print (rereplace(cadena, buscar, reemplazar))