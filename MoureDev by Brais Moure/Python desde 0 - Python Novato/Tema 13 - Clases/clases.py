# Clases

'''
Las clases son objetos que nos permiten almacenar
funciones, atributos, datos, subclases, para utilizarlos
despues

Las clases en Python deben escribirse con Camel Case, la letra de
cada palabra del nombre en mayuscula, pero sin espacios,
sin guiones bajos
'''

class MyEmptyPerson:
    pass # Pass no hace nada, simplemente es una instruccion de pasar, de no hacer nada

# Indica la ruta de la clase
print(MyEmptyPerson)
# Las clases se almacenan en un direccion de memoria
print(MyEmptyPerson())


'''
Las clases representen objetos en la vida real,
en este caso a una persona

Esta funcion llamada __init__ es un contructor es
la funcion que permitira cargar informacion a la
clase, esta es la primera funcion que va a ejecutar
la clase antes de ejecutar las otras

El operador __init__ no es inmutable, tienes permiso
para hacer los cambios dados para la el proyecto
'''
class Person:
    def __init__(self): # Con esto declaramos que no devuelva nada
        pass

print()

class Person:
    def __init__(self, name, surname):
        pass

my_person = Person("Brais", "Moure") # Almacena la clase en una variable
print(my_person) # Ahora se usa la clase
# print(my_person.name) # Causa error porque la funcion no hace nada

print()

'''
Podemos poner los parametros que necesitemos pero siempre hay que llamar a self
self se refiere a si mismo, y sirve para llamar a la clase
'''
class Person:
    def __init__(self, name, surname):
        '''
        self.name es una variable que se instancia para la clase a partir
        del operador self que esta en paramentro y aqui
        '''
        self.name = name # Los que haya en el parametro name lo introducces en self.name
        self.surname = surname
        self.nameeeeeeeeee = name
        self.surnameeeeeeeeee = surname
        self.full_name = f"{name} {surname}"

my_person = Person("Brais", "Moure")
print(my_person.name)
print(my_person.surname)
print(my_person.nameeeeeeeeee)
print(my_person.surnameeeeeeeeee)
print(my_person.full_name)

print()

# Podemos pasar los datos que queramos
my_person = Person(("Brais", "Daniel"), "Moure")
print(my_person.name)
print(my_person.surname)
print(my_person.nameeeeeeeeee)
print(my_person.surnameeeeeeeeee)

print()

class Person:
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}"

my_person = Person("Brais", "Moure")
# print(my_person.surname) # No funcionaria pues no existe self.surname
print(my_person.full_name)

print()

class Person:
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}"
    '''
    def walk(): # Esta funcion da error da error pues no tiene self
        print(f"{full_name} esta caminado")
        
    La forma correcta de acceder a atributos o variables de clase
    es primero poniendo self en el parametro, y segundo llamar a
    la varaible de clase tal que asi
    
    Es obligatorio poner self en todos los atributos
    ''' 
    def walk(self):
        print(f"{self.full_name} esta caminado")

my_person = Person("Brais", "Moure")
print(my_person.full_name)
my_string = my_person.full_name
print(my_string)
my_person.walk() # Las funciones que no son el contructuor se llaman asi

print()

class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})" # Parentesis no hace nada, es texto
    
    def walk(self):
        print(f"{self.full_name} esta caminado")
        
my_other_person = Person("Brais", "Moure")
print(my_other_person.full_name)
my_string = my_other_person.full_name
print(my_string)
my_person.walk()
        
my_other_person = Person("Brais", "Moure", "MoureDev")
print(my_other_person.full_name)
my_string = my_other_person.full_name
print(my_string)
my_person.walk()

print()
 
'''
Podemos modificar la variable ya instanciada

El operador __init__ no es inmutable, tienes permiso
para hacer los cambios dados para la el proyecto

El constructor es de tipado debil, puedes poner todos los tipos datos
'''
my_other_person.full_name = "Héctor de León (El loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 12
print(my_other_person.full_name)

print()

class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})" # Parentesis no hace nada, es texto
        self.__name = name # si pones un self en este formato lo haras private
        self.__surname = surname
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def walk(self):
        print(f"{self.full_name} esta caminado")
        
        
my_other_person = Person("Brais", "Moure")
print(my_other_person.full_name)
# print(my_other_person.__name) # No puedes acceder porque __name, esta con el modificador de privado
print(my_other_person.get_name())
my_other_person.set_name("Abraham")
print(my_other_person.get_name())
my_other_person.walk_2()

print()

class Person:
    def __init__(self) -> None: # Con esto declaramos que devuelva None
        pass