"""
Usa la integración de Montecarlo para estimar el valor de Pi. Genera puntos aleatorios 
en un cuadradoX:[0,1] Y:[0,1], y determina cuántos caen dentro del círculo inscrito de 
radio 1. La relación de puntos dentro del círculo con respecto al cuadrado 
se relaciona con Pi/4
"""
import time
import numpy as np

N = 10000000

x_aleatorias = np.random.uniform(0,1,N)
y_aleatorias = np.random.uniform(0,1,N)

def f(x):
    return np.sqrt(1-x**2)
tic = time.time()
hits = [y_aleatorias[i] for i in range(len(y_aleatorias)) if (y_aleatorias[i]<= f(x_aleatorias[i])) ]
toc = time.time()
print(f"Pi es {(len(hits)/N)*4} y nos tardamos {toc-tic}segundos en calcularlo")
