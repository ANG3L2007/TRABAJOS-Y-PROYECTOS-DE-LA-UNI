palabra = input("ingrese la frase: ")
caracter = input("ingrese el caracter para determinar su ultima posicion: ")
cont = 0
N = -1
while cont != len(palabra):
    if caracter == palabra[cont]:
        N = cont
    cont += 1
print(f"La posicion de tu caracter es: {N+1}")