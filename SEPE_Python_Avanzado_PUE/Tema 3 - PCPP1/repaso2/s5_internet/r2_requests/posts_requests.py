import requests as r
import json

# La libreria requests para los identificadores usa strings
datos = json.dumps({
     "id": "6",
     "nombre": "Daniel", "apellido": "Peñasco",
     "nota": 6, "repetidor": True
})

URL = "http://localhost:3000/alumnos"

try:
    r.post(URL, data=datos)
except r.RequestException:
    print("Conexion rechazada")
else:
    print("Conexion finalizada con exito")
finally:
    print("Programa finalizado")


try:
    respuesta = r.get(URL + "/6")
except r.RequestException:
    print("Conexion rechazada")
else:
    print(respuesta.text)
finally:
    print("Programa finalizado")