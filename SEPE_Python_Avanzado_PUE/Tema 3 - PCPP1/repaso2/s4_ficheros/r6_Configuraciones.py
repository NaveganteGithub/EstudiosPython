import configparser

config = configparser.ConfigParser()

config['default'] = {"User": "preparatoria", "Pass": "asd1w2·"}
# En el campo Pass habia un % antes del segundo 5, pero daba
# un ValueError por lo que tuve que quitarlo
config['admin'] = {"User": "administrator", "Pass": "54f·g $d 56g -.4e6-4  g+5- e41 w6 g4"}

with open("./archivo.ini", "wt", encoding="utf-8") as archivo:
    config.write(archivo)

