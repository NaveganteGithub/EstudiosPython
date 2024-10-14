import requests as r
import json

# POST = INSERTAR

enlace = "http://localhost:3000"
cabecera = {"Content-type": "application/json"}
datos = {"id": "00008", "Nombre": "Alicia Sabadel", "Salario": 1500.15, "Puesto": "System Engineer"}
datos_json = json.dumps(datos)

resultado = r.post(enlace + "/empleados", headers=cabecera, data=datos_json)

# En caso de haber creado el recurso lanzara el codigo de estado 201
print(resultado.status_code)
