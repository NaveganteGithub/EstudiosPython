# Operadores Aritmaticos

print(3 + 4) # Suma
print(3 - 4) # Resta
print(3 * 4) # Multiplicacion
print(3 / 4) # Dividir
print()
print(10 / 3)
print(10 / 4)
print()
print(10 % 3) # Modulo - Resto
print(10 % 2)
print()
'''
Flor Division dividira un numero
y hara una operacion de truncar
para que quede entero
'''
print(10 // 3)
print(10 // 4)
print()

print(2 ** 3) # Exponente

print(2 ** 3 + 3 - 7 / 1 // 4) # Operaciones mas complejas
print()

print("Hola" + "Python") # Concatenado + no solo sirve para sumar
# print("Hola" - "Python") # Da error no puedes meter operaciones a la ligera
print("Hola" + "Python" + "¿Qúe tal?")

'''
No puedes concatenar diferentes tipos de
datos de esta manera, da error, + se utiliza
para sumas y concatenaciones, y Python ya se lia
'''
# print("Hola" + 5)

# Puedes utilizar esta alternativa para arreglarlo en algunas operaciones
print("Hola" + str(5))
# Puedes utilizar esta alternativa para arreglarlo en algunas operaciones
print("Hola", 5)
# Puedes utilizar esta alternativa para arreglarlo en algunas operaciones
print("Hola" + "5") # Aqui 5 seria un string y no int por eso es que no da eror
print()

# Concatenamos 5 veces la palabra Hola , no hace falta bucle
print("Hola " * 5)

'''
La cuestion no es utilizar las comillas dobles en vez de +
la cuestion es poder manejar un tipo de dato adecuado para
ciertas operaciones concretas
'''

# print("Hola " * 2 ** 3 + 3 - 7 / 1 // 4) # Dar error
# print("Hola " * (2 ** 3 + 3 - 7 / 1 // 4)) # Dar error, aunque lo agrupes
# Simplificar la instruccion puede ser de gran ayuda para solucionar el error
print("Hola " * (2 ** 3))
# print("Hola " * 2.5) # Dar error, no puedes multiplicarlo con decimales
# print("Hola " * 2.5 * 2) # Dar error, no puedes multiplicarlo con decimales
'''
Dar error, no puedes multiplicarlo con decimales,
aunque lo agrupes, pues da un dato float y esos
datos para operar en un operacion de multiplicado
de string, pues da error, solo lo puedes hacer
con enteros
''' 
# print("Hola " * (2.5 * 2))

'''
Produce un error porque el resultado que da la operacion
no es un entero, no es 5, sino un float 5.0, y no se puede
utiliza floats en una operacion para multiplicar el texto
'''
my_int = 2.5 * 2 
print("Hola " * int(my_int)) # Puedes transformar el float en entero

my_float = 2.5 * 2
print("Hola " * int(my_float)) # Puedes transformar el float en entero

'''
No da un resultado porque no tiene print

No hacemos nada con esta instruccion, pero no
da error por cuidado porque te puede pasar que
estes haciendo una operacion y no te des cuenta
de que estas haciendo una operacion que a la
final no vas a utilizar
'''
6 + 10

'''
Python se gano su popularidad por sus operaciones
'''

# Operadores Comparativos

print(3 > 4)
print(3 < 4)
print()
print(3 >= 4)
print(4 >= 4)
print()
print(3 <= 4)
print(4 <= 4)
print()
print(3 == 4)
print(4 == 4)
print()
print(3 != 4)
print(4 != 4)
print()
print(3 > 4 == 2) # Da False por la diferencia porque esta comparando False con 2
print()
print()
print()
print()
print()

'''
Ordenacion alfabetica por ASCII: aqui podemos comprobar
que los operadores de comparacion compruban si el texto
esta primero o no en la escala del alfabeto, por cierto
es sensitive case
'''
print("a" >= "a") # a y a son la misma letra o a va despues de la b en el alfabeto
print("a" >= "b") # a y b son la misma letra o a va despues de la b en el alfabeto
print()
print("a" <= "a") # a y a son la misma letra o a va antes de la b en el alfabeto
print("a" <= "b") # a y b son la misma letra o a va antes de la b en el alfabeto
print()
print("a" > "a") # a va despues de la a en el alfabeto
print("a" > "b") # a va despues de la b en el alfabeto
print()
print("a" < "a") # a va antes de la a en el alfabeto
print("a" < "b") # a va antes de la b en el alfabeto
print()
print("a" < "A") # Aqui el resultado seria FALSE
print("a" < "B") # Aqui el resultado seria FALSE
print()
print("aaaa" >= "aaaa")
print("aaaa" >= "abaa")
print()
print()
print()

print("Hola" > "Python")
print("Hola" < "Python")
print()
print("Hola" >= "Zola")
print("Hola" >= "Bola")
print("Hola" >= "Hola")
print("Hola" >= "Python")
print()
print("Hola" <= "Python")
print()
print("Hola" == "Python")
print()
print("Hola" != "Python")
print()
print()
print()

# Para comparar el numero de caracteres tenemos que utilizar len()
print(len("aaaa") >= len("abaa"))
print()
print()

# Operadores Lógicos

'''
and sirve para ver si dos o mas condicionales cumplen o no con la condicion
or sirve para ver si una condicional de toda la condicion cumple con dicha condicion
not sirve para invertir el resultado de una condicion lo que era TRUE se
volvera false y lo que era FALSE sera TRUE
'''

print(3 > 4 and "Hola" > "Python") # Equivalente a && en Python
print(3 > 4 or "Hola" > "Python") # Equivalente a || en Python
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or "Hola" > "Python" and 4 == 4)

'''
Si quisieras hacer que una operacion
tenga prioridad sobre otra operacion
tienes que agregarle mas (), este es
el operador de prioridad
'''
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(3 > 4)
print(not 3 > 4) # Equivalente a ! en Python
print(not (3 > 4))