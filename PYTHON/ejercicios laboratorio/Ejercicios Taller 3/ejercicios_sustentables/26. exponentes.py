i=int(input("ingrese un numero entero para seguir la sucesion 1^1+2^2+...n^n  "))
exponente = 0
resultado=0
numero = 0
while numero!=i:
    numero=numero+1
    exponente=exponente+1
    acum=numero**exponente
    resultado=resultado+acum
print(resultado)