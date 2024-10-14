import tkinter as tk


ventana = tk.Tk()
ventana.geometry("700x500+150+100")

def maximizar():
    ventana.state("zoomed")


boton = tk.Button(ventana, text="Maximizar ventana", command=maximizar)
boton.pack()


def minimizar():
    ventana.state("iconic")


boton = tk.Button(ventana, text="Minimizar ventana", command=minimizar)
boton.pack()


# Puedes utilizar el Administrador de Tareas de Windows para ver los procesos
# en segundo plano, el proceso en segundo plano de este script se llama "Python",
# puedes finalizarlo si quieres desde el administrador de tareas
def segundo_plano():
    ventana.state("withdrawn")


boton = tk.Button(ventana, text="Segundo Plano", command=segundo_plano)
boton.pack()


def normal():
    ventana.state("normal")


boton = tk.Button(ventana, text="Por defecto", command=normal)
boton.pack()


ventana.mainloop()
