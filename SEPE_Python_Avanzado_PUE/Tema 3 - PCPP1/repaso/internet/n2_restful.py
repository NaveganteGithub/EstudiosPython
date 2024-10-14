import requests as r
import json

"""consulta = r.get("https://www.python.org")
print(consulta.text, consulta.status_code, consulta.cookies, consulta.headers, sep="\n")

consulta2 = r.get("https://pokeapi.co/api/v2/pokemon-species/aegislash")
resultado_json = consulta2.json()
print(resultado_json, consulta2.status_code, consulta2.cookies, consulta2.headers, sep="\n")

consulta3 = r.get("http://localhost:3000/cantidades")
resultado_json = consulta3.json()
print(resultado_json, consulta3.status_code, consulta3.cookies, consulta3.headers, sep="\n")"""

datos = {"Salmon": 145.20}
datos_json = json.dumps(datos)
cabecera = {"Content-Type": "application/json"}

resultado = r.post("http://localhost:3000/comida", headers=cabecera, data=datos_json)
print(resultado.status_code)
