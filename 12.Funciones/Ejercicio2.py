#Escribir una función que reciba un número entero positivo y devuelva
#su factorial.
def factorial():
    from math import factorial
    numero = int(input("Ingresa un numero:"))
    if numero > 0:
        print(factorial(numero))
    else:
        print("El numero es negativo y no podemos proceder")

factorial()

