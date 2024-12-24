"""
flask es una libreria que te permite crear un servidor web
en el que puedes ejecutar python.
"""

from flask import *

app = Flask(__name__)

@app.route("/")
def main():
    return "Hola"

if __name__ == "__main__":
    app.run(debug=True)

# Despues de ejecutar Flask ve a la direccion http://localhost:5000/