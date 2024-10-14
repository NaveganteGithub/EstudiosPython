import numpy as np

# El metodo array crea un array pasandole una lista

array_1D = np.array([1,2,3,4,5]) # Crea un array de una dimension o eje
print("Array de una dimension o Eje, se ha pedido el valor", array_1D[0])
print("Array de una dimension o Eje, se ha pedido el valor", array_1D[2])

array_2D = np.array([ [1,2,3,4,5],[6,7,8,9,10] ]) # Crea un array de dos dimensiones, llamada tambien tabla o matriz
print("Array de dos dimensiones o Tabla, se ha pedido el valor", array_2D[0, 4]) 
print("Array de dos dimensiones o Tabla, se ha pedido el valor", array_2D[0][4])
print("Array de dos dimensiones o Tabla, se ha pedido el valor", array_2D[1, 4])
print("Array de dos dimensiones o Tabla, se ha pedido el valor", array_2D[1][4])

array_3D = np.array([ 
                    [[1,2,3,4,5],[6,7,8,9,10]], 
                    [[45,46,47,48,49],[20,12,15,35,57]] 
                  ]) # Crea un array de tres dimensiones o cubo
print("Array de tres dimensiones o Cubo, se ha pedido el valor", array_3D[0, 1, 2])
print("Array de tres dimensiones o Cubo, se ha pedido el valor", array_3D[0][1][2])
print("Array de tres dimensiones o Cubo, se ha pedido el valor", array_3D[0, 0, 3])
print("Array de tres dimensiones o Cubo, se ha pedido el valor", array_3D[0][0][3])

# Crear una sublista mediante un array

print("Sublista 1D", array_1D[1:3])

print("Sublista 2D - 1", array_2D[0, 1:3])
print("Sublista 2D - 2", array_2D[1:3])
print("Sublista 2D - 3", array_2D[:, 1:3])

print("Sublista 3D - 1", array_3D[0, 0, 1:4])
print("Sublista 3D - 2", array_3D[:, :, 1:4])
print("Sublista 3D - 3", array_3D[:, 1:4])
print("Sublista 3D - 4", array_3D[1:4])
print("Sublista 3D - 4", array_3D[0, 1:4])

# empty creara un array vacio, con posiciones y tipos de datos definidos, por defecto los datos definidos seran de tipo float 

array_vacio = np.empty(1) # Una celda
print("Array vacio 1, una celda", array_vacio)

array_vacio = np.empty(5) # Un eje de 5 celdas
print("Array vacio 2", array_vacio)

array_vacio = np.empty((2, 5)) # Una tabla con dos filas y cinco columnas
print("Array vacio 3", array_vacio)

array_vacio = np.empty((7, 2, 4)) # Un cubo con siete filas, dos columnas, y cuatro posiciones de profundidad  
print("Array vacio 4", array_vacio)

array_vacio = np.empty((2, 5), dtype=int) # Una tabla con dos filas y cinco columnas, pero con datos int en vez de float
print("Array vacio 5", array_vacio)

array_vacio[0,1] = 2 # Asi se puede modificar datos de un array
print("Array vacio 5", array_vacio[0,1])

# zeros creara un array rellenado con ceros, funciona de manera similar a empty

array_ceros = np.zeros(7)
print("Array con ceros 1", array_ceros)

array_ceros = np.zeros(7, dtype=int)
print("Array con ceros 2", array_ceros)

array_ceros = np.zeros((7, 2), dtype=int)
print("Array con ceros 3", array_ceros)

# ones creara un array rellenado con unos, funciona de manera similar a empty

array_unos = np.ones(7)
print("Array con unos 1", array_unos)

array_unos = np.ones(7, dtype=int)
print("Array con unos 2", array_unos)

array_unos = np.ones((7, 2), dtype=int)
print("Array con unos 3", array_unos)

# full creara un array rellenado con los valores especificados en el segundo parametro, funciona de manera similar a empty

array_con_valor = np.full(7, 5)
print("Array con unos 1", array_con_valor)

array_con_valor = np.full((7), 5, dtype=int)
print("Array con unos 2", array_con_valor)

array_con_valor = np.full((7, 2), 5, dtype=int)
print("Array con unos 3", array_con_valor)

# Creara un array de dos dimensiones con el mismo numero de celdas y columnas

array_2D_inicio = np.identity(5)
print("Tabla creada desde el inicio", array_2D_inicio)

# Creara un array con un rango de valores, y opcionalmente se puede especificar el salto entre valor y valor

rango_array = np.arange(5,10)
print("Rango de valores en array", rango_array)

rango_array = np.arange(7,49, 7)
print("Rango de valores en array con salto de 7", rango_array)

rango_array = np.arange(7,49, 5)
print("Rango de valores en array con salto de 5", rango_array)

rango_array = np.arange(7,49, 5, dtype=int)
print("Rango de valores enteros en array con salto de 5", rango_array)


""" 
linspace creara un array con un rango de valores que tienen una distancia o un margen unos de 
otros exactamente igual o equisdistantes, y opcionalmente se puede especificar el salto entre 
valor y valor
"""
rango_array = np.linspace(5,10)
print("Rango de valores en array", rango_array)

rango_array = np.linspace(7,49, 7)
print("Rango de valores en array con salto de 7", rango_array)

rango_array = np.linspace(7,49, 5)
print("Rango de valores en array con salto de 5", rango_array)

rango_array = np.linspace(7,49, 5, dtype=int)
print("Rango de valores enteros en array con salto de 5", rango_array)

# random.random creara un array con valores aleatorios

rango_aleatorio_array = np.random.random(7)
print("Array con un rango de valores aleatorios", rango_aleatorio_array)

# ndim especifica el numero de dimensiones que tiene un array

def calcular_dimensiones(resultado=1):
    match resultado:
        case 1:
            return "Array de una dimension o Eje"
        case 2:
            return "Array de dos dimensiones o Tabla"
        case 3:
            return "Array de tres dimensiones o Cubo"

print("El Array de rango_aleatorio_array es un", 
      calcular_dimensiones(
          np.ndim(rango_aleatorio_array)
          )
        )
print("El Array de array_1D es un", 
      calcular_dimensiones(
          np.ndim(array_1D)
          )
      )
print("El Array de array_2D es un", 
      calcular_dimensiones(
          np.ndim(array_2D)
          )
        )
print("El Array de array_3D es un", 
      calcular_dimensiones(
          np.ndim(array_3D)
          )
        )

# size especifica el numero de posiciones que tiene un array

print("Este array tiene", np.size(array_1D), "posiciones.")
print("Este array tiene", np.size(array_2D), "posiciones.")
print("Este array tiene", np.size(array_3D), "posiciones.")

# shape devuelve el numero de filas, columnas y profundidad

tupla = np.shape(array_1D) # Solo devuelve el numero de filas
print("Index devuelto", tupla)

tupla = np.shape(array_2D) # Devuelve el numero de filas y columnas
print("Index devuelto", tupla)

tupla = np.shape(array_3D) # Devuelve el numero de filas, columnas y profundidad
print("Index devuelto", tupla)

# Puedes crear el array de los tipos de datos que tu quieras

varios_tipos_datos = np.array(["dasdads", 54656, 156151.53, True])
print(varios_tipos_datos)
# varios_tipos_datos = np.array(["dasdads", 54656, 156151.53, True, [1564564, "dasdasd"]]) # exceptuando listas anidadas y otros tipos de datos
