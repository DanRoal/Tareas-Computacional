"""
Método de la Secante.

Implementa el método de la secante para encontrar la raíz de la función f(x)=x^2 - 4
Elige dos suposiciones iniciales x_0 y x_1 y utiliza la fórmula x_n+1 = x_n f(x_n)(x_n - x_n-1)/(f(x_n) - f(x_n-1))
para refinar iterativamente la estimación. Detente cuando la diferencia absoluta entre estimaciones
consecutivas sea menor que la tolerancioa especificada, por ejemplo, 1e-6. Imprime la 
raíz aproximada.
"""