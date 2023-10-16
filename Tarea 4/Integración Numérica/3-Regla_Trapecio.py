"""
Estima la integral de f(x) = sin(x) en el intervalo [0, π/2] utilizando la regla
del trapecio con n = 6 subintervalos.
"""
import numpy as np
#Primero definimos la función que queremos integrar
def f(x):
    return np.sin(x)

#Calculamos el ancho de cada subintervalo
n = 6
h = (np.pi/2-0)/n

#obtenemos los límites de cada subintervalo
lista_x = [i*h for i in range(n+1)]

#hacemos una lista con los valores de la función en los límites de cada subintervalo
lista_y = [f(i) for i in lista_x]

#calculamos la suma de los valores de la función en los límites de cada subintervalo
integral = (lista_y[0]+lista_y[-1])/2 + sum(lista_y[1:-1])

#multiplicamos la suma por el ancho de cada subintervalo
integral = integral * h

print(f"La integral aproximada de f(x) = sin(x) en el intervalo [0, π/2] es {integral} y el valor exacto es 1")