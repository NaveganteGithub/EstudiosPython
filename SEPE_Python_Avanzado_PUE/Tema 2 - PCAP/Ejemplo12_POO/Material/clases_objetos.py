class Persona:
    # Constructor por defecto
    '''
    def __init__(self):
        pass
    '''

    # En Python solo se permite un constructor por clase
    def __init__(self, nombre="", edad=0):
        #print("En el constructor recibimos", nombre, edad)
        # Crear las variables de instancia: Cada instancia mantiene una copia de esas variables
        self.nombre = nombre
        self.edad = edad

    # Metodos:  Son funciones declaradas dentro de la clase
    # se invocan a traves del objeto
    def mostrarInfo(self):  # si no pongo el argumento self, no lo reconoce como metodo de la clase Persona
        print("Nombre:", self.nombre, "Edad:", self.edad)
        print("Hola me llamo {} y tengo {} años".format(self.nombre, self.edad))
        print(f"Hola me llamo {self.nombre} y tengo {self.edad} años")

        # Si no pongo self NameError: name 'nombre' is not defined
        #print("Nombre:", nombre, "Edad:", edad)

    def nombre_mayusculas(self):
        return self.nombre.upper()

    # En Python no permite sobrecarga de metodos
    # TypeError: Persona.nombre_mayusculas() missing 1 required positional argument: 'num'
    def nombre_mayusculas(self, num):
        return self.nombre.upper()

# Crear objetos o instancias de Persona
p1 = Persona()  # Invoco al constructor por defecto
print(p1)

p2 = Persona("Juan", 37)
print(p2)

p3 = Persona("Pepito")
p4 = Persona(edad=29)

# Invocar al metodo mostrarInfo()
p1.mostrarInfo()
p2.mostrarInfo()

# Invocar al metodo nombre_mayusculas
print(p3.nombre_mayusculas())
print(p3.nombre_mayusculas(num=7))

# tengo acceso a las propiedades, son publicas
p2.nombre = "Nuevo_Juan"
print("Nuevo nombre de Juan:", p2.nombre)
p2.mostrarInfo()