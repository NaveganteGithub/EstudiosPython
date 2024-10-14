import shelve

ruta = ".\\salidas"
fichero = "fichero"

serializacion = shelve.open(ruta + "\\" + fichero, flag="n")

serializacion['objetivos'] = {"RAS": 3, "AWD": 5, "GTR": 10, "ED": 2}
serializacion['procedimientos'] = ["Explorar", "Identificar", "Examinar", "Detallar", "Accionar"]
serializacion['accionar'] = {"Vigilar": [4562, 4823, 654], "Captura": [5665]}

serializacion.close()

lectura = shelve.open(ruta + "\\" + fichero)
print(lectura['objetivos'])
print(lectura['procedimientos'])
lectura.close()
