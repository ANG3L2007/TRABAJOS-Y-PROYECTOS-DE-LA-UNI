while True:
    try:
        num = float(input("ingrese un numero "))
        den =float(input("ingrese un denominador "))
        
        
        try:
            div = num/den
            print(div)
        except ZeroDivisionError:
            print("no se pude dividir por 0, intentelo denuevo")
    except ValueError:
        print("esta ingresando un caracter no valido ")
    else:
        print("ingreso de datos adecuado sin division entre 0 ")
    finally:
        print("esto siempre se ejecuta, independiente de todo")