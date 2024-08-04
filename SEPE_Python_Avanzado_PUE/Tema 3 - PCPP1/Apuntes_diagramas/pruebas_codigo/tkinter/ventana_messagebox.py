import tkinter
from tkinter import messagebox

ventana = tkinter.Tk()
ventana.geometry("750x550+150+0")


def informacion():
    info = messagebox.showinfo(title="Informacion", message="Hola hola")
    print(info)  # ok


def pregunta():
    info = messagebox.askquestion(title="Pregunta", message="¿Estas activo?")
    print(info)  # False


def pregunta_2():
    info = messagebox.askyesno(title="Pregunta", message="¿Estas activo?")
    print(info)  # True


def pregunta_3():
    info = messagebox.askokcancel(title="Pregunta", message="¿Estas activo?")
    print(info)  # True


def pregunta_4():
    info = messagebox.askretrycancel(title="¿Reintento?", message="¿Quieres volver a intentarlo?")
    print(info)  # True


def pregunta_5():
    info = messagebox.showwarning(title="Peligro", message="Peligro de contaminacion externa")
    print(info)  # True


def pregunta_6():
    info = messagebox.showerror(title="Error", message="Fallo total, apagando sistema")
    print(info)  # True


boton_1 = tkinter.Button(ventana, text="Informacion", command=informacion)
boton_1.pack()

boton_2 = tkinter.Button(ventana, text="Pregunta", command=pregunta)
boton_2.pack()

boton_3 = tkinter.Button(ventana, text="Si o No", command=pregunta_2)
boton_3.pack()

boton_4 = tkinter.Button(ventana, text="Vale o Cancelar", command=pregunta_3)
boton_4.pack()

boton_5 = tkinter.Button(ventana, text="Reintentar o Cancelar", command=pregunta_4)
boton_5.pack()

boton_6 = tkinter.Button(ventana, text="Aviso", command=pregunta_5)
boton_6.pack()

boton_7 = tkinter.Button(ventana, text="Peligro", command=pregunta_6)
boton_7.pack()

ventana.mainloop()
