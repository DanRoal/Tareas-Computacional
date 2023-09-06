"""
Programa que pregunte al usuario una cantidad a invertir, el interes anual y el numero
de años, y muestre en pantalla el capital obtenido en la inversión cada año que dura
"""

inversionInicial = float(input("Introduzca su inversion inicial"))
interes = float(input("introduzca la tasa de interes como porcentaje:"))
anos = int(input("Por favor introduzca cuantos años va a dejar su dinero"))

for i in range(1,anos+1):
    print(inversionInicial * (1 + (interes)/100)**i)