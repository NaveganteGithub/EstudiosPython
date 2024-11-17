import requests as r

URL = "http://localhost:3000/alumnos/6"

try:
    r.delete(URL)
except r.RequestException:
    print("No se ha podido eliminar el elemento")
else:
    print("Elemento eliminado")
