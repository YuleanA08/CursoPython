while True:
    try:
        num1 = int(input("Ingresa un numero entero:"))
        resultado = num1/100
        print(resultado)
        break
    except ZeroDivisionError:
        print("No se puede dividir entre 0")

while True:
    try:
        edad = int (input("Ingresa tu edad:"))
        print("Tu edad es:", edad)
        break
    except ValueError:
        print("Has colocado un valor erroneo")
    except KeyboardInterrupt:
        print("\nHaz cancelado la ejecucion")
    
#Es bueno tener este ultimo en cuenta ya que puede existir la posiblidad
#Que el usario le de cntrol + c y cierre el programa.