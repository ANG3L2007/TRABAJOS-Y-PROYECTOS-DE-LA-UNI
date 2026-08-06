tweet = input("ingrese el tweet que desea extraer: \n")

cont = 0
resultado = ""
while cont != len(tweet):
    
    if tweet[cont] == "#":
        while True:
            if cont == len(tweet) or tweet[cont] == " ":
                break
            else:
                resultado += tweet[cont]
                cont += 1
                continue
    cont += 1

print(resultado)