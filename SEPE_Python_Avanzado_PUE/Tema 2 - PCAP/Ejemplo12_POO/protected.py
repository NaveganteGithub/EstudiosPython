class A:
    def __init__(self):
        self.publica = "publica"
        self._protegida = "protected"
        self.__privada = "privada"

class B(A):
    def prueba(self):
        print(self.publica)
        print(self._protegida)
        # print(self.__privada)  # No tenemos acceso a recursos privados


b = B()
b.prueba()
print(b.publica)
print(b._protegida)
# print(b.__privada)  # No tenemos acceso a recursos privados
# print(b._A__privada) # (Name Mangling)