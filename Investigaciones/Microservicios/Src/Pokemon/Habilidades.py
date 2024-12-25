import requests

inicio_rango = 0
limite_rango = 10
pokeapi_co = "https://pokeapi.co/api/v2/ability?limit=" + str(limite_rango) + "&offset=" + str(inicio_rango)

habilidades = requests.get(pokeapi_co)

if habilidades.status_code == 200:
    habilidades = habilidades.json()

    for habilidad in habilidades['results']:
        print(habilidad['name'])
        informacion = requests.get(habilidad['url']).json()
        print(informacion['effect_entries'][1]['effect'])
        print(informacion['generation']['name'])
        print()