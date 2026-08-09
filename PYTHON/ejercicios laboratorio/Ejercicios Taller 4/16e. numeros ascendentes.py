def ascendente(cadena):
    numero = ""
    anterior = -1
    i = 0

    while i < len(cadena):
        if cadena[i] != "-":
            numero += cadena[i]
        else:
            actual = int(numero)
            if actual < anterior:
                return False
            anterior = actual
            numero = ""
        i += 1

    actual = int(numero)
    if actual < anterior:
        return False

    return True

cadena = "213-321-422"
print(ascendente(cadena))