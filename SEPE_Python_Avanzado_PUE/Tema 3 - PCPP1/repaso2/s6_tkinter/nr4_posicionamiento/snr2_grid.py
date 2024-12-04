import tkinter as tk

ventana = tk.Tk()
ventana.geometry("260x120+40+30")

etiqueta1 = tk.Label(ventana, text="Etiqueta 1")
etiqueta2 = tk.Label(ventana, text="Etiqueta 2")
etiqueta3 = tk.Label(ventana, text="Etiqueta 3")
etiqueta4 = tk.Label(ventana, text="Etiqueta 4")
etiqueta5 = tk.Label(ventana, text="Etiqueta 5")
etiqueta6 = tk.Label(ventana, text="Etiqueta 6")
etiqueta7 = tk.Label(ventana, text="Etiqueta 7")
etiqueta8 = tk.Label(ventana, text="Etiqueta 8")
etiqueta9 = tk.Label(ventana, text="Etiqueta 9")
etiqueta10 = tk.Label(ventana, text="Etiqueta 10")
etiqueta11 = tk.Label(ventana, text="Etiqueta 11")

etiqueta1.grid(row=0, column=0)
etiqueta2.grid(row=0, column=1)
etiqueta3.grid(row=0, column=2)
etiqueta4.grid(row=0, column=3)
etiqueta5.grid(row=1, column=0)
etiqueta6.grid(row=1, column=1)
etiqueta7.grid(row=1, column=2)
etiqueta8.grid(row=1, column=3)
etiqueta9.grid(row=2, column=0, rowspan=2)  # Etiqueta de dos filas de alto
etiqueta10.grid(row=2, column=1, columnspan=3)  # Etiqueta de tres columnas de ancho
etiqueta11.grid(row=3, column=1)

ventana.mainloop()
