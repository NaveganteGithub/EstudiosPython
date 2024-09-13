import tkinter

ventana = tkinter.Tk()
ventana.geometry("750x750+50+0")


################################################################################################

texto = tkinter.StringVar(value="Esperando acción")

def mi_evento(event = None):
    texto.set("Hola")

boton = tkinter.Button(ventana, width=20, text="Saludar", command=mi_evento)
boton.place(x=10, y=10)

etiqueta = tkinter.Label(ventana, textvariable=texto)
etiqueta.place(x=10, y=40)

################################################################################################


def tipos_eventos_raton(event = None):

    if event is None:
        raise RuntimeError from Exception("El evento no ha sido declarado en event")

    match event.num:
        case 1: # Los eventos de tipo Double y Button- tienen el mismo identificador
            print("Has pulsado el boton izquierdo del raton en las coordenadas: X =", event.x, "; Y =", event.y)
        case 2:
            print("Has pulsado el boton central del raton en las coordenadas: X =", event.x, "; Y =", event.y)
        case 3:
            print("Has pulsado el boton derecho del raton en las coordenadas: X =", event.x, "; Y =", event.y)
        case _:
            raise RuntimeError from Exception("Se ha ejecutado un evento no identificado")

caja = tkinter.LabelFrame(ventana, width=150, height=150, background="yellow", border=2)
caja.place(x=10, y=90)

caja.bind("<Button-1>", tipos_eventos_raton)
caja.bind("<Button-2>", tipos_eventos_raton)
caja.bind("<Button-3>", tipos_eventos_raton)
# caja.bind("<Double 1>", tipos_eventos_raton)

################################################################################################

def evento_entrada(event):
    print("Has entrado al frame en la coordenada X =", event.x, "Y =", event.y)

def evento_salida(event):
    print("Has entrado al frame por la coordenada X =", event.x, "Y =", event.y)

caja.bind("<Enter>", evento_entrada)
caja.bind("<Leave>", evento_salida)

################################################################################################

def tecla_pulsada(event):
    print(event.send_event, event.state, event.keysym, event.keycode, event.char, event.x, event.y)
    print("Has pulsado la tecla", event.char)

"""entrada = tkinter.Entry(ventana, width=50)
entrada.place(x=10, y=280)
entrada.bind("<Key>", tecla_pulsada)"""

# ventana.bind("<Key>", tecla_pulsada)

################################################################################################

# Los focos son objetos dentro de los widgets que a su vez son objetos

"""def foco(event = None):
    if event is not None:
        if boton1.focus_get() is boton1: # Pide el foco del boton 1 si lo tiene si no lo tiene None
            print("Boton 1 enfocado")"""

boton1 = tkinter.Button(ventana, text="Boton 1")
boton2 = tkinter.Button(ventana, text="Boton 2")
boton1.place(x=500, y=10)
boton2.place(x=500, y=40)

"""boton1.bind("<FocusIn>", foco)
boton2.bind("<FocusIn>", foco)
boton1.bind("<FocusOut>", foco)
boton2.bind("<FocusOut>", foco)"""

boton1.bind("<FocusIn>", lambda e: print("Boton 1 enfocado", e))
boton2.bind("<FocusIn>", lambda e: print("Boton 2 enfocado", e))
boton1.bind("<FocusOut>", lambda e: print("Boton 1 desenfocado", e))
boton2.bind("<FocusOut>", lambda e: print("Boton 2 desenfocado", e))

boton1.focus_set()

################################################################################################

# No hace falta el parametro del event
ventana.after(1000, lambda: print("Bienvenido"))

ventana.mainloop()
