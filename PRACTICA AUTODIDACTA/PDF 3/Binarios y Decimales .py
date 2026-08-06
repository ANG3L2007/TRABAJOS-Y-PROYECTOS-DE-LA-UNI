opcion = input("En que quiere convertir su numero? (binario/decimal)")

if opcion == "binario":
    resultado = ""
    numero = int(input("ingrese el numero que desea convertir a binario\n"))
    while numero != 0:
        binario = (numero % 2)
        resultado = resultado +str(binario)
        numero = numero // 2
    print (resultado[::-1])
    
elif opcion == "decimal":
    numero = (input("ingrese el numero que desea convertir en decimal \n"))
    cont = 0 
    resultado = 0
    while numero != "0":
        resultado +=  2 ** cont * int(numero[-1])
        numero = int(numero) // 10
        numero = str(numero)
        cont += 1
    print(resultado)