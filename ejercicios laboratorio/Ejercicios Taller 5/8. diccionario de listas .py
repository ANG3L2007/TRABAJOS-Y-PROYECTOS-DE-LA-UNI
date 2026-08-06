def diccionario_listas(diccionario):
    for lista, listas in diccionario.items():
        if len(listas) > 2:
            print (lista, listas)
            
diccionario = {"lista1":["hola",2,6,],
                "lista2": [[2,3,1],"hola"],
                "lista3":[2,4,5,True,False],
                "lista4": ["hola,chao"]}

diccionario_listas(diccionario)