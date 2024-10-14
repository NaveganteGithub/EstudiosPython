import requests

''' DELETE para eliminar un recurso nuevo '''

# Solo se permite borrar por id
try:
    respuesta = requests.delete("http://localhost:3000/alumnos/6")
except requests.RequestException:
    print("Error al modificar")
else:
    if respuesta.status_code == requests.codes.ok:
        print(respuesta.json())
