from tokenize import tokenize, untokenize

# A partir de un lenguaje podemos crear lenguajes personalizados, con
# C se creo Python, y con Python podemos crear nuestro lenguaje.
# https://www.youtube.com/watch?v=6LiKozema58

def ejecucion(archivo_python: str):
    palabras_clave_personalizadas = {
        # 'Alias':  'Palabra python'
        'check': 'if',
        'decline': 'else',
        'each': 'for',
        'numbers': 'range',
        'say': 'print',
        'ALIVE': 'True',
        'DEAD': 'False'
    }

    with open(archivo_python, 'rb') as src:
        tokens = []

        for token in tokenize(src.readline):
            if token.string in palabras_clave_personalizadas:
                t = (token.type, palabras_clave_personalizadas[token.string])
            else:
                t = (token.type, token.string)

            tokens.append(t)


    code = untokenize(tokens).decode('utf-8')
    exec(code)


if __name__ == "__main__":
    ejecucion(archivo_python='mi_test.af')