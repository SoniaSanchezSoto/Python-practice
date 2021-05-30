'''altura = int(input("Altura del triángulo: "))

for i in range(altura):
    for j in range(i + 1):
        print("* ", end="")
    print()'''

altura = int(input("Altura de la línea: "))

for i in range(altura):
    for j in range(i):
        print(" ", end="")
    print("*")