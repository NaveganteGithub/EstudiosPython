import sqlite3 as db

conexion = db.connect('.\\mi_bd.db')

conexion.executescript("""
CREATE TABLE IF NOT EXISTS Empleados (
    id integer primary key,
    nombre text,
    salario real
);

CREATE TABLE IF NOT EXISTS Hijos_Empleados (
    nombre text,
    empleado integer,
    foreign key (empleado) references Empleados(id)
);
""")

conexion.commit()

conexion.close()
