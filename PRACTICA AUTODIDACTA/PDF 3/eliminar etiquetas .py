etiqueta = input("ingrese la etiqueta para convertirla a texto normal \n")

cont = 0
palabra = ""

while cont != len(etiqueta):
    letra = etiqueta[cont]
    if letra == "<":
        while True :
            cont += 1
            letra = etiqueta[cont]
            if letra == ">":
                break
            else:
                continue
    else:
        palabra += letra
    cont += 1
print(f"{palabra}\n")
