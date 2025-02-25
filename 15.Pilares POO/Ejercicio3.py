# Ejercicio 1
# Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio;
# luego crear dos clases mas que hereden de Fabrica, las cuales
# son Moto y Carro. Crear metodos que muestren la cantidad de llantas,
# color y precio de ambos transportes. Por ultimo, crear objetos para
# cada clase y mostrar por pantalla los atributos de cada uno

class Fabrica ():
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

class Moto(Fabrica):
    def detalles (self):
        print ("La moto tiene una cantidad de llantas de:{}\nel color es:{}\nel precio es:{}\n".format(self.llantas,self.color,self.precio))
class Carro(Fabrica):
    def detalles (self):
        print ("El carro tiene una cantidad de llantas de:{}\nel color es:{}\nel precio es:{}".format(self.llantas,self.color,self.precio))


moto1 = Moto(2,"rojo", "$10.000.000")
moto1.detalles()

carro1 = Carro(4,"negro", "$44.000.000")
carro1.detalles()
        