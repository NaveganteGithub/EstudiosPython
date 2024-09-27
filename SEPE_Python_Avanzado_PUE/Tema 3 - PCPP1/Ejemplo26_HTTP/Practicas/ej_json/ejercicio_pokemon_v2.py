'''
    1ª version: buscar un pokemon y sacar la informacion por consola
    2ª version: crear una GUI solicitar el nombre del pokemon en un Entry
                boton que al pulsar buscar lanza la peticion
                mostrar la informacion en una etiqueta
'''

import tkinter as tk
import requests

datos = dict()
claves = ['id', 'especie', 'tipo', 'habilidad', 'stat']

ventana = tk.Tk()
ventana.title("Pokedex")
ventana.resizable(width=False, height=False)
ventana.geometry("400x600")

pregunta = tk.Label(ventana, text="Introduce un id:", font={"Arial", 10})
pregunta.place(x=10, y=10)

for clave_actual in claves:
    datos[clave_actual] = ''

altura_vertical = 130
altura_horizontal = 20
margen = 70
fuente = {"Arial", 20}
fuente_stats = {"Arial", 5}

for clave in datos.keys():
    info_pokemon = tk.StringVar(value=clave.capitalize())
    info_etiqueta = tk.Label(ventana, textvariable=info_pokemon, font=fuente)
    info_etiqueta.place(x=altura_horizontal, y=altura_vertical)
    altura_vertical += margen

# Reiniciamos los contadores para poder orden logico a la interfaz
etiquetas_info = list()
altura_vertical = 130
altura_horizontal = 120
# https://stackoverflow.com/questions/37318060/how-to-justify-text-in-label-in-tkinter
for i in range(len(datos.keys())):
    info_pokemon = tk.StringVar(value=" ")
    info_etiqueta = tk.Label(ventana, textvariable=info_pokemon, justify="left", font=fuente)
    etiquetas_info.append(info_pokemon)
    info_etiqueta.place(x=altura_horizontal, y=altura_vertical)
    altura_vertical += margen

entrada = tk.Entry(width=35)
entrada.place(x=165, y=16)

def busqueda():
    id = entrada.get()
    if id.isdigit():
        try:
            pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
        except requests.RequestException:
            pass
        else:
            if pokemon.status_code == requests.codes.ok:
                respuesta = pokemon.json()

                etiquetas_info[0].set(respuesta['id'])
                etiquetas_info[1].set(respuesta['species']['name'])

                tipos = "\n".join(
                    list(
                        tipo['type']['name'] for tipo in respuesta['types']
                    )
                )
                etiquetas_info[2].set(tipos)

                habilidades = "\n".join(
                    list(
                        habilidad['ability']['name'] for habilidad in respuesta['abilities']
                    )
                )
                etiquetas_info[3].set(habilidades)

                estadisticas = "\n".join(
                    list(
                        stat['stat']['name'] + " " + str(stat['base_stat'])
                            for stat in respuesta['stats']
                    )
                )
                etiquetas_info[4].set(estadisticas)

boton_buscar = tk.Button(ventana, text="Buscar", font={"Arial", 15}, command=busqueda)
boton_buscar.place(x=165, y=50)

ventana.mainloop()