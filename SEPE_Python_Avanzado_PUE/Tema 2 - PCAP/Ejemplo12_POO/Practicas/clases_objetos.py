class Persona:

    # Constructor por defecto, desaparece en cuanto
    # creas otro constructor, porque Python no
    # permite sobrecarga (NO ES NECESARIO PONERLO)
    '''def __init__(self):
        pass'''

    def __init__(self, nombre="", edad=0):
        # Variables de instancia
        self.nombre = nombre
        self.edad = edad

    # Metodos: Son funciones declaradas dentro de una clase
    def mostrar_info(self): # si no pongo el argumento self, no lo reconoce como metodo de la clase Persona
        print("Hola Mundo")
        print("Hola Mundo, mi nombre es", self.nombre, " y mi edad es", self.edad, "años.")
        print("Hola Mundo, mi nombre es {} y mi edad es {} años.".format(self.nombre, self.edad))
        print(f"Hola Mundo, mi nombre es {self.nombre} y mi edad es {self.edad} años.")

    def nombre_mayusculas(self):
        return self.nombre.upper()

# Crear objetos o instancias de Persona
p1 = Persona() # Invoco/Instancio el constructor por defecto
print(p1)

"""Lo que hay dentro de la variable es el objeto ya instanciado,
lo que hay en la asignacion del valor es la instancia
"""
# Objeto
p2 = Persona("Juan", 37) # Instancia del objeto
print(p2)

p3 = Persona("Pepito")
print(p3)

p4 = Persona(edad=29)
print(p4)

p1.mostrar_info()
p2.mostrar_info()
print(p3.nombre_mayusculas())

p2.nombre = "Juan"
print(p2.nombre)
p2.mostrar_info()