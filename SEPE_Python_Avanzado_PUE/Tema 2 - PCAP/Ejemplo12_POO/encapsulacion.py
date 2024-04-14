'''
    Crear clase Fecha (dia, mes y anyo)
    con metodo mostrarFecha()
'''
class Fecha:
    # constructor
    def __init__(self, dia, mes, anyo):
        # variables de instancia
        # Son publicas: se puede acceder a ella para leer o modificar el valor
        self.dia = dia
        self.mes = mes
        self.anyo = anyo

    # metodo de instancia
    # Metodo publico
    def mostrarFecha(self):
        # dia/mes/año
        return f"{self.dia}/{self.mes}/{self.anyo}"

#hoy = Fecha(11,4,2024)
hoy = Fecha(278,87,-26)
# Modifico el valor de dia
hoy.dia = 1000
print("Hoy:", hoy.mostrarFecha())


'''
    Un clase encapsulada tiene todas sus propiedades son privadas y se accede a ellas
    a traves de los metodos de acceso publicos: getter y setter
'''
class FechaEncapsulada:
    # constructor
    def __init__(self, dia, mes, anyo):
        # _nombre -> variable protected (herencia)
        # __nombre -> variable privada
        # Tambien puedo crear aqui las variables inicializadas a 0
        self.__dia = 0
        self.__mes = 0
        self.__anyo = 0
        # Pero siempre hay que invocar los metodos set porque es donde hacemos las validaciones
        self.setDia(dia)
        self.setMes(mes)
        self.setAnyo(anyo)

    # Metodos de acceso publico:
    # getXXX() de lectura, retornan el valor de la variable
    # setXXX() de escritura, establecer o modificar el valor
    def getDia(self):
        return self.__dia


    def setDia(self, dia):
        # comprobacion que el dia recibido es correcto
        # damos por bueno si el dia esta entre 1 y 31
        if dia > 1 and dia <= 31:
            # Son privadas: no se puede acceder a ella desde fuera de la clase
            self.__dia = dia
        else :
            print("Dia no es valido")

    def getMes(self):
        return self.__mes

    def setMes(self, mes):
        # comprobacion que el mes recibido es correcto
        # damos por bueno si el mes esta entre 1 y 12
        if mes >= 1 and mes <= 12:
            self.__mes = mes
        else:
            print("Mes no es valido")

    def getAnyo(self):
        return self.__anyo

    def setAnyo(self, anyo):
        # comprobacion que el anyo recibido es correcto
        # damos por bueno si el año esta entre 2024 y 2025
        if anyo == 2024 or anyo == 2025:
            self.__anyo = anyo
        else:
            print("Anyo no es valido")

    # metodo de instancia
    # Metodo publico
    def mostrarFecha(self):
        # dia/mes/año
        return f"{self.__dia}/{self.__mes}/{self.__anyo}"

fecha = FechaEncapsulada(278,87,-26)

# Modifico el valor de dia
# Acabo de crear una variable __dia y otra
fecha.__dia = 1000   # Al ser una variable privada, no tengo acceso
fecha.otra = "Pepito"

print("Hoy:", fecha.mostrarFecha())

# Accedemos a traves de los metodos de acceso
fecha.setDia(11)
fecha.setMes(4)
fecha.setAnyo(2024)
print("Hoy:", fecha.mostrarFecha())

# name mangling
print("Acceso a variable privada:", fecha._FechaEncapsulada__dia)

# ver el contenido del objeto
print(fecha.__dict__)

# Mostrar una lista con todos los recursos del objeto
print(dir(fecha))

# Mostrar una lista con todos los recursos de la clase
print(dir(FechaEncapsulada))

# Comprobar si el objeto tiene el atributo otra
print(hasattr(fecha, "otra"))   # True
print(hasattr(fecha, "__mes"))  # False
print(hasattr(fecha, "_FechaEncapsulada__mes"))  # True

# Saber el nombre de la clase  que se ha instanciado para obtener el objeto
print(FechaEncapsulada.__name__)
print(type(fecha).__name__)

# Retorna si el objeto es instancia de esa clase
print(isinstance(fecha, FechaEncapsulada))  # True
print(isinstance(hoy, (FechaEncapsulada, Fecha)))   # True  tupla(Clase1, Clase2)
print(isinstance(hoy, FechaEncapsulada))  # False

# Leer el valor de un atributo
#print(getattr(fecha, __mes))  # NameError: name '__mes' is not defined
print(getattr(fecha, "_FechaEncapsulada__mes"))
print(getattr(fecha, "otra"))

# Establecer el valor de un atributo
print(setattr(fecha, "_FechaEncapsulada__mes", 8))
print(fecha.mostrarFecha())
