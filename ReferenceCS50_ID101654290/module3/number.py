# Logical Error - Value Error

'''
Una buena practica que se suele hacer en las excepciones es que no
se introduzcan lineas demas dentro del bloque try solo una linea y
concretamente tiene que ser la linea que pueda dar la excepcion, o
si son varias lineas solo tienes que poner las lineas que tienen
el problema de que puede dar error.
'''
try: # Aqui probara el codigo en cuestion
    x = int(input("What´s x? "))
    '''
    ValueError es una excepcion que indica que a habido un error
    al tratar con valores en este caso ha habido un problema al
    tratar de convertir una cadena de texto introducida por
    alguien en un numero
    '''
except ValueError: # En caso de que algo salga mal ejecuta este codigo
    print("x is not an integer")
else: # En caso de que try no encuentre excepcion que else ejecute el codigo de dentro y asi se soluciona el problema con las variables
    print(f"x is {x}")
    '''
    NameError es una excepcion que indica que a habido un error
    al intentar acceder a una variable, ejemplo la x de este print

    Cuidado con las lineas que mueves, posiblemente necesiten de alguna excepcion
    '''
