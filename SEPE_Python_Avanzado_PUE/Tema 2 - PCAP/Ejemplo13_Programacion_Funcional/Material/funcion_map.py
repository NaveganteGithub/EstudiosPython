# la funcion map se aplica sobre un elemento iterable (coleccion y strings)
# a cada elemento le aplicamos una funcion y el resultado sera el nuevo elemento modificado
# sintaxis:    map(funcion, iterable)

# Ejemplo 1
numeros = [1,2,3,4,5]

def duplicar(numero):
    return numero * 2

numerosDobles = list(map(duplicar, numeros))
print(type(numerosDobles))
print(numerosDobles)

# Ejemplo 2
alumnos = dict(Luis=8.9, Maria=6.3, Adolfo=3.8, Pedro=10)

def sumar_punto(item):
    if item[1] >= 9:
        nota = 10
    else:
        nota = item[1] + 1
    return item[0], nota

nuevas_notas = dict(map(sumar_punto, alumnos.items()))
print(nuevas_notas)

# Ejemplo 3
''' 
    Crear la clase Persona con nombre y edad y sobreescribir __str__
    Crear una lista de personas
    Crear una funcion que reciba el objeto de Persona y retorne el nombre en mayusculas y edad + 1
    crear una lista con la funcion map
'''
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre}, {self.edad}"

personas = [Persona("Juan", 27), Persona("Maria", 35), Persona("Pedro", 22)]

def modificar_persona(persona):
    # Asi estoy creando un nuevo objeto
    #return Persona(persona.nombre.upper(), persona.edad + 1)

    # Modificar el objeto existente
    persona.nombre = persona.nombre.upper()
    persona.edad += 1
    return persona

# si quiero modificar la lista original
personas = list(map(modificar_persona, personas))
print(personas) # [<__main__.Persona object at 0x10de63dc0>, <__main__.Persona object at 0x10de63d90>, <__main__.Persona object at 0x10de63d30>]
for p in personas:
    print(p)

# Ejemplo 4
''' retornar la palabra abracadabra donde la letra a sea mayuscula '''
def mayusculas(letra):
    if letra == 'a':
        return 'A'
    else:
        return letra

palabra = "".join(list(map(mayusculas, "abracadabra")))
print(palabra)