#Escribir una tupla que tenga las letras del alfabeto. Luego, debes
#pedir al usuario un número, el que haya ingresado, es la letra que
#debe imprimir el programa

alfabeto = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

Nmros=int(input("Ingrese un numero entero: "))
if Nmros > 0 and Nmros < len(alfabeto):
    print("La letra seleccionada fue la: "+alfabeto[Nmros-1])
else:
    print("Este numero es muy grande o es negativo y no esta en nuestra base de datos para asignarle una leta")