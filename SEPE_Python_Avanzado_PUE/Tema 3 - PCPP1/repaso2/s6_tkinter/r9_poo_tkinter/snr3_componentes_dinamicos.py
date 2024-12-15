import tkinter as tk
from tkinter import ttk

class Ventana:
# https://recursospython.com/guias-y-manuales/panel-de-pestanas-notebook-tkinter/

    def __init__(self):
        self.panel = None
        self.tabs = list()
        self.mi_ventana = tk.Tk()

    def crear_panel(self):
        self.panel = ttk.Notebook(self.mi_ventana)
        self.panel.place(x=20, y=20)

    def agregar_tab(self):

        def comando_add_tab():
            tab = ttk.Frame(self.panel)
            self.tabs.append(tab)
            self.panel.add(tab, text="Pestaña")

        boton = ttk.Button(self.mi_ventana, text="Agregar pestaña", command=comando_add_tab)
        boton.place(x=100, y=100)

    def delete_tab(self):

        def comando_del_tab():
            tab = self.tabs.pop()
            self.panel.hide(tab)

        boton = ttk.Button(self.mi_ventana, text="Eliminar pestaña", command=comando_del_tab)
        boton.place(x=100, y=140)

    def arrancar_ventana(self):
        self.mi_ventana.mainloop()

ventana = Ventana()
ventana.crear_panel()
ventana.agregar_tab()
ventana.delete_tab()
ventana.arrancar_ventana()
