import tkinter as tk

ventana = tk.Tk()
ventana.geometry("500x150+10+10")

mi_frame = tk.Frame(ventana, background="white", width=100, height=50, relief="raised", borderwidth=2)
mi_frame.pack(side=tk.RIGHT)

"""
Se necesita investigar estos dos parametros de pack
mi_frame = tk.Frame(ventana, background="yellow", width=100, height=50, relief="raised", borderwidth=2)
mi_frame.pack(padx=10)

mi_frame = tk.Frame(ventana, background="blue", width=100, height=50, relief="raised", borderwidth=2)
mi_frame.pack(fill=tk.X)
"""

ventana.mainloop()
