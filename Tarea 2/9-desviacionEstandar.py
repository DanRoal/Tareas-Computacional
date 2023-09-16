"""
Escribir un programa que pregunte por una muestra de números
separados por comas, los guarde en una lista y muestre por pantalla
su media y desviación estandar
"""
from math import *
def promedio(numeros):
    return sum(numeros)/len(numeros)

def desvEstan(muestra):
    sumas = [(x-promedio(muestra))**2 for x in muestra]
    return sqrt(sum(sumas)/(len(muestra)))


mues = list(map(float, input("Introduzca una secuencia de números separados por comas para obtener su desviación estandar y su media:\n").split(",")))

print(promedio(mues))
print(f"El promedio de la muestra es {promedio(mues)} y la desviación estandar es {desvEstan(mues)}")