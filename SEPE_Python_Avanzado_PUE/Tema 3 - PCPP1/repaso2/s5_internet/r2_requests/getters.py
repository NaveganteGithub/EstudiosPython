import requests as r

URL = "http://localhost:3000/alumnos"

try:
    respuesta = r.get(URL)
    print(respuesta)
    print(respuesta.json())
except r.RequestException:
    print("Conexion rechazada")

try:
    respuesta = r.get(URL + "/5")
    print(respuesta.json())
except r.RequestException:
    print("Conexion rechazada")

try:
    respuesta = r.get(URL + "?" + "_sort=nota")
    print(respuesta.json())
except r.RequestException:
    print("Conexion rechazada")


consulta1 = {"_sort": "nota"} # Ordenar en orden ascendete o en alfabetico
consulta2 = {"_sort": "-nota"} # Ordenar en orden descendente
consulta3 = {"repetidor": 0}
consulta4 = {"nota": 5} # equals
consulta5 = {"nota_ne": 7}
consulta6 = {"nota_lt": 7}
consulta7 = {"nota_gt": 7}

try:
    respuesta = r.get(URL, params=consulta7)
    print(respuesta.json())
except r.RequestException:
    print("Conexion rechazada")
