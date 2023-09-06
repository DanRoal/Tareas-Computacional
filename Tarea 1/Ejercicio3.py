"""
Un programa que pide al usuario un entero positivo y muestre 
por pantalla la cuenta atras desde ese numero hasta 0 separados por comas
"""

numero = int(input("Por favor introduza numero para cuenta regresiva:"))
lista = []

for i in range(-numero,1): 
    lista.append(-1*i)

print(lista)