"""
Escribir un programa que almacene la cadena de caracteres en una variable,
pregunte al usuario por la contraseña hasta que ingrese la contraseña correcta
"""

contrasena = "contraseña"

while True:
    intento = input('introduzca la contraseña:\n')
    if intento==contrasena:
        print("Felicidades adivinaste la contraseña")
        break
    elif intento=='exit':
        break
    else:
        print("Esa no es la contraseña, intenta de nuevo o escribe exit para dejar de intentar")