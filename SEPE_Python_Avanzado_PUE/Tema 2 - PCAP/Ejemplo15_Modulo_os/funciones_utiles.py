import os

#funciones con el sistema operativo y maquina

#print(os.uname())
print(os.name)

# Eliminar el directorio
os.rmdir('mi_carpeta')

#crear directorio
os.mkdir('mi_carpeta')
print(os.listdir())

# Borrar directorios con subdirectorios
#os.removedirs('dir1/dir2/dir3')

#crear directorios con subdirectorios
os.makedirs("dir1/dir2/dir3") #FileExistsError: [WinError 183] No se puede crear un archivo que ya existe: 'dir1/dir2/dir3'

# Movernos entre directorios
os.chdir('dir1/dir2')

#En que directorio estoy?
print('Estoy en:', os.getcwd())

# Ejecutar con la funcion System
#os.system('mkdir otro_directorio')

# Mostrar la fecha y la hora del sistema
print(os.system('date')) # Tue Apr 16 12:10:43 CEST 2024

os.chdir('../../') #pongo el curso dos carpetas por encima de donde estoy, para borrarno puedo tener el cursor donde voy a borrar
print('Estoy en', os.getcwd())
#shutil.rmtree('dir1') # borra los directorios vacios o no desde dir1