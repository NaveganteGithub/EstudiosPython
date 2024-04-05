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