def remove_repeated(string):
    cont = 0
    ltr1 = ""
    ltr2 = ""
    resultado = ""
    while cont != len(string):
        ltr2 = ltr1
        ltr1 = string[cont]
        if ltr2 != ltr1:
            resultado += string[cont]
            
        cont += 1
    return resultado
string = input("ingrese el texto")
print(remove_repeated(string))
