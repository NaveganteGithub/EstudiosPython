import tkinter

ventana = tkinter.Tk()
ventana.geometry("750x750+50+0")
ventana.title("Componentes")
ventana.config(padx=30, pady=30)

boton = tkinter.Button(ventana, width=20, text="Boton")
boton.place(x=10, y=10)

etiqueta = tkinter.Label(ventana, text="Mi etiqueta")
etiqueta.place(x=10, y=50)

entrada = tkinter.Entry(ventana, width=20)
entrada.place(x=10, y=90)

radio = tkinter.Radiobutton(ventana, text="Eleccion")
radio.place(x=10, y=130)

check = tkinter.Checkbutton(ventana, text="Licencia")
check.place(x=10, y=170)

texto = tkinter.StringVar(value="Mi texto")
etiqueta2 = tkinter.Label(textvariable=texto)
etiqueta2.place(x=10, y=210)

caja = tkinter.LabelFrame(ventana, width=200, height=200, background="yellow")
caja.place(x=10, y=250)

ventana.mainloop()
