def guion(texto):
    cont = 0
    new_texto = ""
    while cont != len(texto):
        if texto[cont] == " ":
            new_texto += "_"
            cont += 1
        else:
            new_texto += texto[cont]
            cont += 1
    return new_texto

texto = input("ingrese el texto\n")
print(guion(texto))