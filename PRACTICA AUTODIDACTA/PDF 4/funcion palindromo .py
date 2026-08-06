def palindromo(cadena):
    cont = 0
    nueva_cadena = ""
    while cont != len(cadena):
        if str.isalpha(cadena[cont]):
            nueva_cadena += cadena[cont]
            nueva_cadena = str.lower(nueva_cadena)
        cont += 1
    return nueva_cadena == nueva_cadena[::-1]

cadena = input("ingrese una cadena de texto para determinar si es palindromo :\n")
print(palindromo(cadena))