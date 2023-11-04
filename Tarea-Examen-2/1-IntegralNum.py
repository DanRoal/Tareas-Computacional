"""
Calcule la integral usando algún método de integración numérica de su preferencia

int[-inf, inf] e^(-x^2) dx
"""

import numpy as np
import sympy as sp
import time

# Dado que estamos tratando con una función par, podemos calcular la integral en el 
# intervalo [0, inf] y multiplicar el resultado por 2

#Dado que numericamente no podemos calcular hasta infinito, calcularemos la integral
# en el intervalo [0, 1000] y multiplicaremos el resultado por 2

# Definimos la función a integrar
x = sp.Symbol('x')

def f(x):
    return sp.exp(-x**2)

# Definimos un cambio de variable que hará que la integral converja más rápido
def P(x):
    return x**3 *(6*x**2 - 15*x + 10)

# Definimos la derivada de P(x)
def delta_P(x):
    return 30*(x-1)**2 * x**2

N=4000
h = 1/N

lista_P = [P(i/N) for i in range(N)]
list_delP = [delta_P(i/N) for i in range(N)]

# Calculamos la integral
def integral(f, estiramiento):
    """
    función que toma una función f y un estiramiento y calcula la integral
    en el intervalo [0, estiramiento] de f(x) usando el método de rectángulos
    usando la parametrización P(x) la cual va de [0,1]
    """
    inte = sum([f(lista_P[i] * estiramiento) * list_delP[i]  for i in range(N)]) * h * estiramiento
    return inte

# Calculamos la integral
tic = time.time()
inte = integral(f, 10)
toc = time.time()

print("La integral de la función f(x) = e^(-x^2) en el intervalo [-10, 10] es: ", inte*2)
print("El valor exacto de la integral es: ", np.sqrt(np.pi))
print("El error absoluto es: ", abs(inte*2 - np.sqrt(np.pi)))
print("El tiempo de ejecución fue: ", toc-tic, " segundos")
