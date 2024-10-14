import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Ejemplo de los metodo messagebox")
ventana.geometry('300x300')


def boton_info():
    respuesta = messagebox.showinfo("Titulo", "Mensaje de informacion")
    print(respuesta)

def boton_askyesno():
    respuesta = messagebox.askyesno("Titulo", "Estas de acuerdo?")
    print(respuesta)


def boton_askokcancel():
    respuesta = messagebox.askokcancel("Titulo", "Estas seguro que lo quieres eliminar?")
    print(respuesta)

def boton_askretrycancel():
    respuesta = messagebox.askretrycancel("Titulo", "Ha habido un problema")
    print(respuesta)

def boton_askquestion():
    respuesta = messagebox.askquestion("Titulo", "Cerramos ventana?", icon="question")
    print(respuesta)

def boton_showerror():
    respuesta = messagebox.showerror("Titulo", "Error grave")
    print(respuesta)

def boton_show_warning():
    respuesta = messagebox.showwarning("Titulo", "Mensaje de aviso")
    print(respuesta)

boton_info = tk.Button(ventana, text='info', command=boton_info)
boton_info.pack()

boton_si_no = tk.Button(ventana, text='askyesno', command=boton_askyesno)
boton_si_no.pack()

boton_cancel = tk.Button(ventana, text='askokcancel', command=boton_askokcancel)
boton_cancel.pack()

boton_retry = tk.Button(ventana, text='askretrycancel', command=boton_askretrycancel)
boton_retry.pack()

boton_retry = tk.Button(ventana, text='askquestion', command=boton_askquestion)
boton_retry.pack()

boton_error = tk.Button(ventana, text='showerror', command=boton_showerror)
boton_error.pack()

boton_error = tk.Button(ventana, text='showwarning', command=boton_show_warning)
boton_error.pack()

ventana.mainloop()
