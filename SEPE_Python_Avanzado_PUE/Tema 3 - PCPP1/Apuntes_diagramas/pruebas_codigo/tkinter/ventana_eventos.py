
import tkinter

ventana = tkinter.Tk()
ventana.configure(background="yellow")
ventana.geometry("750x500+150+100")

contenedor = tkinter.LabelFrame(ventana, width=200, height=200, background="black", borderwidth=5)
contenedor.place(x=200, y=100)


def actuar_evento(e):
    print("Hemos recibido el evento", e, e.x, e.y)


def actuar_evento_2(e):
    print("Hemos recibido el evento 2", e, e.x, e.y)


def entrada(e):
    print("Hemos entrado")


def salida(e):
    print("Hemos salido")


# Recomendable no utilizar <Button-1> y <Double 1> a la vez saltan al instante
# contenedor.bind("<Button-1>", actuar_evento)
contenedor.bind("<Button-2>", actuar_evento)
contenedor.bind("<Button-3>", actuar_evento)

contenedor.bind("<Double 1>", actuar_evento_2)

contenedor.bind("<Leave>", salida)
contenedor.bind("<Enter>", entrada)

# ventana.bind("<Key>", actuar_evento)

caja1 = tkinter.Entry(ventana, width=50)
caja2 = tkinter.Entry(ventana, width=50)

caja2.focus()

caja1.bind("<FocusIn>", lambda e: print("Enfocada caja 1", e))
caja1.bind("<FocusOut>", lambda e: print("Desenfocada caja 1", e))

caja1.pack()
caja2.pack()

ventana.mainloop()
