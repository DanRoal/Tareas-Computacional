"""
Un programa que pide al usuario un entero positivo y muestre 
por pantalla la cuenta atras desde ese numero hasta 0
"""

numero = int(input("Por favor introduza numero para cuenta regresiva:"))

for i in range(-numero,1):
    print(-1*i)