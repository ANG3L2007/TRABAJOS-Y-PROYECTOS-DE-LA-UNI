formato = input("ingrese el formato para determinar si es correcto: \n")
cont = 6
cont_uno = 0
while cont != 18:
    if formato[cont] == "1":
        cont_uno += 1
    cont += 1
    
if cont_uno % 2 == 0 and formato[18] == "1":
    print("Correcto!")
elif cont_uno % 2 == 1 and formato[18] == "0":
    print("Correcto!")
else:
    print("Incorrecto!")