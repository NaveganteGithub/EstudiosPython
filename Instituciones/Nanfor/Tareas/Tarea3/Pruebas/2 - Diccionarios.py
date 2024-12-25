diccionario = {'nombre': 'Ismael', 'apellidos': 'Montoro Peñasco'}
print(diccionario)
diccionario = dict([['nombre', 'Ismael'], ['apellidos', 'Montoro Peñasco']])
print(diccionario)

# Pedir datos
print(diccionario['nombre'])
print(diccionario.get('nombre'))
print(diccionario.get(2))

# Agregar datos
print(diccionario)
diccionario['edad'] = 22
print(diccionario)
diccionario.update({'codigo': 5641516})
print(diccionario)

# Modificar datos
diccionario['edad'] = 23
print(diccionario)
diccionario.update({'edad': 22})
print(diccionario)

# Mostrar datos del diccionario
print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())

for i in diccionario.keys():
    print(i)

for i in diccionario.values():
    print(i)

for i in diccionario.items():
    print(i)

# Valor existente
print('edad' in diccionario)
print('correo' in diccionario)

# Eliminar datos
print(diccionario)

valor_eliminado = diccionario.pop('correo', 514564154156)
print(valor_eliminado)

valor_eliminado = diccionario.pop('edad', 514564154156) # Elimina un clave-valor del diccionario indicandolo, sino existe devolvera el valor del 2- parametro 
print(valor_eliminado) # ademas devuelve el valor eliminado
print(diccionario)

valor_eliminado = diccionario.popitem() # Elimina el ultimo clave-valor del diccionario
print(valor_eliminado) # ademas devuelve el valor eliminado
print(diccionario)

del diccionario['apellidos'] # Elimina un clave-valor del diccionario indicandolo
print(diccionario)

diccionario.clear() # Elimina todo el diccionario