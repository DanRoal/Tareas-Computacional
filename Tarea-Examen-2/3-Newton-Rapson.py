"""
Usar el método de Newton Rapson para aproximar el valor de pi/2
(hint: define una función cuya raíz sepas que es pi/2 y dale un valor
cercano a pi/2 para que empiece a aproximar como pi/2)
Imprime en pantalla las aproximaciones que va haciendo el método
"""
import numpy as np
import sympy as np
import math

#Definimos la función que tiene raíz en pi/2
def f(x):
    return math.cos(x)

#Definimos la derivada de la función
def df(x):
    return -math.sin(x)

#Definimos la función que calcula la raíz de la función f
def newton_raphson(x, tol=1e-10, max_iter=100):
    for i in range(max_iter):
        dx = -f(x)/df(x)
        x = x + dx
        if abs(dx) < tol:
            print(f"La raíz es {x} con una tolerancia de {tol} y en la iteración {i}")
            return x
        print(f"La aproximación en la iteración {i} es {x}")

#Definimos el valor inicial y llamamos a la función
x0 = 1

aproximación = newton_raphson(x0)
print(f"El valor exacto de pi/2 es {math.pi/2}")