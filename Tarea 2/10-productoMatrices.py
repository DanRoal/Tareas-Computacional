"""
Escribe un programa que almacene las 2 matrices A y B en listas y muestre en pantalla su producto
"""

def productMat(MatrizA, MatrizB):
    resultado = []
    for i in range(len(MatrizA)):
        resultado.append([])
        fila_i = 0
        for h in range(len(MatrizB[i])):
            for x in range(len(MatrizA[i])):
                fila_i += MatrizA[i][x] * MatrizB[x][h]
            resultado[i].append(fila_i)
    return resultado

A = [[1,2,3], [4,5,6]]
B = [[1,-1],[0,1],[-1,1]]

C= [[1,3,6],[9,3,-2],[-1,0,4]]
D= [[2,-1,-3],[4,2,1],[0,3,1]]

print(productMat(A,B))

print(productMat(C,D))