class FabricaTelefonos():
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        print("Se ha creado un objeto con la marca {} y color {}".format(marca, color))
        # El metodo __init__ se llama cuando la clase es instanciada o apenas comienza

    def __str__(self):
        return "El objeto es {}".format(self.marca)
    # Este metodo se utiliza para mostrar una representacion en cadena del objeto o conocer los atributos del objeto

    def __del__(self):
        print("El objeto {} de color {} ha sido destruido".format(self.marca, self.color))
    # The __del__ method is called when the object is destroyed


telefono = FabricaTelefonos("Samsung", "Rojo")
print(telefono)