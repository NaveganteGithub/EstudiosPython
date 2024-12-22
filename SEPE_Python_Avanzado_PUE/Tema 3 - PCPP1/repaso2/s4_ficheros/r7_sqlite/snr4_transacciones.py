import sqlite3 as db

sobreescribir = False

conexion = db.connect("mi_base_datos.db")

conexion.execute("DELETE FROM Clientes")

if sobreescribir:
    conexion.commit()    # Confirmar operaciones
else:
    conexion.rollback()  # Revertir operaciones

conexion.close()
