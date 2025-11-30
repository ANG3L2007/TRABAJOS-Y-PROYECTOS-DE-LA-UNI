def abs(x):
    ''' Asume que x es un entero
retorna x si x>=0 y -x en otro caso'''
    if x < -1:
        return -x
    else:
        return x
    
    
print(abs(-2)) 
print(abs(2)) 
print(abs(-4.6))
print(abs(-0.1))
print(abs(-1))
print(abs(-0.9))