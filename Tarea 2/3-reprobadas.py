"""
Escribir un programa que almacene las asignaturas de  un curso, (Por ejemplo
Matetmáticas, física, química historia y lengua) en una lista, pregunte
al usuario la nota que ha sacado en cada asignatura y elimine de la lista
las asignaturas aprobadas. al final el progrma debe mostrar porpantalla las
asignaturas que el usuario debe repetir.
"""

materias = ['espanol',
            'matematicas',
            'fisica',
            'quimica']

reprobadas = []
for asignatura in materias:
    calif = int(input(f'cual fue tu calificacion en la asignatura de {asignatura}:'))
    if calif < 6:
        reprobadas.append(asignatura)

print('Las materias que reprobaste fueron: ' + ', '.join(i for i in reprobadas))