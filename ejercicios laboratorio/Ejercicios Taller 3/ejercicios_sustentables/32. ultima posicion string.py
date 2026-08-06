string=input("digite un texto: ")
word=input("digite la letra que desea buscar el texto: ")
cont=0
w=-1
while cont< len(string):
    i=string[cont]
    if word==i:
        w=cont
    cont=cont+1

if w!=-1:
    print("la posicion de el caracter es: ",w)
elif w==-1:
    print("el caracter ingresado no pertenece a la palabra ingresada.")