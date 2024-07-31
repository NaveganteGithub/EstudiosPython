import configparser

# Obtener el objeto config
config = configparser.ConfigParser()

# Leer el archivo
config.read(filenames="config.ini")

print(config['mariadb']['host'])  # mostrar dato del fichero
print(config.sections())  # mostrar secciones

print(config['mariadb']['host'])
print(config['mariadb']['port'])
print(config['mariadb']['user'])
print(config['mariadb']['password'])
print(config['mariadb']['database'])

print("-" * 20)

for dato in config['mariadb']:
    print(dato, config['mariadb'][dato])
