# Ejercicio 1
# Realizar un programa que conste de una clase llamada Estudiante,
# que tenga como atributos el nombre y la nota del alumno. Definir los
# métodos para inicializar sus atributos, imprimirlos y mostrar un mens
# aje con el resultado de la nota y si ha aprobado o no.

class Estudiantes ():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def imprimirNota (self):
        print ("Esta es la nota: {} de: {}".format(self.nombre, self.nota))
    def aprobo (self):
        if self.nota >= 3:
            print ("El estudiante Aprobo")
        else:
            print ("El estudiante Reprobo")

estudiante1 = Estudiantes("YUYU", 4)
estudiante1.imprimirNota()
estudiante1.aprobo() 


estudiante2 = Estudiantes("Lala", 2)
estudiante2.imprimirNota()
estudiante2.aprobo() 