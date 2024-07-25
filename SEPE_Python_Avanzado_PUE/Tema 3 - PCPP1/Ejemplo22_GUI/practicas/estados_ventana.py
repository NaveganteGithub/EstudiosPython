import tkinter as tk


ventana = tk.Tk()
ventana.geometry("700x500+150+100")

def maximizar():
    ventana.state("zoomed")


boton = tk.Button(ventana, text="Maximizar ventana", command=maximizar)
boton.pack()


def minimizar():
    ventana.state("iconic")


boton = tk.Button(ventana, text="Minimizar ventana", command=minimizar)
boton.pack()


ventana.mainloop()
