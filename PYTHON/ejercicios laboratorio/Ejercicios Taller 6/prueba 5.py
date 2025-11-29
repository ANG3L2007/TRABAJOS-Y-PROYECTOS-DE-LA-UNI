
def sqrtb(x, epsilon):
    low = 0.0
    high = max(1.0, x)
    ans = (high + low)/2.0
    while abs(ans**2 - x) >= epsilon:
        if ans**2 < x:
            low = ans
        else:
            high = ans
            ans = (high + low)/2.0
    return ans

print(sqrtb(2,2)) #test 1 (black-box)
print(sqrtb(0.5,90)) #test 2 (black-box)
print(sqrtb(-6,4)) #test 3 (black-box)

