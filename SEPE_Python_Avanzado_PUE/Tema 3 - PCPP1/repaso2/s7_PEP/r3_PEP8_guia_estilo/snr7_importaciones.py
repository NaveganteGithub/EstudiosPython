# Las importaciones tienen que seguir unas reglas

#     Regla 1: Las importaciones tienen que seguir un orden:
#       1 Librerias estándar: librerias de la api de python
#       2 Librerias de terceros: librerias descargadas
#       3 Librerias propias: librerias creadas por ti

import os
import paprika
import libreria_ejemplo

#     Regla 2: los imports tienen que estar en líneas separadas

import math
import sys
import json
import csv
import requests

#     Regla 3: Las importaciones de librerias tienen que utilizar rutas absolutas

import EstudiosdeIA.cliente_ChatGPT

#     Regla 4: Con los from import podemos usar importaciones multiples

from subprocess import Popen, PIPE

#     Regla 5: Los from import con comodín están PROHIBIDOS

from libreria_ejemplo import *
