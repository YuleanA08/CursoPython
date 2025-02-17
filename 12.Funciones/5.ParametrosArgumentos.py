#Esta no, ya que ya estan definidas las variables, es por asi decirlo una funcion estatica
def suma():
    num1 = 20
    num2 = 30
    suma = num1 + num2
    return suma

print(suma())

#Esta funcion se puede reutilizar
def suma1(num1,num2):
    suma=  num1 + num2
    return suma

print(suma1(50,40))