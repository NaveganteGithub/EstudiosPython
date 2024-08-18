import json
import requests as r

# PUT = ACTUALIZAR

enlace = "http://localhost:3000"
cabecera = {"Content-type": "application/json"}
datos = {"id": "00008", "Nombre": "Fernando Garrido", "Salario": 1500.12, "Puesto": "Develop"}
datos_json = json.dumps(datos)
resultado = r.put(enlace + "/empleados/00008", headers=cabecera, data=datos_json)

# En caso de haber actualizado el recurso lanzara el codigo de estado 200 o OK
print(resultado.status_code)
