Numeros=input("A que numero desea convertir?\nEscribe binario o decimal.\n")

N=int(input("ingrese el numero que desea convertir\n"))


if Numeros=="binario":
    residuo_acum=""
    while N!=0:
        residuo=str(N%2)
        residuo_acum=residuo_acum+residuo
        N=N//2
    residuo_acum=int(residuo_acum[::-1])
    print(residuo_acum)

elif Numeros=="decimal":
    exponente=0
    residuo_acum=0
    while N!=0:
        residuo=N%10
        bi=residuo*(2**exponente)
        residuo_acum=residuo_acum+bi
        exponente=exponente+1
        N=N//10
    print(residuo_acum)