import requests as r

enlace = "http://localhost:3000"
cabecera = {"Content-type": "application/json"}
r.delete(enlace + "/empleados/00008", headers=cabecera)
