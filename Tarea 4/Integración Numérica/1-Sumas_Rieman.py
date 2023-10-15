"""
Estima la integral de f(x) = 2 x^2 desde x = 0 hasta x = 2 utilizando la regla
del rectángulo con n = 4 subintervalos.
"""

#Primero definimos la función que queremos integrar
def f(x):
    return 2*x**2

#Calculamos el ancho de cada subintervalo
h = (2-0)/4

#obtenemos los límites de cada subintervalo
lista_x = [i*h for i in range(5)]

#hacemos una lista con los valores medios de cada subintervalo
lista_x_medios = [(lista_x[i]+lista_x[i+1])/2 for i in range(4)]

#hacemos una lista con los valores de la función en los puntos medios
lista_y_medios = [f(i) for i in lista_x_medios]

#calculamos la suma de los valores de la función en los puntos medios
integral = sum(lista_y_medios) * h

print(f"La integral aproximada de f(x) = 2 x^2 desde x = 0 hasta x = 2 es {integral} y el valor exacto es 5.333333333333333")