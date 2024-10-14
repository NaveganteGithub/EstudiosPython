# Variables

myVariable = "My String variable" # Esta variable no esta bien para las practicas de python
print(myVariable)

'''
Esta variable esta bien escrita porque sigue las
practicas de python, que este en minuscula y
la variable, los numeros son opcionales, y tenga
un guion bajo por cada espacio en blanco de cada
palabra, como haciendo una serpiente Snake Keys

Podemos utilizar Mayusculas, y podemos prescindir
de guiones bajos, pero en cada lenguaje hay unas
convenciones, cuando aprendemos un lenguaje
se tiene que tener en cuenta esas convenciones
para Pyhton es el Snake Keys
'''
my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Para concatenar en un print se utiliza ,
print(my_string_variable, my_int_variable, my_bool_variable)

print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

'''
En print de recibir todo tipo
de datos para convertirlos en texto
'''

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola linea
name, surname, alias, age = "Brais", "Moure", "MoureDev", 35
print(name)
print(surname)
print(alias)
print(age)

print("Me llamo:", name, surname, ". Mi edad es:", age, "Y mi alias es:", alias)

'''
Puede ser muy peligroso pues
los datos se pueden mezclar,
lo puedes hacer, pero no hagas
muchos para que no te lies

Puedes mezcar varios tipos de datos

¡Cuidado con abusar de esta sintaxis!

Hay funciones que devuelven dos resultados,
cuando queremos empaquetar varios resultados
para utilizarlos en una funcion, solo utilizamos
esta sintaxis y luego despues utilizar la funcion
que pide y muestra esos resultados

'''
# name, surname, alias, age = "Brais", "Moure", 35, "MoureDev" # No da error y por eso ten cuidado

# Para transformar el entero en float
name, surname, alias, age = "Brais", "Moure", "MoureDev", 35.0
name, surname, alias, age = "Brais", "Moure", "MoureDev", float(35)

# Inputs

'''
No es habitual utilizar input
a no ser que el programa en cuestion
se utilizara para la consola
'''

name_surname = input("Your name and surname: ")
age = input("Your age: ")

print(name_surname)
print(age)

'''
Aqui estamos machacando
el valor anterior de la
variable name, es decir,
estamos reasignado el
valor de la variable

Recuerda que las variables
pueden cambiar de valor
'''

name = input("Your name: ")
print(name)

'''
Python no tiene un tipado fuerte,
no es que python trabaje con un
tipo de dato indefinido, pero,
puedes cambiar el tipo de dato
que va a tener una variable o
varias variables, no solamente
su contenido e información

'''

name = 35
age = "Brais"
# name = age
print(name)
print(age)

'''
Recuerda, que si cambias de tipo
de dato, pues un operador como +
puede cambiar el efecto que puede
tener

Pues si tu dices

    'farfqewreqw' + 'afdsafsdasd'
    '5' + '4'
    
estaras concatenando texto,

    'farfqewreqw' + 'afdsafsdasd'
            'farfqewreqwafdsafsdasd'
    '5' + '4'
            '54'

pero, si utilizas + en digitos numericos

    7 + 3
    12 + 4
    
ya estarias sumando

    7 + 3
        10
    12 + 4
        16
'''

'''
Si quieres definir en una variable
el tipo de dato que va tener dicha
variable solo hay que escribir lo
siguiente

ojo esto no significa que aqui
estemos forzando a la variable
a tener dicho dato, solo es una
ayuda visual, ademas de ser una
buena practica para que la
sintaxis se vea mucho mas exacta
concretada, definida, pues con
esto decimos sin comentarios
que la variables es de un tipo
de dato
'''
address: str = "Mi dirección"
print(address)
address: int = 32
print(type(address))
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
print(type(address))

address: int = input("Dato: ") # Ni aun con input podrias forzar el tipo dato para la variable
print(address)

'''
Lo bueno de python es que no tiene
muchos tipos de datos
'''