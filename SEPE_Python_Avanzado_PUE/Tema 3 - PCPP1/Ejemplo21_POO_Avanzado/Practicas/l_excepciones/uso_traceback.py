
try:
    print(7/0)
except ZeroDivisionError as excepcion:
    traza = excepcion.__traceback__
    print(traza)
    print(traza.tb_next)
    print(traza.tb_frame)
    print(traza.tb_lasti)