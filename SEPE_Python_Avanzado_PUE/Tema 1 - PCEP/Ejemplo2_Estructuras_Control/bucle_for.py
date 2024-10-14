# creando una lista [] de nombres
nombres = ['Luis', 'Jorge', 'Maria', 'Laura', 'Pedro']
print(type(nombres))  # <class 'list'>

# por cada elemento que tengo en la lista nombres:
#   en este bloque lo mostramos por consola
for elemento in nombres :
    print(elemento, end=" ")
print("\n---------------- FIN --------------")

"""  rangos  """
# Mostrar los numeros del 0 al 9
for numero in range(10): # Rango va de 0 a numero-1
    print(numero)
print("---------------- FIN --------------")

# Mostrar los numeros del 1 al 10
for numero in range(1,11): # Rango va de 1 a numero-1
    print(numero)
print("---------------- FIN --------------")

# Mostrar los numeros de 0 a 10 de 2 en 2
for numero in range(0, 11, 2): # Rango va de 0 a numero-1
    print(numero)
print("---------------- FIN --------------")

# Mostrar los numeros desde -10 hasta -100 de 10 en 10
for numero in range(-10, -101, -10): # Rango va de -10 a numero-1
    print(numero)
print("---------------- FIN --------------")

# Mostrar los numeros desde 10 hasta el 1
for numero in range(10, 0, -1): # Rango va de 0 a numero-1
    print(numero)
print("---------------- FIN --------------")

# Las listas tienen una longitud que podemos obtener con la funcion len
print("Longitud de la lista de nombres", len(nombres))
#print(nombres[0])

for indice in range(len(nombres)) :
    print(nombres[indice])
print("---------------- FIN --------------")
    
# Mostrar los elementos de la lista empezando por el ultimo
for indice in range(len(nombres)-1, -1, -1) :
    print(nombres[indice])