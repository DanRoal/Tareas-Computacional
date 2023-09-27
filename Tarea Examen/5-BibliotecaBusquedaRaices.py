"""
Biblioteca de busqueda de raíces.

Crea una biblioteca o módulo en Python que incluya funciones para encontrar raíces utilizando
varios métodos (Bisección, Newton, secante, híbridos, etc.) La biblioteca debe permitir a los 
usuarios ingresar sus propias funciones, suposiciones iniciales y tolerencias. Proporciona una
documentación clara y ejemplos de como usar la biblioteca.
"""
import sympy as s

def bisec(funcion, variable, minimo, maximo, tolerancia=1e-6):           #Declaramos una función que coma la funcion de la que se quiere encontrar la raíz
                                                        #Asumimos que la función evaluada en los puntos minimo y maximo, tiene signos distintos. 
    fun = s.lambdify(variable, funcion)
    mitad = (minimo+maximo)/2
    evalmitad = fun(mitad)
    if abs(maximo-minimo) <= tolerancia:
        return [mitad, evalmitad]
    else:
        evalmin = fun(minimo)
        evalmax = fun(maximo)

        if s.sign(evalmitad) != s.sign(evalmin):
            return bisec(funcion, variable, minimo, mitad)
        elif s.sign(evalmitad) != s.sign(evalmax):
            return bisec(funcion, variable, mitad, maximo)

def metNewton(funcion, derivada, variable, x_0, tolerancia=1e-6):
    fun = s.lambdify(variable, funcion)
    dfun = s.lambdify(variable, derivada)

    step = fun(x_0)/dfun(x_0)
    if abs(step) <= tolerancia:
        return [x_0, fun(x_0)]
    else:
        return metNewton(funcion, derivada, variable, x_0-step, tolerancia)

def secanteMetho(funcion, variable, supin0,supin1, tolerancia=1e-6):
    fun = s.lambdify(variable, funcion)

    step = fun(supin1) * (supin1 - supin0)/(fun(supin1) - fun(supin0))

    if abs(step) <= tolerancia:
        return [supin1, fun(supin1)]
    else:
        return secanteMetho(funcion, variable, supin0=supin1, supin1= supin1 - step, tolerancia= tolerancia)

    
def hibrido(func, variable, intervalo, toler=1e-6):
    deriv = s.diff(func,variable)
    primeraprox= bisec(func, variable, intervalo[0],intervalo[1], toler)
    segundaprox = metNewton(func, deriv, variable, primeraprox[0], toler)
    return segundaprox

if __name__ == '__main__':
    ########## Ejemplos de uso ##############
    # Definimos las variables con las que vamos a trabajar
    x, y, z = s.symbols('x y z') 

    ########### Bisección ####################
    f = x**3 - 5* x**2 + 7          # Definimos la función que vamoa a trabajar

    func1 = s.lambdify(x, f)
    
    resultado = bisec(f,x,-10,10)
    print(f"La raíz aproximada es {resultado[0]} y su evaluación en la función es {resultado[1]}")

    ###########################################

    ########### Newton ########################

    func2 = s.exp(y) - 5*y       #Declaramos la función a la cual le queremos aplicar el método

    derivfunc = s.diff(func2, y)    #Usamos la librería sympy para derivar nuestra función

    suposicionInicial = 1

    tolera = 1e-6

    raiz = metNewton(func2, derivfunc, y, suposicionInicial, tolera)

    print(f"La raíz aproximada es {raiz[0]}, y su evaluación en la función es {raiz[1]}")
    ###########################################