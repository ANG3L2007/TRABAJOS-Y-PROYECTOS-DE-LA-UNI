def imc(peso, estatura):
    return peso / (estatura * estatura)

archivo = input("Ingrese el nombre del archivo: ")

mayor_imc = 0
cedula_mayor = ""

with open(archivo, "r") as f:
    for linea in f:

        # ---------------------------------------------
        # 1. Buscamos la primera posición del espacio (cédula)
        # ---------------------------------------------
        pos1 = linea.find(" ")

        # Extraemos la cedula (desde inicio hasta el espacio)
        cedula = linea[:pos1]

        # ---------------------------------------------
        # 2. Buscamos la siguiente posición del espacio (peso)
        #    posición después del primer espacio
        # ---------------------------------------------
        pos2 = linea.find(" ", pos1 + 1)

        # Extraemos el peso (entre los dos espacios)
        peso = linea[pos1+1 : pos2]
        peso = int(peso)

        # ---------------------------------------------
        # 3. Lo que resta en la línea es la estatura
        # ---------------------------------------------
        estatura = linea[pos2+1:]
        estatura = float(estatura)

        # Calculamos el IMC usando la función
        valor_imc = imc(peso, estatura)

        # Si este IMC es mayor al que llevo guardado, lo reemplazo
        if valor_imc > mayor_imc:
            mayor_imc = valor_imc
            cedula_mayor = cedula


print("La cédula con mayor IMC es:", cedula_mayor)
print("Su IMC es:", mayor_imc)