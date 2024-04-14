'''
    Crear una clase Cliente que tenga como propiedades:
        nombre, CIF, vip: boolean, direccion (calle, numero, poblacion)
        por defecto todos los clientes seran NO vip
        crear un metodo que me muestre la informacion

        Crear 2 clientes
'''
class Direccion:  # Los nombres de las clases comienzan en Mayusculas
    def __init__(self, calle, numero, poblacion):
        self.calle = calle
        self.numero = numero
        self.poblacion = poblacion

    def mostrarDir(self):
        # Gran Via, 7 (Madrid)
        return (f"{self.calle}, {self.numero} ({self.poblacion})")

class Cliente:
    def __init__(self, nombre, cif, direccion: Direccion, vip=False):  # direccion es el argumento del constructor, es una variable
        # Variables de instancia
        self.nombre = nombre
        self.cif = cif
        self.vip = vip
        # en self.direccion se almacena de referencia del objeto Direccion recibido en el constructor
        self.direccion = direccion  # self.direccion es una propiedad de la clase Cliente

    def mostrarInfo(self):
        print(f"Nombre: {self.nombre} CIF: {self.cif} vip: {self.vip} Direccion: {self.direccion.mostrarDir()}")



# Crear 2 instancias de Cliente
# Primero creo una instancia u objeto de Direccion y luego
# lo paso al constructor de Cliente
dir = Direccion("Gran Via", 7, "Madrid")
cliente1 = Cliente("Transportes Perez", "B-12345678", dir,True)

#cliente1 = Cliente("Transportes Perez", "B-12345678", "dir",True)

# En el momento de crear el objeto Cliente tambien estoy creando el objeto Direccion
cliente2 = Cliente("Fruteria Antonio", "B-98765432", Direccion("Diagonal", 67, "Barcelona"))

# Mostrar la inormacion
cliente1.mostrarInfo()
cliente2.mostrarInfo()

# Operadores de identidad: is y is not
# Comprobar si los variables apuntan al mismo objeto
print("Mismo objeto: ", dir is cliente1.direccion)   # True
print("Mismo objeto: ", dir is not cliente1.direccion) # False
print("Mismo objeto: ", dir is not cliente2.direccion) # True