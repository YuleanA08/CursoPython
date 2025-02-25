class Animales ():
    def mamifero (self):
        print("Soy un mamifero")

    def descripcion (self):
        print("Yo soy un {}".format(self.animal))

class Perro (Animales):
    pass

class Gato (Animales):
    def __init__(self, animal):
        self.animal = animal

animal = Animales()
animal.mamifero()

perro = Perro()
perro.mamifero()

gato = Gato("Gato")
gato.descripcion()