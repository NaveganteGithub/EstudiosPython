import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("480x480+0+0")
ventana.config(padx=10, pady=10)


# Un cuadrado con un listado de opciones que podemos elegir
lista = tk.Listbox(ventana, selectmode="multiple")  # browse, multiple
lista.insert(tk.END, "Rojo", "Amarillo", "Verde")
lista.place(x=10, y=40)

# Una caja con un botón que podemos usar para desplegar
# la lista de opciones que tenemos disponibles
valor_por_defecto = tk.StringVar(value="Seleccione")
valores = ["Rojo", "Amarillo", "Verde"]
menu_opciones = tk.OptionMenu(ventana, valor_por_defecto, *valores)
menu_opciones.place(x=150, y=240)

# Una lista desplegable simple
combo = ttk.Combobox(ventana, values=["Rojo", "Amarillo", "Verde"])
combo.current(0)
combo.place(x=200, y=330)

################### RECURSOS GRÁFICOS ###################
etiqueta1 = tk.Label(ventana, text="Hola")
etiqueta2 = tk.Label(ventana, text="Que")
etiqueta3 = tk.Label(ventana, text="Tal")
etiqueta1.place(x=10, y=10)
etiqueta2.place(x=150, y=220)
etiqueta3.place(x=200, y=300)

ventana.mainloop()
