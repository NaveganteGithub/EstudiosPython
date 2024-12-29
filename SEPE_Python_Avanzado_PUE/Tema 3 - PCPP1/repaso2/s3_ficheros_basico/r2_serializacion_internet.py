import pickle

mensaje = "Esto es un mensaje que va a ser serializado"

mensaje_serializado = pickle.dumps(mensaje)

mensaje_deserializado = pickle.loads(mensaje_serializado)

print(mensaje_serializado, mensaje_deserializado, sep="\n")

##############################################################

fichero = open("./prueba.txt", "rt", encoding="utf-8")
contenido_en_bytes = fichero.read()

fichero_salida = open("serializado.pckl", "wb")

# Solo puede serializar objetos de Python, como Strings o Clases, ficheros directamente no
pickle.dump(contenido_en_bytes, fichero_salida)

fichero.close()
fichero_salida.close()

fichero_entrada = open("./serializado.pckl", "rb")
fichero = pickle.load(fichero_entrada)
print(fichero)
fichero_entrada.close()
