file=open("datos.csv", mode="a")

file.write("nuevo registro \n")


while True:
    nombre = input("ingrese un nombre " )
    edad = (input ("ingrese la edad "))
    tipo_sangre = input("ingrese el tipo de sangre ")
    line= nombre+","+edad+","+tipo_sangre+"\n"
    file.write(line)
    
    respuesta=input("desea seguir ingresando archivos? (si/no)")
    
    if respuesta == "no":
        break
file.close()