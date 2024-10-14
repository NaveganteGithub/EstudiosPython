import configparser

# Obtener el objeto config
config = configparser.ConfigParser()

# Crear la configuracion (ejemplo, los accesos a las bases de datos)
config['DEFAULT'] = {'host': 'localhost'}
config['sqlite'] = {'host': 'localhost',
                   'database': 'tienda.db'
                   }
config['mysql'] = {'host': 'localhost',
                   'user': 'root',
                   'password': "",
                   "database": "cetelem"
                   }
config['mariadb'] = {
    #"host": "msi.h.filess.io",
    "host": "localhost",
    "port": 3305,
    "user": "Lab_freedomill",
    "password": "217050b98031c1ee067173e1f38c58727b47623c",
    "database": "Lab_freedomill"
}

# Escribir esa configuracion en un fichero "config.ini"
with open("config.ini", "w") as archivo_configuracion:
    config.write(archivo_configuracion)
