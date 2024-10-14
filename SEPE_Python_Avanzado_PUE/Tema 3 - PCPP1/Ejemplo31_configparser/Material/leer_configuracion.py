import configparser

# Obtener el objeto config
config = configparser.ConfigParser()

# leer el archivo
config.read(filenames="config.ini")

# mostrar secciones
print(config.sections())  # ['sqlite', 'mysql', 'mariadb']

# mostrar los datos de mariadb
print(config['mariadb']['host'])
print(config['mariadb']['port'])
print(config['mariadb']['user'])
print(config['mariadb']['password'])
print(config['mariadb']['database'])
