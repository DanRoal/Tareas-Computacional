"""
Calcule la derivada por enfrente, derivada por detrás y
método de la secante para la función f(x) = sin(x)/(x**2),
publique sus resultados en forma de una tabla
"""

import numpy as np
import sympy as sp
import time

# Definimos la función a derivar
x = sp.Symbol('x')

def f(x):
    return sp.sin(x)/(x**2)

# Definimos la derivada de f(x)
def delta_f(x):
    return (2*x*sp.cos(x) - 2*sp.sin(x))/(x**3)

# Definimos la derivada por enfrente
def der_enfrente(x0,h,f=f):
    return (f(x0+h)-f(x0))/h

# Definimos la derivada por detrás
def der_detras(x0,h,f=f):
    return (f(x0)-f(x0-h))/h


# Definimos la derivada por la secante
def secante(x0:float,x1:float,h:float,f,n=100):
#Realizamos el ciclo for del método de la secante    
    for i in range(n):
        x2=x1-f(x1)*(x1-x0)/(f(x1)-f(x0))
#Inluimos la condición de que si el valor absoluto de x2 evaluado en la funcion es mayor que el error hacemos x0=x2   
        if np.abs(f(x2)) < h:
            
            return x2
        x1,x0=x2,x1

# Definimos el intervalo de evaluación
a = 0.1
b = 2*np.pi

# Definimos el tamaño del paso
h = 0.1

# Definimos el número de puntos
n = int((b-a)/h)

# Definimos el arreglo de puntos
x = np.linspace(a,b,n)

# Definimos el arreglo de valores
d_enfrente = np.zeros(n)
d_detras = np.zeros(n)
d_secante = np.zeros(n)
d_analitica = np.zeros(n)

# Hacemos una tabla de resultados
print("{:<10} {:<20} {:<20} {:<20} {:<20}".format('x', 'Derivada Enfrente', 'Derivada Detrás', 'Derivada Secante', 'Derivada Analítica'))

for i in range(n-1):
    d_enfrente[i] = der_enfrente(x[i],h)
    d_detras[i] = der_detras(x[i],h)
    d_secante[i] = secante(x[i],x[i+1],1e-6,f,100)
    d_analitica[i] = delta_f(x[i])
    print("{:<10.2f} {:<20.6f} {:<20.6f} {:<20.6f} {:<20.6f}".format(x[i], d_enfrente[i], d_detras[i], d_secante[i], d_analitica[i]))
