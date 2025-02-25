# Ejercicio 2
# Realizar un programa en el cual se declaren dos valores enteros porteclado 
# utilizando el método init . Calcular después la suma, resta,
# multiplicación y división. Utilizar un método para cada una e imprimir
# los resultados obtenidos. Llamar a la clase Calculadora.

class Calculadora ():
    def __init__(self):
        self.num1 = int(input("Ingresa tu primer numero: "))
        self.num2 = int(input("Ingresa tu segundo numero: "))
    def suma (self):
        print (self.num1 + self.num2)
    def resta (self):
        print (self.num1 - self.num2)
    def multiplicacion (self):
        print (self.num1 * self.num2)
    def division (self):
            try:
                print (self.num1 / self.num2)
            except ZeroDivisionError:
                print("No se puede dividir entre 0")

calculadora = Calculadora()
calculadora.suma()
calculadora.resta()
calculadora.multiplicacion()
calculadora.division()