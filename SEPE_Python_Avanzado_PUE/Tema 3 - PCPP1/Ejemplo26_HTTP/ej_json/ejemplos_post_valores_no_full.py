import json
import requests

''' POST para crear un recurso nuevo '''
new_alumno = {  # Si no pones el id te genera uno automaticamente
      "nombre": "Daniel",
      "apellido": "Albarez",
      "nota": 7,
      "repetidor": True
}
cabeceras = {"Content-type": "application/json"}

try:
    respuesta = requests.post("http://localhost:3000/alumnos", data=json.dumps(new_alumno))
    alumno = requests.get("http://localhost:3000/alumnos")
except requests.RequestException:
    print("Error al modificar")
else:
    print("Alumno creado")
    print(alumno.json())
