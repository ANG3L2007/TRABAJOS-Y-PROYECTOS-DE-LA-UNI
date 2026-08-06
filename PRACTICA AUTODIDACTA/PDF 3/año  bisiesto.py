año = int(input("ingrese el año que desea verificar  \n"))

if año % 100 == 0:
    if año % 400 == 0:
        print (f"el año {año} es bisiesto")
    else:
        print (f"el año {año} ingresado no es bisiesto")
        
elif año % 4 == 0:
    print (f"el año {año} es bisiesto")
else:
    print (f"el año {año} ingresado no es bisiesto")