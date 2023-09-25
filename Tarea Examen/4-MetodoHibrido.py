"""
Método Hibrido.

Escribe un programa que combine el método de la bisección y el método de Newton para encontrar
la raíz de la función f(x)=x^3 -6x^2 +11x - 6. Comienza con un intervalo [a,b] y utiliza la
bisección hasta que el ancho del intervalo sea menor que un umbral determinado, luego cambia
al método de Newton. Detente cuando la diferencia absoluta entre las estimaciones consecutivas
sea menor que 1e-6. Imprime la raíz aproximada.
"""

import sympy as s

def bisec(funcion, variable, min, max, tol):        #Declaramos una función que coma la funcion de la que se quiere encontrar la raíz
                                                    #Asumimos que la función evaluada en los puntos min y max, tiene signos distintos. 
    fun = s.lambdify(variable, funcion)
    mitad = (min+max)/2
    evalmitad = fun(mitad)
    if abs(max-min) <= tol:
        return [mitad, evalmitad]
    else:
        evalmin = fun(min)
        evalmax = fun(max)

        if s.sign(evalmitad) != s.sign(evalmin):
            return bisec(funcion, variable, min, mitad, tol)
        elif s.sign(evalmitad) != s.sign(evalmax):
            return bisec(funcion, variable, mitad, max, tol)
        
def metNewton(funcion, derivada, variable, x_0, tolerancia):
    fun = s.lambdify(variable, funcion)
    dfun = s.lambdify(variable, derivada)

    step = fun(x_0)/dfun(x_0)
    if abs(step) <= tolerancia:
        return [x_0, fun(x_0)]
    else:
        return metNewton(funcion, derivada, variable, x_0-step, tolerancia)
    
def hibrido(func, variable, intervalo, toler):
    deriv = s.diff(func,variable)
    primeraprox= bisec(func, variable, intervalo[0],intervalo[1], toler)
    segundaprox = metNewton(func, deriv, variable, primeraprox[0], toler)
    return segundaprox

x = s.symbols('x')
interval = [1.5, 2.5]
raiz = hibrido(x**3 -6*x**2 +11*x - 6, x, interval, 1e-6)

print(f"Una raíz aproximada de la funcion es {raiz[0]}, y su evaluación es {raiz[1]}")

