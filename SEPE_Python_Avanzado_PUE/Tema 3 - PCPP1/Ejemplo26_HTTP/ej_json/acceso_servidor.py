import requests
"""
El Api Rest es la Unión de 4 tipos de servicios 
lo qume explicaos es que una api rest es como 
un crud en una base de datos.

Cuando tú hablas de me voy a crear una aplicación 
que sea un crud, estamos hablando que a esa base 
de datos le vas a dar la opción de poder consultar 
insertar nuevos registros modificar registros, 
y eliminar registros, vale pero si nosotros todo 
eso tocamos con servicios, web, entonces eso es lo 
que le llamamos una api rest lo que es ese create el aceite vale pero solamente que
utilizamos métodos Http, como ya dijimos, el que es el post, el put y el delete.
"""

url_json = "http://localhost:3000/alumnos"
url_html = "http://localhost:3000"
respuesta = requests.get(url_json)
print(respuesta.status_code)
print(respuesta.cookies)
print(respuesta.text)

respuesta = requests.get(url_html)  # Pedira el index del directorio public
print(respuesta.status_code)
print(respuesta.cookies)
print(respuesta.text)  # Mostrara el contenido de lo que se ha pedido

# Codigos de respuesta disponible
for code in requests.codes.__dict__:
    print(code)

# Condicionales con los codigos de respuesta
if respuesta.status_code == requests.codes.ok:
    print("Conexion correcta")

# Obtener cabecera
cabeceras = respuesta.headers
print(cabeceras)
print(type(cabeceras))
print(cabeceras['Content-Type'])
print(respuesta.headers["Connection"])

try:
    respuesta = requests.get(url_html, timeout=1)
except requests.exceptions.Timeout:
    print("Tiempo excedido")
else:
    print("Conexion ok")

try:
    respuesta = requests.get("http://localhost:3010", timeout=1)
except requests.exceptions.ConnectTimeout:
    print("Error de conexion")
else:
    print("Conexion ok")

try:
    respuesta = requests.get("http:/localhost3010", timeout=1)
except requests.exceptions.InvalidURL:
    print("Error de url")
else:
    print("Conexion ok")

print(dir(requests.exceptions))
