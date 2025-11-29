estudiantes = {"yulieth":4.7,
                "andrea": 4.2,
                "ramon": 5.0}

while True:
    comando=input("\ndigite los comandos agregar, mostrar, eliminar o salir para interactuar con el programa de notas:\n")
    
    if comando == "agregar":
        
        estudiante=input("ingrese el nombre del estudiante que desea agregar: ")
        notas=float(input("ingrese la nota que desea asignar al estudiante: "))
        estudiantes[estudiante]=notas
        print("el estudiante fue agregado con exito")
        
        
    if comando == "mostrar":
        for estudiante, notas in estudiantes.items():
            print(estudiante,notas)
            
            
    if comando == "eliminar":
        estudiante=input("a que estudiante desea eliminar? ")
        if estudiante in estudiantes:
            del estudiantes[estudiante]
            print("eliminando estudiante...")
    
    
    if comando == "salir":
        print("saliendo...")
        break
