#Ejercicio 3
#Crear una funcion que pida dos numeros. Si el primero es mayor al se
#gundo, el programa debe retornar el valor 1; si el segundo es mayor al
#primero, debe retornar -1; si ambos son iguales, debe retornar O

def pedir ():
    n1 = float (input("Ingresa un numero:"))
    n2 = float (input("Ingresa un numero:"))

    if n1 > n2:
        return 1
    elif n1 < n2:
        return -1
    else:
        return 0

print(pedir())