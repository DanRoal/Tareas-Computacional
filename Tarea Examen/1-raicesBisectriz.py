"""
Método de la Bisección

Implementa el método de la bisección para encontrar la raíz de la función f(x) = x^3 - 5*x^2 + 7. 
Utiliza un intervalo inicial [a,b] de tu elección. Escribe un programa que refine iterativamente el 
intervalo y se detenga cuando el ancho del intervalo sea menor que una tolerancia especificada, 
por ejemplo, 1e-6. Imprime la raíz aproximada.
"""

import sympy as s

x,y,z = s.symbols('x y z')

def bisec(funcion, variable, minimo, maximo):         #Declaramos una función que coma la funcion de la que se quiere encontrar la raíz
                                                #Asumimos que la función evaluada en los puntos minimo y maximo, tiene signos distintos. 
    fun = s.lambdify(variable, funcion)
    mitad = (minimo + maximo)/2
    evalmitad = fun(mitad)
    if abs(maximo-minimo) <= 1e-6:
        return [mitad, evalmitad]
    else:
        evalmin = fun(minimo)
        evalmax = fun(maximo)

        if s.sign(evalmitad) != s.sign(evalmin):
            return bisec(funcion, variable, minimo, mitad)
        elif s.sign(evalmitad) != s.sign(evalmax):
            return bisec(funcion, variable, mitad, maximo)

f = x**3 - 5* x**2 + 7

func = s.lambdify(x, f)

print(func(-10), func(10))

resultado = bisec(f,x,-10,10)
print(f"La raíz aproximada es {resultado[0]} y su evaluación en la función es {resultado[1]}")