class FabricadeTelefonos():
    marca = "Samsung"
    color = "Rojo"
    memoria = "64GB"
    almacenamiento = "128GB"

    def llamar(self, mensaje):
        return mensaje
    
    def escucharmusica(self, cancion):
        return "Estas escuchando muscia de " + cancion


telefono = FabricadeTelefonos()

telefono.color
print(telefono.marca)
print(telefono.color)

print(telefono.llamar("Hola, ¡Estoy llamando!"))
print(telefono.escucharmusica("Queen"))