precio_horas = 7500
horas_trabajadas = int(input("ingrese la cantidad de horas que trabajo esta semana  "))
total = 0
if horas_trabajadas <=40:
    total = horas_trabajadas*precio_horas
    if total <= 250000:
        total = total - (total*0.10) 
    elif total > 250000:
        total = total - (total*0.20)
    print(total)
elif horas_trabajadas>40:
    total=(precio_horas*40)+((horas_trabajadas-40)*12000)
    if total <= 250000:
        total = total - (total*0.10) 
    elif total > 250000:
        total = total - (total*0.20)
    print(total)
print=(total)