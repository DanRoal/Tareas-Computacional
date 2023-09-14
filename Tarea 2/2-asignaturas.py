"""
Escribir un programa que almacene las asignaturas de un curso (Por ejemplo
matemáticas, física) en una lista y la muestre por pantalla el mensaje
'Yo estudio <asignatura> donde <asignatura> es cada una de las asignaturas de la lista
"""

asignaturas= ['Fisica atomica y materia condensada',
            'Fisica computacional',
            'Mecanica cuantica',
            'fisica estadistica',
            'Laboratorio de Electronica',
            'Electromagnetismo 2']

for asignatura in asignaturas:
    print(f'Yo estudio {asignatura}')