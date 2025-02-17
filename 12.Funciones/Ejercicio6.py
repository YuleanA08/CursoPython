#Ejercicio 6
#Escribir una función que reciba una muestra de números en una lista
#y devuelva su medida.

def media (*num):
    print("Tamaño de muestra:",len(num))
    for i in num:
        print("Muestra:",i)
    return sum(num)/len(num)

print("Mediana:",media(1,2,3,4,5,6,7,8,9,10),)
