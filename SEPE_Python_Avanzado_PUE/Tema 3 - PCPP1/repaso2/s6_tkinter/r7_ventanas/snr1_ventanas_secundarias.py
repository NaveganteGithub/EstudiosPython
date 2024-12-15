import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

def abrir_ventana():
    ventana_secundaria = tk.Toplevel(ventana)
    ventana_secundaria.mainloop()

boton = ttk.Button(ventana, text="Abrir ventana", command=abrir_ventana)
boton.pack()

ventana.mainloop()
