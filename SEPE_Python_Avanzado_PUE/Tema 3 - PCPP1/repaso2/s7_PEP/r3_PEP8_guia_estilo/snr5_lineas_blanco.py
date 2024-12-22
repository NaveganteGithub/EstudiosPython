# Hay que utilizar los espacios en blanco según el caso

## Tenemos que usar dos líneas en blanco para separar clases y funciones

class Persona:
    pass


class Animal:
    pass


def altura():
    pass


## Tenemos que usar una línea para separar métodos de una clase o para dividir una función en secciones lógicas

class Empresa:

    def informacion_fiscal(self):
        return None

    def cartera_clientes(self):
        return None


def es_cuadrado_matematico(matriz: list[list]): # o Cuadrado magico

    longitud_columna = len(matriz)  # Análisis de matriz cuadrada
    longitud_fila = None
    for fila in matriz:
        if len(fila) != longitud_columna:
            return False
    else:
        longitud_fila = len(matriz[0])
    es_matriz_cuadrada = longitud_fila == longitud_columna

    if not es_matriz_cuadrada:  # En caso negativo
        return False

    if es_matriz_cuadrada:  # En caso positivo
        resultado_fila_inicial = sum(matriz[0])  # Sumas de filas
        for fila in matriz:
            resultado_fila_actual = sum(fila)
            if resultado_fila_actual != resultado_fila_inicial:
                return False

        columna_actual = list()  # Composición de columnas
        resultados_columnas = list()
        for posicion_columna in range(longitud_fila):
            for fila in matriz:
                columna_actual.append(fila[posicion_columna])
            resultados_columnas.append(sum(columna_actual))
            columna_actual.clear()

        else:  # Sumas de columnas
            muestra_columna_anterior = resultados_columnas[0]
            for resultado_columna in resultados_columnas:
                muestra_columna_actual = resultado_columna
                if muestra_columna_actual != muestra_columna_anterior:
                    return False
                else:
                    muestra_columna_anterior = muestra_columna_actual

        return True

