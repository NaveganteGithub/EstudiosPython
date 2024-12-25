import requests

pokeapi_co = "https://pokeapi.co/api/v2/move?limit=10&offset=0"

pokedex = requests.get(pokeapi_co)