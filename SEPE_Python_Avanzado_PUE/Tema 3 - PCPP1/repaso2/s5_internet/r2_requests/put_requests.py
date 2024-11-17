import requests as r
import json

datos = json.dumps({"id": "6", "nombre": "Daniel", "apellido": "Peñasco", "nota": 7, "repetidor": True})
URL = "http://localhost:3000/alumnos/6"

try:
    r.put(URL, data=datos)
    respuesta = r.get(URL)
except r.RequestException:
    print("Conexion fallida")
else:
    print(respuesta.json())
finally:
    print("Programa finalizado")
