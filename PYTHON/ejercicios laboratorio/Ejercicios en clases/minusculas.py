def cMayus(mensaje):
    
    m=""
    cont=0

    while cont<len(mensaje):
        posAscci=ord(mensaje[cont])
        mayus=chr(posAscci-32)
        m=m+mayus
        
        cont=cont+1
    return m
mensaje=("programar")
print(cMayus(mensaje))



def cMINUS(mensaje):
    
    m=""
    cont=0

    while cont<len(mensaje):
        posAscci=ord(mensaje[cont])
        mayus=chr(posAscci+32)
        m=m+mayus
        
        cont=cont+1
    return m
mensaje=("PROGRAMAR")
print(cMINUS(mensaje))
