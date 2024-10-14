import configparser

# Obtener el objeto config
config = configparser.ConfigParser()

# Crear la configuracion (accesos a las BBDD)
config['DEFAULT'] = {'host':'localhost'}
config['sqlite'] = {'host':'localhost',
                    'database':"tienda.db"}
config['mysql'] = {'host':"localhost",
                    'user':"root",
                    'password':"",
                    'database':"cetelem"}
config['mariadb'] = {'host': 'msi.h.filess.io',
                     'port':'3305',
                     'user':'Lab_freedomill',
                     'password':'217050b98031c1ee067173e1f38c58727b47623c',
                     'database':'Lab_freedomill'}


# Escribir esa configuracion en un fichero "config.ini"
with open('config.ini', 'w') as configfile:
    config.write(configfile)