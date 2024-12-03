import tkinter as tk
from tkinter import filedialog

def open_file():
    ruta = filedialog.askopenfile(title="Abrir archivo", mode="r")
    return ruta

ventana = tk.Tk()

barra_navegacion = tk.Menu()
ventana.config(menu=barra_navegacion)

opciones_file = tk.Menu(tearoff=0)
barra_navegacion.add_cascade(label="File", menu=opciones_file)

opciones_edit = tk.Menu()
barra_navegacion.add_cascade(label="Edit", menu=opciones_edit)

opciones_file.add_command(label="Open...", command=open_file)
opciones_file.add_separator()
opciones_file.add_command(label="Save")
opciones_file.add_command(label="Save as..", state="disabled")
opciones_file.add_separator()
opciones_file.add_command(label="Project")


opciones_edit.add_command(label="Find")
opciones_edit.add_command(label="Replace")


ventana.mainloop()
