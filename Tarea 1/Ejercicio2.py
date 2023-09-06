"""
Escribir un programa que pida al usuario un numero entero positivo y
muestre en pantalla todos los números impares desde 1 hasta ese numero
separados por comas
"""

numero = int(input("Introduzca para saber los numeros impares antes del mismo:"))

for i in range(numero):
    impar = i%2
    if impar == 1:
        print(i)