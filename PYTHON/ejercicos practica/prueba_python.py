def promedio(notas):
    acum=0
    cont=0
    
    while cont<len(notas):
        acum=acum+notas[cont]
        cont=cont+1
        
    prom=acum/cont
    return promedio
notas=[4,6,8,5,8,1]
prom=promedio(notas)
print(prom)