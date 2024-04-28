import tkinter as tk
from tkinter import messagebox

# crear una nueva ventana

ventana = tk.Tk()

# Asignarle un titulo

ventana.title("Ejemplo de eventos")

"""def pulsar():
    messagebox.showinfo("Detalle", "Has pulsado el boton")"""

def pulsar(event=None):
    messagebox.showinfo("Detalle", "Has pulsado el boton")

# Agregar boton a la ventana

boton = tk.Button(ventana, text='Pulsame', command=pulsar)
boton.place(x=10, y=20)




def pregunta(event=None):
    respuesta = messagebox.askquestion("Pregunta", "Cerramos la ventana?")
    print("Has elegido yes" if respuesta == "yes" else "Has elegido no")

# Agregar boton a la ventana

boton_2 = tk.Button(ventana, text='Pregunta', command=pregunta)
boton_2.place(x=10, y=80)


# mostrar la ventana
ventana.mainloop()