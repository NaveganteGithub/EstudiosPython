######################### IMPORTACIONES #########################

"""
No hace falta descargar las librerias manualmente ya lo hace el 
script de manera automatica
"""

# Aqui pondriamos la librerias nativas de la API de Python
import tkinter, os, sys, subprocess

depuracion = False # Cambiar el valor de la variable para activar (True) o desactivar (False) los mensajes del script
dependencias_cumplidas = False 
salida = None
errores = None

while not dependencias_cumplidas:
    try:
        # Aqui pondriamos las librerias externas o no nativas de la API
        # descargadas de repositorios
        import openpyxl as excel
        dependencias_cumplidas = True
    except ModuleNotFoundError as module:
        libreria = str(module).split("'")[1]
        print(f"Falta la libreria {libreria}, instalando...")
        if not depuracion:
            salida = subprocess.DEVNULL
            errores = subprocess.DEVNULL
        
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", libreria], stdout=salida, stderr=errores)
        except:
            print("Verifica que tienes las librerias instaladas")
            print("Verifica que tienes una buena conexion a internet para descargar las librerias")
            exit(0)

######################### FUNCIONES ######################### 
def ubicarme() -> None:
    ruta_absoluta = os.path.abspath(__file__)
    last_delimiter = ruta_absoluta.rfind("\\")
    directorio_actual = ruta_absoluta[:last_delimiter + 1]
    os.chdir(directorio_actual)

######################### CODIGO FUENTE #########################
ubicarme()

# Abrir hoja de calculo con open, este metodo devolvera un objeto Workbook, lo necesitaremos
hoja_calculo = excel.open("Ejemplo.xlsx")
# Como necesitamos un objeto de tipo WorkbookChild, guardaremos el atributo activate
apetura = hoja_calculo.active

# Listar hojas (cada hoja tiene una tabla) y columnas de tablas
nombres_hojas = hoja_calculo.sheetnames # Devolvera una lista con todas las hojas de calculo del archivo
hojas = dict()

for hoja in nombres_hojas:
    # print(hoja)
    hojas[hoja] = [columnas[0].value for columnas in apetura.iter_cols()]

# print(hojas)

# Listar Celdas
    
tabla = list()

for hoja in hojas.items():
    if hoja:
        # print(hoja)
        for columna in range(len(hoja[1])):
            tabla.append(
                [cell.value for cell in apetura[chr(65 + columna)] if isinstance(cell.value, (int, float, str))][1:]
                )

# print(tabla)

for row in range(len(tabla[0])):
    for column in range(len(tabla)):
        print(tabla[column][row], end=":::::")
    print()

