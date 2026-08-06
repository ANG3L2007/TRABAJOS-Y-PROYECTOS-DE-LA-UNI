num = int(input("ingrese un numero para ver los numeros primos menores que este \n"))

while num !=0:
    cont = num
    rest = 0
    while cont != 0:
        if num % cont == 0:
            rest +=1
        cont -=1
    if rest == 2:
            print(num)
    num -=1