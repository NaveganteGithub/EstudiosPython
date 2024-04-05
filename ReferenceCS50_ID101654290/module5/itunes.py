import json # libreria python que me permite manejar datos json
import requests # libreria python para interactuar mediante http o https con servidores
import sys

if len(sys.argv) != 2:
    sys.exit()

'''
get es una funcion de request que me permite realizar una peticion a un sitio web
'''
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# json es una funcion de request que me permite formatear la informacion en formato json
# dumps es una funcion que permite formatear la informacion para que quede en un formato mas limpio
# print(json.dumps(response.json(), indent=2))

o = response.json()

for result in o["results"]:
    print(result["trackName"])