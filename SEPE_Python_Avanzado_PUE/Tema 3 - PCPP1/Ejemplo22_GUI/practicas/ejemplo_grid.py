import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo Grid")
ventana.geometry("300x400")

etiqueta_1 = tk.Label(ventana, text="label 1")
etiqueta_2 = tk.Label(ventana, text="label 2")
etiqueta_3 = tk.Label(ventana, text="label 3")
etiqueta_4 = tk.Label(ventana, text="label 4")
# etiqueta_5 = tk.Label(ventana, text="label 5")
etiqueta_6 = tk.Label(ventana, text="label 6")
etiqueta_7 = tk.Label(ventana, text="label 7")

etiqueta_1.grid(row=0, column=0)
etiqueta_2.grid(row=0, column=1, rowspan=2)
etiqueta_3.grid(row=0, column=2)
etiqueta_4.grid(row=1, column=0)
# etiqueta_5.grid(row=1, column=1)
etiqueta_6.grid(row=1, column=2)
etiqueta_7.grid(row=2, column=0, columnspan=3)

ventana.mainloop()
