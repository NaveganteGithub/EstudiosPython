'''
    Crear un funcion que recibe un texto y retornar:
        - Texto en mayusculas
        - Texto en minusculas
        - Longitud del texto
'''

def procesar_texto(texto):
    mayusculas = texto.upper()
    minusculas = texto.lower()
    longitud = len(texto)
    return mayusculas, minusculas, longitud

# recuperar con multiples variables
# ValueError: too many values to unpack (expected 2)
'''
txt_may, txt_min = procesar_texto("Por fin es viernes")
print(txt_may)
print(txt_min)
'''

txt_may, txt_min, len_txt = procesar_texto("Por fin es viernes")
print(txt_may)
print(txt_min)
print(len_txt)


# recuperar con una lista
lista = procesar_texto("Por fin es viernes")
for item in lista:
    print(item)