# https://web.archive.org/web/20111010053227/http://jaynes.colorado.edu/PythonGuidelines.html#module_formatting
__autor__ = "Ismael Montoro Peñasco"
__copyright__ = "Copyright 2024, Rick and Morty"
__credits__ = ["Ismael Montoro Peñasco"]

__license__ = "WTFPL"
__version__ = "1.0.0"
__status__ = "Stable"
__maintainer__ = None
__email__ = None

import tkinter as tk
import requests as http
from urllib.request import urlopen
from PIL import ImageTk, Image  # https://www.activestate.com/resources/quick-reads/how-to-add-images-in-tkinter/

ventana = tk.Tk()

ventana.title("Rick and Morty")
ventana.resizable(width=False, height=False)
ventana.geometry("910x480")
ventana.configure(bg="black")

def peticion(identifiador: int):
    # https://rickandmortyapi.com/api/character/
    # https://rickandmortyapi.com/documentation/#character
    resultado = http.get(f"https://rickandmortyapi.com/api/character/{identifiador}")
    return resultado.json()

def busqueda(identicacion: int = 1):
    personajes = peticion(identicacion)
    nombre = personajes['name']
    especie = personajes['species']
    genero = personajes['gender']
    estado = personajes['status']
    planeta_origen = personajes['origin']['name']

    foto = Image.open(urlopen(personajes['image']))

    return {'nombre': nombre,
            'especie': especie,
            'genero': genero,
            'estado': estado,
            'planeta': planeta_origen,
            'foto': foto}

def actualizacion():
    identificador_busqueda = cuadro_busqueda.get()
    resultado = busqueda(int(identificador_busqueda))
    acceso_info[0].set("Nombre - " + resultado['nombre'])
    acceso_info[1].set("Especie - " + resultado['especie'])
    acceso_info[2].set("Genero - " + resultado['genero'])
    acceso_info[3].set("Estado - " + resultado['estado'])
    acceso_info[4].set("Planeta - " + resultado['planeta'])
    # https://stackoverflow.com/questions/3482081/how-to-update-the-image-of-a-tkinter-label-widget
    # https://www.lawebdelprogramador.com/foros/Python/1693367-Tkinter-cambio-de-imagen-por-otra.html
    foto = ImageTk.PhotoImage(resultado['foto'])
    foto_perfil.configure(image=foto)
    foto_perfil.image = foto

vertical = 120
horizontal = 430

resultado = busqueda()
acceso_info = list()

# https://gist.github.com/esmitt/8bcdb842b7c1206052f18bf9e4b08e66
foto = ImageTk.PhotoImage(resultado['foto'])
foto_perfil = tk.Label(ventana, image=foto, bg="gray")
foto_perfil.place(x=70, y=vertical)

for caracteristica, info in resultado.items():

    if str(caracteristica) == "foto":
        break

    dato_exportado = tk.StringVar(value=f"{caracteristica.capitalize()} - {info}")
    acceso_info.append(dato_exportado)
    etiqueta_info = tk.Label(ventana, textvariable=dato_exportado,
                             bg="black", fg="white", font={"Arial", 20})
    etiqueta_info.place(x=horizontal, y=vertical)
    vertical += 70

pregunta = tk.Label(ventana, text="Identificacion, por favor:",
                    bg="black", fg="white", font={"Arial", 20})
pregunta.place(x=70, y=43)

cuadro_busqueda = tk.Entry(ventana, width=30)
cuadro_busqueda.place(x=320, y=50)

boton_busqueda = tk.Button(ventana, text="Identificar", fg="white", bg="black", borderwidth=2, command=actualizacion)
boton_busqueda.place(x=550, y=45)

ventana.mainloop()
