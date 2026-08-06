formato = input("ingrese el prefijo, numero y la ciudad")

cont = 0
informacion = ""

while cont != len(formato):
    caracter = formato[cont]
    if caracter == "+":
        while True:
            cont += 1
            caracter = formato[cont]
            if caracter == "-":
                break
            else:
                continue
    elif caracter == "-":
        informacion += " "
        informacion += caracter
        informacion += " "
    else:
        informacion += caracter
    cont += 1
print(informacion)