'''class FabricaTelefonos():
    marca = "Samsung"
# Cada vez que utilices metodos o metodos de instancia, debes utilizar el parametro self
    def ElaborarHuangwei(self):
        self.marca = "Huangwei"

telefono = FabricaTelefonos()
print(telefono.marca)

telefono.ElaborarHuangwei()
print(telefono.marca)'''

class FabricaTelefonos():
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
telefono = FabricaTelefonos("Samsung", "Rojo")
print(telefono.marca)
print(telefono.color)
# The __init__ method is called when the class is instantiated