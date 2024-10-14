import tkinter

ventana_principal = tkinter.Tk()
ventana_principal.geometry("750x750+10+0")

def mi_ventana_secundaria():
    ventana_secundaria = tkinter.Toplevel(ventana_principal)
    ventana_secundaria.geometry("550x500+10+0")

boton = tkinter.Button(ventana_principal, text="Abrir ventana", command=mi_ventana_secundaria)
boton.pack()

boton = tkinter.Button(ventana_principal, text="Cerrar ventana principal", command=lambda: ventana_principal.destroy())
boton.pack()

ventana_principal.mainloop()
