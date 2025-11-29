precio=float(input("ingrese el precio de los balones"  ))
cant=float(input("cuantos balones desea comprar?  "))
if cant <= 3 :
    precio=precio*cant
    print(precio)
elif cant >= 4 and cant <=6:
    precio=(precio*cant)-(precio*cant*0.20)
    print(precio)
elif cant > 6:
    precio=(precio*cant)-(precio*cant*0.25)
    print(precio)