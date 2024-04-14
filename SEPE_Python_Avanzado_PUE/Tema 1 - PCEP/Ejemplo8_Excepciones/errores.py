# try-except-else-finally

numero1 = 0
try:
    # las sentencias que podrian causar el error
    numero1 = int(input("Introduce un numero entero: "))
except:
    # capturar el error para que el programa no termine
    print("Error: debe ser un numero entero")
else:
    # solo se ejecuta si no ha habido errores
    print("Correcto, has introducido un numero entero")
finally:
    # siempre se va a ejecutar este bloque haya errores o no
    print("Numero:", numero1)

# Combinaciones minimas
try:
    pass
except:
    pass

try:
    pass
finally:
    pass