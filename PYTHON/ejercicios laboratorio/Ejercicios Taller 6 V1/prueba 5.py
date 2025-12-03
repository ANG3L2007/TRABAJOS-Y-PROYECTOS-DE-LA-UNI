lista=[1,2,4,6,8,9,11]


def busqueda_entero(lista,objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return True,i
    return False, i


print(busqueda_entero(lista, 6))


def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    i = 0
    
    while inicio <= fin:
        i += 1                          # Contar iteraciones
        medio = (inicio + fin) // 2    
        
        if lista[medio] == objetivo:
            return medio, i
        
        elif lista[medio] < objetivo:
            inicio = medio + 1
        
        else:
            fin = medio - 1
    
    return -1, i

print(busqueda_binaria(lista, 6))