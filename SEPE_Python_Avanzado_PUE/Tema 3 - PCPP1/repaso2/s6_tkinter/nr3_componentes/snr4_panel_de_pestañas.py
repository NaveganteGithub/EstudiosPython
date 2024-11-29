import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("280x150+0+0")

notebook = ttk.Notebook(ventana)

pestana = ttk.Frame(notebook)

etiqueta = ttk.Label(pestana, text="Etiqueta dentro de la pestaña")
boton = ttk.Button(pestana, text="Boton dentro de la pestaña")
etiqueta.pack()
boton.pack()

pestana2 = ttk.Frame()
etiqueta = ttk.Label(pestana2, text="Etiqueta dentro de la pestaña 2")
etiqueta.pack()

notebook.add(pestana, text="Pestaña 1", padding=10)
notebook.add(pestana2, text="Pestaña 2", padding=10)
notebook.pack()

ventana.mainloop()
