alumnos = dict(Luis=9.9, Maria=6.3, Adolfo=3.8, Pedro=10)

def sumar_punto(item: dict):
    if item[1] >= 9:
        nota = 10
    else:
        nota = item[1] + 1
    return item[0], nota


nuevas_notas = map(sumar_punto, alumnos.items())
print(dict(nuevas_notas).keys())

'''
Crear la clase Persona con nombre, edad, y str sobreescrito
Crear una lista de personas
Crear una funcion que reciba el objeto de Persona y retorne el nombre en mayusculas, y la edad + 1
Crear una lista con la funcion map
'''

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "{}, {}".format(self.nombre, self.edad)

personas = [Persona('Luis', 15), Persona('Maria', 23), Persona('Adolfo', 12), Persona('Pedro', 25)]

def tratar_personas(person: Persona): # Cuando tratamos con objetos tenemos que hacerlo atraves del parametro
    # Retornar el objeto sin sobreescribir.
    # return Persona(str(person.nombre).upper(), int(person.edad) + 1)
    # Retornar el objeto sobreescribiendo.
    person.nombre = person.nombre.upper()
    person.edad += 1
    return person

persona = list(map(tratar_personas, personas))

for p in persona:
    print(p)


#######################

palabra = "abracadabra"

def mayusculas(letra):
    if letra == "a":
        return "A"
    else:
        return letra

palabra_may = list(map(mayusculas, palabra))
print("".join(palabra_may))