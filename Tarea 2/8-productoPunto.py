"""
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2)
en dos listas y muestre por pantalla su produto escalar
"""
def productoPunto(vecA, vecB):
    resultado = []
    suma = 0
    for i in range(len(vecA)):
        resultado.append(vecA[i] * vecB[i])
    for i in resultado:
        suma = suma + i
    return suma

vector1 = [1,2,3]
vector2 = [-1,0,2]

print(productoPunto(vector1, vector2))

