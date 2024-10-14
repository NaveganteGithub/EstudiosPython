import tkinter as tk
from tkinter import filedialog

ventana = tk.Tk()
ventana.geometry("700x500+100+100")


def boton_capturar_nombre_archivo():
    respuesta = filedialog.askopenfilename()
    print("askopenfilename", respuesta)
    return respuesta


def boton_capturar_nombres_archivos():
    respuesta = filedialog.askopenfilenames()
    print("askopenfile", respuesta)
    return respuesta


def boton_capturar_nombre_directorio():
    respuesta = filedialog.askdirectory()
    print("askdirectory", respuesta)
    return respuesta


def boton_abrir_archivo():
    respuesta = filedialog.askopenfile()
    print("askopenfile", respuesta)
    return respuesta


def boton_abrir_archivos():
    respuesta = filedialog.askopenfiles()
    # askopenfiles [<_io.TextIOWrapper name='ruta_absoluta/archivo_prueba.txt' mode='r' encoding='cp1252'>]
    print("askopenfiles", respuesta)
    return respuesta


def boton_guardar_archivo():
    respuesta = filedialog.asksaveasfile()
    # askopenfiles [<_io.TextIOWrapper name='ruta_absoluta/archivo_prueba.txt' mode='r' encoding='cp1252'>]
    print("askopenfiles", respuesta)
    return respuesta


def boton_guardar_archivos():
    respuesta = filedialog.asksaveasfilename()
    # askopenfiles C:/Users/ismae/PycharmProjects/EstudiosPython/SEPE_Python_Avanzado_PUE/Tema 3 - PCPP1/Ejemplo22_GUI/practicas/rewr.txt
    print("askopenfiles", respuesta)
    return respuesta


boton_archivo = tk.Button(ventana, text="askopenfilename", command=boton_capturar_nombre_archivo)
boton_archivo.pack()

boton_archivo = tk.Button(ventana, text="askopenfilenames", command=boton_capturar_nombres_archivos)
boton_archivo.pack()

boton_archivo = tk.Button(ventana, text="askdirectory", command=boton_capturar_nombre_directorio)
boton_archivo.pack()

boton_archivo = tk.Button(ventana, text="askopenfile", command=boton_abrir_archivo)
boton_archivo.pack()

boton_archivo = tk.Button(ventana, text="askopenfiles", command=boton_abrir_archivos)
boton_archivo.pack()

boton_archivo = tk.Button(ventana, text="asksaveasfile", command=boton_guardar_archivo)
boton_archivo.pack()

boton_archivo = tk.Button(ventana, text="asksaveasfilename", command=boton_guardar_archivos)
boton_archivo.pack()

ventana.mainloop()
