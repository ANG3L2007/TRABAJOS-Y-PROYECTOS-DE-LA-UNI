correo=input("ingrese el correo  ")

separador=correo.split(".")
separador2=separador[1].split("@")
nombre=separador[0]
apellido=separador2[0]

print("Bienvenido, ", nombre," ",apellido,"!" )


"""juan.perez@udea.co"""