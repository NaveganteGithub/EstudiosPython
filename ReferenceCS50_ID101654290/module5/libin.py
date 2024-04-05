import sys

from sayings import hello # Para evitar que la funcion hello colisione con la importacion de sys

if len(sys.argv) == 2:
    hello(sys.argv[1])