'''def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="suspenso"
    return valoracion
print(evaluacion(4))'''

'''print("Programa de evaluación de notas de alumnos")
nota_alumno=input()
def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="suspenso"
    return valoracion
print(evaluacion(int(nota_alumno)))'''

print("Programa de evaluación de notas de alumnos")
nota_alumno=input("Introduce la nota del alumno")

def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="suspenso"
        calificacion=7
    return valoracion
print(evaluacion(int(nota_alumno)))