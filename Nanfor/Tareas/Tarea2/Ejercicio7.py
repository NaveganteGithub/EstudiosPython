import pandas as pd # Primero importamos la libreria pandas

# Tercero se declara la funcion con su parametro
def ordenar_notas(notas_recopiladas):
    ''' 
    Quinto se programa la funcion para que empiece 
    a ordenar los valores del diccionario
    '''
    ordenacion = pd.Series(notas_recopiladas) # Se crea la Serie con el diccionario pasado por parametro
    return ordenacion[ordenacion >= 5].sort_values(ascending=False) # y se retornara todos los valores superiores a 5 y con short_values se ordenaran los valores 

# Segundo se creara el diccionario con los datos
notas_curso = {"Juan Manuel Castilla Fernandez": 9,
         "Alonso Diaz Martinez": 8,
         "Lucia Palomares": 7,
         "Daniel Serrano": 3,
         "Andrea Reviejo": 2,
         "Sofia Castilla Sanchez": 10,
         "Ismael Alba Castellon": 7,
         "Nerea Rosales": 6
         }

notas_ordenadas = ordenar_notas(notas_curso) # Cuarto se llama a la funcion y se guardara el resultado en una variable
print(notas_ordenadas)