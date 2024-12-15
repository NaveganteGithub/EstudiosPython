import tkinter as tk

class Ventana:

    def __init__(self):
        self.mi_ventana = tk.Tk()

    def insertar_boton(self, horizontal: int, vertical: int):
        boton = tk.Button(self.mi_ventana, text="Hola")
        boton.place(x=horizontal, y=vertical)

    def iniciar_ventana(self):
        self.mi_ventana.mainloop()


ventana = Ventana()

# Colocar los tres botones en diagonal
# 10 al 30 salto 10
# 10 al 60 salto 20
# 10 al 90 salto 30
for posicion in range(10, 90 + 10, 30):
    ventana.insertar_boton(posicion, posicion)

ventana.iniciar_ventana()

