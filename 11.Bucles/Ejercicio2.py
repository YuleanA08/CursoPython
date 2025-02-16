#Ejercicio 2
#Escribir un programa que pregunte al usuario su edad y muestre por
#pantalla todos los años que ha cumplido (desde hasta su edad).

edad = int (input("Ingrese tu edad: "))

i=1

while i != edad:
    i +=1
    print("Has tenido estas edades:", i, "años")
    