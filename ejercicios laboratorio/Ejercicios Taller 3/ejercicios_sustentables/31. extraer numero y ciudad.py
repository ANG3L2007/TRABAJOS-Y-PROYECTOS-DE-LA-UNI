formato=input("ingrese el prefijo-numero-ciudad: ")
print(formato[5:])

"""+057-3217192056-Cartagena"""

"""forma 2"""

separador=formato.split("-")
numero=separador[1]
ciudad=separador[2]
print(f"{numero}-{ciudad}")