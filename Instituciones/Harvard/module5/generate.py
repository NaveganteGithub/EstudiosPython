# Librerias : conjunto de modulos que se pueden reutizar en nuestros programas
# Modulo : es un fichero python con funciones que se puede importar a un proyecto
# import es una palabra clave de python que permite importar toda una libreria
import random
'''
coin = random.choice(["heads", "tails"])
print(coin)
'''

'''
from es una palabra clave de python que permite importar una funcion de una libreria
esto es debido a que antiguamente como importaras dos librerias que conteniesen la
misma funcion podria llegar a generar un problema de colision

from random import choice

coin = choice(["heads", "tails"]) # Choice es una funcion que te devuelve un dato de la lista
print(coin)
'''

'''
number = random.randint(1,10) # randint genera numeros aleatorios
print(number)
'''

cards = ["jack", "queen", "king"]
random.shuffle(cards) # Desordena valores de una lista
for card in cards:
    print(card)
