import pyttsx3

# Crearemos el motor para generar audios
motor = pyttsx3.init()

# Crearemos una coleccion con los audios 
# necesarios para generar un audio solo 
# hay dos de hombre y mujer
voces = motor.getProperty('voices')

# Seleccionaremos la voz de hombre indicando
# el indice 0, si quisieras la voz de mujer
# tienes que pedir el indice 1
motor.setProperty('voice', voces[0].id)

# Introduciremos el dialogo o oracion a expresar
oracion = input("Introduce un dialogo: ")

# Guardaremos el audio como un archivo mp3
archivo_salida = "mi_dialogo.mp3"
motor.save_to_file(oracion, archivo_salida)

# Ejecutamos el programa
motor.runAndWait()
