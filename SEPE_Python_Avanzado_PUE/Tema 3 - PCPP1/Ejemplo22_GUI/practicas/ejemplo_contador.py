import tkinter as tk

ventana = tk.Tk()

ventana.title("Ejemplo de contador")
ventana.geometry("200x100+500+200")

def incrementar():
    global contador
    contador += 1
    valor_contador.set(contador)

def decrementar():
    global contador
    contador -= 1
    valor_contador.set(contador)


contador = 0

valor_contador = tk.StringVar(value=contador)
etiqueta = tk.Label(ventana, textvariable=valor_contador)
etiqueta.pack()

boton_incrementar = tk.Button(ventana, text="Incrementar", command=incrementar)
boton_incrementar.pack()
boton_decrementar = tk.Button(ventana, text="Decrementar", command=decrementar)
boton_decrementar.pack()

ventana.mainloop()
