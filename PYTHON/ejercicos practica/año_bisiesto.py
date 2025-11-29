año=int(input("ingrese un año para determinar si el año es bisiesto \n"))

if año % 400 == 0:
    print("el año" , año, "es bisiesto")

elif año % 100 == 0:
    print("el año " ,año, " no es bisiesto")
    
elif año % 4 == 0:
    print("el año " ,año, " es bisiesto")
    
else :
    print("el año " ,año, " no es bisiesto")
    
    