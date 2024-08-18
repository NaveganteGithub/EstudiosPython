import json
import requests as r

# GET = LEER O READ

enlace = "http://localhost:3000"

respuesta = r.get(enlace + "/empleados")

print(respuesta.json())
print(respuesta.status_code)  # En caso de haber encontrado el recurso lanzara el codigo de estado 200 o OK
