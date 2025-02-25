class A ():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0
#Esta es la manera de usar get, tenlo en mente
    @property
    def cuenta (self):
        return self._cuenta
#Esta es la manera de usar set, tenlo en mente
    @cuenta.setter
    def set_cuenta(self, cuenta):
        self._cuenta = cuenta

    
    @property
    def contador (self):
        return self._contador
    @contador.setter
    def set_contador(self, contador):
        self._contador = contador


a = A()

a.set_cuenta = 21398516

print(a.cuenta)
print(a.contador)

a.set_contador= 20
print(a.contador)