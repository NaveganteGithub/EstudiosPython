from tkinter import *
import random

mi_ventana = Tk()

mi_ventana.title("Numero aleatorio")

mi_ventana.geometry('1280x720')

texto = Label(mi_ventana, text="00", font={"Arial", 20})

texto.grid(column=0,row=0)

def numero_aleatorio():
    numero = str(random.randrange(0,20)).zfill(2)
    texto = Label(mi_ventana, text=numero, font={"Arial", 20})
    texto.grid(column=0,row=0)

boton = Button(mi_ventana, text = "Generar numero", command = numero_aleatorio)

boton.grid(column=0, row=1)

mainloop()