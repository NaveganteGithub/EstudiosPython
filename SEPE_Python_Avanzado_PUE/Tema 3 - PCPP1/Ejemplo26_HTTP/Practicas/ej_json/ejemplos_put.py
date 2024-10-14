import json
import requests

''' PUT para modificar '''

new_pedro = {
        "id": "3",
        "nombre": "Pedro",
        "apellido": "Garcia",
        "nota": 5,
        "repetidor": True
}
cabeceras = {"Content-type": "application/json"}

try:
    respuesta = requests.put("http://localhost:3000/alumnos/3", headers=cabeceras, data=json.dumps(new_pedro))
    pedro = requests.get("http://localhost:3000/alumnos/3")
except requests.RequestException:
    print("Error al modificar")
else:
    print("Alumno modificado")
    print(pedro.json())
