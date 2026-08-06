def num_malvado(N):
    original=N
    residuo_acum=""
    while N!=0:
        residuo=str(N%2)
        residuo_acum=residuo_acum+residuo
        N=N//2
    residuo_acum=(residuo_acum[::-1])
    
    i=0
    C=0
    while i<len(residuo_acum):
        B=residuo_acum[i]
        if B == "1":
            C += 1
        i += 1
        
    if C%2==0:
        print(original,"/",residuo_acum," Es malvado")
    else:
        print(original,"/",residuo_acum, " No es malvado")

N=int(input("ingrese un numero "))

m=num_malvado(N)

# def num_poderoso(N):



