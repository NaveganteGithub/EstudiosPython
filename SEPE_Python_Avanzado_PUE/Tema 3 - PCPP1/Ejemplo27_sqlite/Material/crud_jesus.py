import tkinter as tk
import sqlite3
from PIL import Image, ImageTk



ventana = tk.Tk()
ventana.title("Prueba")
ventana.geometry("580x810")
ventana.resizable(False, False)
    
# Connect to an sqlite database
conn = sqlite3.connect('my.db')
cursor = conn.cursor()

# Create the documents table
cursor.execute('''CREATE TABLE IF NOT EXISTS documents(
                    id INTEGER PRIMARY KEY,
                    title VARCHAR(255) NOT NULL,
                    data BLOB NOT NULL
                );''')

# Insert binary data
with open('imagen1.jpg', 'rb') as file:
    image_data = file.read()
    cursor.execute("INSERT INTO documents (title, data) VALUES (?,?)", ('JPG Image',image_data,))

# Retrieve binary data
cursor.execute("SELECT data FROM documents WHERE id = 1")
data = cursor.fetchone()[0]


with open('stored_image.jpg', 'wb') as file:
    file.write(data)
    image = Image.open('stored_image.jpg')
    bgImg = ImageTk.PhotoImage(image)
    label1 = tk.Label(ventana, image = bgImg, height=200, width=200) 
    label1.place(x = 0, y = 0) 


# Commit changes and close the database connection
conn.commit()
conn.close()
ventana.mainloop()
