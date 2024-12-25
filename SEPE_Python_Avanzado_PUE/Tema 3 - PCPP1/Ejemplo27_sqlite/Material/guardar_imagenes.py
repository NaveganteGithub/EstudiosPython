import tkinter as tk
import sqlite3
from PIL import Image, ImageTk

ventana = tk.Tk()
ventana.title("Prueba")
ventana.geometry("580x810")
ventana.resizable(False, False)

# Crear la BBDD
# Abrir una conexion, si no existe la creara
conexion = sqlite3.connect("imagenes.db")

# Obtener un cursor
cursor = conexion.cursor()

# crear la tabla
cursor.execute("CREATE TABLE IF NOT EXISTS IMAGENES (codigo INTEGER PRIMARY KEY, imagen BLOB)")

# guardar la imagen
with open('imagen1.jpg', 'rb') as file:
    image_data = file.read()
    #cursor.execute("INSERT INTO IMAGENES  VALUES (?,?)", (2, image_data))

# IMPORTANTE EL COMMIT
conexion.commit()

# recuperar la imagen
cursor.execute("SELECT imagen FROM IMAGENES WHERE codigo = 2")
data = cursor.fetchone()[0]

with open('stored_image.jpg', 'wb') as file:
    file.write(data)
    image = Image.open('stored_image.jpg')
    bgImg = ImageTk.PhotoImage(image)

    label1 = tk.Label(ventana, image = bgImg, height=200, width=200)
    label1.place(x = 0, y = 0)


# cerrar la conexion
conexion.close()

ventana.mainloop()