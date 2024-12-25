import pandas as pd

def analisis_cotizacion():
    return pd.DataFrame(
            pd.read_csv('Tarea2\\cotizacion.csv', sep=';'),
            columns=['Final', 'Máximo', 'Mínimo']
        )

print(analisis_cotizacion())