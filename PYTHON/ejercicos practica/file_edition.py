import csv
import os

archivo = "datos2.csv"
escribir_encabezado = not os.path.exists(archivo) or os.path.getsize(archivo) == 0

with open(archivo, mode="a", newline="") as file:
    escritor = csv.writer(file)

    if escribir_encabezado:
        escritor.writerow(["Nombre", "Edad", "Tipo de sangre"])

    while True:
        nombre = input("Ingrese un nombre: ")
        edad = input("Ingrese la edad: ")
        tipo_sangre = input("Ingrese el tipo de sangre: ")

        escritor.writerow([nombre, edad, tipo_sangre])

        respuesta = input("¿Desea seguir ingresando registros? (si/no): ")
        if respuesta.lower() == "no":
            break
