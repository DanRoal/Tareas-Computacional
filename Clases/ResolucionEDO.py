"""
Ecuacion del amor (Romeo y Julieta)

dy/dt = -ay + bx
dx/dt = cx + dy

En este caso para simplificar, b = c = 0 y a = d = 1

Se utilizará el método de Runge-Kutta de orden 4
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x, y, t):
    return [-y,x]

def runge_kutta_4(x0, y0, h, n):
    """
    x0: Valor inicial de x
    y0: Valor inicial de y
    h: Tamaño del paso
    n: Número de puntos
    """
    # Definimos los arreglos de puntos
    x = np.zeros(n)
    y = np.zeros(n)
    t = np.zeros(n)
    
    # Definimos los valores iniciales
    x[0] = x0
    y[0] = y0
    t[0] = 0
    
    # Definimos el método de Runge-Kutta de orden 4
    for i in range(n-1):
        k1 = f(x[i], y[i], t[i])
        k2 = f(x[i] + 0.5*k1[0], y[i] + 0.5*k1[1], t[i] + 0.5*h)
        k3 = f(x[i] + 0.5*k2[0], y[i] + 0.5*k2[1], t[i] + 0.5*h)
        k4 = f(x[i] + k3[0], y[i] + k3[1], t[i] + h)
        
        x[i+1] = x[i] + (k1[0] + 2*k2[0] + 2*k3[0] + k4[0])/6
        y[i+1] = y[i] + (k1[1] + 2*k2[1] + 2*k3[1] + k4[1])/6
        t[i+1] = t[i] + h
    
    return [t,x,y]

x0 = 1
y0 = 1
h = 0.1
n = 100

aproximación = runge_kutta_4(x0, y0, h, n)

# Graficamos
plt.plot(aproximación[1], aproximación[2])
plt.show()
