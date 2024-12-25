
conjunto_1 = {1,2,3,4,5,6,7,8,9,10}
conjunto_2 = {7,8,9,10,11,12,13,14}

operacion_1 = conjunto_1 | conjunto_2 # Union - Une los dos conjuntos
print(operacion_1)

operacion_2 = conjunto_1 & conjunto_2 # Interseccion - El resultado es un conjunto con los valores comunes de los dos conjuntos
print(operacion_2)

operacion_3 = conjunto_1 - conjunto_2 # Diferencia - El resultado es un conjunto con los valores que no tengan en comun los dos conjuntos
print(operacion_3)