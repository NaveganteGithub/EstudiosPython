from tkinter import Tk
from tkinter import messagebox
from tkinter import Button

"""
Los valores de la ventana que devuelven pueden ser True, False o None
"""

ventana = Tk()
ventana.geometry("750x750+50+0")

def informacion():
    resultado = messagebox.showinfo("Mensaje", "Este es el cuerpo del mensaje")
    print(resultado)

def pregunta():
    resultado = messagebox.askquestion("Accion", "¿Quieres ejecutar esta accion?")
    print(resultado)

def pregunta_si_no():
    resultado = messagebox.askyesno("Accion", "¿Quieres ejecutar esta accion?")
    print(resultado)

def pregunta_ok_cancel():
    resultado = messagebox.askokcancel("Accion", "¿Quieres ejecutar esta accion?")
    print(resultado)

def pregunta_retry_cancel():
    resultado = messagebox.askretrycancel("Accion", "¿Quieres ejecutar esta accion?")
    print(resultado)

def informacion_advertencia():
    resultado = messagebox.showwarning("Advertencia", "Estas sobrecalentando el PC")
    print(resultado)

def informacion_error():
    resultado = messagebox.showerror("ERROR", "RAM llena")
    print(resultado)

def pregunta_yes_no_cancel():
    resultado = messagebox.askyesnocancel("Accion", "¿Quieres seguir?")
    print(resultado) # El cancel de aqui devuelve None

boton_1 = Button(ventana, text="Boton 1", width=20, command=informacion)
boton_2 = Button(ventana, text="Boton 2", width=20, command=pregunta)
boton_3 = Button(ventana, text="Boton 3", width=20, command=pregunta_si_no)
boton_4 = Button(ventana, text="Boton 4", width=20, command=pregunta_ok_cancel)
boton_5 = Button(ventana, text="Boton 5", width=20, command=pregunta_retry_cancel)
boton_6 = Button(ventana, text="Boton 6", width=20, command=informacion_advertencia)
boton_7 = Button(ventana, text="Boton 7", width=20, command=informacion_error)
boton_8 = Button(ventana, text="Boton 8", width=20, command=pregunta_yes_no_cancel)

boton_1.pack()
boton_2.pack()
boton_3.pack()
boton_4.pack()
boton_5.pack()
boton_6.pack()
boton_7.pack()
boton_8.pack()

ventana.mainloop()
