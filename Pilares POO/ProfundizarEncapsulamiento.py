class A():
    def __init__(self):
        self._contador = 0
        self.cuenta = 0

    def incremento(self):
        self._contador += 1
    
    def cuenta (self):
        return self._contador
a = A()
'''print(a.cuenta)
a.cuenta = 20
print(a.cuenta)''' 
# No es una buena practica esto, cuando veas un guion bajo es para avisarte y avisarle a otro
#programador que ese dato no se debe modificar 