horas_trabajadas=float(input("digite cuantas horas trabajo esta semana:  "))


if horas_trabajadas <= 40:
    pago=horas_trabajadas*7500
elif horas_trabajadas:
    pago=horas_trabajadas*7500+(horas_trabajadas-40)*12000

if pago <= 250000 :
    pago=pago-pago*0.10
    print(pago)
elif pago:
    pago=pago-pago*0.20
    print(pago)