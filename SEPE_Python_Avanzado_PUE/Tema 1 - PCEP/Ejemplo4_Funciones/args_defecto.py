def datos_trabajador(nombre, estado_civil="Soltero", sueldo=21000) :
    return nombre + " esta " + estado_civil + " gana " + str(sueldo)

print(datos_trabajador("Jose"))
#print(datos_trabajador("Jose", 35000))  # interpreta que 35000 es el estado civil
print(datos_trabajador("Jose", sueldo=35000))
print(datos_trabajador("Jose", estado_civil="Casado"))
print(datos_trabajador("Jose", estado_civil="Casado", sueldo=35000))
print(datos_trabajador("Jose", "Casado", 35000))

# crear una funcion que recibe:
#   - datos como numero variable de argumento
#   - caracter separador opcional, por defecto " | "
#   separador.join(datos)

def mi_union1(*datos, separador=" | "):
    return separador.join(datos)

print(mi_union1("1","4","9","8","7","5","3","6","5","4"))
print(mi_union1("1","4","9","8","7","5","3","6","5","4", separador="-"))
print(mi_union1("1","4","9","8","7","5","3","6","5","4", separador=";"))
print()

# El orden de los parametros en una funcion es importante, sobretodo cuando trabajamos con args
def mi_union(separador=" | ", *datos):
    return separador.join(datos)

print(mi_union("1","4","9","8","7","5","3","6","5","4"))
print(mi_union(":", "1","4","9","8","7","5","3","6","5","4"))
# print(mi_union("1","4","9","8","7","5","3","6","5","4", separador="-"))
# print(mi_union("1","4","9","8","7","5","3","6","5","4", separador=";"))

'''
    Crear un funcion que recibe un texto y retornar:
        - Texto en mayusculas
        - Texto en minusculas
        - Longitud del texto
'''

def procesar_texto(texto: str):
    mayusculas = texto.upper()
    minusculas = texto.lower()
    longitud = len(texto)
    return mayusculas, minusculas, longitud

mayusculas, minusculas, longitud = procesar_texto("Hola mundo")
print(mayusculas, minusculas, longitud, sep=", ")

for iterable in procesar_texto("Hola mundo"):
    print(iterable)
