import random

numero = random.randint(1,20) # numero a adivinar

intentos = 0
while True: # Ciclo infinito.
	respuesta = input("Adivina un valor entre 1-20: ")
	intentos = intentos + 1
	try:
		respuesta = int(respuesta)
	except:
		print("Valor ingresado no valido")
		continue # interumpir la iteración actual y comenzar desde el while.
	
	if respuesta>=1 and respuesta<=20:
		if respuesta == numero:
			print("Has acertado al numero.","Sólo te llevo",intentos,"intentos")
			break # interrumpe/rompe el bucle
		elif respuesta>numero:
			print("\tIngresaste un número mayor!")
		else:
			print("\tIngresas un número menor!")
	else:
		print("Valor Ingresado no esta entre 1 y 20.")  
print("-"*25)
print("Fin del Juego")
print("-"*25)
