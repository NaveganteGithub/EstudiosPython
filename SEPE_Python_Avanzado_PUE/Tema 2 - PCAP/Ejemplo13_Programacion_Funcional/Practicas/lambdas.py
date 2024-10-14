alumnos = dict(Luis=9.9, Maria=6.3, Adolfo=3.8, Pedro=10)

'''def sumar_punto(item: dict):
    if item[1] >= 9:
        nota = 10
    else:
        nota = item[1] + 1
    return item[0], nota'''

notas = dict(map(lambda item: (item[0], 10) if item[1] >= 9 else (item[0], item[1] + 1), alumnos.items()))
print(notas)

############################

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "{}, {}".format(self.nombre, self.edad)

personas = [Persona('Luis', 15), Persona('Maria', 23), Persona('Adolfo', 12), Persona('Pedro', 25)]

'''
def tratar_personas(person: Persona): # Cuando tratamos con objetos tenemos que hacerlo atraves del parametro
    # Retornar el objeto sin sobreescribir.
    # return Persona(str(person.nombre).upper(), int(person.edad) + 1)
    # Retornar el objeto sobreescribiendo.
    person.nombre = person.nombre.upper()
    person.edad += 1
    return person
'''

persona_1 = dict(map(lambda person: (person.nombre.upper(), person.edad + 1), personas))
persona_2 = list(map(lambda person: Persona(str(person.nombre).upper(), int(person.edad) + 1), personas))
print(persona_1, persona_2, sep="\n")




palabra = "abracadabra"

'''def mayusculas(letra):
    if letra == "a":
        return "A"
    else:
        return letra'''

palabra_may_1 = list(map(lambda letra: "A" if letra == "a" else letra, palabra))
palabra_may_2 = list(map(lambda letra: (letra,'A')[letra == 'a'], "abracadabra"))
print("".join(palabra_may_1))


alumnos = dict(Luis=9.9, Maria=6.3, Adolfo=3.8, Pedro=10)

'''def aprobados(alumno):
    return alumno[1] >= 5'''

aprobados = list(filter(lambda alumno: alumno[1] >= 5, alumnos.items()))
print(aprobados)

##############################


class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "{}, {}".format(self.nombre, self.edad)

personas = [Persona('Luis', 15), Persona('Maria', 23), Persona('Adolfo', 12),
            Persona('Pedro', 25)]

'''def mayores(persona: Persona):
    return persona.edad > 17'''

mayores_edad = list(filter(lambda persona: persona.edad > 17, personas))
for me in mayores_edad:
    print(me)


#############################

palabra = "ayuntamiento"

def consonantes(palabra: str):
    return palabra not in ['a', 'e', 'i', 'o', 'u']

cons = list(filter(lambda palabra: palabra not in ['a', 'e', 'i', 'o', 'u'], palabra))
print(cons)


##########################


from functools import reduce

numeros = list(range(1,101))

# Una funcion con reduce en la primera tanda recibe
# los dos valores del principio, y luego se ira
# pasando de uno es uno
'''def sumar(acumulador, num):
    print(acumulador, num)
    return acumulador + num'''

result = reduce(lambda acumulador, num: acumulador + num, numeros)
print(result)

##########################

nombres = ['Luis', 'Maria', 'Adolfo', 'Pedro']

'''def nombs_mayus(cadena, nombre: str):
    return cadena.upper() + " - " + nombre.upper()'''

cadena = reduce(lambda cadena, nombre: cadena.upper() + " - " + nombre.upper(), nombres)
print(cadena)

##########################

print((lambda x : x * x)(5))
print((lambda x, y : x * y)(5, 10))