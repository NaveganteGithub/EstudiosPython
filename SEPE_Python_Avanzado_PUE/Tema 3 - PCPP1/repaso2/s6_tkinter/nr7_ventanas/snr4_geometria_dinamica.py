import tkinter as tk

ventana = tk.Tk()

ancho_ventana = 1100
alto_ventana = 520
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

posicion_horizontal = int(ancho_pantalla / 2 - ancho_ventana / 2)
posicion_vertical = int(alto_pantalla / 2 - alto_ventana / 2)

ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_horizontal}+{posicion_vertical}")

ventana.mainloop()
