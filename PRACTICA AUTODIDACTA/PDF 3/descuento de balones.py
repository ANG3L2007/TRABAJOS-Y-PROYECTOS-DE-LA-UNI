valor_balones=10000
cantidad_balones=int(input("digite la cantidad de balones que desea comprar: "))

if cantidad_balones >= 4 and cantidad_balones <= 6:
    descuento=0.2
elif cantidad_balones>6:
    descuento=0.25
total=valor_balones*cantidad_balones
descuento=total*descuento
total=total-descuento

print("el total de los balones que compro siguendo las normas del descuento fue el siguiente: ", total)
