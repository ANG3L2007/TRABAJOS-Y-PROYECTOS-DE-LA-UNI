precio=float(input("ingrese el precio de los balones: "))
cant=float(input("ingrese la cantidad de balones que desea comprar: "))

if cant<=3:
    precio=precio*cant
elif cant>4 and cant<=6:
    precio=(precio*cant)*0.80
else:
    precio=(precio*cant)*0.75

print("el precio es de : ", precio)