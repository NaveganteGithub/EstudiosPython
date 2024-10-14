import sqlite3 as db
import tkinter as tk
from PIL import Image, ImageTk

# Crear la BBDD
# Abrir una conexion, si no existe la creara

conexion = db.connect("archivos.db")
# conexion = db.connect("tienda.sqlite")

# Obtener un cursor
cursor = conexion.cursor()

# Crear la tabla
cursor.execute("CREATE TABLE IF NOT EXISTS IMAGENES (codigo INTEGER PRIMARY KEY, imagen BLOB)")

# Insertar imagen
with open('hacker.jpg', "rb") as file:
    image_data = file.read()
    cursor.execute("INSERT INTO IMAGENES values (?,?)", (1, image_data))

# Realizar commit para guardar lo que hay en memoria a la base de datos
conexion.commit()
# conexion.rollback() # Borrar los cambios en memoria

# Consultar imagen
cursor.execute("SELECT imagen from imagenes where codigo = 1")
data = cursor.fetchone()[0]
print(data)

"""with open("hack.jpg", # Nombre de la nueva imagen
          "wb") as new_image:
    new_image.write(data)"""

with open('hack.jpg', 'wb') as file:
    ventana = tk.Tk()
    ventana.title("Prueba")
    ventana.geometry("580x810")
    ventana.resizable(False, False)

    file.write(data)
    image = Image.open('hack.jpg')
    bgImg = ImageTk.PhotoImage(image)

    label1 = tk.Label(ventana, image=bgImg, height=810, width=580)
    label1.place(x=0, y=0)

    ventana.mainloop()

# Cerrar la conexion
conexion.close()