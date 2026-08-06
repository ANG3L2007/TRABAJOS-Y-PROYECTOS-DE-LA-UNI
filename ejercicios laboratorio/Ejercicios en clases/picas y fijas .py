import random

numero_secreto=random.randint(0000,9999)
numero=input("bienvenido al juego, porfavor ingrese 4 numeros diferentes")

def numero_repetido(numero):
    i=0
    usados=[]
    while i>len(numero):
        if numero[i] in usados:
            print("numero repetido, por favor ingrese otro")
        usados.append(numero[i])
        i += 1
