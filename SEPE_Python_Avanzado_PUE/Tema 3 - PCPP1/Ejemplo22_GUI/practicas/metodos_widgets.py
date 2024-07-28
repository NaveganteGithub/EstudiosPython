import tkinter as tk

ventana = tk.Tk()
ventana.geometry("500x500+150+150")


def mi_boton():
    boton.config(background="black")


boton = tk.Button(ventana, text="Prueba", background="white")
boton.after(5000, mi_boton)
boton.bind("<Button-1>", lambda e: boton.config(background="white"))
boton.pack()

ventana.mainloop()
