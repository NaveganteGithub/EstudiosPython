import tkinter as tk

def on_key_press(event):
    print(f"Tecla presionada: {event.keysym}")
    print(f"Tecla presionada: {event.char}")
    texto_actual = texto.get()
    texto.set(texto_actual + event.char)

# Crear la ventana principal
root = tk.Tk()
root.title("Eventos de Teclas en un Label")

# Texto dinámico
texto = tk.StringVar()

# Crear un frame
etiqueta = tk.Label(root, width=50, height=5, bg="lightgrey", textvariable=texto)
etiqueta.pack(padx=10, pady=10)

# Asegurarse de que el frame pueda recibir el foco de entrada
etiqueta.focus_set()

# Vincular el evento de tecla al frame
etiqueta.bind("<Key>", on_key_press)

# Iniciar el bucle principal de la ventana
root.mainloop()
