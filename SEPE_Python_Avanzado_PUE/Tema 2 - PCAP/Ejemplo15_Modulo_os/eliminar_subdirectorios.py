import os
from pathlib import Path

os.makedirs ("mi_carpeta/prueba1/prueba2/prueba3")
os.makedirs ("mi_carpeta/prueba1/prueba2/prueba4")
print(os.listdir())

def borrar_directorio_recursivo(ruta):
    for elemento in ruta.iterdir():
        if elemento.is_dir():
            borrar_directorio_recursivo(elemento)
        else:
            elemento.unlink()
    ruta.rmdir()

directorio_a_borrar = Path("mi_carpeta")
borrar_directorio_recursivo(directorio_a_borrar)