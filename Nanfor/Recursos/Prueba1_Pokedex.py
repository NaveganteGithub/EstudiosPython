import requests

pokeapi_co = "https://pokeapi.co/api/v2/pokemon?limit=10&offset=0"

pokedex = requests.get(pokeapi_co)

if pokedex.status_code == 200:

    pokedex = pokedex.json()

    """for pokemon in pokedex:
        print(pokemon)"""
    
    for pokemon in pokedex['results']:
        # print(pokemon)

        # print(pokemon['url'])
        
        print(pokemon['name'])
        
        enlace = "https://pokeapi.co/api/v2/pokemon/" + pokemon['name']
        # print(enlace)
        
        enlace = requests.get(enlace)
        if enlace.status_code == 200:
            detalles = enlace.json()

            for detalle in detalles['moves']:
                print(detalle['move']['name'], end=" ")

            print()

            for stat in range(6):
                print(detalles['stats'][stat]['stat']['name'], end=": ")
                print(detalles['stats'][stat]['base_stat'])

            print()

            for tipo in detalles['types']:
                print(tipo['type']['name'])

        print("\n"*2)