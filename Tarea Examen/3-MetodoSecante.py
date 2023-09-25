"""
Método de la Secante.

Implementa el método de la secante para encontrar la raíz de la función f(x)=x^2 - 4
Elige dos suposiciones iniciales x_0 y x_1 y utiliza la fórmula x_n+1 = x_n - f(x_n)(x_n - x_n-1)/(f(x_n) - f(x_n-1))
para refinar iterativamente la estimación. Detente cuando la diferencia absoluta entre estimaciones
consecutivas sea menor que la tolerancioa especificada, por ejemplo, 1e-6. Imprime la raíz aproximada.
"""

import sympy as s

def secanteMetho(funcion, variable, supin0,supin1, tolerancia):
    fun = s.lambdify(variable, funcion)

    step = fun(supin1) * (supin1 - supin0)/(fun(supin1) - fun(supin0))

    if abs(step) <= tolerancia:
        return [supin1, fun(supin1)]
    else:
        return secanteMetho(funcion, variable, supin0=supin1, supin1= supin1 - step, tolerancia= tolerancia)
    
x = s.symbols('x')

func = x**2 - 4

x_0 = 0
x_1 = 1

toleramos = 1e-6

aproximacion = secanteMetho(func, x, x_0,x_1,toleramos)

print(f"La raíz aproximada de la función es {aproximacion[0]}, y su evaluación en la función es {aproximacion[1]}")