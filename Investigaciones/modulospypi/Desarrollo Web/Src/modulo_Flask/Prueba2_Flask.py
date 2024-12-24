from flask import *

# flask es una libreria de Python que te permite ejecutar codigo Python desde el navegador
# flask detecta cambios de manera automatica cada vez que guardas el fichero

app = Flask(__name__)

# Aqui hacemos una funcion que se llamara con una peticion a la raiz del directorio web
# http://localhost:5000/
@app.route("/")
def saludo():
    return "Hola"

# http://localhost:5000/gobierno
@app.route("/gobierno")
def gobierno() -> str:
    return "España"

# Si quisieramos usar una funcion con un parametro solo tenemos que declarar la funcion
# en app.route de esta manera de esta manera /directorio/<nombre_parametro>
@app.route("/gobiernoextranjero/<gobierno>")
def gobierno_extranjero(gobierno: str) -> str:
    return gobierno

# Si quisieramos usar una funcion con mas de un parametro, 
# tendriamos que poner el nombre de todos los parametros 
# de la funcion despues de espeficicar el directorio entre
# parentesis y signos de menos y mayor de la siguiente manera
@app.route("/dato/<a>/<b>")
def calculo(a: int, b: int) -> int:
    resultado = int(a) + int(b)
    return str(resultado) # Ten en cuenta que flask solo trabaja con cadenas de texto


@app.route("/datoHTML/<a>/<b>")
def calculo_HTML(a: int, b: int) -> int:
    resultado = int(a) + int(b)
    return "<h2>" + str(resultado) + "</h2>" # Podemos gestionar de manera dinamica el HTML, CSS, Javascript...

if __name__ == "__main__":
    app.run(debug=True)

    # http://localhost:5000/gobiernoextranjero/<parametro>
        # http://localhost:5000/gobiernoextranjero/Israel
    # http://localhost:5000/dato/<parametro_a>/<parametro_b>
        # http://localhost:5000/dato/5/2
    # http://localhost:5000/datoHTML/<parametro_a>/<parametro_b>
        # http://localhost:5000/datoHTML/5/2