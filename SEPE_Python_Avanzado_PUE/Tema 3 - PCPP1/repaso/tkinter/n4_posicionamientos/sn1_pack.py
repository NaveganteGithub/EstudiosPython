import tkinter

ventana = tkinter.Tk()
ventana.title("Posicionamientos - Pack por Lados")
ventana.geometry("550x550+40+0")

etiqueta1 = tkinter.Label(ventana, text="Etiqueta 1")
etiqueta1.pack(side=tkinter.TOP)
etiqueta2 = tkinter.Label(ventana, text="Etiqueta 2")
etiqueta2.pack(side=tkinter.RIGHT)
etiqueta3 = tkinter.Label(ventana, text="Etiqueta 3")
etiqueta3.pack(side=tkinter.LEFT)
etiqueta4 = tkinter.Label(ventana, text="Etiqueta 4")
etiqueta4.pack(side=tkinter.BOTTOM)
etiqueta5 = tkinter.Label(ventana, text="Etiqueta 5")
etiqueta5.pack(side=tkinter.BOTTOM)

ventana.mainloop()
