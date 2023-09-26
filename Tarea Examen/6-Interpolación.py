"""
Interpolación.

Escribe un programa que realice interpolación lineal para encontrar el valor de una función
f(x) en un punto especificado x_0 utilizando 2 puntos de datos (x_1,y_1) y (x_2,y_2). Pide al
usuario que ingrese los puntos de datos y el x_0 objetivo. Calcula e imprime el valor interpolado.
"""
import sympy as s 

def interpol(punto1, punto2, objetivo):
    pendiente = (punto2[1] - punto1[1])/(punto2[0] - punto1[0])
    f = punto1[1] + pendiente * (x - punto1[0])
    funcion = s.lambdify(x, f)
    return funcion(objetivo)

punto1 = input('Introduzca los valores x_1 y y_1 separados por una coma').split(',')
punto2 = input('Introduzca los valores x_2 y y_2 separados por una coma').split(',')
