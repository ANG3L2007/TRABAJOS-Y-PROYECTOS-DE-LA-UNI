def tweetAlert(msg):
    al = 'fiebre'
    if al+'!!!' in msg:
        return 2
    elif al in msg:
        return 1
    else:
        return 0
    
al = "fiebre !!!"
msg = [ al, "!!!", 44 ]
i = 0
print(tweetAlert(msg))
# while i>len(msg):
#     print(tweetAlert(msg))
#     i += 1