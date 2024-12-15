import tkinter as tk

class Ventana:

    def __init__(self):
        self.mi_ventana = tk.Tk()

    def insertar_boton(self):
        boton = tk.Button(self.mi_ventana, text="Hola")
        boton.place(x=50, y=50)

    def iniciar_ventana(self):
        self.mi_ventana.mainloop()


ventana = Ventana()
ventana.insertar_boton()
ventana.iniciar_ventana()
