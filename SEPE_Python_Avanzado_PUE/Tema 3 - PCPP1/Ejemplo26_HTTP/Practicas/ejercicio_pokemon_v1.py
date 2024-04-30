'''
    1ª version: buscar un pokemon y sacar la informacion por consola
    2ª version: crear una GUI solicitar el nombre del pokemon en un Entry
                boton que al pulsar buscar lanza la peticion
                mostrar la informacion en una etiqueta
'''

import requests

try:
    pokemon = requests.get("https://pokeapi.co/api/v2/pokemon/aegislash-shield")
except requests.RequestException:
    pass
else:
    if pokemon.status_code == requests.codes.ok:

        respuesta = pokemon.json()
        print(respuesta['id'])
        print(respuesta['species']['name'])

        for tipo in respuesta['types']:
            print(tipo['type']['name'])

        for habilidad in respuesta['abilities']:
            print(habilidad['ability']['name'])

        for stat in respuesta['stats']:
            print(stat['stat']['name'], stat['base_stat'])
