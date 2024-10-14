import sys # sys sirve para acceder a los recursos del sistema en este caso a los argumentos de la linea de comandos

from PIL import Image # se importara desde la libreria PIL la funcion Image

images = []

for arg in sys.argv[1:]: # Examine todos los parametros excepto el primero que es el nombre del fichero
    image = Image.open(arg)
    images.append(image)


images[0].save(
    "costumes.gif", # el nombre del archivo resultante
    save_all=True, # aqui se indica que se quiere realizar un guardado a todos las imagenes que se pase por parametro
    append_images=[images[1]], # aqui se indicara las imagenes que se quieren utilizar para unificarlas todas en un fichero
    duration=200, # como es una imagen que se mueve se indicara cuanto tiempo durara la imagen
    loop=0 # Aqui se indicara cuantas veces se tiene que repetir la imagen, en caso de que sea 0 seran infinitas veces
)