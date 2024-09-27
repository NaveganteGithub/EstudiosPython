import requests

try:
    respuesta = requests.get("https://api.chucknorris.io/jokes/random")
except requests.RequestException:
    print("Conexion no realizada")
else:
    if respuesta.status_code == requests.codes.ok:
        respuesta_json = respuesta.json()['value']
        print(respuesta_json)
