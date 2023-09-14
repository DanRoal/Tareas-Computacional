"""
Escribir unn programa en el que se pregunte al usuario por una frase
y una letra y muetre por pantalla el numero de veces que aparece la letra en la fras
"""

frase = input("Por favor introduza una frase:\n")
letra = input("Introduzca la letra o simbolo que desee contar:\n")

print(f"La letra {letra} aparece {frase.count(letra)} veces")

