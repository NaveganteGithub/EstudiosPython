# Mostrar los numeros del 1 al 10
num = 1
while num <= 10 :
    print(num, end=" ")
    num += 1   # num = num + 1
print("\n------ FIN -----")

    
# Recorrer la lista con el bucle while    
nombres = ['Luis', 'Jorge', 'Maria', 'Laura', 'Pedro']
indice = 0
while indice < len(nombres) :
    print(nombres[indice])
    indice += 1
print("------ FIN -----")


# Solicitar pw al usuario hasta que adivine que es "curso"
pw = ""
while pw != "curso" :
    pw = input("Introduce PW: ")
print("Acceso permitido")

# bucle infinito
"""
while True :
    print("hola")
"""

# bucle con else
i = 0
while i != 0:
    print("Hola")
    i -= 1
else: # Solo se ejecuta en caso de que la condicion del while sea False
    print("Adios", i != 0)
    i += 1

print(i)