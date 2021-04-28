'''for letra in "Matematicas":  
    print("Viendo la letra: "+ letra)'''

''' #ignorar# 

for letra in "Matematicas":
    
    if letra=="t":
        continue

    print("Viendo la letra: "+ letra)'''

'''nombre="Pildoras Informaticas"

contador=0

for i in nombre:

    if i==" ":
        continue
    contador+=1

print(contador)'''

email=input("Introduce tu email, por favor: ")

for i in email:

    if i=="@":

        arroba=True

        break;

else:

    arroba=False

print(arroba)