#Ejercicio 2
# Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el
# rango de esos 2 números, pero, solo imprimiendo los números que sean impares

numero1 = int(input("Ingrese un numero de inicio: "))
numero2 = int(input("Ingrese un numero mas alto que el anterior: "))

for i in range(numero1,numero2, +1):
    if i % 2 != 0:
        print("Estos son los numeros impares: ", i)