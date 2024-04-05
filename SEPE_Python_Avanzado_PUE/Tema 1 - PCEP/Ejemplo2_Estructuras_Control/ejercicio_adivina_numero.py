"""
    Generar un numero aleatorio del 0 al 10
    solicitar el numero al usuario hasta que lo adivine
    le vamos dando pistas: te has pasado, te has quedado corto
"""

import random

numero_random = random.randint(0,10)
numero = -1
while numero != numero_random :
    numero = int(input("Adivina numero: "))
    # dar pistas
    if numero > numero_random :
        print("Te has pasado, prueba un numero menor")
    elif numero < numero_random :
        print("Te has quedado corto, prueba con un numero mayor")
    #else :
    #    print("Acertaste")
    
#print("----- FIN del juego -----")
print("Acertaste")

