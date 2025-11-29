agenda_electronica={"lunes":{},
                    "martes":{},
                    "miercoles":{},
                    "jueves":{},
                    "viernes":{},
                    "sabado":{},
                    "domingo":{}}

print("\ncomandos para la agenda electronica\nsi desea agregar un dia debe seguir el siguiente ejemplo:\nnew Martes 14 Examen Informática\nY para ver los dias agendados debe ingresar:\nview Viernes\n")

while True:

    comando = input("ingrese el comando  ")
    partes = comando.split()
    
    if partes[0] == "new" and  len(partes)>=4: #creacion de nueva cita
        dias = partes[1].lower()
        hora = partes[2]
        cita = " ".join(partes[3:])
        
        if dias not in agenda_electronica:
            print("dia invalido, intente nuevamente ")
        elif dias in agenda_electronica:
            
            agenda_electronica[dias][hora]=cita
            
            if agenda_electronica[dias][hora] in agenda_electronica:
                opcion = input("hora ocupada, desea agregarlo de todas formas? (si/no)").lower
                
                if opcion == "si":
                    agenda_electronica[dias][hora]={cita}
                else:
                    continue
    
    if partes[0] == "view" and len(partes) == 2: #visualizacion de la agenda
        dias = partes[1]
        if dias in agenda_electronica:
            agenda_electronica[dias][hora]
            print
        
    if partes[0] == "salir":
            print("saliendo...")
            break
        
        

                    
                
                
                