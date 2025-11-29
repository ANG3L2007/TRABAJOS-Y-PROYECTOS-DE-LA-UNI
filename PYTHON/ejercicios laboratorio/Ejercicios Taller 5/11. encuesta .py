colores={}

while True:
    print("Menu Principal\n1.Agregar Encuesta\n2.Ver Encuestras\n3.Salir")
    opcion = input("digite la opcion que desea usar ")
    
    if opcion == "1":
        
        sexo = input("ingrese el genero (H/M)" ).upper()
        color = input("ingrese el color ").lower()
        
        if color not in colores:
            colores[color]={"H":0,"M":0}
            
        if sexo == "M":
            colores[color]["M"] = colores[color]["M"]+1
            
        elif sexo == "H":
            colores[color]["H"] = colores[color]["H"]+1
            
        else:
            print("sexo invalido, porfavor ingreselo nuevamente ")
        
    elif opcion == "2":
        print("\nresultados!!!")
        total_encuestas=0
        
        for color in colores:
            total_encuestas+=colores[color]["H"]+colores[color]["M"]
        
        if total_encuestas == 0:
            print("no hay encuestas registradas \n")
        
        else:
            for color in colores:
            
                total_color=colores[color]["M"]+colores[color]["H"]
                H=float(colores[color]["H"])
                M=float(colores[color]["M"])
                por_H=(H/total_color)*100
                por_M=(M/total_color)*100
                por_colares=(total_color/total_encuestas)*100
                print(f"{color}: {por_colares:.1f}% (H:  {por_H:.1f}% M:  {por_M:.1f}%)")
        

            
            
    elif opcion == "3":
        print("saliendo...")
        break