""" Implemente la función palindrome() que recibe una cadena de caracteres (una frase) y
retorna True si la frase es palíndroma y False si no lo es. Una frase es palíndroma si se lee
igual hacia adelante o hacia atrás, sin tener en cuenta signos de puntuación y sin distinguir
mayúsculas de minúsculas. Se recomienda usar los métodos str.isalpha() y
str.lower()"""


def palindromo(frase):
    
    i=0
    resultado=""
    while i<len(frase):
        letra=frase[i]
        if letra.isalpha():
            resultado +=letra.lower()
        i += 1
    
    return resultado == resultado[::-1]

"""Anita lava la tina"""

frase=input("\ningrese una frase para determinar si es palindroma  ")
print(palindromo(frase))

