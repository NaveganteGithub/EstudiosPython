import tkinter as tk
from tkinter import ttk, filedialog

ventana = tk.Tk()

def archivo():
    lectura = filedialog.askopenfile(title="Abrir archivo", mode="r")
    print(lectura) # Objeto InputOutput

def archivos():
    lectura = filedialog.askopenfiles(title="Abrir archivos", mode="r")
    print(lectura)  # Lista de objetos InputOutput

def path():
    ruta = filedialog.askopenfilename(title="Abrir archivo")
    print(ruta)  # Ruta en String

def paths():
    ruta = filedialog.askopenfilenames(title="Abrir archivos")
    print(ruta)  # Lista de String con rutas

def salvar_archivo():
    ruta = filedialog.asksaveasfile(title="Guardar archivo")
    print(ruta)  # Objeto Output

def salvar_nombre():
    ruta = filedialog.asksaveasfilename(title="Guardar archivo")
    print(ruta)  # Ruta en String

def directorio():
    ruta = filedialog.askdirectory(title="Apuntar directorio")
    print(ruta)  # Ruta en String del directorio

boton = ttk.Button(ventana, text="Abrir archivo", command=archivo)
boton.pack()

boton = ttk.Button(ventana, text="Abrir archivos", command=archivos)
boton.pack()

boton = ttk.Button(ventana, text="Obtener ruta", command=path)
boton.pack()

boton = ttk.Button(ventana, text="Obtener rutas", command=paths)
boton.pack()

# Aquí antes de dar al botón de guardar, te sale una ventana emergente que
# dice que lo va a sobreescribir, pero porque los saves ofrecen objetos de
# escritura
boton = ttk.Button(ventana, text="Salvar archivo", command=salvar_archivo)
boton.pack()

boton = ttk.Button(ventana, text="Salvar nombre", command=salvar_nombre)
boton.pack()

boton = ttk.Button(ventana, text="Directorio", command=directorio)
boton.pack()

ventana.mainloop()
