N=int(input("Escriba un numero, para terminar escriba cero:  "))

neg = 0
pos = 0
par = 0

while N!=0:
    if N>0:
        pos=pos+N
    else:
        neg=neg+N
    if N%2==0:
        par=par+N
    N=int(input("Escriba un numero, para terminar escriba cero:  "))
print("___________________________________")
print("Total de numeros positivos|| ", pos)
print("___________________________________")
print("Total de numeros negativos|| ", neg)
print("___________________________________")
print("total de numeros pares    || ", par)
    

