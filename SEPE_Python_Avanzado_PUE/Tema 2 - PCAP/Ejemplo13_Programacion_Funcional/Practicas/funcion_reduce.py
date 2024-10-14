from functools import reduce

numeros = list(range(1,101))

# Una funcion con reduce en la primera tanda recibe
# los dos valores del principio, y luego se ira
# pasando de uno es uno
def sumar(acumulador, num):
    print(acumulador, num)
    return acumulador + num

result = reduce(sumar, numeros)
print(result)



nombres = ['Luis', 'Maria', 'Adolfo', 'Pedro']

def nombs_mayus(cadena, nombre: str):
    return cadena.upper() + " - " + nombre.upper()

cadena = reduce(nombs_mayus, nombres)
print(cadena)