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


hombre = tkinter.StringVar(value="Hombre")
mujer = tkinter.StringVar(value="Mujer")
opcion1 = tkinter.Radiobutton(caja, textvariable=hombre, value="O1", background="yellow")
opcion1.place(x=10, y=10)
opcion2 = tkinter.Radiobutton(caja, textvariable=mujer, value="O2", background="yellow")
opcion2.place(x=10, y=80)


lista_multiple = tkinter.Listbox(ventana, selectmode="multiple")
lista_multiple.insert(tkinter.END, "--Seleccione--", "Rojo", "Amarillo", "Purpura", "Azul", "Blanco")
lista_multiple.place(x=260, y=10)

lista = ["Rojo", "Amarillo", "Purpura", "Azul", "Blanco"]
menu = tkinter.OptionMenu(ventana, tkinter.StringVar(), *lista)
menu.place(x=260, y=200)

from tkinter import ttk
lista_desplegable = ttk.Combobox(ventana, values=["Rojo", "Amarillo", "Purpura", "Azul", "Blanco"])
lista_desplegable.current(0) # Opcion por defecto
lista_desplegable.place(x=260, y=300)

ventana.mainloop()
