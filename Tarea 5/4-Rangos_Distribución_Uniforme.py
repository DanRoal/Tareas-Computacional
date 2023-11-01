"""
Genera 50 números aleatorios a partir de una distribución uniforme entre -5 y 5.
Calcula el porcentaje de números que caen dentro de los intervalos [-1,1],[1,3],
y [3,5]
"""

import numpy as np

numeros = np.random.uniform(-5,5,50)

rango1 = [i for i in numeros if (i>-1) and (i<1)]
rango2 = [i for i in numeros if (i>1) and (i<3)]
rango3 = [i for i in numeros if (i>3) and (i<5)]

print(f"El porcentaje de números que están en el rango 1 es {(len(rango1)/len(numeros))*100}%")
print(f"El porcentaje de números que están en el rango 2 es {(len(rango2)/len(numeros))*100}%")
print(f"El porcentaje de números que están en el rango 3 es {(len(rango3)/len(numeros))*100}%")
