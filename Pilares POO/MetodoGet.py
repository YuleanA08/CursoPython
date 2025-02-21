class A ():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0

    @property
    def get_cuenta (self):
        return self._cuenta
    @property
    def get_contador (self):
        return self._contador


a = A()
print(a.get_cuenta)
print(a.get_contador)
    