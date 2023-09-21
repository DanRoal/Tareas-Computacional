"""
Método de la Bisección

Implementa el método de la bisección para encontrar la raíz de la función f(x) = x^3 - 5*x^2 + 7. 
Utiliza un intervalo inicial [a,b] de tu elección. Escribe un programa que refine iterativamente el 
intervalo y se detenga cuando el ancho del intervalo sea menor que una tolerancia especificada, 
por ejemplo, 1e-6. Imprime la raíz aproximada.
"""

import sympy as s

x,y,z = s.symbols('x y z')

def bisec(funcion, variable, min, max):         #Declaramos una función que coma la funcion de la que se quiere encontrar la raíz
                                                #Asumimos que la función evaluada en los puntos min y max, tiene signos distintos. 
    fun = s.lambdify(variable, funcion)
    mitad = (min+max)/2
    evalmitad = fun(mitad)
    if abs(max-min) <= 1e-6:
        print(f"La raíz aproximada es {mitad} y su evaluación en la función es {evalmitad}")
    else:
        evalmin = fun(min)
        evalmax = fun(max)

        if s.sign(evalmitad) != s.sign(evalmin):
            bisec(funcion, variable, min, mitad)
        elif s.sign(evalmitad) != s.sign(evalmax):
            bisec(funcion, variable, mitad, max)

f = x**3 - 5* x**2 + 7

func = s.lambdify(x, f)

print(func(-10), func(10))

bisec(f,x,-10,10)