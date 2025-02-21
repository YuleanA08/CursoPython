class FabricaCarros ():
    def __init__(self, marca, *modelos, **colores):
        self.marca = marca
        self.modelos = modelos
        self.colores = colores

carro = FabricaCarros("Toyota", "Corolla", "Yaris", "Hilux", rojo ="Rojo", azul = "azul ", verde = "Verde")

# Si lleva un * se convierte en tupla, si lleva ** se convierte en diccionario
#La tupla se puede recorrer con un for, el diccionario con un for y un .items()
# La manera de agregar los valores es con un =, no con :, en el diccionario

print(carro.marca)
print(carro.modelos)
print(carro.colores)