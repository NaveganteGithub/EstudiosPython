import configparser

# Obtener el objeto config
config = configparser.ConfigParser()

# Leer el archivo
config.read(filenames="config.ini")

print(config['mariadb']['host'])  # Mostrar dato del fichero, la seccion DEFAULT no se muestra
print(config.sections())  # Mostrara las secciones del fichero .ini leido

print(config['mariadb']['host'])
print(config['mariadb']['port'])
print(config['mariadb']['user'])
print(config['mariadb']['password'])
print(config['mariadb']['database'])

print("-" * 20)

for dato in config['mariadb']:
    print(dato, config['mariadb'][dato])

print("-" * 20)

print(config['DEFAULT']['host'])
