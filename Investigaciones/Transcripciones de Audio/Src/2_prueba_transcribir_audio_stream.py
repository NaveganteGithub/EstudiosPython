import speech_recognition as sr # pip install SpeechRecognition
import pyaudio

# FUENTE: https://www.youtube.com/watch?v=P5lRHwue4aw

# Inciaremos un reconocedor de voz
reconocedor = sr.Recognizer()

# Abriremos el objeto con with
with sr.Microphone() as micro:
    # Ajustaremos el script para utilize el microfono por defecto, 
    # y que la duracion de la grabacion sea de 0.4
    reconocedor.adjust_for_ambient_noise(micro, duration=0.4)
    # Grabaremos el audio con el microfono por defecto
    audio = reconocedor.listen(micro)
    # Convertiremos el audio a texto
    texto: str = reconocedor.recognize_google(audio)
    # Lo imprimimos
    print(texto.lower())
