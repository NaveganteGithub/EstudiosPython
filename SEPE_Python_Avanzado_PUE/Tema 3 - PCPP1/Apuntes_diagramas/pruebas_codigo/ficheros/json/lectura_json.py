import json

with open("prueba.json", "r", encoding="utf-8") as fj:
    lectura = json.load(fj)
    print(lectura)

ej_json = '''
{"identificadores": [4556456, 5456655, 8971345], 
"nombres": ["Lucia", "Raquel", "Daniel"], 
"academicos": true}
'''

print(json.loads(ej_json))  # s de string
