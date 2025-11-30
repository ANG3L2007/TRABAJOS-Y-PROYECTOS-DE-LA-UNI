def tweetAlert(msg):
    al = 'fiebre'
    if al+'!!!' in msg:
        return 2
    elif al in msg:
        return 1
    else:
        return 0
    
    
i=3
cont=0
al="fiebre"
msg = ["hola",al,"!!!"]
while cont< len(msg):
    msg = "".join(msg[:i])
    print(tweetAlert(msg))
    msg = ["hola",al,"!!!"]
    cont+=1
    i -=1