# Formato de texto para guardar e intercambiar informacion

"""
El formato JSON (JavaScript Object Notation; notación de objetos JavaScript)
es muy conocido y utilizado en la industria de las aplicaciones web, dado que
permite crear parseadores de contenido de forma rápida e intercambiar datos
entre aplicaciones utilizando un número de caracteres extra muy pequeño.
Este formato se suele comparar con XML, dado que ambos se utilizan para
intercambiar datos. JSON, sin embargo, necesita menos caracteres para enviar
la misma información y, por tanto, se utiliza más a menudo, principalmente en
aplicaciones web que usan AJAX. - Pedro Ángel Viruega Muñoz
"""

# Objeto JSON {"nombre": "Anabel", "edad": 53}  {"propiedad": valor}
# Objeto JSON con una rpopiedad de tipo Array
{"nombre": "Anabel", "edad": 53, "cursos": ["Python", "Java", "Angular"]}

# Crear un array de objetos JSON
[
    {"id": 1, "descripcion": "Pantalla", "precio": 129.95, "stock": true},
    {"id": 2, "descripcion": "Raton", "precio": 22.50, "stock": true},
    {"id": 3, "descripcion": "Teclado", "precio": 49.80, "stock": false}
 ]

# Tipos de datos JSON

# numeros enteros
{"entero": 6, "hexadecimal": 0x15454546, "octal": 0o15454546, "binario": 0b01110}

# numeros reales
{"real": 50.51, "cientifica":8.12121E15, "negativo": -39.454545E-15}

# cadenas de texto
{"nombre": "Anabel"}

# boleanos
{"cansados": true, "ganas_fiesta": false}

# Nulos
{"energia": null}
