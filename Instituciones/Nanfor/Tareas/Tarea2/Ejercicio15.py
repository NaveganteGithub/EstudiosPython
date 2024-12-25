from tkinter import *

mi_ventana = Tk()

mi_ventana.title("Aviso de infección")
mi_ventana.geometry('720x480')
mi_ventana.anchor('center')

texto = Label(mi_ventana, text="Tu PC ha sido infectado por un virus", font={"Arial", 20})
texto.grid(column=0,row=0,columnspan=2)

def cerrar_ventana():
    mi_ventana.destroy()

boton_aceptar = Button(mi_ventana, text="Aceptar", font={"Arial", 15})
boton_cancelar = Button(mi_ventana, text="Cancelar", font={"Arial", 15}, command=cerrar_ventana)

boton_aceptar.grid(column=0, row=1, pady=10)
boton_cancelar.grid(column=1, row=1, pady=10)

mainloop()