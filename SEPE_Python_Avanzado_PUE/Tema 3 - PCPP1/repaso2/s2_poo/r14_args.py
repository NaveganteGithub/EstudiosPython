
def lista_parametro(*args):
    for data in args:
        print(data)

def diccionario_parametro(**kwargs):
    for clave, valor in kwargs.items():
        print(clave, "tiene el valor", valor)


lista_parametro(1,2,3,4,5,6,7)
diccionario_parametro(
    nombre="David",sueldo=12345,email="davi02@mail.com",
    telefono=555214510,red_social="Telegram",empresa="ADDD",genero="hombre")
