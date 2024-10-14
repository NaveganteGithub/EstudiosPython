# la funcion filter se aplica sobre un elemento iterable
# filtramos los elementos en base a una funcion que retorna:
#     - True: nos quedamos con el elemento, pasa el filtro
#     - False: Lo descartamos
# Sintaxis:   filter(funcion, iterable)

# Ejemplo 1
''' Dada una lista de numeros y una funcion quedarnos solo con los pares '''
numeros = [1,2,3,4,5,6,7,8,9]

'''
def pares(num):
    if num % 2 == 0:
        return True
    else:
        return False
'''
def pares(num):
    return num % 2 == 0

numeros = list(filter(pares, numeros))
print(numeros)


# Ejemplo 2
''' Dado un diccionario con los nombres y notas de cada alumno, filtrar para quedarnos solo con los aprobados '''
alumnos = dict(Luis=3.9, Maria=6.3, Adolfo=3.8, Pedro=10)

def aprobados(item):
    return item[1] >= 5

alumnos_aprobados = dict(filter(aprobados, alumnos.items()))
print(alumnos_aprobados)

# Ejemplo 3
''' partiendo de una lista de instancias de Persona, filtar para quedarnos solo con los mayores de edad'''
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre}, {self.edad}"

personas = [Persona("Juan", 7), Persona("Maria", 35), Persona("Pedro", 12)]

def mayores(persona):
    return persona.edad >= 18

personas = list(filter(mayores, personas))
print(personas)   # [<__main__.Persona object at 0x1056c34f0>]
for p in personas:
    print(p)

# Ejemplo 4
''' Con la palabra ayuntamiento devolver solo las consonantes '''
def consonantes(letra):
    return letra not in "aeiou"

palabra= "".join(list(filter(consonantes, "ayuntamiento")))
print(palabra)