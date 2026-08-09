numero=int(input("digite un numero y para finalizar el ciclo escriba 0||  "))
numero1=0
numero2=0
while numero != 0 :
    numero2=numero1
    numero1=numero
    numero=int(input("digite un numero y para finalizar el ciclo escriba 0||  "))
print("el ultimo numero es:",numero1)
print("el penultimo numero es: ", numero2)