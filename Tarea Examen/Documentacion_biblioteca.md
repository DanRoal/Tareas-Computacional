# Biblioteca de aproximación de raíces

A continuación te mostraré como usar la biblioteca BibBusquedaRaices, la cual podrás encontrar como ejercició 5 de la carpeta "Tarea Examen"
En esta biblioteca tenemos varias funciones útiles a la hora de aproximar raíces, sin embargo hay que saber utilizarlas adecuadamente.

Para cada una de las funciones disponibles te daré una breve descripción y mencionaré los parámetros a insertar. Los ejemplos correspondientes se encontrarán en la parte de abajo del documeto.

## Funciones

| Función       | Argumentos   |
|--------       |---------     |
| `bisec()`     |funcion, variable, minimo, maximo, tolerancia  |
|`metNewton()`  |funcion, derivada, variable, x_0, tolerancia   |
|`secantMetho()`|funcion, variable, supin0, supin1, tolerancia  |
|`hibrido()`    |funcion, variable, intervalo, tolerancia       |

En todos los casos todos los parámetros son obligatorios excepto la tolerancia, la cual está por default en $1 \times 10^{-6}$

## Ejemplos

### Función `bisec()`

Esta función nos permite obtener una aproximación de la raíz usando el método de la bisectriz devuelve una lista con dos elementos:  
`[{Raíz aproximada}, {Evaluación de la función provista en la aprximación}]`

El que devuelva el segundo elemento simplemente sirve para comprovar que tan cerca se encuentra el valor calculado de ser una raíz

```python
f = x**3 - 5* x**2 + 7 
    
resultado = bisec(f,x,-10,10)

print(f"La raíz aproximada es {resultado[0]} y su evaluación en la función es {resultado[1]}")
```

### Función `metNewton()`

Esta función nos permite aproximar raíces por medio del método de Newton Rapson.Usa la fórmula iterativa: $x_{n+1} = x_n - f(x_n)/f'(x_n)$ Devuelve una lista de dos elementos:  
`[{Raíz aproximada}, {Evaluación de la función provista en la aprximación}]`

```python
import sympy as s

func = s.exp(x) - 5*x       #Declaramos la función a la cual le queremos aplicar el método

derivfunc = s.diff(func, x) #Obtenemos su derivada con ayuda de la biblioteca Sympy

suposicionInicial = 1       

tolera = 1e-6               #Definimos nuestra tolerancia, Aunque es opcional

raiz = metNewton(func, derivfunc, x, suposicionInicial, tolera)

print(f"La raíz aproximada es {raiz[0]}, y su evaluación en la función es {raiz[1]}")
```

### Función `secantMetho()`

Obtiene raices aproximadas con el metodo de la secante, utilizando la fórmula iterativa: $x_{n+1} = x_n - f(x_n)(x_n - x_{n-1})/(f(x_n) - f(x_{n-1}))$  
Al igual que las funciones anteriores, devuelve una lista con 2 elementos, la raíz aproximada y su evaluación en la función

```Python
import sympy as s
x = s.symbols('x')

func = x**2 - 4

x_0 = 0            
x_1 = 1         
#Por ser el método de la secante, tenemos que definir 2 valores para x

toleramos = 1e-6

aproximacion = secanteMetho(func, x, x_0,x_1,toleramos)

print(f"La raíz aproximada de la función es {aproximacion[0]}, y su evaluación en la función es {aproximacion[1]}")
```

### Función `hibrido()`

Combina los métodos de bisección y de Newton. Primero reduce el intervalo a un ancho con una tolerancia específicada, y después toma la raíz aproximada y usa eso como suposición inicial en el método de Newton. Devuelve una lista con 2 elementos  
`[{Raíz aproximada}, {Evaluación de la función provista en la aprximación}]`

```Python
import sympy as s
x = s.symbols('x')
interval = [1.5, 2.5]
raiz = hibrido(x**3 -6*x**2 +11*x - 6, x, interval, 1e-6)

print(f"Una raíz aproximada de la funcion es {raiz[0]}, y su evaluación es {raiz[1]}")

```
