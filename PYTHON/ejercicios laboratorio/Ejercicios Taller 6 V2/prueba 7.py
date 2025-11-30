def updSensor(mment, hist, prev):
    if mment in hist:
        return 0
    elif mment > prev:
        return 1
    else:
        return -1

mment = 1
hist = [1,3,"ang",mment]
prev = 2

print (updSensor(mment,hist,prev))

mment = 5

prev = 4

print (updSensor(mment,hist,prev))



hist = [2,"h"]
mment = 1
prev = 5

print (updSensor(mment,hist,prev))