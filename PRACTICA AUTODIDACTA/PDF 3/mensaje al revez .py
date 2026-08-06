mensaje = input("ingrese el mensaje que desea invertir: ")
cont = len(mensaje)
resultado = ""
while cont != 0:
    cont -= 1
    resultado = mensaje[cont]
print(resultado,cont)