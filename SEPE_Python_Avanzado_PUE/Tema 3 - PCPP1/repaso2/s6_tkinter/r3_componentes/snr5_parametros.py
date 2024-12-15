import tkinter as tk

def comando():
    print("Hola")

ventana = tk.Tk()
ventana.geometry("1280x1080+50+10")

# Propiedades
boton_texto = tk.Button(ventana, text="Hola")  # Asignar un texto al botón
boton_ejecutar = tk.Button(ventana, text="Comando", command=comando)  # Asignar un comando al botón
boton_ancho = tk.Button(ventana, text="Ancho del botón", width=7)  # Asignar una longitud al botón
boton_altura = tk.Button(ventana, text="Altura del botón", height=5)  # Asignar una altura al botón

# Asignar a botón el estado ...
boton_estado_activo = tk.Button(ventana, text="Activo", state=tk.ACTIVE)  # activo
boton_estado_normal = tk.Button(ventana, text="Normal", state=tk.NORMAL)  # normal (por defecto)
boton_estado_desactivado = tk.Button(ventana, text="Deshabilitado", state=tk.DISABLED)  # Desactivado

# Estilos
boton_color_fondo = tk.Button(ventana, text="Color de fondo", background="blue")  # Color de fondo para el botón
boton_color_texto = tk.Button(ventana, text="Color de texto", foreground="green")  # Color de la letra del botón
boton_fuente_texto = tk.Button(ventana, text="Fuente de letra", font=("Arial", 12))  # Fuente de la letra

# Control de bordes
ancho_borde_boton = tk.Button(ventana, text="Grosor de borde", borderwidth=4)
boton_borde_levantado = tk.Button(ventana, text="Borde levantado", relief=tk.RAISED)
boton_borde_hundido = tk.Button(ventana, text="Borde hundido", relief=tk.SUNKEN)
boton_borde_plano = tk.Button(ventana, text="Borde plano", relief=tk.FLAT)
boton_borde_cresta = tk.Button(ventana, text="Borde en cresta", relief=tk.RIDGE)
boton_borde_surco = tk.Button(ventana, text="Borde con surco central", relief=tk.GROOVE)
boton_borde_solido = tk.Button(ventana, text="Borde solido", relief=tk.SOLID)

# Relleno
boton_relleno_horizontal = tk.Button(ventana, text="Relleno horizontal", padx=20)
boton_relleno_vertical = tk.Button(ventana, text="Relleno vertical", pady=20)

# Insertar imagen a un botón
imagen = tk.PhotoImage(file=".\\..\\logo\\small_man.png")
imagen_boton = tk.Button(ventana, image=imagen)

##########################################################################################

boton_texto.pack()
boton_ejecutar.pack()
boton_ancho.pack()
boton_altura.pack()

boton_estado_activo.pack()
boton_estado_normal.pack()
boton_estado_desactivado.pack()

boton_color_fondo.pack()
boton_color_texto.pack()
boton_fuente_texto.pack()

ancho_borde_boton.pack()
boton_borde_levantado.pack()
boton_borde_hundido.pack()
boton_borde_plano.pack()
boton_borde_cresta.pack()
boton_borde_surco.pack()
boton_borde_solido.pack()

boton_relleno_horizontal.pack()
boton_relleno_vertical.pack()

imagen_boton.pack()

ventana.mainloop()
