penultimo=0
ultimo=0
while True:
    Numero_Usuario=int(input("Ingrese un numero y para terminar el bucle ingrese 0\n"))
    if Numero_Usuario==0:
        print("sus ultimos numeros ingresados son: ",ultimo," y ",penultimo)
        break
    penultimo= ultimo
    ultimo=Numero_Usuario
    
