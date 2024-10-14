# Funciones

'''
Explicacion larga

    Las funciones tienen la finalidad de :

        Intentar encapsular una logica muy concreta dentro de una
        funcion, para intentar indicar la solucion de un problema
        que vamos a indicar a dicha funcion por medio de
        instrucciones, recuerda las intrucciones son las que dan
        solucion al problema no la funcion

        Evitar errores, pues el codigo que va a solucionar un
        problema muy concreto va estar en un solo lugar, entonces
        cuando queramos solucionar dicho problema solo tenemos que
        llamar a la funcion
        
        Evitar la redundancia de codigo, pues podremos reutilizarlo
        tantas veces como queramos llamando a dicha funcion
        
        Organizar las instrucciones del proyecto para que todo quede
        centralizado por algunas partes del proyecto

Explicacion corta

    Las funciones son trozos de codigo encapsulados que van a resolver
    un problema en concreto, que pueden reutilizarse todas las veces
    que queramos

'''

'''
Para crear una funcion

def <nombre_de_la_funcion>():

Ejemplo de funcion simple
'''
def my_function():
    print("Esto es una función")
    
my_function()

'''
Copiar el codigo directamente es ineficiente:
    
    Corres el riesgo de cometer errores durante la
    copia del codido
    
    El tiempo en que tardas para buscar el codigo
    lo podrias a ver utilizado para algo mejor
    
Mejor centralizalo en una funcion y llamalo tantas
veces como necesites
'''
my_function()
my_function()
my_function()

print()


# En una funcion podemos introduccir datos en argumentos o paramentros de entrada
#						Argumentos o paramentros de entrada
def sum_two_values(first_number, second_number):
    print(first_number + second_number)

'''
Las funciones que requieren de parametros,
al no pasarles nada te daran un error
'''
# sum_two_values()

sum_two_values(5, 7)
sum_two_values(54846, 74784)

'''
Para el caso de que pongamos un parametro
demas a los que requiere empezara a fallar
'''
# sum_two_values(54846, 74784, 1)

sum_two_values("5", "7") # Concatenara texto

print()

# Podemos indicar el tipo de dato del argumento que se debera de pasarle a la funcion
def sum_two_values_2(first_number: int, second_number: int):
    print(first_number + second_number)

'''
Aunque recuerda que no podemos obligar a una variable o parametro a
obtener un tipo de dato concreto
'''
sum_two_values_2(5, 7)
sum_two_values_2(54846, 74784)
sum_two_values_2("5", "7")
sum_two_values_2(1.4, 5.6)

print()

def sum_two_values_3(first_values: int, second_values):
    print(first_values + second_values)

sum_two_values_3(5, 7)
sum_two_values_3(54846, 74784)
sum_two_values_3("5", "7")
sum_two_values_3(1.4, 5.6)

print()

'''
Debemos siempre poner la declaracion de tipo para
indicar siempre al programador que tipo de dato
debe de introduccir
'''

def sum_two_values_4(first_values: int, second_values: int):
    print(first_values / second_values)

sum_two_values_4(5, 7)
sum_two_values_4(54846, 74784)
# sum_two_values_4("5", "7") # Este es el ejemplo de un problema en los lenguajes de tipado debil
sum_two_values_4(1.4, 5.6)

print()

'''
En una funcion podemos hacer que devuelva
algo mediante los parametros de salida

Para ello se utilizara return, lo que hace
este operador es devolver el resultado de
una funcion, o retornar la funcion sin devolver
nada, la finalidad de este ultimo es la de
parar la funcion
'''

def sum_two_values_with_return(first_values: int, second_values):
    return first_values + second_values

# Estos no muestran el resultado porque no tienen un print
sum_two_values_with_return(5, 7)
sum_two_values_with_return(54846, 74784)
sum_two_values_with_return("5", "7")
sum_two_values_with_return(1.4, 5.6)

# Pero estos si
print(sum_two_values_with_return(5, 7))
print(sum_two_values_with_return(54846, 74784))
print(sum_two_values_with_return("5", "7"))
print(sum_two_values_with_return(1.4, 5.6))

# Con esto podemos redirigir los datos como queramos
sum_two_values_with_return(5, 7)
sum_two_values_with_return(54846, 74784)
sum_two_values_with_return("5", "7")
sum_two_values_with_return(1.4, 5.6)

print()

# Ejemplo 1

my_result = sum_two_values_with_return(5, 7)
print(my_result)

# Ejemplo 2

print()
if sum_two_values_with_return(5, 7) == 12:
    print("Es 12")

print()

'''
Dato a tener en cuenta las funciones que no devuelven
nada podran ser utilizadas para propositos diferentes

No imprime my_result porque la funcion no devuelve
nada, esta funcion imprime no retorna, imprime el
resultado del print que tiene la funcion pero no
imprime el print que esta llamando a my_result
'''
my_result = sum_two_values(5, 7)
print(my_result) # Resulta en None

print()

def sum_two_values_with_return(first_values: int, second_values):
    my_sum = first_values + second_values
    return my_sum

print(sum_two_values_with_return(5, 7))

print()

'''
Podemos definir cual sera el orden de
los parametros de la siguiente manera
'''
def print_name(name, surname):
    print("Mi nombre es {} mis apellidos son {}".format(name, surname))

print_name(surname = "Moure", name = "Brais")

# Podemos pasar los datos que queramos
print_name(("Brais", "Daniel"), "Moure")

print()

'''
En las funciones de python podemos poner valores por defecto
un beneficio que puedes obtener a la hora de poner valores
por defecto, es que si no pones un valor en concreto para un
argumento, este utilizara el valor por defecto
'''
def print_name_with_default(name, surname, alias = "Sin alias"):
    print("Mi nombre es {} mis apellidos son {}, hallarme como {}".format(name, surname, alias))

print_name_with_default("Brais", "Moure", "MoureDev")
print_name_with_default("Brais", "Moure")
print()
print_name_with_default("Brais", "MoureDev")
# Recuerda que puede hacer un combinado de todo
print_name_with_default(surname = "Moure", name = "Brais")

print()

'''
Con * hacemos que el parametro se convierta en un args o
parametros arbitrarios, es decir un tipo de parametro
para meter x numero de datos
'''

def print_texts(*texts):
    print(texts)

print_texts("Hola", "Python", "MoureDev")
print_texts("Hola")

print()

def print_texts(*texts):
    for text in texts:
        print(text)

print_texts("Hola", "Python", "MoureDev")
print_texts("Hola")

print()

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "Python", "MoureDev")
print_upper_texts("Hola")

print()

def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "Python", "MoureDev")
print_upper_texts("Hola")

print()

# Se puede sobreescribir funciones

def print_texts(*texts):
    for text in texts:
        print(text.lower())

print_texts("Hola", "Python", "MoureDev")
print_texts("Hola")

def print_texts(*texts):
    for text in texts:
        print(len(text))

print_texts("Hola", "Python", "MoureDev")
print_texts("Hola")