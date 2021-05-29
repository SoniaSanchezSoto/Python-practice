Tamano = 10
 
print("A)")
for i in range(Tamano):
    print("*"*i)
 
print("")
print("B)")
for i in range(Tamano):
    for j in range(i, Tamano-1):
        print("*", end="")
    print()
 
print("")
print("C)")
for i in range(Tamano):
    espacios = Tamano - i
    print(i*" "+"*"*espacios)
 
print("")
print("D)")
for i in range(Tamano):
    espacios = Tamano - i
    print(" "*espacios+"*"*i)