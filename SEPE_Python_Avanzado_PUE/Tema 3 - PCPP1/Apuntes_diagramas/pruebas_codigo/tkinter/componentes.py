
import tkinter

ventana = tkinter.Tk()
ventana.geometry("1000x550+150+0")

boton = tkinter.Button(ventana, text="Mi boton")
boton.place(x=20, y=20)

etiqueta = tkinter.Label(ventana, text="Hola")
etiqueta.place(x=80, y=20)

caja_texto = tkinter.Entry(ventana)
caja_texto.place(x=20, y=60)

radio = tkinter.Radiobutton(ventana, name="radio", text="radio")
radio.place(x=20, y=80)

check = tkinter.Checkbutton(ventana, name="license", text="License")
check.place(x=20, y=120)


texto_dinamico = tkinter.StringVar(value="Hola")
etiqueta_dinamica = tkinter.Label(ventana, textvariable=texto_dinamico)


def cambiar_texto():
    texto_actual = texto_dinamico.get()
    if texto_actual == "Hola":
        texto_dinamico.set("Adios")
    else:
        texto_dinamico.set("Hola")


boton_comando = tkinter.Button(ventana, text="Cambiar el texto", command=cambiar_texto)

etiqueta_dinamica.place(x=20, y=140)
boton_comando.place(x=60, y=140)

contenedor = tkinter.LabelFrame(ventana, width=200, height=200, text="Genero", borderwidth=5)
contenedor.place(x=200, y=20)

radio_man = tkinter.Radiobutton(contenedor, text="Hombre", value="H")
radio_wom = tkinter.Radiobutton(contenedor, text="Mujer", value="M")
radio_man.place(x=10, y=10)
radio_wom.place(x=10, y=40)

ventana.mainloop()
