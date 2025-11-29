numero=int(input("ingrese un numero para buscar los numeros menores que sean primos:  "))
while numero!=0:
    D=0
    i=1
    while i<=numero:
        if numero%i==0:
            D=D+1
        i=i+1
    if D==2:
            numero_primo=numero
            print(numero_primo)
    numero=numero-1
