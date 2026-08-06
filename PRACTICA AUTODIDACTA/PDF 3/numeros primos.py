numero = int(input("ingrese un numero para comprobar si el numero es primo \n"))
cont = numero
rest=0
while cont != 0:
    if numero % cont == 0:
        rest+=1
    cont -=1
if rest ==2 :  
    print(f"el numero  {numero} es primo")
else:
    print(f"el numero  {numero} no es primo") 