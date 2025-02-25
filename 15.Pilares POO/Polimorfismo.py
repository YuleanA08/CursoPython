class Animales ():
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def mamifero (self):
        print(self.mensaje)

class Perro(Animales):
    def mamifero(self):
        print ("Yo si soy un mamifero")

class Pez(Animales):
    def mamifero(self):
        print("Soy un pez, hago glugluglu")

perro = Perro("lulu")
perro.mamifero()

animal = Animales("Mimi")
animal.mamifero()

pez = Pez("Nada")
pez.mamifero()