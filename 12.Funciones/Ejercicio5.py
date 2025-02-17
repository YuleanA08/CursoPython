#Ejercicio 5
#Crear un programa que tenga dos funciones, una que contenga el 
#area de un cuadrado con argumentos de base y altura; y la otra el area
#de un circulo con argumento de radio

import math

def areaCuadrado(base, altura):
    areaCUA = base * altura
    return areaCUA

print(areaCuadrado(20,10))

def areaCirculo(radio):
    return math.pi * (radio**2)
    
print(areaCirculo(10))