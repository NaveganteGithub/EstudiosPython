import json
import requests

''' POST para crear un recurso nuevo '''
new_alumno = {
      "id": "6",
      "nombre": "Pepito",
      "apellido": "Perez",
      "nota": 2.7,
      "repetidor": True
}
cabeceras = {"Content-type": "application/json"}

try:
    respuesta = requests.post("http://localhost:3000/alumnos", headers=cabeceras, data=json.dumps(new_alumno))
    alumno = requests.get("http://localhost:3000/alumnos/6")
except requests.RequestException:
    print("Error al modificar")
else:
    print("Alumno creado")
    print(alumno.json())
