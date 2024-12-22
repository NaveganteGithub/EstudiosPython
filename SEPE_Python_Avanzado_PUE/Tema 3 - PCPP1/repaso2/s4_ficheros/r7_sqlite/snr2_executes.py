import sqlite3 as db

conexion = db.connect("mi_base_datos.db")

conexion.execute("insert into Clientes values ('juan0@example.com', 'Juan', 627000000)")

clientes = [
    ('maria1@mail.com', 'María', 671000001),
    ('pedro2@test.com', 'Pedro', 682000002),
    ('ana3@example.com', 'Ana', 693000003),
    ('luis4@mail.com', 'Luis', 674000004),
    ('elena5@test.com', 'Elena', 685000005),
    ('carlos6@example.com', 'Carlos', 696000006),
    ('laura7@mail.com', 'Laura', 677000007),
    ('miguel8@test.com', 'Miguel', 688000008),
    ('sofia9@example.com', 'Sofía', 669000009),
    ('alberto10@example.com', 'Alberto', 600000010),
    ('beatriz11@mail.com', 'Beatriz', 611000011),
    ('cristina12@test.com', 'Cristina', 622000012),
    ('daniel13@example.com', 'Daniel', 633000013)
]

conexion.executemany("insert into Clientes values (?,?,?)", clientes)


insercciones = ("insert into Clientes values ('eva14@mail.com', 'Eva', 644000014);"
                "insert into Clientes values ('fernando15@test.com', 'Fernando', 655000015);"
                "insert into Clientes values ('gloria16@example.com', 'Gloria', 666000016);"
                "insert into Clientes values ('hector17@mail.com', 'Héctor', 677000017);"
                "insert into Clientes values ('isabel18@test.com', 'Isabel', 688000018);"
                "insert into Clientes values ('javier19@example.com', 'Javier', 619000019);"
                "insert into Clientes values ('jesus49@example.com', 'Jesus', 972000011);")

conexion.executescript(insercciones)

conexion.commit()

conexion.close()
