# Sintaxis:    lambda parametros: cuerpo de la funcion

'''*************** map **************'''
# Ejemplo 1
numerosDobles = list(map(lambda numero: numero * 2, [1,2,3,4,5]))
print(numerosDobles)

# Ejemplo 2
alumnos = dict(Luis=8.9, Maria=6.3, Adolfo=3.8, Pedro=10)
nuevas_notas = dict(map(lambda item: (item[0], 10 if item[1] >= 9 else item[1] + 1), alumnos.items()))
#Hay otro formato de if comprimido: (valor_False,valor_True)[condición]
nuevas_notas = dict(map(lambda item: (item[0], (item[1] + 1, 10)[item[1] >= 9]), alumnos.items()))
print(nuevas_notas)

# Ejemplo 3
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre}, {self.edad}"

personas = [Persona("Juan", 27), Persona("Maria", 35), Persona("Pedro", 22)]
personas = list(map(lambda persona : Persona(persona.nombre.upper(), persona.edad + 1), personas))
for p in personas:
    print(p)

# Ejemplo 4
''' retornar la palabra abracadabra donde la letra a sea mayuscula '''
def mayusculas(letra):
    if letra == 'a':
        return 'A'
    else:
        return letra

palabra = "".join(map(lambda letra: 'A' if letra == 'a' else letra , "abracadabra"))
# (valor_False, valor_True)[condicion]
palabra2 = "".join(map(lambda letra: (letra,'A')[letra == 'a'], "abracadabra"))
print(palabra)
print(palabra2)

'''*************** filter **************'''
# Ejemplo 1
numeros = list(filter(lambda num: num % 2 == 0, [1,2,3,4,5,6,7,8,9]))
print(numeros)

# Ejemplo 2
''' Dado un diccionario con los nombres y notas de cada alumno, filtrar para quedarnos solo con los aprobados '''
alumnos = dict(Luis=3.9, Maria=6.3, Adolfo=3.8, Pedro=10)
alumnos_aprobados = dict(filter(lambda item: item[1] >= 5, alumnos.items()))
print(alumnos_aprobados)

# Ejemplo 3
''' partiendo de una lista de instancias de Persona, filtar para quedarnos solo con los mayores de edad'''
personas = [Persona("Juan", 7), Persona("Maria", 35), Persona("Pedro", 12)]
personas = list(filter(lambda persona: persona.edad >= 18, personas))
for p in personas:
    print(p)

# Ejemplo 4
''' Con la palabra ayuntamiento devolver solo las consonantes '''
palabra = "".join(list(filter(lambda letra: letra not in "aeiou", "ayuntamiento")))
print(palabra)


'''*************** reduce **************'''
from functools import reduce

# Ejemplo 1
print("Suma:", reduce(lambda acum, num: acum + num, [3,8,2,1,7]))

# Ejemplo 2
print(reduce(lambda acum, nombre: acum.upper() + " - " + nombre.upper(), ["Luis", "Maria", "Juan"]))
