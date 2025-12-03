def bin2dec(binum):
    dec = 0
    size = len(binum)
    for i in range(size-1):
        dec += int(binum[size-i-1]) * 2**i
    return dec

def str2dec(decstr):
    dec = 0
    size = len(decstr)
    for i in range(size):
        dec += int(decstr[size-i-1]) * 10**i
    return dec
def sr(x):
    low = 0.0
    high = x
    ans = (high + low)/2.0
    while abs(ans**2 - x) >= 0.001:
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    return ans


def f(nums):
# nums es una lista de números binarios
# o decimales almacenados en strings
    roots = []
    for i in range(len(nums)):
        if nums[i][0]=='b':
            nums[i] = bin2dec(nums[i])
        else:
            nums[i] = str2dec(nums[i])
    sroot = sr(nums[i])
    if sroot not in roots:
        roots.append(sroot)
            
nums = [111,11110,0,10,100,11,1]

print(f(nums))

