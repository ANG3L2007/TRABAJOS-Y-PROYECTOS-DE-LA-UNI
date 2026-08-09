"""6. En el código mostrado, qué efectos tiene sobre el valor final de guesses:
a. Duplicar el valor de step
b. Duplicar el valor de epsilon"""

x = 25
epsilon = 0.01
step = 0.0001
guesses = 0
ans = 0.0


while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += step
    guesses += 1
if abs(ans**2 - x) >= epsilon:
    print('Couldn\'t find the square root of', x)
else:
    print(ans, 'is approximately thesquare root of', x)
print('There were', guesses, 'guesses')


x = 25
epsilon = 0.01
step = 0.0002
guesses = 0
ans = 0.0

while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += step
    guesses += 1
if abs(ans**2 - x) >= epsilon:
    print('Couldn\'t find the square root of', x)
else:
    print(ans, 'is approximately thesquare root of', x)
print('There were', guesses, 'guesses')

x = 25
epsilon = 0.02
step = 0.0001
guesses = 0
ans = 0.0

while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += step
    guesses += 1
if abs(ans**2 - x) >= epsilon:
    print('Couldn\'t find the square root of', x)
else:
    print(ans, 'is approximately thesquare root of', x)
print('There were', guesses, 'guesses')

