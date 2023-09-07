"""
Escribir un programa que pida al usuario un número positivo y muestre en pantalla
si es primo o no.
"""
import math as m
numero = int(input("Introduzca un número para saber si es primo o no:"))

if numero >= 2:
    for i in range(2,m.floor(m.sqrt(numero))+1):
        modulo= numero%i
        if modulo!= 0: continue
        else: print(f"El numero {numero} es divisible por {i}, por lo que no es primo"); break
        print(f'El número {numero} es primo yeii')
elif numero == 1:
    print("El número 1 no es primo")
elif numero <=1:
    print("Introduce un positivo, vuelve a intentarlo")