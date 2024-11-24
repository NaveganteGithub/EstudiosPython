import tkinter as tk

ventana = tk.Tk()
ventana.geometry("750x480+0+0")

def cambiar():
    print("Antes", texto.get())
    texto.set("Mi texto")
    print("Despues", texto.get())

texto = tk.StringVar(value="Mi texto inicial") # StringVar

etiqueta = tk.Label(ventana, textvariable=texto)
etiqueta.pack()

boton = tk.Button(text="Mi boton", command=cambiar)
boton.pack()



# No tiene borde ademas no puedes agregarle una leyenda
frame = tk.Frame(ventana, background="yellow", height=50, width=50)
frame.pack()


# Tiene borde ademas de poder agregarle una leyenda

labelframe = tk.LabelFrame(ventana, background="blue", height=50, width=150, text="Leyenda", font="Arial", fg="white")
labelframe.pack()




foto = tk.PhotoImage(file=".\\..\\logo\\man.png")
etiqueta2 = tk.Label(ventana, image=foto)
etiqueta2.pack()



ventana.mainloop()
