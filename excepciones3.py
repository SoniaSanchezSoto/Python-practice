'''def evaluaEdad(edad):

    if edad<0:
        raise TypeError("No se permiten edades negativas")
    if edad<20:
        retur "Eres muy joven"
    elif edad<40:
        return "Eres Joven"
    elif edad<65:
        return "Eres Maduro"
    elif edad <100:
        return "Cuídate..."

print(evaluaEdad(18))'''

import math

def calculaRaíz(num1):

    if num1<0:
        raise ValueError ("El número no puede ser negativo")
    
    else:
        return math.sqrt(num1)

op1=(int(input("Introduce un número: ")))

try:
    print(calculaRaíz(op1))

except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)
    
print("Programa Terminado")