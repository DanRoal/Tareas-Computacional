"""
Escribir un programa que muestre el eco de todo lo que el usuario introduza
hasta que el usuario escriba "salir"
"""
print("Bienvenido a mi programa eco, para salir escribe 'salir', de otra forma, eco")
while True:
    eco = input()
    if eco!= 'salir':
        print(eco)
        continue
    else: break