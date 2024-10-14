import pickle

# file = "binario.pckl"
file = "binario.bin"
fichero = open(file, "rb")

nombres = pickle.load(fichero)

print(nombres)

fichero.close()