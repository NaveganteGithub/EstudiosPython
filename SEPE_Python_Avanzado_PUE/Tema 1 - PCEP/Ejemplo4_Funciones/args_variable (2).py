# Funcion con numero variable de argumentos
def sumar(*numeros) :
    suma = 0
    for num in numeros :
        suma += num
    return suma

def prueba(*tuplas):
    print(tuplas)

print(sumar())
print(sumar(1))
print(sumar(2,5))
print(sumar(2,5,7))
print(sumar(2,5,7,1,9,2,3,4,5,6,7,8,9))
print()
print("Hola", "Que tal?", "Como vas?")

# crear una funcion que recibe el nombre del alumno y las notas de las asignaturas en las que se ha matriculado
# retornar la nota media del alumno
# mostrar el nombre y la nota media recibida de la funcion
# en el caso de tener varios parametros si uno de ellos es variable debe ir al final
def procesar_notas(nombre, *notas ) :  # 7,3,9,2
    nota_media = sumar(*notas) / len(notas)  # *notas -> 7,3,9,2    notas -> tuple(7,3,9,2)
    return nombre + ": " + str(nota_media)

print(procesar_notas('Pepito', 7,3,9,2))
print(procesar_notas('Juanita', 9,8,7))

tupla = (1,2,3,4,5)
#print(sumar(tupla))  # envio un solo parametro que es una tupla de numeros
print(sumar(*tupla))  # envio los numeros de la tupla

prueba(tupla)