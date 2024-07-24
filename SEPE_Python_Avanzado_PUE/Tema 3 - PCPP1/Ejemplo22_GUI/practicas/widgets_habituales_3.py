import tkinter as tk

# crear una nueva ventana

ventana = tk.Tk()

# Asignarle un titulo

ventana.title("Ejemplo de widgets")

# Definir tamaño de la ventana

'''tamaño = '200x300'
tamaño = '500x800'
ventana.geometry(tamaño)'''

# Definir la posicion de la ventana
tamano = '500x800'  # Ancho por Alto
posicion = '500+200'  # Posicion X mas la posicion Y
forma = tamano + "+" + posicion
ventana.geometry(forma)

# Agregar boton a la ventana

boton = tk.Button(ventana, text='Pulsame')
boton.place(x=10, y=20)

# Agregar una etiqueta de texto a la ventana

etiqueta = tk.Label(ventana, text="Introduce tu nombre:")
etiqueta.place(x=10, y=50)

# Agregar una caja de texto a la ventana

caja_texto = tk.Entry(ventana, width=20)
caja_texto.place(x=150, y=50)

# Agregar una caja de contraseña a la ventana

caja_pass = tk.Entry(ventana, show="*")
caja_pass.place(x=10, y=80)

# Agregar una caja de texto desabilitada a la ventana

caja_texto_desabilitar = tk.Entry(ventana, width=20, state='disabled')
caja_texto_desabilitar.place(x=200, y=140)

# Agregar una caja de texto de solo lectura a la ventana

my_str = tk.StringVar()
my_str.set("This is the default text.")
caja_texto_por_defecto = tk.Entry(ventana, width=20, state="readonly", textvariable=my_str)
caja_texto_por_defecto.place(x=150, y=250)

# Crear un Frame

frame_1 = tk.LabelFrame(ventana, width=400, height=100, borderwidth=2, text="Datos Personales")
frame_1.place(x=10, y=280)

## Introducir cosas en el Frame
etiqueta_frame = tk.Label(frame_1, text="Introduce tu nombre:")
etiqueta_frame.place(x=50, y=50)

caja_texto_frame = tk.Entry(frame_1, width=20)
caja_texto_frame.place(x=180, y=50)

# Agregar boton con comando a la ventana

def cerrar_ventana():
    ventana.destroy()

def abrir_ventana():
    ventana_2 = tk.Toplevel(ventana)
    ventana_2.mainloop()

# boton = tk.Button(ventana, text="cerrar", command=cerrar_ventana) # Opcion 1
# boton = tk.Button(ventana, text="cerrar", command=ventana.destroy) # Opcion 2
boton = tk.Button(ventana, text="cerrar")
boton.bind("<Button-1>", lambda e: ventana.destroy())
boton.pack()
boton = tk.Button(ventana, text="abrir", command=abrir_ventana)
boton.bind("<Button-2>")
boton.pack()

# Crear un Checkbutton

acepto = tk.Checkbutton(ventana, text="Acepto condiciones")
acepto.place(x=200, y=200)

# Crear un Radiobutton

genero_str = tk.StringVar()
genero_hombre = tk.Radiobutton(ventana, text="Hombre", variable=genero_str, value="H")
genero_mujer = tk.Radiobutton(ventana, text="Mujer", variable=genero_str, value="M")
genero_hombre.place(x=100, y=280)
genero_mujer.place(x=100, y=300)

# Crear un Listbox

colores = ['Azul', 'Rosa', 'Amarillo', 'Verde']
color = tk.Listbox(ventana, selectmode="multiple")
for item in colores:
    color.insert(tk.END, item)

color.place(x=200, y=400)

# Crear un Combobox
from tkinter import ttk

colores_2 = ['--Selecciona--', 'Azul', 'Rosa', 'Amarillo', 'Verde']
combo = ttk.Combobox(ventana, values=colores_2, state="readonly")
combo.current(0)  # Selecciona el valor por defecto
combo.place(x=10, y=400)

# Crear un OptionMenu
opciones = ["Opcion 1", "Opcion 2", "Opcion 3"]
combobox = tk.OptionMenu(ventana, tk.StringVar(ventana), *opciones)
combobox.place(x=10, y=450)

# mostrar la ventana

ventana.mainloop()
