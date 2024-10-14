import pickle

# file = "binario.pckl"
file = "binario.bin"
nombres = ["Juan", "Maria", "Pedro", "Pablo", "Laura"]
fichero = open(file, "wb")

pickle.dump(nombres, fichero)

fichero.close()