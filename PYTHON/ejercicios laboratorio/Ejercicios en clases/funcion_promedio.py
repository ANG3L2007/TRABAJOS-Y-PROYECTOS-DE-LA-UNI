def calprom(notas):
    cont=0
    acum=0
    
    while cont<len(notas):
        acum=acum+notas[cont]
        cont=cont+1
        
    promedio=acum/cont
    return promedio

notas=[5,2,4,6,5,2,5]
promedio=calprom(notas)
print(promedio)