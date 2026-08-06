numero_usuario = int(input("ingrese hasta que numero quiere sumar la serie \n"))
cont = 0
suma = 0
exp = 0
num = 0
while cont != numero_usuario:
    exp +=1
    num +=1
    suma = suma + num ** exp
    cont +=1
print(f"la suma total de su numero fue: {suma}")