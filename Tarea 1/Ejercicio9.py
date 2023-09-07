"""
Un programa que pide al usuario un número positivo y muestre en pantalla
el factorial de ese número
"""

factorial = int(input('introduzca un numero para sacarle el factorial:'))

def facto(variable):
    if variable==1: return 1
    multiplicacion = variable*facto(variable-1)
    return multiplicacion

print(facto(factorial))