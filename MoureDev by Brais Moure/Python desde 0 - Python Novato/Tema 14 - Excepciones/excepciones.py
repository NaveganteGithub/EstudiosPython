# Excepciones

'''
Los errores son que nuestro programa ya sea
por alguna razón u otra deja de funcionar

Hay varios tipos de errores
    
    Errores sintaticos: escribes mal una funcion
    
    Errores de logica: errores cometidos a la hora
    de programar tu codigo
    
    Excepciones que son errores en tiempo de ejecucion
    que el usuario haga algo mal que obligue al programa
    a finalizar
    
Podemos tratar con excepciones para prevenirnos para
las eventualidades de nuestro programa, mediante las
estructras de control de errores
'''

'''
No podemos sumar un texto con un numero ni concatenarlo,
ni con el tipado debil (o dinamico )


print(5 + "5")
'''

numberOne, numberTwo = 7, 7
numberTwo = "1"

'''
print(numberOne + numberTwo)
'''

# Como programa falle el if no te puede ayudar
'''
if numberOne > 3:
    print(numberOne + numberTwo)
else:
    print("No se cumplio")
'''
    
'''
Puedes hacer el type, para los casos que tengas
conocimiento de que tipo de dato quieres que
entre en el if, pero hay cirtas circuntancias
que no te permitiran utilizarlo porque realmente
no tendras conocimiento sobre lo que realmente
tendras que evitar, o por una operacion del usuario
que no hayas controlado, por desconocimiento sobre
el uso qe le da el usuario al software

if type(numberTwo) == int:
    print(numberOne + numberTwo)
else:
    print("No se cumplio")

'''

'''
Con la estructura try podemos controlar los fallos
que se puedan dar
'''

try:
    print(numberOne + numberTwo)
    print("No se a produccido un error")
except: # En caso de que try falle saltara este codigo
    print("Se a producido un error")
    
print()

try:
    print(numberOne + numberTwo)
    print("No se a produccido un error")
except: # En caso de que try falle saltara este codigo
    print("Se a producido un error")
else: # En caso de que se cumpla correctamente el try se ejecutara el else
    print("La ejecucion continua correctamente")

print()

try:
    print(numberOne + numberTwo)
    print("No se a produccido un error")
except: # En caso de que try falle saltara este codigo
    print("Se a producido un error")
else: # En caso de que se cumpla correctamente el try se ejecutara el else, opcional
    print("La ejecucion continua correctamente")
finally: # finally se ejecutara siempre, opcional
    print("La ejecucion continua")
    
print()

try:
    print(numberOne + numberTwo)
    print("No se a produccido un error")
except: # En caso de que try falle saltara este codigo
    print("Se a producido un error")
finally: # finally se ejecutara siempre, opcional
    print("La ejecucion continua")
    
print()

'''
Captura de excepciones por tipo

Se puede especificar el tipo de error para cada excepcion

Si se produce un error que este especificado en exception
saltara, el try except no puede manejar otros errores, un
momento a otro provocaran un error que no sea el controlado
entonces el try except fallara
'''
try:
    print(numberOne + numberTwo)
    print("No se a produccido un error")
except TypeError:
    print("Se a producido un error")
    
print()
'''
Podemos espeficar varios tipos de errores para controlar
lo que pasa dentro del codigo
'''
try:
    print(numberOne + numberTwo)
    print("No se a produccido un error")
except ValueError:
    print("Se a producido un ValueError")
except TypeError:
    print("Se a producido un TypeError")
    
print()

# Captura de la informacion de la excepcion
try:
    print(numberOne + numberTwo)
    print("No se a produccido un error")
except ValueError as e:
    print("Se a producido un ValueError")
    print(e)
except TypeError as a:
    print("Se a producido un TypeError")
    print(a)

print()

'''
No se trata de rellenarlo todo con try except
se trata de controlar los errores del software

La utilidad que tiene esto es la de evitar errores
dentro proyectos grandes
'''

'''
En este caso parece que se esta controlando pero no es asi,
dado que el try produce un TypeError, pero no hay un except
TypeError, y para darle control a ello tenemos la excepcion
generica, o la excepcion padre que es para controlar todas
las excepciones
'''

try:
    print(numberOne + numberTwo)
    print("No se a produccido un error")
except ValueError as e:
    print("Se a producido un ValueError")
    print(e)
except Exception as aq: # Exception conocida como la excepcion generica
    print("Se a producido un TypeError")
    print(aq)

print()