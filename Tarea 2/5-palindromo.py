"""
Un programa que detecte si una palabra que introsuzca el usuario
es un palíndromo o no
"""
palabra = list(input("Por favor introduce una palabra para saber si es palíndromo o no: \n"))

reverso = "".join(i for i in palabra[::-1])
if "".join(i for i in palabra)==reverso:
    print(f"La palabra {''.join(i for i in palabra[::-1])} es palíndromo")
else:
    print(f"{''.join(i for i in palabra)} no es palíndromo, intenta de nuevo")
