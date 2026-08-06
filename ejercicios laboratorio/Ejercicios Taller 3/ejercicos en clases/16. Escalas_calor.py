unidades = input("digitar unidades base: digite k, f o c    ")
if unidades == "k":
    k=float(input("digite la temperatura kelvin "))
    f=(k-273.5)*9/5+32
    c=(k-273.15)
    print("La temperatura en farenheit: ",  f)
    print("la temperatura en celsius es: ", c)
elif unidades == "c":
    c=float(input("digite la temperatura en celsius  "))
    k=(c+273.15)
    f=(c*9/5)+32
    print("la temperatura en kelvin es: ", k)
    print("la temperatura en farenheit es: ", f)
elif unidades == "f" :
    f=float(input("digite las unidades en farenheit   "))
    c=(f-32)*5/9
    k=(f-32)*5/9 + 273,15
    print("la temperatura en celsius es: ", c)
    print("la temperatura en kelvin es: ", k)