# diccionarios: los elementos con clave:valor
# No tienen indices y se accede a los elementos a través de su clave
# A partir de 3.7 se garantiza el orden de entrada
# Las claves no se pueden repetir, se sobreescribe el valor
# Los valores si se pueden repetir
# se crean con {}

# Si repito clave, se sobreescribe el valor
alumnos = {'Juan': 6.4, "Maria": 8.3, 'Luis': 6.4, "Adolfo": 7.1, "Maria": 9.3}
print(alumnos)

# ver el tipo de dato
print(type(alumnos)) # <class 'dict'>

# Mostrar solo los nombres de los alumnos (claves)
print(alumnos.keys())  # dict_keys(['Juan', 'Maria', 'Luis', 'Adolfo'])

# Mostrar solo las notas de los alumnos (valores)
print(alumnos.values()) # dict_values([6.4, 9.3, 6.4, 7.1])

# Mostrar los elementos que tengo en el diccionario
# retorna una lista de tuplas
print(alumnos.items())  # dict_items([('Juan', 6.4), ('Maria', 9.3), ('Luis', 6.4), ('Adolfo', 7.1)])

# Operadores de pertenencia in y not in
print("Maria" in alumnos)
print("Paco" not in alumnos)

# Accedemos a los elementos por su clave al no tener indice
print("Nota de Luis:", alumnos['Luis'])   # Error si no lo encuentra KeyError: 'Luisss'
print("Nota de Luis:", alumnos.get('Luissss'))   # si no lo encuentra devuelve None

# Borrar un elemento
del alumnos['Adolfo']  # Error si no lo encuentra KeyError: 'Adolfoooo'
#alumnos.__delitem__('Adolfoooo') # Error si no lo encuentra KeyError: 'Adolfoooo'
print(alumnos)

# Agregar nuevo elementos
alumnos['Pepito'] = 3.5
print(alumnos)

# Modificar el valor de un elemento
alumnos['Pepito'] = 5
print(alumnos)

# Eliminar el ultimo elemento
alumnos.popitem()
print(alumnos)

# Eliminar un elemento por su clave y retorna su valor
#print(alumnos.pop('Pepito'))  # si no existe KeyError: 'Pepito'

# Otra forma de agregar elementos al diccionario
alumnos.update({'Pepito': 5})
print(alumnos)

# Ordenar el diccionario
print("Orden ascendente:", sorted(alumnos.values()))
print("Orden descendente:", sorted(alumnos, reverse=True))
print(alumnos)

# Recorrer un diccionario
for alum in alumnos: # solo me devuelve las claves
    print(alum, alumnos[alum])
    
for item in alumnos.items(): # cada item es una tupla (clave, valor)
    print(item)
    
for clave, valor in alumnos.items(): 
    print(clave, ":", valor)
    
# Otras formas de crear diccionarios
alumnos = dict()
alumnos = {}
alumnos = dict([('Juan', 6.4), ('Maria', 9.3), ('Luis', 6.4), ('Adolfo', 7.1)])
alumnos = dict(Juan=6.4, Maria=9.3, Luis=6.4, Adolfo=7.1)

# eliminar todos los elementos
alumnos.clear()
print(alumnos)