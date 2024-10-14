import os

# print(os.uname()) # Solo funciona con el WLS (Windows Linux Subsystem) activado
print(os.name)
os.rmdir("mi_carpeta")
os.mkdir("mi_carpeta")
print(os.listdir())
os.removedirs("dir1\\dir2\\dir3")
os.makedirs("dir1\\dir2\\dir3")

print("Estoy en", os.getcwd())

# os.system("mkdir otro_directorio")

# print(os.system("date"))