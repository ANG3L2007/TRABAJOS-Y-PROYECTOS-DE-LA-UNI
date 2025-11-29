""" Elabore una función que, dada una lista de números, retorne a una lista en la que todos los
elementos adyacentes iguales sean reducidos a un solo elemento; es decir, si se tienen los
siguientes elementos [1,2,2,3] sean retornados como [1,2,3]. Para lograr esto es necesario
crear una nueva lista o modificar la lista que se pasa como argumento de la función"""


def lista_red(lista):
    i=0
    anterior=0
    nueva=[]
    while i<len(lista):
        if lista[i] != anterior:
            nueva.append(lista[i])
        anterior = lista[i]
        i += 1
    return nueva


lista = [1,1,2,4,6,8,9,4,6,6,3,5,1]
print(lista_red(lista))
