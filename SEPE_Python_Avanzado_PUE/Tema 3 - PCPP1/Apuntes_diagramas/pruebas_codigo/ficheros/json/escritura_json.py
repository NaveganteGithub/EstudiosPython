import json

diccionario = {"identificadores": [4556456, 5456655, 8971345],
               "nombres": ["Lucia", "Raquel", "Daniel"],
               "academicos": True
               }

print(json.dumps(diccionario))

with open("prueba.json", "w", encoding="utf-8") as fj:
    json.dump(diccionario, fj) # s de string
