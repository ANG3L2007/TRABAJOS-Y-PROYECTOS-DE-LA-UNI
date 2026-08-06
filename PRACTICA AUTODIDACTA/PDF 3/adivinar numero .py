Rango = int(input("ingrese un rango de numeros \n"))
valor_minimo = 0
valor_maximo = Rango
valor_medio = Rango // 2 

while True:
    if valor_minimo != valor_maximo:
        respuesta = input(f"el numero es mayor a {valor_medio}? \n responda (si/no): ")
        
        if respuesta == "si":
            valor_minimo = valor_medio
            valor_medio = valor_minimo // 2 + valor_medio
            respuesta_2 = input(f"tu numero es {valor_medio}? si/no \n")
            if respuesta_2 == "si":
                break

        if respuesta == "no":
            valor_maximo = valor_medio
            valor_medio = valor_medio - valor_maximo // 2
            respuesta_2 = input(f"tu numero es {valor_medio}? si/no \n")
            if respuesta_2 == "si":
                break