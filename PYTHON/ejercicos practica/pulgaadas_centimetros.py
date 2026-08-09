unidades=input("digite la unidad a la que desea converitir \npulgadas :p\ncentimetro: c\n")
if unidades == "c":
    p=float(input("digite las unidades en centimetros: "))
    p=p/2.54
    print("las unidades en pulgadas son: ", p)
elif unidades == "p":
    c=float(input("digite las unidades en pulgadas: "))
    c=c*2.54
    print("las unidades en centimetros son : ",c)