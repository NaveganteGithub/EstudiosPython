
num = list(range(1, 101))

def pares(nums):
    return nums % 2 == 0

num_pares = list(filter(pares, num))
print(num_pares)


###############

alumnos = dict(Luis=9.9, Maria=6.3, Adolfo=3.8, Pedro=10)

def aprobados(alumno):
    return alumno[1] >= 5

alumns = dict(filter(aprobados, alumnos.items()))
print(alumns)


###############

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "{}, {}".format(self.nombre, self.edad)

personas = [Persona('Luis', 15), Persona('Maria', 23), Persona('Adolfo', 12),
            Persona('Pedro', 25)]

def mayores(persona: Persona):
    return persona.edad > 17

mayores_edad = list(filter(mayores, personas))
for me in mayores_edad:
    print(me)


###############

palabra = "ayuntamiento"

def consonantes(palabra: str):
    return palabra not in ['a', 'e', 'i', 'o', 'u']

cons = list(filter(consonantes, palabra))
print(cons)