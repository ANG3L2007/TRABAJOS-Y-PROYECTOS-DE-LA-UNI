tweet = input("ingrese el tweet que desea extraer \n")

cont = 0 
resultado = ""

while cont != len(tweet):
    
    if tweet[cont] == "#":
        while True:
            if tweet[cont] == " " or cont == len(tweet):
                break
            else:
                resultado += tweet[cont]
                cont += 1
                print(cont)
                print(tweet[cont])
                print(resultado)
                continue

    cont += 1
    
print(resultado)