mensaje=input("ingrese una lista de productos separadas por coma `,`   \n")
lista=mensaje.split(",")
i=len(lista)
cont=0
while i>cont:
    print(lista[cont])
    cont=cont+1
