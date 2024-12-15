import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()

def panel():
    dato = messagebox.showinfo("Calculadora presupuesto", "Te has pasado un numero")
    print(dato)  # ok

def pregunta():
    dato = messagebox.askquestion("Pregunta", "¿Eres mayor de edad?")
    print(dato)  # yes/no

def respuesta_yesno():
    dato = messagebox.askyesno("Pregunta Si o No", "¿Eres mayor de edad?")
    print(dato)  # True/False

def respuesta_yesnocancel():
    dato = messagebox.askyesnocancel("Pregunta Si, No o Cancelar", "¿Eres mayor de edad?")
    print(dato)  # True/False/None

def respuesta_okcancel():
    dato = messagebox.askokcancel("Pregunta Ok o Cancel", "¿Quieres continuar?")
    print(dato)  # True/False

def respuesta_retrycancel():
    dato = messagebox.askretrycancel("Reintento", "¿Quieres reintentar?")
    print(dato)  # True/False

def advertencia():
    dato = messagebox.showwarning("Advertencia", "¿Se te acaba la memoria RAM?")
    print(dato)  # ok

def error():
    dato = messagebox.showerror("Error", "Consumo elevado de memoria, reiniciando equipo.")
    print(dato)  # ok

boton = ttk.Button(ventana, text="showinfo", command=panel)
boton.pack()

boton = ttk.Button(ventana, text="askquestion", command=pregunta)
boton.pack()

boton = ttk.Button(ventana, text="askyesno", command=respuesta_yesno)
boton.pack()

boton = ttk.Button(ventana, text="askyesnocancel", command=respuesta_yesnocancel)
boton.pack()

boton = ttk.Button(ventana, text="askokcancel", command=respuesta_okcancel)
boton.pack()

boton = ttk.Button(ventana, text="askretrycancel", command=respuesta_retrycancel)
boton.pack()

boton = ttk.Button(ventana, text="showwarning", command=advertencia)
boton.pack()

boton = ttk.Button(ventana, text="showerror", command=error)
boton.pack()

ventana.mainloop()
