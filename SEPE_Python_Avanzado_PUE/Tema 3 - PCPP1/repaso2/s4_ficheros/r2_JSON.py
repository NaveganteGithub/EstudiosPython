import json

json_python = {'clave1': [2, 5, 7, 9, 0x12faedd], 'clave2': True, 'clave3': None}

json_puro = json.dumps(json_python) # Obj Python -- Convert --> Obj Json -- Output --> String
print(json_puro)

json_python_leer = json.loads(json_puro)
print(json_python_leer)

json_python_leer = json.loads('{"clave1": [2, 5, 7, 9, 19902173], "clave2": true, "clave3": null}')
print(json_python_leer)


#######################################

json_python = {'clave1': [5, 7, 0x12faedd], 'clave2': True}

fichero = open("./archivo.json", "wt", encoding="utf-8")
json.dump(json_python, fichero)
fichero.close()

fichero = open("./archivo.json", "rt", encoding="utf-8")
contenido = json.load(fichero)
fichero.close()

print(contenido)
