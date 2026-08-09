def BusEle(notas,ele):
    cont=0
    pos=False
    while cont<len(notas):
        if ele==notas[cont]:
            pos=cont
            break
        cont=cont+1
    return pos

notas_clase=[5,4,4.5,5,3,2,4,5]
buscar=0
print(BusEle(notas_clase,buscar))