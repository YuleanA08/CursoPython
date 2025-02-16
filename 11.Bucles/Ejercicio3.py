#Ejercicio 3
#Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario
#dos numeros y mostrar el rango de numeros entre ambas cifras

for i in range(1,11):
    print(i)

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese un numero mas alto que el anterior: "))

for i in range(numero1,numero2+1):
    print("numero: ",i)