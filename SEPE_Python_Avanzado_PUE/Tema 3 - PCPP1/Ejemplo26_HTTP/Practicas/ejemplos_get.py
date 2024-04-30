import requests

# Consultar todos los alumnos
try:
    respuesta = requests.get("http://localhost:3000/alumnos")
except requests.RequestException:
    print("Ha ocurrido un error")
else:
    if respuesta.status_code == requests.codes.ok:
        print(respuesta.text)
        print(respuesta.json())

# Consultar todos los alumnos ordenados por nota
try:
    respuesta = requests.get("http://localhost:3000/alumnos?_sort=nota")
except requests.RequestException:
    print("Ha ocurrido un error")
else:
    if respuesta.status_code == requests.codes.ok:
        # print(respuesta.text)
        print(respuesta.json())

try:
    respuesta = requests.get("http://localhost:3000/alumnos", params={"_sort": "nota"})
except requests.RequestException:
    print("Ha ocurrido un error")
else:
    if respuesta.status_code == requests.codes.ok:
        # print(respuesta.text)
        print(respuesta.json())

# Consultar todos los alumnos ordenados por nota descendente
try:
    respuesta = requests.get("http://localhost:3000/alumnos", params={"_sort": "-nota"})
except requests.RequestException:
    print("Ha ocurrido un error")
else:
    if respuesta.status_code == requests.codes.ok:
        # print(respuesta.text)
        print(respuesta.json())

try:
    respuesta = requests.get("http://localhost:3000/alumnos?_sort=-nota")
except requests.RequestException:
    print("Ha ocurrido un error")
else:
    if respuesta.status_code == requests.codes.ok:
        # print(respuesta.text)
        print(respuesta.json())

# Consultar todos los alumnos repetidores
try:
    respuesta = requests.get("http://localhost:3000/alumnos", params={"repetidor": 0})
except requests.RequestException:
    print("Ha ocurrido un error")
else:
    if respuesta.status_code == requests.codes.ok:
        # print(respuesta.text)
        print(respuesta.json())

try:
    respuesta = requests.get("http://localhost:3000/alumnos?repetidor=0")
except requests.RequestException:
    print("Ha ocurrido un error")
else:
    if respuesta.status_code == requests.codes.ok:
        # print(respuesta.text)
        print(respuesta.json())

# Consultar todos los alumnos con notas menores a 5
try:
    respuesta = requests.get("http://localhost:3000/alumnos", params={"nota_lt": 5})
except requests.RequestException:
    print("Ha ocurrido un error")
else:
    if respuesta.status_code == requests.codes.ok:
        # print(respuesta.text)
        print(respuesta.json())

# Consultar todos los alumnos por el id
try:
    respuesta = requests.get("http://localhost:3000/alumnos/3", params={"nota_lt": 5})
except requests.RequestException:
    print("Ha ocurrido un error")
else:
    if respuesta.status_code == requests.codes.ok:
        # print(respuesta.text)
        print(respuesta.json())