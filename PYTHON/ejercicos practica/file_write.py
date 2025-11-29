file=open("datos.csv",mode="a")


file.write ("nombre,edad,tipo_sangre")


while True:
    nombre = input("ingrese nombre: ")
    edad = input("ingresa edad: ")
    tipo_sangre = input("ingresa tipo de sangre: ")
    line = "\n"+nombre+ ","+edad+","+tipo_sangre
    file.write(line)
    
    respuesta = input("desea ingresas otro registro? (si/no) ")
    if respuesta == "no":
        break
file.close()