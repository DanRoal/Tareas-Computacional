"""
Método de Newton

Implementa el método de newton para encontrar la raíz de la función f(x)=e^x - 5x. Comienza
con una suposición inicial x_0 de tu elección y utiliza la fórmula x_n+1 = x_n - f(x_n)/f'(x_n) 
Para refinar iterativamente la estimación. Detente cuando la diferencia absoluta entre estimaciones 
consecutivas sea menor que la tolerancia especificada, por ejemplo 1e-6. Imprime la raíz aproximada
"""

import sympy as s

def metNewton(funcion, derivada, variable, x_0, tolerancia):
    fun = s.lambdify(variable, funcion)
    dfun = s.lambdify(variable, derivada)

    step = fun(x_0)/dfun(x_0)
    if abs(step) <= tolerancia:
        return [x_0, fun(x_0)]
    else:
        return metNewton(funcion, derivada, variable, x_0-step, tolerancia)

x = s.symbols('x')          #Definimos las variables con las que vamos a trabajar

func = s.exp(x) - 5*x       #Declaramos la función a la cual le queremos aplicar el método

derivfunc = s.diff(func, x)

suposicionInicial = 1

tolera = 1e-6

raiz = metNewton(func, derivfunc, x, suposicionInicial, tolera)

print(f"La raíz aproximada es {raiz[0]}, y su evaluación en la función es {raiz[1]}")