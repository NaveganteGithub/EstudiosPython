import requests as r

URL = "http://localhost:3000/alumnos"

try:
    respuesta = r.get(URL)
    print(respuesta)
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
consulta4 = {"nota_lt": 7}
consulta5 = {"nota_le": 7}
consulta6 = {"nota_gt": 7}
consulta7 = {"nota_ge": 7}

try:
    respuesta = r.get(URL, params=consulta4)
    print(respuesta.json())
except r.RequestException:
    print("Conexion rechazada")
