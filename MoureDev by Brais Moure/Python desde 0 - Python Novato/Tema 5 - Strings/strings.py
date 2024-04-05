# Strings

my_string = "Mi String"
my_other_string = 'Mi otro String'

# len() averigura la longitud del texto contenido en la variable
print(len(my_string))
print(len(my_other_string))

# Operacion de concatenacion
print(my_string + " " + my_other_string)
print(my_string, my_other_string)

# Operacion de salto de linea
my_new_line_string = "Este es un String\ncon un salto de linea"
print(my_new_line_string)

# Operacion de tabulacion
my_tab_line_string = "\tEste es un String"
print(my_tab_line_string)

# Operacion de escape o anulacion de caracteres especiales
my_scape_string = "\\tEste es un String \n escapado"
print(my_scape_string)
my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# Formatear Strings, equivalente 

name, surname, age= "Brais", "Moure", 35
'''
% va a realizar una accion de formateo, ¿que tenemos para el formateo?:

    %s - que sirve para formatear texto
'''
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
# print("Mi nombre es %s %s y mi edad es %s".format(name, surname, age)) # Esta mal, no funciona
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) # Funciona, con una sintaxis limpia
print("Mi nombre es %s %s y mi edad es %d" %(surname, name, age))
print("Mi nombre es %s %s y mi edad es %s" %(name, surname, "Hola"))
# print("Mi nombre es %s %s y mi edad es %d" %(name, surname, "Hola")) # Esta mal, no funciona, uses string en un % de double o numeros flotantes

# print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age)) # Codigo sucio, con poco rendimiento

# print("Mi nombre es {name} {surname} y mi edad es {age}") # Funciona, pero mal
print(f"Mi nombre es {name} {surname} y mi edad es {age}") # Funciona, con una sintaxis limpia

# Desempaquetado de caracteres

'''
Esto estaria mal y no se ejecutaria, pues aqui estamos declarando
dos variables que tienen que ser rellenadas con un valor cada una
y claro solo rellenamos una variable que es la a y la b se deja
vacia

language = "Python"
a, b = language
print(a)
print(b)

Si quisieramos solucionar este dilema tenemos dos opciones

    Rellenar cada una de las variables con un valor
    
    language = "Python"
    a, b = language, "Mundo"
    
    Rellenar cada variable con cada letra de una cadena
    esto es el desempaquetado de caracteres
'''
language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Division

'''
La operacion de division consiste en la extraccion de caracteres
de forma selectiva, es decir, podemos extraer los caracteres que
queremos de una cadena de texto
'''

language_slice = language[1:3]
print(language_slice)

# Aqui extreriamos desde el caracter de la posicion 1 hasta el final
language_slice = language[1:]
print(language_slice)

# Aqui extreriamos desde el caracter desde el inicio hasta la posicion 4
language_slice = language[:4]
print(language_slice)

# Aqui extraerimos el caractes de la posicion 2 empezando por la parte del final
language_slice = language[-2]
print(language_slice)
language_slice = language[2]
print(language_slice)

'''
Aqui extraemos un rango de caracteres del 0 al 6, pero de ese rango se mostraria
solamente las letras que desde el inicio de ese rango hasta el final de ese rango
tengan saltos de ese numero de salto

    Python
    012345
    
    0:6
    
    Python
    012345
    
    2
    
    Pto
    024
    
    El resultado es Pto

'''
language_slice = language[0:6:2]
print(language_slice)

language_slice = language[1:2:4]
print(language_slice)

# Reverse

reversed_language = language[::-1] # Operacion Reverse nos permite voltear un texto
print(reversed_language)

# Metodos para texto
print(language.capitalize())
print(language.upper())
print(language.lower())
'''
Cuenta el numero de caracteres repetidos dentro
de una cadena, ese caracter es pasado por parametro
'''
print(language.count("t"))
print(language.isnumeric()) # ¿Es numerica la cadena o no?
print("1".isnumeric()) # ¿Es numerica la cadena o no?
print(language.islower()) # Comprueba si una cadena esta en minusculas o no
print(language.isupper()) # Comprueba si una cadena esta en mayusculas o no
print(language.lower().islower())
print(language.upper().isupper())
print(language.lower().isupper())
print(language.upper().islower())
'''
Comprueba si una cadena, empieza o no desde la subcadena indicada
Sensitive Case
'''
print(language.startswith("py"))
print(language.startswith("Py"))