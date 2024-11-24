import tkinter as tk

ventana = tk.Tk()

boton = tk.Button(ventana, text="Mi boton")
boton.pack()

texto = tk.Label(ventana, text="Mi texto")
texto.pack()

caja = tk.Entry(ventana)
caja.pack()

radio = tk.Radiobutton(ventana)

ventana.mainloop()
