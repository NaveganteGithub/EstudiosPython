import sys

try:
    print(7/0)
except ZeroDivisionError as excepcion:
    nomb, desc, traza = sys.exc_info()
    print(nomb, desc, traza, sep="\n")