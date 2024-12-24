from gtts import gTTS # pip install gTTS
from IPython.display import Audio # pip install IPython

# FUENTE: https://www.youtube.com/watch?v=4WU-CUHt4sk

# Creamos el mensaje
mensaje = "Hola, ¿Como estás?"

# Instanciamos el objeto gTTS, usando los parametros 
# text para indicar el mensaje, y lang para indicar 
# el idioma en el que esta escrito el mensaje, tenemos
# varios idiomas disponibles, ingles (en), español (es),
# frances (fr), aleman (de), italiano (it), japones (ja),
# coreano (ko), portugues (pt), ruso (ru), chino (ch), entre
# otros idiomas que tenemos a la mano
tts = gTTS(text=mensaje, lang="es")

archivo_salida = 'mi_mensaje.mp3'
tts.save(archivo_salida)

Audio(archivo_salida)