import speech_recognition as sr # pip install SpeechRecognition

# FUENTE: https://www.youtube.com/watch?v=P5lRHwue4aw

# Inciaremos un reconocedor de voz
reconocedor = sr.Recognizer()

# Capturar el audio guardado. Necesitaremos el archivo de 
# audio en formato wav, no vale mp3 u otros formatos
archivo = 'Archivo.wav'
audio = sr.AudioFile(archivo)

# Abriremos el objeto con with
with audio as source:
    audio = reconocedor.record(source)

# Convertiremos el audio a texto
texto: str = reconocedor.recognize_google(audio)

# Lo imprimimos
print(texto.lower())
