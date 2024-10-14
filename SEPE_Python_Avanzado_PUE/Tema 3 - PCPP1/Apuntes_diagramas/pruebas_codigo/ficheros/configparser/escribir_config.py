import configparser as config

configuracion = config.ConfigParser()

configuracion['DEFAULT'] = {"user": "guest", "pass": ""}
configuracion['USER'] = {"user": "Alex", "pass": "1234567"}
configuracion['ROOT'] = {"user": "root", "pass": "vG54Xf5R·v 4J/f e6(wG fe!46F$vf45"}  # NO ADMITE el caracter %

with open("config.ini", "w", encoding="utf-8") as file_conf:
    configuracion.write(file_conf)
