año=int(input("digite un año para determinar si es bisiesto||  "))
if  año%400 == 0:
    print(año," es un año bisiesto")
elif año%100 ==0:
    print(año, "no es un año bisiesto")
elif año%4 == 0:
    print(año, "es un año bisiesto")