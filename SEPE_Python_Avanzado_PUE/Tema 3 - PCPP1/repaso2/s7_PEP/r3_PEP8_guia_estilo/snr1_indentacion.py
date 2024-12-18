# Python 3 no permite la tabulación, aquí se tiene que usar 4 espacios en blanco,
# en la API de Python 3, existe TabError, excepción que se ejecuta cuando se crea
# una tabulación como indentación para el código, esto es fuera del IDE

## Bueno
def espacios_funct():
    print("Hola")  # 4 Espacios en blanco

## Malo
def tabulation_funct():
	print("Hola")  # Tabulación

espacios_funct()
tabulation_funct()
