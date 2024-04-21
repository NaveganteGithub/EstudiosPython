"""
Entendido, gracias por la aclaración. Ahora profundizaré en la **librería CSV de Python** y su relación con la **clase `csv.excel`**:

1. **Librería CSV en Python**:
   - El módulo `csv` en Python implementa clases para leer y escribir datos tabulares en formato **CSV** (Valores Separados por Comas).
   - Permite a los programadores manipular archivos CSV sin preocuparse por los detalles precisos del formato utilizado por aplicaciones como Excel.
   - Algunos puntos clave:
     - Puedes leer y escribir datos en forma de **secuencias** utilizando los objetos `reader` y `writer`.
     - También puedes trabajar con datos en forma de **diccionario** utilizando las clases `DictReader` y `DictWriter`.
     - El módulo `csv` oculta los detalles de lectura y escritura de datos, lo que facilita su uso.
     - Aunque los delimitadores y separadores pueden variar, el formato general es lo suficientemente similar para que un solo módulo pueda manejarlo eficientemente.
     - Puedes especificar un **dialecto** (conjunto de parámetros específicos) al leer o escribir archivos CSV.
     - Ejemplo de uso básico:
       ```python
       import csv
       with open('datos.csv', newline='') as csvfile:
           reader = csv.reader(csvfile, delimiter=',', quotechar='"')
           for row in reader:
               print(', '.join(row))
       ```
   - Puedes encontrar más detalles en la [documentación oficial del módulo CSV en Python](https://docs.python.org/es/3/library/csv.html) ¹.

2. **Clase `csv.excel`**:
   - La clase `csv.excel` es parte del módulo `csv` en Python.
   - Define un dialecto específico para archivos CSV que sigue las convenciones utilizadas por Excel.
   - Algunas características de este dialecto:
     - Utiliza la coma (`,`) como delimitador.
     - Usa las comillas dobles (`"`) como carácter de escape para campos que contienen caracteres especiales (como comas o saltos de línea).
     - Por defecto, no realiza conversión automática de tipo de datos.
     - Puedes personalizarlo según tus necesidades.
   - Al leer o escribir archivos CSV con este dialecto, estarás siguiendo las convenciones de Excel.

3. **Dato adicional**:
   - A veces, los archivos CSV generados por diferentes aplicaciones pueden tener pequeñas diferencias debido a la falta de un estándar bien definido.
   - Es importante estar al tanto de estas diferencias al procesar archivos CSV desde múltiples fuentes.

Espero que esta información sea útil. Si tienes más preguntas o necesitas más detalles, no dudes en preguntar. 😊

Origen: Conversación con Bing, 4/2/2024
(1) csv — Lectura y escritura de archivos CSV — documentación de Python - 3 .... https://docs.python.org/es/3/library/csv.html.
(2) 11 bibliotecas Python de Excel útiles para la gestión de datos. https://geekflare.com/es/excel-python-libraries/.
(3) pandas.read_excel — pandas 2.2.0 documentation. https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html.

"""

import os
import csv

# 1º Obten la ruta relativa y la ruta absoluta de este archivo de python 

ruta_relativa = os.path.realpath(__file__) # Ruta relativa
ruta_absoluta = os.path.abspath(__file__) # Ruta absoluta
ruta_absoluta_por_variable = __file__
ruta_absoluta_csv = os.path.abspath("datos.csv")
ruta_relativa_csv = os.path.realpath("datos.csv")
print(ruta_relativa, ruta_absoluta, ruta_absoluta_csv, ruta_absoluta_csv, ruta_relativa_csv, sep="\n") 

# Podemos depurar un poco la ruta quitando el archivo final y dejando solo la ruta
# rfind sirve para buscar caracteres empezando por la derecha de cadena (right find)
last_delimiter = ruta_absoluta.rfind("\\")
print(last_delimiter)
directorio_actual = ruta_absoluta[:last_delimiter + 1]
print(directorio_actual)

# La diferencia entre realpath y getcwd es que getcwd me da el directorio actual
# en donde el script trabaja en la terminal y realpath me ofrece la ubicacion del
# archivo de forma relativa.
directorio_actual_en_terminal = os.getcwd()
print(directorio_actual_en_terminal)

# 2º Cambia al directorio de trabajo del script de python

os.chdir(directorio_actual)

# 3º Lee el archivo datos.csv

# newline permite especificar como se manejan los saltos de lineas en el sistema operativo,
# Windows por defecto usa '\r\n' como salto de linea, Linux y MacOS utilizan '\n', y newline=''
# especifica que dependiendo del sistema operativo aplique un salto de linea u otro
with open('datos.csv', newline='') as csvfile:
   # delimiter sirve para indicar los separadores que separan cada campo
   # quotechar sirve para eliminar los caracteres especiales que rodean a los campos
   spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
   for row in spamreader:
      # print(','.join(row), sep="")
      print(row, sep="")

with open('datos.csv', newline='') as csvfile:
   reader = csv.reader(csvfile, delimiter=',')
   for row in reader:
      # print(','.join(row), sep="")
      print(row, sep="")