import sys

'''
sys.argv[1] permite capturar el primer argumento pasado por el comando de python

Comando
    python name.py Ismael Montoro
Resultado
    hello, my name is, Ismael

para el caso de sys.argv[2]

Comando
    python name.py Ismael Montoro
Resultado
    hello, my name is, Montoro

'''
# print("hello, my name is,", sys.argv[1])

'''
sys.argv[0] recogera el nombre del fichero python puesto que es
el primer argumento del comando python
'''
# print("hello, my name is,", sys.argv[0])

'''
try:
    print("hello, my name is,", sys.argv[1])
except IndexError:
    print("Too few arguments")
'''

'''
No hace falta utilizar excepciones siempre, otra cosa que se
puede hacer para que el programa funcione es indicar al usuario
como tiene que realizar la operacion

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is,", sys.argv[1])
'''

'''
Si se quisiera manejar multiples valores se podria realizar lo siguiente

Comando
    python name.py "Ismael Montoro"
Resultado
    hello, my name is, Ismael Montoro

Aunque hay otras formas.
'''

'''
# sys.exit permite finalizar el programa
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is,", sys.argv[1])
'''

'''
Se puede utilizar sys.argv dentro de un for dado que
es un objeto de tipo lista que se puede iterar

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv:
    print("hello, my name is,", arg)
'''


if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# Slices
# [1:] significa que del objeto que estamos accediendo, sacaremos los valores desde la posicion 1 hasta el final
for arg in sys.argv[1:]:
    print("hello, my name is,", arg,)
print()

for arg in sys.argv[1:3]:
    print("hello, my name is,", arg)
print()

for arg in sys.argv[1:4]:
    print("hello, my name is,", arg)
print()

for arg in sys.argv[:3]:
    print("hello, my name is,", arg)
print()

'''
Aqui se esta declarando que la lista se acceda desde
la penultima posicion, hasta la posision 1 y luego
recorrar la lista desde la primera posicion hasta la
hasta la penultima, por cierto
'''
for arg in sys.argv[1:-1]:
    print("hello, my name is,", arg)
print()

'''
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

print("hello, my name is,", end=" ")
for arg in sys.argv:
    print(arg, end=" ")

print("")
'''