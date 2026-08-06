notas_estudiante ={"nombre":"notas"
    
}
while True:
    opcion = input("que opcion desea elegir \nAgregar alumno \nVer Notas \nSalir \n\n\n\n")
    if opcion == "agregar alumno" :
        Alumno = input("Ingrese el nombre del alumno:\n")
        Notas = input("Ingrese la nota del alumno:\n")
        notas_estudiante[Alumno] = Notas
    elif opcion == "ver notas":
        print(notas_estudiante)
    elif opcion == "salir":
        break
    else:
        print("opcion invalida, intentelo denuevo")