import tkinter as tk

ventana = tk.Tk()
ventana.geometry("500x500+150+150")


boton = tk.Button(ventana, text="Prueba", background="white", state="disabled")  # "normal", "active", "disabled"
boton.pack()

caja_texto = tk.Entry(ventana, width=50, state="readonly")  # "normal", "disabled", "readonly"
caja_texto.pack()

etiqueta = tk.Label(ventana, text="Prueba", state="disabled")  # "normal", "active", "disabled"
etiqueta.pack()

check = tk.Checkbutton(ventana, text="Prueba", state="active")  # "normal", "active", "disabled"
check.pack()

check = tk.Radiobutton(ventana, text="Prueba", state="active")  # "normal", "active", "disabled"
check.pack()

canvas = tk.Canvas(ventana, state="disabled")  # "normal", "disabled"
canvas.pack()

ventana.mainloop()
