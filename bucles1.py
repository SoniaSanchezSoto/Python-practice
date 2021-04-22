'''for i in ["primavera","verano","otoño","invierno"]:
    print(i)'''

'''for i in ["pildoras","informatica",3]:
    print("Hola", end="  ")'''

'''for i in "mateo@pildorasinformaticas.es":
    print("Hola", end="  ")'''

email=False

for i in "mateopildorasinformaticas.es":
    
    if(i=="@"):
        
        email=True

if email==True:
    print("Email es correcto")
else:
    print("El Email no es correcto")