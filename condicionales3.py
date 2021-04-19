'''edad=-7
if 0<edad<100:
    print("Edad es correcta")
else:
    print("Edad incorrecta")'''

salario_presidente=int(input("Introduce Salario Presidente: "))
print("Salario Presidente: "+str(salario_presidente))

salario_director=int(input("Introduce Salario Director: "))
print("Salario director: "+str(salario_director))

salario_jefe_area=int(input("Introduce Salario Jefe Área: "))
print("Salario Jefe Área: "+str(salario_jefe_area))

salario_administrativo=int(input("Introduce Salario Administrativo: "))
print("Salario Administrativo: "+str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("Todo funciona correctamente")
else:
    print("Algo falla en esta empresa")