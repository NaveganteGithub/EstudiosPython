
class MiClase:

    apto: bool

    def __init__(self, nomb, apto):
        self.nombre = nomb
        MiClase.apto = apto

    def imprimir(self):
        print(self.nombre)

    def isemploye(self, contratado: bool):
        return MiClase.apto and contratado


instancia = MiClase("Ismael", True)
instancia.imprimir()

es_empleado = instancia.isemploye(contratado=True)
if es_empleado:
    print("Es un empleado")

print(instancia.nombre)
print(MiClase.apto)

instancia_2 = MiClase("David", True)
instancia_2.imprimir()

es_empleado = instancia_2.isemploye(True)
if es_empleado:
    print("Es un empleado")

print(hash(instancia))
print(hash(instancia_2))

instancia_3 = MiClase("Andres", False)
print(MiClase.apto)
