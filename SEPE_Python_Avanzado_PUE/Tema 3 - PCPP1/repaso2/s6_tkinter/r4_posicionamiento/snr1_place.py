import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("240x120+50+20")

etiqueta1 = ttk.Label(ventana, text="Etiqueta 1")
etiqueta1.place(x=20, y=20)
etiqueta2 = ttk.Label(ventana, text="Etiqueta 2")
etiqueta2.place(x=75, y=50)
etiqueta3 = ttk.Label(ventana, text="Etiqueta 3")
etiqueta3.place(x=134, y=80)

ventana.mainloop()
