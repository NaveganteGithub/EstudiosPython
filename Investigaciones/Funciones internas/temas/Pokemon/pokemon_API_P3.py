import sqlite3 as db
import re

bd = "Librerias\\SRC\\Pokemon\\Extracion_Pokemon.sqlite"
datos = None

def abrir_bd(ruta: str):
    conexion = db.connect(bd)
    return (conexion, conexion.cursor())
    
def cerrar_bd(conn: db.Connection, cursor: db.Cursor):
    cursor.close()
    conn.close()

def guardar(conexion: db.Connection):
    conexion.commit()

try:
    mi_conexion, mi_cursor = abrir_bd(bd)
    
    mi_cursor.execute("select Movimiento.Nombre, Movimiento.Poder_drenaje from Movimiento")
    datos = mi_cursor.fetchall()
    
    # print(datos)
    cerrar_bd(mi_conexion, mi_cursor)

except db.OperationalError:
    print("Operacion Erronea")

try:
    
    mi_conexion, mi_cursor = abrir_bd(bd)

    for dato in datos:
        movimiento = dato[0]
        drenaje = dato[1]
        
        if drenaje is None or \
            not re.match("[-]*[0-9]+", drenaje) or \
                drenaje == "0":
            continue
        
        drenaje = int(drenaje)

        columna = None
        if drenaje < 0:
            columna = "Porcentaje_Daño"
        elif drenaje > 0:
            columna = "Porcentaje_Curación"
        actualizacion = f"UPDATE Movimiento set {columna} = ? where Nombre = ?"
        mi_cursor.execute(actualizacion, (str(abs(drenaje)), movimiento))
        
        # print(movimiento, drenaje)
        """if drenaje in [0, None]:
            continue
        elif drenaje < 0:
            pass
        elif drenaje > 0:
            pass"""
    
    guardar(mi_conexion)
    cerrar_bd(mi_conexion, mi_cursor)

except db.OperationalError:
    print("Error al actualizar")