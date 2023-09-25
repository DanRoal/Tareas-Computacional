"""
Biblioteca de busqueda de raíces.

Crea una biblioteca o módulo en Python que incluya funciones para encontrar raíces utilizando
varios métodos (Bisección, Newton, secante, híbridos, etc.) La biblioteca debe permitir a los 
usuarios ingresar sus propias funciones, suposiciones iniciales y tolerencias. Proporciona una
documentación clara y ejemplos de como usar la biblioteca.
"""
import sympy as s

def bisec(funcion, variable, minimo, maximo):           #Declaramos una función que coma la funcion de la que se quiere encontrar la raíz
                                                        #Asumimos que la función evaluada en los puntos minimo y maximo, tiene signos distintos. 
    fun = s.lambdify(variable, funcion)
    mitad = (minimo+maximo)/2
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

def metNewton(funcion, derivada, variable, x_0, tolerancia):
    fun = s.lambdify(variable, funcion)
    dfun = s.lambdify(variable, derivada)

    step = fun(x_0)/dfun(x_0)
    if abs(step) <= tolerancia:
        return [x_0, fun(x_0)]
    else:
        return metNewton(funcion, derivada, variable, x_0-step, tolerancia)

def secanteMetho(funcion, variable, supin0,supin1, tolerancia):
    fun = s.lambdify(variable, funcion)

    step = fun(supin1) * (supin1 - supin0)/(fun(supin1) - fun(supin0))

    if abs(step) <= tolerancia:
        return [supin1, fun(supin1)]
    else:
        return secanteMetho(funcion, variable, supin0=supin1, supin1= supin1 - step, tolerancia= tolerancia)

    
def hibrido(func, variable, intervalo, toler):
    deriv = s.diff(func,variable)
    primeraprox= bisec(func, variable, intervalo[0],intervalo[1], toler)
    segundaprox = metNewton(func, deriv, variable, primeraprox[0], toler)
    return segundaprox
