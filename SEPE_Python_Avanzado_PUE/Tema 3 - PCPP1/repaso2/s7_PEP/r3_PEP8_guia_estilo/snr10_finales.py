# No uses espacios en blanco ni antes, ni después del final


mi_diccionario = dict()

## Bueno
def mi_funcion(num, base=2):
    return num * base

mi_tupla = (0,1,2,)
mi_funcion(5)
mi_diccionario['clave'] = mi_tupla[0]

pera = 5
pera = pera + 10
pera -= 3

pera = pera*4 ** 3
pera = (pera+7) * (pera+12)

## Malo
def mi_funcion(num, base = 2):
    return num * base

mi_tupla = (0,1,2, )
mi_funcion (5)
mi_diccionario['clave'] = mi_tupla [0]

pera = 5
pera = pera+10
pera -=3

pera = pera * 4 ** 3
pera = (pera + 7) * (pera + 12)
