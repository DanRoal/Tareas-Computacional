"""
Escribir un programa que pida al usuario una frase u oración,
y muestre por pantalla el número de veces que contiene cada vocal
"""

frase = list(input("Por favor introduca una frase para contar las vocales:\n"))

dicc ={
    'a': frase.count("a") + frase.count("A"),
    'e': frase.count("e") + frase.count("E"),
    'i': frase.count("i") + frase.count("I"),
    'o': frase.count("o") + frase.count("O"),
    'u': frase.count("u") + frase.count("U")
}

print(dicc)