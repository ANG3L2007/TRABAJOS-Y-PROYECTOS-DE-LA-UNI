num = int(input("ingrese el numero al que desea sacarle el factorial: \n"))
fact = 1
while num != 0:
    fact = fact * num
    num -=1
print(f"el valor del factorial es: {fact}")