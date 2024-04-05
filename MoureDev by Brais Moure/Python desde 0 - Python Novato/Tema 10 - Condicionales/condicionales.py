# Condicionales

'''
Las estructuras condicionales son estructuras de control
que nos permite determinar si se ejecuta cierto codigo o
no
'''

my_condition = True

if my_condition: # Para ejecutar una operacion del if tiene que ser True
    print("Se ejecuta la condicion del if")
    
print("La ejecucion continúa")

print()

my_condition = False

if my_condition:
    print("Se ejecuta la condicion del if") # Este print no se imprime pues la condicion da False
    
print("La ejecucion continúa")

print()

my_condition = True

if my_condition == True: # Esto seria redundante lo mejor es poner directamente my_condition
    print("Se ejecuta la condicion del if")
    
print("La ejecucion continúa")

print()

'''
Podemos realizar condicionales comprobando si una variable
tiene algo o no, para el caso de que la variable no este
vacia no se ejecutara, pero si tiene la variable esta se
ejecutara

Esto como no da ni True ni False lo que hara es comprobar
si existe un valor y si lo hay pues tira hacia adelante
'''
my_condition = 5 * 2

if my_condition: 
    print("Se ejecuta la condicion del segundo if")
    
print("La ejecucion continúa")

print()

'''
En caso de no a ver nada en la variable no ejecutara el
codigo

None sirve para vaciar una variable, tambien sirve para indicar
que no hay nada, pues como el null de Java
https://stackoverflow.com/questions/3289601/null-object-in-python
'''
my_condition = None

if my_condition: 
    print("Se ejecuta la condicion del segundo if")
    
print("La ejecucion continúa")

print()

'''
Daria False puesto que ahora se analizaria el numero para
ver si el resultado de la comprobación es igual o no,
ahora no solo se esta comprobando si hay un valor o no
'''
my_condition = 5 * 2

if my_condition == 11: # Da False
    print("Se ejecuta la condicion del segundo if")
    
print("La ejecucion continúa")

print()

if my_condition == 10: # Da True
    print("Se ejecuta la condicion del segundo if")
    
print("La ejecucion continúa")

print()

if my_condition >= 10: # Da True
    print("Se ejecuta la condicion del segundo if")
    
print("La ejecucion continúa")

print()

if my_condition > 10: # Da False
    print("Se ejecuta la condicion del segundo if")
    
print("La ejecucion continúa")

print()

my_condition = 5 * 2

if my_condition > 10:
    print("Es mayor de 10")
else: # Con else es una parte de la estructura de if que se ejecutara en caso de que las demas condiciones no den True
    print("Es menor o igual que 10")
    
print("La ejecución continúa")

print()

my_condition = 5 * 5

if my_condition > 10 and my_condition < 20: # and es como el operador && de java sirve para ver si dos o mas condicionales dan True
    print("Es mayor de 10 y menor que 20")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")
    
print("La ejecución continúa")

print()

my_condition = 5 * 3

if my_condition > 10 and my_condition < 20:
    print("Es mayor de 10 y menor que 20")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")
    
print("La ejecución continúa")

print()

'''
No importa cuantos saltos de linea metas para crear
tus instrucciones, da igual cuantos saltos de linea
con espacios en blanco dejes, mientras dejes una
tabulacion que indique que esa instruccion pertenece
al if o al else if o else, podras meter todas las
instrucciones que necesites para tu condicional
'''

if my_condition > 10 and my_condition < 20:
    print("Es mayor de 10 y menor que 20")
    print("Es mayor de 10 y menor que 20")
    print("Es mayor de 10 y menor que 20")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")
    
    
    
    print("Es menor o igual que 10 o mayor o igual que 20")
    
print("La ejecución continúa")

print()

my_condition = 5 * 5

if my_condition > 10 and my_condition < 20:
    print("Es mayor de 10 y menor que 20")
    print("Es mayor de 10 y menor que 20")
    print("Es mayor de 10 y menor que 20")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")
    
    
    
    print("Es menor o igual que 10 o mayor o igual que 20")
    
    
print()

my_condition = 1

if my_condition == 10:
    print("Es mayor de 10 y menor que 20")
    print("Es mayor de 10 y menor que 20")
    print("Es mayor de 10 y menor que 20")
elif my_condition > 10 and my_condition < 20:
    print("Es mayor de 10 y menor que 20")
elif my_condition == 1: # else if para java pero elif para python
    print("Es igual a 1")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")
    
    
    
    print("Es menor o igual que 10 o mayor o igual que 20")
    
'''
Ten cuidado con las tabulaciones en python pues el scope, interpretara
que cierta instruccion pertenece ha cierta estructura
'''

'''
Ten cuidado cuando empieces a definir el if y los else if, pues
si quieres que algunas condicionales se ejecuten a parte, debes
de iniciar otro if colocar las condicionales en ese otro if
'''
my_condition = 1

if my_condition == 10:
    print("Es mayor de 10 y menor que 20")
    print("Es mayor de 10 y menor que 20")
    print("Es mayor de 10 y menor que 20")

if my_condition > 10 and my_condition < 20:
    print("Es mayor de 10 y menor que 20")
elif my_condition == 1: # else if para java pero elif para python
    print("Es igual a 1")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")
    
    
    
    print("Es menor o igual que 10 o mayor o igual que 20")
        
print()

my_condition = 1

if my_condition == 10:
    print("Es mayor de 10 y menor que 20")
    print("Es mayor de 10 y menor que 20")
    print("Es mayor de 10 y menor que 20")
    '''
    Entraria dentro del if de == 10 aunque le pongas saltos de 10,
    si quieres hacer que esta condicion se ejecute a parte tienes
    que hacer como en el anterior caso
    
    Recuerda que los comentarios influiran en la ejecucion de tu codigo
    en un sentido de interrupcion en el flujo de tu codigo o en un
    sentido de errores, asi que, si un comentario te esta dando
    problemas nivela la tabulacion
    '''



elif my_condition > 10 and my_condition < 20:
    print("Es mayor de 10 y menor que 20")
elif my_condition == 1:
    print("Es igual a 1")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")
    
    
    
    print("Es menor o igual que 10 o mayor o igual que 20")
    
print()

my_condition = 1

if my_condition == 10:
    print("Es mayor de 10 y menor que 20")
    print("Es mayor de 10 y menor que 20")
    print("Es mayor de 10 y menor que 20")

if my_condition > 10 and my_condition < 20:
    print("Es mayor de 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 1")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")
    
    
    
    print("Es menor o igual que 10 o mayor o igual que 20")

'''
Quitar la tabulacion por completo en una linea despues del
if o else o else if termina con la condicional
'''
print()

'''
Las variables que no tienen un string como
tal, mas bien tienen una cadena vacia, python
lo interpretara como una variable varible
vacia
'''
my_string = ""

if my_string:
    print("Mi cadena de texto no esta vacía")
    
my_string = "Mi cadena de texto"

if my_string:
    print("Mi cadena de texto no esta vacía")

if my_string == "Mi cadena de textooooooo":
    print("Estas cadenas de texto coinciden")

print()

my_string = ""

if not my_string: # Sirve para negar el resultado booleano
    print("Mi cadena de texto esta vacía")