import configparser as config

configuracion = config.ConfigParser()

configuracion.read("config.ini", "utf-8")

print(configuracion["DEFAULT"]["USER"])
print(configuracion["ROOT"]["PASS"])
