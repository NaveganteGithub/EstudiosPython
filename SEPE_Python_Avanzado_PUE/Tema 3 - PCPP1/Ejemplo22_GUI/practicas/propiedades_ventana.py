import tkinter as tk


ventana = tk.Tk()

ventana.title("Ejemplo de propiedades")
# Podemos posicionar la ventana entre las pantallas
# ventana.geometry('400x600+-200+200')
# ventana.geometry('400x600+1900+200')
ventana.geometry('400x600+500+200')
ventana.config(background="yellow", padx=15, pady=15)

ventana.tk.call("wm", "iconphoto", ventana, tk.PhotoImage(file='logo/man.png'))

# ventana.minsize(width="500", height="300")
# ventana.maxsize(width="1280", height="720")
ventana.minsize(width=500, height=300)  # Permite declarar el tamaño minimo de la ventana
ventana.maxsize(width=1280, height=720)  # Permite declarar el tamaño maximo de la ventana

ventana.resizable(width=False, height=False)  # Permite declarar si altura o anchura de la ventana es redimensionable

# Boton de prueba
boton = tk.Button(ventana, text="Prueba", width=50, height=10)
boton.place(x=0, y=0)

# ventana.overrideredirect(True) # Elimina la barra de titulo de la ventana

ventana.mainloop()
