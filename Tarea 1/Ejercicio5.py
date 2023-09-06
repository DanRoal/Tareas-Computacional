

contrasena = "holacrayola"

while True:
    intento = input('introduzca la contraseña:\n')
    if intento==contrasena:
        print("Felicidades adivinaste la contraseña")
        break
    elif intento=='exit':
        break
    else:
        print("esa no es la contraseña, intenta de nuevo o escribe exit para dejar de intentar")

