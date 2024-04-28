import tkinter as tk

def cerrar_ventana():
    ventana.destroy()

ventana = tk.Tk()

ventana.title("Ejemplo de los metodos messagebox")
ventana.geometry('400x600+500+200')

ventana.tk.call("wm", "iconphoto", ventana, tk.PhotoImage(file='logo/man.png'))

ventana.minsize(width="500", height="300")
ventana.maxsize(width="1280", height="720")

ventana.resizable(width=False, height=False)

# boton = tk.Button(ventana, text="cerrar", command=cerrar_ventana) # Opcion 1
# boton = tk.Button(ventana, text="cerrar", command=ventana.destroy) # Opcion 2
boton = tk.Button(ventana, text="cerrar")
boton.bind("<Button-1>", lambda e: ventana.destroy())
boton.pack()




ventana.mainloop()