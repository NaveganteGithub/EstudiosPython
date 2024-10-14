import configparser

config = configparser.ConfigParser()

config['default'] = {"User": "anonimous", "Pass": ""}

with open("registro.ini", "w") as fichero:
    config.write(fichero)
