N=int(input("escribe un numero"))
cont=1
acu=0

while cont<=N:
    acu=acu+cont
    print("el acumulador crecio en " ,cont)
    cont=cont+1
print("el acumulador es", acu)