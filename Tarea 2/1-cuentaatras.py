"""
Escribir un programa que almacene en una lista los numeros del 1 al 10 y los
muestre en orden inverso separados por comas
"""
lista = []
for i in range(1,11):
    lista.append(i)
cuenta= ''
for i in range(1,11):
    if lista[-i]!=lista[0]: 
        cuenta = cuenta + f"{lista[-i]}, "
    else : cuenta = cuenta + f"{lista[0]}"

print(cuenta)