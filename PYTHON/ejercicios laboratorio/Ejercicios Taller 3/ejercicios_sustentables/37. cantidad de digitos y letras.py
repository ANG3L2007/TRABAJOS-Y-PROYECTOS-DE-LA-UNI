cadena=input("ingrese digitos y letras para determianr cuantas hay en su mensaje:\n")
cont=0
digitos=0
letras=0
while cont<len(cadena):
    i=cadena[cont]
    if i.isdigit():
        digitos=digitos+1
    elif i.isalpha():
        letras=letras+1
    cont=cont+1
print("\nla cantidad de digitos es: ",digitos)
print("la cantidad de letras es: ", letras, )