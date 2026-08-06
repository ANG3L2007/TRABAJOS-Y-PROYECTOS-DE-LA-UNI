def repetidos(texto):
    anterior = ""
    nuevo = ""
    i = 0
    while i < len(texto):
        if texto[i] != anterior:
            nuevo += texto[i]
        anterior = texto[i]
        i += 1
    
    return nuevo
    
    
    
texto="hola muuuuundoooooo  kkkk"
print (repetidos(texto))