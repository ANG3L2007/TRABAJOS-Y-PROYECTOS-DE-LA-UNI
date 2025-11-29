# nombres=["juan","camilo","mauricio","andres"]
# años=[23,25,32,28]
# carrera=["telecomunicaciones","aviacion","sistemas","matematicas"]
# promedio=[4.7,3.9,5.0,2.1]

# estudiantes={ "juan": (23, "telecomunicaciones", 4.7),
#             "camilo": (25, "aviacion", 3.9),
#             "mauricio": (32,"sistemas", 5.0),
#             "andres": (28, "matematicas", 2.1)}

# estudiante={"nombre":"camilo",
#             "años":22,
#             "carrera":"telecomunicaciones",
#             "promedio":4.4}
# print(estudiante["promedio"])

# frase=input("ingrese una frase ")


# frase=frase.split()
# cont={}

# for a in frase:
#     if a in cont.keys():
#         cont[a]+=1
#     else:
#         cont[a] = 1
        
# print(cont)


contactos={"santiago":322000355,
            "omar":344204592,
            "alfonso":32004032}
while True:
    opcion=input("digite agregar, buscar o eliminar. para un contacto \nsalir para cerrar el programa \n")
    print(opcion)
    if opcion == "agregar":
        nombre=input("digite el nombre ")
        numero=int(input("digite un numero "))
        contactos[nombre]=numero
        
    elif opcion == "buscar":
        nombre=input("que usuario desea buscar?  ")
        if nombre in contactos:
            print("el nombre de ", nombre,"es ", contactos[nombre])
        else:
            print("este nombre no existe en la libreta ")
            
    elif opcion == "eliminar":
        nombre=input("que contacto desea eliminar? ")
        if nombre in contactos:
            del contactos[nombre]
        print("el contacto fue eliminado ")
        
    elif opcion == "salir":
        break