################## Ejercicio 1 ##################

'''
Crear una clase Cliente que tenga como propiedades:
nombre, CIF, vip: boolean
por defecto todos los clientes seran NO vip
crear un metodo que me muestre la informacion
Crear 2 clientes
'''
"""
class Cliente:

    def __init__(self, nombre: str, cif: int, vip: bool = False):
        self.nombre = nombre
        self.cif = cif
        self.vip = vip

    def info_client(self):
        es_vip = "SI" if self.vip else "NO"
        print(f"Nombre: {self.nombre}; Edad: {self.cif}; VIP: {es_vip}")

cliente_1 = Cliente("Ismael", 1231231232, True)
cliente_2 = Cliente("Pepito", 7987899878)

cliente_1.info_client()
cliente_2.info_client()"""

################## Ejercicio 2 ##################

'''
Crear una clase Direccion que tenga como propiedades:
nombre, CIF, vip: boolean, direccion (calle, numero, poblacion)
por defecto todos los clientes seran NO vip
crear un metodo que me muestre la informacion
Crear 2 clientes
'''

class Direccion:

    def __init__(self, calle, numero, poblacion):
        self.calle = calle
        self.numero = numero
        self.poblacion = poblacion

    def mostrar_info(self):
        return f"{self.calle}; {self.numero}; {self.poblacion};"

class Cliente:

    def __init__(self, nombre: str, cif: int, direccion: Direccion, vip: bool = False):
        self.nombre = nombre
        self.cif = cif
        self.vip = vip
        self.direccion = direccion # Direccion se ha vuelto una clase un atributo o propiedad de esta clase

    def info_client(self):
        es_vip = "SI" if self.vip else "NO"
        dir = self.direccion.mostrar_info() # para usar ese atributo
        print(f"Nombre: {self.nombre}; Edad: {self.cif}; VIP: {es_vip}; Direccion: {dir}")

direccion = Direccion("Vallecas", 7, "Madrid")
cliente_1 = Cliente("Ismael", 1231231232, direccion, True)
cliente_2 = Cliente("Pepito", 7987899878, Direccion("Diagonal", 5, "Madrid"))

cliente_1.info_client()
cliente_2.info_client()

print(type(direccion))
print(type(cliente_1))

print("Mismo objeto:", direccion is cliente_1.direccion)
print("Mismo objeto:", direccion is not cliente_1.direccion)