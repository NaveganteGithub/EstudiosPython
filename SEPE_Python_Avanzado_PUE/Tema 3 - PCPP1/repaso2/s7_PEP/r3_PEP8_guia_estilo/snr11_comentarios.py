# Los comentarios en bloque deben ir con un # seguido de un espacio

def saludar():
    # Esta es una función básica para decir Hola la salida.
    #
    # Por defecto se hace por pantalla, pero se puede
    # modificar el print para redirigir la salida a
    # través del parametro file
    print("Hola")

# Los comentarios en línea deben ser separados del código dos o más espacios en blanco,
# además de no usarlos para cosas innecesarias

## Bien
resultado = 5 + 7   # Resultado de una suma

## Mal
resultado = 8 + 1 # Resultado de una suma

# Intenta siempre que tu código se autocomente, es mucho mejor que hacer comentario

## Bien

identificador_codigo_barras = 0x0001fa330f

## Mal

a = 0x0001fa330f  # Identificador para el código de barras
