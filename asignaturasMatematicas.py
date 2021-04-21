print("Asignaturas Carrera Matemáticas Año 2021")
print("Asignaturas: Algebra Lineal - Cálculo Diferencial - Estadistica - Probabilidad - Lógica MAtemática - Variable Compleja")
opcion=input("Escribe la asignatura escogida: ")

asignatura=opcion.lower()

if asignatura in ("algebra lineal", "cálculo diferencial", "estadistica", "probabilidad", "lógica matemática", "variable compleja"):
    print("Asinatura elegida " + asignatura)
else:
    print("La asignatura escogida no está contemplada")