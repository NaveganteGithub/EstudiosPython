import json

with open("datos.json", "w") as archivo:

    diccionario = {
        "enteros": {"Decimales": [123, -123],
                    "Binarios": 0b0101010,
                    "Octales": 0o151057,
                    "Hexadecimales": 0x42F58D54
                    },
        "decimales": {"Flotantes": [0.04, -0.4],
                      "Cientificos": [65e448662, 57e54653]
                      },
        "cadenas": ["Hola", "Adios"],
        "booleanos": [True, False],
        "Nulos": None
    }

    global diccionario_json_str
    diccionario_json_str = json.dumps(diccionario)

    json.dump(diccionario, archivo)


with open("datos.json", "r") as archivo:

    lectura = json.load(archivo)
    print(lectura)

    lectura = json.loads(diccionario_json_str)
    print(lectura)
