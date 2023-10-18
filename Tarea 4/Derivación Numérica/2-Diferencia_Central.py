'''
Calcula la derivada de numérica de f(x)=sin(x) en x=\pi/4
utilizando el método de diferencia central con h=0.01
'''
import numpy as np
import matplotlib.pyplot as mpl

h = 0.01

x = np.linspace(-2*np.pi,2*np.pi,200)
y = np.sin(x)

espacioprimo = []
for i in x:
    espacioprimo.append((np.sin(i+h)-np.sin(i-h))/(2*h))

fig, ax = mpl.subplots()
fig, ax2 = mpl.subplots()

ax.plot(x,y)
ax2.plot(x, espacioprimo)

mpl.show()